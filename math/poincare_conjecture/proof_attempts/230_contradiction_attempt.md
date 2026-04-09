---
source: PROOF BY CONTRADICTION — blowup forces concentration forces isotropy
type: PROOF ATTEMPT — the self-defeating mechanism
date: 2026-03-29
---

## The Argument

ASSUME: blowup at finite T*. Then ||ω||∞(t) → ∞ as t → T*.

STEP 1: Blowup requires α → ∞ at the max.

  d||ω||∞/dt = α × ||ω||∞.
  For BKM blowup: ||ω||∞ ≥ C/(T*-t).
  So α = (d||ω||∞/dt)/||ω||∞ ≥ 1/(T*-t) → ∞.

STEP 2: α → ∞ requires Dα/Dt > 0 (eventually).

  Dα/Dt = S²ê - 2α² - H_ωω.
  For α → ∞: need Dα/Dt > 0, i.e., S²ê > 2α² + H_ωω.

STEP 3: Blowup concentrates the source.

  Near T*: |ω(x*)| → ∞ while |ω| remains bounded at distance > δ(t)
  from x*, where δ(t) → 0 (the "blowup core" shrinks).

  The source Δp = |ω|²/2 - |S|² ≈ |ω|²/4 (at the attractor).
  As t → T*: the source becomes concentrated in a ball of radius δ → 0,
  with amplitude → ∞. In the limit: source → (const) × δ³-function.

STEP 4: Concentration → isotropy of the pressure Hessian.

  For a POINT source f = Aδ(x-x*):
  H_dev(x*) = T_ij(Aδ)(x*) = A × PV∫ K_ij(y)δ(y)dy = 0

  because the CZ kernel K_ij has zero angular average:
  ∫_{S²} K_ij(ŷ) dΩ = ∫_{S²} (3ŷ_iŷ_j - δ_ij)/|ŷ|³ × (1/(4π)) dΩ = 0.

  So for a point source: H_dev = 0, R = 0, H_ωω = Δp/3 > 0.

  As the source CONCENTRATES toward a point: H_dev → 0 and H_ωω → Δp/3.

STEP 5: Large H_ωω prevents α growth.

  Near blowup: H_ωω ≈ Δp/3 = |ω|²/12 (from concentration + isotropy).
  And S²ê ≤ |S|² = |ω|²/4 (from the attractor).

  Dα/Dt = S²ê - 2α² - H_ωω ≤ |ω|²/4 - 2α² - |ω|²/12
         = |ω|²(1/4 - 1/12) - 2α²
         = |ω|²/6 - 2α²

  At the attractor α ~ |ω|/2: Dα/Dt ≤ |ω|²/6 - |ω|²/2 = -|ω|²/3 < 0.

  CONTRADICTION: α → ∞ requires Dα/Dt > 0, but we showed Dα/Dt < 0.

## CRITICAL ASSESSMENT — WHERE THIS BREAKS

1. Step 3 assumes the blowup concentrates to a POINT. This is plausible
   for self-similar blowup (Type I: |ω| ~ 1/(T*-t)), but not proven.
   The blowup could concentrate along a LINE (1D) instead of a point.

   For a LINE concentration: the source is a 1D object, NOT isotropic.
   The CZ kernel applied to a line source does NOT give zero H_dev.
   In fact: a straight line source gives R = 1 (the tube extremal).

   So: if blowup concentrates along a LINE → H_dev not zero → isotropy
   argument fails → H_ωω might not be large enough.

2. Step 4 uses the CZ kernel's zero angular average. This is exact for
   a point source. For a nearly-point (but still extended) source: the
   remainder depends on the shape of the concentration region.

   For a tube of width σ and length L: H_dev ~ |ω|²σ²/L² (scaling).
   As σ → 0 with L fixed: H_dev → 0. ✓
   But if L → 0 too (both shrinking): H_dev stays O(1).

3. Step 5 uses the attractor |ω|²/|S|² = 4 AND α ~ |ω|/2.
   Near blowup: the attractor might not hold. The attractor was measured
   at moderate |ω| (up to 40). At |ω| → ∞: who knows?

## WHERE THE ARGUMENT IS STRONG

- Steps 1-2 are rigorous (BKM + Riccati identity).
- Step 4 for POINT concentration is rigorous (CZ angular average = 0).
- Step 5 arithmetic is correct given the assumptions.
- The PHYSICAL picture is clear: concentration → isotropy → compression.

## WHERE IT NEEDS WORK

- Step 3: prove blowup concentrates (at least partially — needs to show
  the concentration region shrinks faster in the ê-direction than
  perpendicular, which would give isotropy in the ê-Hessian).
- Step 4: quantify the rate of isotropy convergence for NEAR-point sources.
- Step 5: verify the attractor holds near blowup.

## THE KEY INSIGHT

The self-defeating mechanism:
  blowup → concentration → isotropy → H_ωω > 0 → compression → no blowup

This is a TOPOLOGICAL obstruction: the flow cannot concentrate without
creating the pressure feedback that prevents further concentration.

## RELATION TO CKN

Caffarelli-Kohn-Nirenberg (1982) proved: the 1D Hausdorff measure of
the singular set is zero. This means blowup, if it happens, concentrates
to LESS than 1D (a set of points, not lines).

If the singular set is 0D (isolated points): our Step 4 applies directly!
Point concentration → isotropy → H_ωω > 0 → contradiction.

CKN gives: singular set has H^1 = 0 (parabolic 1D Hausdorff measure zero).
This is ALMOST what we need. If we could improve to spatial 0D
(the singular set is contained in a set of spatial dimension < 1):
the isotropy argument closes.

## 230. The contradiction argument is structurally sound.
## The gap: prove the concentration is point-like (use CKN?).
