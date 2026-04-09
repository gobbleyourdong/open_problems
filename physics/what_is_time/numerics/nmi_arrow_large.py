#!/usr/bin/env python3
"""
nmi_arrow_large.py — NMI arrow of time with large gas simulation.

Problem with kramers_neural.py NMI: quantization noise ~0.01 vs ΔNMI ~0.004/step
→ not strictly monotone. Fix: use 1000-particle gas + grid histogram encoding.

Two encoding strategies:
  A) Raw float32 positions (8000 bytes) — more information, but gzip may struggle
  B) 20×20 grid histogram of uint16 counts (800 bytes) — coarser but more compressible

Strategy B should give cleaner gzip NMI because the histogram compresses well and
the coarse-graining removes short-wavelength noise that randomizes compression length.

Experiment:
  1. Simulate 1000-particle collision-free ideal gas in unit box for 200 steps.
  2. Encode each state as both raw float32 (A) and 20×20 histogram (B).
  3. Compute NMI(state_t, state_{t+τ}) for τ = 1, 2, 5, 10, 20, 50, 100 steps.
     Average over multiple reference frames t.
  4. Report whether NMI is monotone decreasing in τ for each encoding.

NMI via NCD: NMI ≈ 1 - NCD(x, y)
  NCD(x, y) = (C(xy) - min(C(x), C(y))) / max(C(x), C(y))
  C(z) = gzip compressed length.

Also: compute the grid Shannon entropy directly as a clean baseline
(not subject to gzip quantization noise).

Saves: results/nmi_arrow_large_data.json

Numerical track, what_is_time — 2026-04-09
"""

import math
import json
import os
import gzip
import struct
import random

# ── Simulation parameters ──────────────────────────────────────────────────────

N_PARTICLES = 1000
N_STEPS     = 200
DT          = 0.005         # time step (arbitrary units)
GRID_RES    = 20            # 20×20 grid for histogram encoding
LAGS        = [1, 2, 5, 10, 20, 50, 100]

# Number of reference frames to average over (skip first 10 as burn-in)
N_REFS      = 40
REF_START   = 10
REF_STRIDE  = 4             # sample every 4 steps to get ~40 refs in 200 steps

random.seed(42)

# ── Gas simulation ─────────────────────────────────────────────────────────────

def init_particles():
    """Initialize 1000 particles with random positions and velocities in unit box."""
    pos = [(random.random(), random.random()) for _ in range(N_PARTICLES)]
    # Start with all particles on left half (x < 0.5) to create initial non-equilibrium
    pos = [(random.random() * 0.5, random.random()) for _ in range(N_PARTICLES)]
    vel = [(random.gauss(0, 1) * 0.1, random.gauss(0, 1) * 0.1) for _ in range(N_PARTICLES)]
    return pos, vel


def step_gas(pos, vel):
    """Collision-free ballistic motion with periodic boundary conditions."""
    new_pos = []
    for i in range(N_PARTICLES):
        x = (pos[i][0] + vel[i][0] * DT) % 1.0
        y = (pos[i][1] + vel[i][1] * DT) % 1.0
        new_pos.append((x, y))
    return new_pos, vel   # velocities are constant (no collisions)


def run_simulation():
    """Run the full simulation, return list of position arrays."""
    pos, vel = init_particles()
    trajectory = [list(pos)]
    for _ in range(N_STEPS):
        pos, vel = step_gas(pos, vel)
        trajectory.append(list(pos))
    return trajectory   # length N_STEPS + 1


# ── Encoding functions ─────────────────────────────────────────────────────────

def encode_raw(pos):
    """Encode positions as sorted float32 bytes (8000 bytes for 1000 particles)."""
    sorted_pos = sorted(pos)
    buf = bytearray()
    for (x, y) in sorted_pos:
        buf += struct.pack('<f', x)
        buf += struct.pack('<f', y)
    return bytes(buf)


def encode_histogram(pos, grid_res=GRID_RES):
    """Encode positions as flattened 20×20 uint16 histogram (800 bytes)."""
    grid = [[0] * grid_res for _ in range(grid_res)]
    for (x, y) in pos:
        ix = min(int(x * grid_res), grid_res - 1)
        iy = min(int(y * grid_res), grid_res - 1)
        grid[ix][iy] += 1
    buf = bytearray()
    for row in grid:
        for count in row:
            buf += struct.pack('<H', count)   # uint16 little-endian
    return bytes(buf)


def compress(data):
    """Return gzip-compressed length."""
    return len(gzip.compress(data, compresslevel=9))


def ncd(x_bytes, y_bytes):
    """Normalized Compression Distance."""
    cx = compress(x_bytes)
    cy = compress(y_bytes)
    cxy = compress(x_bytes + y_bytes)
    return (cxy - min(cx, cy)) / max(cx, cy)


def nmi_from_ncd(x_bytes, y_bytes):
    """NMI ≈ 1 - NCD (clipped to [0,1])."""
    return max(0.0, min(1.0, 1.0 - ncd(x_bytes, y_bytes)))


# ── Grid entropy ───────────────────────────────────────────────────────────────

def grid_entropy(pos, grid_res=GRID_RES):
    """Shannon entropy of the 20×20 occupancy histogram."""
    grid = {}
    for (x, y) in pos:
        ix = min(int(x * grid_res), grid_res - 1)
        iy = min(int(y * grid_res), grid_res - 1)
        key = (ix, iy)
        grid[key] = grid.get(key, 0) + 1
    total = len(pos)
    H = 0.0
    for count in grid.values():
        p = count / total
        if p > 0:
            H -= p * math.log2(p)
    return H


# ── NMI computation ────────────────────────────────────────────────────────────

def compute_nmi_for_lag(trajectory_enc, lag):
    """
    Compute NMI between state_t and state_{t+lag} averaged over reference frames.
    trajectory_enc: list of encoded byte strings (one per timestep).
    """
    nmi_vals = []
    max_t = len(trajectory_enc) - 1
    refs = list(range(REF_START, min(REF_START + N_REFS * REF_STRIDE, max_t - lag + 1), REF_STRIDE))
    for t in refs:
        t2 = t + lag
        if t2 > max_t:
            break
        nmi = nmi_from_ncd(trajectory_enc[t], trajectory_enc[t2])
        nmi_vals.append(nmi)
    if not nmi_vals:
        return None, None
    mean_nmi = sum(nmi_vals) / len(nmi_vals)
    std_nmi = math.sqrt(sum((v - mean_nmi)**2 for v in nmi_vals) / max(len(nmi_vals) - 1, 1))
    return mean_nmi, std_nmi


# ── Main ───────────────────────────────────────────────────────────────────────

print("Running 1000-particle gas simulation for 200 steps...")
trajectory = run_simulation()
print(f"Trajectory length: {len(trajectory)} states")

# Encode all states
print("Encoding states (raw float32 and 20×20 histogram)...")
traj_raw  = [encode_raw(pos)       for pos in trajectory]
traj_hist = [encode_histogram(pos) for pos in trajectory]
print(f"  Raw state size:  {len(traj_raw[0])} bytes")
print(f"  Hist state size: {len(traj_hist[0])} bytes")
print(f"  Compressed raw[0]:  {compress(traj_raw[0])} bytes")
print(f"  Compressed hist[0]: {compress(traj_hist[0])} bytes")

# Entropy trajectory
print("\nGrid entropy trajectory (first 10 steps):")
entropies = [grid_entropy(pos) for pos in trajectory]
for i in [0, 1, 5, 10, 20, 50, 100, 150, 200]:
    print(f"  step {i:3d}: H = {entropies[i]:.4f} bits")

# Check monotonicity of entropy
entropy_increases = sum(1 for i in range(1, len(entropies)) if entropies[i] > entropies[i-1])
entropy_total = len(entropies) - 1
print(f"Entropy increases in {entropy_increases}/{entropy_total} steps ({100*entropy_increases/entropy_total:.1f}%)")

# NMI for each encoding
print("\n── NMI (raw float32 encoding) ───────────────────────────────────────────────")
print(f"{'Lag (steps)':>12}  {'NMI (mean)':>12}  {'NMI (std)':>10}")
print("-" * 40)

nmi_raw_data = []
for lag in LAGS:
    mean_nmi, std_nmi = compute_nmi_for_lag(traj_raw, lag)
    if mean_nmi is not None:
        print(f"{lag:>12}  {mean_nmi:>12.4f}  {std_nmi:>10.4f}")
        nmi_raw_data.append({"lag": lag, "nmi_mean": mean_nmi, "nmi_std": std_nmi})

print("\n── NMI (20×20 histogram encoding) ──────────────────────────────────────────")
print(f"{'Lag (steps)':>12}  {'NMI (mean)':>12}  {'NMI (std)':>10}")
print("-" * 40)

nmi_hist_data = []
for lag in LAGS:
    mean_nmi, std_nmi = compute_nmi_for_lag(traj_hist, lag)
    if mean_nmi is not None:
        print(f"{lag:>12}  {mean_nmi:>12.4f}  {std_nmi:>10.4f}")
        nmi_hist_data.append({"lag": lag, "nmi_mean": mean_nmi, "nmi_std": std_nmi})

# Check monotonicity
def check_monotone(data):
    vals = [d["nmi_mean"] for d in data]
    strictly = all(vals[i] > vals[i+1] for i in range(len(vals)-1))
    weak     = all(vals[i] >= vals[i+1] for i in range(len(vals)-1))
    return strictly, weak, vals

mono_raw_strict, mono_raw_weak, vals_raw = check_monotone(nmi_raw_data)
mono_hist_strict, mono_hist_weak, vals_hist = check_monotone(nmi_hist_data)

print(f"\nRaw float32:       strictly monotone = {mono_raw_strict}, weakly monotone = {mono_raw_weak}")
print(f"Histogram:         strictly monotone = {mono_hist_strict}, weakly monotone = {mono_hist_weak}")

# NMI range as diagnostic
print(f"\nNMI raw range:  [{min(vals_raw):.4f}, {max(vals_raw):.4f}]  Δ = {max(vals_raw) - min(vals_raw):.4f}")
print(f"NMI hist range: [{min(vals_hist):.4f}, {max(vals_hist):.4f}]  Δ = {max(vals_hist) - min(vals_hist):.4f}")

# ── Save results ──────────────────────────────────────────────────────────────

results = {
    "simulation_params": {
        "N_particles": N_PARTICLES,
        "N_steps": N_STEPS,
        "dt": DT,
        "grid_resolution": GRID_RES,
        "random_seed": 42,
        "N_reference_frames": N_REFS,
        "ref_start": REF_START,
        "ref_stride": REF_STRIDE,
    },
    "entropy_trajectory": {
        f"step_{i}": entropies[i] for i in [0, 1, 5, 10, 20, 50, 100, 150, 200]
    },
    "entropy_monotone_fraction": entropy_increases / entropy_total,
    "nmi_raw_float32": nmi_raw_data,
    "nmi_histogram_20x20": nmi_hist_data,
    "monotonicity": {
        "raw_strictly_monotone": mono_raw_strict,
        "raw_weakly_monotone": mono_raw_weak,
        "histogram_strictly_monotone": mono_hist_strict,
        "histogram_weakly_monotone": mono_hist_weak,
        "nmi_raw_range": max(vals_raw) - min(vals_raw),
        "nmi_hist_range": max(vals_hist) - min(vals_hist),
    },
}

out_path = os.path.join(os.path.dirname(__file__), "..", "results", "nmi_arrow_large_data.json")
out_path = os.path.normpath(out_path)
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\n[saved] {out_path}")

print("\nDone.")
