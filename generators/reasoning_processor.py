"""
Reasoning Processor for Reliability Textbook Questions
Uses OpenRouter API to regenerate reasoning for JSONL data.

Process:
1. For each question, ask the model to solve WITHOUT seeing the answer
2. Compare the model's answer with the expected answer
3. If correct: use the model's reasoning
4. If incorrect: mark reasoning as "REASONING_FAILED: Model answer did not match expected"
"""

import json
import os
import re
import sys
import time
import argparse
import logging
from typing import Optional
import requests
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils.data_io import load_dataset, save_dataset

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# OpenRouter API Configuration
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Best models for reasoning tasks (in order of recommendation)
RECOMMENDED_MODELS = {
    "claude-sonnet-4.5": "anthropic/claude-sonnet-4.5",
    "claude-opus-4.5": "anthropic/claude-opus-4.5",
    "gemini-2.5-pro": "google/gemini-2.5-pro",
    "gpt-5.2": "openai/gpt-5.2",
    "deepseek-v3": "deepseek/deepseek-chat",
    "gemini-2.5-flash": "google/gemini-2.5-flash",
}

# Default model - Claude Sonnet 4.5 is excellent for reasoning
DEFAULT_MODEL = "anthropic/claude-opus-4.5"


def load_items(file_path: str) -> list:
    """Load items from either JSON or JSONL file (auto-detected)."""
    items = load_dataset(file_path)
    fmt = 'JSONL' if Path(file_path).suffix == '.jsonl' else 'JSON'
    logger.info(f"Detected input format: {fmt}")
    return items


def save_items(items: list, file_path: str, output_format: str = 'json'):
    """Save items to either JSON or JSONL file."""
    save_dataset(items, file_path, fmt=output_format)


def create_solving_prompt(question: str) -> str:
    """Create a prompt that asks the model to solve the problem step by step."""
    return f"""You are an expert in reliability engineering, statistics, and probability theory.

Solve the following problem step by step. Show your complete reasoning and calculations.

**IMPORTANT**: 
- Work through the problem methodically
- Show all formulas used
- Show all calculations
- State your final answer clearly at the end

**Problem:**
{question}

**Your Solution:**
"""


def create_verification_prompt(question: str, expected_answer: str, model_solution: str) -> str:
    """Create a prompt to verify if the model's answer matches the expected answer."""
    return f"""Compare the following two answers to determine if they are essentially the same (allowing for minor differences in notation, rounding, or phrasing).

**Original Question:**
{question}

**Expected Answer:**
{expected_answer}

**Model's Solution:**
{model_solution}

**Instructions:**
1. Extract the final numerical answer or conclusion from the model's solution
2. Compare it with the expected answer
3. Consider answers as matching if:
   - Numerical values are within 5% of each other
   - The core conclusion/concept is the same
   - Minor notation differences are acceptable

**Response Format:**
Respond with ONLY one of these two words:
- "MATCH" if the answers are essentially the same
- "MISMATCH" if the answers are different

Your response:"""


def call_openrouter_api(
    api_key: str,
    messages: list,
    model: str = DEFAULT_MODEL,
    temperature: float = 0.1,
    max_tokens: int = 4096,
    max_retries: int = 3,
    retry_delay: float = 2.0
) -> Optional[str]:
    """
    Call the OpenRouter API with retry logic.
    
    Args:
        api_key: OpenRouter API key
        messages: List of message dicts with 'role' and 'content'
        model: Model identifier (e.g., "anthropic/claude-sonnet-4.5")
        temperature: Sampling temperature (lower = more deterministic)
        max_tokens: Maximum tokens in response
        max_retries: Number of retry attempts
        retry_delay: Delay between retries in seconds
    
    Returns:
        Response content string or None if failed
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/reasoning-processor",
        "X-Title": "Reasoning Processor"
    }
    
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.post(
                OPENROUTER_API_URL,
                headers=headers,
                json=payload,
                timeout=120  # 2 minute timeout for complex reasoning
            )
            
            if response.status_code == 200:
                data = response.json()
                if "choices" in data and len(data["choices"]) > 0:
                    return data["choices"][0]["message"]["content"]
                else:
                    logger.error(f"Unexpected response format: {data}")
                    return None
            
            elif response.status_code == 429:  # Rate limited
                wait_time = retry_delay * (2 ** attempt)
                logger.warning(f"Rate limited. Waiting {wait_time}s before retry...")
                time.sleep(wait_time)
                continue
                
            elif response.status_code >= 500:  # Server error
                wait_time = retry_delay * (2 ** attempt)
                logger.warning(f"Server error {response.status_code}. Waiting {wait_time}s...")
                time.sleep(wait_time)
                continue
                
            else:
                logger.error(f"API error {response.status_code}: {response.text}")
                return None
                
        except requests.exceptions.Timeout:
            logger.warning(f"Request timeout on attempt {attempt + 1}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            return None
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error: {e}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            return None
    
    return None


def solve_and_verify(
    api_key: str,
    question: str,
    expected_answer: str,
    model: str = DEFAULT_MODEL
) -> tuple[str, bool]:
    """
    Have the model solve a problem and verify the answer.
    
    Args:
        api_key: OpenRouter API key
        question: The problem to solve
        expected_answer: The expected answer to compare against
        model: Model to use
    
    Returns:
        Tuple of (reasoning_text, is_correct)
    """
    # Step 1: Have the model solve the problem
    solve_prompt = create_solving_prompt(question)
    messages = [{"role": "user", "content": solve_prompt}]
    
    logger.info("Requesting model to solve the problem...")
    model_solution = call_openrouter_api(api_key, messages, model)
    
    if model_solution is None:
        return "REASONING_FAILED: API call failed during solving", False
    
    # Small delay to avoid rate limiting
    time.sleep(0.5)
    
    # Step 2: Verify if the answer matches
    verify_prompt = create_verification_prompt(question, expected_answer, model_solution)
    verify_messages = [{"role": "user", "content": verify_prompt}]
    
    logger.info("Verifying answer...")
    verification = call_openrouter_api(
        api_key, 
        verify_messages, 
        model,
        temperature=0.0,  # Very deterministic for verification
        max_tokens=50
    )
    
    if verification is None:
        # If verification fails, assume mismatch to be safe
        return f"REASONING_FAILED: Verification API call failed\n\nModel's attempted solution:\n{model_solution}", False
    
    # Check verification result
    verification_clean = verification.strip().upper()
    is_correct = "MATCH" in verification_clean and "MISMATCH" not in verification_clean
    
    if is_correct:
        return model_solution, True
    else:
        return f"REASONING_FAILED: Model answer did not match expected answer '{expected_answer}'\n\nModel's attempted solution:\n{model_solution}", False


def process_file(
    input_path: str,
    output_path: str,
    api_key: str,
    model: str = DEFAULT_MODEL,
    output_format: str = 'json',
    skip_existing: bool = True,
    delay_between_items: float = 1.0
) -> dict:
    """
    Process a JSON or JSONL file and regenerate reasoning for each question.
    
    Args:
        input_path: Path to input file (JSON or JSONL)
        output_path: Path to output file
        api_key: OpenRouter API key
        model: Model to use
        output_format: Output format ('json' or 'jsonl')
        skip_existing: Skip items that already have valid reasoning
        delay_between_items: Delay between processing items (to avoid rate limits)
    
    Returns:
        Statistics dict with counts of processed, successful, failed items
    """
    stats = {
        "total": 0,
        "processed": 0,
        "successful": 0,
        "failed": 0,
        "skipped": 0
    }
    
    # Load items (auto-detects format)
    items = load_items(input_path)
    
    stats["total"] = len(items)
    logger.info(f"Loaded {len(items)} items from {input_path}")
    logger.info(f"Output format: {output_format.upper()}")
    
    # Process each item
    processed_items = []
    for i, item in enumerate(items):
        logger.info(f"\n{'='*60}")
        logger.info(f"Processing item {i+1}/{len(items)}: {item.get('title', 'Untitled')}")
        
        question = item.get("question", "")
        answer = item.get("answer", "")
        current_reasoning = item.get("reasoning", "")
        
        if not question or not answer:
            logger.warning("Skipping item with missing question or answer")
            processed_items.append(item)
            stats["skipped"] += 1
            continue
        
        # Skip if reasoning already exists and looks valid (optional)
        if skip_existing and current_reasoning and not current_reasoning.startswith("REASONING_FAILED"):
            # Check if reasoning seems substantive (more than 100 chars)
            if len(current_reasoning) > 100:
                logger.info("Skipping - existing reasoning appears valid")
                processed_items.append(item)
                stats["skipped"] += 1
                continue
        
        # Process this item
        stats["processed"] += 1
        
        try:
            new_reasoning, is_correct = solve_and_verify(
                api_key=api_key,
                question=question,
                expected_answer=answer,
                model=model
            )
            
            item["reasoning"] = new_reasoning
            
            if is_correct:
                stats["successful"] += 1
                logger.info("✓ Successfully regenerated reasoning")
            else:
                stats["failed"] += 1
                logger.warning("✗ Model answer did not match expected")
                
        except Exception as e:
            logger.error(f"Error processing item: {e}")
            item["reasoning"] = f"REASONING_FAILED: Processing error - {str(e)}"
            stats["failed"] += 1
        
        processed_items.append(item)
        
        # Save progress after each item (in case of interruption)
        save_items(processed_items, output_path, output_format)
        
        # Delay between items to avoid rate limiting
        if i < len(items) - 1:
            time.sleep(delay_between_items)
    
    logger.info(f"\n{'='*60}")
    logger.info("Processing complete!")
    logger.info(f"Total items: {stats['total']}")
    logger.info(f"Processed: {stats['processed']}")
    logger.info(f"Successful: {stats['successful']}")
    logger.info(f"Failed: {stats['failed']}")
    logger.info(f"Skipped: {stats['skipped']}")
    logger.info(f"Output saved to: {output_path}")
    
    return stats


def list_available_models():
    """Print available recommended models."""
    print("\nRecommended models for reasoning tasks:")
    print("-" * 50)
    for short_name, full_name in RECOMMENDED_MODELS.items():
        default_marker = " (DEFAULT)" if full_name == DEFAULT_MODEL else ""
        print(f"  {short_name:20} -> {full_name}{default_marker}")
    print("\nYou can also use any model available on OpenRouter.")
    print("See https://openrouter.ai/models for the full list.")


def main():
    parser = argparse.ArgumentParser(
        description="Regenerate reasoning for reliability textbook questions using OpenRouter API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage with default model (Claude Sonnet 4.5) - outputs JSON by default
  python reasoning_processor.py input.jsonl output.json --api-key YOUR_KEY
  
  # Input can be JSON or JSONL (auto-detected)
  python reasoning_processor.py input.json output.json --api-key YOUR_KEY
  
  # Output as JSONL instead of JSON
  python reasoning_processor.py input.json output.jsonl --api-key YOUR_KEY --output-format jsonl
  
  # Use a specific model
  python reasoning_processor.py input.jsonl output.json --api-key YOUR_KEY --model google/gemini-2.5-pro
  
  # Process all items (don't skip existing reasoning)
  python reasoning_processor.py input.jsonl output.json --api-key YOUR_KEY --no-skip
  
  # List available models
  python reasoning_processor.py --list-models
        """
    )
    
    parser.add_argument("input_file", nargs="?", help="Input file path (JSON or JSONL, auto-detected)")
    parser.add_argument("output_file", nargs="?", help="Output file path")
    parser.add_argument("--api-key", "-k", help="OpenRouter API key (or set OPENROUTER_API_KEY env var)")
    parser.add_argument("--model", "-m", default=DEFAULT_MODEL, 
                        help=f"Model to use (default: {DEFAULT_MODEL})")
    parser.add_argument("--output-format", "-f", choices=['json', 'jsonl'], default='json',
                        help="Output format: 'json' (default) or 'jsonl'")
    parser.add_argument("--no-skip", action="store_true",
                        help="Process all items, don't skip existing valid reasoning")
    parser.add_argument("--delay", "-d", type=float, default=1.0,
                        help="Delay between items in seconds (default: 1.0)")
    parser.add_argument("--list-models", "-l", action="store_true",
                        help="List recommended models and exit")
    
    args = parser.parse_args()
    
    if args.list_models:
        list_available_models()
        return
    
    if not args.input_file or not args.output_file:
        parser.print_help()
        return
    
    # Get API key
    api_key = args.api_key or os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OpenRouter API key required.")
        print("Provide via --api-key argument or OPENROUTER_API_KEY environment variable.")
        print("\nTo get an API key:")
        print("1. Go to https://openrouter.ai")
        print("2. Create an account")
        print("3. Go to API Keys section and generate a new key")
        return
    
    # Validate input file
    if not Path(args.input_file).exists():
        print(f"Error: Input file not found: {args.input_file}")
        return
    
    # Resolve model name if short name provided
    model = RECOMMENDED_MODELS.get(args.model, args.model)
    
    logger.info(f"Using model: {model}")
    logger.info(f"Input file: {args.input_file}")
    logger.info(f"Output file: {args.output_file}")
    logger.info(f"Output format: {args.output_format.upper()}")
    logger.info(f"Skip existing: {not args.no_skip}")
    
    # Process the file
    process_file(
        input_path=args.input_file,
        output_path=args.output_file,
        api_key=api_key,
        model=model,
        output_format=args.output_format,
        skip_existing=not args.no_skip,
        delay_between_items=args.delay
    )


if __name__ == "__main__":
    main()