"""Prepare 5-fold cross-validation splits for SFT training.

Input:  data/master_dataset_cleaned.jsonl (256 Q&A pairs)
Output: data/cv_splits/fold_{0-4}_train.jsonl  (chat format for SFT)
        data/cv_splits/fold_{0-4}_test.jsonl   (raw fields for evaluation)
"""

import sys
from pathlib import Path
from sklearn.model_selection import StratifiedKFold

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.data_io import load_dataset, save_dataset
from training.config import DATASET_PATH, CV_SPLITS_DIR, N_FOLDS, RANDOM_STATE, SYSTEM_PROMPT


def format_train_example(item: dict) -> dict:
    """Convert a raw Q&A item into chat format for SFT."""
    reasoning = item.get("reasoning", "")
    answer = item["answer"]

    if reasoning:
        assistant_content = f"{reasoning}\n\nFinal Answer: {answer}"
    else:
        assistant_content = f"Final Answer: {answer}"

    return {
        "conversations": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": item["question"]},
            {"role": "assistant", "content": assistant_content},
        ]
    }


def main():
    dataset = load_dataset(str(DATASET_PATH))
    print(f"Loaded {len(dataset)} items from {DATASET_PATH}")

    answer_types = [item.get("answer_type", "unknown") for item in dataset]
    type_counts = {}
    for t in answer_types:
        type_counts[t] = type_counts.get(t, 0) + 1
    print(f"Answer type distribution: {type_counts}")

    CV_SPLITS_DIR.mkdir(parents=True, exist_ok=True)

    skf = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=RANDOM_STATE)

    for fold_idx, (train_indices, test_indices) in enumerate(skf.split(dataset, answer_types)):
        train_items = [format_train_example(dataset[i]) for i in train_indices]
        train_path = CV_SPLITS_DIR / f"fold_{fold_idx}_train.jsonl"
        save_dataset(train_items, str(train_path))

        test_items = [dataset[i] for i in test_indices]
        test_path = CV_SPLITS_DIR / f"fold_{fold_idx}_test.jsonl"
        save_dataset(test_items, str(test_path))

        train_types = {}
        for i in train_indices:
            t = dataset[i].get("answer_type", "unknown")
            train_types[t] = train_types.get(t, 0) + 1

        test_types = {}
        for i in test_indices:
            t = dataset[i].get("answer_type", "unknown")
            test_types[t] = test_types.get(t, 0) + 1

        print(f"Fold {fold_idx}: {len(train_indices)} train / {len(test_indices)} test")
        print(f"  Train types: {train_types}")
        print(f"  Test types:  {test_types}")

    total = sum(len(list(skf.split(dataset, answer_types))[i][1]) for i in range(N_FOLDS))
    print(f"\nTotal test samples across folds: {total} (should be {len(dataset)})")
    print(f"Output directory: {CV_SPLITS_DIR}")


if __name__ == "__main__":
    main()
