"""Evaluate fine-tuned model on each fold's test set.

For each fold: loads base model + merges LoRA adapter, then runs identical
evaluation to evaluate_baseline.py.

Output: results/sft_cv_{MODEL_TAG}/finetuned/fold_{i}_results.json + summary.json
"""

import json
import re
import sys
import time
from pathlib import Path

import torch
from unsloth import FastLanguageModel

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.data_io import load_dataset
from training.config import (
    MODEL_NAME, MODEL_TAG, MAX_SEQ_LENGTH, N_FOLDS,
    CV_SPLITS_DIR, ADAPTERS_DIR, FINETUNED_DIR, SYSTEM_PROMPT, GENERATION_CONFIG,
)


# ---------------------------------------------------------------------------
# Answer comparison (same as evaluate_baseline.py)
# ---------------------------------------------------------------------------
def normalize_answer(answer: str) -> str:
    answer = answer.lower().strip()
    answer = answer.replace(" ", "")
    answer = answer.replace("\u00d7", "x")
    answer = answer.replace("^", "**")
    return answer


def compare_answers(predicted: str, ground_truth: str) -> dict:
    pred_norm = normalize_answer(predicted)
    truth_norm = normalize_answer(ground_truth)

    exact_match = pred_norm == truth_norm

    pred_numbers = re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", predicted)
    truth_numbers = re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", ground_truth)

    numerical_match = False
    if pred_numbers and truth_numbers:
        try:
            pred_nums = [float(x) for x in pred_numbers]
            truth_nums = [float(x) for x in truth_numbers]
            if len(pred_nums) == len(truth_nums):
                matches = [
                    abs(p - t) / max(abs(t), 1e-10) < 0.05
                    for p, t in zip(pred_nums, truth_nums)
                ]
                numerical_match = all(matches)
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
    FINETUNED_DIR.mkdir(parents=True, exist_ok=True)

    all_fold_summaries = []

    for fold_idx in range(N_FOLDS):
        print(f"\n{'='*60}")
        print(f"FOLD {fold_idx} (fine-tuned {MODEL_TAG})")
        print(f"{'='*60}")

        adapter_path = ADAPTERS_DIR / f"fold_{fold_idx}"
        if not adapter_path.exists():
            print(f"  Adapter not found at {adapter_path}, skipping.")
            continue

        print(f"Loading model + adapter from {adapter_path}")
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=str(adapter_path),
            max_seq_length=MAX_SEQ_LENGTH,
            load_in_4bit=True,
        )
        FastLanguageModel.for_inference(model)
        print("Model loaded with LoRA adapter.\n")

        test_path = CV_SPLITS_DIR / f"fold_{fold_idx}_test.jsonl"
        test_data = load_dataset(str(test_path))
        print(f"Test samples: {len(test_data)}")

        fold_results = []
        start_time = time.time()

        for q_idx, item in enumerate(test_data):
            question = item["question"]
            ground_truth = item["answer"]

            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question},
            ]
            input_ids = tokenizer.apply_chat_template(
                messages, add_generation_prompt=True, return_tensors="pt"
            ).to(model.device)

            with torch.no_grad():
                output_ids = model.generate(
                    input_ids=input_ids,
                    **GENERATION_CONFIG,
                )

            generated_ids = output_ids[0][input_ids.shape[1]:]
            response = tokenizer.decode(generated_ids, skip_special_tokens=True)

            extracted = extract_final_answer(response)
            comparison = compare_answers(extracted, ground_truth)

            result = {
                "fold": fold_idx,
                "question_idx": q_idx,
                "question": question,
                "ground_truth": ground_truth,
                "answer_type": item.get("answer_type", "unknown"),
                "model_response": response,
                "extracted_answer": extracted,
                **comparison,
            }
            fold_results.append(result)

            status = "CORRECT" if comparison["correct"] else "WRONG"
            print(f"  [{q_idx+1}/{len(test_data)}] {status} | "
                  f"Extracted: {extracted[:80]}...")

        elapsed = time.time() - start_time

        n_correct = sum(1 for r in fold_results if r["correct"])
        accuracy = n_correct / len(fold_results) * 100 if fold_results else 0

        type_acc = {}
        for r in fold_results:
            t = r["answer_type"]
            if t not in type_acc:
                type_acc[t] = {"correct": 0, "total": 0}
            type_acc[t]["total"] += 1
            if r["correct"]:
                type_acc[t]["correct"] += 1

        fold_summary = {
            "fold": fold_idx,
            "total": len(fold_results),
            "correct": n_correct,
            "accuracy": accuracy,
            "accuracy_by_type": {
                t: v["correct"] / v["total"] * 100
                for t, v in type_acc.items()
            },
            "elapsed_seconds": elapsed,
        }
        all_fold_summaries.append(fold_summary)

        print(f"  Fold {fold_idx}: {n_correct}/{len(fold_results)} = {accuracy:.1f}% "
              f"({elapsed:.0f}s)\n")

        fold_output = FINETUNED_DIR / f"fold_{fold_idx}_results.json"
        with open(fold_output, "w", encoding="utf-8") as f:
            json.dump(fold_results, f, indent=2, ensure_ascii=False)

        del model, tokenizer
        torch.cuda.empty_cache()

    if all_fold_summaries:
        mean_acc = sum(s["accuracy"] for s in all_fold_summaries) / len(all_fold_summaries)
        summary = {
            "model": MODEL_NAME,
            "model_tag": MODEL_TAG,
            "adapter_dir": str(ADAPTERS_DIR),
            "n_folds": len(all_fold_summaries),
            "mean_accuracy": mean_acc,
            "per_fold": all_fold_summaries,
        }
        with open(FINETUNED_DIR / "summary.json", "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        print(f"{'='*60}")
        print(f"FINETUNED EVALUATION COMPLETE ({MODEL_TAG})")
        print(f"Mean accuracy: {mean_acc:.1f}%")
        for s in all_fold_summaries:
            print(f"  Fold {s['fold']}: {s['accuracy']:.1f}%")
        print(f"Results: {FINETUNED_DIR}")


if __name__ == "__main__":
    main()
