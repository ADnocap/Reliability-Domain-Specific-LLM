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
- 215 numeric Q&A pairs (primary), 280 with hard augmentation
- Sources: 98 textbook-extracted + 158 cross-model verified + 65 hard generated

### Best Results (Qwen3-8B, 5-fold CV, greedy decoding)

| Experiment | Epochs | Baseline | Finetuned | Delta |
|-----------|--------|----------|-----------|-------|
| **v2, 4 epochs (best)** | **4** | **70.7%** | **73.0%** | **+2.3%** |
| v2, 3 epochs | 3 | 70.7% | 71.6% | +0.9% |
| v2, 5 epochs | 5 | 70.7% | 72.6% | +1.9% |

Config: LR=2e-4, NEFTune=5, r=16, alpha=32, dropout=0.05, non-thinking, 215 numeric questions.

### Model Comparison (baseline accuracy, no fine-tuning)

| Model | Accuracy |
|-------|----------|
| Qwen3-8B | 70.7% |
| Llama 3.1 8B | 37.5% |

---

## Setup

1. Install dependencies: `pip install unsloth trl datasets scikit-learn scipy`
2. Copy `.env.example` to `.env` and add your OpenRouter API key
3. For training: see `training/README.md` for HPC cluster instructions
