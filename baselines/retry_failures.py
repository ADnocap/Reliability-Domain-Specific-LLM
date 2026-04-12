"""Retry UNABLE_TO_EXTRACT questions: re-call the model and re-extract.
The original responses were truncated, so we need fresh API calls."""

import sys, json, time, threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from baselines.benchmark_sota import (
    MODELS, DATASETS, BenchmarkConfig,
    call_model, extract_answer, compare_answers,
    token_usage,
)

cfg = BenchmarkConfig()
# Use higher max_tokens for retries to avoid truncation
cfg.max_tokens = 8192

base = Path(cfg.output_base)

total_retried = 0
total_fixed = 0

for ds_info in DATASETS:
    ds_name = ds_info["name"]
    ds_dir = base / ds_name

    for model in MODELS:
        model_short = model.split("/")[-1]
        results_file = ds_dir / f"{model_short}_results.json"

        if not results_file.exists():
            continue

        with open(results_file, encoding="utf-8") as f:
            results = json.load(f)

        # Find failures
        failures = [
            (i, r) for i, r in enumerate(results)
            if "UNABLE_TO_EXTRACT" in str(r.get("extracted_answer", ""))
            or "EXTRACTION_ERROR" in str(r.get("extracted_answer", ""))
        ]

        if not failures:
            print(f"{ds_name}/{model_short}: 0 failures, skipping")
            continue

        print(f"\n{ds_name}/{model_short}: retrying {len(failures)} failures...")

        fixed = 0
        for idx, old_result in tqdm(failures, desc=f"retry {model_short}"):
            question = old_result["question"]
            ground_truth = old_result["ground_truth"]

            # Re-call model
            new_response = call_model(model, question, cfg)
            if new_response.startswith("ERROR"):
                continue

            # Re-extract
            new_extracted = extract_answer(question, new_response, cfg)

            # Compare
            comparison = compare_answers(new_extracted, ground_truth)

            # Update result in-place
            results[idx]["model_response"] = new_response
            results[idx]["extracted_answer"] = new_extracted
            results[idx].update(comparison)

            if "UNABLE_TO_EXTRACT" not in new_extracted and "EXTRACTION_ERROR" not in new_extracted:
                fixed += 1

        # Save updated results
        with open(results_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        new_correct = sum(1 for r in results if r["correct"])
        still_unable = sum(1 for r in results if "UNABLE_TO_EXTRACT" in str(r.get("extracted_answer", "")))

        print(f"  Fixed extraction: {fixed}/{len(failures)}")
        print(f"  Still UNABLE: {still_unable}")
        print(f"  New accuracy: {new_correct}/{len(results)} ({new_correct/len(results)*100:.1f}%)")

        total_retried += len(failures)
        total_fixed += fixed

print(f"\n{'='*60}")
print(f"RETRY COMPLETE: {total_fixed}/{total_retried} extractions fixed")
print(f"{'='*60}")

# Print updated summary
print("\nUpdated results:")
for ds_info in DATASETS:
    ds_name = ds_info["name"]
    ds_dir = base / ds_name
    print(f"\n  {ds_name}:")
    for model in MODELS:
        model_short = model.split("/")[-1]
        results_file = ds_dir / f"{model_short}_results.json"
        if not results_file.exists():
            continue
        with open(results_file, encoding="utf-8") as f:
            results = json.load(f)
        correct = sum(1 for r in results if r["correct"])
        unable = sum(1 for r in results if "UNABLE_TO_EXTRACT" in str(r.get("extracted_answer", "")))
        print(f"    {model_short:>30s}: {correct}/{len(results)} ({correct/len(results)*100:.1f}%)  UNABLE: {unable}")
