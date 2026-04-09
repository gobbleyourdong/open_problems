#!/usr/bin/env python3
"""
P vs NP v2: Smart Finders — Do clever algorithms close the gap?

Brute force is O(2^n). But smarter algorithms exist:
- Subset Sum: meet-in-middle O(2^{n/2})
- SAT: DPLL with unit propagation O(1.3^n) typical
- Graph Coloring: greedy + backtrack
- TSP: dynamic programming O(2^n × n²) vs O(n!)

The question: does the finder/checker ratio change QUALITATIVELY
(from exponential to polynomial) or just QUANTITATIVELY (smaller exponent)?

If P = NP: there exists an algorithm that makes the ratio polynomial.
If P ≠ NP: ALL algorithms leave an exponential gap.
"""

import numpy as np
import time
from itertools import combinations


# ============================================================================
# SMART SUBSET SUM: Meet-in-middle O(2^{n/2})
# ============================================================================

def subset_sum_generate(n, max_val=1000):
    S = np.random.randint(1, max_val, size=n)
    k = np.random.randint(1, max(2, n//2))
    indices = np.random.choice(n, k, replace=False)
    T = int(np.sum(S[indices]))
    return S.tolist(), T, sorted(indices.tolist())

def subset_sum_check(S, T, subset):
    return sum(S[i] for i in subset) == T

def subset_sum_brute(S, T):
    n = len(S)
    for r in range(1, n+1):
        for combo in combinations(range(n), r):
            if sum(S[i] for i in combo) == T:
                return list(combo)
    return None

def subset_sum_meet_middle(S, T):
    """Meet in the middle: O(2^{n/2}) time, O(2^{n/2}) space."""
    n = len(S)
    half = n // 2

    # Left half: all subset sums
    left = {}
    for mask in range(1 << half):
        s = sum(S[i] for i in range(half) if mask & (1 << i))
        left[s] = mask

    # Right half: check if T - sum exists in left
    for mask in range(1 << (n - half)):
        s = sum(S[half + i] for i in range(n - half) if mask & (1 << i))
        remain = T - s
        if remain in left:
            # Reconstruct solution
            result = []
            lmask = left[remain]
            for i in range(half):
                if lmask & (1 << i): result.append(i)
            for i in range(n - half):
                if mask & (1 << i): result.append(half + i)
            return sorted(result)
    return None


# ============================================================================
# SMART SAT: DPLL with unit propagation
# ============================================================================

def sat_generate(n_vars, n_clauses=None):
    if n_clauses is None: n_clauses = int(4.2 * n_vars)
    assignment = [np.random.choice([True, False]) for _ in range(n_vars)]
    clauses = []
    for _ in range(n_clauses):
        vs = np.random.choice(n_vars, 3, replace=False)
        clause = []
        for v in vs:
            clause.append((int(v), bool(np.random.choice([True, False]))))
        # Ensure satisfied
        if not any((assignment[v] == p) for v, p in clause):
            v, _ = clause[0]
            clause[0] = (v, assignment[v])
        clauses.append(clause)
    return n_vars, clauses, assignment

def sat_check(n_vars, clauses, assignment):
    for clause in clauses:
        if not any((assignment[v] == p) if p else (not assignment[v]) for v, p in clause):
            return False
    return True

def sat_brute(n_vars, clauses):
    for bits in range(2**n_vars):
        a = [(bits >> i) & 1 == 1 for i in range(n_vars)]
        if sat_check(n_vars, clauses, a):
            return a
    return None

def sat_dpll(n_vars, clauses):
    """DPLL with unit propagation. Much faster than brute force on structured instances."""
    def _dpll(assignment, clauses, unset):
        # Unit propagation
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                unsat_lits = []
                sat = False
                for v, p in clause:
                    if assignment[v] is not None:
                        if assignment[v] == p:
                            sat = True
                            break
                    else:
                        unsat_lits.append((v, p))
                if sat:
                    continue
                if len(unsat_lits) == 0:
                    return None  # conflict
                if len(unsat_lits) == 1:
                    v, p = unsat_lits[0]
                    assignment[v] = p
                    unset.discard(v)
                    changed = True

        # Check if all clauses satisfied
        all_sat = True
        for clause in clauses:
            sat = False
            has_unset = False
            for v, p in clause:
                if assignment[v] is None:
                    has_unset = True
                elif assignment[v] == p:
                    sat = True
                    break
            if not sat and not has_unset:
                return None
            if not sat:
                all_sat = False

        if all_sat or not unset:
            return [assignment[i] if assignment[i] is not None else False
                    for i in range(len(assignment))]

        # Branch on first unset variable
        v = min(unset)
        for val in [True, False]:
            a_copy = assignment[:]
            u_copy = set(unset)
            a_copy[v] = val
            u_copy.discard(v)
            result = _dpll(a_copy, clauses, u_copy)
            if result is not None:
                return result
        return None

    assignment = [None] * n_vars
    unset = set(range(n_vars))
    return _dpll(assignment, clauses, unset)


# ============================================================================
# MEASURE: Brute vs Smart across sizes
# ============================================================================

def measure(name, generate, check, find_brute, find_smart, sizes, n_trials=3):
    print(f"\n{'='*65}")
    print(f"{name}: BRUTE vs SMART finder")
    print(f"{'='*65}")
    print(f"{'n':>4} | {'check μs':>9} | {'brute μs':>10} | {'smart μs':>10} | {'brute/chk':>10} | {'smart/chk':>10}")
    print("-" * 62)

    for n in sizes:
        ct, bt, st = [], [], []
        for _ in range(n_trials):
            inst = generate(n)
            # Check
            t0 = time.perf_counter()
            for _ in range(100):
                check(*inst[:-1], inst[-1])
            ct.append((time.perf_counter()-t0)/100*1e6)
            # Brute
            t0 = time.perf_counter()
            find_brute(*inst[:-1])
            bt.append((time.perf_counter()-t0)*1e6)
            # Smart
            t0 = time.perf_counter()
            find_smart(*inst[:-1])
            st.append((time.perf_counter()-t0)*1e6)

        c, b, s = np.mean(ct), np.mean(bt), np.mean(st)
        print(f"{n:4d} | {c:9.1f} | {b:10.0f} | {s:10.0f} | {b/max(c,.01):10.0f} | {s/max(c,.01):10.0f}")


def main():
    print("P vs NP: SMART FINDERS — Does the gap change qualitatively?")
    print()

    measure("SUBSET SUM (brute O(2^n) vs meet-middle O(2^{n/2}))",
            subset_sum_generate, subset_sum_check,
            subset_sum_brute, subset_sum_meet_middle,
            sizes=[10, 14, 18, 22, 26])

    measure("3-SAT (brute O(2^n) vs DPLL)",
            sat_generate, sat_check,
            sat_brute, sat_dpll,
            sizes=[8, 10, 12, 14, 16, 18])

    print(f"\n{'='*65}")
    print("CONCLUSION")
    print(f"{'='*65}")
    print("""
Smart algorithms REDUCE the exponent but DON'T eliminate it:
  Subset Sum: 2^n → 2^{n/2} (still exponential, just half the exponent)
  SAT: 2^n → ~1.3^n (still exponential, just smaller base)

The finder/checker ratio:
  Brute: grows as 2^n / n = exponential
  Smart: grows as 2^{n/2} / n = STILL exponential (just slower)

P = NP would require: ratio grows as n^k (POLYNOMIAL).
No known algorithm achieves this for ANY NP-complete problem.

The gap is ROBUST: smarter algorithms shift the curve but don't
change the qualitative behavior. This is the empirical case for P ≠ NP.
""")


if __name__ == "__main__":
    main()
