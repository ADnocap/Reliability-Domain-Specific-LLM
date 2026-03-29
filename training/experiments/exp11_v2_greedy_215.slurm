#!/bin/bash
#SBATCH --job-name=sft-g215
#SBATCH --nodes=1
#SBATCH --time=14:00:00
#SBATCH --gres=gpu:1
#SBATCH --partition=gpua100
#SBATCH --exclude=ruche-gpu11,ruche-gpu12,ruche-gpu15
#SBATCH --mem-per-cpu=12GB
#SBATCH --cpus-per-task=10
#SBATCH --output=logs/exp11_g215_%j.out
#SBATCH --error=logs/exp11_g215_%j.err

# Experiment 11: v2 config on 215 with greedy decoding
# Confirms the +7% result with deterministic baseline (no sampling noise)

echo "=== Experiment 11: v2 greedy on 215 ==="
echo "=== Job started at $(date) ==="
echo "Node: $(hostname)"
echo "GPU: $(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null || echo 'N/A')"

module load apptainer/1.4.4/gcc-15.1.0
cd $WORKDIR/reliability-sft

apptainer exec --nv --writable-tmpfs \
  --bind $WORKDIR:$WORKDIR:rw \
  --bind $WORKDIR/mytmp:/tmp \
  $WORKDIR/unsloth.sif \
  bash -c "
    export HF_HOME=$WORKDIR/.cache/huggingface && \
    export TRANSFORMERS_CACHE=$WORKDIR/.cache/huggingface/hub && \
    export SFT_TAG=qwen3-8b-v2-greedy-215 && \
    export SFT_LR=2e-4 && \
    export SFT_NEFTUNE=5 && \
    export SFT_LORA_DROPOUT=0.05 && \
    export SFT_EPOCHS=3 && \
    cd $WORKDIR/reliability-sft && \
    pip install scikit-learn scipy --quiet 2>/dev/null; \
    find /opt/conda -name '*.pyc' -delete 2>/dev/null; \
    echo '=== Step 1: Preparing data ===' && \
    python training/prepare_data.py && \
    echo '=== Step 2: Evaluating baseline ===' && \
    python training/evaluate_baseline.py && \
    echo '=== Step 3: Training SFT ===' && \
    python training/train_sft.py && \
    echo '=== Step 4: Evaluating finetuned ===' && \
    python training/evaluate_finetuned.py && \
    echo '=== Step 5: Aggregating results ===' && \
    python training/aggregate_results.py && \
    echo '=== Pipeline complete at \$(date) ==='
  "

echo "=== Job finished at $(date) ==="
