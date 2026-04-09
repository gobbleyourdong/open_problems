---
source: κ at the max is 0.1-0.7, NOT < 0.056. The gradient bound fails.
type: NEGATIVE — the simple gradient argument doesn't close
file: 290
date: 2026-03-29
---

## Measurement

κ = |∂ω_⊥/∂z|/|ω| at the max-|ω| point of the trefoil:
Range: 0.094 to 0.674 across 12 time samples.
ALL above the threshold 0.056 needed for the gradient bound.

## What This Means

The proof attempt in file 288 (α > 0 on entire |ω|² support from
the gradient bound ||∂α/∂z|| < α/(3σ)) FAILS because κ is too large.

The z-gradient ||∂α/∂z|| ~ κ|ω| ~ 0.4×25 = 10. And α/(3σ) ≈ 2.5/0.9 ≈ 2.8.
So ||∂α/∂z|| ≈ 10 >> α/(3σ) ≈ 2.8. The gradient bound fails by 3.6×.

## But the Key Integral Is STILL Positive (35/35)

The integral ∫|ω|²α cos(kz) > 0 holds despite κ being large.

WHY: The |ω|² weighting is EXPONENTIALLY strong (Gaussian with σ≈0.3).
Even though α goes negative at |z| > 0.3-0.5 from the max: |ω|² is
EXPONENTIALLY small there. The Gaussian decay (exp(-z²/2σ²)) beats
the linear α variation (α₀ - κ|ω|z).

The first-order gradient bound is too CONSERVATIVE: it uses
linear variation of α but doesn't account for the exponential
suppression of |ω|².

## A Better Bound

∫|ω|²α cos = ∫|ω|²α₀ cos - ∫|ω|²(α₀-α) cos

The correction: |α₀-α(z)| ≤ κ|ω||z| (from gradient bound).
So: |correction| ≤ κ|ω| ∫|ω|²|z| cos dz.

For Gaussian |ω|²: ∫|ω|²|z| cos dz ≈ |ω|²_max σ² √(2/π) exp(-σ²/2).
And: ∫|ω|² cos dz ≈ |ω|²_max σ √(2π) exp(-σ²/2).

Ratio: (∫|ω|²|z|cos) / (∫|ω|²cos) = σ/√π ≈ 0.17.

Condition: κ|ω| × 0.17σ < α₀.
→ κ < α₀/(0.17σ|ω|) = α₀/(0.17×0.3×|ω|) = α₀/(0.051|ω|).

With α₀ ≈ 2.5, |ω| ≈ 25: κ < 2.5/(0.051×25) = 1.96.

Measured κ: 0.09-0.67. ALL below 1.96! ✓ (minimum margin: 2.9×)

## THE BOUND ACTUALLY CLOSES!

The CORRECT comparison uses the Gaussian-weighted ratio:
∫|ω|²|z|cos / ∫|ω|²cos = σ/√π ≈ 0.17

NOT the unweighted ratio which gave the previous bound.

Condition: κ < α/(0.17σ|ω|) ≈ (α/|ω|)/(0.17σ) = c/(0.17σ)

With c = α/|ω| ≈ 0.1 and σ ≈ 0.3: threshold = 0.1/(0.051) = 1.96.
Measured κ: 0.09-0.67. ALL below 1.96. ✓

## REVISED P2 PROOF

STEP 1: ∫|ω|²α cos = α₀∫|ω|²cos + ∫|ω|²(α-α₀)cos.
STEP 2: First term > 0 (monotonicity lemma + α₀ > 0). PROVEN.
STEP 3: |Second term| ≤ κ|ω| × σ/√π × ∫|ω|²cos = κ|ω|σ/√π × (first term/α₀).
STEP 4: |Second/First| ≤ κ|ω|σ/(α₀√π) = κσ/(c√π) where c = α₀/|ω|.
STEP 5: For |Second/First| < 1: need κ < c√π/σ.

With c = α/|ω| ≈ 0.1, σ ≈ 0.3: threshold = 0.1×1.77/0.3 = 0.59.
Measured κ: 0.09-0.67. MOST below 0.59 but κ=0.67 EXCEEDS it.

## STILL MARGINAL

The threshold κ < 0.59 is violated at t=0.02 (κ=0.67).
But 3σκ = 0.607 < 2 = safe margin? No, the threshold IS 0.59.

The issue: the Gaussian-weighted bound gives threshold 0.59, and
one measurement (κ=0.67) exceeds it by 14%.

With the more precise calculation (not approximating cos ≈ 1):
the correction includes the cos(kz) modulation which further
reduces the tail. The ACTUAL threshold is higher than 0.59
because the cos function suppresses the negative tails.

For a Gaussian |ω|² with σ=0.3, the effective support where
|ω|²cos(z) is significant is |z| < min(3σ, π/2) = min(0.9, 1.57) = 0.9.
In this range: cos(z) > cos(0.9) = 0.62. So the cos provides
additional 38% suppression of the tails.

Including this: threshold ≈ 0.59/0.62 × ... gets complicated.

## BOTTOM LINE

The Gaussian-weighted gradient bound gives threshold κ < ~0.6-2.0
(depending on exact calculation). The measured κ = 0.09-0.67 is
at the BOUNDARY — works for 11/12 measurements, marginal for 1.

The key integral is POSITIVE at 35/35 measurements (from file 285).
The bound NEARLY closes. With more careful analysis of the
Gaussian+cos interaction: it may close completely.

## 290. The gradient bound nearly closes with Gaussian weighting.
## κ < 0.59 fails at 1/12 measurements (κ=0.67 at t=0.02).
## The actual integral is positive regardless (35/35).
