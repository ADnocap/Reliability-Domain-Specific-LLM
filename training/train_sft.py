"""Fine-tune model with Unsloth LoRA on each fold's training set.

For each fold (0-4):
  1. Load fresh base model (4-bit quantized)
  2. Apply LoRA adapters
  3. Train with SFTTrainer
  4. Save LoRA adapter to results/sft_cv_{MODEL_TAG}/adapters/fold_{i}/
"""

import sys
from functools import partial
from pathlib import Path

import torch
from unsloth import FastLanguageModel
from trl import SFTTrainer, SFTConfig
from datasets import Dataset

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.data_io import load_dataset
from training.config import (
    MODEL_NAME, MODEL_TAG, MAX_SEQ_LENGTH, N_FOLDS,
    CV_SPLITS_DIR, ADAPTERS_DIR, LORA_CONFIG, TRAIN_CONFIG,
)


def formatting_func(examples, tokenizer):
    """Format examples into chat template strings (model-agnostic).

    Uses tokenizer.apply_chat_template() so the pipeline works with any model
    (Llama, Qwen, Gemma, etc.).

    Unsloth calls this in two ways:
    - Test call: single example (dict with conversations as list of messages)
    - Batched call: dict of lists (conversations is list of list of messages)
    Must always return a list of strings.
    """
    conversations = examples["conversations"]
    if conversations and isinstance(conversations[0], dict):
        convos = [conversations]
    else:
        convos = conversations

    results = []
    for convo in convos:
        text = tokenizer.apply_chat_template(
            convo, tokenize=False, add_generation_prompt=False
        )
        results.append(text)
    return results


def main():
    ADAPTERS_DIR.mkdir(parents=True, exist_ok=True)

    for fold_idx in range(N_FOLDS):
        print(f"\n{'='*60}")
        print(f"FOLD {fold_idx} ({MODEL_TAG})")
        print(f"{'='*60}")

        train_path = CV_SPLITS_DIR / f"fold_{fold_idx}_train.jsonl"
        train_data = load_dataset(str(train_path))
        print(f"Training samples: {len(train_data)}")

        print(f"Loading model: {MODEL_NAME}")
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=MODEL_NAME,
            max_seq_length=MAX_SEQ_LENGTH,
            load_in_4bit=True,
        )

        model = FastLanguageModel.get_peft_model(model, **LORA_CONFIG)
        print("LoRA applied.")

        hf_dataset = Dataset.from_list(train_data)

        fold_output_dir = ADAPTERS_DIR / f"fold_{fold_idx}"
        fold_output_dir.mkdir(parents=True, exist_ok=True)

        sft_config = SFTConfig(
            output_dir=str(fold_output_dir),
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

        print("Starting training...")
        train_result = trainer.train()
        print(f"Training complete. Loss: {train_result.training_loss:.4f}")

        model.save_pretrained(str(fold_output_dir))
        tokenizer.save_pretrained(str(fold_output_dir))
        print(f"Adapter saved to: {fold_output_dir}")

        del model, tokenizer, trainer, hf_dataset
        torch.cuda.empty_cache()

    print(f"\n{'='*60}")
    print(f"ALL FOLDS TRAINED ({MODEL_TAG})")
    print(f"Adapters saved to: {ADAPTERS_DIR}")


if __name__ == "__main__":
    main()
