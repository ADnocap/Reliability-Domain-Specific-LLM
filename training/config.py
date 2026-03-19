"""Shared configuration for the SFT training pipeline.

Change MODEL_NAME and MODEL_TAG to train a different model.
All output paths are derived from MODEL_TAG.
"""

from pathlib import Path

# ---------------------------------------------------------------------------
# Model config — change these to train a different model
# ---------------------------------------------------------------------------
MODEL_NAME = "unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit"
MODEL_TAG = "llama3.1-8b"  # Short name used in output paths

# ---------------------------------------------------------------------------
# Paths (derived from MODEL_TAG)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "data" / "master_dataset_cleaned.jsonl"
CV_SPLITS_DIR = PROJECT_ROOT / "data" / "cv_splits"
RESULTS_DIR = PROJECT_ROOT / "results" / f"sft_cv_{MODEL_TAG}"
BASELINE_DIR = RESULTS_DIR / "baseline"
FINETUNED_DIR = RESULTS_DIR / "finetuned"
ADAPTERS_DIR = RESULTS_DIR / "adapters"

# ---------------------------------------------------------------------------
# Training & evaluation settings
# ---------------------------------------------------------------------------
MAX_SEQ_LENGTH = 2048
N_FOLDS = 5
RANDOM_STATE = 42

SYSTEM_PROMPT = (
    "You are an expert in reliability engineering, probability theory, "
    "and system analysis. Provide clear, accurate answers with step-by-step "
    "reasoning. At the end, clearly state your final answer after "
    "'Final Answer:'."
)

GENERATION_CONFIG = dict(
    max_new_tokens=2048,
    temperature=0.1,
    top_p=0.95,
    do_sample=True,
)

LORA_CONFIG = dict(
    r=16,
    lora_alpha=16,
    lora_dropout=0,
    target_modules=[
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj",
    ],
    use_gradient_checkpointing="unsloth",
    random_state=42,
)

TRAIN_CONFIG = dict(
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    num_train_epochs=3,
    learning_rate=2e-4,
    warmup_steps=5,
    weight_decay=0.01,
    lr_scheduler_type="linear",
    optim="adamw_8bit",
    bf16=True,
    logging_steps=5,
    save_strategy="epoch",
    report_to="none",
    seed=42,
)
