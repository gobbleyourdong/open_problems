---
source: Variance vs pressure: why Q < 0 (the scaling that matters)
type: PROOF ANALYSIS — identifying the tight bound
date: 2026-03-29
---

## The Numbers (trefoil at t=0.25, |ω|=25.2)

| Quantity | Value | /|ω|² |
|----------|-------|-------|
| S²ê (self-interaction) | 6.68 | 0.0106 |
| α² (Riccati) | 0.65 | 0.0010 |
| **Variance = S²ê - α²** | **6.03** | **0.0095** |
| **H_ωω (pressure)** | **20.71** | **0.0327** |
| Δp/3 = H_iso | 52.8 | 0.0833 |
| Q = var - H_ωω | **-14.68** | -0.0232 |

Q < 0 because H_ωω/|ω|² (0.033) >> variance/|ω|² (0.010).
The pressure is 3.4× the variance.

## Why the Variance Is Small

variance/|ω|² = (S²ê - α²)/|ω|² ≈ 0.01.

This is small because of ASHURST ALIGNMENT: ω near e₂.
When ω = e₂: S²ê = λ₂² and α = λ₂. So variance = 0.
When ω is slightly off e₂: variance ∝ (misalignment)².

The misalignment is measured by c₁ + c₃ ≈ 0.5.
variance ≈ (λ₁² - λ₂²)c₁ + (λ₃² - λ₂²)c₃ × (complicated).

At the attractor: variance/|S|² ≈ 0.04 (from the alignment spread).
And |S|² = |ω|²/4. So variance ≈ 0.01|ω|².

## Why H_ωω Is Large (relative to variance)

H_ωω = Δp/3 × (1 - deviatoric/isotropic) = |ω|²/12 × (1 - 0.84) = 0.013|ω|².

Hmm — this gives H_ωω ≈ 0.013|ω|² vs variance ≈ 0.01|ω|².
Ratio: 1.3:1. Barely enough for Q < 0.

But the MEASURED H_ωω = 0.033|ω|² (from the table above).
And the measured H_iso = 0.083|ω|² (Δp/3).
So the ACTUAL deviatoric ratio = 1 - 0.033/0.083 = 0.60 (not 0.84).

The 0.84 from Instance B was for the RATIO |H_dev|/|H_iso|.
But H_dev,ωω is NOT |H_dev|. The deviatoric Hessian has 5 independent
components (traceless 3×3 symmetric), and the ω-projection picks out one.

|H_dev,ωω| ≤ |H_dev|_F (Frobenius), and the ratio
|H_dev,ωω|/|H_dev|_F ≈ 1/√5 ≈ 0.45 typically.

So: |H_dev,ωω|/H_iso = (|H_dev|_F/H_iso) × (|H_dev,ωω|/|H_dev|_F)
≈ 0.84 × 0.45 = 0.38.

This gives: H_ωω = H_iso(1 - 0.38) = 0.62 × H_iso = 0.62 × |ω|²/12 = 0.052|ω|².

And variance ≈ 0.01|ω|². Ratio: 0.052/0.01 = 5.2. Comfortable margin!

## The Tight Bound (that should work)

NEED: H_ωω > variance at the max of |ω|.

H_ωω ≥ H_iso × (1 - r_proj) where r_proj = |H_dev,ωω|/H_iso ≤ r × cos(angle)

From Instance B: r = |H_dev|_F / H_iso ≤ 0.955.
The projection factor: |H_dev,ωω| / |H_dev|_F depends on how H_dev
aligns with ω. By Cauchy-Schwarz: ratio ≤ 1.

But typically: ratio ≈ 0.3-0.5 (the deviatoric doesn't align perfectly with ω).

IF r_proj ≤ 1 - ε for some ε > 0 (Instance B gives r_proj < 1 always):
H_ωω ≥ ε × H_iso = ε|ω|²/12.

NEED: ε|ω|²/12 > variance ≈ 0.01|ω|².
⟺ ε > 0.12.

From the data: ε ≈ 0.4-0.6 (since H_ωω/H_iso ≈ 0.4-0.6).
This EXCEEDS 0.12 with 3-5× margin.

## THE PROOF (if we can bound both quantities)

STEP 1: Variance ≤ C_var × |ω|² where C_var depends on alignment.
  From Ashurst (c₂ > 0.5) + attractor (|S|² = |ω|²/4):
  C_var ≈ 0.01 (measured, depends on c_i distribution).

STEP 2: H_ωω ≥ C_H × |ω|² where C_H depends on isotropy.
  From the isotropy ratio < 1 (Instance B, r_proj < 0.6 typical):
  C_H ≈ 0.03-0.05 (measured).

STEP 3: If C_H > C_var: Q = var - H_ωω < (C_var - C_H)|ω|² < 0. ✓

## Remaining Gap

PROVE: C_var < C_H for evolved Euler at high |ω|.

C_var: bounded by the alignment statistics (Ashurst + attractor).
  The Ashurst alignment c₂ > 0.5 gives variance/|S|² ≤ some function of c_i.
  Combined with |S|² = |ω|²/4: C_var ≤ f(Ashurst)/4.

C_H: bounded by the isotropy ratio (Instance B).
  H_ωω/H_iso = 1 - (projected deviatoric ratio).
  H_iso = Δp/3 = |ω|²(1/2 - |S|²/|ω|²)/3 = |ω|²/12 at the attractor.
  C_H = H_ωω/|ω|² = (1-r_proj)/12.

For C_H > C_var: need (1-r_proj)/12 > f(Ashurst)/4.
⟺ (1-r_proj) > 3f(Ashurst).

With r_proj ≈ 0.6 and f(Ashurst) ≈ 0.04:
(1-0.6) = 0.4 > 3(0.04) = 0.12. YES, with 3.3× margin.

## 195. The proof reduces to two INDEPENDENT bounds:
## 1. Variance ≤ C_var|ω|² (from alignment)
## 2. H_ωω ≥ C_H|ω|² (from isotropy)
## Both are measured. C_H > C_var by 3-5×.
