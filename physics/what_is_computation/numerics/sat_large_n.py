#!/usr/bin/env python3
"""
sat_large_n.py — DPLL+MCV scaling study at large n (20–50 vars).

Phase 3 target: Confirm exponential growth at n=50 where DPLL requires genuine
exponential search. Extends sat_scaling.py and cdcl_comparison.py to larger n
with a 60-second timeout per instance.

Measurements per n:
  - 5 instances at phase transition (alpha = 4.3)
  - Median find/verify ratio, median search time, timeout count
  - K-trajectory: gzip ratio of remaining clauses during DPLL search

Exponential fit: ratio(n) ≈ A × 2^(n/k) on non-timeout data.

Key predictions:
  - At n=50: search time ~10-100× longer than at n=30
  - Doubling period remains ~14 vars (possibly decreasing toward k≈6 without
    conflict learning as DPLL struggles)
  - K-landscape remains FLAT (no gradient) for hard instances

Numerical track, what_is_computation Phase 3 — 2026-04-09
"""

import random
import time
import json
import os
import gzip
import math
import signal
import sys
from typing import Optional

ALPHA = 4.3   # phase-transition clause-to-variable ratio
N_VARS_LIST = [20, 25, 30, 35, 40, 45, 50]
N_INSTANCES = 5
TIMEOUT_SEC = 60.0
# Use diverse seeds
SEEDS = [17, 53, 103, 197, 251]

RESULTS_DIR = "~/open_problems/physics/what_is_computation/results"
NUMERICS_DIR = "~/open_problems/physics/what_is_computation/numerics"

# ── SAT instance generator ────────────────────────────────────────────────────

def sat_instance_guaranteed(n_vars: int, n_clauses: int, seed: int):
    """
    Generate a guaranteed-SAT 3-SAT instance at the phase transition.
    Fix a satisfying assignment first, then generate only clauses satisfied by it.
    Returns (clauses, assignment).
    """
    rng = random.Random(seed)
    assignment = {v: rng.choice([True, False]) for v in range(1, n_vars + 1)}
    clauses = []
    attempts = 0
    max_attempts = n_clauses * 20000
    while len(clauses) < n_clauses and attempts < max_attempts:
        attempts += 1
        vars_ = rng.sample(range(1, n_vars + 1), 3)
        lits = [v if rng.random() < 0.5 else -v for v in vars_]
        if any((l > 0 and assignment[l]) or (l < 0 and not assignment[-l]) for l in lits):
            clauses.append(lits)
    # Fallback: force trivially-satisfied clauses
    while len(clauses) < n_clauses:
        rng2 = random.Random(seed ^ 0xCAFE ^ len(clauses))
        vars_ = rng2.sample(range(1, n_vars + 1), 3)
        lits = [v if assignment[v] else -v for v in vars_]
        clauses.append(lits)
    return clauses, assignment


def sat_verify(clauses, assignment) -> bool:
    for clause in clauses:
        if not any((l > 0 and assignment.get(l, False)) or
                   (l < 0 and not assignment.get(-l, True)) for l in clause):
            return False
    return True


# ── K-proxy (gzip ratio) ──────────────────────────────────────────────────────

def remaining_clause_bytes(clauses, assignment) -> bytes:
    """Encode unsatisfied, partially-unresolved clauses as bytes for K-proxy."""
    result = []
    for clause in clauses:
        sat = any((l > 0 and assignment.get(l, False)) or
                  (l < 0 and not assignment.get(-l, True)) for l in clause)
        if not sat:
            active = [l for l in clause if abs(l) not in assignment]
            for l in active:
                result.append(128 if l > 0 else 0)
                result.append(abs(l) % 256)
    return bytes(result)


def k_proxy(data: bytes) -> float:
    if len(data) < 16:
        return 0.0
    c = gzip.compress(data, compresslevel=9)
    return len(c) / len(data)


# ── Shared helpers ────────────────────────────────────────────────────────────

def lit_true(l: int, asgn: dict) -> bool:
    return (l > 0 and asgn.get(l) is True) or (l < 0 and asgn.get(-l) is False)

def lit_false(l: int, asgn: dict) -> bool:
    return (l > 0 and asgn.get(l) is False) or (l < 0 and asgn.get(-l) is True)


def unit_propagate(clauses: list, asgn: dict) -> Optional[dict]:
    """Apply unit propagation until fixed point. Returns None on conflict."""
    asgn = dict(asgn)
    changed = True
    while changed:
        changed = False
        for clause in clauses:
            if any(lit_true(l, asgn) for l in clause):
                continue  # clause satisfied
            unset = [l for l in clause if not lit_false(l, asgn) and not lit_true(l, asgn)]
            if len(unset) == 0:
                return None  # conflict
            if len(unset) == 1:
                u = unset[0]
                v = abs(u)
                val = u > 0
                if v in asgn:
                    if asgn[v] != val:
                        return None
                else:
                    asgn[v] = val
                    changed = True
    return asgn


def all_satisfied(clauses: list, asgn: dict) -> bool:
    return all(any(lit_true(l, asgn) for l in c) for c in clauses)


def count_occurrences(clauses: list, asgn: dict) -> dict:
    """Count how many unsatisfied clauses each unset variable appears in (MCV)."""
    counts = {}
    for clause in clauses:
        if any(lit_true(l, asgn) for l in clause):
            continue  # satisfied
        for l in clause:
            v = abs(l)
            if v not in asgn:
                counts[v] = counts.get(v, 0) + 1
    return counts


# ── DPLL + MCV solver with K-trajectory tracking ─────────────────────────────

class TimeoutSignal(Exception):
    pass

def _alarm_handler(signum, frame):
    raise TimeoutSignal()


class DPLLwithMCV:
    """
    DPLL with Most-Constrained Variable (MCV) heuristic and optional
    K-trajectory tracking. Designed for n up to ~50 with 60s timeout.
    """
    def __init__(self, n_vars: int, clauses: list, seed: int,
                 track_k: bool = False, deadline: float = None,
                 k_sample_every: int = 50):
        self.n_vars = n_vars
        self.all_vars = set(range(1, n_vars + 1))
        self.clauses = [list(c) for c in clauses]
        self.rng = random.Random(seed ^ 0xF00D)
        self.decisions = 0
        self.conflicts = 0
        self.track_k = track_k
        self.k_trajectory = []
        self._step = 0
        self.deadline = deadline
        self.k_sample_every = k_sample_every

    def solve(self) -> Optional[dict]:
        return self._dpll({})

    def _pick_var(self, asgn: dict) -> Optional[int]:
        """MCV: pick the variable appearing in the most unsatisfied clauses."""
        unset = self.all_vars - set(asgn.keys())
        if not unset:
            return None
        counts = count_occurrences(self.clauses, asgn)
        # Among unset vars, pick max occurrence count; break ties with var index
        return max(unset, key=lambda v: (counts.get(v, 0), v))

    def _dpll(self, asgn: dict) -> Optional[dict]:
        if self.deadline and time.perf_counter() > self.deadline:
            raise TimeoutSignal()

        self._step += 1
        asgn = unit_propagate(self.clauses, asgn)
        if asgn is None:
            self.conflicts += 1
            return None

        # K-content tracking
        if self.track_k and self._step % self.k_sample_every == 0:
            data = remaining_clause_bytes(self.clauses, asgn)
            k = k_proxy(data)
            self.k_trajectory.append({
                "step": self._step,
                "n_assigned": len(asgn),
                "k_proxy": round(k, 6),
            })

        if all_satisfied(self.clauses, asgn):
            for v in self.all_vars:
                if v not in asgn:
                    asgn[v] = True
            return asgn

        var = self._pick_var(asgn)
        if var is None:
            return None

        self.decisions += 1
        for val in [True, False]:
            new_asgn = dict(asgn)
            new_asgn[var] = val
            result = self._dpll(new_asgn)
            if result is not None:
                return result

        return None


# ── Exponential fitting ────────────────────────────────────────────────────────

def fit_exponential(ns: list, ratios: list):
    """
    Fit ratio(n) = A * 2^(n/k) via linear regression on log2(ratio) vs n.
    Returns (A, k, r_squared).
    """
    log_ratios = [math.log2(r) for r in ratios]
    n_pts = len(ns)
    x_mean = sum(ns) / n_pts
    y_mean = sum(log_ratios) / n_pts
    ss_xx = sum((x - x_mean) ** 2 for x in ns)
    ss_xy = sum((x - x_mean) * (y - y_mean) for x, y in zip(ns, log_ratios))
    if ss_xx == 0:
        return (1.0, float('inf'), 0.0)
    b = ss_xy / ss_xx
    a = y_mean - b * x_mean
    A = 2 ** a
    k = 1.0 / b if b != 0 else float('inf')
    y_pred = [a + b * x for x in ns]
    ss_res = sum((y - yp) ** 2 for y, yp in zip(log_ratios, y_pred))
    ss_tot = sum((y - y_mean) ** 2 for y in log_ratios)
    r2 = 1.0 - (ss_res / ss_tot) if ss_tot > 0 else 1.0
    return (A, k, r2)


def median(xs):
    xs = sorted(xs)
    n = len(xs)
    if n == 0:
        return None
    if n % 2 == 1:
        return xs[n // 2]
    return (xs[n // 2 - 1] + xs[n // 2]) / 2.0


# ── Main study ────────────────────────────────────────────────────────────────

def run_n(n_vars: int, seeds: list, timeout_sec: float,
          track_k: bool = True) -> dict:
    """Run all instances for a given n_vars. Returns summary dict."""
    n_clauses = round(ALPHA * n_vars)
    instance_records = []
    timeout_count = 0
    k_trajectories = []

    # MCV heuristic solves most instances in <200 steps, so sample every step
    # to capture the full K-trajectory even for short searches.
    k_sample_every = 1

    print(f"\nn_vars={n_vars}, n_clauses={n_clauses}, timeout={timeout_sec}s")
    print(f"  {'seed':<8} {'t_verify(us)':<15} {'t_search(ms)':<15} {'ratio':<12} status")
    print(f"  {'─'*8} {'─'*13} {'─'*13} {'─'*10} {'─'*8}")

    for seed in seeds:
        clauses, known_asgn = sat_instance_guaranteed(n_vars, n_clauses, seed)

        # Sanity check
        if not sat_verify(clauses, known_asgn):
            print(f"  {seed:<8} [BUG: constructed UNSAT instance]")
            continue

        # Time verification (cheap direction)
        t0 = time.perf_counter()
        sat_verify(clauses, known_asgn)
        t_verify = time.perf_counter() - t0
        t_verify_us = t_verify * 1e6

        # DPLL search with timeout
        deadline = time.perf_counter() + timeout_sec
        solver = DPLLwithMCV(
            n_vars, clauses, seed,
            track_k=track_k,
            deadline=deadline,
            k_sample_every=k_sample_every
        )

        signal.signal(signal.SIGALRM, _alarm_handler)
        signal.alarm(int(math.ceil(timeout_sec)) + 1)
        t_search_start = time.perf_counter()
        timed_out = False
        found_asgn = None
        try:
            found_asgn = solver.solve()
        except TimeoutSignal:
            timed_out = True
        finally:
            signal.alarm(0)
        t_search = time.perf_counter() - t_search_start

        if timed_out:
            timeout_count += 1
            print(f"  {seed:<8} {t_verify_us:<15.2f} {'—':<15} {'TIMEOUT':<12}")
            # Still record K-trajectory if we got any
            if solver.k_trajectory:
                k_trajectories.append({
                    "seed": seed,
                    "status": "timeout",
                    "trajectory": solver.k_trajectory
                })
            continue

        if found_asgn is None:
            print(f"  {seed:<8} {t_verify_us:<15.2f} {'—':<15} {'UNSAT?':<12}")
            continue

        # Verify found assignment
        if not sat_verify(clauses, found_asgn):
            print(f"  {seed:<8} {t_verify_us:<15.2f} {'—':<15} {'BAD_SOL':<12}")
            continue

        ratio = (t_search / t_verify) if t_verify > 0 else float("inf")
        t_search_ms = t_search * 1e3

        rec = {
            "n_vars": n_vars,
            "n_clauses": n_clauses,
            "seed": seed,
            "status": "ok",
            "t_verify_us": round(t_verify_us, 4),
            "t_search_ms": round(t_search_ms, 6),
            "ratio": round(ratio, 4),
            "decisions": solver.decisions,
            "conflicts": solver.conflicts,
        }
        instance_records.append(rec)

        if solver.k_trajectory:
            k_trajectories.append({
                "seed": seed,
                "status": "ok",
                "trajectory": solver.k_trajectory
            })

        print(f"  {seed:<8} {t_verify_us:<15.2f} {t_search_ms:<15.4f} {ratio:<12.1f} ok")

    # Compute medians
    ratios = [r["ratio"] for r in instance_records]
    t_searches = [r["t_search_ms"] for r in instance_records]
    t_verifies = [r["t_verify_us"] for r in instance_records]

    med_ratio = median(ratios)
    med_search = median(t_searches)
    med_verify = median(t_verifies)

    # K-trajectory summary
    all_k_vals = []
    k_slope_vals = []
    for traj in k_trajectories:
        pts = traj["trajectory"]
        if len(pts) >= 2:
            ks = [p["k_proxy"] for p in pts if p["k_proxy"] > 0]
            all_k_vals.extend(ks)
            # Linear trend in k over steps
            steps = [p["step"] for p in pts]
            ks_all = [p["k_proxy"] for p in pts]
            n_pts = len(steps)
            if n_pts >= 2:
                x_mean = sum(steps) / n_pts
                y_mean = sum(ks_all) / n_pts
                ss_xx = sum((x - x_mean)**2 for x in steps)
                ss_xy = sum((x - x_mean)*(y - y_mean)
                            for x, y in zip(steps, ks_all))
                slope = ss_xy / ss_xx if ss_xx > 0 else 0.0
                k_slope_vals.append(slope)

    k_summary = {}
    if all_k_vals:
        k_summary = {
            "mean_k": round(sum(all_k_vals) / len(all_k_vals), 6),
            "min_k": round(min(all_k_vals), 6),
            "max_k": round(max(all_k_vals), 6),
            "n_k_points": len(all_k_vals),
            "mean_slope": round(sum(k_slope_vals) / len(k_slope_vals), 8)
                          if k_slope_vals else None,
            "flat": abs(sum(k_slope_vals) / len(k_slope_vals)) < 1e-4
                    if k_slope_vals else None,
        }

    n_ok = len(instance_records)
    print(f"  Median: verify={med_verify:.2f}us  search={med_search:.4f}ms  "
          f"ratio={med_ratio:.1f}x  ({timeout_count} timeouts, {n_ok} ok)")
    if k_summary:
        print(f"  K-landscape: mean={k_summary['mean_k']:.4f}  "
              f"slope={k_summary.get('mean_slope', 0):.2e}  "
              f"flat={k_summary.get('flat')}")

    return {
        "n_vars": n_vars,
        "n_clauses": n_clauses,
        "n_ok": n_ok,
        "n_timeout": timeout_count,
        "median_ratio": round(med_ratio, 4) if med_ratio is not None else None,
        "median_t_search_ms": round(med_search, 6) if med_search is not None else None,
        "median_t_verify_us": round(med_verify, 4) if med_verify is not None else None,
        "instance_records": instance_records,
        "k_trajectories": k_trajectories,
        "k_summary": k_summary,
    }


def main():
    sys.setrecursionlimit(200000)

    print("=" * 72)
    print("3-SAT Large-n Scaling Study — DPLL+MCV, n=20..50")
    print(f"Phase transition: alpha = {ALPHA}  (n_clauses = {ALPHA} * n_vars)")
    print(f"Instances per n: {N_INSTANCES}   Timeout: {TIMEOUT_SEC}s")
    print(f"n_vars: {N_VARS_LIST}")
    print("=" * 72)

    all_summaries = []
    all_raw = []

    for n_vars in N_VARS_LIST:
        result = run_n(n_vars, SEEDS, TIMEOUT_SEC, track_k=True)
        all_summaries.append(result)
        all_raw.extend(result["instance_records"])

    # Exponential fit on non-timeout data points with >=2 successes
    fit_ns = []
    fit_ratios = []
    for row in all_summaries:
        if row["n_ok"] >= 2 and row["median_ratio"] is not None:
            fit_ns.append(row["n_vars"])
            fit_ratios.append(row["median_ratio"])

    fit_result = {}
    A, k, r2 = None, None, None
    if len(fit_ns) >= 3:
        A, k, r2 = fit_exponential(fit_ns, fit_ratios)
        fit_result = {
            "model": "ratio(n) = A * 2^(n/k)",
            "A": round(A, 6),
            "k": round(k, 6),
            "r_squared": round(r2, 6),
            "n_points": len(fit_ns),
            "ns_used": fit_ns,
        }
        print(f"\n{'='*72}")
        print(f"Exponential fit: ratio(n) = A * 2^(n/k)")
        print(f"  A = {A:.4f}")
        print(f"  k = {k:.4f}  (ratio doubles every {k:.2f} variables)")
        print(f"  R2 = {r2:.4f}")
    else:
        print("\nInsufficient non-timeout data for exponential fit.")

    # Predictions at n=30 and n=50
    print("\n── Results Table ──")
    header = (f"{'n':<6} {'n_cls':<7} {'ok':<4} {'timeout':<9} "
              f"{'med_ratio':<12} {'fit_pred':<12} "
              f"{'search_ms':<12} {'verify_us':<12} "
              f"{'K_mean':<10} {'K_flat'}")
    print(header)
    print("─" * len(header))

    for row in all_summaries:
        n = row["n_vars"]
        pred_str = "—"
        if A is not None and k is not None:
            pred = A * (2 ** (n / k))
            pred_str = f"{pred:.1f}"
        ratio_str = f"{row['median_ratio']:.1f}" if row["median_ratio"] else "—"
        search_str = f"{row['median_t_search_ms']:.4f}" if row["median_t_search_ms"] else "—"
        verify_str = f"{row['median_t_verify_us']:.2f}" if row["median_t_verify_us"] else "—"
        k_sum = row.get("k_summary", {})
        k_mean_str = f"{k_sum.get('mean_k', 0):.4f}" if k_sum else "—"
        k_flat_str = str(k_sum.get("flat", "—")) if k_sum else "—"
        print(f"{n:<6} {row['n_clauses']:<7} {row['n_ok']:<4} {row['n_timeout']:<9} "
              f"{ratio_str:<12} {pred_str:<12} "
              f"{search_str:<12} {verify_str:<12} "
              f"{k_mean_str:<10} {k_flat_str}")

    # Speedup n=50 vs n=30
    t30 = next((r["median_t_search_ms"] for r in all_summaries if r["n_vars"] == 30), None)
    t50 = next((r["median_t_search_ms"] for r in all_summaries if r["n_vars"] == 50), None)
    speedup_note = ""
    if t30 and t50:
        speedup_note = f"n=50 vs n=30 search time ratio: {t50/t30:.1f}x"
    elif t30:
        speedup_note = f"n=30 search time: {t30:.4f}ms (n=50 timed out)"

    print(f"\n{speedup_note}")

    # K-landscape summary
    print("\n── K-Landscape Summary ──")
    for row in all_summaries:
        k_sum = row.get("k_summary", {})
        if k_sum:
            print(f"  n={row['n_vars']}: mean_K={k_sum.get('mean_k', 0):.4f}  "
                  f"slope={k_sum.get('mean_slope', 0):.2e}  "
                  f"flat={k_sum.get('flat')}  n_pts={k_sum.get('n_k_points', 0)}")

    # Save data
    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, "sat_large_n_data.json")

    # Prepare serializable summaries (drop trajectory lists for top-level, keep in raw)
    summary_clean = []
    for row in all_summaries:
        s = {k: v for k, v in row.items()
             if k not in ("instance_records", "k_trajectories")}
        # Summarize k_trajectories count
        s["n_k_trajectory_instances"] = len(row.get("k_trajectories", []))
        summary_clean.append(s)

    output = {
        "description": "3-SAT DPLL+MCV large-n scaling study (n=20..50)",
        "date": "2026-04-09",
        "config": {
            "n_vars_list": N_VARS_LIST,
            "alpha": ALPHA,
            "n_instances": N_INSTANCES,
            "timeout_sec": TIMEOUT_SEC,
            "seeds": SEEDS,
        },
        "summary": summary_clean,
        "exponential_fit": fit_result,
        "speedup_note": speedup_note,
        "raw_instances": [
            {k: v for k, v in r.items()} for r in all_raw
        ],
        "k_trajectories_by_n": {
            str(row["n_vars"]): row.get("k_trajectories", [])
            for row in all_summaries
        },
    }

    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nData saved to {out_path}")

    return output


if __name__ == "__main__":
    result = main()
