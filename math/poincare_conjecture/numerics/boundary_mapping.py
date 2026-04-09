#!/usr/bin/env python3
"""
P vs NP: SOS-Style Boundary Mapping

WHERE exactly does polynomial become exponential?

For k-SAT: k=2 is in P, k=3 is NP-complete.
For graph coloring: k=2 is in P, k=3 is NP-complete.
For subset sum: bounded integers is pseudopoly, unbounded is NP-complete.

Map the BOUNDARY with the same methodology as NS SOS certificates:
measure a quantity (finder/checker ratio) as the "mode count" (k, constraint
tightness, etc.) increases. Look for the phase transition. Fit the scaling.

THE NS ANALOG:
  NS: c(N) = worst S²ê/|ω|² → decreases with N → regularity
  P vs NP: r(k) = finder_time/checker_time → increases with k → hardness

If we can find a quantity that MEASURES the P/NP gap and see how it scales,
that's the SOS certificate approach applied to complexity theory.
"""

import numpy as np
import time
from itertools import combinations


# ============================================================================
# EXPERIMENT 1: k-SAT for k = 2, 2.5, 3, 3.5, 4, 5
# (fractional k = mix of clause widths)
# ============================================================================

def mixed_ksat_generate(n_vars, alpha, k_mean):
    """Generate SAT with mixed clause widths centered at k_mean."""
    n_clauses = int(alpha * n_vars)
    clauses = []
    assignment = [np.random.choice([True, False]) for _ in range(n_vars)]

    for _ in range(n_clauses):
        # Clause width: k_mean ± 1, weighted
        if k_mean == int(k_mean):
            k = int(k_mean)
        else:
            k = int(k_mean) if np.random.random() < (1 - k_mean % 1) else int(k_mean) + 1
        k = max(2, min(k, n_vars))

        vs = np.random.choice(n_vars, k, replace=False)
        clause = [(int(v), bool(np.random.randint(2))) for v in vs]
        # Ensure satisfied
        if not any(assignment[v] == p for v, p in clause):
            v, _ = clause[0]
            clause[0] = (v, assignment[v])
        clauses.append(clause)
    return n_vars, clauses, assignment


def sat_check(n_vars, clauses, assignment):
    for clause in clauses:
        if not any(assignment[v] == p for v, p in clause):
            return False
    return True


def sat_find_brute(n_vars, clauses, max_vars=22):
    if n_vars > max_vars: return None
    for bits in range(2**n_vars):
        a = [(bits >> i) & 1 == 1 for i in range(n_vars)]
        if sat_check(n_vars, clauses, a):
            return a
    return None


# ============================================================================
# EXPERIMENT 2: Graph coloring k=2 (P) → k=3 (NP-complete)
# Interpolate with "soft" coloring: allow ε fraction of violations
# ============================================================================

def graph_generate(n, edge_prob=0.3):
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if np.random.random() < edge_prob:
                edges.append((i, j))
    return n, edges


def coloring_check(n, edges, k, colors, max_violations=0):
    violations = sum(1 for i, j in edges if colors[i] == colors[j])
    return violations <= max_violations


def coloring_find_brute(n, edges, k, max_n=16):
    if n > max_n: return None
    from itertools import product as iprod
    for colors in iprod(range(k), repeat=n):
        if all(colors[i] != colors[j] for i, j in edges):
            return list(colors)
    return None


# ============================================================================
# EXPERIMENT 3: Subset Sum with bounded vs unbounded integers
# Bounded by M: solvable in O(nM) pseudopolynomial time
# Unbounded: NP-complete
# ============================================================================

def subset_sum_dp(S, T):
    """Dynamic programming: O(n×T). Polynomial in T but T can be exponential in n."""
    n = len(S)
    if T < 0: return None
    if T > 10**6: return None  # too large for DP table
    dp = [False] * (T + 1)
    dp[0] = True
    parent = [None] * (T + 1)

    for i, val in enumerate(S):
        for t in range(T, val - 1, -1):
            if dp[t - val] and not dp[t]:
                dp[t] = True
                parent[t] = (i, t - val)

    if not dp[T]: return None
    result = []
    t = T
    while parent[t] is not None:
        idx, t_prev = parent[t]
        result.append(idx)
        t = t_prev
    return sorted(result)


# ============================================================================
# THE BOUNDARY MAP
# ============================================================================

def main():
    print("P vs NP: SOS-STYLE BOUNDARY MAPPING")
    print("="*60)
    print()

    # EXPERIMENT 1: k-SAT boundary
    print("EXPERIMENT 1: k-SAT — WHERE does polynomial become exponential?")
    print("-"*60)
    print(f"{'k':>5} | {'n=12 ratio':>10} | {'n=16 ratio':>10} | {'n=20 ratio':>10} | {'scaling':>10}")
    print("-"*55)

    for k in [2.0, 2.5, 3.0, 3.5, 4.0, 5.0]:
        ratios = []
        for n in [12, 16, 20]:
            alpha = 4.0 if k >= 3 else 2.0  # near-critical ratio
            cts, fts = [], []
            for _ in range(5):
                inst = mixed_ksat_generate(n, alpha, k)
                # Check
                t0 = time.perf_counter()
                for _ in range(100): sat_check(*inst[:-1], inst[-1])
                cts.append((time.perf_counter()-t0)/100*1e6)
                # Find
                t0 = time.perf_counter()
                sat_find_brute(*inst[:-1])
                fts.append((time.perf_counter()-t0)*1e6)
            c, f = np.mean(cts), np.mean(fts)
            ratios.append(f / max(c, 0.01))

        # Scaling from n=12 to n=20
        if ratios[0] > 0 and ratios[2] > 0:
            growth = ratios[2] / ratios[0]
            if growth > 100:
                scaling = "EXPONENTIAL"
            elif growth > 10:
                scaling = f"~n^{np.log(growth)/np.log(20/12):.1f}"
            else:
                scaling = "POLYNOMIAL"
        else:
            scaling = "?"

        print(f"{k:5.1f} | {ratios[0]:10.0f} | {ratios[1]:10.0f} | {ratios[2]:10.0f} | {scaling:>10}")

    # EXPERIMENT 2: Subset Sum bounded vs unbounded
    print(f"\nEXPERIMENT 2: Subset Sum — bounded (pseudopoly) vs unbounded (NP-complete)")
    print("-"*60)
    print(f"{'n':>5} | {'max_val':>8} | {'DP μs':>10} | {'brute μs':>10} | {'DP ratio':>10} | {'brute ratio':>10}")
    print("-"*60)

    for n in [12, 16, 20]:
        for max_val in [100, 10000]:
            S = np.random.randint(1, max_val, size=n).tolist()
            k = np.random.randint(1, n//2)
            T = sum(S[i] for i in np.random.choice(n, k, replace=False))

            # Check
            t0 = time.perf_counter()
            for _ in range(100):
                sum(S[i] for i in range(min(k, n))) == T
            ct = (time.perf_counter()-t0)/100*1e6

            # DP
            t0 = time.perf_counter()
            dp_result = subset_sum_dp(S, T)
            dp_t = (time.perf_counter()-t0)*1e6

            # Brute
            t0 = time.perf_counter()
            for r in range(1, n+1):
                found = False
                for combo in combinations(range(n), r):
                    if sum(S[i] for i in combo) == T:
                        found = True
                        break
                if found: break
            br_t = (time.perf_counter()-t0)*1e6

            print(f"{n:5d} | {max_val:8d} | {dp_t:10.0f} | {br_t:10.0f} | {dp_t/max(ct,.01):10.0f} | {br_t/max(ct,.01):10.0f}")

    # EXPERIMENT 3: The boundary NUMBER
    print(f"\nEXPERIMENT 3: THE BOUNDARY NUMBER — c(k) for k-SAT")
    print("-"*60)
    print("c(k) = finder_time / checker_time at fixed n=16, α=4.0")
    print("Analog of NS c(N) = S²ê/|ω|² — but INCREASING instead of DECREASING.")
    print()

    n = 16
    c_values = []
    for k in np.arange(2.0, 5.5, 0.5):
        cts, fts = [], []
        for _ in range(10):
            inst = mixed_ksat_generate(n, 4.0, k)
            t0 = time.perf_counter()
            for _ in range(100): sat_check(*inst[:-1], inst[-1])
            cts.append((time.perf_counter()-t0)/100*1e6)
            t0 = time.perf_counter()
            sat_find_brute(*inst[:-1])
            fts.append((time.perf_counter()-t0)*1e6)
        c_val = np.mean(fts) / max(np.mean(cts), 0.01)
        c_values.append((k, c_val))
        bar = "█" * min(50, int(np.log10(max(c_val, 1)) * 10))
        print(f"  k={k:.1f}: c(k) = {c_val:10.0f}  {bar}")

    print()
    print("THE NS ANALOG:")
    print("  NS:     c(N) DECREASES with N → regularity (depletion)")
    print("  P vs NP: c(k) INCREASES with k → hardness (complexity)")
    print()
    print("  NS: prove c(N) → 0. Done numerically (c≈1.2/N).")
    print("  P vs NP: prove c(k) → ∞. Obvious empirically.")
    print("  BUT: proving c(k) → ∞ for the BEST algorithm (not just brute force)")
    print("  is EXACTLY the P vs NP problem. The three barriers block this.")


if __name__ == "__main__":
    main()
