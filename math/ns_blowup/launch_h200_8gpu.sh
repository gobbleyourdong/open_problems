#!/bin/bash
# Launch 8 parallel jobs on 8×H200
# Each GPU gets one independent workload
# Results save to /root/gpu{N}/ — sync script pulls them all

mkdir -p /root/gpu{0,1,2,3,4,5,6,7}

# GPU 0: ν sweep at N=128 (ν=10⁻³, 10⁻⁴)
CUDA_VISIBLE_DEVICES=0 nohup python3 -u /root/omega_max_nu_sweep.py \
  --N 128 --nu-values "1e-3,1e-4" --seeds 50 --outdir /root/gpu0/ \
  > /root/gpu0/log.txt 2>&1 &

# GPU 1: ν sweep at N=128 (ν=10⁻⁵, 10⁻⁶)
CUDA_VISIBLE_DEVICES=1 nohup python3 -u /root/omega_max_nu_sweep.py \
  --N 128 --nu-values "1e-5,1e-6" --seeds 50 --outdir /root/gpu1/ \
  > /root/gpu1/log.txt 2>&1 &

# GPU 2: ν sweep at N=128 (ν=0, Euler)
CUDA_VISIBLE_DEVICES=2 nohup python3 -u /root/omega_max_nu_sweep.py \
  --N 128 --nu-values "0" --seeds 50 --outdir /root/gpu2/ \
  > /root/gpu2/log.txt 2>&1 &

# GPU 3: ν sweep at N=256 (ν=10⁻⁴, 10⁻⁵)
CUDA_VISIBLE_DEVICES=3 nohup python3 -u /root/omega_max_nu_sweep.py \
  --N 256 --nu-values "1e-4,1e-5" --seeds 20 --outdir /root/gpu3/ \
  > /root/gpu3/log.txt 2>&1 &

# GPU 4: ν sweep at N=256 (ν=0, Euler)
CUDA_VISIBLE_DEVICES=4 nohup python3 -u /root/omega_max_nu_sweep.py \
  --N 256 --nu-values "0" --seeds 20 --outdir /root/gpu4/ \
  > /root/gpu4/log.txt 2>&1 &

# GPU 5: Adversarial ICs at N=128 (Taylor-Green, Kida-Pelz)
CUDA_VISIBLE_DEVICES=5 nohup python3 -u /root/omega_max_adversarial.py \
  --N 128 --ics "taylor_green,kida_pelz" --seeds 50 --outdir /root/gpu5/ \
  > /root/gpu5/log.txt 2>&1 &

# GPU 6: Adversarial ICs at N=128 (vortex tube, high amplitude)
CUDA_VISIBLE_DEVICES=6 nohup python3 -u /root/omega_max_adversarial.py \
  --N 128 --ics "vortex_tube,high_amp" --seeds 50 --outdir /root/gpu6/ \
  > /root/gpu6/log.txt 2>&1 &

# GPU 7: Long time T=100 at N=64 (ν=10⁻⁴)
CUDA_VISIBLE_DEVICES=7 nohup python3 -u /root/omega_max_longtime.py \
  --N 64 --nu 1e-4 --T 100 --seeds 10 --outdir /root/gpu7/ \
  > /root/gpu7/log.txt 2>&1 &

echo "All 8 GPUs launched. Monitor with:"
echo "  tail -f /root/gpu*/log.txt"
echo "  nvidia-smi"
echo ""
echo "Sync to Spark with:"
echo "  bash sync_h200.sh  (on Spark)"
