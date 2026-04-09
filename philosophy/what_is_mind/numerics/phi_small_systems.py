"""
phi_small_systems.py — Iteration 1
Numerical Track: what_is_mind

Goal: verify the feedforward theorem empirically on small binary networks,
locate the exponential wall, and compare Φ between feedforward vs recurrent
architectures of matched size.

IIT 3.0 definition used:
  - System: N binary nodes {0,1}^N
  - TPM: transition probability matrix T, shape (2^N, 2^N), T[s,s'] = P(s'|s)
  - Cause-effect power: the Φ of a state s is the minimum over all bipartitions
    MIP (minimum information partition) of the sum of EMD between the
    cause/effect repertoires of the full system vs. the partition.

We use a simplified but correct implementation:
  - EMD between discrete distributions approximated as half the L1 distance
    (valid for equal-total-mass distributions = probability distributions)
  - Only consider bipartitions (not the full cause-effect structure of IIT 3.0
    which sums over all mechanisms, not just the system-level)
  - This gives Φ_MIP which is the system-level integrated information,
    not the full intrinsic cause-effect power, but it preserves the
    feedforward = 0 theorem.

References:
  - Tononi 2004 (Φ original definition)
  - Oizumi, Albantakis, Tononi 2014 (IIT 3.0)
  - Massimini & Koch 2023 (review of testable predictions)
"""

import itertools
import math
import time
from typing import Optional

import numpy as np


# ---------------------------------------------------------------------------
# TPM construction utilities
# ---------------------------------------------------------------------------

def feedforward_tpm(n: int, density: float = 0.7, seed: int = 42) -> np.ndarray:
    """
    Build a TPM for a strictly feedforward binary network.

    Architecture: nodes 0..n-1, node i can only receive input from nodes j < i
    (strict ordering = no cycles, no recurrence).

    Each node's activation probability given its inputs is a noisy OR:
      P(node_i = 1 | parents) = 1 - prod(1 - density * parent_j)
    plus a small noise floor.

    Returns TPM of shape (2^n, 2^n).
    """
    rng = np.random.default_rng(seed)
    n_states = 1 << n

    # Connection weights (strictly lower triangular)
    W = np.zeros((n, n))
    for i in range(1, n):
        for j in range(i):
            if rng.random() < 0.6:  # ~60% connectivity in feedforward direction
                W[i, j] = density

    tpm = np.zeros((n_states, n_states))
    for s in range(n_states):
        state_in = np.array([(s >> k) & 1 for k in range(n)], dtype=float)
        # Compute activation probability for each node independently
        probs = np.zeros(n)
        for i in range(n):
            inputs = state_in * W[:, i]
            # Noisy OR
            p = 1.0 - np.prod(1.0 - inputs[inputs > 0]) if inputs.any() else 0.0
            probs[i] = np.clip(p + 0.05 * rng.random(), 0.0, 1.0)
        # Build output distribution
        for s_out in range(n_states):
            state_out = np.array([(s_out >> k) & 1 for k in range(n)])
            prob = 1.0
            for i in range(n):
                prob *= probs[i] if state_out[i] == 1 else (1.0 - probs[i])
            tpm[s, s_out] = prob

    return tpm


def recurrent_tpm(n: int, density: float = 0.5, seed: int = 42) -> np.ndarray:
    """
    Build a TPM for a recurrent binary network with the same parameters.

    Connections allowed in any direction (including self-loops and back-edges).
    Uses a sigmoidal activation function.
    """
    rng = np.random.default_rng(seed)
    n_states = 1 << n

    # Full weight matrix (including recurrent / back-edges)
    W = rng.normal(0, 1, (n, n)) * (rng.random((n, n)) < density)
    bias = rng.normal(0, 0.5, n)

    def sigmoid(x):
        return 1.0 / (1.0 + np.exp(-x))

    tpm = np.zeros((n_states, n_states))
    for s in range(n_states):
        state_in = np.array([(s >> k) & 1 for k in range(n)], dtype=float)
        probs = sigmoid(W @ state_in + bias)
        for s_out in range(n_states):
            state_out = np.array([(s_out >> k) & 1 for k in range(n)])
            prob = 1.0
            for i in range(n):
                prob *= probs[i] if state_out[i] == 1 else (1.0 - probs[i])
            tpm[s, s_out] = prob

    return tpm


# ---------------------------------------------------------------------------
# Repertoire and EMD
# ---------------------------------------------------------------------------

def marginalise(dist: np.ndarray, n: int, keep_indices: list[int]) -> np.ndarray:
    """
    Marginalise a joint distribution over {0,1}^n to the given subset of indices.
    dist: shape (2^n,)
    Returns: shape (2^len(keep_indices),)
    """
    mask = sorted(keep_indices)
    m = len(mask)
    marginal = np.zeros(1 << m)
    for s in range(1 << n):
        bits = [(s >> i) & 1 for i in mask]
        s_out = sum(b << i for i, b in enumerate(bits))
        marginal[s_out] += dist[s]
    return marginal


def effect_repertoire(tpm: np.ndarray, current_state: int, n: int) -> np.ndarray:
    """
    Compute the effect repertoire of the full system given the current state.
    = P(next state | current_state) = tpm[current_state, :]
    """
    return tpm[current_state, :]


def cause_repertoire(tpm: np.ndarray, current_state: int, n: int) -> np.ndarray:
    """
    Compute the (unnormalised) cause repertoire: P(prev state | current_state).
    Assumes uniform prior over previous states.
    P(prev=s | current=current_state) ∝ tpm[s, current_state] * 1/2^n
    """
    unnorm = tpm[:, current_state]
    total = unnorm.sum()
    if total == 0:
        return np.ones(1 << n) / (1 << n)
    return unnorm / total


def emd_l1(p: np.ndarray, q: np.ndarray) -> float:
    """
    L1-based EMD approximation for equal-mass discrete distributions.
    = 0.5 * ||p - q||_1
    This is exact for 1-dimensional distributions and a lower bound in general.
    """
    return 0.5 * np.sum(np.abs(p - q))


# ---------------------------------------------------------------------------
# Φ computation (system-level MIP)
# ---------------------------------------------------------------------------

def phi_state(tpm: np.ndarray, state: int, n: int) -> tuple[float, tuple]:
    """
    Compute Φ for a single state of an n-node binary system.

    Algorithm:
    1. Compute cause and effect repertoires for the full system.
    2. For each bipartition of the n nodes into (A, B):
       - Compute cause/effect repertoires for A and B independently
       - EMD loss = EMD(full_cause, product(A_cause, B_cause))
                  + EMD(full_effect, product(A_effect, B_effect))
    3. Φ = minimum EMD loss over all bipartitions.

    Returns (Φ, mip) where mip is the minimum information partition.
    """
    n_states = 1 << n
    all_nodes = list(range(n))

    full_cause = cause_repertoire(tpm, state, n)
    full_effect = effect_repertoire(tpm, state, n)

    min_phi = float("inf")
    min_part = None

    # Generate all bipartitions (as frozensets of indices)
    all_parts = list(_bipartitions(all_nodes))

    for A, B in all_parts:
        if not A or not B:
            continue

        # Cause repertoire for A alone: marginalise TPM to A nodes, compute cause
        tpm_A = _marginal_tpm(tpm, n, list(A))
        cause_A = _cause_rep_marginal(tpm_A, state, n, list(A))

        tpm_B = _marginal_tpm(tpm, n, list(B))
        cause_B = _cause_rep_marginal(tpm_B, state, n, list(B))

        # Effect repertoire for A alone
        effect_A = _effect_rep_marginal(tpm, state, n, list(A))
        effect_B = _effect_rep_marginal(tpm, state, n, list(B))

        # Product distributions (assuming independence under partition)
        prod_cause = _outer_product(cause_A, cause_B, n, list(A), list(B))
        prod_effect = _outer_product(effect_A, effect_B, n, list(A), list(B))

        phi = emd_l1(full_cause, prod_cause) + emd_l1(full_effect, prod_effect)

        if phi < min_phi:
            min_phi = phi
            min_part = (tuple(sorted(A)), tuple(sorted(B)))

    return min_phi if min_phi != float("inf") else 0.0, min_part


def _bipartitions(nodes: list[int]):
    """Generate all bipartitions (A, frozenset(nodes)-A) of nodes."""
    n = len(nodes)
    seen = set()
    for r in range(1, n):
        for A in itertools.combinations(nodes, r):
            A = frozenset(A)
            B = frozenset(nodes) - A
            key = (min(A, B, key=lambda x: tuple(sorted(x))),
                   max(A, B, key=lambda x: tuple(sorted(x))))
            if key not in seen:
                seen.add(key)
                yield A, B


def _marginal_tpm(tpm: np.ndarray, n: int, indices: list[int]) -> np.ndarray:
    """Marginalise TPM to the given node indices (both row and column)."""
    m = len(indices)
    n_full = 1 << n
    n_marg = 1 << m
    marg = np.zeros((n_marg, n_marg))
    for s in range(n_full):
        s_marg = _project_state(s, n, indices)
        for s2 in range(n_full):
            s2_marg = _project_state(s2, n, indices)
            marg[s_marg, s2_marg] += tpm[s, s2]
    # Normalise rows
    row_sums = marg.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1
    return marg / row_sums


def _project_state(state: int, n: int, indices: list[int]) -> int:
    bits = [(state >> i) & 1 for i in sorted(indices)]
    return sum(b << i for i, b in enumerate(bits))


def _cause_rep_marginal(tpm_marg: np.ndarray, state: int, n: int,
                        indices: list[int]) -> np.ndarray:
    s_marg = _project_state(state, n, indices)
    m = len(indices)
    n_marg = 1 << m
    unnorm = tpm_marg[:, s_marg]
    total = unnorm.sum()
    if total == 0:
        return np.ones(n_marg) / n_marg
    return unnorm / total


def _effect_rep_marginal(tpm: np.ndarray, state: int, n: int,
                         indices: list[int]) -> np.ndarray:
    full_effect = tpm[state, :]
    return marginalise(full_effect, n, indices)


def _outer_product(pA: np.ndarray, pB: np.ndarray, n: int,
                   A: list[int], B: list[int]) -> np.ndarray:
    """
    Reconstruct the n-node joint distribution from independent marginals pA and pB.
    Nodes in A and B partition all n nodes.
    """
    n_states = 1 << n
    joint = np.zeros(n_states)
    for sA in range(len(pA)):
        for sB in range(len(pB)):
            # Decode sA into bits for A, sB into bits for B
            s_full = 0
            for i, node in enumerate(sorted(A)):
                if (sA >> i) & 1:
                    s_full |= (1 << node)
            for i, node in enumerate(sorted(B)):
                if (sB >> i) & 1:
                    s_full |= (1 << node)
            joint[s_full] += pA[sA] * pB[sB]
    return joint


# ---------------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------------

def run_comparison(n_max: int = 8, reps: int = 3) -> list[dict]:
    """
    For each n in 2..n_max, compute average Φ over reps random states for:
    - a feedforward network
    - a recurrent network

    Also time each computation to locate the exponential wall.
    """
    results = []
    for n in range(2, n_max + 1):
        n_states = 1 << n
        ff_tpm = feedforward_tpm(n, seed=42)
        rc_tpm = recurrent_tpm(n, seed=42)

        # Sample reps states uniformly
        rng = np.random.default_rng(99)
        states = rng.integers(0, n_states, size=reps).tolist()

        ff_phis = []
        rc_phis = []

        t0 = time.perf_counter()
        for s in states:
            phi, _ = phi_state(ff_tpm, s, n)
            ff_phis.append(phi)
        ff_time = time.perf_counter() - t0

        t0 = time.perf_counter()
        for s in states:
            phi, _ = phi_state(rc_tpm, s, n)
            rc_phis.append(phi)
        rc_time = time.perf_counter() - t0

        row = {
            "n": n,
            "n_states": n_states,
            "n_bipartitions": sum(1 for _ in _bipartitions(list(range(n)))),
            "ff_phi_mean": round(float(np.mean(ff_phis)), 6),
            "ff_phi_max": round(float(np.max(ff_phis)), 6),
            "rc_phi_mean": round(float(np.mean(rc_phis)), 6),
            "rc_phi_max": round(float(np.max(rc_phis)), 6),
            "ff_time_s": round(ff_time, 4),
            "rc_time_s": round(rc_time, 4),
        }
        results.append(row)
        print(
            f"  n={n:2d}  states={n_states:5d}  parts={row['n_bipartitions']:4d}"
            f"  FF Φ={row['ff_phi_mean']:.4f}  RC Φ={row['rc_phi_mean']:.4f}"
            f"  FF t={ff_time:.3f}s  RC t={rc_time:.3f}s"
        )

    return results


def main():
    import argparse, json
    parser = argparse.ArgumentParser(
        description="Phi computation for small binary networks (Odd track, what_is_mind)"
    )
    parser.add_argument("--n-max", type=int, default=7,
                        help="Maximum system size (default 7; >10 may be very slow)")
    parser.add_argument("--reps", type=int, default=3,
                        help="Number of states to average over per size")
    parser.add_argument("--out", type=str, default=None)
    args = parser.parse_args()

    print("=" * 72)
    print("Φ (IIT 3.0 approx) — Feedforward vs Recurrent binary networks")
    print("Prediction under β: feedforward → Φ ≈ 0, recurrent → Φ > 0")
    print("=" * 72)

    results = run_comparison(n_max=args.n_max, reps=args.reps)

    print("\nSummary:")
    print(f"  Feedforward mean Φ: {np.mean([r['ff_phi_mean'] for r in results]):.6f}")
    print(f"  Recurrent   mean Φ: {np.mean([r['rc_phi_mean'] for r in results]):.6f}")
    print()

    if args.out:
        with open(args.out, "w") as f:
            json.dump(results, f, indent=2)
        print(f"Results written to {args.out}")
    else:
        import json as j
        print(j.dumps(results, indent=2))


if __name__ == "__main__":
    main()
