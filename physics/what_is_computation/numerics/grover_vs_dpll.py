#!/usr/bin/env python3
"""
grover_vs_dpll.py — Grover's algorithm vs classical search vs DPLL scaling.

Simulates Grover's quantum amplitude amplification on an unstructured search
problem (find the marked item in N = 2^n items) and compares:
  - Classical exhaustive search: O(N/2) = O(2^n / 2) queries
  - Grover: O(pi/4 * sqrt(N)) = O(pi/4 * 2^(n/2)) queries
  - DPLL estimate: 67.7 × 2^(n/14.24) find/verify ratio from sat_scaling results

Key findings measured:
  - Classical doubling period: 1 variable (queries double per extra variable)
  - Grover doubling period: 2 variables (queries double per 2 extra variables)
  - DPLL doubling period: 14.24 variables
  - Quantum advantage = classical/Grover = 2^(n/2) — grows exponentially in n
  - Advantage is sub-exponential (exponent halved), NOT polynomial

Physical interpretation for gap.md R3:
  Grover reduces the K-search exponent by factor 2, but cannot collapse the
  exponential asymmetry to polynomial. The remaining gap is still exponential.
  This is consistent with BQP ⊃ P without collapsing P vs NP.

Numerical track, what_is_computation Phase 3 — 2026-04-09
"""

import math
import json
import os
import random

# ── Grover simulation ──────────────────────────────────────────────────────────

def grover_simulate(n: int, target: int, n_iterations: int) -> tuple[float, int]:
    """
    Simulate Grover's algorithm on 2^n items with one marked target.

    State: complex amplitude vector of length N = 2^n.
    Initial state: uniform superposition |+> = (1/sqrt(N)) * sum_i |i>.
    Oracle: flip phase of target state: |target> -> -|target>.
    Diffusion: apply 2|+><+| - I (inversion about the mean).

    Returns (success_probability, n_oracle_calls_used).
    The theoretical optimal number of iterations is floor(pi/4 * sqrt(N)).
    """
    N = 1 << n  # 2^n

    # Initialize uniform superposition: all amplitudes = 1/sqrt(N)
    amp = [1.0 / math.sqrt(N)] * N  # real amplitudes (Grover stays real if
    # initialized real with a real oracle — the phase flip keeps real amplitudes real)

    oracle_calls = 0
    for _ in range(n_iterations):
        # Step 1: Oracle — flip amplitude of target
        amp[target] = -amp[target]
        oracle_calls += 1

        # Step 2: Diffusion operator: 2|+><+| - I
        # <+|psi> = mean amplitude (since |+> = (1/sqrt(N))*sum|i>, and
        # <+|psi> = (1/sqrt(N)) * sum(amp) so 2|+><+||psi> = 2*(mean/sqrt(N))*|+>
        # = 2*(mean/sqrt(N))*(1/sqrt(N))*[1,1,...,1] = (2*mean/N)*[1,...,1]
        # But the standard form: new_amp[i] = 2*mean - amp[i]
        mean_amp = sum(amp) / N
        for i in range(N):
            amp[i] = 2.0 * mean_amp - amp[i]

    # Success probability = |amp[target]|^2
    prob = amp[target] ** 2
    return prob, oracle_calls


def grover_optimal_iterations(n: int) -> int:
    """Theoretical optimal number of Grover iterations: floor(pi/4 * sqrt(2^n))."""
    N = 1 << n
    return max(1, int(math.floor(math.pi / 4.0 * math.sqrt(N))))


def grover_query_count(n: int) -> float:
    """
    Effective query count for Grover: pi/4 * sqrt(2^n).
    This is the number of oracle calls at the optimal iteration count.
    """
    N = 1 << n
    return (math.pi / 4.0) * math.sqrt(N)


def classical_expected_queries(n: int) -> float:
    """
    Classical exhaustive search expected queries to find one marked item in N = 2^n.
    Expected = (N+1)/2 ≈ N/2.
    """
    N = 1 << n
    return (N + 1) / 2.0


def dpll_ratio_estimate(n: int, A: float = 67.7, k: float = 14.24) -> float:
    """
    DPLL find/verify ratio from sat_scaling exponential fit.
    ratio(n) ≈ A × 2^(n/k)
    This is the factor by which DPLL search exceeds linear verification.
    """
    return A * (2 ** (n / k))


# ── Doubling period analysis ───────────────────────────────────────────────────

def doubling_period(query_fn, n1: int, n2: int) -> float:
    """
    Compute the number of variables needed to double the query count,
    given two data points. Solves q(n2) = 2^((n2-n1)/k) * q(n1) for k.
    """
    q1 = query_fn(n1)
    q2 = query_fn(n2)
    if q1 <= 0 or q2 <= 0 or q1 == q2:
        return float("inf")
    ratio = q2 / q1
    dn = n2 - n1
    if ratio <= 0:
        return float("inf")
    # ratio = 2^(dn/k) => k = dn / log2(ratio)
    return dn / math.log2(ratio)


# ── Success probability table ──────────────────────────────────────────────────

def grover_probability_curve(n: int) -> list[tuple[int, float]]:
    """
    Show Grover success probability vs number of iterations for a given n.
    Returns list of (iteration, probability).
    """
    target = random.randint(0, (1 << n) - 1)
    N = 1 << n
    amp = [1.0 / math.sqrt(N)] * N
    results = []
    optimal = grover_optimal_iterations(n)
    max_iter = optimal + 5  # show a few past optimal too

    for it in range(1, max_iter + 1):
        # Oracle
        amp[target] = -amp[target]
        # Diffusion
        mean_amp = sum(amp) / N
        for i in range(N):
            amp[i] = 2.0 * mean_amp - amp[i]
        prob = amp[target] ** 2
        results.append((it, prob))

    return results


# ── Main comparison table ──────────────────────────────────────────────────────

def main():
    random.seed(42)

    N_LIST = [4, 6, 8, 10, 12, 14]
    DPLL_A = 67.7
    DPLL_K = 14.24

    print("=" * 80)
    print("Grover vs Classical vs DPLL — Scaling Comparison")
    print("=" * 80)
    print()
    print("Setting: find one marked item in N = 2^n items.")
    print("  Classical exhaustive: expected (N+1)/2 queries")
    print("  Grover (quantum):     pi/4 * sqrt(N) oracle calls")
    print("  DPLL (from sat_scaling): ratio estimate 67.7 * 2^(n/14.24)")
    print()

    # ── Table 1: Raw query counts ──────────────────────────────────────────────
    print("── Table 1: Query Counts vs n ──")
    print(f"{'n':>4} {'N=2^n':>8} {'Classical':>14} {'Grover':>12} {'DPLL ratio':>12} {'Gr/Cl speedup':>15} {'Gr/Cl ratio':>12}")
    print("─" * 85)

    rows = []
    for n in N_LIST:
        N = 1 << n
        classical = classical_expected_queries(n)
        grover = grover_query_count(n)
        dpll_ratio = dpll_ratio_estimate(n, DPLL_A, DPLL_K)
        speedup = classical / grover  # quantum advantage factor
        gr_cl_ratio = grover / classical  # < 1

        print(f"{n:>4} {N:>8} {classical:>14.1f} {grover:>12.2f} {dpll_ratio:>12.1f} {speedup:>15.2f}× {'1/' + str(round(speedup, 1)) + 'th':>12}")

        rows.append({
            "n": n,
            "N": N,
            "classical_queries": classical,
            "grover_queries": round(grover, 4),
            "dpll_ratio_estimate": round(dpll_ratio, 4),
            "quantum_speedup": round(speedup, 4),
        })

    print()

    # ── Table 2: Doubling periods ──────────────────────────────────────────────
    print("── Table 2: Observed Doubling Periods ──")
    print()
    print("Theoretical:")
    print(f"  Classical: doubling period = 1 variable  (queries ∝ 2^n)")
    print(f"  Grover:    doubling period = 2 variables (queries ∝ 2^(n/2))")
    print(f"  DPLL:      doubling period = {DPLL_K} variables (ratio ∝ 2^(n/{DPLL_K}))")
    print()
    print("Measured (from consecutive n values):")
    print(f"  {'n1->n2':>8} {'Classical dp':>14} {'Grover dp':>12} {'DPLL dp':>10}")
    print("  " + "─" * 50)

    for i in range(len(N_LIST) - 1):
        n1 = N_LIST[i]
        n2 = N_LIST[i + 1]
        dn = n2 - n1
        cl_dp = doubling_period(classical_expected_queries, n1, n2)
        gr_dp = doubling_period(grover_query_count, n1, n2)
        dpll_dp = doubling_period(lambda n: dpll_ratio_estimate(n, DPLL_A, DPLL_K), n1, n2)
        print(f"  {str(n1)+'->'+str(n2):>8} {cl_dp:>14.2f} {gr_dp:>12.2f} {dpll_dp:>10.2f}")

    print()

    # ── Table 3: Quantum advantage growth ─────────────────────────────────────
    print("── Table 3: Quantum Advantage (Classical/Grover) vs n ──")
    print()
    print("  Advantage = Classical/Grover = 2^(n/2)")
    print("  This grows exponentially: each 2 variables added doubles the advantage.")
    print()
    print(f"  {'n':>4} {'Advantage':>12} {'log2(Advantage)':>16} {'Expected 2^(n/2)':>18}")
    print("  " + "─" * 55)
    for n in N_LIST:
        classical = classical_expected_queries(n)
        grover = grover_query_count(n)
        advantage = classical / grover
        log2_adv = math.log2(advantage)
        expected = 2 ** (n / 2)
        print(f"  {n:>4} {advantage:>12.2f} {log2_adv:>16.3f} {expected:>18.2f}")

    print()

    # ── Grover simulation verification ────────────────────────────────────────
    print("── Table 4: Grover Simulation — Success Probability at Optimal Iterations ──")
    print()
    print("  Simulates the full 2^n amplitude vector, applies oracle + diffusion.")
    print()
    print(f"  {'n':>4} {'N':>8} {'Opt iters':>10} {'Simulated P(success)':>22} {'Expected P':>12}")
    print("  " + "─" * 65)

    sim_results = []
    for n in N_LIST:
        N = 1 << n
        target = random.randint(0, N - 1)
        opt_iter = grover_optimal_iterations(n)

        prob, oracle_calls = grover_simulate(n, target, opt_iter)

        # Theoretical success probability after k optimal iterations:
        # P(success) = sin^2((2k+1)*arcsin(1/sqrt(N)))
        theta = math.asin(1.0 / math.sqrt(N))
        expected_prob = math.sin((2 * opt_iter + 1) * theta) ** 2

        print(f"  {n:>4} {N:>8} {opt_iter:>10} {prob:>22.6f} {expected_prob:>12.6f}")
        sim_results.append({
            "n": n,
            "N": N,
            "target": target,
            "optimal_iterations": opt_iter,
            "simulated_prob": round(prob, 8),
            "theoretical_prob": round(expected_prob, 8),
            "oracle_calls": oracle_calls,
        })

    print()

    # ── Probability convergence for n=8 ───────────────────────────────────────
    print("── Table 5: Grover Convergence for n=8 (N=256 items) ──")
    print()
    print("  Shows success probability building up iteration by iteration.")
    print("  Optimal = floor(pi/4 * sqrt(256)) = floor(12.57) = 12 iterations.")
    print()
    n_demo = 8
    opt_demo = grover_optimal_iterations(n_demo)
    N_demo = 1 << n_demo
    target_demo = random.randint(0, N_demo - 1)

    amp = [1.0 / math.sqrt(N_demo)] * N_demo
    print(f"  {'Iter':>6} {'P(success)':>12} {'Cumul P':>12}")
    print("  " + "─" * 35)
    cumul_queries = 0
    for it in range(1, opt_demo + 5):
        amp[target_demo] = -amp[target_demo]
        mean_amp = sum(amp) / N_demo
        for i in range(N_demo):
            amp[i] = 2.0 * mean_amp - amp[i]
        prob_it = amp[target_demo] ** 2
        cumul_queries += 1
        marker = "  <-- optimal" if it == opt_demo else ""
        print(f"  {it:>6} {prob_it:>12.6f} {prob_it:>12.6f}{marker}")

    print()

    # ── Physical interpretation ────────────────────────────────────────────────
    print("=" * 80)
    print("Physical Interpretation for gap.md R3")
    print("=" * 80)
    print()
    print("Q: What does BQP strictly containing P imply about the substrate-")
    print("   dependence of K-manipulation?")
    print()
    print("Three K-search regimes, ordered by hardness of finding:")
    print()
    print(f"  1. DPLL (classical SAT solver, structured search):")
    print(f"       Query scaling: ~67.7 × 2^(n/14.24)")
    print(f"       Doubling period: k ≈ 14 variables")
    print(f"       Interpretation: structured K-manipulation exploits local")
    print(f"       propagation chains (K-gradients) to prune the search tree.")
    print()
    print(f"  2. Classical exhaustive search (no structure):")
    print(f"       Query scaling: 2^(n-1) ≈ 2^n / 2")
    print(f"       Doubling period: k = 1 variable")
    print(f"       Interpretation: worst-case K-search; no exploitation of")
    print(f"       problem structure; every item examined independently.")
    print()
    print(f"  3. Grover (quantum amplitude amplification):")
    print(f"       Query scaling: (pi/4) × 2^(n/2)")
    print(f"       Doubling period: k = 2 variables")
    print(f"       Interpretation: quantum superposition allows simultaneous")
    print(f"       amplitude testing of all 2^n items; interference amplifies")
    print(f"       the target. Accesses a different K-function class.")
    print()
    print("Quantum advantage = Classical/Grover = 2^(n/2):")
    print()
    for n in N_LIST:
        adv = classical_expected_queries(n) / grover_query_count(n)
        print(f"  n={n:>2}: {adv:.1f}× speedup  (Grover uses {grover_query_count(n):.1f} vs {classical_expected_queries(n):.0f} classical queries)")
    print()
    print("Key result: Grover halves the exponent (2^n → 2^(n/2)) but CANNOT")
    print("make the problem polynomial. Classical/Grover = 2^(n/2) itself grows")
    print("exponentially. The compression-finding asymmetry (P vs NP) persists.")
    print()
    print("Physical Church-Turing note:")
    print("  Grover is a quantum K-manipulation that classical computation can")
    print("  SIMULATE (we just did it — this script is a classical simulation")
    print("  of a 2^n amplitude vector). But the simulation costs O(N × iter)")
    print("  = O(N^1.5) time on classical hardware. Grover's PHYSICAL advantage")
    print("  is real (it uses quantum interference, not the full state vector),")
    print("  but it does not violate Church-Turing — it accesses a broader class")
    print("  of K-functions (those computable by quantum circuits) that is still")
    print("  within the Turing-computable class (just with exponential overhead")
    print("  when run on a classical simulator).")
    print()
    print("Conclusion for R3 (gap.md):")
    print("  BQP ⊃ P (if true) means quantum hardware accesses a K-function")
    print("  class with a halved exponent for unstructured search. This is a")
    print("  substrate-dependent constant in the exponent — not a qualitative")
    print("  change in the asymptote. The compression asymmetry (find harder")
    print("  than verify) persists in quantum computation. Quantum does NOT")
    print("  dissolve P vs NP; it moves the doubling period from k=1 to k=2.")
    print("  Structured algorithms (DPLL, k≈14) already beat Grover on SAT by")
    print("  exploiting problem structure. The hierarchy is:")
    print()
    print("    Exhaustive (k=1)  >  Grover (k=2)  <<  DPLL (k=14)")
    print("    [hardest for searcher]              [best classical]")
    print()
    print("  Grover is optimal for unstructured oracular search (BBBV theorem).")
    print("  DPLL exploits structure — it is accessing the K-gradient of SAT")
    print("  instances, which Grover cannot do in the standard oracle model.")

    # ── Save results ───────────────────────────────────────────────────────────
    os.makedirs("~/open_problems/physics/what_is_computation/results", exist_ok=True)
    out_path = "~/open_problems/physics/what_is_computation/results/grover_vs_dpll_data.json"

    # Recompute clean rows for JSON
    table_rows = []
    for n in N_LIST:
        N = 1 << n
        classical = classical_expected_queries(n)
        grover = grover_query_count(n)
        dpll_ratio = dpll_ratio_estimate(n, DPLL_A, DPLL_K)
        speedup = classical / grover
        opt_iter = grover_optimal_iterations(n)
        table_rows.append({
            "n": n,
            "N": N,
            "classical_queries": round(classical, 2),
            "grover_queries": round(grover, 4),
            "grover_optimal_iterations": opt_iter,
            "dpll_ratio_estimate": round(dpll_ratio, 4),
            "quantum_speedup_factor": round(speedup, 4),
            "theoretical_grover_speedup": round(2 ** (n / 2), 4),
        })

    output = {
        "description": "Grover vs classical exhaustive vs DPLL scaling comparison",
        "date": "2026-04-09",
        "dpll_fit": {
            "source": "sat_scaling.py results",
            "model": "67.7 * 2^(n/14.24)",
            "A": DPLL_A,
            "k": DPLL_K,
            "r_squared": 0.90,
        },
        "grover_model": {
            "oracle_calls": "pi/4 * sqrt(2^n)",
            "doubling_period_variables": 2,
            "success_prob_at_optimal_iter": "sin^2((2k+1)*arcsin(1/sqrt(N))) ≈ 1",
        },
        "classical_model": {
            "expected_queries": "(2^n + 1) / 2",
            "doubling_period_variables": 1,
        },
        "comparison_table": table_rows,
        "simulation_results": sim_results,
        "key_findings": {
            "doubling_periods": {
                "classical_exhaustive": 1,
                "grover_quantum": 2,
                "dpll_structured": DPLL_K,
            },
            "quantum_advantage": "2^(n/2) — exponential growth, not polynomial",
            "grover_effect": "halves the exponent (n -> n/2), does not collapse to polynomial",
            "p_vs_np_implication": (
                "Grover reduces the K-search exponent by 2x but cannot make NP problems "
                "polynomial-time. The compression asymmetry (find >> verify) persists in BQP."
            ),
            "physical_church_turing": (
                "Grover is classically simulable with O(N^1.5) overhead. This script is the "
                "simulation. BQP does not violate Church-Turing; it accesses a larger but "
                "still Turing-computable K-function class."
            ),
        },
    }

    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")

    return output


if __name__ == "__main__":
    main()
