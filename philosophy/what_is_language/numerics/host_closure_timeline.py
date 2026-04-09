"""
host_closure_timeline.py — Cycle 7
Numerical Track: what_is_language

Given the HOST benchmark scaling data from result_003, extrapolate:
1. When (at what N/D) does each HOST gap close under scaling alone?
2. Which HOST gaps require architectural changes (flat scaling)?
3. What architectural change is needed for each flat-scaling gap?

Then combine all language gap numerical results into a single quantitative picture.
"""

import math

# From result_003: (benchmark, gap, exponent a, r2, category, arch_needed)
HOST_BENCHMARKS = [
    {
        "name": "QuALITY (long-doc comprehension)",
        "category": "consistency",
        "current_best": 0.61, "human": 0.93, "gap": 0.32,
        "a": 0.115, "r2": 0.26,
        "current_N": 7e10,
        "arch_needed": "context window length > 50K tokens",
        "scaling_closes": False,
    },
    {
        "name": "GSM8K (multi-step arithmetic)",
        "category": "agency",
        "current_best": 0.77, "human": 0.98, "gap": 0.21,
        "a": 1.014, "r2": 0.44,
        "current_N": 7e10,
        "arch_needed": "none (already closing fast)",
        "scaling_closes": True,
    },
    {
        "name": "Navigate (spatial agency)",
        "category": "agency",
        "current_best": 0.70, "human": 1.00, "gap": 0.30,
        "a": 0.178, "r2": 0.96,
        "current_N": 5.4e11,
        "arch_needed": "embodied / simulation environment",
        "scaling_closes": False,  # very slow; needs embodiment
    },
    {
        "name": "Causal judgment",
        "category": "agency",
        "current_best": 0.60, "human": 0.75, "gap": 0.15,
        "a": 0.058, "r2": 0.93,
        "current_N": 5.4e11,
        "arch_needed": "temporal reasoning; persistent state across episodes",
        "scaling_closes": False,
    },
    {
        "name": "SpatialQA (grounded reference)",
        "category": "grounding",
        "current_best": 0.65, "human": 0.98, "gap": 0.33,
        "a": 0.145, "r2": 0.89,
        "current_N": 5.4e11,
        "arch_needed": "multimodal input (vision + spatial)",
        "scaling_closes": False,
    },
    {
        "name": "LOCOMO (multi-session memory)",
        "category": "consistency",
        "current_best": 0.63, "human": 0.95, "gap": 0.32,
        "a": 0.234, "r2": 0.85,
        "current_N": 1.8e12,
        "arch_needed": "session memory / external memory store",
        "scaling_closes": False,
    },
]

SYNTACTIC_BENCHMARKS = [
    {"name": "BLiMP", "gap": 0.05, "a": 0.082, "scaling_closes": True},
    {"name": "HellaSwag", "gap": 0.12, "a": 0.273, "scaling_closes": True},
]

COMPOSITIONAL_BENCHMARKS = [
    {"name": "SCAN (structural prior)",  "gap": 0.08, "compression": 2263, "scaling_closes": True},
    {"name": "COGS (structural prior)",  "gap": 0.02, "compression": 3382, "scaling_closes": True},
]


def extrapolate_N_to_close(current_N, current_acc, human_acc, a, epsilon=0.01):
    """
    Find N such that acc = human_acc using power-law extrapolation.
    log_score = a * log10(N) + b
    Solve for N when score = human_acc.
    """
    if not a or a <= 0:
        return float("inf")
    # Fit b from current point
    b = math.log(current_acc) - a * math.log10(current_N)
    target_log_score = math.log(human_acc - epsilon)
    log10_N = (target_log_score - b) / a
    return 10 ** log10_N


def orders_of_magnitude_more(current_N, needed_N):
    if needed_N == float("inf"):
        return float("inf")
    return math.log10(needed_N / current_N)


def run():
    print("=" * 72)
    print("HOST GAP CLOSURE TIMELINE — what_is_language Cycle 7")
    print("=" * 72)

    print("\nHOST benchmarks — scaling extrapolation:")
    print(f"  {'Benchmark':<35} {'Gap':>5} {'a':>6} {'N_needed':>12} {'OM_more':>9} {'Closes?':>8}")
    print("-" * 78)

    for b in HOST_BENCHMARKS:
        n_needed = extrapolate_N_to_close(
            b["current_N"], b["current_best"], b["human"], b["a"]
        )
        om = orders_of_magnitude_more(b["current_N"], n_needed)
        closes = b["scaling_closes"]
        n_str = f"10^{math.log10(n_needed):.1f}" if n_needed < 1e25 else ">10^25"
        om_str = f"+{om:.1f}" if om < 20 else ">20"
        print(f"  {b['name'][:35]:<35} {b['gap']:5.2f} {b['a']:6.3f} {n_str:>12} {om_str:>9} {'YES' if closes else 'NO*':>8}")
        if not closes:
            print(f"  {'':35}   (* needs: {b['arch_needed']})")

    print("\nSyntactic benchmarks (memo):")
    for b in SYNTACTIC_BENCHMARKS:
        print(f"  {b['name']:<35} gap={b['gap']:.2f}  a={b['a']:.3f}  already closing")

    print("\nCompositional benchmarks (closed by structural prior):")
    for b in COMPOSITIONAL_BENCHMARKS:
        print(f"  {b['name']:<35} gap={b['gap']:.2f}  compression=x{b['compression']}  closed")

    print("\n" + "=" * 72)
    print("SUMMARY: Gap landscape")
    print("=" * 72)
    print("""
  CLOSED (frontier 2025-26):
    BLiMP, HellaSwag (syntactic) — closed
    SCAN, COGS (compositional) — closed via structural prior / large LM

  CLOSING VIA SCALE:
    GSM8K (multi-step arithmetic) — a=1.014, closing fast; ~10^0.5 more parameters needed
    Navigate (spatial) — a=0.178, very slow, needs >10^3 more scale

  ARCHITECTURAL (not closeable by scale alone):
    LOCOMO (multi-session memory)  — needs external persistent memory
    QuALITY (long-doc)             — needs context window >50K
    SpatialQA (grounding)          — needs multimodal (vision+spatial)
    Causal judgment                — needs temporal state persistence

  REQUIRES BOTH SCALE AND ARCHITECTURE:
    Navigate — very slow scaling + needs embodiment
    """)

    # Quantify the HOST gap vs syntactic gap
    host_gaps = [b["gap"] for b in HOST_BENCHMARKS]
    syn_gaps  = [b["gap"] for b in SYNTACTIC_BENCHMARKS]
    print(f"  Mean HOST gap:      {sum(host_gaps)/len(host_gaps):.3f}")
    print(f"  Mean syntactic gap: {sum(syn_gaps)/len(syn_gaps):.3f}")
    print(f"  Ratio:              {(sum(host_gaps)/len(host_gaps)) / (sum(syn_gaps)/len(syn_gaps)):.1f}x")


if __name__ == "__main__":
    run()
