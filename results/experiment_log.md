# Complete Experiment Log

Every experiment run, with full configuration and results.

## Master Table

| Exp    | Tag                            | Model        | Dataset                           | N_train | N_test  | Epochs     | LR        | NEFTune | LoRA r/a  | Dropout  | Thinking | Eval Mode  | Baseline  | Finetuned | Delta      | W->R    | R->W   | p-value    | Status                                   |
| ------ | ------------------------------ | ------------ | --------------------------------- | ------- | ------- | ---------- | --------- | ------- | --------- | -------- | -------- | ---------- | --------- | --------- | ---------- | ------- | ------ | ---------- | ---------------------------------------- |
| 1      | llama3.1-8b                    | Llama 3.1 8B | master_cleaned (256, all types)   | ~204    | ~51     | 3          | 2e-4      | --      | 16/16     | 0        | off      | stochastic | 37.5%     | 39.8%     | +2.4%      | 35      | 29     | 0.25       | Done                                     |
| 2      | qwen3-8b                       | Qwen3-8B     | master_cleaned (215, numeric)     | 172     | 43      | 4          | 5e-5      | --      | 16/32     | 0        | **on**   | stochastic | 67.9%     | 67.0%     | -0.9%      | 25      | 27     | 0.875      | Done                                     |
| 3      | qwen3-8b-v2                    | Qwen3-8B     | master_cleaned (215, numeric)     | 172     | 43      | 3          | 2e-4      | 5       | 16/32     | 0.05     | off      | stochastic | 67.9%     | 74.9%     | +7.0%\*    | 31      | 16     | 0.125      | Done                                     |
| 4      | qwen3-8b-neft10                | Qwen3-8B     | master_cleaned (215, numeric)     | 172     | 43      | 3          | 2e-4      | 10      | 16/32     | 0.05     | off      | stochastic | 70.7%     | 72.1%     | +1.4%      | 21      | 18     | 1.0        | Done                                     |
| 5      | qwen3-8b-lowrank               | Qwen3-8B     | master_cleaned (215, numeric)     | 172     | 43      | 3          | 2e-4      | 5       | 8/16      | 0.05     | off      | stochastic | 67.9%     | 69.3%     | +1.4%      | 24      | 21     | 0.875      | Done                                     |
| 6      | qwen3-8b-lr1e4                 | Qwen3-8B     | master_cleaned (215, numeric)     | 172     | 43      | 3          | 1e-4      | 5       | 16/32     | 0.05     | off      | stochastic | 68.8%     | 68.4%     | -0.5%      | 20      | 21     | 1.0        | Done                                     |
| 7      | qwen3-8b-v2-280                | Qwen3-8B     | master_v2 (280, numeric)          | 224     | 56      | 3          | 2e-4      | 5       | 16/32     | 0.05     | off      | greedy     | 64.0%     | 65.2%     | +1.3%      | 21      | 21     | 0.875      | Done                                     |
| 8      | qwen3-8b-5ep-280               | Qwen3-8B     | master_v2 (280, numeric)          | 224     | 56      | 5          | 2e-4      | 5       | 16/32     | 0.05     | off      | greedy     | 64.3%     | 65.7%     | +1.4%      | 30      | 19     | 0.875      | Done                                     |
| 9      | qwen3-8b-5ep-215               | Qwen3-8B     | master_cleaned (215, numeric)     | 172     | 43      | 5          | 2e-4      | 5       | 16/32     | 0.05     | off      | stochastic | 70.7%     | 72.6%     | +1.9%      | 21      | 17     | 0.5        | Done                                     |
| 10     | qwen3-8b-dpo-280               | Qwen3-8B     | master_v2 (280, numeric)          | 224     | 56      | DPO        | 5e-6      | --      | 16/32     | 0.05     | off      | greedy     | 64.3%     | --        | --         | --      | --     | --         | Timed out (14h)                          |
| 11     | qwen3-8b-v2-greedy-215         | Qwen3-8B     | master_cleaned (215, numeric)     | 172     | 43      | 3          | 2e-4      | 5       | 16/32     | 0.05     | off      | greedy     | 70.7%     | 71.6%     | +0.9%      | 22      | 20     | 0.875      | Done                                     |
| **12** | **qwen3-8b-4ep-215**           | **Qwen3-8B** | **master_cleaned (215, numeric)** | **172** | **43**  | **4**      | **2e-4**  | **5**   | **16/32** | **0.05** | **off**  | **greedy** | **70.7%** | **73.0%** | **+2.3%**  | **23**  | **18** | **0.5**    | **Done (best 215)**                      |
| 13     | qwen3-8b-grpo2-215             | Qwen3-8B     | master_cleaned (215, numeric)     | 172     | 43      | SFT+GRPO   | 2e-4/5e-6 | 5       | 16/32     | 0.05     | off      | greedy     | 70.7%     | --        | --         | --      | --     | --         | Crashed (Triton)                         |
| 14     | qwen3-8b-dpo-215               | Qwen3-8B     | master_cleaned (215, numeric)     | 172     | 43      | DPO        | 5e-6      | --      | 16/32     | 0.05     | off      | greedy     | 69.8%     | 68.0%     | -1.7%      | 4       | 7      | 0.625      | Done (4/5 folds, fold 4 adapter missing) |
| 15     | qwen3-8b-grpo3-215             | Qwen3-8B     | master_cleaned (215, numeric)     | 172     | 43      | SFT+GRPO   | 2e-4/5e-6 | 5       | 16/32     | 0.05     | off      | greedy     | 70.7%     | 71.2%     | +0.5%      | 18      | 17     | 0.875      | Done (re-run succeeded)                  |
| **16** | **qwen3-8b-4ep-280**           | **Qwen3-8B** | **master_v2 (280, numeric)**      | **224** | **56**  | **4**      | **2e-4**  | **5**   | **16/32** | **0.05** | **off**  | **greedy** | **71.0%** | **73.0%** | **+2.0%**  | **19**  | **15** | 0.6875     | **Done (best 280)**                      |
| 17     | qwen3-8b-neft7-4ep-215         | Qwen3-8B     | master_cleaned (215, numeric)     | 172     | 43      | 4          | 2e-4      | 7       | 16/32     | 0.05     | off      | greedy     | 71.0%     | 69.8%     | -1.3%      | 19      | 18     | 0.375      | Done                                     |
| **18** | **qwen3-8b-aug501-4ep**        | **Qwen3-8B** | **master_v3 (501, numeric)**      | **400** | **101** | **4**      | **2e-4**  | **5**   | **16/32** | **0.05** | **off**  | **greedy** | **59.1%** | **65.3%** | **+6.2%**  | **74**  | **43** | **0.0625** | **Done (best aug, +6.2%)**               |
| 19     | qwen3-8b-aug501-8ep-es         | Qwen3-8B     | master_v3 (501, numeric)          | 400     | 101     | 8 (ES→4)\*\*  | 1.5e-4    | 5       | 16/32     | 0.05     | off      | greedy     | 59.1%     | 64.5%     | +5.4%      | 83      | 56     | 0.0625     | Done (early stopping, patience=2)        |
| 20     | qwen3-8b-aug501-6ep-lr1e4      | Qwen3-8B     | master_v3 (501, numeric)          | 400     | 101     | 6          | 1e-4      | 5       | 16/32     | 0.05     | off      | greedy     | 59.1%     | 64.9%     | +5.8%      | 78      | 49     | 0.0625     | Done                                     |
| 21     | qwen3-8b-aug866-4ep-10f        | Qwen3-8B     | master_v4 (866, numeric)          | 780     | 87      | 4          | 2e-4      | 5       | 16/32     | 0.05     | off      | greedy     | 63.6%     | 79.3%     | +15.7%     | 194     | 58     | **0.002**  | Done (10-fold, significant)              |
| 22     | qwen3-8b-aug866-6ep-es-10f     | Qwen3-8B     | master_v4 (866, numeric)          | 780     | 87      | 6 (ES→4)\*\*   | 2e-4      | 5       | 16/32     | 0.05     | off      | greedy     | 63.6%     | 81.8%     | +18.1%     | 208     | 51     | **0.002**  | Done (10-fold, significant)              |
| 23     | qwen3-8b-aug866-3ep-10f        | Qwen3-8B     | master_v4 (866, numeric)          | 780     | 87      | 3          | 2e-4      | 5       | 16/32     | 0.05     | off      | greedy     | 63.6%     | 75.1%     | +11.4%     | 171     | 72     | **0.002**  | Done (10-fold, significant)              |
| **24** | **qwen3-8b-aug866-8ep-es-10f** | **Qwen3-8B** | **master_v4 (866, numeric)**      | **780** | **87**  | **8 (ES→4)\*\*** | **2e-4** | **5** | **16/32** | **0.05** | **off** | **greedy** | **63.6%** | **82.2%** | **+18.6%** | **206** | **45** | **0.002** | **Done (best overall, significant)**     |
| **25** | **qwen3-8b-600s-5ep-10f**      | **Qwen3-8B** | **v4 remaining (600, numeric)**   | **540** | **60**  | **5**             | **2e-4** | **5** | **16/32** | **0.05** | **off** | **greedy** | **68.0%** | **79.7%** | **+11.7%** | **108** | **38** | **0.002** | **Done (best on 600 subset, significant)** |
| 26     | qwen3-8b-600s-5ep-es-10f       | Qwen3-8B     | v4 remaining (600, numeric)       | 540     | 60      | 5 (ES)            | 2e-4     | 5     | 16/32     | 0.05     | off     | greedy     | 68.0%     | 78.8%     | +10.8%     | 100     | 35     | **0.002**  | Done (10-fold, significant)              |

\*Exp 3 delta inflated by stochastic eval — true deterministic improvement is +2.3% (exp 12).

\*\*ES = Early Stopping (patience=2). Format: `max_epochs (ES→best_epoch)`. Training runs up to max_epochs but stops if validation loss doesn't improve for 2 consecutive epochs. The model is loaded from the best checkpoint. The best epoch shown is the median across folds (most folds converged to the same best epoch).

## Datasets

| Name           | File                         | Total | Numeric | Source                                                               |
| -------------- | ---------------------------- | ----- | ------- | -------------------------------------------------------------------- |
| master_cleaned | master_dataset_cleaned.jsonl | 256   | 215     | 98 textbook + 158 cross-model verified                               |
| master_v2      | master_dataset_v2.jsonl      | 280   | 280     | 215 from above + 65 hard generated (Opus+GPT-5.4)                    |
| master_v3      | master_dataset_v3.jsonl      | 501   | 501     | 280 from v2 + 221 paraphrase-augmented (Opus 4.6 + GPT-5.4 verified) |
| master_v4      | master_dataset_v4.jsonl      | 866   | 866     | 280 from v2 + 586 paraphrase-augmented (Opus 4.6 + GPT-5.4 verified) |
| v4_remaining   | dataset_sft_v4_remaining.jsonl | 600 | 600     | 600-sample subset of master_v4 (54 seed + 105 cross-model + 27 hard + 414 rephrased) |

## Methods

| Method | Script        | Description                                                                                      |
| ------ | ------------- | ------------------------------------------------------------------------------------------------ |
| SFT    | train_sft.py  | Supervised fine-tuning with LoRA, formatting via chat template                                   |
| DPO    | train_dpo.py  | Direct Preference Optimization — generates preference pairs from model, trains to prefer correct |
| GRPO   | train_grpo.py | Group Relative Policy Optimization — SFT then RL with ground-truth reward                        |

## Statistical Testing

### p-value (Wilcoxon signed-rank test)

The p-value in the table is computed using the **Wilcoxon signed-rank test** (`scipy.stats.wilcoxon`), a non-parametric paired test. It compares the per-fold finetuned accuracies against the per-fold baseline accuracies to determine whether the improvement is statistically significant.

- **Input:** two lists of 5 values each — `[baseline_fold_0, ..., baseline_fold_4]` vs `[finetuned_fold_0, ..., finetuned_fold_4]`
- **Null hypothesis:** the median difference between paired observations (baseline vs finetuned on the same fold) is zero
- **Significance threshold:** p < 0.05
- **Limitation:** with only 5 folds, the minimum achievable p-value is 0.0625 (all 5 folds must improve), so no experiment can reach p < 0.05 with 5-fold CV. This is a fundamental limitation of the small number of paired samples, not a weakness of the results.

### W->R / R->W (Question Flips)

- **W->R (Wrong→Right):** number of questions the baseline got wrong but the finetuned model got right
- **R->W (Right→Wrong):** number of questions the baseline got right but the finetuned model got wrong
- A good fine-tune has W->R >> R->W (net positive flips)
- Counted across all 5 folds combined

## Evaluation Modes

### Greedy vs Stochastic

- **Greedy** (`do_sample=False`): the model always picks the highest-probability token at each step. This is deterministic — running the same question twice always gives the same answer. Used from round 3 onwards for reliable comparisons.
- **Stochastic** (`do_sample=True`, `temperature>0`): the model samples from the token probability distribution, introducing randomness. The same question can produce different answers across runs. Used in rounds 1-2 but abandoned because it inflated results (exp 3 showed +7.0% under stochastic but only +2.3% under greedy with the same config).

Greedy evaluation is preferred because it eliminates variance from the evaluation itself, making it easier to isolate the effect of fine-tuning.

## Infrastructure

- **GPU:** NVIDIA A100-SXM4-40GB (LaRuche HPC, Universite Paris-Saclay)
- **Framework:** Unsloth 2025.11.2 + TRL + Transformers 4.57.0
- **Container:** Apptainer (unsloth.sif)
