#!/usr/bin/env python3
"""
landscape_k_3dm.py — Cycle 26 Odd (loop 9, 2026-04-09)

Ninth NP family for the K-trajectory probe: 3-dimensional matching.

Problem:
    Given three disjoint sets X, Y, Z of size n and a set T ⊆ X×Y×Z
    of triples, does there exist a perfect matching M ⊆ T such that
    every element of X∪Y∪Z appears in exactly one triple of M?

Hardness lever:
    Random instances at the matching threshold (|T| ≈ 2n log n in
    the typical hardness regime) require search. We generate
    guaranteed-feasible instances by starting from a random perfect
    matching and adding extra triples.

Constraint-remnant histogram proxy:
    For each unmatched element u ∈ X∪Y∪Z, count how many triples in
    T still contain u and have not been excluded (because their other
    members are not yet matched). Bucketize. Encode as fixed-length
    histogram.

If F1 holds → 8/8 testable (clique still untestable). If F2 holds →
7/7 testable.

Writes: results/landscape_k_3dm_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

N_BUCKETS = 16


# ── Instance generator ──────────────────────────────────────────────────────

def gen_3dm_instance(n, extra_factor, seed):
    """
    Generate a guaranteed-feasible 3-DM instance.
    Sets X = {0..n-1}, Y = {n..2n-1}, Z = {2n..3n-1}.
    Build a hidden perfect matching by random pairing, then add
    `extra_factor * n` extra random triples.

    Returns (n, list of triples) where each triple is (x, y, z).
    """
    rng = random.Random(seed * 8101 + n)

    # Hidden perfect matching
    Y_perm = list(range(n, 2 * n))
    Z_perm = list(range(2 * n, 3 * n))
    rng.shuffle(Y_perm)
    rng.shuffle(Z_perm)
    matching = [(i, Y_perm[i], Z_perm[i]) for i in range(n)]

    # Add extra random triples
    triples = list(matching)
    n_extra = int(extra_factor * n)
    seen = set(matching)
    attempts = 0
    while len(triples) < n + n_extra and attempts < 20 * n_extra:
        attempts += 1
        x = rng.randint(0, n - 1)
        y = rng.randint(n, 2 * n - 1)
        z = rng.randint(2 * n, 3 * n - 1)
        t = (x, y, z)
        if t not in seen:
            seen.add(t)
            triples.append(t)
    # SHUFFLE so the embedded matching is not at the front of the list,
    # forcing actual backtracking. Without this, the first triple in each
    # triples_by_x[x] list IS the matching's triple and the search trivially
    # succeeds in exactly n decisions.
    rng.shuffle(triples)
    return n, triples


# ── Constraint-remnant histogram proxy ──────────────────────────────────────

def element_options_bytes(n, triples, matched_x, matched_y, matched_z, used_triples):
    """
    For each STILL-UNMATCHED element u ∈ X∪Y∪Z, count how many triples
    in T still cover u AND have not been used AND have not been
    pruned (i.e. their other elements are not all matched-elsewhere).
    Bucketize all 3n element-options counts to N_BUCKETS bins.
    """
    histogram = [0] * N_BUCKETS

    # X side
    for x in range(n):
        if x in matched_x:
            continue
        opts = sum(
            1 for i, (tx, ty, tz) in enumerate(triples)
            if tx == x and i not in used_triples
            and ty not in matched_y and tz not in matched_z
        )
        bucket = min(opts, N_BUCKETS - 1)
        histogram[bucket] = min(histogram[bucket] + 1, 255)
    # Y side
    for y in range(n, 2 * n):
        if y in matched_y:
            continue
        opts = sum(
            1 for i, (tx, ty, tz) in enumerate(triples)
            if ty == y and i not in used_triples
            and tx not in matched_x and tz not in matched_z
        )
        bucket = min(opts, N_BUCKETS - 1)
        histogram[bucket] = min(histogram[bucket] + 1, 255)
    # Z side
    for z in range(2 * n, 3 * n):
        if z in matched_z:
            continue
        opts = sum(
            1 for i, (tx, ty, tz) in enumerate(triples)
            if tz == z and i not in used_triples
            and tx not in matched_x and ty not in matched_y
        )
        bucket = min(opts, N_BUCKETS - 1)
        histogram[bucket] = min(histogram[bucket] + 1, 255)

    return bytes(histogram)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented backtracking ──────────────────────────────────────────────

class ThreeDMInstrumented:
    """
    Backtracking 3-DM solver. At each step, pick the first unmatched
    X-element and try every unused triple containing it.
    """
    def __init__(self, n, triples, record_every=10, max_steps=80000):
        self.n = n
        self.triples = triples
        self.record_every = record_every
        self.max_steps = max_steps
        self.depth_k_values = []
        self.step = 0
        self.decisions = 0
        self.budget_exhausted = False
        # Index triples by their X member
        self.triples_by_x = [[] for _ in range(n)]
        for i, (tx, ty, tz) in enumerate(triples):
            self.triples_by_x[tx].append(i)

    def solve(self):
        return self._backtrack(set(), set(), set(), set())

    def _backtrack(self, matched_x, matched_y, matched_z, used_triples):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None

        if self.step % self.record_every == 0:
            data = element_options_bytes(
                self.n, self.triples,
                matched_x, matched_y, matched_z, used_triples)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step,
                "matched_count": len(matched_x),
                "k_proxy": round(k, 6),
            })

        if len(matched_x) == self.n:
            return list(used_triples)

        # Pick first unmatched x
        x = next(i for i in range(self.n) if i not in matched_x)

        for ti in self.triples_by_x[x]:
            tx, ty, tz = self.triples[ti]
            if ty in matched_y or tz in matched_z:
                continue
            if ti in used_triples:
                continue
            self.decisions += 1
            res = self._backtrack(
                matched_x | {tx},
                matched_y | {ty},
                matched_z | {tz},
                used_triples | {ti})
            if res is not None:
                return res
            if self.budget_exhausted:
                return None
        return None


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


def run_experiment(n, extra_factor, n_instances=8, seed_base=2500, max_steps=80000):
    results = []
    for inst in range(n_instances):
        nn, triples = gen_3dm_instance(n, extra_factor, seed_base + inst)
        solver = ThreeDMInstrumented(nn, triples,
                                     record_every=10, max_steps=max_steps)
        t0 = time.perf_counter()
        sol = solver.solve()
        elapsed = time.perf_counter() - t0
        k_vals = [r["k_proxy"] for r in solver.depth_k_values]
        metrics = compute_metrics(k_vals)
        record = {
            "instance": inst,
            "n": n,
            "extra_factor": extra_factor,
            "n_triples": len(triples),
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
    print("3-Dimensional Matching K-Trajectory")
    print("Cycle 26 Odd (loop 9) — 9th NP family probe")
    print("=" * 72)

    # Easy: many extra triples (lots of options + propagation)
    # Hard: few extra triples (search must find one matching)
    # extra_factor = ratio of EXTRA triples to n; total triples = n + extra*n
    configs = [
        (15, 8.0, "easy-15"),
        (18, 8.0, "easy-18"),
        (15, 2.0, "hard-15"),
        (18, 2.0, "hard-18"),
        (20, 2.0, "hard-20"),
    ]

    all_results = []
    for (n, extra, label) in configs:
        batch = run_experiment(n, extra, n_instances=8,
                               seed_base=2500, max_steps=80000)
        all_results.extend(batch)
        summarize(batch, label)

    print("\n── Per-config K second-half slope summary ──")
    print(f"{'config':<30} {'avg slope':<15} verdict")
    for (n, extra, label) in configs:
        batch = [r for r in all_results
                 if r["n"] == n and abs(r["extra_factor"] - extra) < 0.01]
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
            print(f"{label:<30} {avg:+.6f}      {verdict}  "
                  f"(solved {solved}/{len(batch)}, dec {sum(decs)/len(decs):.0f})")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_3dm_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_3dm",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "constraint-remnant: element-options histogram",
            "configs": [{"n": n, "extra": e, "label": l}
                        for (n, e, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
