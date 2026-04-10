#!/usr/bin/env python3
"""
landscape_k_subset_sum.py — Cycle 10 Odd (loop 4, 2026-04-09)

Fourth NP family for the K-trajectory probe: subset-sum.

After loop 3:
    F1 (hard → K flat) confirmed on 3 NP families:
        SAT (clause remnants), Ham cycle (candidate list), 3-coloring
        (forbidden-color histogram).
    F2 (easier → K decreasing) is SAT-specific.

Goal: a 4/4 confirmation pushing F1 universality past the threshold of
"three independent confirmations" toward "candidate axiom."

Subset-sum specifics:
    Input:  a multiset S of integers and a target T.
    NP question: is there a subset of S summing to T?

    The natural "constraint remnant" at a backtracking decision is the
    REACHABLE-SUM SET — given the partial choice, the set of sums
    reachable from the remaining elements that could still hit T.
    A direct encoding of all reachable sums is exponential, so we use
    a HISTOGRAM proxy: bucketize the gap (T - current_sum) modulo each
    remaining element, and gzip the bucket counts.

    Easy instances: many elements with small values → many ways to
    reach T → reachable-sum histogram stays diffuse → flat K-slope.
    Hard instances: few large elements with tight target → few ways
    to reach T → histogram becomes constrained → K-slope ?

    Actually, the directional prediction here is less clear than for
    clausal problems. We will measure both directions and report the
    empirical verdict.

Writes: results/landscape_k_subset_sum_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)


# ── Instance generator ──────────────────────────────────────────────────────

def gen_subset_sum_instance(n, hardness, seed):
    """
    Generate a subset-sum instance guaranteed to be SAT.
    `hardness` ∈ {"easy", "hard"}:
      - easy: small elements (1-100), so backtracking finds a witness fast
      - hard: large elements (10^5..10^6) AND target offset by a small
        adjustment, so the search has to actually navigate the
        exponential space rather than greedily including elements
    """
    rng = random.Random(seed * 6151 + n)
    if hardness == "easy":
        elements = [rng.randint(1, 100) for _ in range(n)]
    else:  # "hard"
        # Large pseudo-random elements at the "hard" subset-sum scale.
        elements = [rng.randint(10**5, 10**6) for _ in range(n)]

    # Pick a hidden subset (about half the elements) to define the target.
    while True:
        mask = [rng.choice([0, 1]) for _ in range(n)]
        if n // 3 <= sum(mask) <= 2 * n // 3:
            break
    target = sum(e for e, m in zip(elements, mask) if m)
    return elements, target


# ── Constraint-remnant proxy ────────────────────────────────────────────────

def reachable_buckets_bytes(elements, used, remaining_target, n_buckets=16):
    """
    Encode a histogram of reachable sums modulo each unused element.
    Specifically: for each unused element e, compute (remaining_target % e)
    and bucketize. The histogram measures how aligned remaining elements
    are with the residual target.

    For easy instances: many elements compatible with the residual,
    histogram is diverse, gzip ratio is high (low compressibility).
    For hard instances: few or repetitive residual matches, gzip ratio
    is lower (high compressibility) — but this depends on instance.

    Output is a fixed-length byte sequence (n_buckets bytes), so gzip
    ratio is stable.
    """
    if remaining_target <= 0:
        return bytes(n_buckets)  # all zeros — search complete
    counts = [0] * n_buckets
    for i, e in enumerate(elements):
        if used[i]:
            continue
        if e > remaining_target:
            continue  # too big to fit
        bucket = (remaining_target % e) % n_buckets
        counts[bucket] = min(counts[bucket] + 1, 255)
    return bytes(counts)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented backtracking ──────────────────────────────────────────────

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
        used = [False] * self.n
        return self._backtrack(used, 0, 0)

    def _backtrack(self, used, idx, current_sum):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None

        if self.step % self.record_every == 0:
            data = reachable_buckets_bytes(
                self.elements, used, self.target - current_sum)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step,
                "depth": idx,
                "remaining_target": self.target - current_sum,
                "k_proxy": round(k, 6),
            })

        if current_sum == self.target:
            return [i for i in range(self.n) if used[i]]
        if idx >= self.n or current_sum > self.target:
            return None

        # Branch 1: include element idx
        self.decisions += 1
        used[idx] = True
        res = self._backtrack(used, idx + 1, current_sum + self.elements[idx])
        if res is not None:
            return res
        if self.budget_exhausted:
            return None
        used[idx] = False

        # Branch 2: skip element idx
        self.decisions += 1
        return self._backtrack(used, idx + 1, current_sum)


# ── Metrics (loop 3 convention) ────────────────────────────────────────────

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


def run_experiment(n, hardness, n_instances=8, seed_base=900,
                   max_steps=80000):
    results = []
    for inst in range(n_instances):
        elements, target = gen_subset_sum_instance(n, hardness,
                                                    seed_base + inst)
        solver = SubsetSumInstrumented(elements, target,
                                       record_every=20,
                                       max_steps=max_steps)
        t0 = time.perf_counter()
        sol = solver.solve()
        elapsed = time.perf_counter() - t0
        k_vals = [r["k_proxy"] for r in solver.depth_k_values]
        metrics = compute_metrics(k_vals)
        record = {
            "instance": inst,
            "n": n,
            "hardness": hardness,
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
            "decreasing (F2)" if avg < -0.0005
            else "increasing" if avg > 0.0005
            else "flat (F1 holds)"
        )
        print(f"  avg 2nd-half slope: {avg:+.6f}  →  {verdict}")


def run():
    print("=" * 72)
    print("Subset-sum K-Trajectory — reachable-bucket histogram proxy")
    print("Cycle 10 Odd (loop 4) — 4th NP family probe")
    print("=" * 72)

    # Two hardness regimes: small elements (easy) vs large elements (hard).
    # Both at the same n so any difference is structural, not size.
    configs = [
        (25, "easy",  "easy-25 (small elements)"),
        (25, "hard",  "hard-25 (large elements)"),
        (30, "easy",  "easy-30 (small elements)"),
        (30, "hard",  "hard-30 (large elements)"),
        (35, "hard",  "hard-35 (large elements)"),
    ]

    all_results = []
    for (n, hardness, label) in configs:
        batch = run_experiment(n, hardness, n_instances=8, seed_base=900,
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
                  f"(solved {solved}/{len(batch)}, avg dec {sum(decs)/len(decs):.0f})")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_subset_sum_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_subset_sum",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "constraint-remnant: reachable-bucket histogram",
            "configs": [{"n": n, "density": d, "label": l}
                        for (n, d, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
