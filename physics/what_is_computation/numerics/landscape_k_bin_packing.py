#!/usr/bin/env python3
"""
landscape_k_bin_packing.py — Cycle 31 Odd (loop 11, 2026-04-09)

Eleventh NP family for the K-trajectory probe: bin packing decision.

Problem:
    Given items with sizes s₁..sₙ and bin capacity B, can the items
    fit in k bins?

Hardness lever:
    k = (greedy bin count - 1). At k below the optimum, the search
    must enumerate. For random uniform items, the gap between greedy
    and optimum is small but enough to force exponential search.

Constraint-remnant histogram proxy:
    For each item not yet placed, count how many bins still have
    enough remaining capacity to hold it. Bucketize. Encode as fixed-
    length histogram. Easy regime: most items fit in many bins.
    Hard regime: most items fit in few bins (tight packing).

Push F1/F2 cross-family count to 11.

Writes: results/landscape_k_bin_packing_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

N_BUCKETS = 16


# ── Instance generator ──────────────────────────────────────────────────────

def gen_bin_packing_instance(n, capacity, seed):
    """
    Generate items with random sizes in [1, capacity//2]. Return
    (items, capacity).
    """
    rng = random.Random(seed * 7937 + n)
    items = [rng.randint(1, capacity // 2) for _ in range(n)]
    return items, capacity


def first_fit_bins(items, capacity):
    """First-fit greedy bin packing — gives an upper bound."""
    bins = []
    for s in sorted(items, reverse=True):  # first-fit-decreasing
        placed = False
        for i, b in enumerate(bins):
            if b + s <= capacity:
                bins[i] += s
                placed = True
                break
        if not placed:
            bins.append(s)
    return len(bins)


# ── Constraint-remnant histogram proxy ──────────────────────────────────────

def fits_per_item_histogram(items, placed, bin_remaining, capacity):
    """
    For each unplaced item, count how many bins (in `bin_remaining`)
    still have enough capacity to hold it. Bucketize counts.
    """
    histogram = [0] * N_BUCKETS
    for i, s in enumerate(items):
        if i in placed:
            continue
        fits = sum(1 for r in bin_remaining if r >= s)
        bucket = min(fits, N_BUCKETS - 1)
        histogram[bucket] = min(histogram[bucket] + 1, 255)
    return bytes(histogram)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented backtracking ──────────────────────────────────────────────

class BinPackInstrumented:
    """
    Backtracking bin packing: process items in order. For each item,
    try each existing bin (if it fits) and optionally open a new bin.
    Stop if total bins > k.
    """
    def __init__(self, items, capacity, k, record_every=10, max_steps=80000):
        self.items = items
        self.capacity = capacity
        self.k = k
        self.n = len(items)
        self.record_every = record_every
        self.max_steps = max_steps
        self.depth_k_values = []
        self.step = 0
        self.decisions = 0
        self.budget_exhausted = False

    def solve(self):
        return self._backtrack(set(), [], 0)

    def _backtrack(self, placed, bin_remaining, item_idx):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None

        if self.step % self.record_every == 0:
            data = fits_per_item_histogram(
                self.items, placed, bin_remaining, self.capacity)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step,
                "placed_count": len(placed),
                "n_bins": len(bin_remaining),
                "k_proxy": round(k, 6),
            })

        if item_idx == self.n:
            return list(bin_remaining)
        if len(bin_remaining) > self.k:
            return None  # too many bins already

        s = self.items[item_idx]
        new_placed = placed | {item_idx}

        # Try each existing bin (if it fits)
        for i in range(len(bin_remaining)):
            if bin_remaining[i] >= s:
                self.decisions += 1
                new_bins = list(bin_remaining)
                new_bins[i] -= s
                res = self._backtrack(new_placed, new_bins, item_idx + 1)
                if res is not None:
                    return res
                if self.budget_exhausted:
                    return None

        # Try opening a new bin
        if len(bin_remaining) < self.k:
            self.decisions += 1
            new_bins = bin_remaining + [self.capacity - s]
            return self._backtrack(new_placed, new_bins, item_idx + 1)
        return None


# ── Metrics ─────────────────────────────────────────────────────────────────

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


def run_experiment(n, capacity, k_offset, n_instances=8,
                   seed_base=3100, max_steps=80000):
    results = []
    for inst in range(n_instances):
        items, cap = gen_bin_packing_instance(n, capacity, seed_base + inst)
        ff = first_fit_bins(items, cap)
        k = max(1, ff + k_offset)
        solver = BinPackInstrumented(items, cap, k=k,
                                     record_every=10, max_steps=max_steps)
        t0 = time.perf_counter()
        sol = solver.solve()
        elapsed = time.perf_counter() - t0
        k_vals = [r["k_proxy"] for r in solver.depth_k_values]
        metrics = compute_metrics(k_vals)
        record = {
            "instance": inst,
            "n": n,
            "capacity": cap,
            "first_fit_bins": ff,
            "k_target": k,
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
            "decreasing (F2)" if avg < -0.0005
            else "increasing" if avg > 0.0005
            else "flat (F1 holds)"
        )
        print(f"  avg 2nd-half slope: {avg:+.6f}  →  {verdict}")


def run():
    print("=" * 72)
    print("Bin Packing Decision K-Trajectory")
    print("Cycle 31 Odd (loop 11) — 11th NP family probe")
    print("=" * 72)

    configs = [
        (15, 100, +1, "easy-15 (k > first-fit)"),
        (20, 100, -1, "hard-20 (k = first-fit - 1)"),
        (25, 100, -1, "hard-25"),
        (30, 100, -1, "hard-30"),
        (25, 50, -1, "hard-25-tight"),
    ]

    all_results = []
    for (n, cap, koff, label) in configs:
        batch = run_experiment(n, cap, koff, n_instances=8,
                               seed_base=3100, max_steps=80000)
        all_results.extend(batch)
        summarize(batch, label)

    print("\n── Per-config K second-half slope summary ──")
    print(f"{'config':<28} {'avg slope':<15} verdict")
    for (n, cap, koff, label) in configs:
        batch = [r for r in all_results
                 if r["n"] == n and r["capacity"] == cap
                 and (r["k_target"] - r["first_fit_bins"]) == koff]
        slopes = [r["second_half_slope"] for r in batch if "second_half_slope" in r]
        decs   = [r["decisions"] for r in batch]
        solved = sum(1 for r in batch if r.get("solved"))
        if slopes:
            avg = sum(slopes) / len(slopes)
            verdict = (
                "decreasing" if avg < -0.0005
                else "increasing" if avg > 0.0005
                else "flat"
            )
            print(f"{label:<28} {avg:+.6f}      {verdict}  "
                  f"(solved {solved}/{len(batch)}, dec {sum(decs)/len(decs):.0f})")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_bin_packing_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_bin_packing",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "constraint-remnant: fits-per-item histogram",
            "configs": [{"n": n, "cap": cap, "k_offset": koff, "label": l}
                        for (n, cap, koff, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
