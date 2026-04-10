#!/usr/bin/env python3
"""
landscape_k_hamiltonian_v3_f2.py — Cycle 23 Odd (loop 8, 2026-04-09)

F2 redesign attempt on Hamiltonian cycle.

Loop 3 finding (negative): F2 fails on Ham cycle under the candidate-
list bytes proxy, because easy Ham cycle instances at high edge
density showed POSITIVE slope (constraint-remnant completion artifact)
not the expected DECREASING slope.

Loop 7 verdict: F2 holds wherever the easy regime produces
"constraint-frontier shrinkage." Ham cycle's candidate-list IS a
constraint frontier, but the LIST grows shorter via DELETION rather
than via PROPAGATION CASCADES that compress the frontier.

This loop's hypothesis: a different proxy that explicitly tracks
**unvisited-degree** (the average number of remaining adjacent
unvisited nodes per unvisited node) would capture shrinkage as
propagation. As nodes are visited, the average unvisited-degree
decreases — that's the shrinkage signal.

Try this proxy on EASY Ham cycle instances (sparse graphs near the
threshold) and see if F2 flips from FailsOn to HoldsOn.

Writes: results/landscape_k_hamiltonian_v3_f2_data.json
"""

import random, time, gzip, json, os, sys, math

sys.setrecursionlimit(50000)

N_BUCKETS = 16


# ── Generator (same as v1/v2) ──────────────────────────────────────────────

def gen_ham_instance(n, edge_prob, seed):
    rng = random.Random(seed * 7919 + n)
    perm = list(range(n))
    rng.shuffle(perm)
    adj = [set() for _ in range(n)]
    for i in range(n):
        u, v = perm[i], perm[(i + 1) % n]
        adj[u].add(v)
        adj[v].add(u)
    for i in range(n):
        for j in range(i + 1, n):
            if j not in adj[i] and rng.random() < edge_prob:
                adj[i].add(j)
                adj[j].add(i)
    return adj, perm


# ── New proxy: unvisited-degree histogram (shrinkage signal) ───────────────

def unvisited_degree_histogram_bytes(adj, visited, n):
    """
    For each unvisited node u, count its UNVISITED neighbors. Bucketize.
    As more nodes get visited, the histogram shifts toward zero (each
    unvisited node has fewer unvisited neighbors), creating a shrinkage
    signal that the histogram-of-integers gzip proxy can detect.
    """
    counts = [0] * N_BUCKETS
    for u in range(n):
        if visited[u]:
            continue
        deg = sum(1 for v in adj[u] if not visited[v])
        bucket = min(deg, N_BUCKETS - 1)
        counts[bucket] = min(counts[bucket] + 1, 255)
    return bytes(counts)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented Ham cycle backtracking ────────────────────────────────────

class HamInstrumented:
    def __init__(self, n, adj, record_every=10, max_steps=80000):
        self.n = n
        self.adj = adj
        self.record_every = record_every
        self.max_steps = max_steps
        self.depth_k_values = []
        self.step = 0
        self.decisions = 0
        self.budget_exhausted = False

    def solve(self):
        visited = [False] * self.n
        visited[0] = True
        return self._backtrack([0], visited)

    def _backtrack(self, path, visited):
        self.step += 1
        if self.step > self.max_steps:
            self.budget_exhausted = True
            return None

        if self.step % self.record_every == 0:
            data = unvisited_degree_histogram_bytes(self.adj, visited, self.n)
            k = k_proxy(data)
            self.depth_k_values.append({
                "step": self.step,
                "depth": len(path),
                "k_proxy": round(k, 6),
            })

        if len(path) == self.n:
            if 0 in self.adj[path[-1]]:
                return list(path)
            return None

        u = path[-1]
        for v in sorted(self.adj[u]):
            if not visited[v]:
                visited[v] = True
                path.append(v)
                self.decisions += 1
                res = self._backtrack(path, visited)
                if res is not None:
                    return res
                if self.budget_exhausted:
                    return None
                path.pop()
                visited[v] = False
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


def run_experiment(n, edge_prob, n_instances=8, seed_base=2100, max_steps=80000):
    results = []
    for inst in range(n_instances):
        adj, _ = gen_ham_instance(n, edge_prob, seed_base + inst)
        solver = HamInstrumented(n, adj, record_every=10, max_steps=max_steps)
        t0 = time.perf_counter()
        sol = solver.solve()
        elapsed = time.perf_counter() - t0
        k_vals = [r["k_proxy"] for r in solver.depth_k_values]
        metrics = compute_metrics(k_vals)
        record = {
            "instance": inst,
            "n": n,
            "edge_prob": edge_prob,
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
    print("Hamiltonian Cycle K-Trajectory v3 — F2 redesign attempt")
    print("Cycle 23 Odd (loop 8) — unvisited-degree shrinkage proxy")
    print("=" * 72)

    # Test both easy and hard regimes with the new proxy:
    # - Loop 7 prediction: easy → decreasing (F2), hard → flat (F1)
    configs = []
    for n in [30, 40, 50]:
        thresh = math.log(n) / n
        for ratio, label_suffix in [(2.0, "easy"), (4.0, "v-easy"), (1.0, "hard")]:
            p = ratio * thresh
            label = f"n={n} p={p:.3f} ({label_suffix})"
            configs.append((n, round(p, 4), label, thresh))

    all_results = []
    for (n, p, label, thresh) in configs:
        batch = run_experiment(n, p, n_instances=8, seed_base=2100, max_steps=80000)
        all_results.extend(batch)
        summarize(batch, label)

    print("\n── F2 redesign verdict (Hamiltonian cycle, unvisited-degree proxy) ──")
    print(f"{'config':<28} {'avg slope':<15} verdict")
    for (n, p, label, thresh) in configs:
        batch = [r for r in all_results
                 if r["n"] == n and abs(r["edge_prob"] - p) < 1e-6]
        slopes = [r["second_half_slope"] for r in batch if "second_half_slope" in r]
        if slopes:
            avg = sum(slopes) / len(slopes)
            verdict = (
                "decreasing (F2!)" if avg < -0.0005
                else "increasing" if avg > 0.0005
                else "flat (F1)"
            )
            print(f"{label:<28} {avg:+.6f}      {verdict}")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_hamiltonian_v3_f2_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_hamiltonian_v3_f2",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "unvisited-degree histogram (loop 8 F2 redesign)",
            "configs": [{"n": n, "p": p, "label": l, "thresh": t}
                        for (n, p, l, t) in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
