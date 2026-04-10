#!/usr/bin/env python3
"""
landscape_k_dominating_set.py — Cycle 46 Odd (loop 16, 2026-04-09)

Thirteenth NP family for the K-trajectory probe: dominating set
decision.

Problem:
    Given graph G = (V, E) and integer k, does there exist S ⊆ V
    with |S| ≤ k such that every vertex is either in S or has at
    least one neighbor in S? (S "dominates" V.)

Hardness lever:
    k = (greedy dominating set size − 1). Greedy picks the vertex
    that dominates the most undominated others; greedy − 1 forces
    enumeration.

Constraint-remnant histogram proxy:
    For each undominated vertex u, count how many vertices are still
    in the candidate pool (not excluded) that could dominate u
    (i.e. u itself or its neighbors). Bucketize. The histogram
    shrinks as the search adds vertices to S, the F2 shrinkage
    signal.

Push F1/F2 cross-family count to 13/13.

Writes: results/landscape_k_dominating_set_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

N_BUCKETS = 16


def gen_dominating_set_instance(n, edge_prob, seed):
    rng = random.Random(seed * 6271 + n)
    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < edge_prob:
                adj[i].add(j)
                adj[j].add(i)
    return adj


def closed_neighborhood(adj, v):
    """N[v] = {v} ∪ N(v)."""
    return {v} | adj[v]


def greedy_dominating_set(adj):
    n = len(adj)
    undominated = set(range(n))
    cover = set()
    while undominated:
        # Pick the vertex (in or outside cover) whose closed nbhd
        # covers the most undominated vertices.
        best = max(range(n),
                   key=lambda v: len(closed_neighborhood(adj, v) & undominated))
        cover.add(best)
        undominated -= closed_neighborhood(adj, best)
    return len(cover)


def domination_options_histogram(adj, included, excluded, dominated, n):
    """
    For each undominated vertex u, count how many candidate vertices
    (in [0,n) - excluded) have u in their closed neighborhood.
    Bucketize.
    """
    histogram = [0] * N_BUCKETS
    for u in range(n):
        if u in dominated:
            continue
        opts = 0
        for v in range(n):
            if v in excluded:
                continue
            if v == u or u in adj[v]:
                opts += 1
        bucket = min(opts, N_BUCKETS - 1)
        histogram[bucket] = min(histogram[bucket] + 1, 255)
    return bytes(histogram)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


class DominatingSetInstrumented:
    def __init__(self, adj, k, record_every=10, max_steps=80000):
        self.adj = adj
        self.n = len(adj)
        self.k = k
        self.record_every = record_every
        self.max_steps = max_steps
        self.depth_k_values = []
        self.step = 0
        self.decisions = 0
        self.budget_exhausted = False

    def solve(self):
        return self._backtrack(set(), set(), set())

    def _backtrack(self, included, excluded, dominated):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None

        if self.step % self.record_every == 0:
            data = domination_options_histogram(
                self.adj, included, excluded, dominated, self.n)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step,
                "included_count": len(included),
                "dominated_count": len(dominated),
                "k_proxy": round(k, 6),
            })

        if len(dominated) == self.n:
            return list(included)
        if len(included) >= self.k:
            return None

        # Find first undominated vertex
        first_undom = None
        for u in range(self.n):
            if u not in dominated:
                first_undom = u
                break
        if first_undom is None:
            return None

        # Branch on each candidate that can dominate first_undom
        candidates = [first_undom] + sorted(self.adj[first_undom])
        for v in candidates:
            if v in excluded or v in included:
                continue
            self.decisions += 1
            new_inc = included | {v}
            new_dom = dominated | closed_neighborhood(self.adj, v)
            res = self._backtrack(new_inc, excluded, new_dom)
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


def run_experiment(n, edge_prob, k_offset, n_instances=8,
                   seed_base=4600, max_steps=80000):
    results = []
    for inst in range(n_instances):
        adj = gen_dominating_set_instance(n, edge_prob, seed_base + inst)
        greedy_size = greedy_dominating_set(adj)
        k = max(1, greedy_size + k_offset)
        solver = DominatingSetInstrumented(adj, k=k,
                                           record_every=10, max_steps=max_steps)
        t0 = time.perf_counter()
        sol = solver.solve()
        elapsed = time.perf_counter() - t0
        k_vals = [r["k_proxy"] for r in solver.depth_k_values]
        metrics = compute_metrics(k_vals)
        record = {
            "instance": inst,
            "n": n,
            "edge_prob": edge_prob,
            "greedy_dom": greedy_size,
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
    print("Dominating Set Decision K-Trajectory")
    print("Cycle 46 Odd (loop 16) — 13th NP family probe")
    print("=" * 72)

    configs = [
        (20, 0.3, +1, "easy-20 (k > greedy)"),
        (25, 0.3, -1, "hard-25 (k = greedy - 1)"),
        (30, 0.3, -1, "hard-30"),
        (35, 0.3, -1, "hard-35"),
        (30, 0.4, -1, "hard-30-dense"),
    ]

    all_results = []
    for (n, p, koff, label) in configs:
        batch = run_experiment(n, p, koff, n_instances=8,
                               seed_base=4600, max_steps=80000)
        all_results.extend(batch)
        summarize(batch, label)

    print("\n── Per-config K second-half slope summary ──")
    print(f"{'config':<28} {'avg slope':<15} verdict")
    for (n, p, koff, label) in configs:
        batch = [r for r in all_results
                 if r["n"] == n and abs(r["edge_prob"] - p) < 0.01
                 and (r["k_target"] - r["greedy_dom"]) == koff]
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
    out_path = "results/landscape_k_dominating_set_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_dominating_set",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "constraint-remnant: domination-options histogram",
            "configs": [{"n": n, "p": p, "k_offset": koff, "label": l}
                        for (n, p, koff, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
