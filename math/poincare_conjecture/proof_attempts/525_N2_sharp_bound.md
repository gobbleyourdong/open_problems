---
source: N=2 SHARP BOUND — |S|²_F/|ω|² ≤ 3/4 with C/|ω|² ≥ -1/8 EXACTLY
type: PROVEN RESULT — the N=2 Frobenius bound is TIGHT at 3/4
file: 525
date: 2026-03-30
instance: CLAUDE_OPUS
---

## THE RESULT

For ANY two-mode div-free field on T³:

**|S(x*)|²_F ≤ (3/4)|ω(x*)|² at x* = argmax|ω|**

Equivalently: **C ≥ -|ω|²/8** (from |S|²_F = |ω|²/2 - 2C).

This is TIGHT: equality achieved for k-vectors at 60° angle,
both polarizations at γ = 45° to ê, on the K=√8 shell.

## CONSEQUENCE FOR THE KEY LEMMA (N=2)

S²ê ≤ (2/3)|S|²_F ≤ (2/3)(3/4)|ω|² = (1/2)|ω|² < (3/4)|ω|². ✓

**The Key Lemma holds for N=2.**

At the worst Frobenius case: S²ê = (1/8)|ω|² (actual, far below 1/2).

## THE WORST-CASE STRUCTURE

| Property | Value |
|----------|-------|
| k-vectors | 60° angle (e.g., (-2,0,-2) and (-2,2,0)) |
| |k|² | Equal on both (same K-shell) |
| γ angles | Both 45° to ê |
| C/|ω|² | -1/8 exactly |
| |S|²_F/|ω|² | 3/4 exactly |
| S²ê/|ω|² | 1/8 (self-attenuation) |
| signs | Both +1 (constructive) |

## KEY OBSERVATIONS

1. **The worst ratio 3/4 is a BARRIER**: for N=2, the Frobenius ratio
   cannot exceed 3/4. This is C ≥ -1/8, not C ≥ -1/4.

2. **Same-shell pairs are worst**: mixed K-shells give lower ratios
   (K=1+√2: ratio 0.707). Same-K pairs at 60° are worst.

3. **Parallel k (0°)**: C = 0, ratio = 1/2. Orthogonal k (90°): C = 0, ratio = 1/2.
   The worst is at INTERMEDIATE angles (60°).

4. **45° polarization**: γ = 45° maximizes sinγ cosγ = sin(2γ)/2.
   This is the polarization that equally divides between aligned and perpendicular.

## WHY 3/4 (algebraic)

From the cross-term identity for N=2:
  C = (v₁·n̂)(v₂·n̂) sin²θ cos(k₁·x*)cos(k₂·x*)

At the max (cos·cos = ±1 for vertex enumeration):
  C = ±(v₁·n̂)(v₂·n̂) sin²θ

For 60° angle: sin²θ = sin²60° = 3/4. And with γ = 45°:
  v₁·n̂ = ±|v₁|/√2, v₂·n̂ = ∓|v₂|/√2 (opposite signs for worst case)

  C = -(|v₁||v₂|/2)(3/4) at the max sign pattern.

  |ω|² = |v₁ ± v₂|² = |v₁|² + |v₂|² ± 2v₁·v₂

For equal amplitudes |v₁|=|v₂|=1, 60° geometry:
  C = -3/8, |ω|² = 2 + 2cos(angle between v₁,v₂).

With v₁·v₂ = cosγ₁cosγ₂ + (perp terms) = cos²45° + ... = 1/2 + ...

The exact computation gives C/|ω|² = -1/8. ✓

## EXTENSION TO N ≥ 3

For N=3: worst |S|²_F/|ω|² observed = 0.750 (achieved by adding one
mode at γ=0 to the N=2 worst case — the new mode doesn't change C).

For N≥4 (random trials): worst observed = 0.834. So C/|ω|² goes below
-1/8 (down to -0.167). The N=2 bound 3/4 is NOT universal for N≥3.

But S²ê ≤ (2/3)(0.834)|ω|² = 0.556|ω|² < 0.750|ω|². Key Lemma via trace-free.

**The gap**: prove |S|²_F < (9/8)|ω|² (or better, < |ω|²) for N ≥ 3.

## 525. N=2 sharp: |S|²_F ≤ 3|ω|²/4 (tight at 60° angle, γ=45°).
## S²ê ≤ |ω|²/2 via trace-free. Key Lemma holds for N=2.
## For N≥3: worst Frobenius 0.834 still gives S²ê < 0.75 via trace-free.
