"""Evaluate base or fine-tuned model on the independent holdout set (54 questions).

Usage:
  SFT_HOLDOUT_MODE=baseline python training/evaluate_holdout.py
  SFT_HOLDOUT_MODE=finetuned python training/evaluate_holdout.py

For finetuned mode, uses fold_0 adapter from the specified experiment.
"""

import json
import os
import re
import sys
import time
from pathlib import Path

import torch
from unsloth import FastLanguageModel

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.data_io import load_dataset
from training.config import (
    MODEL_NAME, MODEL_TAG, MAX_SEQ_LENGTH,
    ADAPTERS_DIR, SYSTEM_PROMPT, GENERATION_CONFIG, EVAL_THINKING,
)

MODE = os.environ.get("SFT_HOLDOUT_MODE", "baseline")  # "baseline" or "finetuned"
HOLDOUT_PATH = Path(__file__).resolve().parent.parent / "data" / "independent_holdout_54q.jsonl"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "results" / f"holdout_{MODEL_TAG}" / MODE


# ---------------------------------------------------------------------------
# Answer comparison (same as evaluate_baseline.py)
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


def compare_answers(predicted: str, ground_truth: str) -> dict:
    pred_norm = normalize_answer(predicted)
    truth_norm = normalize_answer(ground_truth)
    exact_match = pred_norm == truth_norm

    pred_frac = _eval_fraction(pred_norm)
    truth_frac = _eval_fraction(truth_norm)

    pred_clean = re.sub(r'(\d+\.?\d*)%', lambda m: str(float(m.group(1))/100), predicted)
    truth_clean = re.sub(r'(\d+\.?\d*)%', lambda m: str(float(m.group(1))/100), ground_truth)
    pred_numbers = re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", pred_clean)
    truth_numbers = re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", truth_clean)

    numerical_match = False
    if pred_frac is not None and truth_numbers:
        try:
            truth_val = float(truth_numbers[0])
            numerical_match = abs(pred_frac - truth_val) / max(abs(truth_val), 1e-10) < 0.05
        except ValueError:
            pass
    elif truth_frac is not None and pred_numbers:
        try:
            pred_val = float(pred_numbers[0])
            numerical_match = abs(pred_val - truth_frac) / max(abs(truth_frac), 1e-10) < 0.05
        except ValueError:
            pass

    if not numerical_match and pred_numbers and truth_numbers:
        try:
            pred_nums = [float(x) for x in pred_numbers]
            truth_nums = [float(x) for x in truth_numbers]
            if len(pred_nums) == len(truth_nums):
                matches = [abs(p - t) / max(abs(t), 1e-10) < 0.05 for p, t in zip(pred_nums, truth_nums)]
                numerical_match = all(matches)
            elif len(truth_nums) == 1:
                numerical_match = any(abs(p - truth_nums[0]) / max(abs(truth_nums[0]), 1e-10) < 0.05 for p in pred_nums)
        except (ValueError, ZeroDivisionError):
            pass

    partial_match = truth_norm in pred_norm or pred_norm in truth_norm
    return {
        "exact_match": exact_match,
        "numerical_match": numerical_match,
        "partial_match": partial_match,
        "correct": exact_match or numerical_match or (partial_match and len(truth_norm) > 3),
    }


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


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Mode: {MODE}")
    print(f"Model tag: {MODEL_TAG}")
    print(f"Holdout: {HOLDOUT_PATH}")
    print(f"Output: {OUTPUT_DIR}")

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

    dataset = load_dataset(str(HOLDOUT_PATH))
    print(f"Holdout questions: {len(dataset)}")

    results = []
    start = time.time()

    for q_idx, item in enumerate(dataset):
        question = item["question"]
        ground_truth = item["answer"]

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

        extracted = extract_final_answer(response)
        comparison = compare_answers(extracted, ground_truth)

        result = {
            "question_idx": q_idx,
            "question": question,
            "ground_truth": ground_truth,
            "answer_type": item.get("answer_type", "unknown"),
            "source": item.get("source", "unknown"),
            "model_response": response,
            "extracted_answer": extracted,
            **comparison,
        }
        results.append(result)

        status = "CORRECT" if comparison["correct"] else "WRONG"
        print(f"  [{q_idx+1}/{len(dataset)}] {status} | GT: {ground_truth[:50]} | Pred: {extracted[:50]}")

    elapsed = time.time() - start
    n_correct = sum(1 for r in results if r["correct"])
    accuracy = n_correct / len(results) * 100

    print(f"\n{'='*60}")
    print(f"HOLDOUT EVALUATION: {MODE} ({MODEL_TAG})")
    print(f"Accuracy: {n_correct}/{len(results)} = {accuracy:.1f}%")
    print(f"Elapsed: {elapsed:.0f}s")
    print(f"{'='*60}")

    # Save results
    with open(OUTPUT_DIR / "results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    summary = {
        "mode": MODE,
        "model": MODEL_NAME,
        "model_tag": MODEL_TAG,
        "holdout_path": str(HOLDOUT_PATH),
        "total": len(results),
        "correct": n_correct,
        "accuracy": accuracy,
        "elapsed_seconds": elapsed,
    }
    with open(OUTPUT_DIR / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"Results saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
