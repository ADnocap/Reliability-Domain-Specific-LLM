#!/bin/bash
#SBATCH --job-name=gsm-base
#SBATCH --nodes=1
#SBATCH --time=12:00:00
#SBATCH --gres=gpu:1
#SBATCH --partition=gpua100
#SBATCH --exclude=ruche-gpu11,ruche-gpu12,ruche-gpu15
#SBATCH --mem-per-cpu=12GB
#SBATCH --cpus-per-task=10
#SBATCH --output=logs/gsm8k_baseline_%j.out
#SBATCH --error=logs/gsm8k_baseline_%j.err

# Evaluate BASE Qwen3-8B on GSM8K (1319 math questions)
# Tests general math reasoning ability before fine-tuning

echo "=== GSM8K Baseline Evaluation ==="
echo "=== Job started at $(date) ==="
echo "Node: $(hostname)"

module load apptainer/1.4.4/gcc-15.1.0
cd $WORKDIR/reliability-sft

apptainer exec --nv --writable-tmpfs \
  --bind $WORKDIR:$WORKDIR:rw \
  --bind $WORKDIR/mytmp:/tmp \
  $WORKDIR/unsloth.sif \
  bash -c "
    export HF_HOME=$WORKDIR/.cache/huggingface && \
    export TRANSFORMERS_CACHE=$WORKDIR/.cache/huggingface/hub && \
    export SFT_TAG=qwen3-8b-aug866-8ep-es-10f && \
    export SFT_DATASET=master_dataset_v4.jsonl && \
    export SFT_FOLDS=10 && \
    export SFT_GSM8K_MODE=baseline && \
    cd $WORKDIR/reliability-sft && \
    pip install datasets --quiet 2>/dev/null && \
    python training/evaluate_gsm8k.py
  "

echo "=== Job finished at $(date) ==="
