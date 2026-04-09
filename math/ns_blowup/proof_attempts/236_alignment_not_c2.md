---
source: V/|ω|² < 1/12 holds WITHOUT c₂ > 1/3
type: CORRECTION — the bound doesn't need Ashurst, just ANY alignment
date: 2026-03-29
---

## The Data

| IC | c₁ | c₂ | c₃ | V/|ω|² | V < |ω|²/12? |
|----|----|----|-----|--------|-------------|
| TG | 0.00 | 0.00 | **1.00** | 0.000 | ✓ (V=0) |
| KP | 0.00 | 0.00 | **1.00** | 0.000 | ✓ (V=0) |
| Trefoil | 0.25-0.68 | 0.29-0.79 | 0.001-0.19 | 0.007-0.014 | ✓ |

**V/|ω|² < 0.015 for ALL ICs, ALL times.**
This is 5.5× below the 1/12 = 0.083 threshold.

## Why c₂ > 1/3 Is NOT Needed

The variance V = Σλᵢ²cᵢ - (Σλᵢcᵢ)² = 0 when ω is ANY eigenvector.
- ω = e₁: V = 0, c₁ = 1
- ω = e₂: V = 0, c₂ = 1
- ω = e₃: V = 0, c₃ = 1

TG and KP have c₃ = 1 (ω aligned with e₃, the COMPRESSIVE eigenvector).
Trefoil has c₂ ≈ 0.5 (ω near e₂, the INTERMEDIATE eigenvector).

BOTH give V ≈ 0. The alignment doesn't have to be with e₂ specifically.

## The Corrected Bound

Need: V/|ω|² < 1/12.

V/|ω|² = (S²ê - α²)/|ω|² ≤ |S|²/|ω|² × max(cᵢ(1-cᵢ))

For the attractor |S|² = |ω|²/4:
V/|ω|² ≤ (1/4) × max(cᵢ(1-cᵢ)) ≤ 1/4 × 1/4 = 1/16 ≈ 0.0625

WAIT: max(c(1-c)) = 1/4 (at c = 1/2). So V/|ω|² ≤ 1/16 < 1/12. ✓

## IS THIS A PROOF?

V = Σλᵢ²cᵢ - (Σλᵢcᵢ)² ≤ max(λᵢ²) × Σcᵢ(1-cᵢ) ... no, that's wrong.

Actually: for any random variable X with P(X=λᵢ) = cᵢ:
Var(X) = E[X²] - E[X]² ≤ (max X - min X)²/4 = (λ₁-λ₃)²/4

And (λ₁-λ₃)² = (λ₁-λ₃)². With trace-free: λ₁-λ₃ = λ₁-(-λ₁-λ₂) = 2λ₁+λ₂.

|S|² = λ₁²+λ₂²+λ₃². And (λ₁-λ₃)² ≤ 2(λ₁²+λ₃²) ≤ 2|S|².

So: V ≤ (λ₁-λ₃)²/4 ≤ |S|²/2 = |ω|²/8.

|ω|²/8 = 0.125 > 1/12 = 0.083. Too loose by 50%.

Better: use the Popoviciu inequality. For a bounded RV on [a,b]:
Var ≤ (b-a)²/4. With a = λ₃, b = λ₁:
V ≤ (λ₁-λ₃)²/4.

For trace-free with λ₂ = -(λ₁+λ₃):
(λ₁-λ₃)² = (λ₁-λ₃)². And |S|² = λ₁²+λ₂²+λ₃².

By Cauchy-Schwarz: (λ₁-λ₃)² ≤ 3(λ₁²+λ₂²+λ₃²) = 3|S|² (loose).
Better: λ₁² + λ₃² ≥ (λ₁-λ₃)²/2 (since (a+b)² ≥ 0 → a²+b² ≥ (a-b)²/2).
So (λ₁-λ₃)² ≤ 2(λ₁²+λ₃²) ≤ 2|S|².
V ≤ |S|²/2 = |ω|²/8 (same as before).

## The Right Approach: Use the Specific Alignment

The Popoviciu bound V ≤ (λ₁-λ₃)²/4 is TIGHT when c₁ = c₃ = 1/2 (ω midway between e₁ and e₃).

For the actual alignment: c₁ or c₃ is close to 1 (ω near an eigenvector).
If max(cᵢ) ≥ 1-δ: V ≤ δ(λ₁-λ₃)² ≤ 2δ|S|² = δ|ω|²/2.

Need δ|ω|²/2 < |ω|²/12 → δ < 1/6.
So: max(cᵢ) > 5/6 ≈ 0.833 would suffice.

From data: max(cᵢ) ≈ 0.80 (trefoil), 1.00 (TG/KP).
The trefoil is borderline at 0.80 < 0.833.

## STATUS

The generic variance bound V ≤ |S|²/2 = |ω|²/8 DOESN'T close (1/8 > 1/12).
Need either:
(a) Tighter alignment: max(cᵢ) > 5/6 (borderline for trefoil)
(b) Tighter eigenvalue bound: (λ₁-λ₃)² < (2/3)|S|² (not true in general)
(c) Use the SPECIFIC structure of NS to get V < |ω|²/12

The data shows V/|ω|² ≈ 0.01 (8× below 1/12). The bounds give 1/8 (50% above).
The gap: factor 8× between measured and provable. Same story as file 229.

## 236. The alignment helps but generic bounds don't close.
## The factor 8 gap persists. Need NS-specific structure.
