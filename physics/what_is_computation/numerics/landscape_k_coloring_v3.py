#!/usr/bin/env python3
"""
landscape_k_coloring_v3.py — Cycle 8 Odd (loop 3, 2026-04-09)

Third 3-coloring K-trajectory proxy, applying the constraint-remnant
diagnosis from loop 2 (C18) and loop 3 (landscape_k_hamiltonian_v2
strong hard-flat result).

Proxy design:
    For each UNASSIGNED node, count the number of DISTINCT colors
    already used by its assigned neighbors ("forbidden colors"). This
    gives a per-node value in {0, 1, 2, 3} that measures how
    constrained that node is.

    Encode the sorted list of forbidden-count values as a byte
    sequence. As search progresses:
      - Easy instances: unit-propagation-like constraint collapse
        produces a heavily-skewed histogram (many 3s = forced moves).
        Highly repetitive → K decreases (analog of SAT unit propagation).
      - Hard instances: histogram stays diffuse (values spread across
        0, 1, 2, 3). Less repetitive → K flat.

This is the Ham-cycle-style constraint-remnant proxy ported to
3-coloring, avoiding the v1 (unresolved edges + gzip overhead) and
v2 (solution state + assignment-progress artifact) pitfalls.

Writes: results/landscape_k_coloring_v3_data.json
"""

import random, time, gzip, json, os, math, sys

sys.setrecursionlimit(100000)


# ── Graph generator ────────────────────────────────────────────────────────

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


# ── Constraint-remnant proxy: forbidden-color histogram bytes ───────────────

def forbidden_count_bytes(coloring, adj):
    """
    For each UNASSIGNED node, count the distinct colors already used
    by its assigned neighbors. Encode the sorted sequence as bytes.
    """
    n = len(coloring)
    counts = []
    for u in range(n):
        if coloring[u] != -1:
            continue
        used = set()
        for v in adj[u]:
            if coloring[v] != -1:
                used.add(coloring[v])
        counts.append(len(used))
    counts.sort()
    return bytes(counts)


def k_proxy(data):
    if len(data) < 10:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented backtracking ──────────────────────────────────────────────

class ColoringInstrumented:
    def __init__(self, n_nodes, edges, k=3, record_every=5, max_steps=40000):
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
            data = forbidden_count_bytes(coloring, self.adj)
            if len(data) >= 10:
                k = k_proxy(data)
                n_assigned = sum(1 for c in coloring if c != -1)
                self.depth_k_values.append({
                    "step": self.step,
                    "depth": node,
                    "n_assigned": n_assigned,
                    "k_proxy": round(k, 6),
                    "encoded_len": len(data),
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
        "k_final":   round(k_vals[-1], 4),
        "k_mean":    round(sum(k_vals) / n, 4),
        "full_slope": round(full_slope, 6),
        "second_half_slope": round(second_half_slope, 6),
        "n_records": n,
    }


def run_experiment(n, density, n_instances=8, seed_base=700, max_steps=40000):
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
    solved = sum(1 for r in batch if r.get("solved"))
    budget = sum(1 for r in batch if r.get("budget_exhausted"))
    decs   = [r["decisions"] for r in batch]
    print(f"\n{label}")
    print(f"  instances:    {len(batch)}  (solved={solved}, budget={budget})")
    print(f"  avg decisions: {sum(decs)/len(decs):.1f}")
    if slopes_h2:
        avg = sum(slopes_h2) / len(slopes_h2)
        verdict = (
            "decreasing (F2 holds)" if avg < -0.0005
            else "increasing" if avg > 0.0005
            else "flat (F1 holds)"
        )
        print(f"  avg 2nd-half slope: {avg:+.6f}  →  {verdict}")


def run():
    print("=" * 72)
    print("3-Coloring K-Trajectory v3 — forbidden-color histogram proxy")
    print("Cycle 8 Odd (loop 3)")
    print("=" * 72)

    # 3-coloring phase transition for random G(n,p) is around c/n ≈ 2.35.
    # We use edge-density (edges per node) directly to match the earlier
    # experiments.
    configs = []
    for n in [40, 60]:
        for density in [1.0, 2.0, 2.3, 3.0]:
            label = f"n={n} density={density}"
            configs.append((n, density, label))

    all_results = []
    for (n, density, label) in configs:
        batch = run_experiment(n, density, n_instances=8, seed_base=700,
                               max_steps=40000)
        all_results.extend(batch)
        summarize(batch, label)

    print("\n── Per-config K second-half slope summary ──")
    print(f"{'n':<5} {'density':<10} {'slope':<15} verdict")
    for (n, density, label) in configs:
        batch = [r for r in all_results if r["n"] == n and abs(r["edge_density"] - density) < 0.01]
        slopes = [r["second_half_slope"] for r in batch if "second_half_slope" in r]
        if slopes:
            avg = sum(slopes) / len(slopes)
            verdict = (
                "decreasing" if avg < -0.0005
                else "increasing" if avg > 0.0005
                else "flat"
            )
            print(f"{n:<5} {density:<10} {avg:+.6f}      {verdict}")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_coloring_v3_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_coloring_v3",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "constraint-remnant: forbidden-color histogram bytes",
            "configs": [{"n": n, "density": d, "label": l}
                        for (n, d, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
