"""
phi_controlled.py — Cycle 2
Numerical Track: what_is_mind

Controlled test of the IIT feedforward theorem.

Cycle 1 found that feedforward networks scored HIGHER Phi than recurrent ones,
opposite to IIT's prediction. Root cause: uncontrolled TPM statistics (different
activation functions, different densities). This module fixes that.

Two approaches:
  A. Matched-entropy TPMs: construct feedforward and recurrent networks by
     starting from IDENTICAL random TPMs, then surgically zero out back-edges
     for the feedforward variant. This ensures matched statistics.

  B. Theoretical feedforward test: construct a network where some nodes have
     state-INDEPENDENT transition probabilities (driven by external inputs).
     IIT predicts Phi=0 for such a network because the state-independent
     nodes contribute no cause-effect integration.

Approach A tests: does topology (FF vs RC) matter when statistics are held constant?
Approach B tests: does the feedforward theorem hold in its canonical form?
"""

import itertools
import math
import time
from typing import Optional

import numpy as np

from phi_small_systems import (
    phi_state,
    _bipartitions,
    feedforward_tpm,
    recurrent_tpm,
)


# ---------------------------------------------------------------------------
# Approach A: Matched-entropy TPMs
# ---------------------------------------------------------------------------

def random_tpm(n: int, seed: int = 42) -> np.ndarray:
    """
    Build a random TPM with no structural constraint.
    Each row is sampled from a Dirichlet(alpha=1) distribution (uniform over simplex).
    This gives a fully stochastic, maximally uncertain transition matrix.
    """
    rng = np.random.default_rng(seed)
    n_states = 1 << n
    tpm = rng.dirichlet(np.ones(n_states), size=n_states)
    return tpm


def feedforward_from_tpm(base_tpm: np.ndarray, n: int) -> np.ndarray:
    """
    Create a 'feedforward' version of a TPM by zeroing out transitions that
    would require back-edges, then renormalising.

    The feedforward constraint: the next state of node i can only depend on
    nodes 0..i in the current state, not on nodes i+1..n-1.

    Implementation: for each row (current state s), the transition probability
    to next state s' is set to zero if s' encodes a "1" for any node whose
    required-cause includes a node with higher index.

    Simpler approximation: zero out the least-significant half of the state space
    as valid "next states" — enforce that next_state[n//2:] is 0 (lower half of
    nodes drive upper half but not vice versa).

    Better: build a mask M[s, s'] = 1 if s' is "reachable" from s in a strictly
    feedforward manner, then set tpm[s, s'] = 0 for all unmasked entries.

    For simplicity: use the "block lower triangular" structure on binary state:
    s' must have the SAME upper bits as s for the upper nodes. This enforces that
    upper nodes don't affect lower nodes.
    """
    n_states = 1 << n
    split = n // 2  # first 'split' nodes are "lower layer"

    ff_tpm = base_tpm.copy()
    for s in range(n_states):
        for s2 in range(n_states):
            # Upper bits of s' must be determinable from lower bits of s only.
            # Zero out any transition where the upper bits of s' differ from
            # what the lower bits of s would imply.
            # Approximation: upper bits of s' must equal upper bits of s
            # (upper nodes can't change unless driven by lower nodes in SAME step)
            # This enforces: upper nodes are only driven by lower nodes.
            upper_s  = (s  >> split)
            upper_s2 = (s2 >> split)
            # Allow upper bits to change, but FORCE lower bits of s' to depend
            # only on lower bits of s: enforce s'_lower = f(s_lower) only.
            # Simplest: restrict to transitions where s'_upper = s_upper (upper
            # nodes don't change in one step from lower-node input).
            # This is a STRONG feedforward constraint.
            if upper_s != upper_s2:
                ff_tpm[s, s2] = 0.0

    # Renormalise rows
    row_sums = ff_tpm.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1.0
    ff_tpm = ff_tpm / row_sums
    return ff_tpm


def entropy_of_tpm(tpm: np.ndarray) -> float:
    """Mean per-row Shannon entropy of the TPM."""
    n_states = tpm.shape[0]
    H = 0.0
    for row in tpm:
        row_H = -sum(p * math.log2(p) for p in row if p > 0)
        H += row_H
    return H / n_states


# ---------------------------------------------------------------------------
# Approach B: Theoretical feedforward (state-independent nodes)
# ---------------------------------------------------------------------------

def state_independent_tpm(n: int, n_independent: int = 1, seed: int = 42) -> np.ndarray:
    """
    Build a TPM where the first n_independent nodes have state-INDEPENDENT
    transition probabilities (they are driven by "external input," not by
    the system state).

    IIT's feedforward theorem: if a node's transition is independent of the
    system state, it contributes zero cause-effect power. A system where ALL
    nodes are state-independent has Phi=0.

    This function builds:
    - Nodes 0..(n_independent-1): P(node_i' = 1) = p_i regardless of state
    - Nodes n_independent..(n-1): standard random transitions

    By progressively increasing n_independent from 0 to n, we track how Phi
    changes as more nodes become "feedforward/input-driven."
    """
    rng = np.random.default_rng(seed)
    n_states = 1 << n

    # Fixed output distributions for the "input" nodes (state-independent)
    input_probs = rng.uniform(0.1, 0.9, size=n_independent)

    # Full random TPM for the "processing" nodes
    base = rng.dirichlet(np.ones(n_states), size=n_states)

    # Build the final TPM
    tpm = np.zeros((n_states, n_states))
    for s in range(n_states):
        for s2 in range(n_states):
            # Factor over all nodes
            prob = 1.0
            for i in range(n):
                bit = (s2 >> i) & 1
                if i < n_independent:
                    # State-independent input node
                    p = input_probs[i]
                    prob *= p if bit == 1 else (1 - p)
                else:
                    # Processing node: depends on full current state
                    # Use the marginalised transition from base TPM
                    # (just use the prob from base[s, s2] split by this bit)
                    # Simplification: use base row normalised over this bit
                    p_1 = sum(base[s, s3] for s3 in range(n_states) if (s3 >> i) & 1)
                    p = p_1 if bit == 1 else (1 - p_1)
                    prob *= p
            tpm[s, s2] = prob

    # Renormalise
    row_sums = tpm.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1.0
    return tpm / row_sums


# ---------------------------------------------------------------------------
# Experiments
# ---------------------------------------------------------------------------

def experiment_a(n: int = 6, reps: int = 5, seed: int = 42) -> dict:
    """
    Matched-entropy comparison: start from the same base TPM, create FF and RC
    variants, compare Phi.
    """
    rng = np.random.default_rng(seed)
    n_states = 1 << n
    base = random_tpm(n, seed=seed)
    ff_tpm = feedforward_from_tpm(base, n)

    H_base = entropy_of_tpm(base)
    H_ff = entropy_of_tpm(ff_tpm)

    states = rng.integers(0, n_states, size=reps).tolist()

    t0 = time.perf_counter()
    base_phis = [phi_state(base, s, n)[0] for s in states]
    t_base = time.perf_counter() - t0

    t0 = time.perf_counter()
    ff_phis = [phi_state(ff_tpm, s, n)[0] for s in states]
    t_ff = time.perf_counter() - t0

    return {
        "n": n,
        "H_base": round(H_base, 4),
        "H_ff": round(H_ff, 4),
        "base_phi_mean": round(float(np.mean(base_phis)), 6),
        "ff_phi_mean": round(float(np.mean(ff_phis)), 6),
        "base_phi_max": round(float(np.max(base_phis)), 6),
        "ff_phi_max": round(float(np.max(ff_phis)), 6),
        "t_base_s": round(t_base, 3),
        "t_ff_s": round(t_ff, 3),
    }


def experiment_b(n: int = 5, reps: int = 10, seed: int = 42) -> list[dict]:
    """
    State-independent nodes: track Phi as we increase the number of input-driven
    (state-independent) nodes from 0 to n.

    IIT prediction: Phi decreases monotonically as more nodes become
    state-independent. At n_independent=n (all nodes), Phi=0.
    """
    rng = np.random.default_rng(seed)
    n_states = 1 << n
    states = rng.integers(0, n_states, size=reps).tolist()

    results = []
    for k in range(n + 1):
        tpm = state_independent_tpm(n, n_independent=k, seed=seed)
        phis = [phi_state(tpm, s, n)[0] for s in states]
        results.append({
            "n_independent": k,
            "n_total": n,
            "phi_mean": round(float(np.mean(phis)), 6),
            "phi_max": round(float(np.max(phis)), 6),
            "phi_min": round(float(np.min(phis)), 6),
        })
        print(
            f"  k={k}/{n} independent nodes  "
            f"Phi_mean={results[-1]['phi_mean']:.4f}  "
            f"Phi_max={results[-1]['phi_max']:.4f}"
        )
    return results


def main():
    import json

    print("=" * 72)
    print("CONTROLLED Phi COMPARISON — what_is_mind Cycle 2")
    print("=" * 72)

    # Experiment A: matched-entropy feedforward vs fully-random
    print("\n--- Experiment A: Matched-entropy FF vs base random TPM (n=6) ---")
    result_a = experiment_a(n=6, reps=5)
    print(f"  Base TPM:         H={result_a['H_base']:.3f}  Phi_mean={result_a['base_phi_mean']:.4f}")
    print(f"  Feedforward TPM:  H={result_a['H_ff']:.3f}  Phi_mean={result_a['ff_phi_mean']:.4f}")
    print(f"  Ratio FF/base: {result_a['ff_phi_mean']/max(result_a['base_phi_mean'],1e-9):.3f}")
    print(f"  (IIT predicts FF < base)")

    # Experiment B: state-independent nodes, n=5
    print("\n--- Experiment B: Phi vs n_independent nodes (n=5) ---")
    print("  IIT predicts: Phi decreases monotonically to 0 as k→n")
    result_b = experiment_b(n=5, reps=10)

    # Check monotone decrease
    phis = [r["phi_mean"] for r in result_b]
    is_monotone = all(phis[i] >= phis[i+1] for i in range(len(phis)-1))
    print(f"\n  Monotone decrease: {is_monotone}")
    print(f"  Phi at k=0 (all processing): {phis[0]:.4f}")
    print(f"  Phi at k=n (all independent): {phis[-1]:.4f}")
    print(f"  IIT prediction (Phi→0 at k=n): {'CONFIRMED' if phis[-1] < 0.01 else 'NOT confirmed (Phi=' + str(phis[-1]) + ')'}")

    print("\n" + json.dumps({"experiment_a": result_a, "experiment_b": result_b}, indent=2))


if __name__ == "__main__":
    main()
