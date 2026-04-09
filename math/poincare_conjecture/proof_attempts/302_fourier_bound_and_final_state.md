---
source: FOURIER PER-MODE BOUND + FINAL STATE OF THE PROOF
type: DEFINITIVE — where we stand after 302 files
date: 2026-03-29
---

## THE PER-MODE BOUND (NEW, PROVEN)

LEMMA: For each Fourier mode k of a divergence-free field ω on T³:
  |α̂(k)| ≤ |ω̂(k)|/2

PROOF: α̂(k) = (k·ê)((k×ω̂)·ê)/|k|². Div-free: ω̂ ⊥ k → |k×ω̂| = |k||ω̂|.
Then: |α̂| ≤ |k·ê|×|k||ω̂|/(|k|²) = cos(θ)sin(θ)|ω̂| = sin(2θ)/2 × |ω̂| ≤ |ω̂|/2.
Equality iff θ = π/4 (mode at 45° to vorticity) and ω̂ fully transverse. ∎

NUMERICALLY: confirmed zero violations across 48 samples, 8 ICs, 6 timesteps.

## WHAT THE PER-MODE BOUND GIVES AND DOESN'T GIVE

GIVES: α = Σ α̂(k)e^{ikx*} ≤ Σ|α̂| ≤ Σ|ω̂|/2. Combined with |ω| ≤ Σ|ω̂|:
  α/|ω| ≤ (Σ|ω̂|/2)/(|Σω̂e^{ikx*}|) which can exceed 1/2.

DOESN'T GIVE: α < |ω|/2 (the denominator can be smaller than the numerator)

For a SINGLE mode at θ = π/4: α/|ω| = 1/2 exactly (bound saturated).
For MULTIPLE modes: α/|ω| < 1/2 empirically (angular spread causes cancellation).
The gap: proving that NS dynamics generates sufficient angular spread.

## THE ORTHOGONAL SUBSPACE STRUCTURE

KEY INSIGHT (from the Fourier analysis):

Each mode ω̂(k) decomposes into PARALLEL (ω̂·ê) and TRANSVERSE (ω̂_⊥) parts.
- |ω(x*)| depends on ALL of ω̂ (both parallel and transverse)
- α(x*) depends ONLY on the transverse ω̂_⊥ at angles ~45° to ê
- They compete for the same Fourier energy budget ||ω̂||²

Modes at θ ≈ 0 (k parallel to ê): contribute to |ω| but NOT to α
Modes at θ ≈ π/4 (45°): contribute equally to both
Modes at θ ≈ π/2 (k perpendicular to ê): contribute to |ω| but NOT to α

For α/|ω| to approach 1/2: need ALL Fourier energy at θ = π/4.
On the integer lattice Z³: this is impossible for most directions ê.
The lattice structure FORCES angular spread.

CONJECTURE: For a divergence-free field on T³ with ||ω||_{H^s} < ∞ (s > 3/2):
  α(x*) < |ω(x*)|/2 - δ(s) where δ(s) > 0 depends on the smoothness.

This is an arithmetic geometry result about CZ operators on the integer lattice.
The proof likely involves the distribution of lattice points near the 45° cone.

## COMPLETE PROOF STATE (302 FILES)

### PROVEN UNCONDITIONALLY:
1. H_ωω > 0 at the max of |ω| when α > 0 (Fourier lemma, file 267)
2. Q = -H_ωω < 0 when c₁ = 1 (algebraic, file 258)
3. D²α < 2α³ at Q = 0 for α < 0.445|ω| (eigenvalue cubic, file 299)
4. |α̂(k)| ≤ |ω̂(k)|/2 per mode (geometric, this file)
5. Q < 0 → Riccati → α bounded → BKM → regularity (standard)
6. Type I blowup impossible for NS (Seregin 2012)
7. -Ω² coefficient = 1/4 exactly (gives |ω|²/|S|² = 4 attractor ODE)
8. -S² is diagonal in eigenbasis (no eigenvector rotation, file 286)

### PROVEN FOR NS (NOT EULER):
9. If α ≤ β||ω||∞ for some β < 1/2 for all time:
   d||ω||∞/dt ≤ β||ω||∞² → ||ω|| ≤ C/(T-t) (Type I)
   → no blowup by Seregin. REGULARITY. ∎

### THE ONE REMAINING GAP:
10. PROVE: α(x*) < |ω(x*)|/2 at the max of |ω| for NS solutions on T³.

    This is equivalent to any of:
    (a) Prove α/|ω| stays bounded below 1/2 along the dynamics
    (b) Prove the per-mode angular spread gives δ > 0 in α < (1/2 - δ)|ω|
    (c) Prove the attractor |ω|²/|S|² > 2.667 at the max
    (d) Prove H_ωω ≥ c|ω|² for explicit c > 0

### EMPIRICAL EVIDENCE FOR THE GAP:
- α/|ω| < 0.48 across 15+ ICs at N=32 (margin 4% to 0.5)
- α/|ω| < 0.42 for 14 of 15 ICs (margin 16%)
- Q < 0 when α/|ω| > 0.2 at >90% of max-point measurements
- The per-mode bound is saturated only by unrealistic single-mode fields

### WHAT DOESN'T WORK:
- Timescale argument: actual tilting rate 6× weaker than predicted (0.16×, not 2×)
- Lei-Ren-Tian double cone: requires FIXED axis, e₂ varies (dead)
- Constantin-Fefferman: CF ratio ~8, not bounded (dead)
- Miller orthogonality: L² only, not pointwise (dead)
- CKN + isotropy: gives α ≤ |ω|/(2√3), still proportional (dead for Euler)
- Generic positive function: 45% violation rate (dead for kinematic bound)
- Simple Cauchy-Schwarz on Fourier: gives α < 0.707|ω|, not 0.5 (dead)

## THE PROOF FOR NS (CONDITIONAL ON ONE INEQUALITY)

THEOREM (conditional): Smooth solutions to 3D incompressible Navier-Stokes on T³
remain smooth for all finite time, IF α(x*) < |ω(x*)|/2 at all vorticity maxima.

PROOF:
1. Suppose blowup at T*. Then ||ω||∞ → ∞ as t → T*.
2. By hypothesis: α(x*) < ||ω||∞/2. So d||ω||∞/dt < ||ω||∞²/2.
3. This gives ||ω||∞ ≤ 2/(T*-t). This is Type I (rate (T*-t)^{-1}).
4. By Seregin (2012): NS solutions cannot develop Type I singularities.
5. Contradiction. ∎

TO CLOSE: prove α < |ω|/2 at vorticity maxima of 3D NS on T³.
This may follow from the per-mode Fourier bound + lattice angular spread + smoothness.

## THE PATH FORWARD

The most promising approach: formalize the per-mode bound into a full proof.

The argument: for a smooth (H^s, s > 5/2) divergence-free field on T³,
the Fourier energy cannot be concentrated on a single angle θ = π/4.
The integer lattice Z³ forces angular spread, giving δ > 0.

This is a problem in arithmetic geometry / harmonic analysis on lattices.
Specifically: for the CZ kernel R_{ij}(k) on Z³, the operator norm
||ê·R·ê||_{ℓ∞→ℓ∞} may be strictly < 1/2 when restricted to smooth fields.

A computer-assisted proof (interval arithmetic on the Fourier coefficients)
could close this by showing α < 0.499|ω| for all sufficiently smooth fields.

## 302 files. One inequality. The per-mode bound points the way.
