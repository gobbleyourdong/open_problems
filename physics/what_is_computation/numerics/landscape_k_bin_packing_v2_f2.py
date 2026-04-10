#!/usr/bin/env python3
"""
landscape_k_bin_packing_v2_f2.py — Cycle 38 Odd (loop 13, 2026-04-09)

F2 redesign attempt on bin packing.

Loop 11 confirmed F1 cleanly on bin packing via the fits-per-item
proxy, but found F2 untestable (easy regime trivial: 15 decisions).

Loops 12-13 demonstrated that the difficulty cliff can be escaped
with a redesigned proxy. Subset-sum (loop 12) flipped via
residual-relative-size histogram. Knapsack (loop 13 Cycle 37 Odd)
flipped marginally via weight-residual density.

This loop applies the same template to bin packing:
    For each unplaced item, compute its size as a fraction of
    each bin's REMAINING capacity, and bucketize the histogram
    of these fit-ratios. As bins fill up, the histogram shifts
    toward "no-fit" — F2 shrinkage signal.

If F2 flips, bin packing joins the both-testable category and
all 12 NP families have BOTH F1 and F2 confirmed (modulo F1
untestables for 3-DM and FVS).

Writes: results/landscape_k_bin_packing_v2_f2_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

N_BUCKETS = 16


def gen_bin_packing_medium(n, capacity, seed):
    """
    Medium-difficulty bin packing: items distributed in [0.1*cap, 0.4*cap]
    so that 2-3 items fit per bin and the search must explore which
    items go together.
    """
    rng = random.Random(seed * 7937 + n)
    items = [rng.randint(int(0.1 * capacity), int(0.4 * capacity)) for _ in range(n)]
    rng.shuffle(items)  # disrupt any natural order
    return items, capacity


def first_fit_bins(items, capacity):
    """First-fit-decreasing greedy upper bound."""
    bins = []
    for s in sorted(items, reverse=True):
        placed = False
        for i, b in enumerate(bins):
            if b + s <= capacity:
                bins[i] += s
                placed = True
                break
        if not placed:
            bins.append(s)
    return len(bins)


# ── Density proxy: item-to-min-bin-residual ratio histogram ────────────────

def item_density_bytes(items, placed, bin_remaining, capacity):
    """
    For each unplaced item, classify by max(item_size / bin_remaining[b])
    over all bins b — i.e., the BEST fit-ratio across existing bins.
    Items that fit nowhere (no bin has enough room) go to bucket 0.
    Items that exactly fill some bin go to bucket N_BUCKETS-1.
    """
    histogram = [0] * N_BUCKETS
    for i, s in enumerate(items):
        if i in placed:
            continue
        # Find the tightest fit across all existing bins
        best_ratio = 0.0
        fits_anywhere = False
        for r in bin_remaining:
            if s <= r:
                fits_anywhere = True
                ratio = s / r
                if ratio > best_ratio:
                    best_ratio = ratio
        if not fits_anywhere:
            # Doesn't fit in any current bin → would need a new bin
            histogram[0] = min(histogram[0] + 1, 255)
            continue
        bucket = min(N_BUCKETS - 1, int(best_ratio * (N_BUCKETS - 1)) + 1)
        histogram[bucket] = min(histogram[bucket] + 1, 255)
    return bytes(histogram)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented backtracking ──────────────────────────────────────────────

class BinPackInstrumentedV2:
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
            data = item_density_bytes(
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
            return None

        s = self.items[item_idx]
        new_placed = placed | {item_idx}

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

        if len(bin_remaining) < self.k:
            self.decisions += 1
            new_bins = bin_remaining + [self.capacity - s]
            return self._backtrack(new_placed, new_bins, item_idx + 1)
        return None


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
                   seed_base=3800, max_steps=80000):
    results = []
    for inst in range(n_instances):
        items, cap = gen_bin_packing_medium(n, capacity, seed_base + inst)
        ff = first_fit_bins(items, cap)
        k = max(1, ff + k_offset)
        solver = BinPackInstrumentedV2(items, cap, k=k,
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
            "decreasing (F2 NEW!)" if avg < -0.0005
            else "increasing" if avg > 0.0005
            else "flat (F1)"
        )
        print(f"  avg 2nd-half slope: {avg:+.6f}  →  {verdict}")


def run():
    print("=" * 72)
    print("Bin Packing F2 retest v2 — item-density proxy")
    print("Cycle 38 Odd (loop 13)")
    print("=" * 72)

    # Use larger n with k = first-fit (not -1) so the search has work
    # but still completes
    configs = [
        (15, 100, 0, "n=15 k=ff"),
        (20, 100, 0, "n=20 k=ff"),
        (25, 100, 0, "n=25 k=ff"),
        (20, 100, +1, "n=20 k=ff+1 (loose)"),
    ]

    all_results = []
    for (n, cap, koff, label) in configs:
        batch = run_experiment(n, cap, koff, n_instances=8,
                               seed_base=3800, max_steps=80000)
        all_results.extend(batch)
        summarize(batch, label)

    print("\n── F2 redesign verdict (bin packing, density proxy) ──")
    print(f"{'config':<25} {'avg slope':<15} verdict")
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
                "decreasing (F2!)" if avg < -0.0005
                else "increasing" if avg > 0.0005
                else "flat (F1)"
            )
            print(f"{label:<25} {avg:+.6f}      {verdict}  "
                  f"(solved {solved}/{len(batch)}, dec {sum(decs)/len(decs):.0f})")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_bin_packing_v2_f2_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_bin_packing_v2_f2",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "item-density (max fit-ratio across bins) histogram",
            "configs": [{"n": n, "cap": cap, "k_offset": koff, "label": l}
                        for (n, cap, koff, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
