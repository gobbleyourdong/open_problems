# Frequency Function N(r) on Burgers Vortex — Phase 1 Result

**Date:** 2026-04-09
**Script:** `numerics/frequency_function.py`
**Track:** Numerical

## The Frequency Function

  N(r) = r · D(r) / H(r)
  D(r) = ∫_{B_r} |∇u|² dV
  H(r) = ∫_{∂B_r} |u|² dS

For harmonic functions: N(r) = degree of the polynomial (constant).
For bounded harmonic: N(r) ≤ 0 → u = const (classical Liouville).

## Result on Burgers Vortex (α = Γ = ν = 1)

| R | D(R) | H(R) | N(R) | monotone? |
|---|------|------|------|-----------|
| 0.5 | 0.793 | 0.397 | 0.9997 | — |
| 1.0 | 6.331 | 6.332 | 0.9998 | YES |
| 1.5 | 21.33 | 32.00 | 1.0001 | YES |
| 2.0 | 50.51 | 100.97 | 1.0005 | YES |
| 3.0 | 170.25 | 510.39 | **1.0007** (peak) | YES |
| 4.0 | 403.29 | 1612.33 | 1.0005 | **NO** |
| 5.0 | 787.39 | 3935.69 | 1.0003 | **NO** |

**N(r) is remarkably close to 1** (range 0.9997 to 1.0007) but
NOT monotone — it peaks at R ≈ 3 and then decreases slightly.

## Interpretation

### N(r) ≈ 1 means the Burgers vortex behaves like a degree-1 harmonic function

The dominant component u_z = αz is degree-1 (linear in z), so N(r) ≈ 1
is expected. The small deviations from 1 come from the vortical component
u_θ (which is NOT a harmonic function).

### Non-monotonicity is TINY but REAL

The peak-to-tail drop: N(3) − N(5) = 0.0004. This is the NS nonlinearity
manifesting in the frequency function. For the Liouville problem:
- Even on a simple explicit 3D NS solution, Almgren monotonicity fails
- The failure is small (< 0.05%) but exists at all radii > R_peak
- A MODIFIED frequency function would need to correct this by ~0.0004

### What this means for Mountain 1

The gap.md says: "the error term is O(M · r² · D(r))." On Burgers:
- M ≈ ∞ (unbounded), but the error is still tiny
- This is because the Burgers vortex is "almost harmonic" — the nonlinear
  part of the velocity is exponentially localized near the core

For a hypothetical BOUNDED ancient solution with |u| ≤ M:
- The error would be O(M · r² · D(r))
- At large r, D(r) ~ r³ (volume growth), so error ~ M · r⁵
- The good term in dN/dr is ~ r · D'(r) ~ r⁴
- So error/good ~ M · r → ∞ for large r
- This confirms the gap.md prediction: for large M, the error dominates

## For the Theory Track

This numerics shows:
1. N(r) ≈ constant even on a non-harmonic NS solution (good news)
2. But non-monotonicity exists (bad news for the direct Almgren approach)
3. The deviation is localized near the vortex core (r ≈ 3)
4. A PRESSURE-WEIGHTED frequency function might fix this (gap.md suggestion)

**Next numerical priority**: compute the frequency function with
pressure-weighted integrals to see if the non-monotonicity disappears.
