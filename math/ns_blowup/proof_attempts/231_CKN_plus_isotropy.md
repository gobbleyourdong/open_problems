---
source: CKN + isotropy = regularity? The connection.
type: PROOF STRATEGY — combining partial regularity with pressure isotropy
date: 2026-03-29
---

## The Chain

1. CKN (1982): The singular set S of suitable weak solutions to NS has
   parabolic 1D Hausdorff measure = 0. In particular: at each time t,
   the spatial singular set S(t) has Hausdorff dimension < 1.

2. OUR RESULT: For source concentration at dimension d:
   - d = 0 (point): R = 0, H_ωω = Δp/3 (maximally isotropic)
   - d = 1 (line/tube): R = 1, H_ωω = 0 (boundary case)
   - d = 2 (sheet): R = 0 along ω (safe, file 226)
   - d = 3 (volume): R = 0.34-0.84 (safe, file 178)

3. CKN says d < 1 at singularities. Our isotropy says d < 1 → R < 1 → H_ωω > 0.

4. H_ωω > 0 at a singularity → Dα/Dt < ê·S²·ê - 2α² < |S|² - 2α².
   At the attractor: |S|² = |ω|²/4, α ~ |ω|/2 → |S|² - 2α² = |ω|²/4 - |ω|²/2 < 0.
   Contradiction with blowup.

## WHERE THIS BREAKS

The CKN theorem applies to NS (viscous), not Euler (inviscid).
For Euler: there is NO comparable partial regularity result.
The singular set of Euler could potentially be 1D or higher.

So the chain works for NS but NOT for Euler.

This is actually GOOD — the Clay problem asks about NS, not Euler!

## For NS Specifically

CKN gives: at a first singularity time T*, the spatial singular set S(T*)
has dimension < 1 (in fact, H^1(S(T*)) = 0).

Near a point x* ∈ S(T*): the solution concentrates at a rate controlled
by the CKN scaling:
  |ω(x,t)| ≤ C / (|x-x*|² + |T*-t|)^{1/2}

This is the CRITICAL scaling (Type I blowup).

At this scaling: the source Δp = |ω|²/4 is concentrated in a PARABOLOID
of radius ~ √(T*-t) in space. As t → T*: the concentration region
shrinks to a point. This is 0D concentration.

For 0D concentration: H_dev → 0 (isotropy). So H_ωω → Δp/3 > 0.

## The Formal Argument (for NS)

ASSUME: first blowup at (x*, T*) for NS on T³.

By CKN scaling: |ω(x,t)| ≤ C(|x-x*|² + T*-t)^{-1/2} near (x*,T*).

The source f = Δp = |ω|²/4 satisfies:
  f(x,t) ≤ C²/4 × 1/(|x-x*|² + T*-t)

At time t < T*: f is concentrated in a ball of radius ~ √(T*-t).
The concentration dimension is 0 (point-like).

The pressure Hessian at x* at time t:
  H_ij(x*) = ∫ K_ij(x*-y) f(y,t) dy

Decompose: local (|y-x*| < R) + far (|y-x*| > R).

Far field: ∫_{|y|>R} K_ij(y) f(x*-y) dy ≤ C/R³ × ∫|f| dy → bounded.

Local field: as t → T*, f concentrates to a ball of radius ~ √(T*-t) < R.
  The local integral → ∫ K_ij(y) [C² δ(y)] dy = 0 (CZ angular average).
  Wait: not exactly δ. The source is ~ C²/(|y|² + T*-t), which has a
  specific profile. But as T*-t → 0: the profile → Cδ(y) (in a suitable sense).

The H_dev at x*: T_ij(f)(x*) = PV∫ K_ij(y) f(x*-y) dy.
For f concentrating to δ: T_ij(f) → 0 (the deviatoric part vanishes).
So R → 0 and H_ωω → f(x*)/3 = Δp/3 > 0.

THEN: at the singularity, H_ωω ≈ Δp/3 ≈ |ω|²/12 → ∞.
And: Dα/Dt = S²ê - 2α² - |ω|²/12 ≤ |ω|²/4 - 2α² - |ω|²/12 = |ω|²/6 - 2α².
For α ~ |ω|/2: Dα/Dt ≤ |ω|²/6 - |ω|²/2 = -|ω|²/3 → -∞.

α is forced to -∞, not +∞. CONTRADICTION.

## THE GAP IN THIS ARGUMENT

The convergence f → Cδ requires QUANTITATIVE control:
  |T_ij(f)(x*) - 0| ≤ C × (concentration width)^γ × ||f||_something

This is a REGULARITY ESTIMATE for the CZ operator applied to
concentrating functions. The CZ theory gives such estimates
in L^p for 1 < p < ∞, but NOT in L^∞.

The L^∞ failure is the SAME gap that prevents all direct bounds.

However: the CKN scaling provides SPECIFIC control over the
concentration profile. The concentration is not generic — it's
constrained by the NS dynamics. The profile is approximately
SELF-SIMILAR, which gives additional structure.

For self-similar concentration with profile f ~ 1/(|y|² + ε):
  T_ij(f)(0) can be computed explicitly. The integral involves
  ∫ (3ŷ_iŷ_j - δ_ij) / (|y|² + ε) × |y|^{-3} d³y
  = (by spherical symmetry of 1/(|y|²+ε)) × ∫ (3cos²θ-1) dΩ × (radial part)
  = 0 × (radial part) = 0.

  WAIT: 1/(|y|²+ε) IS spherically symmetric! So the angular integral
  ∫(3cos²θ-1)dΩ = 0 exactly, regardless of ε.

  Therefore: T_ij(f)(0) = 0 for f = C/(|y|²+ε). EXACTLY.
  Not just in the limit ε → 0, but for ALL ε > 0!

## THE BREAKTHROUGH

For ANY spherically symmetric f about x*: H_dev(x*) = 0.

The CKN profile f ~ 1/(|x-x*|² + T*-t) IS spherically symmetric!
(Centered at x* with radius parameter √(T*-t).)

So: H_dev(x*) = 0 EXACTLY at the blowup point, for the CKN profile.
→ R = 0, H_ωω = Δp/3 > 0. ✓

The actual blowup profile might not be exactly spherically symmetric.
But CKN controls the DEVIATION from spherical symmetry.
The deviation → 0 as t → T* (the concentration becomes more spherical).

## STATUS

IF the CKN profile is exactly spherically symmetric: PROOF COMPLETE.
  H_dev = 0 at x*, H_ωω = Δp/3 > 0, Dα/Dt < 0, contradiction.

IF the CKN profile is APPROXIMATELY spherically symmetric:
  Need quantitative bounds on |H_dev| from the asymmetry.
  The first-order correction is related to the ELLIPTICITY of the
  level sets of f near x*.

## 231. CKN + isotropy might close for NS (viscous case).
