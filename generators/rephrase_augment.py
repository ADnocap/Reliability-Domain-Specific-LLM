"""Paraphrase augmentation for reliability engineering Q&A dataset.

Rephrases questions and reasoning using Claude Opus 4.6, then verifies
meaning preservation with GPT-5.4. Based on MetaMath/PersonaMath research:
few-shot prompting with explicit preservation constraints.

Usage:
    # Pilot: rephrase 5 samples and verify
    python generators/rephrase_augment.py --pilot 5

    # Hard generated only, 2 paraphrases each
    python generators/rephrase_augment.py --all --source hard_generated --num-paraphrases 2 --workers 3

    # Seed questions, 1 paraphrase, cap at 90 samples
    python generators/rephrase_augment.py --all --source seed --num-paraphrases 1 --max-samples 90 --workers 3
"""

import json
import os
import re
import sys
import time
import argparse
import random
import concurrent.futures
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Unbuffered stdout for real-time progress, with safe encoding for Windows
sys.stdout.reconfigure(line_buffering=True, errors='replace')

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
REPHRASE_MODEL = "anthropic/claude-opus-4-6"
VERIFY_MODEL = "openai/gpt-5.4"
REPHRASE_TEMPERATURE = 0.7
VERIFY_TEMPERATURE = 0.1
MAX_TOKENS_REPHRASE = 8000
MAX_TOKENS_VERIFY = 2000

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "data" / "master_dataset_v2.jsonl"
OUTPUT_PATH = PROJECT_ROOT / "data" / "rephrased_augmented.jsonl"
PILOT_OUTPUT_PATH = PROJECT_ROOT / "data" / "rephrased_pilot.jsonl"

# ---------------------------------------------------------------------------
# Few-shot examples (manually crafted to anchor quality)
# ---------------------------------------------------------------------------
FEW_SHOT_EXAMPLES = [
    {
        "original_question": "What is the minimum sample size that will allow us to verify a 500,000-hour MTTF with 85% confidence, given that the test can run for 2500 hours?",
        "original_reasoning": "For a zero-failure reliability demonstration test, we use the relationship: n \u2265 -ln(\u03b1) / (\u03bb_obj \u00b7 T), where \u03b1 is the producer's risk (1 - confidence level), \u03bb_obj is the objective failure rate, and T is the test duration per unit.\n\nGiven:\n- MTTF_obj = 500,000 hours\n- Confidence = 85%, so \u03b1 = 1 - 0.85 = 0.15\n- T = 2,500 hours\n\nCalculate objective failure rate:\n\u03bb_obj = 1/MTTF_obj = 1/500,000 = 2 \u00d7 10^(-6) failures/hour\n\nCalculate -ln(\u03b1):\n-ln(0.15) = 1.897\n\nCalculate the denominator:\n\u03bb_obj \u00b7 T = (2 \u00d7 10^(-6)) \u00d7 2,500 = 0.005\n\nCalculate n:\nn \u2265 1.897 / 0.005 = 379.4\n\nSince we cannot test a fractional number of units, we round up to n_min = 380 units.\n\nVerification: Total test time = 380 \u00d7 2,500 = 950,000 unit-hours. P(0 failures | \u03bb = \u03bb_obj) = e^(-1.9) \u2248 0.15 = \u03b1, confirming 85% confidence.",
        "rephrased_question": "A reliability demonstration test allows each unit to be tested for up to 2500 hours. Determine the smallest number of units required to demonstrate a mean time to failure of 500,000 hours at the 85% confidence level.",
        "rephrased_reasoning": "This is a zero-failure demonstration test. The governing formula is n \u2265 -ln(\u03b1) / (\u03bb_obj \u00b7 T), with \u03b1 representing the producer's risk, \u03bb_obj the target failure rate, and T the per-unit test duration.\n\nParameters:\n- Target MTTF = 500,000 hours \u2192 \u03bb_obj = 1/500,000 = 2 \u00d7 10^(-6) per hour\n- Confidence = 85% \u2192 \u03b1 = 0.15\n- Per-unit test time T = 2,500 hours\n\nComputing the numerator: -ln(0.15) = 1.897\n\nComputing the denominator: \u03bb_obj \u00b7 T = (2 \u00d7 10^(-6))(2,500) = 0.005\n\nTherefore: n \u2265 1.897 / 0.005 = 379.4\n\nRounding up (since partial units are impossible): n_min = 380.\n\nCross-check: 380 \u00d7 2,500 = 950,000 total unit-hours. The probability of zero failures at the target rate is e^(-1.9) \u2248 0.15, which equals \u03b1, confirming the 85% confidence level.",
    },
    {
        "original_question": "Three assembly plants produce the same parts. Plant A produces 25% of the volume and has a shipment defect rate of 1%. Plant B produces 30% of the volume and ships 1.2% defectives. Plant C produces the remainder and ships 0.6% defectives. Given that a component picked at random from the warehouse stocked by these plants is defective, what is the probability that it was manufactured by plant A?",
        "original_reasoning": "Using Bayes' Theorem to find P(A|D).\n\nGiven:\n- P(A) = 0.25, P(D|A) = 0.01\n- P(B) = 0.30, P(D|B) = 0.012\n- P(C) = 0.45, P(D|C) = 0.006\n\nFirst, calculate total probability of defect using Law of Total Probability:\nP(D) = P(D|A)\u00b7P(A) + P(D|B)\u00b7P(B) + P(D|C)\u00b7P(C)\nP(D) = 0.01\u00d70.25 + 0.012\u00d70.30 + 0.006\u00d70.45\nP(D) = 0.0025 + 0.0036 + 0.0027 = 0.0088\n\nApply Bayes' Theorem:\nP(A|D) = P(D|A)\u00b7P(A) / P(D) = 0.0025 / 0.0088 = 25/88 \u2248 0.2841",
        "rephrased_question": "A warehouse receives identical components from three factories. Factory A accounts for 25% of the supply and has a 1% defect rate, Factory B accounts for 30% with a 1.2% defect rate, and Factory C provides the rest with a 0.6% defect rate. A component chosen at random is found to be defective. What is the probability that it came from Factory A?",
        "rephrased_reasoning": "We need P(A|D), which calls for Bayes' Theorem.\n\nKnown values:\n- P(A) = 0.25 with P(D|A) = 0.01\n- P(B) = 0.30 with P(D|B) = 0.012\n- P(C) = 1 - 0.25 - 0.30 = 0.45 with P(D|C) = 0.006\n\nBy the Law of Total Probability, the overall defect rate is:\nP(D) = (0.01)(0.25) + (0.012)(0.30) + (0.006)(0.45)\nP(D) = 0.0025 + 0.0036 + 0.0027 = 0.0088\n\nApplying Bayes' Theorem:\nP(A|D) = P(D|A) \u00b7 P(A) / P(D) = 0.0025 / 0.0088 = 25/88 \u2248 0.2841",
    },
]

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------
REPHRASE_PROMPT = """You are a technical writer specializing in reliability engineering. Your task is to rephrase a question and its solution reasoning while preserving their exact mathematical meaning.

STRICT RULES:
1. ALL numerical values, failure rates, probabilities, time periods, and parameters must remain EXACTLY the same
2. ALL formulas, equations, and mathematical relationships must be preserved
3. The correct answer must be IDENTICAL — do not change, round, or reformat any numbers
4. Change the wording, sentence structure, and phrasing to create a distinct version
5. Do NOT add any information, assumptions, or conditions not present in the original
6. Do NOT remove any constraints, conditions, or given values from the original
7. Minor restructuring of the reasoning steps is allowed, but every calculation step and intermediate result must be preserved
8. If the original uses LaTeX notation (e.g., $F(t)$, \\frac{{}}{{}}), keep equivalent LaTeX in the rephrasing
9. Keep approximately the same level of detail — do not significantly expand or compress

WHAT TO CHANGE:
- Synonyms for non-technical words (e.g., "compute" → "determine", "find" → "calculate")
- Sentence structure and ordering of clauses
- How the scenario is framed (e.g., "plant" → "factory", "component" → "part")
- Transition words and connecting phrases in the reasoning
- Minor reordering of reasoning steps (as long as logical flow is preserved)

WHAT MUST NOT CHANGE:
- Any number, rate, probability, or parameter value
- Variable names in formulas (λ, α, n, t, etc.)
- The mathematical operations and formulas used
- The final answer
- The number of calculation steps (do not skip or add steps)

Here are examples of good rephrasings:

{few_shot}

Now rephrase the following:

ORIGINAL QUESTION:
{question}

ORIGINAL REASONING:
{reasoning}

ANSWER (do not change): {answer}

Respond with ONLY a JSON object (no markdown fences, no extra text):
{{"question": "your rephrased question", "reasoning": "your rephrased reasoning"}}"""

VERIFY_PROMPT = """You are verifying whether a rephrased reliability engineering question preserves the exact mathematical meaning of the original.

Compare the ORIGINAL and REPHRASED versions below. Check ALL of the following:

1. NUMERICAL VALUES: Are ALL numbers, rates, probabilities, percentages, and time periods EXACTLY the same in both versions?
2. MATHEMATICAL MEANING: Do both questions ask for the EXACT same quantity to be computed?
3. CONSTRAINTS: Are ALL conditions, assumptions, and given information preserved?
4. SOLUTION: Would the EXACT same calculation steps produce the correct answer for both versions?
5. REASONING: Are ALL formulas, equations, and intermediate values identical in the reasoning?

ORIGINAL:
Question: {original_question}
Reasoning: {original_reasoning}
Answer: {answer}

REPHRASED:
Question: {rephrased_question}
Reasoning: {rephrased_reasoning}

Respond with ONLY a JSON object (no markdown fences, no extra text):
{{"values_preserved": true/false, "meaning_preserved": true/false, "constraints_preserved": true/false, "solution_equivalent": true/false, "reasoning_equivalent": true/false, "overall_valid": true/false, "issues": "description of any issues found, or 'none'"}}"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def create_client():
    api_key = os.environ.get("NEW_KEY")
    if not api_key:
        print("ERROR: NEW_KEY not set in .env")
        sys.exit(1)
    return OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)


def build_few_shot_text():
    parts = []
    for i, ex in enumerate(FEW_SHOT_EXAMPLES, 1):
        parts.append(f"""--- Example {i} ---

ORIGINAL QUESTION:
{ex['original_question']}

ORIGINAL REASONING:
{ex['original_reasoning']}

REPHRASED QUESTION:
{ex['rephrased_question']}

REPHRASED REASONING:
{ex['rephrased_reasoning']}""")
    return "\n\n".join(parts)


def parse_json_response(text: str) -> dict | None:
    """Extract JSON from a model response, handling markdown fences."""
    # Try raw parse first
    text = text.strip()
    # Remove markdown code fences if present
    text = re.sub(r'^```(?:json)?\s*\n?', '', text)
    text = re.sub(r'\n?```\s*$', '', text)
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Try to find JSON object in the text
        match = re.search(r'\{[\s\S]*\}', text)
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                pass
    return None


def extract_key_numbers(text: str) -> set[str]:
    """Extract key numerical values — decimals and numbers with 3+ digits.

    Skips small integers (< 100) which the rephrase model often writes
    as words (e.g., "ten" instead of "10"). The LLM verifier catches
    any real meaning changes.
    """
    raw = re.findall(r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?', text)
    key = set()
    for n in raw:
        clean = n.lstrip('+-')
        # Keep decimals (contain '.'), scientific notation, or numbers >= 100
        if '.' in clean or 'e' in clean.lower():
            key.add(n)
        else:
            try:
                if abs(int(clean)) >= 100:
                    key.add(n)
            except ValueError:
                pass
    return key


def validate_numbers_preserved(original_q: str, rephrased_q: str,
                                original_r: str, rephrased_r: str) -> tuple[bool, str]:
    """Check that key numerical values from original question appear in rephrased.

    Only checks decimals and large numbers (>=100) in the question.
    Small integers are often written as words by the rephraser.
    The GPT verifier is the real quality gate for meaning preservation.
    """
    orig_q_nums = extract_key_numbers(original_q)
    repr_q_nums = extract_key_numbers(rephrased_q)
    missing_q = orig_q_nums - repr_q_nums
    if missing_q:
        return False, f"Question missing numbers: {missing_q}"

    return True, "question numbers preserved"


# ---------------------------------------------------------------------------
# Core pipeline
# ---------------------------------------------------------------------------
def rephrase_one(client, item: dict, few_shot_text: str,
                 attempt: int = 0) -> dict | None:
    """Rephrase a single Q&A pair using the rephrase model."""
    prompt = REPHRASE_PROMPT.format(
        few_shot=few_shot_text,
        question=item["question"],
        reasoning=item["reasoning"],
        answer=item["answer"],
    )
    try:
        resp = client.chat.completions.create(
            model=REPHRASE_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=REPHRASE_TEMPERATURE,
            max_tokens=MAX_TOKENS_REPHRASE,
        )
        result = parse_json_response(resp.choices[0].message.content)
        if not result or "question" not in result or "reasoning" not in result:
            if attempt < 1:
                time.sleep(2)
                return rephrase_one(client, item, few_shot_text, attempt + 1)
            return None

        # Local validation: check all numbers preserved
        ok, msg = validate_numbers_preserved(
            item["question"], result["question"],
            item["reasoning"], result["reasoning"],
        )
        if not ok:
            print(f"    LOCAL FAIL: {msg}")
            if attempt < 1:
                time.sleep(2)
                return rephrase_one(client, item, few_shot_text, attempt + 1)
            return None

        return result
    except Exception as e:
        print(f"    API error: {e}")
        if attempt < 2:
            time.sleep(5)
            return rephrase_one(client, item, few_shot_text, attempt + 1)
        return None


def verify_one(client, original: dict, rephrased: dict) -> dict | None:
    """Verify meaning preservation using the verifier model."""
    prompt = VERIFY_PROMPT.format(
        original_question=original["question"],
        original_reasoning=original["reasoning"],
        answer=original["answer"],
        rephrased_question=rephrased["question"],
        rephrased_reasoning=rephrased["reasoning"],
    )
    try:
        resp = client.chat.completions.create(
            model=VERIFY_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=VERIFY_TEMPERATURE,
            max_tokens=MAX_TOKENS_VERIFY,
        )
        result = parse_json_response(resp.choices[0].message.content)
        return result
    except Exception as e:
        print(f"    Verify API error: {e}")
        return None


def process_one(client, item: dict, idx: int, few_shot_text: str,
                total: int) -> list[dict]:
    """Rephrase and verify a single item. Returns list of valid rephrased items."""
    q_preview = item["question"][:70]
    print(f"  [{idx+1}/{total}] {q_preview}...")

    rephrased = rephrase_one(client, item, few_shot_text)
    if not rephrased:
        print(f"    SKIP: failed to generate valid rephrase")
        return []

    # Verify with GPT-5.4
    verification = verify_one(client, item, rephrased)
    if not verification:
        print(f"    SKIP: verification API failed")
        return []

    if not verification.get("overall_valid", False):
        issues = verification.get("issues", "unknown")
        print(f"    REJECTED: {issues}")
        return []

    # Build output item
    result = {
        "question": rephrased["question"],
        "reasoning": rephrased["reasoning"],
        "answer": item["answer"],
        "answer_type": item.get("answer_type", "numeric"),
        "source": "rephrased",
        "original_index": item.get("original_index", idx),
    }
    print(f"    PASS")
    return [result]


def process_one_worker(args):
    """Worker wrapper for concurrent processing."""
    client, item, idx, few_shot_text, total = args
    return process_one(client, item, idx, few_shot_text, total)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Paraphrase augmentation for reliability Q&A dataset"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--pilot", type=int, metavar="N",
                       help="Pilot run: rephrase N random samples")
    group.add_argument("--all", action="store_true",
                       help="Full run: rephrase all samples")

    parser.add_argument("--num-paraphrases", type=int, default=1,
                        help="Number of paraphrases per question (default: 1)")
    parser.add_argument("--workers", type=int, default=1,
                        help="Number of concurrent workers (default: 1)")
    parser.add_argument("--source", type=str, default=None,
                        choices=["seed", "hard_generated", "cross_model_verified"],
                        help="Filter by source field (default: all)")
    parser.add_argument("--max-samples", type=int, default=None,
                        help="Max number of source samples to rephrase")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for sample selection")
    parser.add_argument("--append", action="store_true",
                        help="Append to existing output file instead of overwriting")
    args = parser.parse_args()

    random.seed(args.seed)

    # Load dataset
    data = []
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line.strip()))
    print(f"Loaded {len(data)} samples from {DATASET_PATH}")

    # Filter by source
    if args.source:
        data = [d for d in data if d.get("source") == args.source]
        print(f"Filtered to {len(data)} samples with source='{args.source}'")

    # Select samples
    if args.pilot:
        samples = random.sample(data, min(args.pilot, len(data)))
        output_path = PILOT_OUTPUT_PATH
        print(f"Pilot mode: rephrasing {len(samples)} random samples")
    else:
        samples = data
        if args.max_samples and len(samples) > args.max_samples:
            samples = random.sample(samples, args.max_samples)
            print(f"Capped to {len(samples)} random samples (--max-samples)")
        output_path = OUTPUT_PATH
        print(f"Full mode: rephrasing {len(samples)} samples")

    print(f"Rephrase model: {REPHRASE_MODEL}")
    print(f"Verify model:   {VERIFY_MODEL}")
    print(f"Paraphrases per question: {args.num_paraphrases}")
    print(f"Workers: {args.workers}")
    print(f"Output: {output_path}\n")

    client = create_client()
    few_shot_text = build_few_shot_text()

    n_attempted = 0
    n_accepted = 0
    write_lock = __import__('threading').Lock()

    # Initialize output file (clear if not appending)
    if not args.append:
        open(output_path, "w", encoding="utf-8").close()

    def save_result(item: dict):
        """Append a single result to the output file (thread-safe)."""
        with write_lock:
            with open(output_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")

    for para_round in range(args.num_paraphrases):
        if args.num_paraphrases > 1:
            print(f"\n{'='*60}")
            print(f"PARAPHRASE ROUND {para_round + 1}/{args.num_paraphrases}")
            print(f"{'='*60}\n")

        if args.workers > 1:
            worker_args = [
                (client, item, i, few_shot_text, len(samples))
                for i, item in enumerate(samples)
            ]
            with concurrent.futures.ThreadPoolExecutor(
                max_workers=args.workers
            ) as executor:
                futures = {
                    executor.submit(process_one_worker, wa): i
                    for i, wa in enumerate(worker_args)
                }
                for future in concurrent.futures.as_completed(futures):
                    results = future.result()
                    n_attempted += 1
                    if results:
                        n_accepted += len(results)
                        for item in results:
                            save_result(item)
        else:
            for i, item in enumerate(samples):
                results = process_one(client, item, i, few_shot_text, len(samples))
                n_attempted += 1
                if results:
                    n_accepted += len(results)
                    for item in results:
                        save_result(item)

    print(f"\n{'='*60}")
    print(f"DONE")
    print(f"{'='*60}")
    print(f"Attempted: {n_attempted}")
    print(f"Accepted:  {n_accepted} ({n_accepted/max(n_attempted,1)*100:.0f}%)")
    print(f"Output:    {output_path}")

    if args.pilot and all_results:
        print(f"\n--- PILOT REVIEW ---")
        print(f"Review the output at {output_path}")
        print(f"Compare original vs rephrased to verify quality before scaling.")
        print(f"\nSample comparison:")
        sample = all_results[0]
        orig = next(
            (d for d in data
             if d.get("original_index") == sample.get("original_index")),
            None,
        )
        if orig:
            print(f"\n  ORIGINAL Q: {orig['question'][:120]}...")
            print(f"  REPHRASED Q: {sample['question'][:120]}...")
            print(f"  ANSWER: {sample['answer']}")


if __name__ == "__main__":
    main()
