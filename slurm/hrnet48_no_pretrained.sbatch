#!/usr/bin/bash
#SBATCH --job-name=hrnet32_final
#SBATCH --output=hrnet32_final.out
#SBATCH --error=hrnet32_final.err
#SBATCH -p gpu
#SBATCH --nodes=1
#SBATCH --gpus=1
#SBATCH -C GPU_MEM:16GB
#SBATCH --mem=16GB
#SBATCH --time=48:00:00

python3 tools/train.py configs/body_2d_keypoint/topdown_heatmap/infinity/hrnet48/td-hm_hrnet-w48_dark-8xb32-210e_no_pretrained.py --amp --resume


