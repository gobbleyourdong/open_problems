#!/usr/bin/env python3
"""
landscape_k_hamiltonian.py — Cycle 5 Odd (loop 2, 2026-04-09)

Third NP family for the K-trajectory probe: Hamiltonian cycle.

Lessons from the 3-coloring experiments (landscape_k_coloring v1, v2):

  v1 (unresolved edges + gzip): gzip overhead on shrinking blob
                                → artifact signal, dead-end
  v2 (full state bytes + gzip): measures assignment progress, not
                                landscape opacity → dead-end

  Diagnosis (in landscape_k_coloring_v2_findings.md):
      The SAT fingerprint works because `landscape_k.py` measures the
      REMAINING CLAUSES — the actual constraint landscape that unit
      propagation collapses. For 3-coloring backtracking, no equivalent
      "constraint collapses" during search, so there is no analog.

Hamiltonian cycle has the SAME structural issue as 3-coloring: the
constraint is the adjacency list and it never collapses. So we apply
a different approach: a CONSTRAINT-REMNANT proxy that measures, at
each decision point, the REMAINING DEGREE OF FREEDOM — how many valid
continuations exist from the current partial path. This is the Ham
cycle analog of "remaining clauses":

  K-proxy(partial_path) =
      gzip-ratio of the encoded list of valid next-step candidates
      across all frontier nodes.

For easy instances, this degree of freedom drops quickly via
forced-move detection; for hard instances, it stays diffuse.

Writes:
    results/landscape_k_hamiltonian_data.json
"""

import random, time, gzip, json, os, sys

sys.setrecursionlimit(50000)


# ── Graph generator ─────────────────────────────────────────────────────────

def gen_ham_instance(n, edge_prob, seed):
    """
    Random undirected graph G(n, p). To ensure a Hamiltonian cycle
    exists, we seed it with a random cycle, then add extra random
    edges on top. Returns (adj list, embedded_cycle).
    """
    rng = random.Random(seed * 7919 + n)
    perm = list(range(n))
    rng.shuffle(perm)
    adj = [set() for _ in range(n)]
    for i in range(n):
        u = perm[i]
        v = perm[(i + 1) % n]
        adj[u].add(v)
        adj[v].add(u)
    # Extra edges with probability edge_prob (not counting the cycle edges).
    for i in range(n):
        for j in range(i + 1, n):
            if j not in adj[i] and rng.random() < edge_prob:
                adj[i].add(j)
                adj[j].add(i)
    return adj, perm


# ── Constraint-remnant K-proxy ──────────────────────────────────────────────

def candidate_list_bytes(adj, path, visited, n):
    """
    Encode the 'remaining degrees of freedom' at this state:
      - For the current endpoint of the path, list valid next neighbors
        (those not yet in the path).
      - For each unvisited node, list its neighbors still unvisited.
    This measures how much of the adjacency structure remains unconstrained.
    """
    out = bytearray()
    # Current endpoint choices
    if path:
        u = path[-1]
        out.append(0xFF)                              # delimiter
        out.append(u & 0xFF)
        for v in sorted(adj[u]):
            if not visited[v]:
                out.append(v & 0xFF)
    # Unvisited-node adjacency remnants
    for u in range(n):
        if visited[u]:
            continue
        out.append(0xFE)                              # delimiter
        out.append(u & 0xFF)
        for v in sorted(adj[u]):
            if not visited[v]:
                out.append(v & 0xFF)
    return bytes(out)


def k_proxy(data):
    if len(data) == 0:
        return 0.0
    c = gzip.compress(data, compresslevel=9)
    return len(c) / len(data)


# ── Instrumented Hamiltonian-cycle backtracking ────────────────────────────

class HamInstrumented:
    def __init__(self, n, adj, record_every=5, max_steps=30000):
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
            k = k_proxy(data) if len(data) >= 20 else 0.0
            self.depth_k_values.append({
                "step": self.step,
                "depth": len(path),
                "k_proxy": round(k, 6),
                "encoded_len": len(data),
            })

        if len(path) == self.n:
            # Need to close the cycle back to node 0
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


# ── Experiment driver ───────────────────────────────────────────────────────

def run_experiment(n, edge_prob, n_instances=3, seed_base=400, max_steps=30000):
    results = []
    for inst in range(n_instances):
        adj, embedded = gen_ham_instance(n, edge_prob, seed_base + inst)
        solver = HamInstrumented(n, adj, record_every=5, max_steps=max_steps)
        t0 = time.perf_counter()
        sol = solver.solve()
        elapsed = time.perf_counter() - t0

        k_vals = [r["k_proxy"] for r in solver.depth_k_values]
        k_initial = k_vals[0] if k_vals else None
        k_final   = k_vals[-1] if k_vals else None
        k_mean    = sum(k_vals) / len(k_vals) if k_vals else None
        slope = ((k_vals[-1] - k_vals[0]) / max(len(k_vals) - 1, 1)
                 if len(k_vals) >= 2 else 0.0)
        if len(k_vals) >= 2:
            trend = (
                "decreasing" if k_vals[-1] < k_vals[0] - 0.01
                else "increasing" if k_vals[-1] > k_vals[0] + 0.01
                else "flat"
            )
        else:
            trend = "too_short"
        n_edges = sum(len(s) for s in adj) // 2

        results.append({
            "instance": inst,
            "n": n,
            "edge_prob": edge_prob,
            "n_edges": n_edges,
            "solved": sol is not None,
            "budget_exhausted": solver.budget_exhausted,
            "decisions": solver.decisions,
            "steps": solver.step,
            "time_ms": round(elapsed * 1000, 4),
            "n_k_records": len(k_vals),
            "k_initial": round(k_initial, 4) if k_initial is not None else None,
            "k_final":   round(k_final,   4) if k_final   is not None else None,
            "k_mean":    round(k_mean,    4) if k_mean    is not None else None,
            "k_slope":   round(slope, 6),
            "k_trend":   trend,
            "k_trajectory_head": solver.depth_k_values[:20],
        })
    return results


def summarize(batch, label):
    if not batch:
        return
    kinit = [r["k_initial"] for r in batch if r["k_initial"] is not None]
    kfin  = [r["k_final"]   for r in batch if r["k_final"]   is not None]
    kslope= [r["k_slope"]   for r in batch]
    decs  = [r["decisions"] for r in batch]
    print(f"\n{label}")
    print(f"  n_edges (avg):     {sum(r['n_edges'] for r in batch)/len(batch):.1f}")
    if kinit:
        print(f"  K_initial (avg):   {sum(kinit)/len(kinit):.4f}")
        print(f"  K_final   (avg):   {sum(kfin)/len(kfin):.4f}")
        print(f"  K_slope   (avg):   {sum(kslope)/len(kslope):+.6f}")
    else:
        print(f"  K: too few records")
    print(f"  decisions (avg):   {sum(decs)/len(decs):.1f}")
    counts = {
        "decreasing": sum(1 for r in batch if r["k_trend"] == "decreasing"),
        "flat":       sum(1 for r in batch if r["k_trend"] == "flat"),
        "increasing": sum(1 for r in batch if r["k_trend"] == "increasing"),
        "too_short":  sum(1 for r in batch if r["k_trend"] == "too_short"),
    }
    print(f"  trends:            {counts}")


def run():
    print("=" * 72)
    print("Hamiltonian Cycle K-Trajectory — constraint-remnant proxy")
    print("Cycle 5 Odd (loop 2) — third NP family")
    print("=" * 72)

    # edge_prob = 0.0 → minimal cycle (trivially solvable via embedded)
    # edge_prob = 0.05 → slightly denser (still easy)
    # edge_prob = 0.2 → dense; backtracking has many wrong moves
    # edge_prob = 0.5 → very dense; usually multiple Ham cycles, still easy-ish
    configs = [
        (20, 0.05, "sparse-20"),
        (20, 0.20, "moderate-20"),
        (30, 0.05, "sparse-30"),
        (30, 0.20, "moderate-30"),
    ]

    all_results = []
    for n, p, label in configs:
        batch = run_experiment(n, p, n_instances=3, seed_base=400, max_steps=30000)
        all_results.extend(batch)
        summarize(batch, f"{label} (n={n}, edge_prob={p}):")

    print("\n── Per-config K-slope summary ──")
    for n, p, label in configs:
        batch = [r for r in all_results if r["n"] == n and abs(r["edge_prob"] - p) < 0.01]
        slopes = [r["k_slope"] for r in batch]
        if slopes:
            avg = sum(slopes) / len(slopes)
            verdict = (
                "decreasing"  if avg < -0.001
                else "increasing" if avg > 0.001
                else "flat"
            )
            print(f"  {label:<20}  avg slope = {avg:+.6f}  →  {verdict}")

    os.makedirs("results", exist_ok=True)
    out_path = "results/landscape_k_hamiltonian_data.json"
    with open(out_path, "w") as f:
        json.dump({
            "label": "landscape_k_hamiltonian",
            "date": time.strftime("%Y-%m-%d"),
            "proxy": "constraint-remnant: valid-next + unvisited-adjacency",
            "configs": [{"n": c[0], "p": c[1], "desc": c[2]} for c in configs],
            "results": all_results,
        }, f, indent=2)
    print(f"\nManifest → {out_path}")


if __name__ == "__main__":
    run()
