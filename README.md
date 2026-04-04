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
