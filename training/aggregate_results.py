"""Aggregate cross-validation results: baseline vs fine-tuned.

Produces:
  - results/sft_cv_{MODEL_TAG}/cv_comparison.csv
  - results/sft_cv_{MODEL_TAG}/cv_summary.json

Can run locally after downloading results from LaRuche.
"""

import json
import csv
import sys
from pathlib import Path
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from training.config import RESULTS_DIR, BASELINE_DIR, FINETUNED_DIR, N_FOLDS, MODEL_TAG


def load_fold_results(directory: Path, fold_idx: int) -> list:
    path = directory / f"fold_{fold_idx}_results.json"
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    print(f"Aggregating cross-validation results for {MODEL_TAG}...\n")

    baseline_accs = []
    finetuned_accs = []
    comparison_rows = []
    all_deltas = []
    type_stats = {}

    for fold_idx in range(N_FOLDS):
        b_results = load_fold_results(BASELINE_DIR, fold_idx)
        f_results = load_fold_results(FINETUNED_DIR, fold_idx)

        if not b_results or not f_results:
            print(f"Fold {fold_idx}: missing results, skipping.")
            continue

        b_correct = sum(1 for r in b_results if r["correct"])
        f_correct = sum(1 for r in f_results if r["correct"])
        total = len(b_results)
        b_acc = b_correct / total * 100
        f_acc = f_correct / total * 100

        baseline_accs.append(b_acc)
        finetuned_accs.append(f_acc)

        comparison_rows.append({
            "fold": fold_idx,
            "total": total,
            "baseline_correct": b_correct,
            "baseline_accuracy": round(b_acc, 2),
            "finetuned_correct": f_correct,
            "finetuned_accuracy": round(f_acc, 2),
            "delta": round(f_acc - b_acc, 2),
        })

        print(f"Fold {fold_idx}: baseline={b_acc:.1f}% | finetuned={f_acc:.1f}% | "
              f"delta={f_acc - b_acc:+.1f}%")

        b_by_q = {r["question"]: r for r in b_results}
        f_by_q = {r["question"]: r for r in f_results}

        for q, b_r in b_by_q.items():
            f_r = f_by_q.get(q)
            if f_r is None:
                continue

            answer_type = b_r.get("answer_type", "unknown")

            if answer_type not in type_stats:
                type_stats[answer_type] = {
                    "baseline_correct": 0, "finetuned_correct": 0, "total": 0
                }
            type_stats[answer_type]["total"] += 1
            if b_r["correct"]:
                type_stats[answer_type]["baseline_correct"] += 1
            if f_r["correct"]:
                type_stats[answer_type]["finetuned_correct"] += 1

            b_ok = b_r["correct"]
            f_ok = f_r["correct"]
            if b_ok != f_ok:
                all_deltas.append({
                    "fold": fold_idx,
                    "question": q[:120],
                    "answer_type": answer_type,
                    "ground_truth": b_r["ground_truth"],
                    "baseline_correct": bool(b_ok),
                    "finetuned_correct": bool(f_ok),
                    "flip": "wrong->right" if f_ok else "right->wrong",
                    "baseline_answer": b_r.get("extracted_answer", "")[:100],
                    "finetuned_answer": f_r.get("extracted_answer", "")[:100],
                })

    if not baseline_accs:
        print("No complete fold results found. Exiting.")
        return

    n = len(baseline_accs)
    b_mean = sum(baseline_accs) / n
    f_mean = sum(finetuned_accs) / n
    b_std = (sum((x - b_mean) ** 2 for x in baseline_accs) / n) ** 0.5
    f_std = (sum((x - f_mean) ** 2 for x in finetuned_accs) / n) ** 0.5

    try:
        wilcoxon_stat, wilcoxon_p = stats.wilcoxon(finetuned_accs, baseline_accs)
    except ValueError:
        wilcoxon_stat, wilcoxon_p = float("nan"), float("nan")

    type_breakdown = {}
    for t, v in type_stats.items():
        total = v["total"]
        type_breakdown[t] = {
            "total": total,
            "baseline_correct": v["baseline_correct"],
            "baseline_accuracy": round(v["baseline_correct"] / total * 100, 2) if total else 0,
            "finetuned_correct": v["finetuned_correct"],
            "finetuned_accuracy": round(v["finetuned_correct"] / total * 100, 2) if total else 0,
            "delta": round(
                (v["finetuned_correct"] - v["baseline_correct"]) / total * 100, 2
            ) if total else 0,
        }

    print(f"\n{'='*60}")
    print(f"CROSS-VALIDATION SUMMARY ({MODEL_TAG})")
    print(f"{'='*60}")
    print(f"Baseline:   {b_mean:.1f}% +/- {b_std:.1f}%")
    print(f"Finetuned:  {f_mean:.1f}% +/- {f_std:.1f}%")
    print(f"Delta:      {f_mean - b_mean:+.1f}%")
    print(f"Wilcoxon p: {wilcoxon_p:.4f}")
    print(f"Significant (p<0.05): {'Yes' if wilcoxon_p < 0.05 else 'No'}")

    print(f"\nBy answer type:")
    for t, v in type_breakdown.items():
        print(f"  {t}: baseline={v['baseline_accuracy']:.1f}% -> "
              f"finetuned={v['finetuned_accuracy']:.1f}% "
              f"(delta={v['delta']:+.1f}%, n={v['total']})")

    print(f"\nQuestion flips ({len(all_deltas)} total):")
    wrong_to_right = [d for d in all_deltas if d["flip"] == "wrong->right"]
    right_to_wrong = [d for d in all_deltas if d["flip"] == "right->wrong"]
    print(f"  Wrong->Right: {len(wrong_to_right)}")
    print(f"  Right->Wrong: {len(right_to_wrong)}")

    csv_path = RESULTS_DIR / "cv_comparison.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=comparison_rows[0].keys())
        writer.writeheader()
        writer.writerows(comparison_rows)
    print(f"\nSaved: {csv_path}")

    is_nan = wilcoxon_stat != wilcoxon_stat
    summary = {
        "model_tag": MODEL_TAG,
        "n_folds": n,
        "baseline": {
            "mean_accuracy": round(b_mean, 2),
            "std_accuracy": round(b_std, 2),
            "per_fold": baseline_accs,
        },
        "finetuned": {
            "mean_accuracy": round(f_mean, 2),
            "std_accuracy": round(f_std, 2),
            "per_fold": finetuned_accs,
        },
        "delta_mean": round(f_mean - b_mean, 2),
        "wilcoxon_statistic": float(wilcoxon_stat) if not is_nan else None,
        "wilcoxon_p_value": float(wilcoxon_p) if not is_nan else None,
        "significant": bool(wilcoxon_p < 0.05) if not is_nan else None,
        "accuracy_by_type": type_breakdown,
        "question_flips": all_deltas,
        "per_fold_comparison": comparison_rows,
    }
    summary_path = RESULTS_DIR / "cv_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"Saved: {summary_path}")


if __name__ == "__main__":
    main()
