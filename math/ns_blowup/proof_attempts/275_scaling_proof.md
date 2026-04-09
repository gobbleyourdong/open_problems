---
source: SCALING ARGUMENT — DH_ωω/Dt ~ |ω|⁴ beats 2α³ ~ |ω|³ for large |ω|
type: PROOF SKETCH — the pressure growth dominates at high vorticity
file: 275
date: 2026-03-29
---

## The Scaling Argument

At the max of |ω| with α > 0:

### Term 1: DH_ωω/Dt (pressure Hessian growth)

Chain: α > 0 → stretching (ω·∇)u creates ⊥ω vorticity at rate |ω|²
→ this creates z-variation in the source Δp at rate |ω|²
→ Fourier lemma converts z-variation to H_ωω at rate ~1
→ NET: DH_ωω/Dt ~ C₁|ω|⁴  (product of creation rate × conversion)

### Term 2: 2α³

At the |ω|²/|S|² = 4 attractor: α ≤ |S| ≤ |ω|/2.
In practice: α ~ c|ω| where c ≈ 0.03-0.12 (from data).
So: 2α³ ~ 2c³|ω|³ = C₂|ω|³.

### Comparison for large |ω|

DH_ωω/Dt ~ C₁|ω|⁴  vs  2α³ ~ C₂|ω|³

For |ω| > C₂/C₁: DH_ωω/Dt > 2α³.

Then: D²α = DVar/Dt + 2α³ + 2αH_ωω - DH_ωω/Dt
The DH_ωω/Dt term dominates (|ω|⁴) and is SUBTRACTED.
So: D²α ≈ -DH_ωω/Dt + lower order < 0.

And: D²α < 0 < 2α³ → Hou-Li condition satisfied → REGULARITY.

## The Two Regimes

REGIME 1: |ω| > M (large vorticity).
  DH_ωω/Dt dominates → D²α < 0 < 2α³ → g'' > 0 → no blowup.

REGIME 2: |ω| ≤ M (bounded vorticity).
  ||ω||∞ ≤ M → trivially bounded → no blowup.

In BOTH regimes: regularity. ∎

## Making It Rigorous

Step 1: Bound DH_ωω/Dt from below.
  DH_ωω/Dt ≥ C₁|ω|⁴ when α > 0.
  Requires: quantitative Fourier lemma applied to the EVOLVING source.
  The stretching creates z-variation at rate (ω·∇)u ~ |ω|²|S| ~ |ω|³/2.
  The Fourier lemma converts z-variation to H_ωω with coefficient ~ |ω|/k²
  (where k is the z-wavenumber of the variation, k ~ 1/σ_z ~ |ω|^{1/2}).
  Net: DH_ωω/Dt ~ |ω|³/2 × |ω|/k² ~ |ω|³ × |ω|^{1/2} ~ |ω|^{7/2}???

  Hmm, the scaling depends on the z-wavenumber k. Let me be more careful.

  The stretching creates z-variation with wavenumber k ~ 2π/σ_z.
  The core width σ_z ~ σ_core ~ √(Γ/(π|ω|)) ~ |ω|^{-1/2}.
  So k ~ |ω|^{1/2}.

  The Fourier lemma: H_ωω contribution from mode k:
  δH_ωω = k² |p_k| where (Δ_xy - k²)p_k = f_k.
  |p_k| ≤ |f_k|/k² (from the operator bound). So δH_ωω ≤ |f_k|.

  The source variation: |f_k| ~ |ω|² × (amplitude of z-modulation).
  The z-modulation amplitude grows at rate ~ |ω|² × dt (from stretching).
  So: d|f_k|/dt ~ |ω|² × |ω| = |ω|³ (stretching rate × source magnitude).

  And: DH_ωω/Dt ~ d|f_k|/dt ~ |ω|³ (not |ω|⁴ as I first estimated).

  With 2α³ ~ |ω|³/C: the scaling is the SAME (both |ω|³). The comparison
  is between the COEFFICIENTS, not the scaling.

## Revised Scaling

DH_ωω/Dt ~ C₁|ω|³ and 2α³ ~ C₂|ω|³ where:
C₁ ~ (stretching efficiency) ≈ 0.5
C₂ ~ 2(α/|ω|)³ = 2c³ ≈ 2(0.05)³ = 0.00025

So C₁/C₂ ~ 2000. The pressure growth is 2000× faster than 2α³.

Even if C₁ is overestimated by 100×: C₁/C₂ ~ 20. Still dominant.

The condition D²α < 2α³ holds because:
D²α ≈ -C₁|ω|³ + (other terms ~ |ω|² or less)
2α³ ≈ C₂|ω|³

For C₁ > C₂: D²α < -C₁|ω|³ + ... < C₂|ω|³ = 2α³.

## Numerical Verification

From the data (file 274):
D²α ≈ -62, 2α³ ≈ +32.
|ω| ≈ 25, α ≈ 2.5.

DH_ωω/Dt contribution to D²α: estimated at ~326 (from the calculation in the analysis).
This dominates all other terms combined.

Scaling: DH_ωω/Dt ≈ 326 ~ C₁|ω|³ → C₁ ≈ 326/15625 ≈ 0.021.
2α³ ≈ 32 → C₂ ≈ 32/15625 ≈ 0.002.
Ratio: C₁/C₂ ≈ 10. Pressure growth 10× stronger. ✓

## The Formal Gap (FINAL)

PROVE: DH_ωω/Dt ≥ C₁|ω|³ at the max when α > 0, where C₁ > 2(α/|ω|)³.

This requires:
(a) The stretching creates z-variation in the source at rate ~ α|ω|²
    (from Dω/Dt = S·ω, the S·ω term projects onto ⊥ω with magnitude |S||ω|)
(b) The z-variation converts to H_ωω via the Fourier lemma (quantitative)
(c) The net: DH_ωω/Dt ≥ α|ω|² × (conversion factor)
(d) With α > 0 and |ω| large: this exceeds 2α³ = 2α³.

The comparison: α|ω|² × C vs 2α³ → C|ω|² > 2α² → C > 2(α/|ω|)².
With α/|ω| ~ 0.05: need C > 0.005. The conversion factor C ~ 0.02 >> 0.005. ✓

## 275. The scaling argument shows DH_ωω/Dt >> 2α³ by factor ~10.
## The formal proof needs the quantitative Fourier lemma for evolving sources.
