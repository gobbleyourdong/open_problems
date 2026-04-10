"""
Montgomery's pair correlation conjecture for ζ-zeros.

Montgomery (1973): under RH, the pair correlation function of normalized
imaginary parts of ζ-zeros equals the GUE (Gaussian Unitary Ensemble)
pair correlation:
    R_2(x) = 1 - (sin(π x) / (π x))²

Equivalently, the nearest-neighbor spacing distribution should follow the
Wigner surmise (an approximation to the exact GUE result):
    P(s) = (32 / π²) · s² · exp(-4 s² / π)

This is one of the deepest connections in modern mathematics — connecting
Riemann zeros to eigenvalues of random Hermitian matrices. It is partially
proven (Montgomery's theorem covers a smooth class of test functions) and
fully verified numerically by Odlyzko at γ ~ 10²⁰ to extreme precision.

This script verifies it using the 500 zeros cached from von_mangoldt_NT.py.
At low γ ~ 100-1000, the GUE statistics should already be visible, though
with sample-size noise from only ~500 zeros.

NORMALIZATION (Riemann-von Mangoldt):
    Density of zeros at height γ ≈ (1/(2π)) · log(γ / (2π))
    So normalized zeros: w_n = γ_n · (1/(2π)) · log(γ_n / (2π))
                       = θ(γ_n)/π + 1   (essentially)
After normalization, ⟨w_{n+1} - w_n⟩ ≈ 1, allowing direct comparison
with the universal GUE statistics.
"""
import numpy as np
import json
import os
import mpmath
from math import pi, log, exp


def load_zeros(path='/tmp/rh_zeros_NT.json'):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Cached zeros not found at {path}. "
                                f"Run von_mangoldt_NT.py first to generate.")
    with open(path, 'r') as f:
        return [float(g) for g in json.load(f)]


def normalize_zeros(gammas):
    """Unfold zeros using Riemann-Siegel theta:
        w_n = θ(γ_n)/π + 1 = N_smooth(γ_n)
    This gives mean spacing exactly 1 since N(γ_n) = n + S(γ_n) and the
    smooth part is monotone with the right local rate."""
    return np.array([float(mpmath.siegeltheta(g)) / pi + 1 for g in gammas])


def wigner_surmise_GUE(s):
    """Nearest-neighbor spacing distribution for GUE (Wigner surmise)."""
    return (32 / pi ** 2) * s ** 2 * np.exp(-4 * s ** 2 / pi)


def poisson_density(s):
    """Density for an uncorrelated Poisson process (for comparison)."""
    return np.exp(-s)


def gue_pair_correlation(x):
    """GUE pair correlation function R_2(x) = 1 - (sin πx / πx)²."""
    px = pi * x
    sinc = np.where(np.abs(px) < 1e-12, 1.0, np.sin(px) / px)
    return 1.0 - sinc ** 2


def main():
    print("Montgomery's pair correlation conjecture")
    print("=" * 76)

    gammas = load_zeros()
    print(f"Loaded {len(gammas)} ζ zeros")
    print(f"  γ_1 = {gammas[0]:.6f}")
    print(f"  γ_500 = {gammas[-1]:.6f}")
    print()

    w = normalize_zeros(gammas)
    print(f"After normalization w_n = γ_n/(2π) · log(γ_n/(2π)):")
    print(f"  w_1 = {w[0]:.6f}")
    print(f"  w_500 = {w[-1]:.6f}")
    print(f"  ⟨w_{{n+1}} - w_n⟩ = {(w[-1] - w[0]) / (len(w) - 1):.6f}  (should ≈ 1)")
    print()

    # Nearest-neighbor spacings
    spacings = np.diff(w)
    print(f"Nearest-neighbor spacings: {len(spacings)} values")
    print(f"  mean = {spacings.mean():.6f}  (should ≈ 1)")
    print(f"  std  = {spacings.std():.6f}")
    print(f"  min  = {spacings.min():.6f}")
    print(f"  max  = {spacings.max():.6f}")
    print()

    # Histogram of spacings vs GUE Wigner surmise vs Poisson
    print("Nearest-neighbor distribution histogram (GUE vs observed vs Poisson):")
    bins = np.arange(0, 3.05, 0.15)
    counts, _ = np.histogram(spacings, bins=bins)
    bin_centers = (bins[:-1] + bins[1:]) / 2
    bin_width = bins[1] - bins[0]
    obs_density = counts / (counts.sum() * bin_width)
    gue_density = wigner_surmise_GUE(bin_centers)
    poi_density = poisson_density(bin_centers)
    print(f"{'s':>6} {'GUE':>10} {'observed':>10} {'Poisson':>10} {'count':>8}")
    print("-" * 50)
    for i, s in enumerate(bin_centers):
        bar_obs = "█" * int(obs_density[i] * 20)
        print(f"{s:>6.2f} {gue_density[i]:>10.4f} {obs_density[i]:>10.4f} "
              f"{poi_density[i]:>10.4f} {counts[i]:>8}  {bar_obs}")

    # KS-style comparison: integrate squared deviation
    chi2_gue = np.sum((obs_density - gue_density) ** 2 * bin_width)
    chi2_poi = np.sum((obs_density - poi_density) ** 2 * bin_width)
    print()
    print(f"Integrated squared deviation (GUE):     {chi2_gue:.6f}")
    print(f"Integrated squared deviation (Poisson): {chi2_poi:.6f}")
    if chi2_gue < chi2_poi:
        print(f"GUE fits {chi2_poi / chi2_gue:.1f}× better than Poisson.")
    print()

    # Pair correlation R_2(x): proportion of pairs (n, m) with w_n - w_m in (x, x+dx)
    print("Pair correlation R_2(x):")
    print("Counting pairs (i, j) with j > i and (w_j - w_i) in each bin")
    print()
    diffs = []
    for i in range(len(w)):
        for j in range(i + 1, min(i + 30, len(w))):
            d = w[j] - w[i]
            if d <= 5.0:
                diffs.append(d)
    diffs = np.array(diffs)
    print(f"  Total pairs collected (within 5 mean spacings): {len(diffs)}")

    bins2 = np.arange(0, 5.05, 0.2)
    counts2, _ = np.histogram(diffs, bins=bins2)
    bin_centers2 = (bins2[:-1] + bins2[1:]) / 2
    bin_width2 = bins2[1] - bins2[0]
    # Normalization: density of pairs at distance x is (n_pairs / total length) × ?
    # For a process with mean spacing 1, R_2(x) = (density of pairs at sep x) / (density at sep ∞)
    # Density at sep ∞ ≈ 1 (in normalized units)
    # We want: counts2 / (n × bin_width2 × 1) where n is the number of base zeros
    # But pairs (i, j) with j > i: n_pairs ≈ n × density × bin_width per bin
    n_zeros = len(w)
    expected_uniform = n_zeros * bin_width2  # for each bin, naïve uniform rate
    # However we restricted to j ∈ [i+1, i+30], so we need to correct:
    # this captures spacings up to ~30 mean units, which includes everything < 5
    obs_R2 = counts2 / expected_uniform
    gue_R2 = gue_pair_correlation(bin_centers2)

    print(f"{'x':>6} {'GUE R_2(x)':>12} {'observed':>12} {'count':>8}")
    print("-" * 44)
    for i, x in enumerate(bin_centers2):
        print(f"{x:>6.2f} {gue_R2[i]:>12.4f} {obs_R2[i]:>12.4f} {counts2[i]:>8}")

    # The key feature: R_2(0) = 0 for GUE (level repulsion)
    # vs R_2(0) = 1 for Poisson (no repulsion)
    print()
    print("KEY DIAGNOSTIC: R_2 near 0")
    print(f"  obs R_2(0.1) = {obs_R2[0]:.4f}")
    print(f"  GUE pred     = {gue_R2[0]:.4f} (level repulsion → 0)")
    print(f"  Poisson pred = 1.0000 (no repulsion)")
    print()

    if obs_R2[0] < 0.5:
        print("✓ Observed shows GUE-like LEVEL REPULSION at small spacings.")
        print("  Riemann zeros do NOT act like a Poisson point process.")
    else:
        print("✗ Level repulsion not visible at this sample size.")


if __name__ == '__main__':
    main()
