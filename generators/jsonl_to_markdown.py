#!/usr/bin/env python3
"""
JSONL to Markdown Converter

Converts a JSONL file containing questions, reasoning, and answers
into a clean, readable Markdown document.
"""

import json
import argparse
import re
from pathlib import Path


def clean_text(text: str) -> str:
    """Clean up text for markdown output."""
    if not text:
        return ""
    # Normalize whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Strip trailing # markers (orphaned headings from parse_generated_output)
    text = re.sub(r'\s*#{1,6}\s*$', '', text)
    return text.strip()


def format_question(question: str) -> str:
    """Format the question text, handling LaTeX and special formatting."""
    if not question:
        return ""
    
    # Clean up the question
    question = clean_text(question)
    
    return question


def format_reasoning(reasoning: str) -> str:
    """Format the reasoning text, adjusting heading levels."""
    if not reasoning:
        return "*No reasoning provided.*"
    
    # Check if reasoning failed
    if reasoning.startswith("REASONING_FAILED"):
        return f"⚠️ {reasoning}"
    
    reasoning = clean_text(reasoning)
    
    # Increase heading levels by 3 so they nest properly under ### Solution
    # Must process longer patterns first (######, #####, etc.) to avoid double-processing
    # Process lines that start with # headings
    lines = reasoning.split('\n')
    adjusted_lines = []
    
    for line in lines:
        # Match lines that start with 1-6 # followed by space
        if re.match(r'^(#{1,6})\s', line):
            # Add 3 more # to the heading
            match = re.match(r'^(#{1,6})(\s.*)', line)
            if match:
                hashes = match.group(1)
                rest = match.group(2)
                # Cap at 6 # (markdown max)
                new_hashes = '#' * min(len(hashes) + 3, 6)
                line = new_hashes + rest
        adjusted_lines.append(line)
    
    return '\n'.join(adjusted_lines)


def title_from_question(question: str) -> str:
    """Generate a short title from the first ~60 chars of question text."""
    text = clean_text(question)
    # Collapse whitespace to single spaces
    text = re.sub(r'\s+', ' ', text)
    if len(text) <= 60:
        return text
    # Truncate at a word boundary
    truncated = text[:60].rsplit(' ', 1)[0]
    return truncated + "..."


def format_answer(answer: str) -> str:
    """Format the answer text."""
    if not answer:
        return "*No answer provided.*"
    
    return clean_text(answer)


def jsonl_to_markdown(
    input_path: str,
    output_path: str,
    title: str = "Problem Set",
    include_toc: bool = True,
    include_reasoning: bool = True,
    number_problems: bool = True
) -> int:
    """
    Convert JSONL file to Markdown.
    
    Args:
        input_path: Path to input JSONL file
        output_path: Path to output Markdown file
        title: Document title
        include_toc: Whether to include table of contents
        include_reasoning: Whether to include reasoning section
        number_problems: Whether to number problems
    
    Returns:
        Number of problems processed
    """
    # Read all items
    items = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    items.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"Warning: Skipping invalid JSON line: {e}")
    
    if not items:
        print("No valid items found in input file.")
        return 0
    
    # Build markdown content
    md_lines = []
    
    # Title
    md_lines.append(f"# {title}")
    md_lines.append("")
    
    # Summary
    md_lines.append(f"*{len(items)} problems*")
    md_lines.append("")
    
    # Table of Contents
    if include_toc:
        md_lines.append("## Table of Contents")
        md_lines.append("")
        for i, item in enumerate(items, 1):
            problem_title = item.get("title") or title_from_question(item.get("question", "")) or f"Problem {i}"
            # Create anchor-friendly slug
            slug = re.sub(r'[^a-z0-9\s-]', '', problem_title.lower())
            slug = re.sub(r'\s+', '-', slug).strip('-')
            if number_problems:
                md_lines.append(f"{i}. [{problem_title}](#{slug})")
            else:
                md_lines.append(f"- [{problem_title}](#{slug})")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")
    
    # Problems
    for i, item in enumerate(items, 1):
        problem_title = item.get("title") or title_from_question(item.get("question", "")) or f"Problem {i}"
        question = item.get("question", "")
        reasoning = item.get("reasoning", "")
        answer = item.get("answer", "")
        
        # Problem header
        if number_problems:
            md_lines.append(f"## {i}. {problem_title}")
        else:
            md_lines.append(f"## {problem_title}")
        md_lines.append("")
        
        # Question
        md_lines.append("### Question")
        md_lines.append("")
        md_lines.append(format_question(question))
        md_lines.append("")
        
        # Reasoning (optional)
        if include_reasoning and reasoning:
            md_lines.append("### Reasoning")
            md_lines.append("")
            md_lines.append(format_reasoning(reasoning))
            md_lines.append("")
        
        # Answer
        md_lines.append("### Answer")
        md_lines.append("")
        md_lines.append(f"**{format_answer(answer)}**")
        md_lines.append("")
        
        # Separator between problems
        if i < len(items):
            md_lines.append("---")
            md_lines.append("")
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))
    
    print(f"Done: Converted {len(items)} problems to {output_path}")
    return len(items)


PRESETS = {
    "verified": {
        "input_file": "../data/cross_model_verified.jsonl",
        "output_file": "../data/cross_model_verified.md",
        "title": "Cross-Model Verified Problems",
    },
    "rejected": {
        "input_file": "../data/cross_model_rejected.jsonl",
        "output_file": "../data/cross_model_rejected.md",
        "title": "Cross-Model Rejected Problems",
    },
}


def main():
    parser = argparse.ArgumentParser(
        description="Convert JSONL problem set to clean Markdown",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic conversion
  python jsonl_to_markdown.py problems.jsonl problems.md

  # Custom title
  python jsonl_to_markdown.py problems.jsonl problems.md --title "Reliability Engineering Problems"

  # Use a preset for cross-model files
  python jsonl_to_markdown.py --preset verified
  python jsonl_to_markdown.py --preset rejected

  # Without table of contents
  python jsonl_to_markdown.py problems.jsonl problems.md --no-toc

  # Without reasoning (questions and answers only)
  python jsonl_to_markdown.py problems.jsonl problems.md --no-reasoning
        """
    )

    parser.add_argument("input_file", nargs="?", help="Input JSONL file path")
    parser.add_argument("output_file", nargs="?", help="Output Markdown file path")
    parser.add_argument("--preset", choices=PRESETS.keys(),
                        help="Use preset paths for cross-model files (verified/rejected)")
    parser.add_argument("--title", "-t", default=None,
                        help="Document title (default: 'Problem Set')")
    parser.add_argument("--no-toc", action="store_true",
                        help="Don't include table of contents")
    parser.add_argument("--no-reasoning", action="store_true",
                        help="Don't include reasoning/solution section")
    parser.add_argument("--no-numbers", action="store_true",
                        help="Don't number problems")

    args = parser.parse_args()

    # Apply preset defaults, then let explicit args override
    if args.preset:
        preset = PRESETS[args.preset]
        if args.input_file is None:
            args.input_file = preset["input_file"]
        if args.output_file is None:
            args.output_file = preset["output_file"]
        if args.title is None:
            args.title = preset["title"]

    if args.title is None:
        args.title = "Problem Set"

    if not args.input_file or not args.output_file:
        parser.error("input_file and output_file are required (or use --preset)")

    # Validate input
    if not Path(args.input_file).exists():
        print(f"Error: Input file not found: {args.input_file}")
        return

    # Convert
    jsonl_to_markdown(
        input_path=args.input_file,
        output_path=args.output_file,
        title=args.title,
        include_toc=not args.no_toc,
        include_reasoning=not args.no_reasoning,
        number_problems=not args.no_numbers
    )


if __name__ == "__main__":
    main()