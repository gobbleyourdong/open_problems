#!/usr/bin/env python3
"""
landscape_k_hamiltonian_v2.py — Cycle 7 Odd (loop 3, 2026-04-09)

Strengthens the weak signal from loop 2's landscape_k_hamiltonian.py.

Loop 2 result (n=30):
    sparse-30  (p=0.05, BELOW threshold = harder)  → slope ≈ 0 (flat)
    moderate-30 (p=0.20, above threshold = easier) → slope ≈ -0.001 (decreasing)

    Direction matches SAT fingerprint but signal was weak: 3 instances
    per config, mixed per-instance trends, small slopes.

Loop 3 strengthening:
    - Larger n (40, 50) where search genuinely occupies the recording
      window without trivial completion
    - More instances per config (8) for statistical reasonability
    - Edge probability sweep near the Hamiltonian-cycle phase
      transition (threshold ~ ln(n)/n)
    - Use second-half slope (after initial transient) instead of whole-
      trajectory slope

Writes: results/landscape_k_hamiltonian_v2_data.json
"""

import random, time, gzip, json, os, math, sys

sys.setrecursionlimit(200000)

SENTINEL_CURRENT = 0xFF
SENTINEL_UNVISITED = 0xFE


# ── Graph generator ────────────────────────────────────────────────────────

def gen_ham_instance(n, edge_prob, seed):
    """Random undirected graph with an embedded Hamiltonian cycle."""
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


# ── Constraint-remnant K-proxy (same as v1) ────────────────────────────────

def candidate_list_bytes(adj, path, visited, n):
    out = bytearray()
    if path:
        u = path[-1]
        out.append(SENTINEL_CURRENT)
        out.append(u & 0xFF)
        for v in sorted(adj[u]):
            if not visited[v]:
                out.append(v & 0xFF)
    for u in range(n):
        if visited[u]:
            continue
        out.append(SENTINEL_UNVISITED)
        out.append(u & 0xFF)
        for v in sorted(adj[u]):
            if not visited[v]:
                out.append(v & 0xFF)
    return bytes(out)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    return len(gzip.compress(data, compresslevel=9)) / len(data)


# ── Instrumented backtracking ──────────────────────────────────────────────

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
            data = candidate_list_bytes(self.adj, path, visited, self.n)
            if len(data) >= 20:
                k = k_proxy(data)
                self.depth_k_values.append({
                    "step": self.step,
                    "depth": len(path),
                    "k_proxy": round(k, 6),
                    "encoded_len": len(data),
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
    """Return initial/final/mean, full-range slope, and SECOND-HALF slope
    (to discount the initial transient where the proxy is climbing from
    the high-constraint starting state)."""
    if not k_vals:
        return None
    n = len(k_vals)
    k_init = k_vals[0]
    k_final = k_vals[-1]
    k_mean = sum(k_vals) / n
    full_slope = ((k_vals[-1] - k_vals[0]) / max(n - 1, 1)) if n >= 2 else 0.0
    if n >= 4:
        mid = n // 2
        tail = k_vals[mid:]
        if len(tail) >= 2:
            second_half_slope = (tail[-1] - tail[0]) / (len(tail) - 1)
        else:
            second_half_slope = 0.0
    else:
        second_half_slope = full_slope
    return {
        "k_initial": round(k_init, 4),
        "k_final":   round(k_final, 4),
        "k_mean":    round(k_mean, 4),
        "full_slope": round(full_slope, 6),
        "second_half_slope": round(second_half_slope, 6),
        "n_records": n,
    }


def run_experiment(n, edge_prob, n_instances=8, seed_base=500,
                   max_steps=80000):
    results = []
    for inst in range(n_instances):
        adj, embedded = gen_ham_instance(n, edge_prob, seed_base + inst)
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


def summarize(batch, label, near_threshold):
    if not batch:
        return
    decs = [r["decisions"] for r in batch]
    slopes_full = [r.get("full_slope") for r in batch if "full_slope" in r]
    slopes_h2   = [r.get("second_half_slope") for r in batch if "second_half_slope" in r]
    solved = sum(1 for r in batch if r.get("solved"))
    budget = sum(1 for r in batch if r.get("budget_exhausted"))
    print(f"\n{label}  (threshold ≈ ln(n)/n = {near_threshold:.3f})")
    print(f"  instances:    {len(batch)}  (solved={solved}, budget_exhausted={budget})")
    print(f"  avg decisions: {sum(decs)/len(decs):.1f}")
    if slopes_full:
        avg_full = sum(slopes_full) / len(slopes_full)
        print(f"  avg full slope:        {avg_full:+.6f}")
    if slopes_h2:
        avg_h2 = sum(slopes_h2) / len(slopes_h2)
        verdict = (
            "decreasing (easier fingerprint)" if avg_h2 < -0.0005
            else "increasing (unusual)" if avg_h2 > 0.0005
            else "flat (harder fingerprint)"
        )
        print(f"  avg second-half slope: {avg_h2:+.6f}  →  {verdict}")


def run():
    print("=" * 72)
    print("Hamiltonian Cycle K-Trajectory v2 — larger n, more instances")
    print("Cycle 7 Odd (loop 3)")
    print("=" * 72)

    # Loop 3 scale-up: n=40 and n=50, edge-prob sweep across the
    # Hamiltonian-cycle phase-transition threshold ln(n)/n.
    configs = []
    for n in [40, 50]:
        thresh = math.log(n) / n
        # Sweep p around the threshold: below, near, above.
        ps = [thresh * 0.5, thresh * 1.0, thresh * 2.0, thresh * 4.0]
        for p in ps:
            label = f"n={n} p={p:.3f} (thresh ratio {p/thresh:.1f}×)"
            configs.append((n, round(p, 4), label, thresh))

    all_results = []
    for (n, p, label, thresh) in configs:
        batch = run_experiment(n, p, n_instances=8, seed_base=500,
                               max_steps=80000)
        all_results.extend(batch)
        summarize(batch, label, thresh)

    print("\n── Per-config K second-half slope table ──")
    print(f"{'n':<5} {'p':<8} {'p/thresh':<10} {'2nd-half slope (avg)':<25} verdict")
    for (n, p, label, thresh) in configs:
        batch = [r for r in all_results if r["n"] == n and abs(r["edge_prob"] - p) < 1e-6]
        slopes = [r.get("second_half_slope") for r in batch if "second_half_slope" in r]
        if slopes:
            avg = sum(slopes) / len(slopes)
            ratio = p / thresh
            verdict = (
                "decreasing" if avg < -0.0005
                else "increasing" if avg > 0.0005
                else "flat"
            )
            print(f"{n:<5} {p:<8.4f} {ratio:<10.2f} {avg:+.6f}                 {verdict}")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_hamiltonian_v2_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_hamiltonian_v2",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "constraint-remnant: candidate list + unvisited adjacency",
            "configs": [
                {"n": n, "p": p, "label": label, "thresh": thresh}
                for (n, p, label, thresh) in configs
            ],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
