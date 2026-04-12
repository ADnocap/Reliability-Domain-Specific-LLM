"""Evaluate base or fine-tuned model on GSM8K (grade school math benchmark).

Tests whether reliability-engineering fine-tuning preserves or improves
general mathematical reasoning ability.

Usage:
  SFT_GSM8K_MODE=baseline python training/evaluate_gsm8k.py
  SFT_GSM8K_MODE=finetuned python training/evaluate_gsm8k.py

GSM8K test set: 1319 questions. Each answer is a single integer.
"""

import json
import os
import re
import sys
import time
from pathlib import Path

import torch
from datasets import load_dataset as hf_load_dataset
from unsloth import FastLanguageModel

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from training.config import (
    MODEL_NAME, MODEL_TAG, MAX_SEQ_LENGTH,
    ADAPTERS_DIR, GENERATION_CONFIG, EVAL_THINKING,
)

MODE = os.environ.get("SFT_GSM8K_MODE", "baseline")
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "results" / f"gsm8k_{MODEL_TAG}" / MODE

SYSTEM_PROMPT = (
    "You are a helpful math tutor. Solve the following problem step-by-step. "
    "At the end, clearly state your final numerical answer after 'Final Answer:'."
)


def extract_gsm8k_answer(text: str) -> str:
    """Extract the numeric answer from a GSM8K ground truth string.
    GSM8K answers end with '#### <number>'."""
    match = re.search(r'####\s*([\-\d,]+)', text)
    if match:
        return match.group(1).replace(",", "").strip()
    return text.strip()


def extract_model_answer(response: str) -> str:
    """Extract the final numerical answer from model response."""
    # Try "Final Answer:" pattern first
    patterns = [
        r"[Ff]inal\s+[Aa]nswer\s*:\s*\$?\\?boxed\{?([\-\d,\.]+)\}?\$?",
        r"[Ff]inal\s+[Aa]nswer\s*:\s*([\-\d,\.]+)",
        r"[Tt]he\s+answer\s+is\s*:?\s*([\-\d,\.]+)",
        r"=\s*([\-\d,\.]+)\s*$",
    ]
    for pattern in patterns:
        match = re.search(pattern, response)
        if match:
            return match.group(1).replace(",", "").strip()

    # Fallback: last number in the response
    numbers = re.findall(r'[\-]?\d[\d,]*\.?\d*', response)
    if numbers:
        return numbers[-1].replace(",", "").strip()
    return response.strip()


def compare_gsm8k(predicted: str, ground_truth: str) -> bool:
    """Compare predicted answer to GSM8K ground truth (exact integer match)."""
    try:
        pred = int(float(predicted.replace(",", "").strip()))
        truth = int(float(ground_truth.replace(",", "").strip()))
        return pred == truth
    except (ValueError, OverflowError):
        return predicted.strip() == ground_truth.strip()


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Mode: {MODE}")
    print(f"Model tag: {MODEL_TAG}")
    print(f"Output: {OUTPUT_DIR}")

    # Load model
    if MODE == "finetuned":
        adapter_path = ADAPTERS_DIR / "fold_0"
        print(f"Loading fine-tuned model from {adapter_path}")
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=str(adapter_path),
            max_seq_length=MAX_SEQ_LENGTH,
            load_in_4bit=True,
        )
    else:
        print(f"Loading base model: {MODEL_NAME}")
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=MODEL_NAME,
            max_seq_length=MAX_SEQ_LENGTH,
            load_in_4bit=True,
        )

    FastLanguageModel.for_inference(model)
    print("Model loaded.\n")

    # Load GSM8K
    print("Loading GSM8K test set...")
    gsm8k = hf_load_dataset("openai/gsm8k", "main", split="test")
    print(f"GSM8K test questions: {len(gsm8k)}")

    results = []
    start = time.time()
    correct_count = 0

    for q_idx, item in enumerate(gsm8k):
        question = item["question"]
        gt_answer = extract_gsm8k_answer(item["answer"])

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ]
        input_ids = tokenizer.apply_chat_template(
            messages, add_generation_prompt=True, return_tensors="pt",
            enable_thinking=EVAL_THINKING,
        ).to(model.device)

        with torch.no_grad():
            output_ids = model.generate(input_ids=input_ids, **GENERATION_CONFIG)

        generated_ids = output_ids[0][input_ids.shape[1]:]
        response = tokenizer.decode(generated_ids, skip_special_tokens=True)

        predicted = extract_model_answer(response)
        is_correct = compare_gsm8k(predicted, gt_answer)
        if is_correct:
            correct_count += 1

        result = {
            "idx": q_idx,
            "question": question,
            "ground_truth": gt_answer,
            "model_response": response,
            "extracted_answer": predicted,
            "correct": is_correct,
        }
        results.append(result)

        status = "OK" if is_correct else "XX"
        if (q_idx + 1) % 50 == 0 or q_idx < 5:
            running_acc = correct_count / (q_idx + 1) * 100
            print(f"  [{q_idx+1}/{len(gsm8k)}] {status} | GT: {gt_answer} | Pred: {predicted} | Running: {running_acc:.1f}%")

    elapsed = time.time() - start
    accuracy = correct_count / len(results) * 100

    print(f"\n{'='*60}")
    print(f"GSM8K EVALUATION: {MODE} ({MODEL_TAG})")
    print(f"Accuracy: {correct_count}/{len(results)} = {accuracy:.1f}%")
    print(f"Elapsed: {elapsed:.0f}s ({elapsed/len(results):.1f}s/question)")
    print(f"{'='*60}")

    # Save results
    with open(OUTPUT_DIR / "results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    summary = {
        "benchmark": "gsm8k",
        "mode": MODE,
        "model": MODEL_NAME,
        "model_tag": MODEL_TAG,
        "total": len(results),
        "correct": correct_count,
        "accuracy": accuracy,
        "elapsed_seconds": elapsed,
    }
    with open(OUTPUT_DIR / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"Results saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
