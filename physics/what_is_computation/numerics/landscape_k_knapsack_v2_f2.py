#!/usr/bin/env python3
"""
landscape_k_knapsack_v2_f2.py — Cycle 37 Odd (loop 13, 2026-04-09)

F2 redesign attempt on knapsack (mirror of loop-12 subset-sum success).

Loop 5 confirmed F1 cleanly on knapsack via the feasibility-bucket
proxy. Loop 7 Cycle 20 Odd attempted F2 but found a difficulty
cliff: easy regimes finish in ~10 decisions, hard regimes fill the
budget at flat slopes.

Loop 12 demonstrated the same cliff pattern on subset-sum can be
escaped via a redesigned proxy. The lesson: instead of measuring
the constraint frontier directly, measure a DENSITY of how many
remaining items "fit" into the residual capacity, encoded as a
fixed-length 16-bucket histogram of weight-to-residual ratios.

This loop applies the template to knapsack:
    For each unused item, classify by ratio `weight_i / capacity_remaining`.
    Bucketize. The histogram shifts toward bucket-0 ("no-fit") as
    capacity tightens — the F2 shrinkage signal.

Generator: medium-difficulty correlated knapsack with target = 80%
of brute-force optimum. Loose enough that several near-optimal
subsets exist, but tight enough to require backtracking.

Writes: results/landscape_k_knapsack_v2_f2_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

N_BUCKETS = 16


def brute_force_optimum(weights, values, capacity):
    """O(2^n) brute force — viable for n ≤ 22."""
    n = len(weights)
    best = 0
    for mask in range(1 << n):
        w = v = 0
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


def gen_knapsack_medium(n, seed):
    """
    Medium-difficulty knapsack: UNCORRELATED items (weight, value
    independent), capacity = sum/2, target = 95% of brute-force
    optimum. Uncorrelated + tight target + permuted order forces
    real backtracking even on easy regimes.
    """
    rng = random.Random(seed * 5471 + n)
    weights = []
    values = []
    for _ in range(n):
        w = rng.randint(10**3, 10**4)
        v = rng.randint(10**3, 10**4)  # independent of w
        weights.append(w)
        values.append(v)
    # Permute item order so the optimum subset isn't at the front
    perm = list(range(n))
    rng.shuffle(perm)
    weights = [weights[i] for i in perm]
    values = [values[i] for i in perm]
    capacity = sum(weights) // 2
    optimum = brute_force_optimum(weights, values, capacity)
    target = max(1, int(optimum * 0.95))
    return weights, values, capacity, target


# ── Density proxy: weight-to-residual ratio histogram ──────────────────────

def weight_residual_density_bytes(weights, used, capacity_remaining):
    """
    For each unused item, classify by `weight / capacity_remaining`
    ratio:
      - Bucket 0: weight > capacity_remaining (no-fit)
      - Buckets 1..15: bucketized fit-ratio in [0, 1)
    Encode the 16-byte histogram.

    For easy instances: many items fit loosely → histogram is
    spread across upper buckets → high diversity → high gzip ratio.
    As capacity tightens via accepted items, more shift to no-fit
    bucket → histogram becomes skewed → gzip ratio drops.
    """
    histogram = [0] * N_BUCKETS
    if capacity_remaining <= 0:
        return bytes(N_BUCKETS)
    for i, w in enumerate(weights):
        if used[i]:
            continue
        if w > capacity_remaining:
            histogram[0] = min(histogram[0] + 1, 255)
            continue
        ratio = w / capacity_remaining
        bucket = min(N_BUCKETS - 1, int(ratio * (N_BUCKETS - 1)) + 1)
        histogram[bucket] = min(histogram[bucket] + 1, 255)
    return bytes(histogram)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented backtracking ──────────────────────────────────────────────

class KnapsackInstrumentedV2:
    def __init__(self, weights, values, capacity, target_value,
                 record_every=10, max_steps=80000):
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
            data = weight_residual_density_bytes(
                self.weights, used, self.capacity - cw)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step,
                "depth": idx,
                "current_weight": cw,
                "current_value": cv,
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


def run_experiment(n, n_instances=8, seed_base=3700, max_steps=80000):
    results = []
    for inst in range(n_instances):
        weights, values, capacity, target = gen_knapsack_medium(n, seed_base + inst)
        solver = KnapsackInstrumentedV2(weights, values, capacity, target,
                                        record_every=10, max_steps=max_steps)
        t0 = time.perf_counter()
        sol = solver.solve()
        elapsed = time.perf_counter() - t0
        k_vals = [r["k_proxy"] for r in solver.depth_k_values]
        metrics = compute_metrics(k_vals)
        record = {
            "instance": inst,
            "n": n,
            "capacity": capacity,
            "target_value": target,
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
    print("Knapsack F2 retest v2 — weight-residual density proxy")
    print("Cycle 37 Odd (loop 13)")
    print("=" * 72)

    # n ≤ 22 because brute_force_optimum is O(2^n)
    configs = [
        (15, "n=15 medium"),
        (17, "n=17 medium"),
        (19, "n=19 medium"),
        (21, "n=21 medium"),
    ]

    all_results = []
    for (n, label) in configs:
        batch = run_experiment(n, n_instances=8, seed_base=3700, max_steps=80000)
        all_results.extend(batch)
        summarize(batch, label)

    print("\n── F2 redesign verdict (knapsack, density proxy) ──")
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
    out_path = "results/landscape_k_knapsack_v2_f2_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_knapsack_v2_f2",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "weight-residual density histogram (loop 13 F2 redesign)",
            "configs": [{"n": n, "label": l} for (n, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
