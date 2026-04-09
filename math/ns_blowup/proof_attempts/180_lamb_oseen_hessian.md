---
source: Instance A — Lamb-Oseen vortex pressure Hessian (analytical)
type: PROOF ATTEMPT A3 — exact computation for the simplest case
date: 2026-03-29
---

## Setup: Lamb-Oseen Vortex on T³

Axisymmetric Gaussian vortex tube along z-axis:
  ω = (0, 0, ω₀ exp(-r²/2σ²))  where r² = x² + y²

On T³ (periodic): approximate as valid when σ << 2π.

Velocity (Biot-Savart, cylindrical):
  u_θ(r) = (Γ/2πr)(1 - exp(-r²/2σ²))  where Γ = 2πσ²ω₀

Strain tensor in cylindrical:
  S_rr = ∂u_r/∂r = 0  (no radial velocity for axisymmetric)
  S_θθ = u_r/r = 0
  S_rθ = (1/2)(∂u_θ/∂r - u_θ/r) = (1/2)r∂(u_θ/r)/∂r

Compute: u_θ/r = (Γ/2πr²)(1 - exp(-r²/2σ²))
∂(u_θ/r)/∂r = -(Γ/πr³)(1 - exp(-r²/2σ²)) + (Γ/2πr²)(r/σ²)exp(-r²/2σ²)

At r = 0 (center of tube):
  u_θ/r → ω₀/2 (solid body rotation)
  ∂(u_θ/r)/∂r → 0 (by L'Hôpital)
  So S_rθ(0) = 0.

Therefore: |S(0)| = 0 at the center of a Lamb-Oseen vortex!
And |ω(0)| = ω₀ (maximum).

## Pressure at the center

Δp = |ω|²/2 - |S|² = ω₀²/2 - 0 = ω₀²/2 at r=0.

The pressure source Δp(r) = |ω(r)|²/2 - |S(r)|²
  = ω₀² exp(-r²/σ²)/2 - |S(r)|²

Near r = 0: |S| ~ r²/σ⁴ × something (goes to zero as r² at center).
So Δp(r) ≈ ω₀² exp(-r²/σ²)/2 near the center (positive, Gaussian).

## Pressure Hessian at the center

For an axisymmetric source Δp(r,z) on T³:
  p(0) = ∫ G(y) Δp(y) dy where G is the Green's function.

The Hessian: H_ij(0) = ∫ ∂²G/∂y_i∂y_j × Δp(y) dy

For the Lamb-Oseen vortex (independent of z):
The source is 2D (cylindrically symmetric): Δp = Δp(r) only.

By symmetry at r = 0:
  H_xx = H_yy (by rotational symmetry in xy)
  H_zz = different (no z-dependence → H_zz from the 3D Poisson)
  H_xy = H_xz = H_yz = 0

The trace: H_xx + H_yy + H_zz = Δp(0) = ω₀²/2.
By symmetry: 2H_xx + H_zz = ω₀²/2.

Now: ω = (0, 0, ω₀), so ê = (0, 0, 1).
H_ωω = H_zz.

## Computing H_zz

For a source independent of z: Δp(x,y,z) = Δp(r) = f(r).

The 3D Poisson: ∇²p = f(r). Since f doesn't depend on z:
  ∂²p/∂x² + ∂²p/∂y² + ∂²p/∂z² = f(r)

If p also doesn't depend on z: ∂²p/∂z² = 0 → H_zz = 0.
Then: ∂²p/∂x² + ∂²p/∂y² = f(r) (2D Poisson).

But wait — on T³, the solution MUST be periodic in z.
If f doesn't depend on z, then p doesn't depend on z (the z-modes
all vanish except k_z = 0). So H_zz = 0.

Therefore: H_ωω = H_zz = 0 for a straight, z-independent tube!

And: tr(H) = ω₀²/2, so H_xx = H_yy = ω₀²/4.
H_iso = ω₀²/6.
H_dev,ωω = H_zz - tr(H)/3 = 0 - ω₀²/6 = -ω₀²/6.

Ratio = |H_dev,ωω|/(Δp/3) = (ω₀²/6)/(ω₀²/6) = 1.000 exactly!

## THE STRAIGHT TUBE SITS EXACTLY ON THE BOUNDARY!

For a perfectly straight, infinite (z-independent) Lamb-Oseen vortex:
  Ratio = |H_dev,ωω|/(Δp/3) = 1.0 EXACTLY.

This is the WORST CASE. Any deviation from the straight tube
(curvature, z-variation, interaction with other structures) will
reduce the ratio below 1.

## Why curvature helps

For a curved tube: the source has z-dependence → H_zz ≠ 0.
Specifically, curvature creates a nonzero k_z component → H_zz > 0.
This pushes the ratio below 1.

The trefoil (ratio 0.84) has significant curvature → 16% below 1.
TG (ratio 0.34) is volume-filling → 66% below 1.

## The Proof Strategy

1. STRAIGHT TUBE: ratio = 1 exactly (marginal case)
2. ANY PERTURBATION (curvature, interaction, z-variation): ratio < 1
3. Smooth solutions on T³ CANNOT maintain a perfectly straight,
   z-independent tube forever (the dynamics create z-variation)
4. Therefore: ratio < 1 for all evolved Euler solutions on T³

Step 3 is the key: a straight tube on T³ is UNSTABLE.
The Crow instability (1970) makes straight vortex tubes develop
z-periodic perturbations. These perturbations create H_zz > 0 → ratio < 1.

## PROBLEM WITH THIS ARGUMENT

At t = 0: the IC COULD be a straight tube (ratio = 1 exactly).
The argument needs: ratio < 1 for t > 0 (after dynamics develop).

But at t = 0: α = 0 for a straight tube (S = 0 at the center).
So even though ratio = 1, there's no stretching → no blowup danger.

The danger is ONLY when α > 0. And α > 0 requires strain,
which requires z-variation or interaction, which reduces the ratio < 1.

## FORMALIZATION

CLAIM: For any smooth solution to 3D Euler on T³ with ω ≠ 0:
  At any point x* where |ω(x*)| = ||ω||∞ AND α(x*) > 0:
    |H_dev,ωω(x*)| < Δp(x*)/3

PROOF SKETCH:
  α > 0 requires nonzero strain at x*: |S(x*)| > 0.
  Nonzero strain requires the flow to deviate from solid-body rotation.
  This deviation creates z-variation in ω (or more generally, variation
  along the ω direction).
  This variation makes H_ωω = H_zz > 0 (positive contribution along ω).
  The positive H_zz reduces |H_dev,ωω| below Δp/3.

  Quantitatively: H_zz ≈ C × (variation along ω) × Δp.
  And α > 0 requires sufficient strain, which requires sufficient variation.
  The two are LINKED through the NS equations.

## 180. The straight tube is the worst case at ratio = 1 exactly.
## Any dynamics reduce it below 1. The proof needs to quantify this.
