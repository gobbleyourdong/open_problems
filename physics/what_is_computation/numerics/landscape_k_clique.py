#!/usr/bin/env python3
"""
landscape_k_clique.py — Cycle 22 Odd (loop 8, 2026-04-09)

Eighth NP family for the K-trajectory probe: clique decision.

Problem:
    Given graph G = (V, E) and integer k, does G contain a clique of
    size k? (A clique = subset of vertices with every pair connected.)

Hardness lever:
    k near the maximum clique size ω(G). For random graphs G(n, p),
    ω(G) ≈ 2 log_{1/p}(n). Asking k = ω + 1 is UNSAT (and forces full
    enumeration); asking k = ω is hard SAT.

Constraint-remnant histogram proxy:
    During branch-and-bound clique extension, for each vertex still
    in the candidate set, count how many other candidates it is
    adjacent to (its "co-degree"). Encode the histogram of these
    co-degrees as fixed-length bytes. This measures how K-flat the
    candidate frontier is — high co-degrees = many extension options.

If F1 holds → 8/8 cross-family universality.

Writes: results/landscape_k_clique_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

N_BUCKETS = 16


# ── Instance generator ──────────────────────────────────────────────────────

def gen_clique_instance(n, edge_prob, seed):
    """
    Random graph G(n, p). For p large enough we get cliques of size
    around 2 log_{1/p}(n). Returns adjacency as list of sets.
    """
    rng = random.Random(seed * 9941 + n)
    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < edge_prob:
                adj[i].add(j)
                adj[j].add(i)
    return adj


def greedy_clique(adj):
    """
    Greedy max clique upper bound: repeatedly add the highest-degree
    vertex that's adjacent to all currently-included vertices.
    Returns the size of the clique found.
    """
    n = len(adj)
    if n == 0:
        return 0
    # Start with highest-degree vertex
    candidates = set(range(n))
    clique = []
    while candidates:
        # Pick the vertex in candidates with the most edges to others
        # in candidates
        best = max(candidates, key=lambda v: len(adj[v] & candidates))
        clique.append(best)
        candidates &= adj[best]
    return len(clique)


# ── Constraint-remnant histogram proxy ──────────────────────────────────────

def codegree_histogram_bytes(adj, candidates):
    """
    For each vertex v in `candidates`, count how many OTHER vertices in
    candidates are adjacent to v (its co-degree within the candidate
    set). Bucketize and emit as fixed-length histogram.
    """
    counts = [0] * N_BUCKETS
    cand_list = sorted(candidates)
    for v in cand_list:
        codegree = len(adj[v] & candidates)
        bucket = min(codegree, N_BUCKETS - 1)
        counts[bucket] = min(counts[bucket] + 1, 255)
    return bytes(counts)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented clique branch-and-bound ───────────────────────────────────

class CliqueInstrumented:
    """
    Standard branch-and-bound clique enumeration:
      maintain current clique C and candidate set P (vertices that
      could extend C). Branch by picking a vertex v from P and either
      including it (C ∪ {v}, P ∩ N(v)) or excluding it (P \\ {v}).
    """
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
        return self._extend(set(), set(range(self.n)))

    def _extend(self, clique, candidates):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None

        if self.step % self.record_every == 0:
            data = codegree_histogram_bytes(self.adj, candidates)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step,
                "clique_size": len(clique),
                "candidate_size": len(candidates),
                "k_proxy": round(k, 6),
            })

        if len(clique) >= self.k:
            return list(clique)
        if len(clique) + len(candidates) < self.k:
            return None  # bound: can't reach k

        # Pick a candidate (lowest index)
        v = min(candidates)
        new_cand = candidates - {v}

        # Branch 1: include v
        self.decisions += 1
        res = self._extend(clique | {v}, new_cand & self.adj[v])
        if res is not None:
            return res
        if self.budget_exhausted:
            return None

        # Branch 2: exclude v
        self.decisions += 1
        return self._extend(clique, new_cand)


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
                   seed_base=1900, max_steps=80000):
    """
    k_offset: relative to greedy clique size.
        +1: ask for one more than greedy (typically tight or unsat)
        +2: ask for two more than greedy (very hard, often unsat)
    """
    results = []
    for inst in range(n_instances):
        adj = gen_clique_instance(n, edge_prob, seed_base + inst)
        greedy_size = greedy_clique(adj)
        k = max(2, greedy_size + k_offset)
        solver = CliqueInstrumented(adj, k=k,
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
            "greedy_clique": greedy_size,
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
    print("Clique Decision K-Trajectory — codegree histogram proxy")
    print("Cycle 22 Odd (loop 8) — 8th NP family probe")
    print("=" * 72)

    # Hard configs: ask for k = greedy + 1 or +2 on dense graphs.
    # Easy config: k well below greedy.
    configs = [
        (40, 0.5, -2, "easy-40 (k = greedy - 2)"),
        (40, 0.5, +1, "hard-40 (k = greedy + 1)"),
        (50, 0.5, +1, "hard-50 (k = greedy + 1)"),
        (60, 0.5, +1, "hard-60 (k = greedy + 1)"),
        (50, 0.7, +1, "hard-50-dense"),
    ]

    all_results = []
    for (n, p, koff, label) in configs:
        batch = run_experiment(n, p, koff, n_instances=8,
                               seed_base=1900, max_steps=80000)
        all_results.extend(batch)
        summarize(batch, f"{label}:")

    print("\n── Per-config K second-half slope summary ──")
    print(f"{'config':<30} {'avg slope':<15} verdict")
    for (n, p, koff, label) in configs:
        batch = [r for r in all_results
                 if r["n"] == n and abs(r["edge_prob"] - p) < 0.01
                 and (r["k_target"] - r["greedy_clique"]) == koff]
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
    out_path = "results/landscape_k_clique_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_clique",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "constraint-remnant: codegree histogram",
            "configs": [{"n": n, "p": p, "k_offset": koff, "label": l}
                        for (n, p, koff, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
