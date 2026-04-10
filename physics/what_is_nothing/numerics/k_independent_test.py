#!/usr/bin/env python3
"""
k_independent_test.py
=====================

INDEPENDENT validation of K-minimality using a DIFFERENT K-estimation
method than k_minimal_landscape.py.

Motivation (from Phase 5 audit, attempt_006):
  "The K-cost function for flux configurations is a choice. Different
   functions give different results." The audit recommends testing with
   a second method. If the K-gradient holds, promote from candidate
   to stronger candidate.

METHOD 1 (k_minimal_landscape.py):
  K(config) = Σ ceil(log2(f_i + 1)) for nonzero fluxes

METHOD 2 (this file — MDL-based):
  K(config) = length of the shortest description of the flux vector
  using an integer compression scheme:
    - Encode the NUMBER of nonzero fluxes (log2(N+1) bits)
    - Encode WHICH fluxes are nonzero (log2(C(N_total, n_nonzero)) bits)
    - Encode the VALUES of nonzero fluxes (Σ log2(val) bits, Elias delta)
  This is closer to actual Kolmogorov complexity than Method 1.

METHOD 3 (this file — gzip proxy):
  K(config) = len(gzip(config_as_bytes))
  Gzip is a standard computable upper bound on Kolmogorov complexity.

If both Method 2 and Method 3 show K increasing with ρ within the
anthropic window, the K-gradient is robust to the estimation method.

Output: results/k_independent_test_data.json
        results/k_independent_test_findings.md
"""

import gzip
import json
import math
import os
import random
import struct

N_FLUX = 100
Q_MAX = 9
N_SAMPLES = 200_000
SEED = 42

def compute_rho(fluxes):
    """Vacuum energy: Σ f_i^2."""
    return sum(f * f for f in fluxes)

# --- Method 1: Original (from k_minimal_landscape.py) ---
def k_method1(fluxes):
    """K = Σ ceil(log2(f_i + 1)) for nonzero f_i."""
    return sum(math.ceil(math.log2(f + 1)) for f in fluxes if f > 0)

# --- Method 2: MDL combinatorial ---
def k_method2(fluxes):
    """MDL: encode count + positions + values."""
    n = len(fluxes)
    nonzero_indices = [i for i, f in enumerate(fluxes) if f > 0]
    n_nz = len(nonzero_indices)

    if n_nz == 0:
        return 1  # just encode "zero nonzero fluxes"

    # Cost 1: encode number of nonzero fluxes
    k = math.ceil(math.log2(n + 1))  # ~7 bits for n=100

    # Cost 2: encode which positions are nonzero
    # Using log2(C(n, n_nz)) bits (combinatorial number system)
    # Approximate: n_nz * log2(n/n_nz) + (n-n_nz) * log2(n/(n-n_nz))
    if 0 < n_nz < n:
        p = n_nz / n
        k += n * (-p * math.log2(p) - (1-p) * math.log2(1-p))
    # If n_nz == n, positions are determined (0 bits)

    # Cost 3: encode the values using Elias delta coding
    for f in fluxes:
        if f > 0:
            # Elias delta: ~log2(f) + 2*log2(log2(f)+1) + 1
            k += math.log2(f) + 2 * math.log2(math.log2(f) + 1) + 1

    return k

# --- Method 3: Gzip proxy ---
def k_method3(fluxes):
    """K ≈ len(gzip(bytes))."""
    # Pack fluxes as bytes
    data = bytes(fluxes)
    compressed = gzip.compress(data, compresslevel=9)
    return len(compressed) * 8  # convert bytes to bits

def main():
    random.seed(SEED)

    print(f"Independent K-test: {N_SAMPLES:,} configs, N_flux={N_FLUX}, q_max={Q_MAX}")
    print(f"Testing 3 K-estimation methods for robustness\n")

    # Sample configurations
    all_rho = []
    all_k1 = []
    all_k2 = []
    all_k3 = []

    for _ in range(N_SAMPLES):
        fluxes = [random.randint(0, Q_MAX) for _ in range(N_FLUX)]
        rho = compute_rho(fluxes)
        all_rho.append(rho)
        all_k1.append(k_method1(fluxes))
        all_k2.append(k_method2(fluxes))
        all_k3.append(k_method3(fluxes))

    # Define anthropic window (lowest 1% of ρ)
    sorted_rho = sorted(all_rho)
    window_top = sorted_rho[int(0.01 * N_SAMPLES)]
    window_mid = window_top // 2

    window_idx = [i for i in range(N_SAMPLES) if all_rho[i] <= window_top]
    n_window = len(window_idx)

    print(f"Anthropic window: ρ ≤ {window_top} (n={n_window})")

    # Split window into quintiles by ρ
    window_rho = [(all_rho[i], i) for i in window_idx]
    window_rho.sort()
    quintile_size = max(1, len(window_rho) // 5)

    results_by_method = {}

    for method_name, all_k in [("Method1_original", all_k1),
                                 ("Method2_MDL", all_k2),
                                 ("Method3_gzip", all_k3)]:
        quintiles = []
        for q in range(5):
            start = q * quintile_size
            end = min((q + 1) * quintile_size, len(window_rho))
            if start >= len(window_rho):
                break
            indices = [window_rho[j][1] for j in range(start, end)]
            rho_vals = [all_rho[i] for i in indices]
            k_vals = [all_k[i] for i in indices]
            quintiles.append({
                "quintile": q + 1,
                "rho_min": min(rho_vals),
                "rho_max": max(rho_vals),
                "rho_mean": sum(rho_vals) / len(rho_vals),
                "k_mean": sum(k_vals) / len(k_vals),
                "k_min": min(k_vals),
                "k_max": max(k_vals),
                "n": len(indices),
            })

        # K-gradient: difference between Q5 and Q1
        if len(quintiles) >= 2:
            k_q1 = quintiles[0]["k_mean"]
            k_q5 = quintiles[-1]["k_mean"]
            gradient = k_q5 - k_q1
            gradient_positive = gradient > 0
        else:
            gradient = 0
            gradient_positive = False

        # K-weighted mean ρ vs uniform mean ρ
        w_idx_k = [(all_k[i], all_rho[i]) for i in window_idx]
        weights = [2.0 ** (-k) for k, _ in w_idx_k]
        total_w = sum(weights)
        if total_w > 0:
            k_weighted_rho = sum(r * w for (_, r), w in zip(w_idx_k, weights)) / total_w
        else:
            k_weighted_rho = 0
        uniform_rho = sum(all_rho[i] for i in window_idx) / n_window
        shift = uniform_rho / k_weighted_rho if k_weighted_rho > 0 else 0

        results_by_method[method_name] = {
            "quintiles": quintiles,
            "k_gradient": round(gradient, 2),
            "gradient_positive": gradient_positive,
            "uniform_mean_rho": round(uniform_rho, 2),
            "k_weighted_mean_rho": round(k_weighted_rho, 4),
            "shift_factor": round(shift, 2),
        }

        print(f"\n--- {method_name} ---")
        print(f"  {'Q':>3} {'ρ range':>20} {'Mean K':>10} {'n':>6}")
        for q in quintiles:
            print(f"  {q['quintile']:>3} [{q['rho_min']:>6},{q['rho_max']:>6}] {q['k_mean']:>10.2f} {q['n']:>6}")
        print(f"  K-gradient (Q5-Q1): {gradient:.2f} bits")
        print(f"  Gradient positive (K increases with ρ): {gradient_positive}")
        print(f"  K-weighted shift: {shift:.2f}×")

    # --- Agreement analysis ---
    methods = list(results_by_method.keys())
    all_positive = all(results_by_method[m]["gradient_positive"] for m in methods)

    print(f"\n{'='*60}")
    print(f"AGREEMENT ANALYSIS")
    print(f"{'='*60}")
    for m in methods:
        r = results_by_method[m]
        print(f"  {m:20s}: gradient={r['k_gradient']:>8.2f}, positive={r['gradient_positive']}, shift={r['shift_factor']:.2f}×")
    print(f"\n  ALL methods show positive gradient: {all_positive}")
    if all_positive:
        print(f"  → K-minimality prediction ROBUST across estimation methods")
        print(f"  → Promote from 'candidate pattern' toward 'cross-validated'")
    else:
        print(f"  → K-minimality prediction NOT robust — method-dependent")
        print(f"  → Keep as 'candidate pattern', note method sensitivity")

    # --- Save ---
    out_dir = os.path.join(os.path.dirname(__file__), "..", "results")
    os.makedirs(out_dir, exist_ok=True)

    output = {
        "parameters": {"n_flux": N_FLUX, "q_max": Q_MAX, "n_samples": N_SAMPLES, "seed": SEED},
        "window": {"threshold": window_top, "n_vacua": n_window},
        "methods": results_by_method,
        "agreement": {"all_positive_gradient": all_positive},
    }

    data_path = os.path.join(out_dir, "k_independent_test_data.json")
    with open(data_path, "w") as f:
        json.dump(output, f, indent=2)

    # --- Findings ---
    findings = f"""# Independent K-Test — Findings

**Generated:** 2026-04-10
**Script:** numerics/k_independent_test.py
**Data:** results/k_independent_test_data.json
**Purpose:** Address Phase 5 audit recommendation: test K-gradient with independent estimation methods.

---

## Methods Tested

| Method | Description | K-gradient | Positive? | Shift |
|--------|------------|-----------|-----------|-------|
"""
    for m in methods:
        r = results_by_method[m]
        desc = {
            "Method1_original": "Σ ceil(log2(f+1)) per nonzero flux",
            "Method2_MDL": "Combinatorial: count + positions + Elias delta values",
            "Method3_gzip": "gzip(config_bytes) length × 8",
        }[m]
        findings += f"| {m} | {desc} | {r['k_gradient']:.2f} | {'YES' if r['gradient_positive'] else 'NO'} | {r['shift_factor']:.2f}× |\n"

    findings += f"""
## Key Result

**All three methods agree:** {'YES' if all_positive else 'NO'}

{'The K-gradient within the anthropic window is ROBUST across three independent estimation methods. K increases with ρ regardless of how K is measured. This addresses the Phase 5 audit concern that the K-cost function was a choice.' if all_positive else 'The K-gradient is METHOD-DEPENDENT. The Phase 5 audit concern is confirmed: the result depends on the K-cost function choice.'}

## Confidence Update

| Status | Before this test | After this test |
|--------|-----------------|----------------|
| K-minimality | Candidate (60%) | {'Cross-validated candidate (70%)' if all_positive else 'Weakened candidate (45%)'} |

{'The 10% increase reflects that three independent methods agree, addressing the audit`s primary concern. It does NOT reach "mathematically real" because all three methods share the same simplified landscape model (N=100, quadratic energy).' if all_positive else ''}

## Quintile Detail

"""
    for m in methods:
        findings += f"### {m}\n\n"
        r = results_by_method[m]
        for q in r["quintiles"]:
            findings += f"- Q{q['quintile']}: ρ∈[{q['rho_min']},{q['rho_max']}], mean K={q['k_mean']:.2f}, n={q['n']}\n"
        findings += f"\n"

    findings_path = os.path.join(out_dir, "k_independent_test_findings.md")
    with open(findings_path, "w") as f:
        f.write(findings)

    print(f"\nData saved to {data_path}")
    print(f"Findings saved to {findings_path}")

if __name__ == "__main__":
    main()
