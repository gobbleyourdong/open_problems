#!/usr/bin/env python3
"""
landscape_k_fvs.py — Cycle 29 Odd (loop 10, 2026-04-09)

Tenth NP family for the K-trajectory probe: feedback vertex set
decision.

Problem:
    Given graph G = (V, E) and integer k, does there exist S ⊆ V
    with |S| ≤ k such that G − S is acyclic (a forest)?

Hardness lever:
    k = (greedy upper bound − 1). At k below the minimum FVS, search
    must enumerate. For random dense graphs, the minimum FVS is large,
    so k = greedy − 1 is typically tight.

Constraint-remnant histogram proxy:
    For each STILL-PRESENT vertex (not yet removed from the candidate
    set), count how many cycles in the current graph still pass
    through it (its "cycle-load"). Bucketize. Encode as fixed-length
    histogram.

    Easy proxy: cycle counts can be exponential, so we approximate
    via "vertex-degree-in-cycle-subgraph" — counting only vertices
    whose degree is ≥ 2 in the current induced subgraph (vertices
    with degree < 2 are not in any cycle by definition).

If F1 holds → 8/9 testable (or 9/10 probed). If F2 holds → 8/8
testable.

Writes: results/landscape_k_fvs_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

N_BUCKETS = 16


# ── Instance generator ──────────────────────────────────────────────────────

def gen_fvs_instance(n, edge_prob, seed):
    """Random graph G(n, p)."""
    rng = random.Random(seed * 6263 + n)
    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < edge_prob:
                adj[i].add(j)
                adj[j].add(i)
    return adj


def has_cycle(adj_dict):
    """DFS-based cycle detection on the current graph."""
    visited = set()
    def dfs(u, parent):
        visited.add(u)
        for v in adj_dict.get(u, set()):
            if v not in visited:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False
    for u in adj_dict:
        if u not in visited:
            if dfs(u, -1):
                return True
    return False


def induced_subgraph(adj, removed):
    """Return adjacency dict of G − removed."""
    sub = {}
    for u in range(len(adj)):
        if u in removed:
            continue
        sub[u] = adj[u] - removed
    return sub


def greedy_fvs(adj):
    """
    Greedy FVS upper bound: iteratively remove the highest-degree
    vertex from the current graph until acyclic.
    """
    n = len(adj)
    removed = set()
    sub = induced_subgraph(adj, removed)
    while has_cycle(sub):
        # Pick highest-degree vertex
        best = max(sub.keys(), key=lambda u: len(sub[u]))
        removed.add(best)
        sub = induced_subgraph(adj, removed)
    return len(removed)


# ── Constraint-remnant histogram proxy ──────────────────────────────────────

def vertex_load_histogram(adj, removed, n):
    """
    For each non-removed vertex, count its degree in the induced
    subgraph (G − removed). Bucketize to N_BUCKETS bins. Vertices with
    degree < 2 cannot be in any cycle of the current graph; vertices
    with high degree are heavily involved in cycle structure.
    """
    histogram = [0] * N_BUCKETS
    for u in range(n):
        if u in removed:
            continue
        deg = sum(1 for v in adj[u] if v not in removed)
        bucket = min(deg, N_BUCKETS - 1)
        histogram[bucket] = min(histogram[bucket] + 1, 255)
    return bytes(histogram)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented FVS backtracking ──────────────────────────────────────────

class FVSInstrumented:
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
        return self._backtrack(set())

    def _backtrack(self, removed):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None

        if self.step % self.record_every == 0:
            data = vertex_load_histogram(self.adj, removed, self.n)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step,
                "removed": len(removed),
                "k_proxy": round(k, 6),
            })

        sub = induced_subgraph(self.adj, removed)
        if not has_cycle(sub):
            return list(removed)
        if len(removed) >= self.k:
            return None

        # Find a cycle and branch on its vertices.
        # Simpler: pick the highest-degree vertex in the current subgraph.
        if not sub:
            return None
        best = max(sub.keys(), key=lambda u: len(sub[u]))

        # Branch 1: include best in removed set
        self.decisions += 1
        res = self._backtrack(removed | {best})
        if res is not None:
            return res
        if self.budget_exhausted:
            return None

        # Branch 2: try other high-degree vertices in turn
        # (this gives the search more options without being exhaustive)
        sorted_vertices = sorted(
            sub.keys(), key=lambda u: -len(sub[u])
        )
        for v in sorted_vertices[1:3]:  # try 2 more options
            self.decisions += 1
            res = self._backtrack(removed | {v})
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
        "full_slope": round(full_slope, 6),
        "second_half_slope": round(second_half_slope, 6),
        "n_records": n,
    }


def run_experiment(n, edge_prob, k_offset, n_instances=8,
                   seed_base=2900, max_steps=80000):
    results = []
    for inst in range(n_instances):
        adj = gen_fvs_instance(n, edge_prob, seed_base + inst)
        greedy_size = greedy_fvs(adj)
        k = max(1, greedy_size + k_offset)
        solver = FVSInstrumented(adj, k=k,
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
            "greedy_fvs": greedy_size,
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
    print("Feedback Vertex Set K-Trajectory")
    print("Cycle 29 Odd (loop 10) — 10th NP family probe")
    print("=" * 72)

    configs = [
        (20, 0.4, +1, "easy-20 (k > greedy)"),
        (25, 0.5, -1, "hard-25 (k = greedy - 1)"),
        (30, 0.5, -1, "hard-30 (k = greedy - 1)"),
        (35, 0.5, -1, "hard-35 (k = greedy - 1)"),
        (30, 0.6, -1, "hard-30-dense"),
    ]

    all_results = []
    for (n, p, koff, label) in configs:
        batch = run_experiment(n, p, koff, n_instances=8,
                               seed_base=2900, max_steps=80000)
        all_results.extend(batch)
        summarize(batch, label)

    print("\n── Per-config K second-half slope summary ──")
    print(f"{'config':<28} {'avg slope':<15} verdict")
    for (n, p, koff, label) in configs:
        batch = [r for r in all_results
                 if r["n"] == n and abs(r["edge_prob"] - p) < 0.01
                 and (r["k_target"] - r["greedy_fvs"]) == koff]
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
    out_path = "results/landscape_k_fvs_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_fvs",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "constraint-remnant: vertex-degree histogram",
            "configs": [{"n": n, "p": p, "k_offset": koff, "label": l}
                        for (n, p, koff, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
