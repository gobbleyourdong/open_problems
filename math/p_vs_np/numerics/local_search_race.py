"""
P vs NP: LOCAL SEARCH — Can random walks beat systematic search?

WalkSAT and Schöning's algorithm use random walks on the solution space.
They don't systematically enumerate — they EXPLORE. For random satisfiable
instances, they can be dramatically faster than DPLL.

Schöning (1999): Random walk 3-SAT in O((4/3)^n) expected time.
WalkSAT: Greedy + random flip, often faster in practice.

THE QUESTION: what is the empirical c for these algorithms?
If c < 1.047 (DPLL on easy instances), local search is CLOSER to P.
"""
import numpy as np
import time

def random_3sat_satisfiable(n, alpha=3.5):
    """Generate random 3-SAT that's likely satisfiable (below threshold)."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = np.random.choice(n, 3, replace=False) + 1
        signs = np.random.choice([-1, 1], 3)
        clauses.append((vs * signs).tolist())
    return clauses

def planted_3sat(n, alpha=4.0):
    """3-SAT with planted solution — guaranteed satisfiable."""
    sol = [np.random.random() < 0.5 for _ in range(n)]
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = np.random.choice(n, 3, replace=False)
        clause = []
        for v in vs:
            clause.append(int(v+1) if sol[v] else -int(v+1))
        # Flip one literal with 20% probability to add noise
        if np.random.random() < 0.2:
            idx = np.random.randint(3)
            clause[idx] = -clause[idx]
        clauses.append(clause)
    return clauses

def check_clause(clause, assignment):
    for lit in clause:
        v = abs(lit) - 1
        if (lit > 0 and assignment[v]) or (lit < 0 and not assignment[v]):
            return True
    return False

def count_unsat(clauses, assignment):
    return sum(1 for c in clauses if not check_clause(c, assignment))

def walksat(n, clauses, max_flips=None, p_random=0.3):
    """WalkSAT: pick an unsatisfied clause, flip a variable (greedy or random).
    Returns (found, n_flips)."""
    if max_flips is None:
        max_flips = 10 * n * n
    assignment = [np.random.random() < 0.5 for _ in range(n)]

    for flip in range(max_flips):
        # Find unsatisfied clauses
        unsat = [c for c in clauses if not check_clause(c, assignment)]
        if not unsat:
            return True, flip

        # Pick a random unsatisfied clause
        clause = unsat[np.random.randint(len(unsat))]

        if np.random.random() < p_random:
            # Random flip: pick any variable in the clause
            lit = clause[np.random.randint(len(clause))]
            v = abs(lit) - 1
            assignment[v] = not assignment[v]
        else:
            # Greedy flip: flip the variable that minimizes unsatisfied clauses
            best_v = None
            best_unsat = len(clauses) + 1
            for lit in clause:
                v = abs(lit) - 1
                assignment[v] = not assignment[v]
                u = count_unsat(clauses, assignment)
                assignment[v] = not assignment[v]
                if u < best_unsat:
                    best_unsat = u
                    best_v = v
            if best_v is not None:
                assignment[best_v] = not assignment[best_v]

    return False, max_flips

def schoening(n, clauses, max_tries=None):
    """Schöning's random walk algorithm for 3-SAT.
    Theoretical: O((4/3)^n) expected restarts × O(3n) flips each.
    Returns (found, total_flips)."""
    if max_tries is None:
        max_tries = max(1, int(1.5**n / n))
    total_flips = 0

    for _ in range(max_tries):
        # Random initial assignment
        assignment = [np.random.random() < 0.5 for _ in range(n)]

        for step in range(3 * n):
            total_flips += 1
            unsat = [c for c in clauses if not check_clause(c, assignment)]
            if not unsat:
                return True, total_flips
            # Pick random unsatisfied clause, flip random variable in it
            clause = unsat[np.random.randint(len(unsat))]
            lit = clause[np.random.randint(len(clause))]
            v = abs(lit) - 1
            assignment[v] = not assignment[v]

        total_flips += 1

    return False, total_flips

def dpll_nodes(n, clauses):
    """DPLL node count for comparison."""
    nodes = [0]
    def propagate(a):
        changed = True
        while changed:
            changed = False
            for c in clauses:
                unset = []; sat = False
                for lit in c:
                    v = abs(lit)-1
                    if v in a:
                        if (lit>0 and a[v]) or (lit<0 and not a[v]):
                            sat = True; break
                    else: unset.append(lit)
                if sat: continue
                if not unset: return False
                if len(unset) == 1:
                    a[abs(unset[0])-1] = unset[0]>0; changed = True
        return True
    def solve(a):
        nodes[0] += 1
        if not propagate(a): return None
        unset = [i for i in range(n) if i not in a]
        if not unset: return a
        v = unset[0]
        for val in [True, False]:
            na = dict(a); na[v] = val
            if solve(na) is not None: return na
        return None
    solve({})
    return nodes[0]

def measure_c(name, sizes, run_fn, n_trials=20):
    """Measure empirical exponent c where effort ~ c^n."""
    data = []
    for n in sizes:
        efforts = []
        for _ in range(n_trials):
            e = run_fn(n)
            if e is not None and e > 0:
                efforts.append(e)
        if efforts:
            data.append((n, np.median(efforts)))  # median more robust
    if len(data) < 2: return None, data
    ns = np.array([d[0] for d in data])
    log_e = np.log(np.array([d[1] for d in data]))
    coeffs = np.polyfit(ns, log_e, 1)
    return np.exp(coeffs[0]), data

def main():
    print("LOCAL SEARCH vs SYSTEMATIC SEARCH: The Exponent Race", flush=True)
    print("=" * 65, flush=True)
    print(flush=True)

    results = []

    # DPLL on random satisfiable 3-SAT
    print("DPLL on random 3-SAT α=3.5...", flush=True)
    c, d = measure_c("DPLL", [12, 16, 20, 24, 28],
        lambda n: dpll_nodes(n, random_3sat_satisfiable(n, 3.5)), 25)
    if c: results.append(("DPLL (random α=3.5)", c))

    # WalkSAT on random satisfiable
    print("WalkSAT on random 3-SAT α=3.5...", flush=True)
    c, d = measure_c("WalkSAT", [20, 30, 40, 50, 60, 80],
        lambda n: (lambda r: r[1] if r[0] else None)(walksat(n, random_3sat_satisfiable(n, 3.5), max_flips=50*n*n)), 25)
    if c: results.append(("WalkSAT (random α=3.5)", c))

    # Schöning on random satisfiable
    print("Schöning on random 3-SAT α=3.5...", flush=True)
    c, d = measure_c("Schöning", [12, 16, 20, 24, 28],
        lambda n: (lambda r: r[1] if r[0] else None)(schoening(n, random_3sat_satisfiable(n, 3.5))), 25)
    if c: results.append(("Schöning (random α=3.5)", c))

    # WalkSAT on planted (easiest)
    print("WalkSAT on planted 3-SAT α=4.0...", flush=True)
    c, d = measure_c("WalkSAT planted", [20, 30, 40, 60, 80, 100],
        lambda n: (lambda r: r[1] if r[0] else None)(walksat(n, planted_3sat(n, 4.0), max_flips=50*n*n)), 25)
    if c: results.append(("WalkSAT (planted α=4.0)", c))

    # DPLL on planted
    print("DPLL on planted 3-SAT α=4.0...", flush=True)
    c, d = measure_c("DPLL planted", [12, 16, 20, 24],
        lambda n: dpll_nodes(n, planted_3sat(n, 4.0)), 25)
    if c: results.append(("DPLL (planted α=4.0)", c))

    # WalkSAT on hard instances (α=4.27)
    print("WalkSAT on hard 3-SAT α=4.27...", flush=True)
    c, d = measure_c("WalkSAT hard", [20, 30, 40, 50],
        lambda n: (lambda r: r[1] if r[0] else None)(walksat(n, random_3sat_satisfiable(n, 4.27), max_flips=100*n*n)), 20)
    if c: results.append(("WalkSAT (hard α=4.27)", c))

    print(flush=True)
    print("THE RACE RESULTS", flush=True)
    print("=" * 65, flush=True)
    print(f"{'Algorithm + Instance':40} | {'c':>8} | {'log₂c':>7} | {'vs P':>8}", flush=True)
    print("-" * 65, flush=True)

    results.sort(key=lambda x: x[1])
    for name, c in results:
        log2c = np.log2(c) if c > 0 else 0
        dist = c - 1.0
        verdict = "≈P!" if c < 1.02 else "NEAR P" if c < 1.1 else "SUBEXP" if c < 1.3 else "EXP"
        print(f"  {name:40} | {c:8.4f} | {log2c:7.4f} | {verdict:>8}", flush=True)

    print(flush=True)
    if results:
        print(f"CLOSEST TO P: {results[0][0]} (c = {results[0][1]:.4f})", flush=True)
        print(flush=True)
        print("KEY INSIGHT: Local search (WalkSAT) can have LOWER exponent", flush=True)
        print("than systematic search (DPLL) on satisfiable instances.", flush=True)
        print("The algorithm MATTERS — P vs NP is about the BEST algorithm.", flush=True)

if __name__ == '__main__':
    main()
