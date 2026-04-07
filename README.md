# Domain-Specific LLM for Reliability Engineering

**Research Project** | CentraleSupelec - LGI Laboratory
**Supervisor**: Zhiguo Zeng
**Group Members**: Alex Dalban, Elora Drouilhet

Fine-tuning Large Language Models for reliability engineering through synthetic data generation and paraphrase augmentation.

See [RESULTS.md](RESULTS.md) for detailed experiment results and findings.
See [results/experiment_log.md](results/experiment_log.md) for the complete experiment log with all configurations and metrics.

---

## Project Overview

Engineers working with complex systems (nuclear plants, aircraft, electrical grids) require sophisticated reliability analysis. General-purpose LLMs fail at reliability-specific problems due to lack of specialized training data.

This project develops a domain-specific LLM by:
1. **Synthetic data generation** from reliability textbooks using an adapted Self-Instruct pipeline
2. **Cross-model answer verification** to ensure data quality
3. **Paraphrase augmentation** using Claude Opus 4.6 with GPT-5.4 verification (based on MetaMath/PersonaMath research)
4. **LoRA fine-tuning** with 5-fold cross-validation on Qwen3-8B
5. **Rigorous evaluation** with automated answer comparison and statistical testing (Wilcoxon signed-rank)

---

## Results Summary

### Datasets

| Dataset | Samples | Source |
|---------|---------|--------|
| master_cleaned (v1) | 215 numeric | 98 textbook + 158 cross-model verified |
| master_v2 | 280 numeric | v1 + 65 hard generated (Opus + GPT-5.4) |
| **master_v3** | **501 numeric** | **v2 + 221 paraphrase-augmented** |

### Best Results (Qwen3-8B, 5-fold CV, greedy decoding)

| Dataset | Epochs | Baseline | Finetuned | Delta | p-value |
|---------|--------|----------|-----------|-------|---------|
| 215 (v1) | 4 | 70.7% | 73.0% | +2.3% | 0.50 |
| **501 (v3, augmented)** | **4** | **59.1%** | **65.3%** | **+6.2%** | **0.0625** |

Paraphrase augmentation nearly tripled the SFT improvement (+6.2% vs +2.3%).

Config: LR=2e-4, NEFTune=5, LoRA r=16/alpha=32, dropout=0.05, non-thinking mode.

### Key Findings

1. **Model selection matters most**: Qwen3-8B (70.7%) vs Llama 3.1 8B (37.5%)
2. **Paraphrase augmentation is the most effective strategy**: +6.2% vs +2.3% with original data
3. **4 epochs is the sweet spot** across all dataset sizes
4. **RL methods (DPO, GRPO) don't beat SFT** on this dataset size
5. **Surface-level diversity > difficulty**: rephrased questions help more than harder questions

### 20 Experiments Completed

See [results/experiment_log.md](results/experiment_log.md) for the full table covering model selection, hyperparameter search, deterministic eval, DPO/GRPO, and paraphrase augmentation.

---

## Repository Structure

```
data/                       # Datasets (JSONL format)
generators/                 # Data generation and augmentation scripts
  generate_hard_numeric.py  # Hard question generator (Opus + GPT-5.4 verification)
  rephrase_augment.py       # Paraphrase augmentation pipeline
training/                   # Training and evaluation pipeline
  config.py                 # Shared configuration (env var overrides)
  prepare_data.py           # 5-fold CV split generation
  train_sft.py              # SFT training with optional early stopping
  train_dpo.py              # DPO training
  train_grpo.py             # GRPO training
  evaluate_baseline.py      # Baseline (no fine-tuning) evaluation
  evaluate_finetuned.py     # Fine-tuned model evaluation
  aggregate_results.py      # CV aggregation, Wilcoxon test, per-type breakdown
  experiments/              # SLURM job scripts for LaRuche HPC
results/                    # Per-experiment results (numbered exp01-exp20)
utils/                      # Shared utilities (API client, data I/O)
```

## Setup

1. Install dependencies: `pip install unsloth trl datasets scikit-learn scipy`
2. Copy `.env.example` to `.env` and add your OpenRouter API key
3. For training on HPC: see SLURM scripts in `training/experiments/`
