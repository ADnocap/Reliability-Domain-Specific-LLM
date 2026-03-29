"""DPO training on reliability engineering questions.

For each fold:
  1. Load base model, generate responses for training questions
  2. Score against ground truth (5% numerical tolerance)
  3. Build preference pairs: chosen=ground_truth reasoning, rejected=model's wrong answer
  4. Apply LoRA and train with DPOTrainer (ref_model=None -> base model as reference)
  5. Save adapter to adapters/fold_X/ for evaluate_finetuned.py
"""

import json
import re
import sys
import time
from pathlib import Path

import torch
from unsloth import FastLanguageModel
from trl import DPOTrainer, DPOConfig
from datasets import Dataset

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.data_io import load_dataset
from training.config import (
    MODEL_NAME, MODEL_TAG, MAX_SEQ_LENGTH, N_FOLDS,
    CV_SPLITS_DIR, ADAPTERS_DIR, LORA_CONFIG, SYSTEM_PROMPT,
)


# ---------------------------------------------------------------------------
# Answer comparison (same as evaluate scripts, with comma fix)
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
    """Check if predicted answer matches ground truth within tolerance."""
    pred_norm = normalize_answer(predicted)
    truth_norm = normalize_answer(ground_truth)
    if pred_norm == truth_norm:
        return True

    # Fraction evaluation
    pred_frac = _eval_fraction(pred_norm)
    truth_frac = _eval_fraction(truth_norm)

    # Percentage conversion
    pred_clean = re.sub(r'(\d+\.?\d*)%', lambda m: str(float(m.group(1))/100), predicted)
    truth_clean = re.sub(r'(\d+\.?\d*)%', lambda m: str(float(m.group(1))/100), ground_truth)

    pred_numbers = re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", pred_clean)
    truth_numbers = re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", truth_clean)

    # Fraction vs decimal
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

    # Standard number comparison
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

    # Partial match
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
# DPO config
# ---------------------------------------------------------------------------
DPO_GENERATION_CONFIG = dict(
    max_new_tokens=2048,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
)

DPO_TRAIN_CONFIG = dict(
    beta=0.1,
    loss_type="sigmoid",
    max_length=2048,
    max_prompt_length=512,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=8,
    num_train_epochs=2,
    learning_rate=5e-6,
    warmup_ratio=0.1,
    lr_scheduler_type="cosine",
    optim="adamw_8bit",
    bf16=True,
    logging_steps=1,
    save_strategy="epoch",
    report_to="none",
    seed=42,
)

N_SAMPLES = 2  # responses per question for rejection sampling (2 is faster, still effective)


def generate_preference_pairs(model, tokenizer, train_data):
    """Generate DPO preference pairs from model responses vs ground truth."""
    pairs = []
    stats = {"total": 0, "model_wrong": 0, "model_right": 0, "pairs_created": 0}

    for idx, item in enumerate(train_data):
        # Reconstruct the original question from chat format
        convos = item["conversations"]
        question = None
        gt_answer = None
        for msg in convos:
            if msg["role"] == "user":
                question = msg["content"]
            if msg["role"] == "assistant":
                gt_response = msg["content"]
                # Extract answer from "Final Answer: ..."
                fa = extract_final_answer(gt_response)
                gt_answer = fa

        if not question or not gt_answer:
            continue

        stats["total"] += 1

        # Generate N responses from the model
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ]
        input_ids = tokenizer.apply_chat_template(
            messages, add_generation_prompt=True, return_tensors="pt",
            enable_thinking=False,
        ).to(model.device)

        wrong_responses = []
        right_responses = []

        for _ in range(N_SAMPLES):
            with torch.no_grad():
                output_ids = model.generate(
                    input_ids=input_ids,
                    **DPO_GENERATION_CONFIG,
                )
            generated_ids = output_ids[0][input_ids.shape[1]:]
            response = tokenizer.decode(generated_ids, skip_special_tokens=True)
            extracted = extract_final_answer(response)

            if is_correct(extracted, gt_answer):
                right_responses.append(response)
            else:
                wrong_responses.append(response)

        if wrong_responses:
            stats["model_wrong"] += 1
            # Chosen: ground truth reasoning from dataset (or best correct response)
            if right_responses:
                chosen = right_responses[0]
            else:
                chosen = gt_response  # use dataset reasoning as chosen

            rejected = wrong_responses[0]

            pairs.append({
                "prompt": messages,
                "chosen": [{"role": "assistant", "content": chosen}],
                "rejected": [{"role": "assistant", "content": rejected}],
            })
            stats["pairs_created"] += 1
        else:
            stats["model_right"] += 1

        if (idx + 1) % 20 == 0:
            print(f"  [{idx+1}/{len(train_data)}] pairs: {stats['pairs_created']}, "
                  f"model_right: {stats['model_right']}, model_wrong: {stats['model_wrong']}")

    return pairs, stats


def main():
    ADAPTERS_DIR.mkdir(parents=True, exist_ok=True)

    for fold_idx in range(N_FOLDS):
        print(f"\n{'='*60}")
        print(f"FOLD {fold_idx} - DPO ({MODEL_TAG})")
        print(f"{'='*60}")

        train_path = CV_SPLITS_DIR / f"fold_{fold_idx}_train.jsonl"
        train_data = load_dataset(str(train_path))
        print(f"Training samples: {len(train_data)}")

        # Phase 1: Generate preference pairs
        print(f"\n--- Phase 1: Generating preference pairs ---")
        print(f"Loading model: {MODEL_NAME}")
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=MODEL_NAME,
            max_seq_length=MAX_SEQ_LENGTH,
            load_in_4bit=True,
        )
        FastLanguageModel.for_inference(model)

        start_time = time.time()
        pairs, stats = generate_preference_pairs(model, tokenizer, train_data)
        elapsed = time.time() - start_time
        print(f"\nPreference pairs: {len(pairs)} from {stats['total']} questions "
              f"({elapsed:.0f}s)")
        print(f"  Model correct on all samples: {stats['model_right']}")
        print(f"  Model wrong on some samples: {stats['model_wrong']}")

        if len(pairs) < 10:
            print(f"  Too few pairs ({len(pairs)}), skipping DPO for this fold.")
            del model, tokenizer
            torch.cuda.empty_cache()
            continue

        # Save pairs for analysis
        pairs_path = ADAPTERS_DIR / f"fold_{fold_idx}_dpo_pairs.json"
        with open(pairs_path, "w", encoding="utf-8") as f:
            json.dump(pairs, f, indent=2, ensure_ascii=False)

        # Free inference model
        del model, tokenizer
        torch.cuda.empty_cache()

        # Phase 2: DPO training
        print(f"\n--- Phase 2: DPO training ---")
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=MODEL_NAME,
            max_seq_length=MAX_SEQ_LENGTH,
            load_in_4bit=True,
        )
        model = FastLanguageModel.get_peft_model(model, **LORA_CONFIG)
        print("LoRA applied for DPO.")

        dpo_dataset = Dataset.from_list(pairs)

        fold_output_dir = ADAPTERS_DIR / f"fold_{fold_idx}"
        fold_output_dir.mkdir(parents=True, exist_ok=True)

        dpo_config = DPOConfig(
            output_dir=str(fold_output_dir),
            **DPO_TRAIN_CONFIG,
        )

        trainer = DPOTrainer(
            model=model,
            ref_model=None,
            train_dataset=dpo_dataset,
            tokenizer=tokenizer,
            args=dpo_config,
        )

        print("Starting DPO training...")
        train_result = trainer.train()
        print(f"DPO training complete. Loss: {train_result.training_loss:.4f}")

        model.save_pretrained(str(fold_output_dir))
        tokenizer.save_pretrained(str(fold_output_dir))
        print(f"DPO adapter saved to: {fold_output_dir}")

        del model, tokenizer, trainer, dpo_dataset
        torch.cuda.empty_cache()

    print(f"\n{'='*60}")
    print(f"ALL FOLDS DPO TRAINED ({MODEL_TAG})")
    print(f"Adapters saved to: {ADAPTERS_DIR}")


if __name__ == "__main__":
    main()
