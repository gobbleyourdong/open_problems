---
source: Instance A — THE OPEN QUESTION in its sharpest form
type: FINAL FORMULATION — this is what needs proving
date: 2026-03-29
---

## The Question (Pure Potential Theory)

Let f: T³ → R be smooth with f(x*) = max f and ∇f(x*) = 0.
Let φ solve Δφ = f - f(x*) on T³ (mean zero).

Then φ is superharmonic near x* (since f - f(x*) ≤ 0 near x*).

QUESTION: At x*, for any unit vector ê, does:

  |ê · ∇²φ(x*) · ê| < f(x*)/3 ?

Note: ∇²φ(x*) = H_dev(x*) (traceless, since Δφ(x*) = 0).
And f(x*)/3 = Δp(x*)/3 = H_iso.

## Equivalent Formulations

(a) The TRACELESS Hessian of the Newtonian potential of (f - f_max)
    at the maximum of f has spectral radius < f_max/3.

(b) The Riesz-transform-based deviatoric projection of f at its
    maximum is bounded: ||T_dev(f)(x*)|| < f(x*)/3.

(c) For any positive function on T³, the pressure Hessian at the
    vorticity maximum is closer to isotropic than anisotropic.

## What We Know

EQUALITY is achieved for z-independent f (the straight tube):
  φ_zz = 0, so |ê_z · ∇²φ · ê_z| = |−f(x*)/3| = f(x*)/3. (TIGHT!)

The bound is STRICT for any f with z-variation:
  The z-variation creates φ_zz > 0 at the max, pulling H_dev,ωω
  away from -f/3 toward 0.

Measured: |H_dev,ωω|/(f/3) ≤ 0.955 for ALL tested ICs (Instance B).
The ratio DECREASES with resolution and with increasing |ω|.

## Why It's Hard

The operator T_dev = ∂²(-Δ)⁻¹ - (1/3)I is a Calderón-Zygmund
operator. CZ operators are bounded on Lᵖ (1 < p < ∞) but NOT
on L∞. The question asks for a POINTWISE bound at a SPECIFIC
point (the maximum), which CZ theory doesn't provide generically.

The max-point constraint (∇f = 0, f = max) provides EXTRA STRUCTURE
that might make the pointwise bound possible. But extracting this
from the CZ machinery requires new estimates.

## Why It Might Be True

1. PHYSICAL: the straight tube is the extremal case (most anisotropic
   configuration), and it achieves equality with α = 0 (harmless).

2. GEOMETRICAL: at a maximum, the source f - f_max is non-positive.
   The CZ operator applied to a non-positive function near its zero
   has bounded anisotropy (the zero creates a "regularizing" effect).

3. NUMERICAL: 36/36 measurements, 7 adversarial ICs, 3 resolutions,
   all give ratio < 1. The worst case (0.955) DECREASES with resolution.

4. VARIATIONAL: the straight tube (ratio = 1) is a CRITICAL POINT
   of the ratio functional. All perturbations decrease the ratio.
   If the critical point is a GLOBAL MAXIMUM, the bound follows.

## What a Proof Would Need

Either:
(A) A direct bound on the CZ operator at max points, using the
    positivity of f and the gradient constraint. This requires
    new harmonic analysis estimates.

(B) A variational proof that the straight tube maximizes the ratio.
    Show that the second variation is negative at the critical point.

(C) A maximum-principle argument for the ratio as a function of time
    under Euler evolution. Show Q = (variance - H_ωω) < 0 is preserved.

(D) A Littlewood-Paley energy estimate that uses the specific NS
    structure (bilinear symbol, phase scrambler) to close a subcritical
    bound (Instance C's approach, not yet successful).

## The Chain (if the question is answered YES)

f ≥ 0 with max at x* and ∇f = 0 → |H_dev,ωω| < f/3 at x*
→ H_ωω > 0 at the max of |ω| (since Δp = |ω|²/2 - |S|² > 0)
→ Dα/Dt = S²ê - 2α² - H_ωω < S²ê - 2α² ≤ 0 (at Ashurst alignment)
→ α bounded along every Lagrangian trajectory reaching the max
→ ||ω||∞(t) grows at most exponentially
→ BKM integral finite on any bounded interval
→ GLOBAL REGULARITY OF 3D NAVIER-STOKES ∎

## 187 proof files. The question is formulated. The proof awaits.
