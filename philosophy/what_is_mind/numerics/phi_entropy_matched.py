"""
phi_entropy_matched.py — Cycle 3
Numerical Track: what_is_mind

Residual confound from Cycle 2 Experiment A:
  When we zeroed back-edges to create a feedforward variant, the TPM entropy
  also dropped (H: 5.4 → 2.5). Phi dropped from 0.51 to 0.16. We cannot
  attribute the Phi reduction to topology vs entropy.

This module builds ENTROPY-MATCHED feedforward and recurrent networks:
  Both variants use the SAME sigmoid activation function, same weight magnitudes,
  same noise level. The ONLY difference is whether back-edges exist.

Construction:
  For a network of n nodes with state space {0,1}^n:
  - RC variant: W is a full n×n random weight matrix
  - FF variant: W is lower-triangular (W_ij = 0 for j >= i)
  To match entropy: both use the same sigma (noise level).
  We scale weights so that both produce the same average per-row TPM entropy.

Method: binary search over scale factor `s` such that the FF network's
TPM entropy matches the RC network's entropy.
"""

import itertools
import math
import time

import numpy as np

from phi_small_systems import phi_state, _bipartitions


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -30, 30)))


def build_tpm_from_weights(W: np.ndarray, bias: np.ndarray, n: int) -> np.ndarray:
    """
    Build a TPM from weight matrix W and bias vector.
    P(node_i' = 1 | state) = sigmoid(sum_j W_ij * state_j + bias_i)
    Transition probability is the product over nodes (independent given state).
    """
    n_states = 1 << n
    tpm = np.zeros((n_states, n_states))
    for s in range(n_states):
        state = np.array([(s >> j) & 1 for j in range(n)], dtype=float)
        probs = sigmoid(W @ state + bias)
        for s2 in range(n_states):
            prob = 1.0
            for i in range(n):
                bit = (s2 >> i) & 1
                prob *= probs[i] if bit == 1 else (1.0 - probs[i])
            tpm[s, s2] = prob
    return tpm


def tpm_entropy(tpm: np.ndarray) -> float:
    """Mean per-row Shannon entropy."""
    H = 0.0
    for row in tpm:
        row_H = -sum(p * math.log2(p) for p in row if p > 0)
        H += row_H
    return H / len(tpm)


def build_matched_pair(n: int, seed: int = 42, target_H: float = None,
                       scale_init: float = 1.0) -> dict:
    """
    Build entropy-matched (FF, RC) pair.

    Steps:
    1. Sample a random full weight matrix W_rc (recurrent) and W_ff (lower-tri).
    2. Compute TPMs for both. If entropies differ, scale W_ff until they match.
    3. Return both TPMs with confirmed matched entropy.
    """
    rng = np.random.default_rng(seed)

    # Recurrent: full weight matrix
    W_rc = rng.normal(0, scale_init, (n, n))
    bias = rng.normal(0, 0.1, n)
    tpm_rc = build_tpm_from_weights(W_rc, bias, n)
    H_rc = tpm_entropy(tpm_rc)

    # Feedforward: lower-triangular (j < i only; diagonal allowed = self-loops)
    # Use same scale as RC initially
    W_ff_raw = rng.normal(0, scale_init, (n, n))
    W_ff = np.tril(W_ff_raw, k=-1)  # strictly lower triangular (no self-loops)

    # Binary search to match entropy H_rc
    lo, hi = 0.0, 10.0
    for _ in range(60):
        scale_ff = (lo + hi) / 2.0
        W_ff_scaled = W_ff * scale_ff / max(scale_init, 1e-9)
        tpm_ff = build_tpm_from_weights(W_ff_scaled, bias, n)
        H_ff = tpm_entropy(tpm_ff)
        if abs(H_ff - H_rc) < 0.01:
            break
        if H_ff < H_rc:
            hi = scale_ff
        else:
            lo = scale_ff

    # Final
    W_ff_final = W_ff * scale_ff / max(scale_init, 1e-9)
    tpm_ff_final = build_tpm_from_weights(W_ff_final, bias, n)
    H_ff_final = tpm_entropy(tpm_ff_final)

    return {
        "tpm_rc": tpm_rc,
        "tpm_ff": tpm_ff_final,
        "H_rc": round(H_rc, 4),
        "H_ff": round(H_ff_final, 4),
        "H_delta": round(abs(H_rc - H_ff_final), 4),
        "scale_ff": round(scale_ff, 4),
    }


def run_entropy_matched_comparison(n: int = 6, reps: int = 5, n_seeds: int = 5):
    """
    Run the entropy-matched comparison across multiple seeds, collect Phi values.
    """
    n_states = 1 << n
    rng = np.random.default_rng(77)
    states = rng.integers(0, n_states, size=reps).tolist()

    all_rc_phi = []
    all_ff_phi = []
    all_H_delta = []

    print(f"  seed  H_rc  H_ff  ΔH    FF_Φ_mean  RC_Φ_mean  ratio(FF/RC)")
    print("-" * 65)

    for seed in range(n_seeds):
        pair = build_matched_pair(n=n, seed=seed)
        H_delta = pair["H_delta"]

        rc_phis = [phi_state(pair["tpm_rc"], s, n)[0] for s in states]
        ff_phis = [phi_state(pair["tpm_ff"], s, n)[0] for s in states]

        rc_mean = float(np.mean(rc_phis))
        ff_mean = float(np.mean(ff_phis))
        ratio = ff_mean / max(rc_mean, 1e-9)

        all_rc_phi.extend(rc_phis)
        all_ff_phi.extend(ff_phis)
        all_H_delta.append(H_delta)

        print(
            f"  {seed:<4}  {pair['H_rc']:.3f}  {pair['H_ff']:.3f}  "
            f"{H_delta:.3f}  {ff_mean:.4f}     {rc_mean:.4f}     {ratio:.3f}"
        )

    print("-" * 65)
    print(
        f"  mean                       "
        f"  {float(np.mean(all_ff_phi)):.4f}     {float(np.mean(all_rc_phi)):.4f}"
        f"     {float(np.mean(all_ff_phi))/max(float(np.mean(all_rc_phi)),1e-9):.3f}"
    )
    print()
    print(
        f"  IIT prediction: FF_Φ < RC_Φ  "
        f"→ {'CONFIRMED' if np.mean(all_ff_phi) < np.mean(all_rc_phi) else 'NOT CONFIRMED'}"
    )
    print(f"  Mean ΔH (entropy match quality): {float(np.mean(all_H_delta)):.4f}")

    return {
        "n": n,
        "ff_phi_mean": round(float(np.mean(all_ff_phi)), 6),
        "rc_phi_mean": round(float(np.mean(all_rc_phi)), 6),
        "ratio": round(float(np.mean(all_ff_phi)) / max(float(np.mean(all_rc_phi)), 1e-9), 4),
        "mean_H_delta": round(float(np.mean(all_H_delta)), 4),
    }


if __name__ == "__main__":
    import json

    print("=" * 72)
    print("ENTROPY-MATCHED Φ: FF vs RC — what_is_mind Cycle 3")
    print("Prediction: FF Φ < RC Φ, controlling for TPM entropy")
    print("=" * 72)

    for n in [4, 5, 6]:
        print(f"\n--- n={n} ---")
        result = run_entropy_matched_comparison(n=n, reps=4, n_seeds=4)
        print(json.dumps(result, indent=2))
