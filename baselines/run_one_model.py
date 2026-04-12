"""Run benchmark for a single model on a single dataset. Usage:
    python baselines/run_one_model.py <model_index> <dataset_index>
    model_index:   0=gemini, 1=claude, 2=o3-mini
    dataset_index: 0=v4_500sample, 1=holdout_54q
"""
import sys, json, time, threading
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from baselines.benchmark_sota import (
    MODELS, DATASETS, BenchmarkConfig,
    evaluate_question, token_usage,
    _load_dataset, save_dataset,
)
import random

model_idx = int(sys.argv[1]) if len(sys.argv) > 1 else 0
ds_idx = int(sys.argv[2]) if len(sys.argv) > 2 else 0

cfg = BenchmarkConfig()
model = MODELS[model_idx]
ds_info = DATASETS[ds_idx]
model_short = model.split("/")[-1]

output_dir = Path(cfg.output_base) / ds_info["name"]
output_dir.mkdir(parents=True, exist_ok=True)

# Load & sample (same logic as main script)
dataset = _load_dataset(ds_info["path"])
sample_size = ds_info.get("sample_size")
if sample_size and sample_size < len(dataset):
    random.seed(cfg.seed)
    dataset = random.sample(dataset, sample_size)

# Save sampled questions if not already there
sq = output_dir / "sampled_questions.jsonl"
if not sq.exists():
    save_dataset(dataset, str(sq))

print(f"Model: {model} | Dataset: {ds_info['name']} ({len(dataset)} questions)")
print(f"Output: {output_dir}")

results = []
start = time.time()

with ThreadPoolExecutor(max_workers=cfg.max_workers) as pool:
    futures = {pool.submit(evaluate_question, item, model, cfg): item for item in dataset}
    for fut in tqdm(as_completed(futures), total=len(dataset), desc=model_short):
        try:
            results.append(fut.result())
        except Exception as e:
            print(f"  [FAIL] {e}")

elapsed = time.time() - start
correct = sum(1 for r in results if r["correct"])
unable = sum(1 for r in results if "UNABLE_TO_EXTRACT" in str(r.get("extracted_answer", "")))

print(f"\n{model_short}: {correct}/{len(results)} correct ({correct/len(results)*100:.1f}%)")
print(f"UNABLE_TO_EXTRACT: {unable}")
print(f"Elapsed: {elapsed/60:.1f} min")
print(f"Tokens: {token_usage.get(model, 0):,}")

# Save
out_file = output_dir / f"{model_short}_results.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
print(f"Saved to {out_file}")
