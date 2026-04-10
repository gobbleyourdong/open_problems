#!/usr/bin/env python3
"""
landscape_k_set_cover.py — Cycle 19 Odd (loop 7, 2026-04-09)

Seventh NP family for the K-trajectory probe: set cover decision.

Problem:
    Given universe U, family F of subsets of U, integer k, does there
    exist a sub-family of size ≤ k whose union is U?

Hardness lever:
    k = (greedy upper bound - 1). At k = optimum the search must find
    THE optimal cover. Greedy gives a log-factor approximation, so
    greedy-1 is typically below optimum and forces extensive search.

Constraint-remnant histogram proxy:
    For each uncovered element u ∈ U, count how many sets in the
    family still contain u and have not yet been excluded from the
    cover. Encode as a fixed-length histogram. Easy regime: many
    options per element (diffuse). Hard regime: few options
    constrained by k budget (concentrated).

If F1 holds → 7/7 cross-family universality.

Writes: results/landscape_k_set_cover_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

N_BUCKETS = 16


# ── Instance generator ──────────────────────────────────────────────────────

def gen_set_cover_instance(n_universe, n_sets, density, seed):
    """
    Generate a guaranteed-feasible set cover instance.
    `density` ∈ (0, 1) — fraction of universe each set covers (avg).
    Returns (universe_size, list of sets, sets_covering_universe).
    Each set is a frozenset of element indices.
    """
    rng = random.Random(seed * 8087 + n_universe)
    universe = list(range(n_universe))

    # Generate random sets
    sets = []
    for _ in range(n_sets):
        size = max(1, int(density * n_universe))
        size = max(1, size + rng.randint(-2, 2))
        size = min(size, n_universe)
        s = frozenset(rng.sample(universe, size))
        sets.append(s)

    # Ensure feasibility: for any element NOT covered by the random sets,
    # add a set containing just that element.
    union = set().union(*sets)
    missing = [u for u in universe if u not in union]
    for u in missing:
        sets.append(frozenset({u}))

    return n_universe, sets


def greedy_cover(n_universe, sets):
    """Greedy set cover: pick the set that covers the most still-uncovered."""
    uncovered = set(range(n_universe))
    cover = []
    while uncovered:
        best = max(sets, key=lambda s: len(s & uncovered))
        cover.append(best)
        uncovered -= best
    return cover


# ── Constraint-remnant histogram proxy ──────────────────────────────────────

def element_options_bytes(n_universe, sets, included, excluded, covered_so_far):
    """
    For each STILL-UNCOVERED element u, count how many sets still
    available (not in `included` or `excluded`) contain u. Bucketize
    these counts to N_BUCKETS bins and emit the histogram.
    """
    counts_per_element = []
    for u in range(n_universe):
        if u in covered_so_far:
            continue
        c = 0
        for s_idx, s in enumerate(sets):
            if s_idx in excluded:
                continue
            if u in s:
                c += 1
        counts_per_element.append(c)

    # Bucketize
    histogram = [0] * N_BUCKETS
    for c in counts_per_element:
        bucket = min(c, N_BUCKETS - 1)
        histogram[bucket] = min(histogram[bucket] + 1, 255)
    return bytes(histogram)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented backtracking ──────────────────────────────────────────────

class SetCoverInstrumented:
    def __init__(self, n_universe, sets, k, record_every=15, max_steps=80000):
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
        return self._backtrack(set(), set(), set(), 0)

    def _backtrack(self, included, excluded, covered, depth):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None

        if self.step % self.record_every == 0:
            data = element_options_bytes(
                self.n_universe, self.sets, included, excluded, covered)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step,
                "depth": depth,
                "cover_size": len(included),
                "uncovered": self.n_universe - len(covered),
                "k_proxy": round(k, 6),
            })

        # Goal check
        if len(covered) == self.n_universe:
            return list(included)
        if len(included) >= self.k:
            return None

        # Pick first uncovered element
        first_uncovered = None
        for u in range(self.n_universe):
            if u not in covered:
                first_uncovered = u
                break
        if first_uncovered is None:
            return None

        # Branch: try each set containing this element
        for s_idx, s in enumerate(self.sets):
            if s_idx in included or s_idx in excluded:
                continue
            if first_uncovered not in s:
                continue
            self.decisions += 1
            new_inc = included | {s_idx}
            new_cov = covered | s
            res = self._backtrack(new_inc, excluded, new_cov, depth + 1)
            if res is not None:
                return res
            if self.budget_exhausted:
                return None
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
        "k_mean": round(sum(k_vals) / n, 4),
        "full_slope": round(full_slope, 6),
        "second_half_slope": round(second_half_slope, 6),
        "n_records": n,
    }


def run_experiment(n_universe, n_sets, density, k_offset, n_instances=8,
                   seed_base=1500, max_steps=80000):
    results = []
    for inst in range(n_instances):
        u, sets = gen_set_cover_instance(n_universe, n_sets, density,
                                         seed_base + inst)
        greedy = greedy_cover(u, sets)
        k = max(1, len(greedy) + k_offset)
        solver = SetCoverInstrumented(u, sets, k=k,
                                      record_every=15, max_steps=max_steps)
        t0 = time.perf_counter()
        sol = solver.solve()
        elapsed = time.perf_counter() - t0
        k_vals = [r["k_proxy"] for r in solver.depth_k_values]
        metrics = compute_metrics(k_vals)
        record = {
            "instance": inst,
            "n_universe": n_universe,
            "n_sets": n_sets,
            "density": density,
            "greedy_size": len(greedy),
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
    print("Set Cover K-Trajectory — element-options histogram proxy")
    print("Cycle 19 Odd (loop 7) — 7th NP family probe")
    print("=" * 72)

    # Configurations: vary universe size, sets, density, k_offset
    # Easy: more sets per element (diffuse, k > greedy)
    # Hard: few sets per element, k = greedy - 1 (tight)
    configs = [
        (30, 60, 0.20, +1, "easy-30 (k > greedy)"),
        (30, 60, 0.15, -1, "hard-30 (k = greedy - 1)"),
        (40, 80, 0.15, -1, "hard-40 (k = greedy - 1)"),
        (50, 100, 0.12, -1, "hard-50 (k = greedy - 1)"),
        (40, 100, 0.10, -1, "hard-40-sparse"),
    ]

    all_results = []
    for (u, ns, dens, koff, label) in configs:
        batch = run_experiment(u, ns, dens, koff, n_instances=8,
                               seed_base=1500, max_steps=80000)
        all_results.extend(batch)
        summarize(batch, f"{label}:")

    print("\n── Per-config K second-half slope summary ──")
    print(f"{'config':<25} {'avg slope':<15} verdict")
    for (u, ns, dens, koff, label) in configs:
        batch = [r for r in all_results
                 if r["n_universe"] == u and r["n_sets"] == ns
                 and abs(r["density"] - dens) < 0.001
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
            print(f"{label:<25} {avg:+.6f}      {verdict}  "
                  f"(solved {solved}/{len(batch)}, dec {sum(decs)/len(decs):.0f})")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_set_cover_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_set_cover",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "constraint-remnant: element-options histogram",
            "configs": [{"u": u, "n_sets": ns, "density": dens,
                         "k_offset": koff, "label": l}
                        for (u, ns, dens, koff, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
