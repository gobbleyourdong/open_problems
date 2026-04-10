#!/usr/bin/env python3
"""
landscape_k_f2_retest.py — Cycle 20 Odd (loop 7, 2026-04-09)

Retest F2 ("easier → K decreasing") on subset-sum and knapsack with a
moderate-difficulty regime that produces NON-trivially-long searches
(thousands of decisions instead of tens). The loop 4-5 easy regimes
were too short (3-200 decisions per instance) for F2 to be detectable.

Strategy:
    For both families, generate "moderate" instances that:
      - Have enough elements/items to require thousands of decisions
      - Are not at the hardest regime (so they finish within budget)
      - Produce >10 K-records each (enough for second-half slope)

For subset-sum: medium-large elements (10^3..10^5), target = 1/3 of
sum (loose enough to find a witness, tight enough to require search).

For knapsack: medium-correlated items, target value = (1 - 1/n) of
optimum (so the search has to find one of many near-optimal solutions
rather than the unique optimum).

Writes: results/landscape_k_f2_retest_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

# ── Subset-sum reusing the loop 4 proxy ────────────────────────────────────

N_BUCKETS_SS = 16


def gen_subset_sum_moderate(n, seed):
    """Medium scale for non-trivial F2 testing."""
    rng = random.Random(seed * 6151 + n)
    elements = [rng.randint(10**3, 10**5) for _ in range(n)]
    while True:
        mask = [rng.choice([0, 1]) for _ in range(n)]
        s = sum(mask)
        if n // 4 <= s <= n // 2:
            break
    target = sum(e for e, m in zip(elements, mask) if m)
    return elements, target


def reachable_buckets_bytes_ss(elements, used, remaining_target):
    if remaining_target <= 0:
        return bytes(N_BUCKETS_SS)
    counts = [0] * N_BUCKETS_SS
    for i, e in enumerate(elements):
        if used[i]:
            continue
        if e > remaining_target:
            continue
        bucket = (remaining_target % e) % N_BUCKETS_SS
        counts[bucket] = min(counts[bucket] + 1, 255)
    return bytes(counts)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


class SubsetSumInstrumented:
    def __init__(self, elements, target, record_every=20, max_steps=80000):
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
            data = reachable_buckets_bytes_ss(
                self.elements, used, self.target - current_sum)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step, "depth": idx,
                "k_proxy": round(k, 6),
            })
        if current_sum == self.target:
            return [i for i in range(self.n) if used[i]]
        if idx >= self.n or current_sum > self.target:
            return None
        self.decisions += 1
        used[idx] = True
        res = self._backtrack(used, idx + 1, current_sum + self.elements[idx])
        if res is not None:
            return res
        if self.budget_exhausted:
            return None
        used[idx] = False
        self.decisions += 1
        return self._backtrack(used, idx + 1, current_sum)


# ── Knapsack reusing the loop 5 proxy ──────────────────────────────────────

N_BUCKETS_KS = 16


def gen_knapsack_moderate(n, seed):
    """
    Moderate-correlated knapsack: weight = value with small noise,
    capacity = sum/2, target = optimum * (1 - 2/n) (loose enough that
    several near-optimal subsets work).
    """
    rng = random.Random(seed * 5471 + n)
    weights = []
    values = []
    for _ in range(n):
        w = rng.randint(10**3, 10**4)
        v = w + rng.randint(-100, 100)
        weights.append(w)
        values.append(max(1, v))
    capacity = sum(weights) // 2
    optimum = brute_force_optimum(weights, values, capacity)
    # Loose target: 90% of optimum
    target = max(1, int(optimum * 0.90))
    return weights, values, capacity, target


def brute_force_optimum(weights, values, capacity):
    n = len(weights)
    best = 0
    for mask in range(1 << n):
        w = 0
        v = 0
        for i in range(n):
            if mask & (1 << i):
                w += weights[i]
                v += values[i]
                if w > capacity:
                    break
        else:
            if v > best:
                best = v
    return best


def feasibility_buckets_bytes(weights, used, capacity_remaining):
    if capacity_remaining <= 0:
        return bytes(N_BUCKETS_KS)
    counts = [0] * N_BUCKETS_KS
    for i, w in enumerate(weights):
        if used[i]:
            continue
        if w > capacity_remaining:
            counts[0] = min(counts[0] + 1, 255)
            continue
        margin = capacity_remaining - w
        bucket = min(N_BUCKETS_KS - 1,
                     int((margin / capacity_remaining) * (N_BUCKETS_KS - 1)) + 1)
        counts[bucket] = min(counts[bucket] + 1, 255)
    return bytes(counts)


class KnapsackInstrumented:
    def __init__(self, weights, values, capacity, target_value,
                 record_every=20, max_steps=80000):
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.target_value = target_value
        self.n = len(weights)
        self.record_every = record_every
        self.max_steps = max_steps
        self.depth_k_values = []
        self.step = 0
        self.decisions = 0
        self.budget_exhausted = False

    def solve(self):
        return self._backtrack([False] * self.n, 0, 0, 0)

    def _backtrack(self, used, idx, cw, cv):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None
        if self.step % self.record_every == 0:
            data = feasibility_buckets_bytes(
                self.weights, used, self.capacity - cw)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step, "depth": idx,
                "k_proxy": round(k, 6),
            })
        if cv >= self.target_value and cw <= self.capacity:
            return [i for i in range(self.n) if used[i]]
        if idx >= self.n or cw > self.capacity:
            return None
        if cw + self.weights[idx] <= self.capacity:
            self.decisions += 1
            used[idx] = True
            res = self._backtrack(used, idx + 1,
                                  cw + self.weights[idx],
                                  cv + self.values[idx])
            if res is not None:
                return res
            if self.budget_exhausted:
                return None
            used[idx] = False
        self.decisions += 1
        return self._backtrack(used, idx + 1, cw, cv)


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


# ── Main ───────────────────────────────────────────────────────────────────

def run():
    print("=" * 72)
    print("F2 retest on subset-sum and knapsack — moderate regime")
    print("Cycle 20 Odd (loop 7)")
    print("=" * 72)

    all_results = []

    # Subset-sum moderate
    print("\n── subset-sum moderate ──")
    for n in [25, 28, 30]:
        for inst in range(8):
            elements, target = gen_subset_sum_moderate(n, 1700 + inst)
            solver = SubsetSumInstrumented(elements, target,
                                           record_every=20, max_steps=80000)
            t0 = time.perf_counter()
            sol = solver.solve()
            elapsed = time.perf_counter() - t0
            k_vals = [r["k_proxy"] for r in solver.depth_k_values]
            metrics = compute_metrics(k_vals)
            rec = {
                "family": "subset-sum",
                "n": n,
                "instance": inst,
                "solved": sol is not None,
                "decisions": solver.decisions,
                "time_ms": round(elapsed * 1000, 3),
            }
            if metrics:
                rec.update(metrics)
            all_results.append(rec)

        batch = [r for r in all_results if r["family"] == "subset-sum" and r["n"] == n]
        slopes = [r["second_half_slope"] for r in batch if "second_half_slope" in r]
        decs   = [r["decisions"] for r in batch]
        solved = sum(1 for r in batch if r.get("solved"))
        if slopes:
            avg = sum(slopes) / len(slopes)
            verdict = (
                "decreasing (F2)" if avg < -0.0005
                else "increasing" if avg > 0.0005
                else "flat"
            )
            print(f"  n={n}: avg slope = {avg:+.6f} → {verdict}  "
                  f"(solved {solved}/{len(batch)}, dec {sum(decs)/len(decs):.0f})")

    # Knapsack moderate (small n because brute_force_optimum is O(2^n))
    # record_every=2 because moderate knapsack solves quickly
    print("\n── knapsack moderate ──")
    for n in [17, 19, 21]:
        for inst in range(8):
            weights, values, capacity, target = gen_knapsack_moderate(n, 1800 + inst)
            solver = KnapsackInstrumented(weights, values, capacity, target,
                                          record_every=2, max_steps=80000)
            t0 = time.perf_counter()
            sol = solver.solve()
            elapsed = time.perf_counter() - t0
            k_vals = [r["k_proxy"] for r in solver.depth_k_values]
            metrics = compute_metrics(k_vals)
            rec = {
                "family": "knapsack",
                "n": n,
                "instance": inst,
                "solved": sol is not None,
                "decisions": solver.decisions,
                "time_ms": round(elapsed * 1000, 3),
            }
            if metrics:
                rec.update(metrics)
            all_results.append(rec)

        batch = [r for r in all_results if r["family"] == "knapsack" and r["n"] == n]
        slopes = [r["second_half_slope"] for r in batch if "second_half_slope" in r]
        decs   = [r["decisions"] for r in batch]
        solved = sum(1 for r in batch if r.get("solved"))
        if slopes:
            avg = sum(slopes) / len(slopes)
            verdict = (
                "decreasing (F2)" if avg < -0.0005
                else "increasing" if avg > 0.0005
                else "flat"
            )
            print(f"  n={n}: avg slope = {avg:+.6f} → {verdict}  "
                  f"(solved {solved}/{len(batch)}, dec {sum(decs)/len(decs):.0f})")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_f2_retest_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_f2_retest",
            "date": time.strftime("%Y-%m-%d"),
            "purpose": "F2 retest on subset-sum and knapsack with moderate regime",
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
