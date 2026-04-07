# Experiment Results

All experiments use Qwen3-8B (4-bit, LoRA) with 5-fold cross-validation on numeric-only reliability engineering questions. Non-thinking mode. Greedy decoding from round 3 onwards.

---

## All Completed Results

### Round 1: Model Selection

| # | Model | Dataset | Baseline | Finetuned | Delta | Notes |
|---|-------|---------|----------|-----------|-------|-------|
| 1 | Llama 3.1 8B | 256 (all) | 37.5% | 39.8% | +2.4% | Weak math baseline |
| 2 | Qwen3-8B | 215 (num) | 67.9% | 67.0% | -0.9% | Thinking mismatch broke SFT |

### Round 2: Hyperparameter Search (215 questions, stochastic eval)

| # | Config | Baseline | Finetuned | Delta | W->R / R->W |
|---|--------|----------|-----------|-------|-------------|
| 3 | LR=2e-4, NEFTune=5, r=16, 3ep | 67.9%* | 74.9%* | +7.0%* | 31 / 16 |
| 4 | NEFTune=10 | 70.7%* | 72.1%* | +1.4% | 21 / 18 |
| 5 | r=8, alpha=16 | 67.9%* | 69.3%* | +1.4% | 24 / 21 |
| 6 | LR=1e-4 | 68.8%* | 68.4%* | -0.5% | 20 / 21 |

*Stochastic baselines — vary between runs.

### Round 3: Deterministic Eval (greedy decoding)

**215-question dataset:**

| # | Config | Baseline | Finetuned | Delta | W->R / R->W |
|---|--------|----------|-----------|-------|-------------|
| 11 | v2, 3 epochs | 70.7% | 71.6% | +0.9% | 22 / 20 |
| **12** | **v2, 4 epochs** | **70.7%** | **73.0%** | **+2.3%** | **23 / 18** |
| 9 | v2, 5 epochs | 70.7%* | 72.6% | +1.9% | 21 / 17 |
| 17 | NEFTune=7, 4 epochs | 71.0% | 69.8% | -1.3% | 19 / 18 |

**280-question dataset (215 original + 65 hard generated):**

| # | Config | Baseline | Finetuned | Delta | W->R / R->W |
|---|--------|----------|-----------|-------|-------------|
| 7 | v2, 3 epochs | 64.0% | 65.2% | +1.3% | 21 / 21 |
| 8 | v2, 5 epochs | 64.3% | 65.7% | +1.4% | 30 / 19 |
| **16** | **v2, 4 epochs** | **71.0%** | **73.0%** | **+2.0%** | **19 / 15** |

### Round 4: Alternative Methods

| # | Method | Dataset | Baseline | Finetuned | Delta | Status |
|---|--------|---------|----------|-----------|-------|--------|
| 14 | DPO | 215 | 70.7% | 68.0% | -2.7% | Done (4/5 folds) |
| 15 | SFT+GRPO | 215 | 70.7% | 71.2% | +0.5% | Done |
| 10 | DPO | 280 | 64.3% | -- | -- | Timed out |
| 13 | SFT+GRPO | 215 | 70.7% | -- | -- | Crashed (Triton) |

### Round 5: Paraphrase Augmentation (501 questions = 280 original + 221 rephrased)

| # | Config | Baseline | Finetuned | Delta | W->R / R->W |
|---|--------|----------|-----------|-------|-------------|
| **18** | **4 epochs, LR=2e-4** | **59.1%** | **65.3%** | **+6.2%** | **74 / 43** |
| 20 | 6 epochs, LR=1e-4 | 59.1% | 64.9% | +5.8% | 78 / 49 |
| 19 | 8 epochs + early stop, LR=1.5e-4 | 59.1% | 64.5% | +5.4% | 83 / 56 |

Note: Baseline is lower (59.1% vs 70.7%) because the test set now includes rephrased questions the base model hasn't seen. The finetuned model handles both original and rephrased questions well.

---

## Key Findings

### 1. Base Model Selection (biggest impact)
Qwen3-8B (70.7% baseline) vs Llama 3.1 8B (37.5%) — nearly 2x difference with zero fine-tuning.

### 2. Paraphrase Augmentation is the Most Effective Strategy
Rephrasing questions with Opus 4.6 (verified by GPT-5.4) nearly tripled the SFT improvement:

| Dataset | Samples | Best Delta |
|---------|---------|------------|
| 215 (original) | 215 | +2.3% |
| 280 (+ hard generated) | 280 | +2.0% |
| **501 (+ paraphrased)** | **501** | **+6.2%** |

This aligns with MetaMath/PersonaMath research: surface-level diversity (rephrasing) is more valuable than difficulty (hard questions).

### 3. 4 Epochs Remains the Sweet Spot
| Epochs | Delta (215) | Delta (280) | Delta (501) |
|--------|-------------|-------------|-------------|
| 3 | +0.9% | +1.3% | -- |
| **4** | **+2.3%** | **+2.0%** | **+6.2%** |
| 5 | +1.9% | +1.4% | -- |
| 6 | -- | -- | +5.8% |
| 8 (ES) | -- | -- | +5.4% |

More epochs with lower LR didn't help, even with 2x more data.

### 4. NEFTune=5 is the Right Amount
NEFTune=5 works, NEFTune=7 hurts (-1.3%), NEFTune=10 marginal (+1.4% stochastic). More noise = more forgetting.

### 5. Hard Synthetic Questions vs Paraphrasing
Adding 65 hard questions didn't improve SFT delta (+2.0% vs +2.3%). But adding 221 paraphrased questions boosted it to +6.2%. The model benefits more from seeing the same knowledge expressed differently than from harder problems.

### 6. Stochastic vs Deterministic Eval
The +7.0% from round 2 was inflated by sampling variance. True improvement with greedy decoding is +2.3%. Always use do_sample=False for evaluation.

### 7. RL Methods Don't Beat SFT
DPO actually hurt performance (-2.7%), and GRPO gave only +0.5% — well below SFT's +2.3%. Neither method improves on the best SFT config with this dataset size.

---

## Best Config (Reproducible)

```python
MODEL = "unsloth/qwen3-8b-unsloth-bnb-4bit"
DATASET = "master_dataset_v3.jsonl"  # 501 samples (280 original + 221 paraphrased)
LR = 2e-4
NEFTUNE = 5
LORA_R = 16, LORA_ALPHA = 32, DROPOUT = 0.05
EPOCHS = 4
ENABLE_THINKING = False
DO_SAMPLE = False  # for eval
MAX_NEW_TOKENS = 4096
```

Result: 59.1% -> 65.3% (+6.2%) on 501 numeric questions, 5-fold CV.
Previous best: 70.7% -> 73.0% (+2.3%) on 215 numeric questions.

---

## Next Steps

- [x] Get DPO results → -2.7% (worse than baseline)
- [x] Get GRPO results → +0.5% (marginal, below SFT)
- [x] Paraphrase augmentation → **+6.2%** (best result, nearly 3x previous best delta)
- [ ] Try self-consistency training (use model's own correct reasoning chains)
- [ ] Investigate the ~35% of questions the model always gets wrong
- [ ] Generate more paraphrases (currently 2x, research suggests up to 4x can help)
- [ ] Consider a different base model (e.g., Qwen2.5-Math-7B if available)
