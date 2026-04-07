"""GRPO (Group Relative Policy Optimization) training on reliability engineering.

Two-stage per fold:
  1. SFT with v2 config (LoRA on base model)
  2. GRPO on the SFT model using ground truth as reward signal

GRPO generates multiple responses per question, scores them against ground truth,
and optimizes the model to prefer correct reasoning chains.
"""

import json
import os
import re
import sys
import time
from functools import partial
from pathlib import Path

# Disable torch.compile to avoid Triton crash in older containers
os.environ["TORCHDYNAMO_DISABLE"] = "1"

import torch
from unsloth import FastLanguageModel
from trl import SFTTrainer, SFTConfig, GRPOTrainer, GRPOConfig
from datasets import Dataset

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.data_io import load_dataset
from training.config import (
    MODEL_NAME, MODEL_TAG, MAX_SEQ_LENGTH, N_FOLDS,
    CV_SPLITS_DIR, ADAPTERS_DIR, LORA_CONFIG, TRAIN_CONFIG,
    SYSTEM_PROMPT,
)

# GRPO needs a larger sequence buffer than SFT because it generates
# completions during training. prompt (~500 tokens) + completion (~2048)
GRPO_MAX_SEQ_LENGTH = 4096
GRPO_MAX_COMPLETION = 2048


# ---------------------------------------------------------------------------
# Answer comparison (same as evaluate scripts)
# ---------------------------------------------------------------------------
def normalize_answer(answer: str) -> str:
    answer = answer.lower().strip()
    answer = re.sub(r'\$\\boxed\{(.*?)\}\$', r'\1', answer)
    answer = re.sub(r'\\boxed\{(.*?)\}', r'\1', answer)
    answer = re.sub(r'\$(.*?)\$', r'\1', answer)
    answer = re.sub(r'\\frac\{(\d+)\}\{(\d+)\}', r'\1/\2', answer)
    answer = answer.replace(" ", "")
    answer = re.sub(r'(\d),(\d)', r'\1\2', answer)
    answer = answer.replace("\u00d7", "x")
    answer = answer.replace("^", "**")
    return answer


def _eval_fraction(s: str):
    m = re.match(r'^(-?\d+)/(\d+)$', s.strip())
    if m:
        num, den = int(m.group(1)), int(m.group(2))
        if den != 0:
            return num / den
    return None


def is_correct(predicted: str, ground_truth: str, tolerance: float = 0.05) -> bool:
    pred_norm = normalize_answer(predicted)
    truth_norm = normalize_answer(ground_truth)
    if pred_norm == truth_norm:
        return True
    pred_frac = _eval_fraction(pred_norm)
    truth_frac = _eval_fraction(truth_norm)
    pred_clean = re.sub(r'(\d+\.?\d*)%', lambda m: str(float(m.group(1))/100), predicted)
    truth_clean = re.sub(r'(\d+\.?\d*)%', lambda m: str(float(m.group(1))/100), ground_truth)
    pred_numbers = re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", pred_clean)
    truth_numbers = re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", truth_clean)
    if pred_frac is not None and truth_numbers:
        try:
            truth_val = float(truth_numbers[0])
            if abs(pred_frac - truth_val) / max(abs(truth_val), 1e-10) < tolerance:
                return True
        except ValueError:
            pass
    elif truth_frac is not None and pred_numbers:
        try:
            pred_val = float(pred_numbers[0])
            if abs(pred_val - truth_frac) / max(abs(truth_frac), 1e-10) < tolerance:
                return True
        except ValueError:
            pass
    if pred_numbers and truth_numbers:
        try:
            pred_nums = [float(x) for x in pred_numbers]
            truth_nums = [float(x) for x in truth_numbers]
            if len(pred_nums) == len(truth_nums):
                if all(abs(p - t) / max(abs(t), 1e-10) < tolerance
                       for p, t in zip(pred_nums, truth_nums)):
                    return True
            elif len(truth_nums) == 1:
                if any(abs(p - truth_nums[0]) / max(abs(truth_nums[0]), 1e-10) < tolerance
                       for p in pred_nums):
                    return True
        except (ValueError, ZeroDivisionError):
            pass
    if len(truth_norm) > 3 and (truth_norm in pred_norm or pred_norm in truth_norm):
        return True
    return False


def extract_final_answer(response: str) -> str:
    patterns = [
        r"[Ff]inal\s+[Aa]nswer\s*:\s*(.*)",
        r"[Tt]he\s+answer\s+is\s*:\s*(.*)",
        r"[Tt]herefore\s*,?\s*(.*)",
    ]
    for pattern in patterns:
        match = re.search(pattern, response, re.DOTALL)
        if match:
            return match.group(1).strip()
    lines = [l.strip() for l in response.strip().split("\n") if l.strip()]
    return lines[-1] if lines else response


# ---------------------------------------------------------------------------
# SFT formatting (same as train_sft.py)
# ---------------------------------------------------------------------------
def formatting_func(examples, tokenizer):
    conversations = examples["conversations"]
    if conversations and isinstance(conversations[0], dict):
        convos = [conversations]
    else:
        convos = conversations
    results = []
    for convo in convos:
        text = tokenizer.apply_chat_template(
            convo, tokenize=False, add_generation_prompt=False,
            enable_thinking=False,
        )
        results.append(text)
    return results


# ---------------------------------------------------------------------------
# GRPO reward function
# ---------------------------------------------------------------------------
def make_reward_fn(train_data):
    """Create a reward function that checks answers against ground truth."""
    qa_lookup = {}
    for item in train_data:
        question = None
        answer = None
        for msg in item["conversations"]:
            if msg["role"] == "user":
                question = msg["content"]
            if msg["role"] == "assistant":
                answer = extract_final_answer(msg["content"])
        if question and answer:
            qa_lookup[question] = answer

    def reward_fn(completions, prompts=None, **kwargs):
        """Score each completion: 1.0 if correct, 0.0 if wrong."""
        rewards = []
        for i, completion in enumerate(completions):
            prompt_text = prompts[i] if prompts and i < len(prompts) else ""

            # Find matching ground truth
            gt_answer = None
            for q, a in qa_lookup.items():
                if q in prompt_text:
                    gt_answer = a
                    break

            if gt_answer is None:
                rewards.append(0.0)
                continue

            extracted = extract_final_answer(completion)
            rewards.append(1.0 if is_correct(extracted, gt_answer) else 0.0)

        return rewards

    return reward_fn


def main():
    ADAPTERS_DIR.mkdir(parents=True, exist_ok=True)

    for fold_idx in range(N_FOLDS):
        print(f"\n{'='*60}")
        print(f"FOLD {fold_idx} - SFT+GRPO ({MODEL_TAG})")
        print(f"{'='*60}")

        train_path = CV_SPLITS_DIR / f"fold_{fold_idx}_train.jsonl"
        train_data = load_dataset(str(train_path))
        print(f"Training samples: {len(train_data)}")

        # ==== Phase 1: SFT ====
        print(f"\n--- Phase 1: SFT ---")
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=MODEL_NAME,
            max_seq_length=MAX_SEQ_LENGTH,  # 2048 is fine for SFT
            load_in_4bit=True,
        )
        model = FastLanguageModel.get_peft_model(model, **LORA_CONFIG)
        print("LoRA applied for SFT.")

        hf_dataset = Dataset.from_list(train_data)
        fold_output_dir = ADAPTERS_DIR / f"fold_{fold_idx}"
        fold_output_dir.mkdir(parents=True, exist_ok=True)

        sft_config = SFTConfig(
            output_dir=str(fold_output_dir / "sft"),
            max_seq_length=MAX_SEQ_LENGTH,
            dataset_text_field=None,
            **TRAIN_CONFIG,
        )
        trainer = SFTTrainer(
            model=model,
            tokenizer=tokenizer,
            train_dataset=hf_dataset,
            args=sft_config,
            formatting_func=partial(formatting_func, tokenizer=tokenizer),
        )
        print("Starting SFT training...")
        sft_result = trainer.train()
        print(f"SFT complete. Loss: {sft_result.training_loss:.4f}")

        model.save_pretrained(str(fold_output_dir / "sft"))
        tokenizer.save_pretrained(str(fold_output_dir / "sft"))
        del model, tokenizer, trainer
        torch.cuda.empty_cache()

        # ==== Phase 2: Pre-screen ====
        print(f"\n--- Phase 2: Pre-screen (filter hopeless questions) ---")
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=str(fold_output_dir / "sft"),
            max_seq_length=GRPO_MAX_SEQ_LENGTH,  # 4096 for generation
            load_in_4bit=True,
        )
        FastLanguageModel.for_inference(model)

        grpo_prompts = []
        skipped = 0
        for item in train_data:
            question = None
            gt_answer = None
            for msg in item["conversations"]:
                if msg["role"] == "user":
                    question = msg["content"]
                if msg["role"] == "assistant":
                    gt_answer = extract_final_answer(msg["content"])
            if not question or not gt_answer:
                continue

            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question},
            ]
            input_ids = tokenizer.apply_chat_template(
                messages, add_generation_prompt=True, return_tensors="pt",
                enable_thinking=False,
            ).to(model.device)

            got_one_right = False
            for _ in range(2):
                with torch.no_grad():
                    out = model.generate(
                        input_ids=input_ids, max_new_tokens=1024,
                        do_sample=True, temperature=0.7, top_p=0.9,
                    )
                resp = tokenizer.decode(out[0][input_ids.shape[1]:], skip_special_tokens=True)
                if is_correct(extract_final_answer(resp), gt_answer):
                    got_one_right = True
                    break

            if got_one_right:
                prompt = tokenizer.apply_chat_template(
                    messages, tokenize=False, add_generation_prompt=True,
                    enable_thinking=False,
                )
                grpo_prompts.append({"prompt": prompt})
            else:
                skipped += 1

        del model, tokenizer
        torch.cuda.empty_cache()

        print(f"Kept {len(grpo_prompts)} prompts, skipped {skipped} hopeless questions")

        if len(grpo_prompts) < 10:
            print(f"Too few prompts for GRPO, skipping this fold.")
            continue

        # ==== Phase 3: GRPO ====
        print(f"\n--- Phase 3: GRPO ---")

        # Reload SFT model with larger buffer for GRPO generation
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=str(fold_output_dir / "sft"),
            max_seq_length=GRPO_MAX_SEQ_LENGTH,  # 4096 — critical fix
            load_in_4bit=True,
        )
        # Model already has LoRA from SFT adapter — GRPOTrainer will train it
        print(f"SFT model loaded for GRPO (max_seq_length={GRPO_MAX_SEQ_LENGTH}).")

        grpo_dataset = Dataset.from_list(grpo_prompts)

        grpo_config = GRPOConfig(
            output_dir=str(fold_output_dir),
            num_generations=4,
            max_completion_length=GRPO_MAX_COMPLETION,  # 2048 tokens for completion
            per_device_train_batch_size=4,  # must be multiple of num_generations
            gradient_accumulation_steps=4,
            num_train_epochs=1,
            learning_rate=5e-6,
            warmup_ratio=0.1,
            lr_scheduler_type="cosine",
            optim="adamw_8bit",
            bf16=True,
            logging_steps=1,
            save_strategy="no",
            report_to="none",
            seed=42,
        )

        reward_fn = make_reward_fn(train_data)

        grpo_trainer = GRPOTrainer(
            model=model,
            tokenizer=tokenizer,
            train_dataset=grpo_dataset,
            reward_funcs=reward_fn,
            args=grpo_config,
        )

        print("Starting GRPO training...")
        grpo_result = grpo_trainer.train()
        print(f"GRPO complete. Loss: {grpo_result.training_loss:.4f}")

        # Save final adapter (GRPO on top of SFT)
        model.save_pretrained(str(fold_output_dir))
        tokenizer.save_pretrained(str(fold_output_dir))
        print(f"GRPO adapter saved to: {fold_output_dir}")

        del model, tokenizer, grpo_trainer
        torch.cuda.empty_cache()

    print(f"\n{'='*60}")
    print(f"ALL FOLDS SFT+GRPO TRAINED ({MODEL_TAG})")
    print(f"Adapters saved to: {ADAPTERS_DIR}")


if __name__ == "__main__":
    main()
