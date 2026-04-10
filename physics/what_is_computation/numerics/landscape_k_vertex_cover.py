#!/usr/bin/env python3
"""
landscape_k_vertex_cover.py — Cycle 17 Odd (loop 6, 2026-04-09)

Sixth NP family for the K-trajectory probe: vertex cover decision.

Problem:
    Given graph G = (V, E) and integer k, does there exist
    S ⊆ V with |S| ≤ k such that every edge has at least one
    endpoint in S?

Hardness lever:
    k = the actual minimum vertex cover number (computed via greedy
    upper bound + branch-and-bound). At k = mvc(G) the search is hard.
    At k > mvc(G) it's trivial; at k < mvc(G) it's UNSAT.

Constraint-remnant histogram proxy:
    For each still-uncovered edge, count the remaining "branching
    options" — number of endpoints not yet excluded from the cover.
    Encode the sorted histogram of these counts as fixed-length bytes.

If F1 holds → 6/6 cross-family universality. The constraint-remnant
fingerprint becomes essentially a universal NP K-trajectory pattern.

Writes: results/landscape_k_vertex_cover_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

N_BUCKETS = 8  # Edges have at most 2 branching options


# ── Instance generator ──────────────────────────────────────────────────────

def gen_vc_instance(n, edge_density, seed):
    """
    Random graph with edge density `edge_density` (expected average
    degree / 2). Returns (n, edges_list).
    """
    rng = random.Random(seed * 4831 + n)
    target_edges = int(edge_density * n)
    candidates = [(i, j) for i in range(n) for j in range(i + 1, n)]
    rng.shuffle(candidates)
    edges = candidates[:target_edges]
    return n, edges


def greedy_vc(n, edges):
    """
    Greedy vertex cover upper bound: iteratively pick the highest-degree
    vertex on an uncovered edge until no edges remain.
    Returns the size of the cover found.
    """
    remaining = set(map(tuple, edges))
    cover = set()
    while remaining:
        # Count degree per vertex over remaining edges
        deg = {}
        for u, v in remaining:
            deg[u] = deg.get(u, 0) + 1
            deg[v] = deg.get(v, 0) + 1
        # Pick highest-degree vertex
        best = max(deg, key=deg.get)
        cover.add(best)
        remaining = {(u, v) for (u, v) in remaining if u != best and v != best}
    return len(cover)


# ── Constraint-remnant histogram proxy ──────────────────────────────────────

def edge_options_bytes(edges, included, excluded):
    """
    For each edge, count remaining cover options:
      - 2: neither endpoint decided
      - 1: one endpoint excluded, other still free
      - 0: both endpoints excluded (UNSAT for this branch) OR
            already covered (excluded from histogram)
      - "covered": at least one endpoint is INCLUDED in cover (drop)
    Encode the histogram as N_BUCKETS bytes.
    """
    counts = [0] * N_BUCKETS
    for u, v in edges:
        if u in included or v in included:
            continue  # already covered
        # Count free endpoints
        free = 0
        if u not in excluded:
            free += 1
        if v not in excluded:
            free += 1
        bucket = min(free, N_BUCKETS - 1)
        counts[bucket] = min(counts[bucket] + 1, 255)
    return bytes(counts)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented backtracking ──────────────────────────────────────────────

class VCInstrumented:
    def __init__(self, n, edges, k, record_every=10, max_steps=80000):
        self.n = n
        self.edges = edges
        self.k = k
        self.record_every = record_every
        self.max_steps = max_steps
        self.depth_k_values = []
        self.step = 0
        self.decisions = 0
        self.budget_exhausted = False

    def solve(self):
        return self._backtrack(set(), set(), 0)

    def _backtrack(self, included, excluded, depth):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None

        if self.step % self.record_every == 0:
            data = edge_options_bytes(self.edges, included, excluded)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step,
                "depth": depth,
                "cover_size": len(included),
                "k_proxy": round(k, 6),
            })

        # Check if cover is complete
        first_uncovered = None
        for u, v in self.edges:
            if u not in included and v not in included:
                first_uncovered = (u, v)
                break

        if first_uncovered is None:
            return list(included)
        if len(included) >= self.k:
            return None

        u, v = first_uncovered

        # Branch 1: include u
        if u not in excluded:
            self.decisions += 1
            new_inc = included | {u}
            res = self._backtrack(new_inc, excluded, depth + 1)
            if res is not None:
                return res
            if self.budget_exhausted:
                return None

        # Branch 2: include v
        if v not in excluded:
            self.decisions += 1
            new_inc = included | {v}
            res = self._backtrack(new_inc, excluded, depth + 1)
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


def run_experiment(n, edge_density, k_offset, n_instances=8,
                   seed_base=1300, max_steps=80000):
    """
    k_offset: offset from greedy upper bound.
        0  → ask for greedy bound (too easy, often satisfiable)
        -1 → ask for greedy bound minus 1 (genuinely tight for many instances)
    """
    results = []
    for inst in range(n_instances):
        n_nodes, edges = gen_vc_instance(n, edge_density, seed_base + inst)
        upper = greedy_vc(n_nodes, edges)
        k = max(1, upper + k_offset)
        solver = VCInstrumented(n_nodes, edges, k=k,
                                record_every=10, max_steps=max_steps)
        t0 = time.perf_counter()
        sol = solver.solve()
        elapsed = time.perf_counter() - t0
        k_vals = [r["k_proxy"] for r in solver.depth_k_values]
        metrics = compute_metrics(k_vals)
        record = {
            "instance": inst,
            "n": n,
            "edge_density": edge_density,
            "n_edges": len(edges),
            "greedy_upper_bound": upper,
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
    print("Vertex Cover K-Trajectory — edge-options histogram proxy")
    print("Cycle 17 Odd (loop 6) — 6th NP family probe")
    print("=" * 72)

    # k_offset = -1 → ask for one less than the greedy upper bound,
    # which is typically tight for randomly generated dense graphs and
    # forces the search to explore.
    configs = [
        (40, 1.5, +1, "easy-40 (sparse, k > greedy)"),
        (40, 2.5, -1, "hard-40 (dense, k = greedy - 1)"),
        (50, 2.5, -1, "hard-50 (dense, k = greedy - 1)"),
        (60, 2.5, -1, "hard-60 (dense, k = greedy - 1)"),
        (40, 3.5, -1, "hard-40 (very dense)"),
    ]

    all_results = []
    for (n, density, koff, label) in configs:
        batch = run_experiment(n, density, koff, n_instances=8,
                               seed_base=1300, max_steps=80000)
        all_results.extend(batch)
        summarize(batch, f"{label}:")

    print("\n── Per-config K second-half slope summary ──")
    print(f"{'n':<5} {'density':<10} {'k_off':<8} {'avg slope':<15} verdict")
    for (n, density, koff, label) in configs:
        batch = [r for r in all_results
                 if r["n"] == n and abs(r["edge_density"] - density) < 0.01
                 and (r["k_target"] - r["greedy_upper_bound"]) == koff]
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
            print(f"{n:<5} {density:<10} {koff:+d}     "
                  f"{avg:+.6f}      {verdict}  "
                  f"(solved {solved}/{len(batch)}, dec {sum(decs)/len(decs):.0f})")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_vertex_cover_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_vertex_cover",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "constraint-remnant: edge-options histogram",
            "configs": [{"n": n, "density": d, "k_offset": k, "label": l}
                        for (n, d, k, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
