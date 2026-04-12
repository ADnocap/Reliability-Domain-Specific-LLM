"""
Benchmark state-of-the-art LLMs on reliability engineering datasets.

Models: Gemini 3.1 Pro, Claude Sonnet 4.6, o3-mini
Datasets:
  1. master_dataset_v4.jsonl (150-sample)
  2. independent_holdout_54q.jsonl (all 54)

All models run with reasoning/thinking tokens OFF and low temperature
to match fine-tuned model evaluation conditions.
"""

import json
import re
import sys
import random
import time
import threading

# Fix Windows console encoding for unicode/emoji in model responses
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.api_client import create_openrouter_client
from utils.data_io import load_dataset as _load_dataset, save_dataset

# ── Config ───────────────────────────────────────────────────────────────────

MODELS = [
    "google/gemini-3.1-pro-preview",
    "anthropic/claude-sonnet-4.6",
    "openai/o3-mini",
]

# Per-model extra params to disable reasoning/thinking tokens
MODEL_EXTRA_PARAMS = {
    "openai/o3-mini": {"reasoning_effort": "low"},
    # Claude and Gemini have thinking/reasoning off by default
}

DATASETS = [
    {
        "name": "v4_500sample",
        "path": str(Path(__file__).resolve().parent.parent / "data" / "master_dataset_v4.jsonl"),
        "sample_size": 500,
        "description": "500-question sample from master_dataset_v4 (866 total)",
    },
    {
        "name": "holdout_54q",
        "path": str(Path(__file__).resolve().parent / "independent_holdout_54q.jsonl"),
        "sample_size": None,  # use all
        "description": "Independent holdout set (54 questions)",
    },
]


@dataclass
class BenchmarkConfig:
    models: List[str] = field(default_factory=lambda: MODELS)
    extractor_model: str = "google/gemini-2.5-flash"
    seed: int = 42
    max_workers: int = 5
    temperature: float = 0.1
    max_tokens: int = 4096
    output_base: str = str(Path(__file__).resolve().parent / "results")


# ── Globals ──────────────────────────────────────────────────────────────────

import os
from dotenv import load_dotenv
load_dotenv()
client = create_openrouter_client(api_key=os.getenv("OPENROUTER_API_KEY_PROF"))
token_usage: Dict[str, int] = {}
token_lock = threading.Lock()

# ── Prompts ──────────────────────────────────────────────────────────────────

EVAL_PROMPT = """You are an expert in reliability engineering, probability theory, and system analysis.

A student has asked you the following question. Provide a clear, accurate answer.

IMPORTANT INSTRUCTIONS:
1. Read the question carefully and identify what is being asked
2. Show your reasoning step-by-step
3. Perform any necessary calculations accurately
4. At the end, clearly state your FINAL ANSWER
5. For multi-part questions (a, b, c, etc.), provide ALL answers
6. Format your final answer clearly - use numbers, comma-separated values, or True/False as appropriate

Question:
{question}

Please solve this problem step-by-step and provide your final answer."""

EXTRACTION_PROMPT = """You are extracting the final answer from a model's response to a reliability engineering question.

The model may have provided reasoning, calculations, or thinking. Your job is to extract ONLY the final answer.

EXTRACTION RULES:
1. Look for phrases like "final answer", "the answer is", "therefore", "result"
2. Extract the numerical value(s), boolean (True/False), or expression
3. For multi-part answers, provide comma-separated values
4. Remove units, explanations, and extra text
5. If multiple numbers are given, extract all of them comma-separated
6. If no clear answer exists, respond with: "UNABLE_TO_EXTRACT"

EXAMPLES:
Model response: "After calculating, the reliability is 0.95 and the MTTF is 1000 hours."
Your extraction: "0.95, 1000"

Model response: "The system will fail, so the answer is False."
Your extraction: "False"

Model response: "Therefore, the final answer is approximately 0.8413."
Your extraction: "0.8413"

ORIGINAL QUESTION:
{question}

MODEL'S RESPONSE:
{model_response}

Extract ONLY the final answer (no explanation):"""

# ── Core functions ───────────────────────────────────────────────────────────

def call_model(model: str, question: str, cfg: BenchmarkConfig) -> str:
    try:
        kwargs = dict(
            model=model,
            max_tokens=cfg.max_tokens,
            temperature=cfg.temperature,
            timeout=180,
            messages=[{"role": "user", "content": EVAL_PROMPT.format(question=question)}],
        )
        extra = MODEL_EXTRA_PARAMS.get(model, {})
        if extra:
            kwargs["extra_body"] = extra

        resp = client.chat.completions.create(**kwargs)
        with token_lock:
            token_usage[model] = token_usage.get(model, 0) + (
                resp.usage.prompt_tokens + resp.usage.completion_tokens
            )
        return resp.choices[0].message.content
    except Exception as e:
        print(f"  [ERROR] {model}: {e}")
        return f"ERROR: {e}"


def extract_answer(question: str, model_response: str, cfg: BenchmarkConfig) -> str:
    try:
        resp = client.chat.completions.create(
            model=cfg.extractor_model,
            max_tokens=200,
            temperature=0.1,
            timeout=180,
            messages=[{"role": "user", "content": EXTRACTION_PROMPT.format(
                question=question, model_response=model_response
            )}],
        )
        with token_lock:
            token_usage[cfg.extractor_model] = token_usage.get(cfg.extractor_model, 0) + (
                resp.usage.prompt_tokens + resp.usage.completion_tokens
            )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        print(f"  [EXTRACT ERROR] {e}")
        return "EXTRACTION_ERROR"


def normalize_answer(answer: str) -> str:
    answer = answer.lower().strip()
    answer = answer.replace(" ", "")
    answer = answer.replace("\u00d7", "x")
    answer = answer.replace("^", "**")
    return answer


def compare_answers(predicted: str, ground_truth: str) -> Dict:
    pred_norm = normalize_answer(predicted)
    truth_norm = normalize_answer(ground_truth)

    exact_match = pred_norm == truth_norm

    pred_numbers = re.findall(r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?', predicted)
    truth_numbers = re.findall(r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?', ground_truth)

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


def evaluate_question(item: Dict, model: str, cfg: BenchmarkConfig) -> Dict:
    question = item["question"]
    ground_truth = item["answer"]

    model_response = call_model(model, question, cfg)
    extracted = extract_answer(question, model_response, cfg)
    comparison = compare_answers(extracted, ground_truth)

    return {
        "source": item.get("source", "unknown"),
        "answer_type": item.get("answer_type", "unknown"),
        "question": question,
        "ground_truth": ground_truth,
        "model_response": model_response,
        "extracted_answer": extracted,
        **comparison,
    }


# ── Single-dataset benchmark ────────────────────────────────────────────────

def run_single_benchmark(dataset_info: Dict, cfg: BenchmarkConfig) -> pd.DataFrame:
    ds_name = dataset_info["name"]
    output_dir = Path(cfg.output_base) / ds_name
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load & sample
    dataset = _load_dataset(dataset_info["path"])
    print(f"\nLoaded {len(dataset)} questions from {dataset_info['path']}")

    sample_size = dataset_info.get("sample_size")
    if sample_size and sample_size < len(dataset):
        random.seed(cfg.seed)
        dataset = random.sample(dataset, sample_size)
        print(f"Sampled {sample_size} questions (seed={cfg.seed})")

    # Save sampled questions for reproducibility
    save_dataset(dataset, str(output_dir / "sampled_questions.jsonl"))

    all_results: Dict[str, List[Dict]] = {}
    start = time.time()

    print(f"\n{'='*80}")
    print(f"BENCHMARK: {dataset_info['description']}")
    print(f"{'='*80}")
    print(f"  Output:   {output_dir}")
    print(f"  Samples:  {len(dataset)}")
    print(f"  Models:   {', '.join(m.split('/')[-1] for m in cfg.models)}")
    print(f"  Temp:     {cfg.temperature}  |  Reasoning tokens: OFF")
    print(f"  Total API calls: {len(dataset) * len(cfg.models)} (+ extraction)")
    print(f"{'='*80}\n")

    for model in cfg.models:
        model_short = model.split("/")[-1]
        extra = MODEL_EXTRA_PARAMS.get(model, {})
        extra_str = f"  (extra: {extra})" if extra else ""
        print(f"\n--- Evaluating: {model}{extra_str} ---")

        results = []
        with ThreadPoolExecutor(max_workers=cfg.max_workers) as pool:
            futures = {
                pool.submit(evaluate_question, item, model, cfg): item
                for item in dataset
            }
            for fut in tqdm(as_completed(futures), total=len(dataset), desc=model_short):
                try:
                    results.append(fut.result())
                except Exception as e:
                    print(f"  [FAIL] {e}")

        all_results[model] = results

        correct = sum(1 for r in results if r["correct"])
        print(f"  => {model_short}: {correct}/{len(results)} correct ({correct/len(results)*100:.1f}%)")

        # Save per-model results
        model_file = output_dir / f"{model_short}_results.json"
        with open(model_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

    elapsed = time.time() - start

    # ── Summary ──────────────────────────────────────────────────────────
    print(f"\n{'='*80}")
    print(f"RESULTS: {ds_name}  (elapsed: {elapsed/60:.1f} min)")
    print(f"{'='*80}")

    rows = []
    for model, results in all_results.items():
        model_short = model.split("/")[-1]
        n = len(results)
        correct = sum(1 for r in results if r["correct"])
        exact = sum(1 for r in results if r["exact_match"])
        numerical = sum(1 for r in results if r["numerical_match"])
        partial = sum(1 for r in results if r["partial_match"])

        rows.append({
            "Model": model_short,
            "Correct": correct,
            "Exact": exact,
            "Numerical": numerical,
            "Partial": partial,
            "Total": n,
            "Accuracy (%)": round(correct / n * 100, 2) if n else 0,
            "Tokens": token_usage.get(model, 0),
        })
        print(f"  {model_short:>35s}:  {correct}/{n}  ({correct/n*100:.1f}%)")

    summary_df = pd.DataFrame(rows)
    summary_df.to_csv(output_dir / "summary.csv", index=False)

    # ── Detailed combined CSV ────────────────────────────────────────────
    combined = []
    for i, item in enumerate(dataset):
        row = {
            "idx": i,
            "source": item.get("source", "unknown"),
            "answer_type": item.get("answer_type", "unknown"),
            "question": item["question"],
            "ground_truth": item["answer"],
        }
        for model, results in all_results.items():
            ms = model.split("/")[-1]
            match = [r for r in results if r["question"] == item["question"]]
            if match:
                row[f"{ms}_extracted"] = match[0]["extracted_answer"]
                row[f"{ms}_correct"] = match[0]["correct"]
            else:
                row[f"{ms}_extracted"] = "N/A"
                row[f"{ms}_correct"] = False
        combined.append(row)

    pd.DataFrame(combined).to_csv(output_dir / "detailed_results.csv", index=False)

    # ── Accuracy by answer type ──────────────────────────────────────────
    print(f"\nAccuracy by answer type:")
    for model, results in all_results.items():
        ms = model.split("/")[-1]
        by_type: Dict[str, List[bool]] = {}
        for r in results:
            atype = r.get("answer_type", "unknown")
            by_type.setdefault(atype, []).append(r["correct"])
        print(f"  {ms}:")
        for atype, vals in sorted(by_type.items()):
            acc = sum(vals) / len(vals) * 100
            print(f"    {atype:>12s}: {sum(vals)}/{len(vals)} ({acc:.1f}%)")

    print(f"\nResults saved to: {output_dir}/")
    return summary_df


# ── Main: run on both datasets ──────────────────────────────────────────────

def main():
    cfg = BenchmarkConfig()

    # Cost tracking (approximate $/1M tokens on OpenRouter)
    COST_PER_1M = {
        "google/gemini-3.1-pro-preview": 2.50,
        "anthropic/claude-sonnet-4.6": 9.00,
        "openai/o3-mini": 1.10,
        "google/gemini-2.5-flash": 0.30,
    }

    all_summaries = {}

    for ds_info in DATASETS:
        summary = run_single_benchmark(ds_info, cfg)
        all_summaries[ds_info["name"]] = summary

    # ── Final combined summary ───────────────────────────────────────────
    print(f"\n{'='*80}")
    print(f"FINAL SUMMARY ACROSS ALL DATASETS")
    print(f"{'='*80}")

    for ds_name, summary in all_summaries.items():
        print(f"\n  {ds_name}:")
        for _, row in summary.sort_values("Accuracy (%)", ascending=False).iterrows():
            print(f"    {row['Model']:>35s}:  {row['Correct']}/{row['Total']}  ({row['Accuracy (%)']:.1f}%)")

    # ── Cost estimate ────────────────────────────────────────────────────
    total_cost = 0.0
    print(f"\nEstimated costs (combined):")
    for model, tokens in token_usage.items():
        cpm = COST_PER_1M.get(model, 5.0)
        cost = tokens / 1_000_000 * cpm
        total_cost += cost
        print(f"  {model.split('/')[-1]:>35s}: {tokens:>10,} tokens  ~${cost:.2f}")
    print(f"  {'TOTAL':>35s}: ~${total_cost:.2f}")

    # Save combined summary
    combined_path = Path(cfg.output_base) / "combined_summary.csv"
    frames = []
    for ds_name, summary in all_summaries.items():
        s = summary.copy()
        s.insert(0, "Dataset", ds_name)
        frames.append(s)
    pd.concat(frames).to_csv(combined_path, index=False)
    print(f"\nCombined summary saved to: {combined_path}")


if __name__ == "__main__":
    main()
