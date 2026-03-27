# Domain-Specific LLM for Reliability Engineering

**Research Project** | CentraleSupelec - LGI Laboratory
**Supervisor**: Zhiguo Zeng
**Group Members**: Alex Dalban, Elora Drouilhet

Fine-tuning Large Language Models for reliability engineering through self-instruct synthetic data generation.

See [METHODOLOGY.md](METHODOLOGY.md) for a detailed write-up of all strategies, experiments, and findings.

---

## Project Overview

Engineers working with complex systems (nuclear plants, aircraft, electrical grids) require sophisticated reliability analysis. General-purpose LLMs fail at reliability-specific problems due to lack of specialized training data.

This project develops a domain-specific LLM by:
1. **Synthetic data generation** from reliability textbooks using an adapted Self-Instruct pipeline
2. **Cross-model answer verification** to ensure data quality
3. **LoRA fine-tuning** with 5-fold cross-validation on open-weight models
4. **Rigorous evaluation** with automated answer comparison and statistical testing

---

## Repository Structure

```
├── data/
│   ├── master_dataset_cleaned.jsonl   # Final dataset (256 items)
│   ├── cv_splits/                     # 5-fold train/test splits
│   ├── seed_dataset.json              # Original textbook extractions
│   ├── seed_subset_49.jsonl           # Filtered high-quality seed
│   ├── cross_model_verified.jsonl     # Cross-model verified items
│   └── cross_model_rejected.jsonl     # Rejected items
├── training/
│   ├── config.py                      # Experiment config (env var overrides)
│   ├── prepare_data.py                # CV split generation
│   ├── evaluate_baseline.py           # Base model evaluation
│   ├── train_sft.py                   # LoRA SFT training
│   ├── evaluate_finetuned.py          # Fine-tuned model evaluation
│   ├── aggregate_results.py           # Cross-validation aggregation
│   └── experiments/                   # Per-experiment SLURM scripts
├── generators/
│   ├── synthetic_data_generation.ipynb # Self-instruct generation
│   ├── cross_model_generation.ipynb   # Cross-model verification
│   └── reasoning_processor.py         # Reasoning chain validation
├── evaluators/
│   ├── baseline_small_models.ipynb    # Multi-model baseline eval
│   └── model_evaluation.ipynb         # General evaluation
├── extractors/
│   ├── textbook_qa_extractor.ipynb    # OCR -> Q/R/A extraction
│   ├── dataset_cleaning.ipynb         # Final cleaning pipeline
│   └── fix_unicode_latex_llm.ipynb    # LaTeX/Unicode fixing
├── results/                           # Experiment results (per model tag)
├── utils/
│   ├── api_client.py                  # OpenRouter API client
│   └── data_io.py                     # JSONL I/O helpers
├── literature/                        # Reference papers
└── ocr_output/                        # Textbook OCR markdown
```

---

## Results Summary

### Dataset
- 256 Q&A pairs (215 numeric, 21 formula, 19 text, 1 boolean)
- Sources: 98 textbook-extracted (seed) + 158 cross-model verified (synthetic)

### Fine-Tuning Experiments (Qwen3-8B, numeric-only, 5-fold CV)

| Experiment | Key Change | Baseline | Finetuned | Delta |
|-----------|-----------|----------|-----------|-------|
| Run 1 (thinking enabled) | LR=5e-5, no NEFTune | 67.9% | 67.0% | -0.9% |
| **v2 (best guess)** | **LR=2e-4, NEFTune=5, no-think** | **67.9%** | **74.9%** | **+7.0%** |
| neft10 | NEFTune=10 | 67.9% | 72.1% | +4.2% |
| lowrank | r=8, alpha=16 | 67.9% | 69.3% | +1.4% |
| lr1e4 | LR=1e-4 | 67.9% | TBD | TBD |

### Earlier Experiments

| Model | Dataset | Baseline | Finetuned | Delta |
|-------|---------|----------|-----------|-------|
| Qwen3-14B | 288 (all) | 8.6% | 13.8% | +5.2% |
| Llama 3.1 8B | 256 (all) | 37.5% | 39.8% | +2.4% |

---

## Setup

1. Install dependencies: `pip install unsloth trl datasets scikit-learn scipy`
2. Copy `.env.example` to `.env` and add your OpenRouter API key
3. For training: see `training/README.md` for HPC cluster instructions
