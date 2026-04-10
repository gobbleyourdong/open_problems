#!/usr/bin/env python3
"""
landscape_k_3dm_v2_f1.py — Cycle 43 Odd (loop 15, 2026-04-09)

F1 retest on 3-DM using the loop-14 depth-distribution proxy mechanism.

Loop 9 found 3-DM F1 untestable: backtracking is too efficient,
the search exhausts in 528-29k decisions instead of filling the
80k budget. Loop 14 introduced a NEW F1 mechanism class via the
depth-distribution proxy, which exposed F1 on FVS at n=25 where
the depth distribution saturates.

This loop applies the same template to 3-DM. If the depth
distribution saturates at small n on the embedded matching
search, F1 should be detectable.

If F1 holds → 3-DM moves from F2-only to fully testable, the dual
partition becomes 12+0+0 (every probed family in the both-testable
category) — the strongest possible state.

Writes: results/landscape_k_3dm_v2_f1_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

N_BUCKETS = 16


# ── Generator (same as v1) ─────────────────────────────────────────────────

def gen_3dm_instance(n, extra_factor, seed):
    rng = random.Random(seed * 8101 + n)
    Y_perm = list(range(n, 2 * n))
    Z_perm = list(range(2 * n, 3 * n))
    rng.shuffle(Y_perm)
    rng.shuffle(Z_perm)
    matching = [(i, Y_perm[i], Z_perm[i]) for i in range(n)]

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
    rng.shuffle(triples)
    return n, triples


# ── New proxy: depth-distribution histogram ────────────────────────────────

def depth_histogram_bytes(depth_counts):
    histogram = [min(c, 255) for c in depth_counts[:N_BUCKETS]]
    while len(histogram) < N_BUCKETS:
        histogram.append(0)
    return bytes(histogram)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented backtracking with depth tracking ──────────────────────────

class ThreeDMInstrumentedV2:
    def __init__(self, n, triples, record_every=10, max_steps=80000):
        self.n = n
        self.triples = triples
        self.record_every = record_every
        self.max_steps = max_steps
        self.depth_k_values = []
        self.step = 0
        self.decisions = 0
        self.budget_exhausted = False
        self.depth_counts = [0] * N_BUCKETS
        self.triples_by_x = [[] for _ in range(n)]
        for i, (tx, ty, tz) in enumerate(triples):
            self.triples_by_x[tx].append(i)

    def solve(self):
        return self._backtrack(set(), set(), set(), set(), 0)

    def _backtrack(self, matched_x, matched_y, matched_z, used_triples, depth):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None

        if depth < N_BUCKETS:
            self.depth_counts[depth] += 1

        if self.step % self.record_every == 0:
            data = depth_histogram_bytes(self.depth_counts)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step,
                "matched_count": len(matched_x),
                "depth": depth,
                "k_proxy": round(k, 6),
            })

        if len(matched_x) == self.n:
            return list(used_triples)

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
                used_triples | {ti},
                depth + 1)
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


def run_experiment(n, extra_factor, n_instances=8, seed_base=4300, max_steps=80000):
    results = []
    for inst in range(n_instances):
        nn, triples = gen_3dm_instance(n, extra_factor, seed_base + inst)
        solver = ThreeDMInstrumentedV2(nn, triples,
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
            else "flat (F1 NEW!)"
        )
        print(f"  avg 2nd-half slope: {avg:+.6f}  →  {verdict}")


def run():
    print("=" * 72)
    print("3-DM F1 retest v2 — depth-distribution proxy (loop 15)")
    print("Cycle 43 Odd")
    print("=" * 72)

    # Sweep n looking for the regime where depth-distribution saturates
    configs = [
        (15, 2.0, "n=15 hard"),
        (18, 2.0, "n=18 hard"),
        (20, 2.0, "n=20 hard"),
        (15, 8.0, "n=15 easy"),
        (18, 8.0, "n=18 easy"),
    ]

    all_results = []
    for (n, extra, label) in configs:
        batch = run_experiment(n, extra, n_instances=8,
                               seed_base=4300, max_steps=80000)
        all_results.extend(batch)
        summarize(batch, label)

    print("\n── F1 redesign verdict (3-DM, depth-distribution proxy) ──")
    print(f"{'config':<25} {'avg slope':<15} verdict")
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
                else "flat (F1!)"
            )
            print(f"{label:<25} {avg:+.6f}      {verdict}  "
                  f"(solved {solved}/{len(batch)}, dec {sum(decs)/len(decs):.0f})")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_3dm_v2_f1_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_3dm_v2_f1",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "depth-distribution histogram (loop 15 F1 redesign)",
            "configs": [{"n": n, "extra": e, "label": l}
                        for (n, e, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
