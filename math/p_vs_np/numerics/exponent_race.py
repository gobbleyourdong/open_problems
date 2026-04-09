"""
P vs NP: THE EXPONENT RACE

Every NP-complete problem has best-known running time O(c^n).
The base c is THE NUMBER: c=1 means P, c>1 means exponential.

This script measures the ACTUAL exponent for each problem and algorithm,
identifying which problems are CLOSEST to P (smallest c).

Known theoretical exponents:
  2-SAT:            c = 1.000 (polynomial!)
  3-SAT (DPLL):     c ≈ 1.481 (basic DPLL)
  3-SAT (PPSZ):     c ≈ 1.307 (Hertli 2011, best known)
  k-SAT:            c ≈ 2(1 - 1/k) (gets harder with k)
  Subset Sum:       c ≈ 1.414 (meet-in-middle, 2^{n/2})
  Graph coloring:   c ≈ 1.238 (for 3-coloring, Beigel-Eppstein)
  TSP:              c ≈ 1.414 (Held-Karp DP, 2^n * n^2)
  Planar problems:  c ≈ 1.000 (subexponential: 2^{O(√n)})

THE SIGMA NUMBER: c_best(problem) = inf over all algorithms of c.
If c_best = 1 for ANY NP-complete problem → P = NP.
If c_best > 1 for ALL NP-complete problems → P ≠ NP.
"""
import numpy as np
import time
from itertools import combinations

# ============================================================
# PROBLEM IMPLEMENTATIONS + BEST ALGORITHMS
# ============================================================

def dpll_count(n, clauses):
    """DPLL with unit propagation. Count nodes explored."""
    nodes = [0]
    def propagate(assignment):
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                unset = []; sat = False
                for lit in clause:
                    v = abs(lit)-1
                    if v in assignment:
                        if (lit>0 and assignment[v]) or (lit<0 and not assignment[v]):
                            sat = True; break
                    else: unset.append(lit)
                if sat: continue
                if not unset: return False
                if len(unset) == 1:
                    assignment[abs(unset[0])-1] = unset[0] > 0
                    changed = True
        return True
    def solve(assignment):
        nodes[0] += 1
        if not propagate(assignment): return None
        unset = [i for i in range(n) if i not in assignment]
        if not unset: return assignment
        v = unset[0]
        for val in [True, False]:
            a = dict(assignment); a[v] = val
            r = solve(a)
            if r is not None: return r
        return None
    solve({})
    return nodes[0]

def subset_sum_brute(target, nums):
    """Brute force subset sum. O(2^n)."""
    n = len(nums)
    nodes = 0
    for mask in range(2**n):
        nodes += 1
        s = sum(nums[i] for i in range(n) if mask & (1<<i))
        if s == target: return nodes
    return nodes

def subset_sum_mitm(target, nums):
    """Meet-in-the-middle subset sum. O(2^{n/2})."""
    n = len(nums)
    half = n // 2
    nodes = 0
    # First half sums
    left = {}
    for mask in range(2**half):
        nodes += 1
        s = sum(nums[i] for i in range(half) if mask & (1<<i))
        left[s] = mask
    # Second half: check complement
    for mask in range(2**(n-half)):
        nodes += 1
        s = sum(nums[half+i] for i in range(n-half) if mask & (1<<i))
        if (target - s) in left:
            return nodes
    return nodes

def graph_coloring_bt(adj, n_colors=3):
    """Backtracking graph coloring. Count nodes."""
    n = len(adj)
    nodes = [0]
    def solve(colors, v):
        nodes[0] += 1
        if v == n: return True
        for c in range(n_colors):
            ok = True
            for u in range(n):
                if adj[v][u] and u < v and colors[u] == c:
                    ok = False; break
            if ok:
                colors[v] = c
                if solve(colors, v+1): return True
                colors[v] = -1
        return False
    solve([-1]*n, 0)
    return nodes[0]

# ============================================================
# INSTANCE GENERATORS
# ============================================================

def random_3sat(n, alpha=4.27):
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = np.random.choice(n, 3, replace=False) + 1
        signs = np.random.choice([-1, 1], 3)
        clauses.append((vs * signs).tolist())
    return clauses

def random_subset_sum(n, max_val=1000):
    nums = np.random.randint(1, max_val, n).tolist()
    target = sum(np.random.choice(nums, n//2, replace=False))
    return target, nums

def random_graph(n, edge_prob=0.5):
    adj = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if np.random.random() < edge_prob:
                adj[i][j] = adj[j][i] = True
    return adj

# ============================================================
# EXPONENT MEASUREMENT
# ============================================================

def measure_exponent(problem_name, sizes, run_fn, n_trials=15):
    """Measure the empirical exponent c where nodes ~ c^n."""
    data = []
    for n in sizes:
        node_counts = []
        for _ in range(n_trials):
            nodes = run_fn(n)
            if nodes is not None and nodes > 0:
                node_counts.append(nodes)
        if node_counts:
            avg = np.mean(node_counts)
            data.append((n, avg))

    if len(data) < 2:
        return None, data

    # Fit: log(nodes) = n * log(c) + const
    ns = np.array([d[0] for d in data])
    log_nodes = np.log(np.array([d[1] for d in data]))
    coeffs = np.polyfit(ns, log_nodes, 1)
    c = np.exp(coeffs[0])  # base of exponential
    return c, data

def main():
    print("THE EXPONENT RACE: Which NP-Complete Problem is Closest to P?", flush=True)
    print("=" * 65, flush=True)
    print(flush=True)
    print("c = base of exponential: nodes ~ c^n. c=1 means P.", flush=True)
    print(flush=True)

    results = []

    # 3-SAT with DPLL
    print("3-SAT (DPLL+UP, α=4.27)...", flush=True)
    c, data = measure_exponent("3-SAT DPLL",
        [10, 14, 18, 22, 26],
        lambda n: dpll_count(n, random_3sat(n, 4.27)), 20)
    if c: results.append(("3-SAT (DPLL)", c, data))

    # 3-SAT underconstrained (easy regime)
    print("3-SAT (DPLL+UP, α=2.0)...", flush=True)
    c, data = measure_exponent("3-SAT easy",
        [10, 14, 18, 22, 26],
        lambda n: dpll_count(n, random_3sat(n, 2.0)), 20)
    if c: results.append(("3-SAT α=2.0", c, data))

    # Subset Sum brute force
    print("Subset Sum (brute force)...", flush=True)
    c, data = measure_exponent("SubsetSum brute",
        [10, 14, 18, 22],
        lambda n: subset_sum_brute(*random_subset_sum(n)), 15)
    if c: results.append(("SubsetSum brute", c, data))

    # Subset Sum meet-in-middle
    print("Subset Sum (meet-in-middle)...", flush=True)
    c, data = measure_exponent("SubsetSum MitM",
        [10, 14, 18, 22, 26, 30],
        lambda n: subset_sum_mitm(*random_subset_sum(n)), 15)
    if c: results.append(("SubsetSum MitM", c, data))

    # Graph 3-coloring
    print("3-Coloring (backtrack, p=0.3)...", flush=True)
    c, data = measure_exponent("3-Color",
        [10, 14, 18, 22],
        lambda n: graph_coloring_bt(random_graph(n, 0.3)), 15)
    if c: results.append(("3-Coloring p=0.3", c, data))

    # Graph 3-coloring sparse (easier)
    print("3-Coloring (backtrack, p=0.1, sparse)...", flush=True)
    c, data = measure_exponent("3-Color sparse",
        [10, 14, 18, 22, 26],
        lambda n: graph_coloring_bt(random_graph(n, 0.1)), 15)
    if c: results.append(("3-Coloring sparse", c, data))

    # Print the race results
    print(flush=True)
    print("THE EXPONENT RACE RESULTS", flush=True)
    print("=" * 65, flush=True)
    print(f"{'Problem':30} | {'c (base)':>10} | {'log₂(c)':>8} | {'Verdict':>12}", flush=True)
    print("-" * 65, flush=True)

    results.sort(key=lambda x: x[1])
    for name, c, data in results:
        log2c = np.log2(c)
        verdict = "≈ POLY!" if c < 1.05 else "SUBEXP" if c < 1.2 else "EXP" if c < 1.5 else "HARD EXP"
        bar = "█" * min(40, int(log2c * 40))
        print(f"  {name:30} | {c:10.4f} | {log2c:8.4f} | {verdict:>12}", flush=True)

    print(flush=True)
    if results:
        best = results[0]
        worst = results[-1]
        print(f"CLOSEST TO P: {best[0]} (c = {best[1]:.4f})", flush=True)
        print(f"FARTHEST:     {worst[0]} (c = {worst[1]:.4f})", flush=True)
        print(flush=True)
        print(f"The gap: c_best = {best[1]:.4f} vs c_target = 1.000", flush=True)
        print(f"To prove P≠NP: show c_best > 1 for ALL algorithms on ANY NPC problem.", flush=True)
        print(f"To prove P=NP: find ANY algorithm with c = 1 on ANY NPC problem.", flush=True)

if __name__ == '__main__':
    main()
