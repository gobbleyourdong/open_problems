#!/usr/bin/env python3
"""
landscape_k_coloring_v2.py — Cycle 4 Odd (loop 2, 2026-04-09)

Fixes the measurement artifact from landscape_k_coloring.py (Cycle 2 Odd).

Problem diagnosed in `results/landscape_k_coloring_findings.md`:
    The V1 proxy encoded only UNRESOLVED edges. As search progressed, the
    encoded blob shrank below ~50 bytes; gzip header overhead dominated
    and the ratio rose above 1.0, giving a spurious "K increasing" trend
    that was an artifact, not a real K-opacity signal.

Fix (recommended in V1 findings §"What would answer the question"):
    Use a FIXED-SIZE state encoding — one byte per node, sentinel 255
    for unassigned, 0/1/2 for assigned colors. The input length is
    exactly `n_nodes` bytes throughout the entire search, so gzip
    overhead is a constant-per-run bias rather than a time-varying
    artifact.

This lets us ask the actual structural question: does the K-content of
the coloring state behave like SAT's K-content during search? Decreasing
for easy, flat for hard?

Writes:
    results/landscape_k_coloring_v2_data.json
"""

import random, time, gzip, json, os


# ── Graph generator (same as V1) ────────────────────────────────────────────

def gen_coloring_instance(n_nodes, edge_density, seed):
    rng = random.Random(seed * 9973 + n_nodes)
    colors = [rng.randint(0, 2) for _ in range(n_nodes)]
    target_edges = int(edge_density * n_nodes)
    candidate_pairs = [
        (i, j) for i in range(n_nodes) for j in range(i + 1, n_nodes)
        if colors[i] != colors[j]
    ]
    rng.shuffle(candidate_pairs)
    edges = candidate_pairs[:target_edges]
    return edges, colors


# ── Fixed-size state encoding ───────────────────────────────────────────────

SENTINEL_UNASSIGNED = 255

def coloring_state_bytes(coloring):
    """
    Encode the partial coloring as n bytes. Assigned nodes carry 0/1/2,
    unassigned nodes carry SENTINEL_UNASSIGNED (255). Input length stays
    constant at n for the whole search.
    """
    return bytes(SENTINEL_UNASSIGNED if c == -1 else c for c in coloring)


def k_proxy(data):
    """gzip ratio — stable for inputs ≥ ~30 bytes with fixed length."""
    if len(data) == 0:
        return 0.0
    c = gzip.compress(data, compresslevel=9)
    return len(c) / len(data)


# ── Instrumented backtracking ───────────────────────────────────────────────

class ColoringInstrumented:
    def __init__(self, n_nodes, edges, k=3, record_every=3, max_steps=20000):
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
        coloring = [-1] * self.n
        return self._backtrack(coloring, 0)

    def _backtrack(self, coloring, node):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None

        if self.step % self.record_every == 0:
            data = coloring_state_bytes(coloring)
            k = k_proxy(data)
            n_assigned = sum(1 for c in coloring if c != -1)
            self.depth_k_values.append({
                "step": self.step,
                "depth": node,
                "n_assigned": n_assigned,
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


# ── Experiment driver ───────────────────────────────────────────────────────

def run_experiment(n_nodes, edge_density, n_instances=3, seed_base=300,
                   max_steps=50000):
    results = []
    for inst in range(n_instances):
        edges, embedded = gen_coloring_instance(n_nodes, edge_density, seed_base + inst)
        solver = ColoringInstrumented(n_nodes, edges, k=3, record_every=3,
                                      max_steps=max_steps)
        t0 = time.perf_counter()
        sol = solver.solve()
        elapsed = time.perf_counter() - t0

        k_vals = [r["k_proxy"] for r in solver.depth_k_values]
        k_initial = k_vals[0] if k_vals else None
        k_final = k_vals[-1] if k_vals else None
        k_min = min(k_vals) if k_vals else None
        k_max = max(k_vals) if k_vals else None
        k_mean = sum(k_vals) / len(k_vals) if k_vals else None
        # Slope: difference between first and last, normalized by count.
        slope = ((k_vals[-1] - k_vals[0]) / max(len(k_vals) - 1, 1)
                 if len(k_vals) >= 2 else 0.0)
        trend = (
            "decreasing" if len(k_vals) >= 2 and k_vals[-1] < k_vals[0] - 0.01
            else "increasing" if len(k_vals) >= 2 and k_vals[-1] > k_vals[0] + 0.01
            else "flat" if len(k_vals) >= 2
            else "too_short"
        )

        results.append({
            "instance": inst,
            "n_nodes": n_nodes,
            "edge_density": edge_density,
            "n_edges": len(edges),
            "solved": sol is not None,
            "budget_exhausted": solver.budget_exhausted,
            "decisions": solver.decisions,
            "steps": solver.step,
            "time_ms": round(elapsed * 1000, 4),
            "n_k_records": len(k_vals),
            "k_initial": round(k_initial, 4) if k_initial is not None else None,
            "k_final":   round(k_final,   4) if k_final   is not None else None,
            "k_min":     round(k_min,     4) if k_min     is not None else None,
            "k_max":     round(k_max,     4) if k_max     is not None else None,
            "k_mean":    round(k_mean,    4) if k_mean    is not None else None,
            "k_slope":   round(slope, 6),
            "k_trend": trend,
            "k_trajectory_head": solver.depth_k_values[:20],
        })
    return results


def summarize_batch(batch, label):
    n = len(batch)
    if n == 0:
        print(f"{label}: empty")
        return
    kinit = [r["k_initial"] for r in batch if r["k_initial"] is not None]
    kfin  = [r["k_final"]   for r in batch if r["k_final"]   is not None]
    kmean = [r["k_mean"]    for r in batch if r["k_mean"]    is not None]
    kslope= [r["k_slope"]   for r in batch]
    decs  = [r["decisions"] for r in batch]
    print(f"\n{label}")
    print(f"  instances:        {n}")
    if kinit:
        print(f"  K_initial (avg):  {sum(kinit)/len(kinit):.4f}")
        print(f"  K_final   (avg):  {sum(kfin)/len(kfin):.4f}")
        print(f"  K_mean    (avg):  {sum(kmean)/len(kmean):.4f}")
        print(f"  K_slope   (avg):  {sum(kslope)/len(kslope):+.6f}  (per recorded step)")
    print(f"  decisions (avg):  {sum(decs)/len(decs):.1f}")
    print(f"  trend counts:     "
          f"decreasing={sum(1 for r in batch if r['k_trend']=='decreasing')}, "
          f"flat={sum(1 for r in batch if r['k_trend']=='flat')}, "
          f"increasing={sum(1 for r in batch if r['k_trend']=='increasing')}, "
          f"too_short={sum(1 for r in batch if r['k_trend']=='too_short')}")


def run():
    print("=" * 72)
    print("3-Coloring Landscape K-Content v2 — Fixed-Size State Encoding")
    print("Cycle 4 Odd (loop 2)")
    print("=" * 72)

    configs = [
        # Small n so easy instances produce enough K-records to compare.
        (30, 1.5, "easy-30 (density 1.5n)"),
        (30, 2.3, "hard-30 (phase transition ~2.35n)"),
        (50, 1.5, "easy-50 (density 1.5n)"),
        (50, 2.3, "hard-50 (phase transition)"),
    ]

    all_results = []
    for n, density, label in configs:
        batch = run_experiment(n, density, n_instances=3, seed_base=300,
                               max_steps=50000)
        all_results.extend(batch)
        summarize_batch(batch, f"{label}:")

    print("\n── Comparison vs SAT fingerprint ──")
    print("SAT (landscape_k.py):   easy → K decreases,  hard → K flat")
    print("3-coloring v1 (gzip):   BOTH regimes show artifact K-increasing (proxy failure)")
    print("3-coloring v2 (fixed):  ← this run; look for SAT-like fingerprint below")
    print()
    for n, density, label in configs:
        batch = [r for r in all_results if r["n_nodes"] == n and abs(r["edge_density"] - density) < 0.01]
        kslopes = [r["k_slope"] for r in batch]
        if kslopes:
            avg_slope = sum(kslopes) / len(kslopes)
            verdict = (
                "decreasing (easy fingerprint)" if avg_slope < -0.001
                else "increasing (unusual)" if avg_slope > 0.001
                else "flat (hard fingerprint)"
            )
            print(f"  {label:<40} avg k_slope = {avg_slope:+.6f}  →  {verdict}")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_coloring_v2_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_coloring_v2",
            "date": time.strftime("%Y-%m-%d"),
            "encoding": "fixed-size per-node state, sentinel 255 for unassigned",
            "configs": [{"n": c[0], "density": c[1], "desc": c[2]} for c in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
