"""Shared configuration for the SFT training pipeline.

Change MODEL_NAME and MODEL_TAG to train a different model.
All output paths are derived from MODEL_TAG.
Override settings via environment variables (SFT_*) for experiments.
"""

import os
from pathlib import Path


def _env_float(key, default):
    """Read a float from an environment variable, or return default."""
    v = os.environ.get(key)
    return float(v) if v else default


def _env_int(key, default):
    """Read an int from an environment variable, or return default."""
    v = os.environ.get(key)
    return int(v) if v else default


# ---------------------------------------------------------------------------
# Model config
# ---------------------------------------------------------------------------
MODEL_NAME = os.environ.get("SFT_MODEL", "unsloth/qwen3-8b-unsloth-bnb-4bit")
MODEL_TAG = os.environ.get("SFT_TAG", "qwen3-8b-v2")

# ---------------------------------------------------------------------------
# Paths (derived from MODEL_TAG)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "data" / os.environ.get("SFT_DATASET", "master_dataset_cleaned.jsonl")
CV_SPLITS_DIR = PROJECT_ROOT / "data" / "cv_splits"
RESULTS_DIR = PROJECT_ROOT / "results" / f"sft_cv_{MODEL_TAG}"
BASELINE_DIR = RESULTS_DIR / "baseline"
FINETUNED_DIR = RESULTS_DIR / "finetuned"
ADAPTERS_DIR = RESULTS_DIR / "adapters"

# ---------------------------------------------------------------------------
# Training & evaluation settings
# ---------------------------------------------------------------------------
MAX_SEQ_LENGTH = 2048
N_FOLDS = _env_int("SFT_FOLDS", 5)
RANDOM_STATE = 42

SYSTEM_PROMPT = (
    "You are an expert in reliability engineering, probability theory, "
    "and system analysis. Provide clear, accurate answers with step-by-step "
    "reasoning. At the end, clearly state your final answer after "
    "'Final Answer:'."
)

GENERATION_CONFIG = dict(
    max_new_tokens=_env_int("SFT_MAX_TOKENS", 4096),
    do_sample=False,
)

# Thinking mode: controls enable_thinking kwarg in apply_chat_template for EVAL.
# Training always uses enable_thinking=False (training data has no <think> blocks).
EVAL_THINKING = os.environ.get("SFT_THINKING", "false").lower() == "true"

_neftune = _env_float("SFT_NEFTUNE", 5)

LORA_CONFIG = dict(
    r=_env_int("SFT_LORA_R", 16),
    lora_alpha=_env_int("SFT_LORA_ALPHA", 32),
    lora_dropout=_env_float("SFT_LORA_DROPOUT", 0.05),
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
    num_train_epochs=_env_int("SFT_EPOCHS", 3),
    learning_rate=_env_float("SFT_LR", 2e-4),
    warmup_steps=5,
    weight_decay=0.01,
    lr_scheduler_type="cosine",
    optim="adamw_8bit",
    bf16=True,
    logging_steps=5,
    save_strategy="epoch",
    report_to="none",
    seed=42,
    neftune_noise_alpha=_neftune if _neftune > 0 else None,
)
