#!/usr/bin/env python3
"""
P vs NP: Empirical Framework — Measure the Gap Between Finding and Checking.

For each NP problem:
  - CHECKER: given a candidate solution, verify it in polynomial time
  - FINDER: given the problem, find a solution (best known algorithm)
  - MEASURE: the ratio finder_time / checker_time as problem size grows

If P = NP: the ratio should be polynomial (bounded by n^k for some k).
If P ≠ NP: the ratio should grow super-polynomially (exponential).

This framework tests from BOTH angles:
  1. Can we make the checker SLOWER? (approach P from above)
  2. Can we make the finder FASTER? (approach NP from below)

The GAP between best checker and best finder IS the P vs NP question,
measured empirically as a function of problem size.

Deps: numpy only.
"""

import numpy as np
import time
from itertools import combinations


# ============================================================================
# DOMAIN 1: SUBSET SUM
# Given a set S of integers and a target T, find a subset that sums to T.
# NP-complete. Checker: O(n). Finder: O(2^n) brute force, O(2^{n/2}) meet-in-middle.
# ============================================================================

def subset_sum_generate(n, max_val=1000):
    """Generate a random Subset Sum instance with a planted solution."""
    S = np.random.randint(1, max_val, size=n)
    # Plant a solution: pick a random subset
    k = np.random.randint(1, n)
    indices = np.random.choice(n, k, replace=False)
    T = int(np.sum(S[indices]))
    return S.tolist(), T, sorted(indices.tolist())

def subset_sum_check(S, T, subset_indices):
    """Check if the given subset sums to T. O(n)."""
    return sum(S[i] for i in subset_indices) == T

def subset_sum_find_brute(S, T, max_size=20):
    """Brute force finder. O(2^n)."""
    n = len(S)
    for r in range(1, n+1):
        for combo in combinations(range(n), r):
            if sum(S[i] for i in combo) == T:
                return list(combo)
    return None


# ============================================================================
# DOMAIN 2: GRAPH COLORING
# Given a graph G and k colors, find a valid k-coloring.
# NP-complete for k ≥ 3. Checker: O(m). Finder: O(k^n) brute force.
# ============================================================================

def graph_coloring_generate(n, edge_prob=0.3, k=3):
    """Generate a random graph with a planted k-coloring."""
    # Plant coloring first
    colors = np.random.randint(0, k, size=n)
    # Add edges only between different colors
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if colors[i] != colors[j] and np.random.random() < edge_prob:
                edges.append((i, j))
    return n, edges, k, colors.tolist()

def graph_coloring_check(n, edges, k, colors):
    """Check if coloring is valid. O(m)."""
    for i, j in edges:
        if colors[i] == colors[j]:
            return False
    return True

def graph_coloring_find_brute(n, edges, k, max_n=15):
    """Brute force k-coloring. O(k^n)."""
    if n > max_n: return None
    from itertools import product as iprod
    for coloring in iprod(range(k), repeat=n):
        valid = True
        for i, j in edges:
            if coloring[i] == coloring[j]:
                valid = False
                break
        if valid:
            return list(coloring)
    return None


# ============================================================================
# DOMAIN 3: SAT (Boolean Satisfiability)
# Given a CNF formula, find a satisfying assignment.
# THE canonical NP-complete problem. Checker: O(n·m). Finder: O(2^n).
# ============================================================================

def sat_generate(n_vars, n_clauses, clause_size=3):
    """Generate a random 3-SAT instance with a planted solution."""
    assignment = [np.random.choice([True, False]) for _ in range(n_vars)]
    clauses = []
    for _ in range(n_clauses):
        vars_in_clause = np.random.choice(n_vars, clause_size, replace=False)
        clause = []
        for v in vars_in_clause:
            # Ensure the clause is satisfied by the planted assignment
            if np.random.random() < 0.5:
                clause.append((v, True))  # positive literal
            else:
                clause.append((v, False))  # negative literal
        # Fix: make sure at least one literal is satisfied
        satisfied = any((assignment[v] == pos) for v, pos in clause)
        if not satisfied:
            # Flip one literal to match the assignment
            v, pos = clause[0]
            clause[0] = (v, assignment[v])
        clauses.append(clause)
    return n_vars, clauses, assignment

def sat_check(n_vars, clauses, assignment):
    """Check if assignment satisfies all clauses. O(n·m)."""
    for clause in clauses:
        satisfied = False
        for var, positive in clause:
            if positive and assignment[var]:
                satisfied = True
                break
            elif not positive and not assignment[var]:
                satisfied = True
                break
        if not satisfied:
            return False
    return True

def sat_find_brute(n_vars, clauses, max_vars=20):
    """Brute force SAT solver. O(2^n)."""
    if n_vars > max_vars: return None
    for bits in range(2**n_vars):
        assignment = [(bits >> i) & 1 == 1 for i in range(n_vars)]
        if sat_check(n_vars, clauses, assignment):
            return assignment
    return None


# ============================================================================
# DOMAIN 4: TRAVELING SALESMAN (Decision version)
# Given cities and distances, is there a tour of length ≤ L?
# NP-complete. Checker: O(n). Finder: O(n!) brute force, O(2^n n²) DP.
# ============================================================================

def tsp_generate(n, max_dist=100):
    """Generate random TSP with a planted short tour."""
    # Random distances
    dist = np.random.randint(1, max_dist, size=(n, n))
    dist = (dist + dist.T) // 2  # symmetric
    np.fill_diagonal(dist, 0)
    # Planted tour: 0, 1, 2, ..., n-1, 0
    tour = list(range(n))
    tour_length = sum(dist[tour[i]][tour[(i+1) % n]] for i in range(n))
    return dist.tolist(), tour_length + 10, tour  # L = tour_length + slack

def tsp_check(dist, L, tour):
    """Check if tour has length ≤ L. O(n)."""
    n = len(tour)
    length = sum(dist[tour[i]][tour[(i+1) % n]] for i in range(n))
    return length <= L

def tsp_find_brute(dist, L, max_n=10):
    """Brute force TSP. O(n!)."""
    n = len(dist)
    if n > max_n: return None
    from itertools import permutations
    for perm in permutations(range(n)):
        length = sum(dist[perm[i]][perm[(i+1) % n]] for i in range(n))
        if length <= L:
            return list(perm)
    return None


# ============================================================================
# THE FRAMEWORK: Measure checker_time vs finder_time across sizes
# ============================================================================

def measure_gap(domain_name, generate, check, find, sizes, n_trials=3):
    """Measure the empirical gap between checking and finding."""
    print(f"\n{'='*60}")
    print(f"DOMAIN: {domain_name}")
    print(f"{'='*60}")
    print(f"{'n':>5} | {'check (μs)':>12} | {'find (μs)':>12} | {'ratio':>10} | {'scaling':>10}")
    print("-" * 55)

    ratios = []
    for n in sizes:
        check_times = []
        find_times = []

        for _ in range(n_trials):
            # Generate instance
            instance = generate(n)

            # Time the checker
            t0 = time.perf_counter()
            for _ in range(100):  # repeat for timing accuracy
                result = check(*instance[:-1], instance[-1])
            check_t = (time.perf_counter() - t0) / 100

            # Time the finder
            t0 = time.perf_counter()
            solution = find(*instance[:-1])
            find_t = time.perf_counter() - t0

            if solution is not None:
                check_times.append(check_t)
                find_times.append(find_t)

        if check_times and find_times:
            avg_check = np.mean(check_times) * 1e6  # microseconds
            avg_find = np.mean(find_times) * 1e6
            ratio = avg_find / max(avg_check, 0.01)
            ratios.append((n, ratio))

            # Detect scaling: ratio ~ n^k (polynomial) or ~ 2^n (exponential)?
            scaling = "?"
            if len(ratios) >= 2:
                n1, r1 = ratios[-2]
                n2, r2 = ratios[-1]
                if r2 > 0 and r1 > 0:
                    log_ratio = np.log(r2/r1) / np.log(n2/n1) if n2 != n1 else 0
                    if log_ratio < 5:
                        scaling = f"~n^{log_ratio:.1f}"
                    else:
                        scaling = "EXPONENTIAL"

            print(f"{n:5d} | {avg_check:12.1f} | {avg_find:12.1f} | {ratio:10.1f} | {scaling:>10}")

    return ratios


def main():
    print("P vs NP EMPIRICAL FRAMEWORK")
    print("Measuring the gap between CHECKING and FINDING")
    print()

    # Subset Sum
    ratios_ss = measure_gap(
        "SUBSET SUM",
        lambda n: subset_sum_generate(n),
        lambda S, T, sol: subset_sum_check(S, T, sol),
        lambda S, T: subset_sum_find_brute(S, T),
        sizes=[8, 10, 12, 14, 16, 18, 20],
    )

    # 3-SAT
    ratios_sat = measure_gap(
        "3-SAT",
        lambda n: sat_generate(n, n_clauses=int(4.2*n)),
        lambda nv, cl, sol: sat_check(nv, cl, sol),
        lambda nv, cl: sat_find_brute(nv, cl),
        sizes=[6, 8, 10, 12, 14, 16],
    )

    # Graph Coloring
    ratios_gc = measure_gap(
        "GRAPH 3-COLORING",
        lambda n: graph_coloring_generate(n),
        lambda n, e, k, c: graph_coloring_check(n, e, k, c),
        lambda n, e, k: graph_coloring_find_brute(n, e, k),
        sizes=[6, 8, 10, 12],
    )

    # TSP
    ratios_tsp = measure_gap(
        "TRAVELING SALESMAN",
        lambda n: tsp_generate(n),
        lambda d, L, t: tsp_check(d, L, t),
        lambda d, L: tsp_find_brute(d, L),
        sizes=[5, 6, 7, 8, 9, 10],
    )

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY: The Checking-Finding Gap")
    print(f"{'='*60}")
    print()
    print("If P = NP: ratios should grow POLYNOMIALLY (n^k for fixed k).")
    print("If P ≠ NP: ratios should grow EXPONENTIALLY (2^n or worse).")
    print()
    for name, ratios in [("Subset Sum", ratios_ss), ("3-SAT", ratios_sat),
                          ("3-Coloring", ratios_gc), ("TSP", ratios_tsp)]:
        if len(ratios) >= 2:
            n1, r1 = ratios[0]
            n2, r2 = ratios[-1]
            if r1 > 0:
                growth = r2 / r1
                print(f"  {name:>15}: ratio grew {growth:.0f}× from n={n1} to n={n2}")


if __name__ == "__main__":
    main()
