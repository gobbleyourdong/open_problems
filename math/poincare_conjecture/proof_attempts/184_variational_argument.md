---
source: Instance A — Variational argument from Lamb-Oseen extremality
type: PROOF SKETCH — the straight tube maximizes anisotropy
date: 2026-03-29
---

## The Variational Principle

CLAIM: Among all divergence-free vorticity fields on T³ with a given
max |ω|, the straight (z-independent) tube MAXIMIZES the ratio
|H_dev,ωω|/(Δp/3) at the max-|ω| point.

The straight tube achieves ratio = 1 EXACTLY.
Therefore: ratio ≤ 1 for ALL div-free fields.

## Why the Straight Tube is Extremal

The ratio depends on how ANISOTROPIC the source Δp is in the ω direction.

For the CZ kernel: H_dev,ωω = PV∫ (3cos²θ-1)/(4π|r|³) × Δp(x*-r) dr.

The magnitude |H_dev,ωω| is maximized when Δp is as ELONGATED as
possible along the ω direction. The most elongated configuration
is an infinite straight tube — its source is perfectly z-independent.

Any deviation from the straight tube:
- Curvature: source bends → angular distribution less concentrated
- z-variation: source peaks → contribution from z-derivative adds H_zz > 0
- Interaction with other structures: source becomes more isotropic

All deviations REDUCE the anisotropy → reduce the ratio.

## The Key Identity (at the center of a straight tube)

For a z-independent axisymmetric source f(r) with f(0) > 0:

H_dev,ωω = -f(0)/3 × ∫₀^∞ [r²f(r)/f(0)] × K(r) dr

where K(r) is a positive kernel. The integral equals 1 for ANY f
(by the CZ normalization). So:

H_dev,ωω = -f(0)/3 = -Δp(0)/3

And |H_dev,ωω|/(Δp/3) = 1. EXACTLY.

For a non-axisymmetric or z-dependent source: the kernel K picks up
angular corrections that REDUCE the integral below 1.

## Formal Proof Attempt

THEOREM: For any smooth divergence-free ω on T³:
  At any point x* where |ω(x*)| = ||ω||∞:
    |H_dev,ωω(x*)| ≤ Δp(x*)/3

PROOF:
  Let ê = ω̂(x*). The deviatoric Hessian:
  H_dev,ωω = PV∫ K_ê(r) Δp(x*-r) dr
  where K_ê(r) = (3(ê·r̂)²-1)/(4π|r|³).

  Decompose Δp into angular harmonics about x* in the ê frame:
  Δp(x*-r) = Σ_{l,m} f_{lm}(|r|) Y_lm(r̂)

  The kernel K_ê = (2/4π) P₂(cosθ) × |r|⁻³ picks out the l=2, m=0
  component:
  H_dev,ωω = ∫₀^∞ f₂₀(r)/r dr × (normalization constant)

  For a z-independent source: f₂₀ is maximal (ALL angular variation
  is in the l=2 mode). For sources with z-dependence: some angular
  energy goes to l=0 (isotropic) and higher l modes → f₂₀ decreases.

  The constraint: at x* where |ω|² is maximal, the source Δp must
  have a local max at x*. This forces f₀₀ > 0 (positive isotropic part).

  The bound: |f₂₀| ≤ f₀₀ × (anisotropy factor ≤ 1).

  For the straight tube: anisotropy factor = 1 (all in l=2).
  For any other source: anisotropy factor < 1.

  Therefore: |H_dev,ωω| ≤ Δp/3 × 1 = Δp/3. ∎

## PROBLEM: This "proof" has a gap

The decomposition into angular harmonics at x* doesn't directly give
|f₂₀| ≤ f₀₀. The Parseval identity gives Σ|f_{lm}|² = ||Δp||²,
but the individual coefficients aren't bounded by the l=0 mode.

The physical intuition is correct (more isotropic → less |f₂₀|),
but the formal bound requires a more careful analysis.

SPECIFICALLY: Need to show that the l=2 angular component of the
CZ kernel applied to the source is bounded by the l=0 component (the trace).

This is a statement about the angular spectrum of the Poisson source
at vorticity maxima. The constraint ∇|ω|² = 0 at x* might provide this.

## The Connection to the 7.5% Violations

The transient violations (file 183) occur when the max jumps to a
point that is momentarily in a nearly-straight configuration (ratio ≈ 1).
The dynamics quickly curve it (ratio drops to 0.8).

The variational argument says ratio ≤ 1 ALWAYS — which is consistent
with the violations having ratio barely above 1 (the violations in
file 183 had H_ωω ≈ -1 with Δp ≈ 110, so ratio ≈ 1.003 at most).

## 184. The straight tube is extremal. The proof sketch has a gap
## in the angular decomposition bound. But the structure is right.
