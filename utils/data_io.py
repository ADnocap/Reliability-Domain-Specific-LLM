"""JSON / JSONL dataset load and save helpers."""

import json
from pathlib import Path
from typing import Dict, List, Optional


def load_dataset(filepath: str) -> List[Dict]:
    """Load a dataset from a JSON or JSONL file (auto-detected).

    Args:
        filepath: Path to a .json or .jsonl file.

    Returns:
        A list of dictionaries.
    """
    filepath = Path(filepath)
    items: List[Dict] = []

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        return items

    # Try JSON first
    try:
        data = json.loads(content)
        if isinstance(data, list):
            return data
        return [data]
    except json.JSONDecodeError:
        pass

    # Fall back to JSONL
    for line_num, line in enumerate(content.splitlines(), 1):
        line = line.strip()
        if line:
            try:
                items.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"Warning: skipping invalid JSON on line {line_num}")

    return items


def save_dataset(
    data: List[Dict],
    filepath: str,
    fmt: Optional[str] = None,
) -> None:
    """Save a dataset to a JSON or JSONL file.

    Args:
        data: List of dictionaries to save.
        filepath: Destination path.
        fmt: ``'json'`` or ``'jsonl'``. If *None*, inferred from file extension.
    """
    filepath = Path(filepath)

    if fmt is None:
        fmt = "jsonl" if filepath.suffix == ".jsonl" else "json"

    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        if fmt == "jsonl":
            for item in data:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
        else:
            json.dump(data, f, ensure_ascii=False, indent=2)
