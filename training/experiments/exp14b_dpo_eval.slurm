#!/bin/bash
#SBATCH --job-name=dpo-eval
#SBATCH --nodes=1
#SBATCH --time=06:00:00
#SBATCH --gres=gpu:1
#SBATCH --partition=gpua100
#SBATCH --exclude=ruche-gpu11,ruche-gpu12,ruche-gpu15
#SBATCH --mem-per-cpu=12GB
#SBATCH --cpus-per-task=10
#SBATCH --output=logs/exp14b_dpo_eval_%j.out
#SBATCH --error=logs/exp14b_dpo_eval_%j.err

echo "=== DPO eval-only ==="
echo "=== Job started at $(date) ==="
module load apptainer/1.4.4/gcc-15.1.0
cd $WORKDIR/reliability-sft

apptainer exec --nv --writable-tmpfs \
  --bind $WORKDIR:$WORKDIR:rw \
  --bind $WORKDIR/mytmp:/tmp \
  $WORKDIR/unsloth.sif \
  bash -c "
    export HF_HOME=$WORKDIR/.cache/huggingface && \
    export TRANSFORMERS_CACHE=$WORKDIR/.cache/huggingface/hub && \
    export SFT_TAG=qwen3-8b-dpo-215 && \
    cd $WORKDIR/reliability-sft && \
    pip install scikit-learn scipy --quiet 2>/dev/null; \
    find /opt/conda -name '*.pyc' -delete 2>/dev/null; \
    echo '=== Evaluating DPO finetuned ===' && \
    python training/evaluate_finetuned.py && \
    echo '=== Done ==='
  "

echo "=== Job finished at $(date) ==="
