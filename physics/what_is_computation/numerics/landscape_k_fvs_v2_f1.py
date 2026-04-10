#!/usr/bin/env python3
"""
landscape_k_fvs_v2_f1.py — Cycle 41 Odd (loop 14, 2026-04-09)

F1 redesign attempt on FVS using a depth-distribution proxy.

Loop 10 found FVS F1 untestable: vertex-degree histogram on the
induced subgraph monotonically shrinks because the search itself
removes vertices on every branch (natural-progress shrinkage).

This loop's hypothesis: a proxy that does NOT depend on the
constraint frontier shrinking. Specifically, track the histogram
of "decisions per recursion depth" — how many decisions have
happened at each depth d ∈ [1..16]. If the search is STUCK
(F1 hard), it spends time at all depths uniformly; if PROGRESSING
(F2 easy), the depth distribution drifts toward deeper levels.

This is structurally different from constraint-frontier proxies:
it measures the SEARCH TREE shape, not the problem instance.

If F1 holds on hard FVS instances under this proxy, it would
flip FVS from F1 untestable to F1 HoldsOn.

Writes: results/landscape_k_fvs_v2_f1_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

N_BUCKETS = 16


# ── Generator (same as v1) ─────────────────────────────────────────────────

def gen_fvs_instance(n, edge_prob, seed):
    rng = random.Random(seed * 6263 + n)
    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < edge_prob:
                adj[i].add(j)
                adj[j].add(i)
    return adj


def has_cycle(adj_dict):
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
    sub = {}
    for u in range(len(adj)):
        if u in removed:
            continue
        sub[u] = adj[u] - removed
    return sub


def greedy_fvs(adj):
    n = len(adj)
    removed = set()
    sub = induced_subgraph(adj, removed)
    while has_cycle(sub):
        best = max(sub.keys(), key=lambda u: len(sub[u]))
        removed.add(best)
        sub = induced_subgraph(adj, removed)
    return len(removed)


# ── New proxy: depth-distribution histogram ─────────────────────────────────

def depth_histogram_bytes(depth_counts):
    """
    Encode the histogram of decisions-per-depth as fixed-length bytes.
    Each bucket holds a count, capped at 255.
    """
    histogram = [min(c, 255) for c in depth_counts[:N_BUCKETS]]
    while len(histogram) < N_BUCKETS:
        histogram.append(0)
    return bytes(histogram)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented backtracking ──────────────────────────────────────────────

class FVSInstrumentedV2:
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
        self.depth_counts = [0] * N_BUCKETS

    def solve(self):
        return self._backtrack(set(), 0)

    def _backtrack(self, removed, depth):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None

        # Track decision at this depth
        if depth < N_BUCKETS:
            self.depth_counts[depth] += 1

        if self.step % self.record_every == 0:
            data = depth_histogram_bytes(self.depth_counts)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step,
                "removed": len(removed),
                "depth": depth,
                "k_proxy": round(k, 6),
            })

        sub = induced_subgraph(self.adj, removed)
        if not has_cycle(sub):
            return list(removed)
        if len(removed) >= self.k:
            return None

        if not sub:
            return None
        best = max(sub.keys(), key=lambda u: len(sub[u]))

        self.decisions += 1
        res = self._backtrack(removed | {best}, depth + 1)
        if res is not None:
            return res
        if self.budget_exhausted:
            return None

        sorted_vertices = sorted(sub.keys(), key=lambda u: -len(sub[u]))
        for v in sorted_vertices[1:3]:
            self.decisions += 1
            res = self._backtrack(removed | {v}, depth + 1)
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
                   seed_base=4000, max_steps=80000):
    results = []
    for inst in range(n_instances):
        adj = gen_fvs_instance(n, edge_prob, seed_base + inst)
        greedy_size = greedy_fvs(adj)
        k = max(1, greedy_size + k_offset)
        solver = FVSInstrumentedV2(adj, k=k,
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
            else "flat (F1 NEW!)"
        )
        print(f"  avg 2nd-half slope: {avg:+.6f}  →  {verdict}")


def run():
    print("=" * 72)
    print("FVS F1 retest v2 — depth-distribution proxy (loop 14)")
    print("Cycle 41 Odd")
    print("=" * 72)

    configs = [
        (25, 0.5, -1, "hard-25 (k = greedy - 1)"),
        (30, 0.5, -1, "hard-30"),
        (35, 0.5, -1, "hard-35"),
        (30, 0.6, -1, "hard-30-dense"),
    ]

    all_results = []
    for (n, p, koff, label) in configs:
        batch = run_experiment(n, p, koff, n_instances=8,
                               seed_base=4000, max_steps=80000)
        all_results.extend(batch)
        summarize(batch, label)

    print("\n── F1 redesign verdict (FVS, depth-distribution proxy) ──")
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
                else "flat (F1!)"
            )
            print(f"{label:<28} {avg:+.6f}      {verdict}  "
                  f"(solved {solved}/{len(batch)}, dec {sum(decs)/len(decs):.0f})")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_fvs_v2_f1_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_fvs_v2_f1",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "depth-distribution histogram (loop 14 F1 redesign)",
            "configs": [{"n": n, "p": p, "k_offset": koff, "label": l}
                        for (n, p, koff, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
