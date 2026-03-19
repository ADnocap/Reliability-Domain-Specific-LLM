#!/bin/bash
# Run once on LaRuche login node after uploading repo
# Usage: bash $WORKDIR/reliability-sft/training/setup_laruche.sh

cd $WORKDIR

mkdir -p reliability-sft/data/cv_splits
mkdir -p reliability-sft/logs
mkdir -p mytmp

echo "Directory structure created."
echo ""
echo "Setup complete. Ready to sbatch."
echo "  cd \$WORKDIR/reliability-sft"
echo "  sbatch training/run_pipeline.slurm"
