#!/usr/bin/env python3
"""
landscape_k_clique_v2_f1.py — Cycle 28 Odd (loop 10, 2026-04-09)

F1 retest on clique with WEAKENED bound.

Loop 8 (Cycle 22 Odd) found clique F1 untestable: branch-and-bound
with the bound `|C| + |P| < k → prune` was too efficient. Hard
configurations exhausted in 4-9920 decisions instead of filling the
80k step budget.

Loop 10 hypothesis: removing the bound (or weakening it) will let
the search explore more of the state space, filling the recording
window and exposing F1 if it's there.

Two strategies:
  v2a — REMOVE the bound entirely. Pure exhaustive search through
        the candidate set, branching include/exclude on every vertex.
  v2b — Use the bound but ask k = greedy + 2 or +3 (much harder
        UNSAT, more exhaustive backtracking required).

If F1 holds → clique moves from F1-untestable into the 5+2+2 dual
structure as the first family in BOTH the F1 and F2 testable subsets
(since loop 8 already confirmed F2 holds on clique).

Writes: results/landscape_k_clique_v2_f1_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)

N_BUCKETS = 16


def gen_clique_instance(n, edge_prob, seed):
    rng = random.Random(seed * 9941 + n)
    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < edge_prob:
                adj[i].add(j)
                adj[j].add(i)
    return adj


def greedy_clique(adj):
    n = len(adj)
    if n == 0:
        return 0
    candidates = set(range(n))
    clique = []
    while candidates:
        best = max(candidates, key=lambda v: len(adj[v] & candidates))
        clique.append(best)
        candidates &= adj[best]
    return len(clique)


def codegree_histogram_bytes(adj, candidates):
    counts = [0] * N_BUCKETS
    for v in sorted(candidates):
        codegree = len(adj[v] & candidates)
        bucket = min(codegree, N_BUCKETS - 1)
        counts[bucket] = min(counts[bucket] + 1, 255)
    return bytes(counts)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented unbounded clique search ──────────────────────────────────

class CliqueUnboundedInstrumented:
    """
    Clique search WITHOUT the standard bound. Branch on every vertex
    with include/exclude. Always explores the full tree (or the
    step-budget portion of it), exposing K-trajectory regardless of
    the bound's effectiveness.
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
        if not candidates:
            return None

        # NO BOUND — pick first candidate, branch include/exclude
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


def run_experiment(n, edge_prob, k_offset, n_instances=8, seed_base=2700, max_steps=80000):
    """Note: k_offset relative to greedy. k = greedy + offset.
    UNSAT for offset > 0 typically. The unbounded search will explore
    much more of the tree before terminating."""
    results = []
    for inst in range(n_instances):
        adj = gen_clique_instance(n, edge_prob, seed_base + inst)
        greedy_size = greedy_clique(adj)
        k = max(2, greedy_size + k_offset)
        solver = CliqueUnboundedInstrumented(adj, k=k,
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
    print("Clique F1 Retest — UNBOUNDED branch-and-bound, k = greedy + 2")
    print("Cycle 28 Odd (loop 10) — clique F1 testability")
    print("=" * 72)

    # Without the bound, even small n will fill the budget at greedy+2.
    # Try multiple sizes to find the regime where the budget is filled
    # but the slope is still measurable.
    configs = [
        (25, 0.5, +2, "n=25 k=greedy+2"),
        (30, 0.5, +2, "n=30 k=greedy+2"),
        (35, 0.5, +2, "n=35 k=greedy+2"),
        (40, 0.5, +2, "n=40 k=greedy+2"),
        (35, 0.5, +3, "n=35 k=greedy+3 (harder)"),
    ]

    all_results = []
    for (n, p, koff, label) in configs:
        batch = run_experiment(n, p, koff, n_instances=8,
                               seed_base=2700, max_steps=80000)
        all_results.extend(batch)
        summarize(batch, label)

    print("\n── Per-config K second-half slope summary ──")
    print(f"{'config':<25} {'avg slope':<15} verdict")
    for (n, p, koff, label) in configs:
        batch = [r for r in all_results
                 if r["n"] == n and abs(r["edge_prob"] - p) < 0.01
                 and (r["k_target"] - r["greedy_clique"]) == koff]
        slopes = [r["second_half_slope"] for r in batch if "second_half_slope" in r]
        decs   = [r["decisions"] for r in batch]
        solved = sum(1 for r in batch if r.get("solved"))
        budget = sum(1 for r in batch if r.get("budget_exhausted"))
        if slopes:
            avg = sum(slopes) / len(slopes)
            verdict = (
                "decreasing" if avg < -0.0005
                else "increasing" if avg > 0.0005
                else "flat"
            )
            print(f"{label:<25} {avg:+.6f}      {verdict}  "
                  f"(solved {solved}/{len(batch)}, budget={budget}, "
                  f"dec {sum(decs)/len(decs):.0f})")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_clique_v2_f1_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_clique_v2_f1",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "constraint-remnant: codegree histogram (UNBOUNDED search)",
            "configs": [{"n": n, "p": p, "k_offset": koff, "label": l}
                        for (n, p, koff, l) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
