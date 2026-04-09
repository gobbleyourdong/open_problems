#!/usr/bin/env python3
"""
sat_n60.py — Phase 4: extend the DPLL+MCV scaling study to n=55, 60.

Context: sat_large_n.py confirmed K-flat landscape at n=50 (hardest instance:
K_mean=0.620, σ=0.017 across 62 K-points). SAT k=26.6 doubling period at
large n.  This script pushes to n=55,60 with a 120-second timeout, adds those
data points to the exponential fit, and shows the K-trajectory is still flat.

Measurements per n:
  - 5 instances at phase transition (alpha = 4.3)
  - Median find/verify ratio, median search time, timeout count
  - K-trajectory with finer gzip sampling (every step)

Exponential fit includes prior data from sat_large_n_data.json.

Also runs a phase-transition anatomy study: find/verify ratio at three clause
ratios (2.0, 4.3, 7.0) for n=30, to demonstrate why 4.3 is the hardest.

Numerical track, what_is_computation Phase 4 — 2026-04-09
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

ALPHA = 4.3        # phase-transition clause-to-variable ratio
N_VARS_NEW = [55, 60]
N_INSTANCES = 5
TIMEOUT_SEC = 120.0
SEEDS = [17, 53, 103, 197, 251]

# For anatomy study
ANATOMY_N = 30
ANATOMY_RATIOS = [2.0, 4.3, 7.0]
ANATOMY_SEEDS = [17, 53, 103, 197, 251]
ANATOMY_TIMEOUT = 60.0

RESULTS_DIR = "~/open_problems/physics/what_is_computation/results"
PRIOR_DATA_PATH = os.path.join(RESULTS_DIR, "sat_large_n_data.json")
OUT_DATA_PATH = os.path.join(RESULTS_DIR, "sat_n60_data.json")


# ── SAT instance generator ────────────────────────────────────────────────────

def sat_instance_guaranteed(n_vars: int, n_clauses: int, seed: int):
    """
    Generate a guaranteed-SAT 3-SAT instance.
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


def sat_instance_random(n_vars: int, n_clauses: int, seed: int):
    """
    Generate a random 3-SAT instance (may be UNSAT, especially at high ratio).
    Returns (clauses, None).
    """
    rng = random.Random(seed)
    clauses = []
    for _ in range(n_clauses):
        vars_ = rng.sample(range(1, n_vars + 1), 3)
        lits = [v if rng.random() < 0.5 else -v for v in vars_]
        clauses.append(lits)
    return clauses, None


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
                continue
            unset = [l for l in clause if not lit_false(l, asgn) and not lit_true(l, asgn)]
            if len(unset) == 0:
                return None
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
            continue
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
    K-trajectory tracking. Extended for n up to ~60 with 120s timeout.
    """
    def __init__(self, n_vars: int, clauses: list, seed: int,
                 track_k: bool = False, deadline: float = None,
                 k_sample_every: int = 1):
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
        return max(unset, key=lambda v: (counts.get(v, 0), v))

    def _dpll(self, asgn: dict) -> Optional[dict]:
        if self.deadline and time.perf_counter() > self.deadline:
            raise TimeoutSignal()

        self._step += 1
        asgn = unit_propagate(self.clauses, asgn)
        if asgn is None:
            self.conflicts += 1
            return None

        # K-content tracking (finer sampling: every k_sample_every steps)
        if self.track_k and self._step % self.k_sample_every == 0:
            data = remaining_clause_bytes(self.clauses, asgn)
            k = k_proxy(data)
            if k > 0:
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


def stdev(xs):
    if len(xs) < 2:
        return 0.0
    m = sum(xs) / len(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


# ── Run a batch of instances at a given (n_vars, alpha) ──────────────────────

def run_batch(n_vars: int, alpha: float, seeds: list, timeout_sec: float,
              track_k: bool = True, guaranteed_sat: bool = True,
              k_sample_every: int = 1) -> dict:
    """Run all instances for a given (n_vars, alpha). Returns summary dict."""
    n_clauses = round(alpha * n_vars)
    instance_records = []
    timeout_count = 0
    k_trajectories = []
    unsat_count = 0

    print(f"\n  n={n_vars}, alpha={alpha:.1f}, n_clauses={n_clauses}, "
          f"timeout={timeout_sec}s, guaranteed={'yes' if guaranteed_sat else 'no'}")
    print(f"  {'seed':<8} {'t_verify(us)':<15} {'t_search(ms)':<15} {'ratio':<12} {'status'}")
    print(f"  {'─'*8} {'─'*13} {'─'*13} {'─'*10} {'─'*8}")

    for seed in seeds:
        if guaranteed_sat:
            clauses, known_asgn = sat_instance_guaranteed(n_vars, n_clauses, seed)
            if not sat_verify(clauses, known_asgn):
                print(f"  {seed:<8} [BUG: constructed UNSAT instance]")
                continue
            # Time verification (cheap direction)
            t0 = time.perf_counter()
            sat_verify(clauses, known_asgn)
            t_verify = time.perf_counter() - t0
        else:
            clauses, known_asgn = sat_instance_random(n_vars, n_clauses, seed)
            # Verify with DPLL first pass to get timing baseline
            t0 = time.perf_counter()
            # For random instances at high ratio, verification is trivially via
            # the DPLL solution — we measure DPLL time only.
            t_verify = 1e-6  # placeholder; will compute from DPLL time
            known_asgn = None

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
            if solver.k_trajectory:
                k_trajectories.append({
                    "seed": seed,
                    "status": "timeout",
                    "trajectory": solver.k_trajectory,
                })
            continue

        if found_asgn is None:
            unsat_count += 1
            print(f"  {seed:<8} {t_verify_us:<15.2f} "
                  f"{t_search*1e3:<15.4f} {'UNSAT':<12}")
            instance_records.append({
                "n_vars": n_vars,
                "n_clauses": n_clauses,
                "alpha": alpha,
                "seed": seed,
                "status": "unsat",
                "t_verify_us": round(t_verify_us, 4),
                "t_search_ms": round(t_search * 1e3, 6),
                "ratio": None,
                "decisions": solver.decisions,
                "conflicts": solver.conflicts,
            })
            continue

        # Measure verify time properly if we didn't have a known assignment
        if known_asgn is None:
            t0 = time.perf_counter()
            sat_verify(clauses, found_asgn)
            t_verify = time.perf_counter() - t0
            t_verify_us = t_verify * 1e6

        if not sat_verify(clauses, found_asgn):
            print(f"  {seed:<8} {t_verify_us:<15.2f} {'—':<15} {'BAD_SOL':<12}")
            continue

        ratio = (t_search / t_verify) if t_verify > 0 else float("inf")
        t_search_ms = t_search * 1e3

        rec = {
            "n_vars": n_vars,
            "n_clauses": n_clauses,
            "alpha": alpha,
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
                "trajectory": solver.k_trajectory,
            })

        print(f"  {seed:<8} {t_verify_us:<15.2f} {t_search_ms:<15.4f} {ratio:<12.1f} ok")

    # Compute statistics over SAT-solved instances
    ok_records = [r for r in instance_records if r["status"] == "ok"]
    ratios = [r["ratio"] for r in ok_records]
    t_searches = [r["t_search_ms"] for r in ok_records]
    t_verifies = [r["t_verify_us"] for r in ok_records]

    med_ratio = median(ratios)
    med_search = median(t_searches)
    med_verify = median(t_verifies)
    max_ratio = max(ratios) if ratios else None
    min_ratio = min(ratios) if ratios else None

    # K-trajectory summary (only ok trajectories)
    all_k_vals = []
    k_slope_vals = []
    for traj in k_trajectories:
        if traj["status"] != "ok":
            continue
        pts = traj["trajectory"]
        if len(pts) >= 2:
            ks = [p["k_proxy"] for p in pts if p["k_proxy"] > 0]
            all_k_vals.extend(ks)
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
        mean_slope = (sum(k_slope_vals) / len(k_slope_vals)) if k_slope_vals else 0.0
        k_summary = {
            "mean_k": round(sum(all_k_vals) / len(all_k_vals), 6),
            "stdev_k": round(stdev(all_k_vals), 6),
            "min_k": round(min(all_k_vals), 6),
            "max_k": round(max(all_k_vals), 6),
            "n_k_points": len(all_k_vals),
            "mean_slope": round(mean_slope, 8) if k_slope_vals else None,
            "flat": abs(mean_slope) < 1e-3 if k_slope_vals else None,
        }

    n_ok = len(ok_records)
    if med_ratio is not None:
        print(f"  Median: verify={med_verify:.2f}us  search={med_search:.4f}ms  "
              f"ratio={med_ratio:.1f}x  max_ratio={max_ratio:.1f}x  "
              f"({timeout_count} TO, {unsat_count} UNSAT, {n_ok} ok)")
    else:
        print(f"  No SAT solutions found  "
              f"({timeout_count} TO, {unsat_count} UNSAT, {n_ok} ok)")

    if k_summary:
        print(f"  K: mean={k_summary['mean_k']:.4f}±{k_summary['stdev_k']:.4f}  "
              f"slope={k_summary.get('mean_slope', 0):.2e}  "
              f"flat={k_summary.get('flat')}  n_pts={k_summary['n_k_points']}")

    return {
        "n_vars": n_vars,
        "n_clauses": n_clauses,
        "alpha": alpha,
        "n_ok": n_ok,
        "n_timeout": timeout_count,
        "n_unsat": unsat_count,
        "median_ratio": round(med_ratio, 4) if med_ratio is not None else None,
        "max_ratio": round(max_ratio, 4) if max_ratio is not None else None,
        "min_ratio": round(min_ratio, 4) if min_ratio is not None else None,
        "median_t_search_ms": round(med_search, 6) if med_search is not None else None,
        "median_t_verify_us": round(med_verify, 4) if med_verify is not None else None,
        "instance_records": instance_records,
        "k_trajectories": k_trajectories,
        "k_summary": k_summary,
    }


# ── Phase-transition anatomy: 3 clause ratios at n=30 ────────────────────────

def run_anatomy(n_vars: int, alphas: list, seeds: list, timeout_sec: float) -> dict:
    """
    For each alpha in alphas, run instances and measure find/verify ratio
    and K-landscape. Returns anatomy dict keyed by alpha.
    """
    print(f"\n{'='*72}")
    print(f"Phase-Transition Anatomy: n={n_vars}, alphas={alphas}")
    print("  At alpha<4.3: underconstrained (many SAT solutions, easy)")
    print("  At alpha=4.3: maximally constrained (K-flat, hardest)")
    print("  At alpha>4.3: overconstrained (likely UNSAT, easy to refute)")
    print(f"{'='*72}")

    anatomy = {}
    for alpha in alphas:
        use_guaranteed = alpha <= 4.3  # random instances more natural above transition
        result = run_batch(
            n_vars=n_vars,
            alpha=alpha,
            seeds=seeds,
            timeout_sec=timeout_sec,
            track_k=True,
            guaranteed_sat=use_guaranteed,
            k_sample_every=1,
        )
        anatomy[str(alpha)] = {
            "alpha": alpha,
            "n_vars": n_vars,
            "n_clauses": result["n_clauses"],
            "n_ok": result["n_ok"],
            "n_timeout": result["n_timeout"],
            "n_unsat": result["n_unsat"],
            "median_ratio": result["median_ratio"],
            "max_ratio": result["max_ratio"],
            "median_t_search_ms": result["median_t_search_ms"],
            "median_t_verify_us": result["median_t_verify_us"],
            "k_summary": result["k_summary"],
            "instance_records": result["instance_records"],
            "k_trajectories": result["k_trajectories"],
        }

    print(f"\n── Anatomy Summary (n={n_vars}) ──")
    print(f"{'alpha':<8} {'regime':<22} {'n_ok':<6} {'n_unsat':<9} "
          f"{'med_ratio':<12} {'K_mean':<10} {'K_slope':<12} {'K_flat'}")
    print("─" * 90)
    for alpha in alphas:
        row = anatomy[str(alpha)]
        if alpha < 4.0:
            regime = "underconstrained"
        elif alpha <= 4.5:
            regime = "phase transition"
        else:
            regime = "overconstrained"
        ks = row["k_summary"]
        ratio_str = f"{row['median_ratio']:.1f}" if row["median_ratio"] is not None else "—"
        km = f"{ks.get('mean_k', 0):.4f}" if ks else "—"
        ksl = f"{ks.get('mean_slope', 0):.2e}" if ks else "—"
        kfl = str(ks.get('flat', '—')) if ks else "—"
        print(f"{alpha:<8.1f} {regime:<22} {row['n_ok']:<6} {row['n_unsat']:<9} "
              f"{ratio_str:<12} {km:<10} {ksl:<12} {kfl}")

    return anatomy


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    sys.setrecursionlimit(500000)
    os.makedirs(RESULTS_DIR, exist_ok=True)

    print("=" * 72)
    print("3-SAT Phase 4 — n=55,60 + Phase-Transition Anatomy")
    print(f"Phase transition: alpha = {ALPHA}")
    print(f"New n_vars: {N_VARS_NEW}   Timeout: {TIMEOUT_SEC}s   Instances: {N_INSTANCES}")
    print("=" * 72)

    # ── Step 1: Load prior data from sat_large_n_data.json ─────────────────
    prior_summaries = []
    if os.path.exists(PRIOR_DATA_PATH):
        with open(PRIOR_DATA_PATH) as f:
            prior_data = json.load(f)
        prior_summaries = prior_data.get("summary", [])
        print(f"\nLoaded {len(prior_summaries)} prior data points from "
              f"sat_large_n_data.json (n=20..50)")
    else:
        print(f"\nWarning: prior data not found at {PRIOR_DATA_PATH}")

    # ── Step 2: Run n=55, 60 at alpha=4.3 ──────────────────────────────────
    print(f"\n{'='*72}")
    print(f"Running new n-values: {N_VARS_NEW} at alpha={ALPHA}")
    print(f"{'='*72}")

    new_summaries = []
    new_all_records = []

    for n_vars in N_VARS_NEW:
        result = run_batch(
            n_vars=n_vars,
            alpha=ALPHA,
            seeds=SEEDS,
            timeout_sec=TIMEOUT_SEC,
            track_k=True,
            guaranteed_sat=True,
            k_sample_every=1,   # finer gzip sampling
        )
        new_summaries.append(result)
        new_all_records.extend(result["instance_records"])

    # ── Step 3: Exponential fit, combining prior + new data ─────────────────
    # Build combined (n, median_ratio) series
    combined_ns = []
    combined_ratios = []

    for row in prior_summaries:
        if row.get("n_ok", 0) >= 2 and row.get("median_ratio") is not None:
            combined_ns.append(row["n_vars"])
            combined_ratios.append(row["median_ratio"])

    for row in new_summaries:
        if row.get("n_ok", 0) >= 2 and row.get("median_ratio") is not None:
            combined_ns.append(row["n_vars"])
            combined_ratios.append(row["median_ratio"])

    fit_result = {}
    A, k_fit, r2 = None, None, None
    if len(combined_ns) >= 3:
        A, k_fit, r2 = fit_exponential(combined_ns, combined_ratios)
        fit_result = {
            "model": "ratio(n) = A * 2^(n/k)",
            "A": round(A, 6),
            "k": round(k_fit, 6),
            "r_squared": round(r2, 6),
            "n_points": len(combined_ns),
            "ns_used": combined_ns,
            "ratios_used": [round(r, 4) for r in combined_ratios],
        }
        print(f"\n{'='*72}")
        print("Combined Exponential Fit (n=20..60, DPLL+MCV, alpha=4.3):")
        print(f"  ratio(n) = {A:.4f} * 2^(n / {k_fit:.4f})")
        print(f"  k = {k_fit:.4f}  (ratio doubles every {k_fit:.2f} variables)")
        print(f"  R² = {r2:.4f}   n_points = {len(combined_ns)}")

    # ── Step 4: Phase-transition anatomy at n=30 ────────────────────────────
    anatomy = run_anatomy(
        n_vars=ANATOMY_N,
        alphas=ANATOMY_RATIOS,
        seeds=ANATOMY_SEEDS,
        timeout_sec=ANATOMY_TIMEOUT,
    )

    # ── Step 5: Full results table (prior + new) ─────────────────────────────
    print(f"\n{'='*72}")
    print("Full Results Table (prior sat_large_n + new n=55,60):")
    header = (f"{'n':<6} {'alpha':<7} {'n_ok':<5} {'TO':<4} "
              f"{'med_ratio':<12} {'fit_pred':<12} "
              f"{'search_ms':<12} {'verify_us':<11} "
              f"{'K_mean':<10} {'K_flat'}")
    print(header)
    print("─" * len(header))

    all_rows = []
    for row in prior_summaries:
        all_rows.append({
            "n_vars": row["n_vars"],
            "alpha": ALPHA,
            "n_ok": row["n_ok"],
            "n_timeout": row.get("n_timeout", 0),
            "median_ratio": row.get("median_ratio"),
            "median_t_search_ms": row.get("median_t_search_ms"),
            "median_t_verify_us": row.get("median_t_verify_us"),
            "k_summary": row.get("k_summary", {}),
        })

    for row in new_summaries:
        all_rows.append({
            "n_vars": row["n_vars"],
            "alpha": row["alpha"],
            "n_ok": row["n_ok"],
            "n_timeout": row.get("n_timeout", 0),
            "median_ratio": row.get("median_ratio"),
            "median_t_search_ms": row.get("median_t_search_ms"),
            "median_t_verify_us": row.get("median_t_verify_us"),
            "k_summary": row.get("k_summary", {}),
        })

    for row in all_rows:
        n = row["n_vars"]
        pred_str = "—"
        if A is not None and k_fit is not None:
            pred = A * (2 ** (n / k_fit))
            pred_str = f"{pred:.1f}"
        ratio_str = f"{row['median_ratio']:.1f}" if row["median_ratio"] else "—"
        search_str = f"{row['median_t_search_ms']:.4f}" if row["median_t_search_ms"] else "—"
        verify_str = f"{row['median_t_verify_us']:.2f}" if row["median_t_verify_us"] else "—"
        ks = row.get("k_summary", {})
        k_mean_str = f"{ks.get('mean_k', 0):.4f}" if ks else "—"
        k_flat_str = str(ks.get("flat", "—")) if ks else "—"
        print(f"{n:<6} {row['alpha']:<7.1f} {row['n_ok']:<5} {row['n_timeout']:<4} "
              f"{ratio_str:<12} {pred_str:<12} "
              f"{search_str:<12} {verify_str:<11} "
              f"{k_mean_str:<10} {k_flat_str}")

    # ── Step 6: Save data ────────────────────────────────────────────────────
    def clean_summary(row):
        """Return summary without full trajectory lists."""
        s = {kk: vv for kk, vv in row.items()
             if kk not in ("instance_records", "k_trajectories")}
        s["n_k_trajectory_instances"] = len(row.get("k_trajectories", []))
        return s

    anatomy_clean = {}
    for alpha_str, arow in anatomy.items():
        ac = {kk: vv for kk, vv in arow.items()
              if kk not in ("instance_records", "k_trajectories")}
        ac["n_k_trajectory_instances"] = len(arow.get("k_trajectories", []))
        anatomy_clean[alpha_str] = ac

    output = {
        "description": (
            "3-SAT DPLL+MCV phase 4 study — n=55,60 + phase-transition anatomy"
        ),
        "date": "2026-04-09",
        "config": {
            "n_vars_new": N_VARS_NEW,
            "alpha": ALPHA,
            "n_instances": N_INSTANCES,
            "timeout_sec": TIMEOUT_SEC,
            "seeds": SEEDS,
            "anatomy_n": ANATOMY_N,
            "anatomy_alphas": ANATOMY_RATIOS,
            "anatomy_seeds": ANATOMY_SEEDS,
            "anatomy_timeout": ANATOMY_TIMEOUT,
        },
        "new_summaries": [clean_summary(r) for r in new_summaries],
        "combined_exponential_fit": fit_result,
        "prior_fit": {
            "A": 49.266773,
            "k": 26.568305,
            "r_squared": 0.647298,
            "n_points": 7,
            "ns_used": [20, 25, 30, 35, 40, 45, 50],
        },
        "anatomy": anatomy_clean,
        "raw_new_instances": [
            {kk: vv for kk, vv in r.items()} for r in new_all_records
        ],
        "k_trajectories_new": {
            str(row["n_vars"]): row.get("k_trajectories", [])
            for row in new_summaries
        },
        "anatomy_k_trajectories": {
            alpha_str: arow.get("k_trajectories", [])
            for alpha_str, arow in anatomy.items()
        },
    }

    with open(OUT_DATA_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nData saved to {OUT_DATA_PATH}")

    return output


if __name__ == "__main__":
    result = main()
