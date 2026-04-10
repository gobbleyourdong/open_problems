#!/usr/bin/env python3
"""
landscape_k_coloring_v4_f2.py — Cycle 25 Odd (loop 9, 2026-04-09)

F2 redesign attempt on 3-coloring.

Loop 6 (v3 forbidden-color histogram) confirmed F1 on 3-coloring at
n=60 hard configs but found F2 fails — easy regimes showed positive
slopes (completion artifact).

Loop 8 (Ham cycle v3 unvisited-degree histogram) demonstrated that
the F1/F2 verdict is proxy-design-sensitive: a different proxy that
captures **constraint-frontier shrinkage as a histogram-of-integers**
can flip a FailsOn verdict to HoldsOn.

This loop's hypothesis for 3-coloring: a proxy that tracks
**available-color-count per unassigned node**, but encoded as a
HISTOGRAM (counting how many unassigned nodes have each
available-color count) will produce shrinkage in easy instances.

For an easy 3-coloring instance:
  - Initially, most unassigned nodes have all 3 colors available.
    Histogram: many counts of "3", few counts of "0/1/2".
  - As nodes get assigned, many neighbors lose one available color.
    Histogram: shifts toward "0/1/2" counts.
  - Eventually, most unassigned nodes have 0 or 1 colors available
    (forced moves), histogram becomes very repetitive (long runs of
    the same value), and gzip ratio drops.

  → DECREASING K-proxy = F2 holds.

For a hard 3-coloring instance at the phase transition:
  - The available-count distribution stays diffuse throughout.
  - Histogram doesn't compress well, K stays flat.
  - → F1 holds, F2 fails.

Writes: results/landscape_k_coloring_v4_f2_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

N_BUCKETS = 16  # match Ham cycle v3 fixed-length design


# ── Generator (same as v1/v2/v3) ───────────────────────────────────────────

def gen_coloring_instance(n_nodes, edge_density, seed):
    rng = random.Random(seed * 9973 + n_nodes)
    colors = [rng.randint(0, 2) for _ in range(n_nodes)]
    target_edges = int(edge_density * n_nodes)
    candidates = [
        (i, j) for i in range(n_nodes) for j in range(i + 1, n_nodes)
        if colors[i] != colors[j]
    ]
    rng.shuffle(candidates)
    return candidates[:target_edges], colors


# ── New proxy: available-color count histogram ─────────────────────────────

def unassigned_neighbor_degree_histogram(coloring, adj, n):
    """
    3-coloring analog of Ham cycle v3 unvisited-degree histogram.
    For each unassigned node u, count its UNASSIGNED neighbors
    (i.e. neighbors v with coloring[v] = -1). Bucketize to N_BUCKETS
    fixed bins. Output is always 16 bytes regardless of search state.

    For easy 3-coloring instances at low density: as nodes get
    assigned, the unassigned-neighbor degree histogram shifts toward
    lower buckets → distribution becomes skewed → high compressibility
    → K-proxy decreases.

    For hard instances at the phase transition: the histogram stays
    roughly Poisson-distributed around the average degree → diverse
    → low compressibility → K-proxy flat.
    """
    histogram = [0] * N_BUCKETS
    for u in range(n):
        if coloring[u] != -1:
            continue
        deg = sum(1 for v in adj[u] if coloring[v] == -1)
        bucket = min(deg, N_BUCKETS - 1)
        histogram[bucket] = min(histogram[bucket] + 1, 255)
    return bytes(histogram)


# Keep the function name expected by ColoringInstrumented
available_color_histogram_bytes = unassigned_neighbor_degree_histogram


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented backtracking ──────────────────────────────────────────────

class ColoringInstrumented:
    def __init__(self, n_nodes, edges, k=3, record_every=5, max_steps=80000):
        self.n = n_nodes
        self.edges = edges
        self.k = k
        self.record_every = record_every
        self.max_steps = max_steps
        self.depth_k_values = []
        self.step = 0
        self.decisions = 0
        self.budget_exhausted = False
        self.adj = [set() for _ in range(n_nodes)]
        for u, v in edges:
            self.adj[u].add(v)
            self.adj[v].add(u)

    def solve(self):
        return self._backtrack([-1] * self.n, 0)

    def _backtrack(self, coloring, node):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None

        if self.step % self.record_every == 0:
            data = available_color_histogram_bytes(coloring, self.adj, self.n)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step,
                "depth": node,
                "k_proxy": round(k, 6),
            })

        if node == self.n:
            return list(coloring)

        neighbor_colors = {coloring[nb] for nb in self.adj[node] if coloring[nb] != -1}
        for c in range(self.k):
            if c not in neighbor_colors:
                coloring[node] = c
                self.decisions += 1
                res = self._backtrack(coloring, node + 1)
                if res is not None:
                    return res
                if self.budget_exhausted:
                    return None
                coloring[node] = -1
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


def run_experiment(n, density, n_instances=8, seed_base=2300, max_steps=80000):
    results = []
    for inst in range(n_instances):
        edges, _ = gen_coloring_instance(n, density, seed_base + inst)
        solver = ColoringInstrumented(n, edges, k=3, record_every=5,
                                      max_steps=max_steps)
        t0 = time.perf_counter()
        sol = solver.solve()
        elapsed = time.perf_counter() - t0
        k_vals = [r["k_proxy"] for r in solver.depth_k_values]
        metrics = compute_metrics(k_vals)
        record = {
            "instance": inst,
            "n": n,
            "edge_density": density,
            "n_edges": len(edges),
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
    print("3-Coloring K-Trajectory v4 — F2 redesign attempt")
    print("Cycle 25 Odd (loop 9) — available-color histogram proxy")
    print("=" * 72)

    # Test both easy (low density) and hard (phase transition ~2.35)
    configs = [
        (40, 1.0, "easy-40"),
        (40, 1.5, "easy-mid-40"),
        (60, 1.0, "easy-60"),
        (60, 1.5, "easy-mid-60"),
        (60, 2.3, "hard-60"),
        (80, 2.3, "hard-80"),
    ]

    all_results = []
    for (n, density, label) in configs:
        batch = run_experiment(n, density, n_instances=8,
                               seed_base=2300, max_steps=80000)
        all_results.extend(batch)
        summarize(batch, label)

    print("\n── F2 redesign verdict (3-coloring, available-color proxy) ──")
    print(f"{'config':<20} {'avg slope':<15} verdict")
    for (n, density, label) in configs:
        batch = [r for r in all_results
                 if r["n"] == n and abs(r["edge_density"] - density) < 0.01]
        slopes = [r["second_half_slope"] for r in batch if "second_half_slope" in r]
        if slopes:
            avg = sum(slopes) / len(slopes)
            verdict = (
                "decreasing (F2!)" if avg < -0.0005
                else "increasing" if avg > 0.0005
                else "flat (F1)"
            )
            print(f"{label:<20} {avg:+.6f}      {verdict}")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_coloring_v4_f2_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_coloring_v4_f2",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "available-color count histogram (loop 9 F2 redesign)",
            "configs": [{"n": n, "density": d, "label": l}
                        for (n, d, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
