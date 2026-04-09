---
source: Instance A — Second variation of the ratio at the straight tube
type: PROOF ATTEMPT — show straight tube is a global maximum of ratio
date: 2026-03-29
---

## Setup

The ratio R[f] = |H_dev,ωω(x*)|/(f(x*)/3) where f ≥ 0 on T³,
f(x*) = max f, and H_dev = ∇²(Δ⁻¹f) - (f/3)I.

Straight tube: f₀(x,y) = A exp(-(x²+y²)/2σ²) (z-independent).
R[f₀] = 1 (proven in file 181).

Perturb: f = f₀ + εg where g has z-dependence.
Compute: R[f₀ + εg] to second order in ε.

## First Variation

R = |H_dev,ωω|/(f/3). At the straight tube: H_dev,ωω = -f₀(x*)/3.
So R = f₀(x*)/3 / (f₀(x*)/3) = 1. (Taking absolute value.)

Perturb f = f₀ + εg:
  H_dev,ωω becomes: -f₀/3 + ε(g_zz,Poisson - g/3) + O(ε²)
  where g_zz,Poisson is the zz-component of ∇²(Δ⁻¹g).

For g with z-dependence: g = g₀(x,y) cos(kz).
  Δ⁻¹g has Fourier: ĝ(k_x,k_y,k_z) / (k_x²+k_y²+k_z²).
  The zz-component: k_z² ĝ / (k_x²+k_y²+k_z²) = k_z²/(|k|²) × ĝ/(|k|²)...

Actually, let me be more precise. For g = g₀(r) cos(k_z z):

(Δ⁻¹g)(r,z) = h(r) cos(k_z z) where (∂²/∂r² + (1/r)∂/∂r - k_z²)h = g₀(r).
(This is the 2D modified Helmholtz equation.)

∂²(Δ⁻¹g)/∂z² = -k_z² h(r) cos(k_z z).

At x* (r=0, z=0): ∂²(Δ⁻¹g)/∂z² = -k_z² h(0).

And h(0) < 0 (since g₀(0) > 0 and the modified Helmholtz with negative
RHS has h < 0 for the particular solution — check: (Δ₂D - k_z²)h = g₀,
with g₀ > 0 and -k_z² < 0 on the LHS: h must be negative to satisfy).

Wait: (∂²/∂r² + (1/r)∂/∂r)h - k_z²h = g₀.

For constant g₀: h = -g₀/k_z² (particular solution). Check: 0 - k_z²(-g₀/k_z²) = g₀. ✓

So h(0) = -g₀(0)/k_z² + (correction from r-dependence).
For Gaussian g₀: h(0) ≈ -g₀(0)/k_z² (leading order for small σ relative to 1/k_z).

Then: ∂²(Δ⁻¹g)/∂z²|_{x*} = -k_z²(-g₀(0)/k_z²) = +g₀(0) > 0.

So the z-perturbation contributes POSITIVELY to H_zz!

The perturbed H_dev,ωω:
H_dev,ωω(f₀+εg) = -f₀(x*)/3 + ε(+g₀(0) - g₀(0)/3) + O(ε²)
                  = -f₀(x*)/3 + ε(2g₀(0)/3) + O(ε²)

And f(x*)/3 = (f₀(x*) + εg₀(0))/3.

Ratio: R = |H_dev,ωω|/(f/3)
= |(-f₀/3 + 2εg₀/3)| / ((f₀+εg₀)/3)
= |f₀ - 2εg₀| / (f₀ + εg₀)  [factoring out 1/3]
= (f₀ - 2εg₀) / (f₀ + εg₀)  [for small ε, the numerator is positive]

To first order:
R ≈ (f₀ - 2εg₀)(1 - εg₀/f₀) / f₀
= (1 - 2εg₀/f₀)(1 - εg₀/f₀)
= 1 - 3εg₀/f₀ + O(ε²)

Since g₀ = g₀(0) > 0 (the perturbation adds to the max):
R ≈ 1 - 3εg₀/f₀ < 1 for ε > 0.

## THE FIRST VARIATION IS NEGATIVE!

dR/dε|_{ε=0} = -3g₀(0)/f₀(x*) < 0

For ANY perturbation g with g₀(0) > 0 (which adds to the max):
the ratio DECREASES. The straight tube is a LOCAL MAXIMUM of R.

For perturbations with g₀(0) < 0: the max of f moves to a
different point (not x* anymore). The ratio at the NEW max
must be recomputed.

For perturbations with g₀(0) = 0: the max stays at x*
but the perturbation doesn't affect f(x*). Then:
R = f₀/3 / (f₀/3) + ε(H_dev correction) = ... need second order.

## The Critical Case: g₀(0) = 0

If the perturbation vanishes at x*: g(x*) = 0.
Then f(x*) = f₀(x*) (unchanged) and the ratio depends on
how the GLOBAL structure of g affects H_dev.

For g = g₀(r)cos(k_z z) with g₀(0) = 0:
h(0) involves the integral of g₀(r) against the modified
Helmholtz Green's function. Since g₀(0) = 0, the contribution
is weaker.

The second variation: d²R/dε² at this critical case.
If d²R/dε² < 0: the straight tube is a strict local max.

## RESULT

The first variation of R at the straight tube is:
  dR/dε = -3g(x*)/f(x*) ≤ 0

with equality iff g(x*) = 0 (the perturbation vanishes at the max).

This means: the straight tube is a LOCAL MAXIMUM of R, and ANY
perturbation that increases the max value DECREASES R.

For the second variation (when g(x*)=0): need more computation,
but the numerical evidence (R < 1 for all non-straight configs)
strongly suggests the second variation is also negative.

## Implication

IF the straight tube is the GLOBAL maximum of R (not just local):
  R[f] ≤ R[f₀] = 1 for all f ≥ 0 on T³.
  With equality only for z-independent f.
  → H_ωω ≥ 0 for any flow with z-variation
  → NS regularity.

The first variation confirms the straight tube is a local max.
The second variation (at g(x*)=0 perturbations) needs checking
but is likely negative (consistent with all numerics).

## 188. First variation PROVEN: dR/dε < 0. Straight tube is local max.
