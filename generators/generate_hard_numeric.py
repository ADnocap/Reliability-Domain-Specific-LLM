"""Generate hard numeric-only reliability engineering questions.

Uses Claude Sonnet 4.5 for generation, Google Gemini 2.5 Flash for
independent verification. Only produces single-answer numeric questions.

Usage:
    python generators/generate_hard_numeric.py [--target 200]
"""

import json
import os
import re
import random
import sys
import time
import argparse
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
GENERATOR_MODEL = "anthropic/claude-opus-4.6"
VERIFIER_MODEL = "openai/gpt-5.4"
QUESTIONS_PER_BATCH = 2
NUM_SEED_EXAMPLES = 3
GEN_TEMPERATURE = 0.8
VERIFY_TEMPERATURE = 0.1
MAX_TOKENS_GEN = 16000
MAX_TOKENS_VERIFY = 8000
NUMERICAL_TOLERANCE = 0.05

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SEED_PATH = PROJECT_ROOT / "data" / "master_dataset_cleaned.jsonl"
OUTPUT_PATH = PROJECT_ROOT / "data" / "hard_numeric_generated.jsonl"

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------
GENERATION_PROMPT = """You are an expert reliability engineering professor creating CHALLENGING exam problems for graduate students.

I will show you {num_examples} example problems. Create {num_to_generate} NEW problems that are SIGNIFICANTLY HARDER and require DEEPER REASONING than the examples.

STRICT FORMAT REQUIREMENTS:
1. Each problem must be a SINGLE question with exactly ONE numeric answer
2. NO multi-part questions (no "a)", "b)", "also find", "additionally compute")
3. The question must be FULLY SELF-CONTAINED (all data included, no references to tables or figures)
4. The answer must be a PLAIN NUMBER with NO UNITS and NO COMMAS
   - Probabilities as decimals: 95% -> 0.95
   - No units: just "380" not "380 hours"
   - No commas: "12000" not "12,000"
   - Use reasonable precision (4-6 significant figures for decimals)

DIFFICULTY REQUIREMENTS — the problem MUST require at least TWO of:
- Combining multiple distributions (e.g., Weibull components in a k-out-of-n system)
- Conditional probability or Bayesian updating with prior information
- System-level analysis (series-parallel, standby redundancy, common cause failures)
- Parameter estimation from censored or incomplete data
- Competing risks or dependent failure modes
- Optimization under constraints (e.g., minimizing cost subject to reliability target)
- Renewal theory or availability calculations with repair
- Accelerated life testing with stress-life relationships

AVOID these (too easy):
- Single-formula plug-and-chug (e.g., "find R(t) for exponential with lambda=0.001")
- Direct table lookups
- Questions solvable in fewer than 3 calculation steps

# EXAMPLE PROBLEMS (for reference — make yours HARDER):

{examples}

# YOUR TASK:

Generate {num_to_generate} new problems. For each problem provide EXACTLY this format:

QUESTION: [Complete problem statement]

REASONING: [Complete step-by-step solution with all intermediate calculations]

ANSWER: [Single plain number, no units, no commas, percentages as decimals]

---

Generate the problems now:"""

VERIFICATION_PROMPT = """You are an expert in reliability engineering, statistics, and probability.

Solve this problem completely. Show all steps and calculations.

IMPORTANT: State your final answer as a SINGLE PLAIN NUMBER.
- No units, no commas
- Probabilities as decimals (not percentages)
- Round to 4 significant figures if needed

Problem:
{question}

Solve step by step, then state your final numerical answer:"""


# ---------------------------------------------------------------------------
# Answer standardization
# ---------------------------------------------------------------------------
def standardize_answer(answer: str) -> str:
    """Convert any answer format to a plain number string."""
    s = answer.strip()
    # Strip LaTeX
    s = re.sub(r'\$\\boxed\{(.*?)\}\$', r'\1', s)
    s = re.sub(r'\\boxed\{(.*?)\}', r'\1', s)
    s = re.sub(r'\$(.*?)\$', r'\1', s)
    s = re.sub(r'\\frac\{(\d+)\}\{(\d+)\}',
               lambda m: str(round(int(m.group(1)) / int(m.group(2)), 8)), s)
    # Remove commas between digits
    s = re.sub(r'(\d),(\d)', r'\1\2', s)
    # Convert percentage to decimal
    m_pct = re.match(r'^([-+]?\d*\.?\d+)\s*%$', s.strip())
    if m_pct:
        s = str(round(float(m_pct.group(1)) / 100, 8))
    # Strip common unit suffixes
    s = re.sub(
        r'\s*(hours?|hrs?|days?|years?|yrs?|failures?|units?|FITs?|cycles?'
        r'|per\s+\w+|million|thousand)\s*$', '', s, flags=re.IGNORECASE)
    # Strip surrounding whitespace and trailing periods
    s = s.strip().rstrip('.')
    # Evaluate simple fraction if present
    frac = re.match(r'^(-?\d+)/(\d+)$', s)
    if frac:
        s = str(round(int(frac.group(1)) / int(frac.group(2)), 8))
    return s


def extract_number(text: str) -> str | None:
    """Extract the final numerical answer from a model response."""
    # Try explicit answer patterns first
    patterns = [
        r'[Ff]inal\s+[Aa]nswer\s*[:\-]\s*([-+]?\d[\d,]*\.?\d*(?:[eE][-+]?\d+)?)',
        r'[Aa]nswer\s*[:\-]\s*([-+]?\d[\d,]*\.?\d*(?:[eE][-+]?\d+)?)',
        r'[Tt]he\s+answer\s+is\s*:?\s*([-+]?\d[\d,]*\.?\d*(?:[eE][-+]?\d+)?)',
        r'=\s*([-+]?\d[\d,]*\.?\d*(?:[eE][-+]?\d+)?)\s*$',
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.MULTILINE)
        if match:
            return match.group(1)
    # Fallback: last number in the response
    numbers = re.findall(r'[-+]?\d[\d,]*\.?\d*(?:[eE][-+]?\d+)?', text)
    return numbers[-1] if numbers else None


def answers_match(ans1: str, ans2: str) -> bool:
    """Check if two answers match within tolerance."""
    a1 = standardize_answer(ans1)
    a2 = standardize_answer(ans2)
    if a1 == a2:
        return True
    try:
        v1, v2 = float(a1), float(a2)
        denom = max(abs(v1), abs(v2), 1e-10)
        return abs(v1 - v2) / denom < NUMERICAL_TOLERANCE
    except ValueError:
        return False


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------
def parse_generated(text: str) -> list[dict]:
    """Parse QUESTION/REASONING/ANSWER blocks from generator output."""
    results = []
    # Split on QUESTION: (with optional markdown bold/heading)
    blocks = re.split(r'(?:^|\n)\s*(?:\*\*)?(?:#{0,3}\s*)?QUESTION\s*(?:\*\*)?:\s*', text, flags=re.IGNORECASE)
    for block in blocks[1:]:
        # Match REASONING and ANSWER with flexible formatting
        r_match = re.search(
            r'(?:\*\*)?(?:#{0,3}\s*)?REASONING\s*(?:\*\*)?:\s*(.*?)(?=\n\s*(?:\*\*)?(?:#{0,3}\s*)?ANSWER)',
            block, re.DOTALL | re.IGNORECASE)
        a_match = re.search(
            r'(?:\*\*)?(?:#{0,3}\s*)?ANSWER\s*(?:\*\*)?:\s*(.*?)(?:\n---|\n\n\n|\Z)',
            block, re.DOTALL | re.IGNORECASE)
        q_match = re.match(
            r'(.*?)(?=\n\s*(?:\*\*)?(?:#{0,3}\s*)?REASONING)',
            block, re.DOTALL | re.IGNORECASE)
        if not (q_match and r_match and a_match):
            continue
        question = q_match.group(1).strip()
        reasoning = r_match.group(1).strip()
        answer = a_match.group(1).strip().split('\n')[0].strip()
        # Quality gates
        if len(question) < 50 or len(reasoning) < 50:
            continue
        if any(p in question.lower() for p in ['[insert', 'tbd', 'xxx', '???']):
            continue
        # Reject multi-part
        if re.search(r'\b[a-d]\)\s', question) or 'also find' in question.lower():
            continue
        answer = standardize_answer(answer)
        # Must be parseable as a number
        try:
            float(answer)
        except ValueError:
            continue
        results.append({
            'question': question,
            'reasoning': reasoning,
            'answer': answer,
            'answer_type': 'numeric',
            'source': 'hard_generated',
        })
    return results


# ---------------------------------------------------------------------------
# API calls
# ---------------------------------------------------------------------------
def create_client():
    api_key = os.environ.get("OPENROUTER_API_KEY_PROF")
    if not api_key:
        print("ERROR: OPENROUTER_API_KEY_PROF not set")
        sys.exit(1)
    return OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)


def generate_batch(client, seed_data, existing_prefixes):
    """Generate a batch of questions from seed examples."""
    examples = random.sample(seed_data, min(NUM_SEED_EXAMPLES, len(seed_data)))
    examples_text = "\n".join(
        f"Example {i+1}:\nQUESTION: {ex['question']}\n"
        f"REASONING: {ex['reasoning']}\nANSWER: {ex['answer']}\n"
        for i, ex in enumerate(examples)
    )
    prompt = GENERATION_PROMPT.format(
        num_examples=len(examples),
        num_to_generate=QUESTIONS_PER_BATCH,
        examples=examples_text,
    )
    resp = client.chat.completions.create(
        model=GENERATOR_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=GEN_TEMPERATURE,
        max_tokens=MAX_TOKENS_GEN,
    )
    items = parse_generated(resp.choices[0].message.content)
    # Deduplicate
    new = []
    for item in items:
        prefix = item['question'][:200].lower()
        if prefix not in existing_prefixes:
            existing_prefixes.add(prefix)
            new.append(item)
    return new


def verify_question(client, item):
    """Have a different model independently solve the question."""
    prompt = VERIFICATION_PROMPT.format(question=item['question'])
    resp = client.chat.completions.create(
        model=VERIFIER_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=VERIFY_TEMPERATURE,
        max_tokens=MAX_TOKENS_VERIFY,
    )
    verifier_text = resp.choices[0].message.content
    verifier_answer = extract_number(verifier_text)
    if verifier_answer and answers_match(item['answer'], verifier_answer):
        return True, verifier_answer
    return False, verifier_answer


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', type=int, default=200,
                        help='Target number of verified questions')
    args = parser.parse_args()

    print(f"=== Hard Numeric Question Generator ===")
    print(f"Generator: {GENERATOR_MODEL}")
    print(f"Verifier:  {VERIFIER_MODEL}")
    print(f"Target:    {args.target} verified questions\n")

    # Load seed data (numeric only)
    seed_data = []
    with open(SEED_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            item = json.loads(line.strip())
            if item.get('answer_type') == 'numeric':
                seed_data.append(item)
    print(f"Loaded {len(seed_data)} numeric seed examples")

    # Track existing questions
    existing_prefixes = set()
    for item in seed_data:
        existing_prefixes.add(item['question'][:200].lower())

    # Resume from existing output
    verified = []
    if OUTPUT_PATH.exists():
        with open(OUTPUT_PATH, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    item = json.loads(line.strip())
                    verified.append(item)
                    existing_prefixes.add(item['question'][:200].lower())
        print(f"Resuming from {len(verified)} existing questions")

    client = create_client()
    batch_num = 0
    total_gen = 0
    total_checked = 0

    while len(verified) < args.target:
        batch_num += 1
        print(f"\nBatch {batch_num} | verified: {len(verified)}/{args.target}")

        items = generate_batch(client, seed_data, existing_prefixes)
        total_gen += len(items)
        if not items:
            print("  No valid items, retrying...")
            continue

        for item in items:
            total_checked += 1
            matched, ver_ans = verify_question(client, item)
            if matched:
                verified.append(item)
                with open(OUTPUT_PATH, 'a', encoding='utf-8') as f:
                    f.write(json.dumps(item, ensure_ascii=False) + '\n')
                q_preview = item['question'][:70].encode('ascii', 'replace').decode()
                print(f"  PASS ({len(verified)}/{args.target}): "
                      f"{q_preview}... = {item['answer']}")
            else:
                gen_a = item['answer']
                ver_a = standardize_answer(ver_ans) if ver_ans else 'N/A'
                q_preview = item['question'][:60].encode('ascii', 'replace').decode()
                print(f"  FAIL: gen={gen_a} ver={ver_a} | {q_preview}...")

        rate = len(verified) / max(total_checked, 1) * 100
        print(f"  Accept rate: {rate:.0f}%")
        if batch_num > 30 and rate < 10:
            print("Accept rate too low, stopping.")
            break

    print(f"\n=== Generation Done ===")
    print(f"Generated: {total_gen} | Verified: {len(verified)} | "
          f"Rate: {len(verified)/max(total_gen,1)*100:.0f}%")
    print(f"Output: {OUTPUT_PATH}")

    # Merge with existing numeric data
    merged_path = PROJECT_ROOT / "data" / "master_dataset_v2.jsonl"
    existing_numeric = []
    with open(SEED_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            item = json.loads(line.strip())
            if item.get('answer_type') == 'numeric':
                existing_numeric.append(item)

    merged = existing_numeric + verified
    with open(merged_path, 'w', encoding='utf-8') as f:
        for item in merged:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')

    print(f"\n=== Merged Dataset ===")
    print(f"Existing numeric: {len(existing_numeric)}")
    print(f"New hard questions: {len(verified)}")
    print(f"Total: {len(merged)}")
    print(f"Saved to: {merged_path}")


if __name__ == "__main__":
    main()
