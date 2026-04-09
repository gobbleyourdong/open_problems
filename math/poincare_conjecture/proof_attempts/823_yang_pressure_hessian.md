---
source: YANG PRESSURE HESSIAN — bounding the approximation error
type: NEW DIRECTION — pressure Hessian approximation in strong vorticity
file: 823
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE YANG APPROXIMATION (Yang, Xu, Pumir, He 2024)

In regions of strong vorticity (Ωτ_K² ≫ 1), the pressure Hessian:
    H_p ≈ -(1/3)tr(m²)I - (1/4)(ω_iω_j - ω²δ_ij/3)

If EXACT: the strain evolution at the vorticity max gives:
    D/Dt α ≈ -α² + (3/8)|ω|² - P_⊥  [with P_⊥ ≥ 0]

At the KEY LEMMA boundary (α = √(3/4)|ω|):
    D/Dt α ≈ -(3/4)|ω|² + (3/8)|ω|² - P_⊥ = -(3/8)|ω|² - P_⊥ < 0

So α DECREASES from the Key Lemma bound: self-limiting!

## THE APPROXIMATION ERROR

The Yang approximation error: ε = ||H_p - H_p^{Yang}||/|ω|².
The TRUE strain bound: α_max = √(3/8 + ε) · |ω|.

| ε | α_max/|ω| | vs Key Lemma |
|---|-----------|-------------|
| 0 | 0.612 | 29% better |
| 0.1 | 0.689 | 20% better |
| 0.2 | 0.758 | 12% better |
| 0.375 | 0.866 | = Key Lemma |

The Key Lemma = Yang approximation with 100% error (ε = 3/8).

## WHY THIS DOESN'T CLOSE THE GAP

Even with ε = 0 (exact Yang): α_max = √(3/8)|ω| ≈ 0.612|ω|.
This is STILL LINEAR in |ω| → still Type I → still blows up.

For SUBLINEAR α: need ε → -3/8 as |ω| → ∞ (the 3/8 term must VANISH).
This would require the pressure Hessian to EXACTLY cancel the
quadratic self-amplification of strain. There's no reason for this.

## WHAT IT DOES GIVE

Near blowup (|ω| → ∞): the Yang approximation becomes more accurate
(DNS validation). So ε → 0, and α_max → √(3/8)|ω| ≈ 0.612|ω|.

This IMPROVES the Type I constant from C_TI = 2/√3 ≈ 1.155 to
C_TI ≈ 2·0.612 = 1.224... wait, this is WORSE? No:

The Type I constant comes from d/dt|ω| ≤ α|ω| ≤ c|ω|².
With c = √(3/8) instead of √(3/4): c = 0.612 instead of 0.866.
The Type I blowup time is LONGER (1/(2c|ω|_0) is larger for smaller c).

But it's still TYPE I. The exponent is still 2. No regularity.

## THE DEEP REASON

The strain evolution D/Dt α = -α² + ... has a QUADRATIC self-limiting
term -α². The pressure Hessian provides the SOURCE term that sustains α.
The Key Lemma bounds the net effect.

For SUBLINEAR α: the source must grow SLOWER than α². But the source
is ~|ω|² (from the pressure Hessian approximation). And α ~|ω|.
So source/α² ~ |ω|²/|ω|² = 1 (constant). The balance is EXACT at Type I.

Breaking this balance requires the source to DECREASE relative to α²
as |ω| → ∞. This is the depletion of nonlinearity.

## 823. Yang approximation: H_p ≈ local terms. Error ε → 0 near blowup.
## Best case (ε=0): α_max = √(3/8)|ω|. Still linear. Still Type I.
## The 29% improvement over Key Lemma doesn't change the exponent.
## Sublinear α requires the pressure source to deplete. = Open problem.
