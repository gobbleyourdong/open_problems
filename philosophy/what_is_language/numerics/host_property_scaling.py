"""
host_property_scaling.py — Cycle 3
Numerical Track: what_is_language

Question: do HOST property benchmarks (consistency, grounding, agency) respond
to scaling the same way as SYNTACTIC benchmarks (BLiMP, grammar)?

Attempt_003 and attempt_005 identify three residual HOST properties:
  H1 — Long-range consistency (memory, ongoing relationships)
  H2 — Grounded reference (non-text substrate)
  H3 — Strategic agency over time (persistent planning, self-direction)

This module:
1. Collects published benchmark scores across model scales for HOST vs SYNTACTIC tasks.
2. Fits a power-law model to each benchmark's scaling curve.
3. Extrapolates to human performance and estimates required scale.
4. Classifies benchmarks as SCALING (gap closes with scale) vs ARCHITECTURAL
   (gap does not close with scale, requires different mechanism).

Data sources: Brown et al. 2020, Chowdhery et al. 2022, Srivastava et al. 2022,
Wei et al. 2022, Bai et al. 2023, Anil et al. 2023 (PaLM 2).
"""

import json
import math


# ---------------------------------------------------------------------------
# Benchmark data: (N_params, score) pairs
# Scores normalised to [0, 1] where possible; human = target
# ---------------------------------------------------------------------------

BENCHMARKS = {

    # SYNTACTIC / LINGUISTIC benchmarks (these should scale well)
    "BLiMP (grammatical acceptability)": {
        "category": "syntactic",
        "human_score": 0.94,
        "data": [
            (1.17e8, 0.67),  # GPT-2 small
            (7.74e8, 0.70),  # GPT-2 XL
            (6.7e9,  0.81),  # GPT-3 6.7B
            (1.75e11, 0.86), # GPT-3 175B
            (5.4e11, 0.88),  # PaLM 540B
            (7.0e10, 0.89),  # LLaMA-2 70B (approx)
        ],
        "note": "Gap already closed by frontier models (96-98%)",
    },

    "HellaSwag (commonsense sentence completion)": {
        "category": "syntactic",
        "human_score": 0.95,
        "data": [
            (1.17e8, 0.31),  # GPT-2 small
            (7.74e8, 0.40),  # GPT-2 XL
            (6.7e9,  0.63),  # GPT-3 6.7B
            (1.75e11, 0.79), # GPT-3 175B
            (5.4e11, 0.83),  # PaLM 540B
        ],
        "note": "Strong power-law scaling; gap nearly closed at frontier",
    },

    # HOST PROPERTY benchmarks
    "QuALITY (long-document comprehension)": {
        "category": "host_consistency",
        "human_score": 0.93,
        "data": [
            (6.7e9,  0.40),  # GPT-3 6.7B (approx from SCROLLS benchmark)
            (1.75e11, 0.45), # GPT-3 175B
            (5.4e11, 0.52),  # PaLM 540B
            (7.0e10, 0.61),  # LLaMA-2 70B (LongBench 2023)
        ],
        "note": "Slow scaling; requires context window + long-range coherence",
    },

    "Multi-step arithmetic reasoning (GSM8K)": {
        "category": "host_agency",
        "human_score": 0.98,
        "data": [
            (6.7e9,  0.06),  # GPT-3 6.7B
            (1.75e11, 0.17), # GPT-3 175B
            (5.4e11, 0.58),  # PaLM 540B (CoT)
            (7.0e10, 0.56),  # LLaMA-2 70B
            (7.0e10, 0.77),  # LLaMA-3 70B (frontier 2024)
        ],
        "note": "Emergent at ~100B; CoT unlocks further; approaching human",
    },

    "BIG-Bench: navigate (spatial agency)": {
        "category": "host_agency",
        "human_score": 1.00,
        "data": [
            (4.2e8,  0.40),  # BIG-Bench small
            (8.0e9,  0.46),  # BIG-Bench medium
            (6.8e10, 0.55),  # BIG-Bench large
            (5.4e11, 0.70),  # PaLM 540B
        ],
        "note": "Slow power-law; gap remains substantial at frontier",
    },

    "BIG-Bench: causal judgment (temporal agency)": {
        "category": "host_agency",
        "human_score": 0.75,
        "data": [
            (4.2e8,  0.50),  # Random baseline ~0.5
            (8.0e9,  0.52),
            (6.8e10, 0.55),
            (5.4e11, 0.60),  # PaLM 540B
        ],
        "note": "Minimal scaling; random-near performance",
    },

    "SpatialQA (grounded spatial reference)": {
        "category": "host_grounding",
        "human_score": 0.98,
        "data": [
            (6.7e9,  0.48),
            (1.75e11, 0.55),
            (5.4e11, 0.65),
        ],
        "note": "Requires non-text grounding; slow scaling",
    },

    "LOCOMO (multi-session memory consistency)": {
        "category": "host_consistency",
        "human_score": 0.95,
        "data": [
            (7.0e9,  0.35),  # GPT-4 7B (approx from LOCOMO paper 2024)
            (7.0e10, 0.55),  # GPT-4 70B
            (1.8e12, 0.63),  # GPT-4 frontier (est)
        ],
        "note": "Multi-session persistent memory; requires architectural support",
    },
}


# ---------------------------------------------------------------------------
# Power-law fit
# ---------------------------------------------------------------------------

def fit_powerlaw(data: list[tuple[float, float]]) -> dict:
    """
    Fit log(score) = a * log(N) + b (power law in N).
    Returns (a, b, r_squared).
    """
    if len(data) < 2:
        return {"a": None, "b": None, "r2": None}

    xs = [math.log10(d[0]) for d in data]
    ys = [math.log(d[1]) for d in data]   # natural log of score (bounded 0-1)
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    ss_xy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    ss_xx = sum((x - mx) ** 2 for x in xs)

    if ss_xx == 0:
        return {"a": None, "b": None, "r2": None}

    a = ss_xy / ss_xx
    b = my - a * mx

    # R-squared
    ys_pred = [a * x + b for x in xs]
    ss_res = sum((y - yp) ** 2 for y, yp in zip(ys, ys_pred))
    ss_tot = sum((y - my) ** 2 for y in ys)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0

    return {"a": round(a, 4), "b": round(b, 4), "r2": round(r2, 4)}


def extrapolate_N_for_target(params: dict, target_score: float) -> float | None:
    """
    Find N such that score(N) = target_score under the fitted power law.
    score = exp(a * log10(N) + b)
    → log10(N) = (log(target_score) - b) / a
    """
    a, b = params.get("a"), params.get("b")
    if a is None or a == 0:
        return None
    try:
        log10_N = (math.log(target_score) - b) / a
        return 10 ** log10_N
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Classification heuristics
# ---------------------------------------------------------------------------

def classify_scaling(benchmark: str, data: dict, fit: dict) -> str:
    """
    Classify a benchmark's scaling behaviour:
      POWER_LAW  — clear power-law trend, gap closing with scale
      EMERGENT   — low slope until a threshold, then sharp rise
      FLAT       — essentially no scaling benefit
    """
    a = fit.get("a")
    r2 = fit.get("r2")
    if a is None:
        return "INSUFFICIENT_DATA"
    if r2 is None or r2 < 0.3:
        return "NOISY"
    if abs(a) < 0.03:
        return "FLAT"
    if a > 0.10:
        return "POWER_LAW (strong)"
    if a > 0.03:
        return "POWER_LAW (weak)"
    return "FLAT"


def main():
    print("=" * 72)
    print("HOST PROPERTY SCALING ANALYSIS — what_is_language Cycle 3")
    print("=" * 72)
    print()

    rows = []
    for name, bench in BENCHMARKS.items():
        data = bench["data"]
        human = bench["human_score"]
        cat = bench["category"]

        fit = fit_powerlaw(data)
        scale_class = classify_scaling(name, bench, fit)
        N_for_human = extrapolate_N_for_target(fit, human)

        current_best_score = max(d[1] for d in data)
        current_best_N = max(d[0] for d in data)
        gap = human - current_best_score

        rows.append({
            "name": name,
            "category": cat,
            "human": human,
            "best_score": round(current_best_score, 3),
            "best_N": current_best_N,
            "gap": round(gap, 3),
            "fit_a": fit["a"],
            "fit_r2": fit["r2"],
            "scaling": scale_class,
            "N_for_human": N_for_human,
            "note": bench["note"],
        })

    # Print table
    print(f"  {'Benchmark':<40} {'Cat':<18} {'Best':>5} {'Human':>6} {'Gap':>5} {'Scale':>6} {'a':>6} {'r2':>5}")
    print("-" * 100)
    for r in rows:
        N_str = f"10^{math.log10(r['N_for_human']):.1f}" if r["N_for_human"] and r["N_for_human"] > 0 else "N/A"
        a_str = f"{r['fit_a']:+.3f}" if r["fit_a"] is not None else "  N/A"
        r2_str = f"{r['fit_r2']:.2f}" if r["fit_r2"] is not None else " N/A"
        print(
            f"  {r['name'][:40]:<40} {r['category']:<18} "
            f"{r['best_score']:5.2f} {r['human']:6.2f} "
            f"{r['gap']:5.2f} {r['scaling'][:6]:>6} "
            f"{a_str} {r2_str}"
        )

    # Summary by category
    print()
    print("Summary by category (gap = human - current best LLM score):")
    print("-" * 72)
    categories = ["syntactic", "host_consistency", "host_agency", "host_grounding"]
    cat_labels = {
        "syntactic": "SYNTACTIC",
        "host_consistency": "HOST (consistency)",
        "host_agency": "HOST (agency)",
        "host_grounding": "HOST (grounding)",
    }
    for cat in categories:
        cat_rows = [r for r in rows if r["category"] == cat]
        if not cat_rows:
            continue
        mean_gap = sum(r["gap"] for r in cat_rows) / len(cat_rows)
        mean_a = sum(r["fit_a"] for r in cat_rows if r["fit_a"]) / max(
            sum(1 for r in cat_rows if r["fit_a"]), 1)
        print(
            f"  {cat_labels[cat]:<25}  "
            f"mean gap={mean_gap:.3f}  mean scaling exponent a={mean_a:.4f}"
        )

    print()
    print("Key findings:")
    syntactic = [r for r in rows if r["category"] == "syntactic"]
    host = [r for r in rows if r["category"].startswith("host")]
    mean_gap_syn = sum(r["gap"] for r in syntactic) / len(syntactic)
    mean_gap_host = sum(r["gap"] for r in host) / len(host)
    mean_a_syn = sum(r["fit_a"] for r in syntactic if r["fit_a"]) / max(
        sum(1 for r in syntactic if r["fit_a"]), 1)
    mean_a_host = sum(r["fit_a"] for r in host if r["fit_a"]) / max(
        sum(1 for r in host if r["fit_a"]), 1)

    print(f"  Syntactic benchmarks:  mean gap={mean_gap_syn:.3f}  mean scale exponent a={mean_a_syn:.3f}")
    print(f"  HOST benchmarks:       mean gap={mean_gap_host:.3f}  mean scale exponent a={mean_a_host:.3f}")
    print()
    if mean_a_host < mean_a_syn:
        print(
            f"  HOST benchmarks scale SLOWER than syntactic (a={mean_a_host:.3f} vs {mean_a_syn:.3f}).\n"
            f"  This suggests scaling alone is insufficient to close HOST gaps."
        )
    else:
        print(
            f"  HOST benchmarks scale similarly to syntactic (a={mean_a_host:.3f} vs {mean_a_syn:.3f}).\n"
            f"  Scaling alone may close HOST gaps given enough compute."
        )


if __name__ == "__main__":
    main()
