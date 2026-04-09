---
source: TWO-SIGN PROOF — DVar < 0 AND DH > 0 gives DQ < 0 automatically
type: PROOF STRUCTURE — if both signs hold, the attractor follows
file: 283
date: 2026-03-29
---

## The Key Decomposition

Q = Var - H_ωω  (where Var = ê·S²·ê - α²)

DQ/Dt = DVar/Dt - DH_ωω/Dt

If DVar/Dt < 0 AND DH_ωω/Dt > 0:
  DQ/Dt = (negative) - (positive) < 0.  ∎

No comparison needed between magnitudes! The signs alone suffice.

## Claim 1: DVar/Dt < 0 (Eigenvector Tilting)

Var = Σλᵢ²cᵢ - (Σλᵢcᵢ)² measures alignment spread.

The -Ω² = (1/4)(ωω^T - |ω|²I) term in the strain equation:
  DS/Dt = -S² - Ω² - H

The -Ω² term has eigenvalue 0 along ω and -|ω|²/4 perpendicular.
This COMPRESSES strain in the ⊥ω direction while leaving the
ω-direction unchanged.

Effect on eigenvectors: they ROTATE toward ω alignment
(file 154: e₃ rotates toward ω at 85-90% of dc₃/dt).

Effect on Var: as ω approaches an eigenvector, Var → 0.
The approach is MONOTONIC when the -Ω² term dominates (which it
does — it's O(|ω|²) while -S² is O(|S|²) = O(|ω|²/4)).

MEASURED: file 173, TILT (= eigenvalue × alignment rate) dominates
eigenvalue changes by 15:1 at the max. The TILT is negative (reducing α).
DVar/Dt tracks with the TILT (both depend on alignment change rate).

FORMAL STATUS: DVar/Dt < 0 at the max is MEASURED (100% between
jumps from file 173 data). The MECHANISM (-Ω² dominates) is identified
but not formally proven (need to show the -S² and -H terms don't
overcome -Ω² in the variance evolution).

## Claim 2: DH_ωω/Dt > 0 (Non-Local Pressure Growth)

H_ωω = ∫ K_ê(x*-y) Δp(y) dy (CZ integral)

DH_ωω/Dt ≈ ∫ K_ê(x*-y) D(Δp)(y)/Dt dy  (plus kernel motion terms)

D(Δp)/Dt = D(|ω|²/2 - |S|²)/Dt = |ω|²α - (strain terms)

The LEADING term: ∫ K_ê(y) |ω(y)|²α(y) dy.

This integral has the SAME sign structure as H_ωω itself (same kernel K_ê).
If the source |ω|²α has the SAME spatial pattern as |ω|²
(which it does when α is spatially correlated with |ω|):
then DH_ωω/Dt has the SAME sign as H_ωω.

Since H_ωω > 0 (Fourier lemma): DH_ωω/Dt > 0 when α > 0 at the max.

MORE PRECISELY: the z-Fourier decomposition.
DH_ωω/Dt gets a contribution from each z-mode:
  Dk²|p_k|/Dt = k² D|p_k|/Dt = k² |D[(Δ_xy-k²)⁻¹ f_k]/Dt|

Since (Δ_xy-k²)⁻¹ is a fixed operator:
  D|p_k|/Dt = |(Δ_xy-k²)⁻¹ Df_k/Dt|

If Df_k/Dt > 0 at the max (the z-variation of the source INCREASES):
  D|p_k|/Dt > 0 (by the same negative-definite argument as the Fourier lemma).

Df_k/Dt > 0: the z-Fourier component of D(Δp)/Dt is positive at (x₀,y₀).
This holds when the stretching α > 0 creates MORE z-variation
(from the (ω·∇)u term generating ⊥ω vorticity with z-structure, file 151).

FORMAL STATUS: DH_ωω/Dt > 0 when α > 0 is MEASURED (DH_ωω ≈ +326
at the max, file 274). The mechanism (stretching creates z-variation →
Fourier lemma applied to Df/Dt) is identified.

The formal proof requires: show D(Δp)_k/Dt > 0 at the max from α > 0.
This is a DYNAMIC version of the Fourier lemma: the TIME DERIVATIVE
of the source z-component is positive when stretching is positive.

## The Proof Chain (if both claims hold)

1. α > 0 at the max (stretching case — the only case that matters)
2. DVar/Dt < 0 (eigenvector tilting, Claim 1)
3. DH_ωω/Dt > 0 (non-local pressure growth, Claim 2)
4. DQ/Dt = DVar/Dt - DH_ωω/Dt < 0 (both signs contribute negatively)
5. Q attracted to Q < 0
6. Q < 0 → Dα/Dt = Q - α² < -α²
7. α ≤ α₀/(1+α₀t) → bounded
8. ||ω||∞(t) ≤ ||ω||₀(1+α₀t) → linear growth
9. BKM: ∫||ω||∞ dt < ∞ → REGULARITY ∎

## Remaining Formal Gaps

CLAIM 1 GAP: Prove DVar/Dt < 0 at the max from the -Ω² dominance.
  Need: the -Ω² contribution to the variance evolution exceeds
  the -S² and -H contributions. Scaling: -Ω² is O(|ω|²) while
  -S² is O(|S|²) = O(|ω|²/4). Factor 4 margin in the leading term.

CLAIM 2 GAP: Prove DH_ωω/Dt > 0 at the max when α > 0.
  Need: the dynamic Fourier lemma — the z-variation of the source
  increases when stretching is positive. This follows from the
  vorticity stretching creating ⊥ω modes with z-structure (file 151).
  But the QUANTITATIVE bound (that the z-component of Df/Dt is
  positive at (x₀,y₀)) requires the dynamic Green's function argument.

## 283. The TWO-SIGN structure makes DQ < 0 automatic.
## Two claims needed: DVar < 0 and DH > 0. Both measured. Both need proof.
