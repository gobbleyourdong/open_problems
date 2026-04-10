#!/usr/bin/env python3
"""
landscape_k_knapsack.py — Cycle 13 Odd (loop 5, 2026-04-09)

Fifth NP family for the K-trajectory probe: 0/1 knapsack (decision
version).

Problem:
    Given items (weight_i, value_i), capacity W, target value V:
    is there a subset with total weight ≤ W and total value ≥ V?

Constraint-remnant histogram proxy (HistogramProxy form):
    At each backtracking decision, for the remaining unchosen items,
    bucketize the per-item "fit-feasibility offset":

      offset_i = (W_remaining - weight_i)

    encoded as a value in some normalized range. The histogram counts
    how many items fall into each feasibility bucket. For easy
    instances, items either obviously fit or don't (skewed histogram);
    for hard instances near the capacity threshold, the histogram is
    diffuse.

    16 fixed-length buckets, gzip ratio. Same template as subset-sum.

If F1 holds → 5/5 cross-family universality, the strongest empirical
support yet for the constraint-remnant fingerprint claim.

Writes: results/landscape_k_knapsack_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

N_BUCKETS = 16


# ── Instance generator ──────────────────────────────────────────────────────

def brute_force_optimum(weights, values, capacity):
    """
    O(2^n) brute-force search for the optimal feasible value. Only viable
    for small n (≤ 22). Returns max_value found. Used to ensure the
    target is exactly the optimum so the search must find THE specific
    optimal subset(s) rather than any feasible one.
    """
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


def gen_knapsack_instance(n, hardness, seed):
    """
    Generate a 0/1 knapsack decision instance.

    hardness:
      "easy" — small weights, loose capacity, target = small fraction of optimum
      "hard" — correlated weight=value items, tight capacity, target = OPTIMUM
               (forces the search to find one of the few optimal subsets)
    """
    rng = random.Random(seed * 5471 + n)

    if hardness == "easy":
        weights = [rng.randint(1, 100) for _ in range(n)]
        values  = [rng.randint(1, 100) for _ in range(n)]
        capacity = sum(weights) // 2
        target_value = sum(values) // 8  # easy: any decent subset wins
    else:  # "hard"
        # Correlated knapsack: weight ≈ value (+/- small noise). This is the
        # classic "hard" benchmark family because density (value/weight) is
        # nearly constant, so no greedy heuristic helps.
        weights = []
        values = []
        for _ in range(n):
            w = rng.randint(10**4, 10**5)
            v = w + rng.randint(-1000, 1000)  # small correlated noise
            weights.append(w)
            values.append(max(1, v))
        capacity = sum(weights) // 2
        # Target = the actual optimum value. Forces the search to find
        # an optimal-value subset rather than any feasible one.
        target_value = brute_force_optimum(weights, values, capacity)

    return weights, values, capacity, target_value


# ── Constraint-remnant histogram proxy ──────────────────────────────────────

def feasibility_buckets_bytes(weights, used, capacity_remaining):
    """
    For each unused item, compute (capacity_remaining - weight_i),
    bucketize to N_BUCKETS, and emit the histogram.
    Items that don't fit (weight > capacity_remaining) get bucket 0.
    Items that fit exactly get the highest bucket.
    """
    if capacity_remaining <= 0:
        return bytes(N_BUCKETS)
    counts = [0] * N_BUCKETS
    for i, w in enumerate(weights):
        if used[i]:
            continue
        if w > capacity_remaining:
            counts[0] = min(counts[0] + 1, 255)
            continue
        # Map fit-margin to bucket [0, N_BUCKETS-1]
        margin = capacity_remaining - w
        bucket = min(N_BUCKETS - 1,
                     int((margin / capacity_remaining) * (N_BUCKETS - 1)) + 1)
        counts[bucket] = min(counts[bucket] + 1, 255)
    return bytes(counts)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented backtracking ──────────────────────────────────────────────

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
        used = [False] * self.n
        return self._backtrack(used, 0, 0, 0)

    def _backtrack(self, used, idx, current_weight, current_value):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None

        if self.step % self.record_every == 0:
            data = feasibility_buckets_bytes(
                self.weights, used, self.capacity - current_weight)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step,
                "depth": idx,
                "current_weight": current_weight,
                "current_value": current_value,
                "k_proxy": round(k, 6),
            })

        # Goal check
        if current_value >= self.target_value and current_weight <= self.capacity:
            return [i for i in range(self.n) if used[i]]

        # Bound check
        if idx >= self.n or current_weight > self.capacity:
            return None

        # Branch 1: include item idx (if it fits)
        if current_weight + self.weights[idx] <= self.capacity:
            self.decisions += 1
            used[idx] = True
            res = self._backtrack(used, idx + 1,
                                  current_weight + self.weights[idx],
                                  current_value + self.values[idx])
            if res is not None:
                return res
            if self.budget_exhausted:
                return None
            used[idx] = False

        # Branch 2: skip item idx
        self.decisions += 1
        return self._backtrack(used, idx + 1, current_weight, current_value)


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
        "k_mean": round(sum(k_vals) / n, 4),
        "full_slope": round(full_slope, 6),
        "second_half_slope": round(second_half_slope, 6),
        "n_records": n,
    }


def run_experiment(n, hardness, n_instances=8, seed_base=1100,
                   max_steps=80000):
    results = []
    for inst in range(n_instances):
        weights, values, capacity, target = gen_knapsack_instance(
            n, hardness, seed_base + inst)
        solver = KnapsackInstrumented(weights, values, capacity, target,
                                      record_every=20, max_steps=max_steps)
        t0 = time.perf_counter()
        sol = solver.solve()
        elapsed = time.perf_counter() - t0
        k_vals = [r["k_proxy"] for r in solver.depth_k_values]
        metrics = compute_metrics(k_vals)
        record = {
            "instance": inst,
            "n": n,
            "hardness": hardness,
            "capacity": capacity,
            "target_value": target,
            "max_weight": max(weights),
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
    print("Knapsack K-Trajectory — feasibility-bucket histogram proxy")
    print("Cycle 13 Odd (loop 5) — 5th NP family probe")
    print("=" * 72)

    # Constrained to n ≤ 22 because brute_force_optimum is O(2^n).
    # 2^22 ≈ 4M iterations per instance × 8 instances per config is fine.
    configs = [
        (18, "easy",  "easy-18"),
        (18, "hard",  "hard-18"),
        (20, "easy",  "easy-20"),
        (20, "hard",  "hard-20"),
        (22, "hard",  "hard-22"),
    ]

    all_results = []
    for (n, hardness, label) in configs:
        batch = run_experiment(n, hardness, n_instances=8, seed_base=1100,
                               max_steps=80000)
        all_results.extend(batch)
        summarize(batch, f"{label} (n={n}):")

    print("\n── Per-config K second-half slope summary ──")
    print(f"{'n':<5} {'hardness':<10} {'avg slope':<15} verdict")
    for (n, hardness, label) in configs:
        batch = [r for r in all_results
                 if r["n"] == n and r.get("hardness") == hardness]
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
            print(f"{n:<5} {hardness:<10} {avg:+.6f}      {verdict}  "
                  f"(solved {solved}/{len(batch)}, dec {sum(decs)/len(decs):.0f})")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_knapsack_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_knapsack",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "constraint-remnant: feasibility-bucket histogram",
            "configs": [{"n": n, "hardness": h, "label": l}
                        for (n, h, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
