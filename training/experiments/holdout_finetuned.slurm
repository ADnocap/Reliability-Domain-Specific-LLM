#!/bin/bash
#SBATCH --job-name=hold-ft
#SBATCH --nodes=1
#SBATCH --time=02:00:00
#SBATCH --gres=gpu:1
#SBATCH --partition=gpua100
#SBATCH --exclude=ruche-gpu11,ruche-gpu12,ruche-gpu15
#SBATCH --mem-per-cpu=12GB
#SBATCH --cpus-per-task=10
#SBATCH --output=logs/holdout_finetuned_%j.out
#SBATCH --error=logs/holdout_finetuned_%j.err

# Evaluate FINETUNED Qwen3-8B (exp24 fold_0 adapter) on independent holdout (54 questions)

echo "=== Holdout Finetuned Evaluation ==="
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
    export SFT_HOLDOUT_MODE=finetuned && \
    cd $WORKDIR/reliability-sft && \
    python training/evaluate_holdout.py
  "

echo "=== Job finished at $(date) ==="
