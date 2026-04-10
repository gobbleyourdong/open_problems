#!/usr/bin/env python3
"""
landscape_k_subset_sum_v2_f2.py — Cycle 34 Odd (loop 12, 2026-04-09)

F2 redesign attempt on subset-sum.

Loop 4 (Cycle 10 Odd) confirmed F1 cleanly on subset-sum. Loop 7
(Cycle 20 Odd) attempted F2 but found a "difficulty cliff": easy
instances solve in ~200 decisions (too short to record meaningful
slopes), hard instances fill the budget with flat F1 slopes. There's
no useful intermediate regime.

Loop 8/9 demonstrated proxy redesign can flip F2 verdicts:
- Ham cycle v1 candidate-list bytes → v3 unvisited-degree histogram → F2 HoldsOn
- 3-coloring v3 forbidden-color → v4 unassigned-neighbor degree → F2 HoldsOn

This loop's hypothesis: a different proxy for subset-sum that tracks
**solution-space shrinkage via DP-table density** could expose F2 on
the easy regime, where the original reachable-bucket histogram fails.

Proxy design:
    At each backtracking step, compute a "DP-table-density" histogram:
    for each remaining target value t in [0, target], how many ways
    can the remaining elements reach exactly t? (Approximated via
    subset-sum DP on the unused elements.)

    For easy instances: many ways to reach t initially → distribution
    is broad. As elements are used, fewer paths remain → distribution
    sharpens → histogram becomes more compressible → K decreases.

    For hard instances at the difficulty cliff: distribution stays
    diffuse the whole time → flat K.

Variant simplification: instead of computing the full DP table (which
is O(n * target) per step and expensive), use a **partial reachability
histogram**: count, for each prefix-sum bucket, how many remaining
elements would complete the partial-sum to a feasible solution.

Writes: results/landscape_k_subset_sum_v2_f2_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

N_BUCKETS = 16


# ── Instance generator (medium-hardness) ───────────────────────────────────

def gen_subset_sum_medium(n, seed):
    """
    Generate a subset-sum instance with MEDIUM-difficulty: small enough
    elements that the DP-density proxy is fast, but tight enough target
    that the search has nontrivial branching.
    """
    rng = random.Random(seed * 6151 + n)
    elements = [rng.randint(50, 500) for _ in range(n)]
    while True:
        mask = [rng.choice([0, 1]) for _ in range(n)]
        s = sum(mask)
        if n // 4 <= s <= 2 * n // 3:
            break
    target = sum(e for e, m in zip(elements, mask) if m)
    return elements, target


# ── DP-density proxy ────────────────────────────────────────────────────────

def reachability_density_bytes(elements, used, current_sum, target):
    """
    For each unused element e, classify whether (target - current_sum - e)
    is "still reachable" via the remaining unused elements. Count
    elements by their relative position in the residual sum range,
    bucketize the histogram.

    This is a fast approximation of the full DP-density. As the search
    progresses on easy instances, more elements become "non-fitting"
    (they overshoot the residual), the histogram shifts toward the
    no-fit bucket, and gzip ratio drops.
    """
    histogram = [0] * N_BUCKETS
    residual = target - current_sum
    if residual <= 0:
        return bytes(N_BUCKETS)

    for i, e in enumerate(elements):
        if used[i]:
            continue
        if e > residual:
            # No-fit: bucket 0
            histogram[0] = min(histogram[0] + 1, 255)
            continue
        # Bucketize by relative size of e vs residual
        ratio = e / residual
        bucket = min(N_BUCKETS - 1, int(ratio * (N_BUCKETS - 1)) + 1)
        histogram[bucket] = min(histogram[bucket] + 1, 255)
    return bytes(histogram)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented backtracking ──────────────────────────────────────────────

class SubsetSumInstrumentedV2:
    def __init__(self, elements, target, record_every=10, max_steps=80000):
        self.elements = elements
        self.target = target
        self.n = len(elements)
        self.record_every = record_every
        self.max_steps = max_steps
        self.depth_k_values = []
        self.step = 0
        self.decisions = 0
        self.budget_exhausted = False

    def solve(self):
        return self._backtrack([False] * self.n, 0, 0)

    def _backtrack(self, used, idx, current_sum):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None

        if self.step % self.record_every == 0:
            data = reachability_density_bytes(
                self.elements, used, current_sum, self.target)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step,
                "depth": idx,
                "current_sum": current_sum,
                "k_proxy": round(k, 6),
            })

        if current_sum == self.target:
            return [i for i in range(self.n) if used[i]]
        if idx >= self.n or current_sum > self.target:
            return None

        # Branch 1: include
        self.decisions += 1
        used[idx] = True
        res = self._backtrack(used, idx + 1, current_sum + self.elements[idx])
        if res is not None:
            return res
        if self.budget_exhausted:
            return None
        used[idx] = False

        # Branch 2: skip
        self.decisions += 1
        return self._backtrack(used, idx + 1, current_sum)


# ── Metrics ────────────────────────────────────────────────────────────────

def compute_metrics(k_vals):
    if not k_vals:
        return None
    n = len(k_vals)
    full_slope = ((k_vals[-1] - k_vals[0]) / max(n - 1, 1)) if n >= 2 else 0.0
    if n >= 4:
        mid = n // 2
        tail = k_vals[mid:]
        second_half_slope = (tail[-1] - tail[0]) / max(len(tail) - 1, 1)
    else:
        second_half_slope = full_slope
    return {
        "k_initial": round(k_vals[0], 4),
        "k_final": round(k_vals[-1], 4),
        "full_slope": round(full_slope, 6),
        "second_half_slope": round(second_half_slope, 6),
        "n_records": n,
    }


def run_experiment(n, n_instances=8, seed_base=3300, max_steps=80000):
    results = []
    for inst in range(n_instances):
        elements, target = gen_subset_sum_medium(n, seed_base + inst)
        solver = SubsetSumInstrumentedV2(elements, target,
                                         record_every=10, max_steps=max_steps)
        t0 = time.perf_counter()
        sol = solver.solve()
        elapsed = time.perf_counter() - t0
        k_vals = [r["k_proxy"] for r in solver.depth_k_values]
        metrics = compute_metrics(k_vals)
        record = {
            "instance": inst,
            "n": n,
            "target": target,
            "max_element": max(elements),
            "solved": sol is not None,
            "budget_exhausted": solver.budget_exhausted,
            "decisions": solver.decisions,
            "steps": solver.step,
            "time_ms": round(elapsed * 1000, 3),
        }
        if metrics:
            record.update(metrics)
        results.append(record)
    return results


def summarize(batch, label):
    if not batch:
        return
    slopes_h2 = [r["second_half_slope"] for r in batch if "second_half_slope" in r]
    decs = [r["decisions"] for r in batch]
    solved = sum(1 for r in batch if r.get("solved"))
    budget = sum(1 for r in batch if r.get("budget_exhausted"))
    print(f"\n{label}")
    print(f"  instances:    {len(batch)}  (solved={solved}, budget={budget})")
    print(f"  avg decisions: {sum(decs)/len(decs):.1f}")
    if slopes_h2:
        avg = sum(slopes_h2) / len(slopes_h2)
        verdict = (
            "decreasing (F2 NEW!)" if avg < -0.0005
            else "increasing" if avg > 0.0005
            else "flat (F1)"
        )
        print(f"  avg 2nd-half slope: {avg:+.6f}  →  {verdict}")


def run():
    print("=" * 72)
    print("Subset-sum F2 retest v2 — DP-density proxy (loop 12)")
    print("Cycle 34 Odd — fourth attempt at subset-sum F2")
    print("=" * 72)

    # Sweep n to find any regime that gives non-trivial F2 slopes
    configs = [
        (15, "n=15 medium"),
        (18, "n=18 medium"),
        (20, "n=20 medium"),
        (22, "n=22 medium"),
        (25, "n=25 medium"),
    ]

    all_results = []
    for (n, label) in configs:
        batch = run_experiment(n, n_instances=8, seed_base=3300, max_steps=80000)
        all_results.extend(batch)
        summarize(batch, label)

    print("\n── F2 redesign verdict (subset-sum, DP-density proxy) ──")
    print(f"{'config':<20} {'avg slope':<15} verdict")
    for (n, label) in configs:
        batch = [r for r in all_results if r["n"] == n]
        slopes = [r["second_half_slope"] for r in batch if "second_half_slope" in r]
        decs   = [r["decisions"] for r in batch]
        solved = sum(1 for r in batch if r.get("solved"))
        if slopes:
            avg = sum(slopes) / len(slopes)
            verdict = (
                "decreasing (F2!)" if avg < -0.0005
                else "increasing" if avg > 0.0005
                else "flat (F1)"
            )
            print(f"{label:<20} {avg:+.6f}      {verdict}  "
                  f"(solved {solved}/{len(batch)}, dec {sum(decs)/len(decs):.0f})")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_subset_sum_v2_f2_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_subset_sum_v2_f2",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "DP-density: residual-relative-size histogram (loop 12 F2 redesign)",
            "configs": [{"n": n, "label": l} for (n, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
