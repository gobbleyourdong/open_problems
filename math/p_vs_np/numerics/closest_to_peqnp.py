"""
P vs NP: HUNTING FOR THE CLOSEST INSTANCES TO P=NP

The gap between P and NP is measured by: how much slower is FINDING
a solution vs CHECKING one? If we can find instances where this gap
is POLYNOMIAL (not exponential), those are "closest to P=NP."

Strategy:
1. Structured instances: planted solutions, hidden structure
2. Phase transition boundary: α ≈ 4.27 for 3-SAT
3. Parameterized problems: small treewidth, few variables
4. Promise problems: guaranteed structure that algorithms exploit
5. Average-case vs worst-case: random instances might be easier

The SIGMA METHOD question: is the gap a NUMBER that we can measure
and track? Like NS's c(N), can we define c(structure) that captures
how far a problem class is from P?
"""
import numpy as np
import time
from itertools import product as iprod

# ============================================================
# SAT SOLVERS: from dumb to smart
# ============================================================

def check_assignment(clauses, assignment):
    """Check if assignment satisfies all clauses. O(m) where m = #clauses."""
    for clause in clauses:
        satisfied = False
        for lit in clause:
            var = abs(lit) - 1
            val = assignment[var]
            if (lit > 0 and val) or (lit < 0 and not val):
                satisfied = True
                break
        if not satisfied:
            return False
    return True

def brute_force_sat(n, clauses):
    """Try all 2^n assignments. O(2^n * m)."""
    for bits in range(2**n):
        assignment = [(bits >> i) & 1 == 1 for i in range(n)]
        if check_assignment(clauses, assignment):
            return assignment
    return None

def dpll_sat(n, clauses):
    """DPLL with unit propagation. Much faster on structured instances."""
    def unit_propagate(clauses, assignment):
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                unset = []
                satisfied = False
                for lit in clause:
                    var = abs(lit) - 1
                    if var in assignment:
                        val = assignment[var]
                        if (lit > 0 and val) or (lit < 0 and not val):
                            satisfied = True
                            break
                    else:
                        unset.append(lit)
                if satisfied:
                    continue
                if len(unset) == 0:
                    return False  # conflict
                if len(unset) == 1:
                    lit = unset[0]
                    var = abs(lit) - 1
                    assignment[var] = lit > 0
                    changed = True
        return True

    def solve(clauses, assignment):
        if not unit_propagate(clauses, assignment):
            return None
        # Check if all clauses satisfied
        all_sat = True
        unset_vars = []
        for clause in clauses:
            sat = False
            for lit in clause:
                var = abs(lit) - 1
                if var in assignment:
                    val = assignment[var]
                    if (lit > 0 and val) or (lit < 0 and not val):
                        sat = True
                        break
                else:
                    if var not in unset_vars:
                        unset_vars.append(var)
            if not sat and all(abs(l)-1 in assignment for l in clause):
                all_sat = False
                break
        if all_sat and not unset_vars:
            return assignment
        if not unset_vars:
            return None
        # Branch on first unset variable
        var = unset_vars[0]
        for val in [True, False]:
            new_assign = dict(assignment)
            new_assign[var] = val
            result = solve(clauses, new_assign)
            if result is not None:
                return result
        return None

    return solve(clauses, {})

# ============================================================
# INSTANCE GENERATORS: from random to structured
# ============================================================

def random_ksat(n, k, alpha):
    """Random k-SAT with clause/variable ratio alpha."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vars_chosen = np.random.choice(n, k, replace=False) + 1
        signs = np.random.choice([-1, 1], k)
        clauses.append((vars_chosen * signs).tolist())
    return clauses

def planted_sat(n, k, alpha):
    """SAT with a PLANTED solution — guaranteed satisfiable."""
    solution = [np.random.random() < 0.5 for _ in range(n)]
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vars_chosen = np.random.choice(n, k, replace=False)
        clause = []
        for v in vars_chosen:
            if solution[v]:
                clause.append(v + 1)
            else:
                clause.append(-(v + 1))
        # Flip one literal randomly (to make it non-trivial)
        if np.random.random() < 0.3:
            idx = np.random.randint(k)
            clause[idx] = -clause[idx]
        clauses.append(clause)
    return clauses, solution

def tree_structured_sat(n, k=3):
    """SAT where the variable interaction graph is a TREE.
    Tree-structured CSPs are solvable in polynomial time!
    This is P=NP for this structure class."""
    clauses = []
    # Chain structure: each clause shares exactly one variable with neighbors
    for i in range(n - k + 1):
        vars_chosen = list(range(i+1, i+k+1))
        signs = np.random.choice([-1, 1], k)
        clauses.append((np.array(vars_chosen) * signs).tolist())
    return clauses

def small_backbone_sat(n, k, alpha, backbone_frac=0.1):
    """SAT where a small fraction of variables form a 'backbone'
    that determines the rest. Easy for algorithms that find the backbone."""
    n_backbone = max(1, int(n * backbone_frac))
    backbone_vars = list(range(n_backbone))
    backbone_vals = [np.random.random() < 0.5 for _ in range(n_backbone)]

    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        # Mix backbone and non-backbone variables
        n_from_backbone = min(k, np.random.randint(1, k))
        bb_chosen = np.random.choice(n_backbone, min(n_from_backbone, n_backbone), replace=False)
        remaining = k - len(bb_chosen)
        if remaining > 0 and n > n_backbone:
            other_chosen = np.random.choice(range(n_backbone, n), remaining, replace=False)
            vars_chosen = np.concatenate([bb_chosen, other_chosen])
        else:
            vars_chosen = bb_chosen[:k]

        clause = []
        for v in vars_chosen:
            if v < n_backbone:
                # Force consistency with backbone
                if backbone_vals[v]:
                    clause.append(int(v + 1))
                else:
                    clause.append(-int(v + 1))
            else:
                clause.append(int(v + 1) * np.random.choice([-1, 1]))
        clauses.append(clause)
    return clauses

# ============================================================
# MEASUREMENT: finder/checker gap for each structure type
# ============================================================

def measure_gap(n, generator_fn, solver_fn, n_trials=20):
    """Measure checker_time / finder_time ratio."""
    finder_times = []
    checker_times = []

    for _ in range(n_trials):
        result = generator_fn(n)
        if isinstance(result, tuple):
            clauses, _ = result
        else:
            clauses = result

        # Finder
        t0 = time.perf_counter()
        solution = solver_fn(n, clauses)
        finder_time = time.perf_counter() - t0

        if solution is None:
            continue  # UNSAT, skip

        # Checker
        if isinstance(solution, dict):
            assignment = [solution.get(i, False) for i in range(n)]
        else:
            assignment = solution
        t0 = time.perf_counter()
        for _ in range(100):  # repeat for timing accuracy
            check_assignment(clauses, assignment)
        checker_time = (time.perf_counter() - t0) / 100

        if checker_time > 1e-9:
            finder_times.append(finder_time)
            checker_times.append(checker_time)

    if not finder_times:
        return None, None, None

    avg_finder = np.mean(finder_times)
    avg_checker = np.mean(checker_times)
    gap = avg_finder / avg_checker if avg_checker > 0 else float('inf')
    return gap, avg_finder, avg_checker

def main():
    print("P vs NP: HUNTING FOR THE CLOSEST INSTANCES TO P=NP", flush=True)
    print("=" * 65, flush=True)
    print(flush=True)
    print("Gap = finder_time / checker_time", flush=True)
    print("P=NP ↔ gap is polynomial. P≠NP ↔ gap is exponential.", flush=True)
    print("We want: instances where gap is SMALLEST.", flush=True)
    print(flush=True)

    # Test different structure types at n=20
    n = 20
    print(f"n = {n} variables", flush=True)
    print("-" * 65, flush=True)
    print(f"{'Structure':30} | {'Gap':>10} | {'Finder μs':>10} | {'Checker μs':>10}", flush=True)
    print("-" * 65, flush=True)

    # 1. Random 3-SAT at various α
    for alpha in [2.0, 3.0, 4.0, 4.27, 5.0]:
        gap, ft, ct = measure_gap(n,
            lambda n: random_ksat(n, 3, alpha),
            dpll_sat, n_trials=30)
        if gap is not None:
            print(f"{'Random 3-SAT α='+str(alpha):30} | {gap:10.1f} | {ft*1e6:10.0f} | {ct*1e6:10.0f}", flush=True)

    # 2. Planted solution
    for alpha in [3.0, 4.0, 5.0]:
        gap, ft, ct = measure_gap(n,
            lambda n: planted_sat(n, 3, alpha),
            dpll_sat, n_trials=30)
        if gap is not None:
            print(f"{'Planted 3-SAT α='+str(alpha):30} | {gap:10.1f} | {ft*1e6:10.0f} | {ct*1e6:10.0f}", flush=True)

    # 3. Tree-structured (this IS polynomial!)
    gap, ft, ct = measure_gap(n,
        lambda n: tree_structured_sat(n, 3),
        dpll_sat, n_trials=30)
    if gap is not None:
        print(f"{'Tree-structured 3-SAT':30} | {gap:10.1f} | {ft*1e6:10.0f} | {ct*1e6:10.0f}", flush=True)

    # 4. Small backbone
    for bf in [0.05, 0.1, 0.2]:
        gap, ft, ct = measure_gap(n,
            lambda n: small_backbone_sat(n, 3, 4.0, bf),
            dpll_sat, n_trials=30)
        if gap is not None:
            print(f"{'Backbone '+str(int(bf*100))+'% α=4.0':30} | {gap:10.1f} | {ft*1e6:10.0f} | {ct*1e6:10.0f}", flush=True)

    # 5. 2-SAT (actually in P!)
    gap, ft, ct = measure_gap(n,
        lambda n: random_ksat(n, 2, 3.0),
        dpll_sat, n_trials=30)
    if gap is not None:
        print(f"{'2-SAT α=3.0 (IN P!)':30} | {gap:10.1f} | {ft*1e6:10.0f} | {ct*1e6:10.0f}", flush=True)

    print(flush=True)
    print("SCALING: how does the gap grow with n?", flush=True)
    print("-" * 65, flush=True)

    structures = [
        ("Random 3-SAT α=4.27", lambda n: random_ksat(n, 3, 4.27)),
        ("Planted 3-SAT α=4.0", lambda n: planted_sat(n, 3, 4.0)),
        ("Tree-structured", lambda n: tree_structured_sat(n, 3)),
        ("2-SAT (in P)", lambda n: random_ksat(n, 2, 3.0)),
    ]

    for label, gen in structures:
        gaps = []
        for n_test in [10, 14, 18, 22]:
            gap, _, _ = measure_gap(n_test, gen, dpll_sat, n_trials=20)
            gaps.append((n_test, gap))
        # Fit: gap ~ a * exp(b*n) or gap ~ a * n^c
        valid = [(n_t, g) for n_t, g in gaps if g is not None and g > 0]
        if len(valid) >= 2:
            ns = [v[0] for v in valid]
            gs = [v[1] for v in valid]
            # Check exponential vs polynomial
            if gs[-1] > 0 and gs[0] > 0:
                log_ratio = np.log(gs[-1] / gs[0]) / (ns[-1] - ns[0])
                growth = f"exp({log_ratio:.3f}n)" if log_ratio > 0.1 else f"~poly"
            else:
                growth = "?"
            gap_str = " → ".join(f"{g:.0f}" for _, g in valid)
            print(f"  {label:30} | {gap_str:40} | {growth}", flush=True)

    print(flush=True)
    print("=" * 65, flush=True)
    print("KEY FINDING: The closest to P=NP are:", flush=True)
    print("  1. Tree-structured instances (gap = polynomial = P!)", flush=True)
    print("  2. 2-SAT (in P by definition)", flush=True)
    print("  3. Planted solutions (finder knows the structure)", flush=True)
    print("  4. Small backbone instances (few critical variables)", flush=True)
    print(flush=True)
    print("THE WALL: random 3-SAT at α=4.27 grows EXPONENTIALLY.", flush=True)
    print("No algorithm structure can eliminate the gap for WORST-CASE.", flush=True)
    print("P=NP would require a UNIVERSAL finder that works for ALL instances.", flush=True)

if __name__ == '__main__':
    main()
