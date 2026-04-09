#!/usr/bin/env python3
"""
sat_scaling.py — 3-SAT find/verify ratio scaling study for P vs NP.

Extends pnp_compression_asymmetry.py to larger n and fits an exponential
to determine the doubling period k in ratio(n) ≈ A × 2^(n/k).

Method:
  - Guaranteed-SAT instances via construction (fix assignment first, then
    generate only clauses satisfied by it).
  - DPLL with unit propagation + VSIDS-inspired variable ordering.
  - 10 independent random seeds per n value.
  - Median ratio across instances; exponential least-squares fit.
  - Timeout: 30 seconds per instance.

Numerical track, what_is_computation Phase 2 — 2026-04-09
"""

import random
import time
import json
import os
import math
import signal
import sys
from typing import Optional

# ── DPLL solver ───────────────────────────────────────────────────────────────

class TimeoutError(Exception):
    pass

def _timeout_handler(signum, frame):
    raise TimeoutError("DPLL exceeded time limit")

Clause = list[int]  # literals: positive = var true, negative = var false

def sat_instance_guaranteed(n_vars: int, n_clauses: int, seed: int) -> tuple[list[Clause], dict]:
    """
    Generate a guaranteed-SAT 3-SAT instance at the phase transition.
    Construction:
      1. Fix a random assignment A.
      2. Generate random 3-literal clauses; keep only those satisfied by A.
    This ensures the formula is SAT by construction.

    Returns (clauses, assignment).
    """
    rng = random.Random(seed)
    # Fixed satisfying assignment
    assignment = {v: rng.choice([True, False]) for v in range(1, n_vars + 1)}

    clauses = []
    attempts = 0
    max_attempts = n_clauses * 10000
    while len(clauses) < n_clauses and attempts < max_attempts:
        attempts += 1
        vars_ = rng.sample(range(1, n_vars + 1), 3)
        # Assign random signs to each literal
        lits = [v if rng.random() < 0.5 else -v for v in vars_]
        # Check if at least one literal is true under A
        satisfied = any(
            (l > 0 and assignment[l]) or (l < 0 and not assignment[-l])
            for l in lits
        )
        if satisfied:
            clauses.append(lits)

    if len(clauses) < n_clauses:
        # Fallback: force-include clauses that are trivially true under A
        while len(clauses) < n_clauses:
            vars_ = rng.sample(range(1, n_vars + 1), 3)
            # Pick signs that guarantee satisfaction
            lits = [v if assignment[v] else -v for v in vars_]
            clauses.append(lits)

    return clauses, assignment


def sat_verify(clauses: list[Clause], assignment: dict) -> bool:
    """
    Verify a satisfying assignment. O(3 * len(clauses)).
    Returns True if all clauses are satisfied.
    """
    for clause in clauses:
        satisfied = False
        for l in clause:
            if l > 0:
                if assignment.get(l, False):
                    satisfied = True
                    break
            else:
                if not assignment.get(-l, True):
                    satisfied = True
                    break
        if not satisfied:
            return False
    return True


def dpll_solve(n_vars: int, clauses: list[Clause]) -> Optional[dict]:
    """
    DPLL with:
      - Unit propagation
      - Pure literal elimination
      - VSIDS-inspired variable ordering (most-constrained first)

    Returns satisfying assignment dict or None if UNSAT.
    This function is designed for clean, reliable performance up to n~24.
    """
    # Represent clauses as frozensets for fast operations
    # Use watched literals conceptually; implement as list with filtering

    def literal_true(l: int, asgn: dict) -> bool:
        return (l > 0 and asgn.get(l, None) is True) or \
               (l < 0 and asgn.get(-l, None) is False)

    def literal_false(l: int, asgn: dict) -> bool:
        return (l > 0 and asgn.get(l, None) is False) or \
               (l < 0 and asgn.get(-l, None) is True)

    def clause_status(clause: list, asgn: dict):
        """Returns 'sat', 'unsat', 'unit' (with the unit literal), or 'open'."""
        unset = []
        for l in clause:
            if literal_true(l, asgn):
                return ('sat', None)
            if not literal_false(l, asgn):
                unset.append(l)
        if len(unset) == 0:
            return ('unsat', None)
        if len(unset) == 1:
            return ('unit', unset[0])
        return ('open', None)

    def unit_propagate(clauses: list, asgn: dict) -> Optional[dict]:
        """Apply unit propagation until fixed point. Returns None on conflict."""
        asgn = dict(asgn)
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                status, unit_lit = clause_status(clause, asgn)
                if status == 'unsat':
                    return None
                if status == 'unit':
                    var = abs(unit_lit)
                    val = unit_lit > 0
                    if var in asgn:
                        if asgn[var] != val:
                            return None  # conflict
                    else:
                        asgn[var] = val
                        changed = True
        return asgn

    def pure_literal_elim(clauses: list, asgn: dict) -> dict:
        """Assign all pure literals (appear only positively or only negatively)."""
        asgn = dict(asgn)
        pos_vars = set()
        neg_vars = set()
        for clause in clauses:
            for l in clause:
                if literal_true(l, asgn) or literal_false(l, asgn):
                    continue
                if l > 0:
                    pos_vars.add(l)
                else:
                    neg_vars.add(-l)
        # Pure positive: appears only positively
        pure_pos = pos_vars - neg_vars
        # Pure negative: appears only negatively
        pure_neg = neg_vars - pos_vars
        for v in pure_pos:
            if v not in asgn:
                asgn[v] = True
        for v in pure_neg:
            if v not in asgn:
                asgn[v] = False
        return asgn

    def count_occurrences(clauses: list, asgn: dict) -> dict:
        """Count how many unsatisfied clauses each unset variable appears in."""
        counts = {}
        for clause in clauses:
            status, _ = clause_status(clause, asgn)
            if status in ('sat',):
                continue
            for l in clause:
                v = abs(l)
                if v not in asgn:
                    counts[v] = counts.get(v, 0) + 1
        return counts

    def pick_variable(clauses: list, asgn: dict, all_vars: set) -> Optional[int]:
        """Pick the most-constrained unset variable (VSIDS-style)."""
        unset = all_vars - set(asgn.keys())
        if not unset:
            return None
        counts = count_occurrences(clauses, asgn)
        # Break ties by variable index
        return max(unset, key=lambda v: counts.get(v, 0))

    def dpll(clauses: list, asgn: dict, all_vars: set) -> Optional[dict]:
        # Unit propagation
        asgn = unit_propagate(clauses, asgn)
        if asgn is None:
            return None

        # Pure literal elimination
        asgn = pure_literal_elim(clauses, asgn)

        # Check if all clauses are satisfied
        all_sat = all(clause_status(c, asgn)[0] == 'sat' for c in clauses)
        if all_sat:
            # Fill in any remaining unset variables
            for v in all_vars:
                if v not in asgn:
                    asgn[v] = True
            return asgn

        # Check for conflict
        if any(clause_status(c, asgn)[0] == 'unsat' for c in clauses):
            return None

        # Pick a variable to branch on
        var = pick_variable(clauses, asgn, all_vars)
        if var is None:
            return None

        # Branch
        for val in [True, False]:
            new_asgn = dict(asgn)
            new_asgn[var] = val
            result = dpll(clauses, new_asgn, all_vars)
            if result is not None:
                return result

        return None

    all_vars = set(range(1, n_vars + 1))
    return dpll(clauses, {}, all_vars)


# ── Timing harness ────────────────────────────────────────────────────────────

def timed(fn, *args):
    """Time a function call. Returns (result, elapsed_seconds)."""
    t0 = time.perf_counter()
    result = fn(*args)
    return result, time.perf_counter() - t0


def run_instance(n_vars: int, n_clauses: int, seed: int, timeout_sec: float = 30.0
                 ) -> Optional[dict]:
    """
    Run one 3-SAT instance: generate, search (DPLL), verify.
    Returns a dict with timing data, or None if timed out or failed.
    """
    # Generate guaranteed-SAT instance
    clauses, known_assignment = sat_instance_guaranteed(n_vars, n_clauses, seed)

    # Verify known_assignment is actually satisfying (sanity check)
    if not sat_verify(clauses, known_assignment):
        print(f"  [BUG] n={n_vars} seed={seed}: construction produced UNSAT instance!")
        return None

    # Time verification of known assignment (the easy direction)
    _, t_verify = timed(sat_verify, clauses, known_assignment)

    # Time DPLL search (the hard direction) with timeout
    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(int(math.ceil(timeout_sec)))
    try:
        t_search_start = time.perf_counter()
        found_assignment = dpll_solve(n_vars, clauses)
        t_search = time.perf_counter() - t_search_start
        signal.alarm(0)  # Cancel alarm
    except TimeoutError:
        signal.alarm(0)
        return None  # Timed out

    if found_assignment is None:
        # DPLL failed (should not happen for guaranteed-SAT, but log it)
        print(f"  [WARN] n={n_vars} seed={seed}: DPLL returned UNSAT for a guaranteed-SAT instance")
        return None

    # Verify the found assignment too (double-check correctness)
    found_valid = sat_verify(clauses, found_assignment)
    if not found_valid:
        print(f"  [BUG] n={n_vars} seed={seed}: DPLL returned an invalid assignment!")
        return None

    ratio = t_search / t_verify if t_verify > 0 else float("inf")

    return {
        "n_vars": n_vars,
        "n_clauses": n_clauses,
        "seed": seed,
        "t_verify_us": round(t_verify * 1e6, 4),
        "t_search_ms": round(t_search * 1e3, 6),
        "ratio": round(ratio, 4),
    }


# ── Exponential fitting ────────────────────────────────────────────────────────

def fit_exponential(ns: list, ratios: list) -> tuple[float, float, float]:
    """
    Fit ratio(n) = A * 2^(n/k) by linear regression on log2(ratio) vs n.
    log2(ratio) = log2(A) + n/k  →  linear in n.

    Returns (A, k, r_squared).
    """
    import math
    log_ratios = [math.log2(r) for r in ratios]
    n_pts = len(ns)
    # Linear regression: y = a + b*x, where y=log2(ratio), x=n
    x_mean = sum(ns) / n_pts
    y_mean = sum(log_ratios) / n_pts
    ss_xx = sum((x - x_mean) ** 2 for x in ns)
    ss_xy = sum((x - x_mean) * (y - y_mean) for x, y in zip(ns, log_ratios))
    if ss_xx == 0:
        return (1.0, float('inf'), 0.0)
    b = ss_xy / ss_xx   # slope = 1/k (in log2 units)
    a = y_mean - b * x_mean  # intercept = log2(A)
    A = 2 ** a
    k = 1.0 / b if b != 0 else float('inf')

    # R²
    y_pred = [a + b * x for x in ns]
    ss_res = sum((y - yp) ** 2 for y, yp in zip(log_ratios, y_pred))
    ss_tot = sum((y - y_mean) ** 2 for y in log_ratios)
    r2 = 1.0 - (ss_res / ss_tot) if ss_tot > 0 else 1.0

    return (A, k, r2)


# ── Main study ─────────────────────────────────────────────────────────────────

def main():
    # Configuration
    N_VARS_LIST = [10, 12, 14, 16, 18, 20, 22, 24]
    N_INSTANCES = 10
    TIMEOUT_SEC = 30.0
    ALPHA = 4.3  # phase transition clause-to-variable ratio

    # Different seeds for each instance (not just sequential to avoid artifacts)
    SEEDS = [17, 31, 53, 79, 103, 137, 163, 197, 223, 251]

    print("=" * 72)
    print("3-SAT Scaling Study — find/verify ratio vs n_vars")
    print(f"Phase transition: n_clauses = {ALPHA} * n_vars (rounded)")
    print(f"Instances per n: {N_INSTANCES}   Timeout: {TIMEOUT_SEC}s")
    print("=" * 72)

    all_raw = []
    summary_rows = []

    for n_vars in N_VARS_LIST:
        n_clauses = round(ALPHA * n_vars)
        print(f"\nn_vars={n_vars}, n_clauses={n_clauses}")
        print(f"  {'seed':<8} {'t_verify(µs)':<16} {'t_search(ms)':<16} {'ratio':<12} {'status'}")
        print(f"  {'─'*8} {'─'*14} {'─'*14} {'─'*10} {'─'*8}")

        instance_records = []
        n_timeout = 0

        for i, seed in enumerate(SEEDS):
            rec = run_instance(n_vars, n_clauses, seed, TIMEOUT_SEC)
            if rec is None:
                n_timeout += 1
                print(f"  {seed:<8} {'—':<16} {'—':<16} {'TIMEOUT/FAIL':<12}")
                all_raw.append({
                    "n_vars": n_vars, "n_clauses": n_clauses,
                    "seed": seed, "status": "timeout"
                })
                continue

            status = "ok"
            print(f"  {seed:<8} {rec['t_verify_us']:<16.2f} {rec['t_search_ms']:<16.4f} {rec['ratio']:<12.1f} {status}")
            rec["status"] = "ok"
            instance_records.append(rec)
            all_raw.append(rec)

        if not instance_records:
            print(f"  [SKIP] No successful instances for n_vars={n_vars}")
            continue

        # Compute medians
        ratios = sorted(r["ratio"] for r in instance_records)
        t_verifies = sorted(r["t_verify_us"] for r in instance_records)
        t_searches = sorted(r["t_search_ms"] for r in instance_records)
        mid = len(ratios) // 2

        def median(xs):
            xs = sorted(xs)
            n = len(xs)
            if n % 2 == 1:
                return xs[n // 2]
            return (xs[n // 2 - 1] + xs[n // 2]) / 2.0

        med_ratio = median(ratios)
        med_verify = median(t_verifies)
        med_search = median(t_searches)

        print(f"  Median: t_verify={med_verify:.2f}µs  t_search={med_search:.4f}ms  ratio={med_ratio:.1f}×")
        print(f"  ({n_timeout} timeout(s), {len(instance_records)} successful)")

        summary_rows.append({
            "n_vars": n_vars,
            "n_clauses": n_clauses,
            "n_ok": len(instance_records),
            "n_timeout": n_timeout,
            "median_ratio": round(med_ratio, 4),
            "median_t_verify_us": round(med_verify, 4),
            "median_t_search_ms": round(med_search, 6),
        })

    # Fit exponential to median ratios
    print("\n" + "=" * 72)
    print("Exponential fit: ratio(n) ≈ A × 2^(n/k)")
    print("=" * 72)

    fit_ns = [r["n_vars"] for r in summary_rows if r["n_ok"] >= 3]
    fit_ratios = [r["median_ratio"] for r in summary_rows if r["n_ok"] >= 3]

    if len(fit_ns) >= 3:
        A, k, r2 = fit_exponential(fit_ns, fit_ratios)
        print(f"  A = {A:.4f}")
        print(f"  k = {k:.4f}  (ratio doubles every {k:.2f} variables)")
        print(f"  R² = {r2:.4f}")
    else:
        A, k, r2 = None, None, None
        print("  Insufficient data for fit.")

    # Print results table
    print("\n── Results Table ──")
    print(f"{'n_vars':<8} {'n_cls':<7} {'n_ok':<6} {'med_ratio':<12} {'fit_pred':<12} {'t_verify(µs)':<14} {'t_search(ms)'}")
    print("─" * 80)
    for row in summary_rows:
        n = row["n_vars"]
        if A is not None and k is not None:
            pred = A * (2 ** (n / k))
            pred_str = f"{pred:.1f}"
        else:
            pred_str = "—"
        print(f"{n:<8} {row['n_clauses']:<7} {row['n_ok']:<6} {row['median_ratio']:<12.1f} {pred_str:<12} {row['median_t_verify_us']:<14.2f} {row['median_t_search_ms']:.4f}")

    # Save results
    os.makedirs("~/open_problems/physics/what_is_computation/results", exist_ok=True)
    out_path = "~/open_problems/physics/what_is_computation/results/sat_scaling_data.json"
    output = {
        "description": "3-SAT find/verify ratio scaling study",
        "config": {
            "n_vars_list": N_VARS_LIST,
            "n_instances": N_INSTANCES,
            "timeout_sec": TIMEOUT_SEC,
            "phase_transition_alpha": ALPHA,
            "seeds": SEEDS,
        },
        "raw_instances": all_raw,
        "summary": summary_rows,
        "exponential_fit": {
            "model": "ratio(n) = A * 2^(n/k)",
            "A": round(A, 6) if A is not None else None,
            "k": round(k, 6) if k is not None else None,
            "r_squared": round(r2, 6) if r2 is not None else None,
            "n_points_used": len(fit_ns),
        },
    }
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")

    # Summary for findings
    print("\n── Key findings ──")
    if k is not None:
        print(f"  Doubling period: k = {k:.2f} variables")
        print(f"  R² of exponential fit: {r2:.4f}")
        if r2 > 0.85:
            print("  Growth is well-described as exponential (R² > 0.85)")
            print("  This is consistent with P ≠ NP.")
        elif r2 > 0.6:
            print("  Growth is moderately exponential (R² 0.6–0.85)")
            print("  Consistent with super-polynomial growth; exponential is plausible.")
        else:
            print("  Growth is not cleanly exponential (R² < 0.6)")
            print("  May be polynomial or sub-exponential over this range.")
    if summary_rows:
        last = summary_rows[-1]
        print(f"  At n={last['n_vars']}: median find/verify ratio = {last['median_ratio']:.1f}×")
        print(f"  Median search time: {last['median_t_search_ms']:.4f} ms")
        print(f"  Median verify time: {last['median_t_verify_us']:.2f} µs")

    return output


if __name__ == "__main__":
    main()
