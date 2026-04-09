#!/usr/bin/env python3
"""
landscape_k.py — K-content of the SAT search landscape during DPLL.

Hypothesis from sat_scaling.py findings: hard SAT instances have K-RICH landscapes
(no gradient toward the solution — the partial assignment at each DPLL branch provides
no compressible regularity pointing toward the solution), while easy instances have
K-POOR landscapes (unit propagation chains create gradient structure = compressible).

This script:
1. Generates SAT instances of varying difficulty (easy: near-satisfiable, hard: phase transition)
2. Runs DPLL with instrumentation: at each decision point, records the current partial assignment
3. Computes gzip ratio of the partial assignment as a K-proxy for local landscape K-content
4. Tracks: does K decrease (gradient found) or stay high (no gradient) for hard vs easy instances?

Landscape K-metric at depth d:
  K_landscape(d) = gzip_ratio(partial_assignment_at_depth_d)
  - Low K: the partial assignment is compressible — structure found (gradient)
  - High K: the partial assignment is incompressible — no local pattern toward solution

Prediction:
  - Easy instances (few clauses, weak constraints): K decreases quickly via unit propagation
  - Hard instances (phase-transition, no local gradient): K stays high throughout search

Usage:
    cd ~/open_problems/physics/what_is_computation
    python3 numerics/landscape_k.py

Numerical track, what_is_computation — 2026-04-09
"""

import random, time, gzip, json, os, math
from collections import defaultdict

# ── SAT Instance Generators ───────────────────────────────────────────────────

def gen_sat_guaranteed(n_vars, n_clauses, seed):
    """Guaranteed-SAT instance at given clause density."""
    rng = random.Random(seed * 997 + n_vars)
    assignment = {i: rng.choice([True, False]) for i in range(1, n_vars + 1)}
    clauses = []
    attempts = 0
    while len(clauses) < n_clauses and attempts < n_clauses * 1000:
        attempts += 1
        vars_ = rng.sample(range(1, n_vars + 1), 3)
        lits = [v if assignment[v] else -v for v in vars_]
        for j in range(len(lits)):
            if rng.random() < 0.4:
                lits[j] = -lits[j]
        if any((l > 0 and assignment[l]) or (l < 0 and not assignment[-l]) for l in lits):
            clauses.append(lits)
    return clauses, assignment

def remaining_clauses_to_bytes(clauses: list, assignment: dict) -> bytes:
    """
    Encode the REMAINING (not-yet-satisfied) clauses as bytes.
    A clause is satisfied if any literal is true under assignment.
    Remaining clauses are the unsatisfied constraints — their K-content reflects
    how much structure remains in the search problem.
    At the start: all clauses present (high S but unknown K).
    During easy search: clauses collapse quickly via unit propagation (K drops).
    During hard search: clauses remain complex (K stays high).
    Each literal encoded as signed byte (var_id mod 127) with sign = polarity.
    """
    remaining = []
    for clause in clauses:
        # Check if clause is already satisfied
        satisfied = any((l > 0 and assignment.get(l, False)) or
                       (l < 0 and not assignment.get(-l, True)) for l in clause)
        if not satisfied:
            # Encode remaining literals (those not yet resolved)
            active_lits = []
            for l in clause:
                v = abs(l)
                if v not in assignment:
                    active_lits.append(l)
            if active_lits:  # clause has unresolved literals
                remaining.extend(active_lits)
    # Encode as bytes: each literal as 2 bytes (high byte = sign+var_high, low byte = var_low)
    result = []
    for l in remaining:
        result.append(128 if l > 0 else 0)  # sign byte
        result.append(abs(l) % 256)          # variable byte
    return bytes(result)

def k_proxy(data: bytes) -> float:
    if len(data) == 0:
        return 0.0
    c = gzip.compress(data, compresslevel=9)
    return len(c) / len(data)

# ── Instrumented DPLL ─────────────────────────────────────────────────────────

class DPLLInstrumented:
    def __init__(self, n_vars, clauses, record_every=5):
        self.n_vars = n_vars
        self.clauses = clauses
        self.record_every = record_every
        self.depth_k_values = []  # (depth, k_proxy, step)
        self.step = 0
        self.decisions = 0

    def solve(self):
        return self._dpll({}, 0)

    def _unit_propagate(self, cls, assignment):
        changed = True
        while changed:
            changed = False
            for clause in cls:
                unset = [l for l in clause if abs(l) not in assignment]
                if not unset:
                    if not any((l > 0 and assignment.get(l)) or
                               (l < 0 and not assignment.get(-l)) for l in clause):
                        return None
                elif len(unset) == 1:
                    l = unset[0]
                    assignment[abs(l)] = l > 0
                    changed = True
        return assignment

    def _dpll(self, assignment, depth):
        self.step += 1
        assignment = self._unit_propagate(self.clauses, dict(assignment))
        if assignment is None:
            return None

        # Record K-content at this depth
        if self.step % self.record_every == 0:
            data = remaining_clauses_to_bytes(self.clauses, assignment)
            k = k_proxy(data) if len(data) >= 20 else 0.0
            n_assigned = sum(1 for i in range(1, self.n_vars + 1) if i in assignment)
            self.depth_k_values.append({
                "step": self.step,
                "depth": depth,
                "n_assigned": n_assigned,
                "k_proxy": round(k, 6),
            })

        # Check if satisfied
        all_satisfied = all(
            any((l > 0 and assignment.get(l, False)) or
                (l < 0 and not assignment.get(-l, True)) for l in clause)
            for clause in self.clauses
        )
        if all_satisfied:
            return assignment

        # Pick unset variable
        all_vars = set(abs(l) for clause in self.clauses for l in clause)
        unset = [v for v in sorted(all_vars) if v not in assignment]
        if not unset:
            return None

        # Most-constrained-variable heuristic
        var_counts = defaultdict(int)
        for clause in self.clauses:
            for l in clause:
                if abs(l) not in assignment:
                    var_counts[abs(l)] += 1
        v = max(unset, key=lambda x: var_counts[x])

        self.decisions += 1
        for val in [True, False]:
            new_assign = dict(assignment)
            new_assign[v] = val
            result = self._dpll(new_assign, depth + 1)
            if result is not None:
                return result
        return None

# ── Main experiment ───────────────────────────────────────────────────────────

def run_experiment(n_vars, clause_ratio, n_instances=5, seed_base=100):
    """Run DPLL with K-instrumentation on instances at given clause ratio."""
    n_clauses = int(clause_ratio * n_vars)
    all_results = []

    for inst in range(n_instances):
        clauses, _ = gen_sat_guaranteed(n_vars, n_clauses, seed_base + inst)
        solver = DPLLInstrumented(n_vars, clauses, record_every=3)
        t0 = time.perf_counter()
        sol = solver.solve()
        elapsed = time.perf_counter() - t0

        k_values = [r["k_proxy"] for r in solver.depth_k_values]
        k_initial = k_values[0] if k_values else None
        k_final = k_values[-1] if k_values else None
        k_min = min(k_values) if k_values else None
        k_trend = "decreasing" if len(k_values) >= 2 and k_values[-1] < k_values[0] else "flat/increasing"

        all_results.append({
            "instance": inst,
            "n_vars": n_vars,
            "n_clauses": n_clauses,
            "clause_ratio": clause_ratio,
            "solved": sol is not None,
            "decisions": solver.decisions,
            "steps": solver.step,
            "time_ms": round(elapsed * 1000, 4),
            "k_initial": round(k_initial, 4) if k_initial else None,
            "k_final": round(k_final, 4) if k_final else None,
            "k_min": round(k_min, 4) if k_min else None,
            "k_trend": k_trend,
            "k_trajectory": solver.depth_k_values[:20],  # First 20 records
        })

    return all_results

def run():
    print("=" * 70)
    print("SAT Search Landscape K-Content: Easy vs Hard Instances")
    print("=" * 70)

    all_results = []
    configs = [
        # (n_vars, clause_ratio, description)
        (25, 2.0, "easy-25 (sparse, under-constrained)"),
        (25, 4.3, "hard-25 (phase transition)"),
        (30, 2.0, "easy-30 (sparse)"),
        (30, 4.3, "hard-30 (phase transition)"),
    ]

    for n_vars, ratio, desc in configs:
        results = run_experiment(n_vars, ratio, n_instances=5)
        all_results.extend(results)

        k_initials = [r["k_initial"] for r in results if r["k_initial"] is not None]
        k_finals = [r["k_final"] for r in results if r["k_final"] is not None]
        decisions = [r["decisions"] for r in results]
        decreasing = sum(1 for r in results if r["k_trend"] == "decreasing")

        print(f"\n{desc} (n={n_vars}, ratio={ratio}):")
        if k_initials:
            print(f"  K_initial: {sum(k_initials)/len(k_initials):.4f} (avg)")
            print(f"  K_final:   {sum(k_finals)/len(k_finals):.4f} (avg) [n={len(k_finals)}]")
            print(f"  ΔK:        {sum(k_finals)/len(k_finals) - sum(k_initials)/len(k_initials):+.4f}")
        else:
            print(f"  K_initial: N/A (solved too quickly to record)")
        print(f"  Decisions: {sum(decisions)/len(decisions):.1f} (avg)")
        print(f"  K decreasing: {decreasing}/{len(results)} instances")

    print("\n── Summary: K-trend vs difficulty ──")
    print(f"{'Config':<35} {'K_init':<10} {'K_final':<10} {'ΔK':<10} {'Decisions':<12} {'K↓ count'}")
    print("─" * 80)
    for n_vars, ratio, desc in configs:
        batch = [r for r in all_results if r["n_vars"] == n_vars and abs(r["clause_ratio"] - ratio) < 0.1]
        ki = [r["k_initial"] for r in batch if r["k_initial"]]
        kf = [r["k_final"] for r in batch if r["k_final"]]
        d = [r["decisions"] for r in batch]
        down = sum(1 for r in batch if r["k_trend"] == "decreasing")
        if ki and kf and d:
            avg_ki = sum(ki)/len(ki)
            avg_kf = sum(kf)/len(kf)
            avg_d = sum(d)/len(d)
            print(f"{desc:<35} {avg_ki:<10.4f} {avg_kf:<10.4f} {avg_kf-avg_ki:<10.4f} {avg_d:<12.1f} {down}/{len(batch)}")

    print()
    print("Prediction:")
    print("  Easy (under-constrained): K decreases quickly — unit propagation creates gradient.")
    print("  Hard (phase transition):  K stays HIGH — no local structure pointing to solution.")
    print("  Over-constrained:         K may stay high or drop (UNSAT branches prune early).")
    print()
    print("If K_hard >> K_easy at final decision depth, this supports:")
    print("  P ≠ NP claim: hard NP instances have K-OPAQUE search landscapes.")
    print("  No polynomial algorithm can exploit compressible structure (there is none).")

    os.makedirs("results", exist_ok=True)
    with open("results/landscape_k_data.json", "w") as f:
        json.dump({"configs": [{"n": c[0], "ratio": c[1], "desc": c[2]} for c in configs],
                   "results": all_results}, f, indent=2)
    print(f"\nManifest → results/landscape_k_data.json")

if __name__ == "__main__":
    run()
