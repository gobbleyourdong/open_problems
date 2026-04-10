#!/usr/bin/env python3
"""
landscape_k_hitting_set.py — Cycle 35 Odd (loop 12, 2026-04-09)

Twelfth NP family for the K-trajectory probe: hitting set decision.

Problem:
    Given a universe U, a family of subsets F ⊆ 2^U, integer k:
    does there exist H ⊆ U with |H| ≤ k such that every set S ∈ F
    has H ∩ S ≠ ∅?

This is the DUAL of set cover (which selects sets to cover all
elements; hitting set selects elements to hit all sets). Both are
NP-complete but structurally distinct.

Hardness lever:
    k = (greedy hitting set size − 1). Greedy hits the most-frequent
    element first; greedy − 1 forces exhaustive enumeration.

Constraint-remnant histogram proxy:
    For each unhit set S, count how many elements of S are still in
    the candidate pool (not yet excluded). Bucketize. Encode as
    fixed-length 16-byte histogram.

Push F1/F2 cross-family count to 12.

Writes: results/landscape_k_hitting_set_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

N_BUCKETS = 16


def gen_hitting_set_instance(n_universe, n_sets, set_size_avg, seed):
    """Generate a guaranteed-feasible hitting set instance."""
    rng = random.Random(seed * 8231 + n_universe)
    universe = list(range(n_universe))
    sets = []
    for _ in range(n_sets):
        size = max(2, set_size_avg + rng.randint(-2, 2))
        size = min(size, n_universe)
        s = frozenset(rng.sample(universe, size))
        sets.append(s)
    return n_universe, sets


def greedy_hit(n_universe, sets):
    """Greedy hitting set upper bound."""
    uncovered = set(range(len(sets)))
    hit = set()
    while uncovered:
        # Pick element that hits the most uncovered sets
        scores = {}
        for u in range(n_universe):
            if u in hit:
                continue
            scores[u] = sum(1 for i in uncovered if u in sets[i])
        if not scores:
            break
        best = max(scores, key=scores.get)
        if scores[best] == 0:
            break
        hit.add(best)
        uncovered = {i for i in uncovered if best not in sets[i]}
    return len(hit)


def set_options_histogram(sets, included, excluded, n_universe):
    """
    For each set NOT YET HIT (i.e., no included element in it), count
    how many elements of the set are still in the candidate pool
    (not in `excluded`). Bucketize.
    """
    histogram = [0] * N_BUCKETS
    for s in sets:
        if any(e in included for e in s):
            continue  # already hit
        opts = sum(1 for e in s if e not in excluded)
        bucket = min(opts, N_BUCKETS - 1)
        histogram[bucket] = min(histogram[bucket] + 1, 255)
    return bytes(histogram)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


class HittingSetInstrumented:
    def __init__(self, n_universe, sets, k, record_every=10, max_steps=80000):
        self.n_universe = n_universe
        self.sets = sets
        self.k = k
        self.record_every = record_every
        self.max_steps = max_steps
        self.depth_k_values = []
        self.step = 0
        self.decisions = 0
        self.budget_exhausted = False

    def solve(self):
        return self._backtrack(set(), set())

    def _backtrack(self, included, excluded):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None

        if self.step % self.record_every == 0:
            data = set_options_histogram(
                self.sets, included, excluded, self.n_universe)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step,
                "included_count": len(included),
                "excluded_count": len(excluded),
                "k_proxy": round(k, 6),
            })

        # Goal check
        all_hit = all(any(e in included for e in s) for s in self.sets)
        if all_hit:
            return list(included)
        if len(included) >= self.k:
            return None

        # Find first unhit set
        first_unhit = None
        for s in self.sets:
            if not any(e in included for e in s):
                first_unhit = s
                break
        if first_unhit is None:
            return None

        # Branch on each element of the first unhit set
        for e in sorted(first_unhit):
            if e in excluded:
                continue
            self.decisions += 1
            res = self._backtrack(included | {e}, excluded)
            if res is not None:
                return res
            if self.budget_exhausted:
                return None
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


def run_experiment(n_universe, n_sets, set_size, k_offset, n_instances=8,
                   seed_base=3500, max_steps=80000):
    results = []
    for inst in range(n_instances):
        u, sets = gen_hitting_set_instance(n_universe, n_sets, set_size,
                                           seed_base + inst)
        greedy = greedy_hit(u, sets)
        k = max(1, greedy + k_offset)
        solver = HittingSetInstrumented(u, sets, k=k,
                                        record_every=10, max_steps=max_steps)
        t0 = time.perf_counter()
        sol = solver.solve()
        elapsed = time.perf_counter() - t0
        k_vals = [r["k_proxy"] for r in solver.depth_k_values]
        metrics = compute_metrics(k_vals)
        record = {
            "instance": inst,
            "n_universe": n_universe,
            "n_sets": n_sets,
            "set_size": set_size,
            "greedy_size": greedy,
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
    print("Hitting Set Decision K-Trajectory")
    print("Cycle 35 Odd (loop 12) — 12th NP family probe")
    print("=" * 72)

    configs = [
        (25, 50, 4, +1, "easy-25 (k > greedy)"),
        (30, 60, 4, -1, "hard-30 (k = greedy - 1)"),
        (35, 70, 4, -1, "hard-35"),
        (40, 80, 4, -1, "hard-40"),
        (35, 100, 5, -1, "hard-35-dense"),
    ]

    all_results = []
    for (u, ns, ss, koff, label) in configs:
        batch = run_experiment(u, ns, ss, koff, n_instances=8,
                               seed_base=3500, max_steps=80000)
        all_results.extend(batch)
        summarize(batch, label)

    print("\n── Per-config K second-half slope summary ──")
    print(f"{'config':<28} {'avg slope':<15} verdict")
    for (u, ns, ss, koff, label) in configs:
        batch = [r for r in all_results
                 if r["n_universe"] == u and r["n_sets"] == ns
                 and (r["k_target"] - r["greedy_size"]) == koff]
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
    out_path = "results/landscape_k_hitting_set_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_hitting_set",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "constraint-remnant: set-options histogram",
            "configs": [{"u": u, "n_sets": ns, "set_size": ss,
                         "k_offset": koff, "label": l}
                        for (u, ns, ss, koff, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
