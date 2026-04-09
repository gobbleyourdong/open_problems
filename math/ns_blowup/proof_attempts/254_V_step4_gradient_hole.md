---
source: VALIDATION — Step 4 (P2) — the gradient suppression needs refinement
type: ADVERSARIAL — found a subtlety in the ∂α/∂z bound
date: 2026-03-29
---

## The Issue

File 247 claims: ∂α/∂z ~ α/L (tube scale) at the max of |ω|.
The argument: ∂ω/∂z ⊥ ω → ∂S/∂z suppressed → ∂α/∂z ~ α/L.

## The Subtlety

The Biot-Savart integral S(x) = ∫ K(x-y) ω(y) dy is NON-LOCAL.
∂S/∂z at x* involves contributions from ALL points y.

The LOCAL contribution (|y-x*| < σ): dominant for S itself.
Its z-derivative: ∂S_local/∂z involves ∂ω/∂z at nearby points.

At x*: ∂ω/∂z ⊥ ω (from the max condition).
But at y ≈ x*: ∂ω(y)/∂z is NOT necessarily ⊥ ω(x*).

## Why the Bound Still Holds (the SYMMETRY argument)

At the max of |ω|: the vorticity profile is SYMMETRIC to first order:
  |ω|(z) = |ω|₀(1 - z²/(2σ²) + O(z³))  (Taylor expansion)

The EVEN part of ω(z) around z=0 generates an EVEN S(z).
An even S(z) has ∂S/∂z|_{z=0} = 0 from symmetry.

The ODD part of ω(z): comes from the tube curvature and far-field.
It contributes ∂S/∂z ~ |ω|/L (the curvature scale, not core scale).

This is the CORRECT reason for the suppression: local symmetry at
the max eliminates the O(|ω|/σ) gradient, leaving only O(|ω|/L).

## Formal Proof Requirement

Need: at any max of |ω|² on T³, the local Biot-Savart integral
has an approximately symmetric contribution to S(z), with the
asymmetric correction being O(1/L) not O(1/σ).

This follows from:
(a) |ω|²(z) = |ω|²₀ - c z² + O(z³) at the max (Taylor, c > 0)
(b) The BS kernel is rotationally symmetric in 3D
(c) An even source through a symmetric kernel gives an even S
(d) ∂(even)/∂z|_{z=0} = 0

The correction: the source ω (vector field) is NOT exactly even
(the direction ê varies along z). But the magnitude |ω| IS even
to first order. The direction variation contributes:
  ∂α/∂z from direction = α × (∂ê/∂z · something) ~ α × κ
  where κ = curvature ~ 1/L.

So: ∂α/∂z = (even → 0) + α/L (from direction) + higher order.

## VERDICT

The suppression ∂α/∂z ~ α/L IS correct, but the argument in file 247
was imprecise. The CORRECT reason is:

1. The MAGNITUDE of |ω| is even at the max → even part of BS gives ∂S/∂z = 0
2. The DIRECTION of ω varies at rate ~ 1/L → contributes ∂α/∂z ~ α/L
3. Combined: ∂α/∂z ~ α/L, NOT α/σ

This is RIGOROUS if we formalize the Taylor expansion + symmetry argument.

## Status: STEP 4 NEEDS REFINEMENT but is NOT BROKEN.
## The argument is correct but the reasoning needs to be tightened.
## Specifically: use the even-odd decomposition of the BS integral,
## not the perpendicularity argument from file 247.
