# Fine-Tuning Pipeline: SFT on Reliability Engineering Dataset

5-fold cross-validation SFT pipeline using Unsloth LoRA on LaRuche A100 GPUs.

## Switching Models

Edit `training/config.py` to change the model:
```python
MODEL_NAME = "unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit"
MODEL_TAG = "llama3.1-8b"
```

All output paths are derived from `MODEL_TAG`, so results for different models are stored separately under `results/sft_cv_{MODEL_TAG}/`.

## Pipeline Steps

| Step | Script | Description |
|------|--------|-------------|
| 1 | `prepare_data.py` | Create 5-fold stratified CV splits |
| 2 | `evaluate_baseline.py` | Evaluate base model (no fine-tuning) per fold |
| 3 | `train_sft.py` | Fine-tune with LoRA per fold (~2 min/fold on A100) |
| 4 | `evaluate_finetuned.py` | Evaluate fine-tuned model per fold |
| 5 | `aggregate_results.py` | Combine results + Wilcoxon significance test |

## LaRuche Instructions

### 1. Upload repo

```bash
rsync -avz --exclude '.git' --exclude '__pycache__' --exclude '*.pyc' \
  . <username>@ruche.mesocentre.universite-paris-saclay.fr:$WORKDIR/reliability-sft/
```

### 2. SSH and setup

```bash
ssh <username>@ruche.mesocentre.universite-paris-saclay.fr
bash $WORKDIR/reliability-sft/training/setup_laruche.sh
```

### 3. Submit batch job

```bash
cd $WORKDIR/reliability-sft
sbatch training/run_pipeline.slurm
squeue -u <username>
```

### 4. Download results

```bash
scp -r <username>@ruche.mesocentre.universite-paris-saclay.fr:$WORKDIR/reliability-sft/results/ results/
```

## Output Structure

```
results/sft_cv_{MODEL_TAG}/
├── baseline/
│   ├── fold_{0-4}_results.json
│   └── summary.json
├── finetuned/
│   ├── fold_{0-4}_results.json
│   └── summary.json
├── adapters/
│   └── fold_{0-4}/
├── cv_comparison.csv
└── cv_summary.json
```

## Llama 3.1 8B Results

```
Baseline:   37.5% +/- 3.2%
Finetuned:  39.8% +/- 4.1%
Delta:      +2.4% (p=0.25, not significant)

By type:
  numeric: 41.4% -> 40.0% (-1.4%, n=215)
  formula: 33.3% -> 61.9% (+28.6%, n=21)
  text:     0.0% -> 15.8% (+15.8%, n=19)
```
