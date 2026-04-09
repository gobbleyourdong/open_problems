"""
phi_star_approx.py — Cycle 5
Numerical Track: what_is_mind

Phi* approximation: instead of enumerating all 2^(n-1) bipartitions,
use a greedy minimum-spanning-tree approach to find the MIP (minimum
information partition) more efficiently.

Algorithm (Balduzzi & Tononi 2008 approximation):
  1. Build a pairwise "integration graph" where edge weight(i,j) =
     phi_pair(i, j) = the Phi of the 2-node subsystem {i,j}.
  2. The MIP is approximated by the minimum weight cut in this graph,
     computed via minimum spanning tree (Kruskal's algorithm on the
     complement: max spanning tree → min cut).
  3. The Phi* value is the minimum edge weight in the max-spanning tree
     (= the minimum cut value = approximate Phi).

This approximation:
  - Runs in O(n^2 * n_states^2) instead of O(2^n * n_states^2)
  - Accurate when the true MIP is a bipartition of individual elements
  - May underestimate Phi when the true MIP involves non-trivial groupings

Use: validate against exact Phi for n <= 8, then push to n = 10-12.
"""

import heapq
import itertools
import math
import time

import numpy as np
from phi_small_systems import (
    phi_state, marginalise, cause_repertoire, effect_repertoire, emd_l1,
    _marginal_tpm, _cause_rep_marginal, _effect_rep_marginal,
    _outer_product, _project_state, feedforward_tpm, recurrent_tpm,
)


# ---------------------------------------------------------------------------
# Pairwise Phi for a 2-node subsystem {i, j} embedded in n-node system
# ---------------------------------------------------------------------------

def phi_pair(tpm: np.ndarray, state: int, n: int, i: int, j: int) -> float:
    """
    Approximate the Phi contribution of the pair {i, j} within the full system.
    Uses the bipartition {i} vs {j} within the 2-node marginalised system.
    """
    indices = [i, j]
    m = 2

    # Marginalise TPM to just nodes i and j
    tpm_ij = _marginal_tpm(tpm, n, indices)
    s_ij = _project_state(state, n, indices)

    # Full cause/effect on the 2-node system
    full_cause = _cause_rep_marginal(tpm_ij, s_ij, n, indices)
    full_effect = _effect_rep_marginal(tpm, state, n, indices)

    # Bipartition {i} vs {j} (only bipartition of size-2 system)
    tpm_i = _marginal_tpm(tpm_ij, m, [0])   # node i within the 2-node system
    tpm_j = _marginal_tpm(tpm_ij, m, [1])   # node j

    si = s_ij & 1             # bit 0 = node i's value in state
    sj = (s_ij >> 1) & 1     # bit 1 = node j's value in state

    cause_i = _cause_rep_marginal(tpm_i, si, m, [0])
    cause_j = _cause_rep_marginal(tpm_j, sj, m, [1])
    effect_i = marginalise(full_effect, m, [0])
    effect_j = marginalise(full_effect, m, [1])

    prod_cause  = _outer_product(cause_i,  cause_j,  m, [0], [1])
    prod_effect = _outer_product(effect_i, effect_j, m, [0], [1])

    return emd_l1(full_cause, prod_cause) + emd_l1(full_effect, prod_effect)


# ---------------------------------------------------------------------------
# Phi* via minimum spanning tree on pairwise integration graph
# ---------------------------------------------------------------------------

def phi_star_state(tpm: np.ndarray, state: int, n: int) -> float:
    """
    Compute Phi* for a state using the pairwise integration graph + MST approach.

    1. Compute phi_pair(i, j) for all pairs.
    2. Build max spanning tree (high-integration pairs stay together).
    3. Phi* = min edge in the max spanning tree (= approximate MIP cut value).
    """
    if n < 2:
        return 0.0

    # Step 1: pairwise phi matrix
    pair_phi = {}
    for i in range(n):
        for j in range(i + 1, n):
            pair_phi[(i, j)] = phi_pair(tpm, state, n, i, j)

    # Step 2: max spanning tree (Prim's algorithm)
    # We want the max spanning tree of the integration graph,
    # then the MIP is the minimum-weight edge in this tree.
    in_tree = {0}
    max_st_edges = []

    while len(in_tree) < n:
        best_w = -1
        best_edge = None
        for u in in_tree:
            for v in range(n):
                if v not in in_tree:
                    key = (min(u, v), max(u, v))
                    w = pair_phi.get(key, 0.0)
                    if w > best_w:
                        best_w = w
                        best_edge = (u, v, w)
        if best_edge is None:
            break
        max_st_edges.append(best_edge)
        in_tree.add(best_edge[1])

    if not max_st_edges:
        return 0.0

    # Step 3: Phi* = min edge in max spanning tree
    return min(e[2] for e in max_st_edges)


# ---------------------------------------------------------------------------
# Validation: Phi* vs exact Phi for n = 4..8
# ---------------------------------------------------------------------------

def validate(n_max: int = 8, reps: int = 5):
    """Validate Phi* against exact Phi."""
    from phi_small_systems import feedforward_tpm, recurrent_tpm

    print(f"{'n':>3}  {'type':<4}  {'exact_mean':>10}  {'star_mean':>10}  "
          f"{'ratio':>7}  {'corr_r':>7}  {'t_exact':>8}  {'t_star':>7}")
    print("-" * 65)

    import numpy as np
    rng = np.random.default_rng(42)

    for n in range(4, n_max + 1):
        n_states = 1 << n
        states = rng.integers(0, n_states, size=reps).tolist()

        for label, tpm in [("FF", feedforward_tpm(n)), ("RC", recurrent_tpm(n))]:
            t0 = time.perf_counter()
            exact = [phi_state(tpm, s, n)[0] for s in states]
            t_exact = time.perf_counter() - t0

            t0 = time.perf_counter()
            star = [phi_star_state(tpm, s, n) for s in states]
            t_star = time.perf_counter() - t0

            from scipy.stats import spearmanr
            rho, _ = spearmanr(exact, star)

            ratio = np.mean(star) / max(np.mean(exact), 1e-9)
            print(
                f"{n:3d}  {label:<4}  {np.mean(exact):10.5f}  {np.mean(star):10.5f}  "
                f"{ratio:7.3f}  {rho:7.3f}  {t_exact:8.3f}s  {t_star:7.3f}s"
            )


# ---------------------------------------------------------------------------
# Push to larger n using Phi* only
# ---------------------------------------------------------------------------

def push_large_n(n_max: int = 12, reps: int = 3):
    """Use Phi* to push to larger n values."""
    print(f"\n{'n':>3}  {'FF_star':>9}  {'RC_star':>9}  {'ratio':>7}  "
          f"{'t_FF':>7}  {'t_RC':>7}  {'IIT_ok':>7}")
    print("-" * 55)

    rng = np.random.default_rng(99)
    for n in range(9, n_max + 1):
        n_states = 1 << n
        states = rng.integers(0, n_states, size=reps).tolist()

        ff_tpm = feedforward_tpm(n)
        rc_tpm = recurrent_tpm(n)

        t0 = time.perf_counter()
        ff_stars = [phi_star_state(ff_tpm, s, n) for s in states]
        t_ff = time.perf_counter() - t0

        t0 = time.perf_counter()
        rc_stars = [phi_star_state(rc_tpm, s, n) for s in states]
        t_rc = time.perf_counter() - t0

        ff_m = float(np.mean(ff_stars))
        rc_m = float(np.mean(rc_stars))
        ratio = ff_m / max(rc_m, 1e-9)
        ok = "YES" if ff_m < rc_m else "NO "

        print(
            f"{n:3d}  {ff_m:9.5f}  {rc_m:9.5f}  {ratio:7.3f}  "
            f"{t_ff:7.3f}s  {t_rc:7.3f}s  {ok}"
        )


if __name__ == "__main__":
    print("=" * 72)
    print("PHI* APPROXIMATION — what_is_mind Cycle 5")
    print("=" * 72)
    print("\nA. Validation: Phi* vs exact Phi (n=4..8)")
    validate(n_max=8, reps=5)
    print("\nB. Larger n using Phi* only (n=9..12)")
    push_large_n(n_max=12, reps=3)
