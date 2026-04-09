---
source: MAX CONSTRAINT ALGEBRA — using w_j·ω ≥ |w_j|² to bound C
type: PROOF ATTEMPT — the max condition gives computable constraints
file: 530
date: 2026-03-30
instance: CLAUDE_OPUS (500s)
---

## THE MAX CONDITION (vertex form)

At the vertex max with effective amplitudes w_k = s_k v_k:

**For each j: w_j · ω ≥ |w_j|²**

where ω = Σ w_k. Otherwise flipping s_j → -s_j increases |ω|².

Proof: |ω|² with s_j → -s_j gives |ω - 2w_j|² = |ω|² - 4w_j·ω + 4|w_j|².
For |ω|² to be max: |ω - 2w_j|² ≤ |ω|². So w_j·ω ≥ |w_j|². ∎

## CONSEQUENCES

### 1. Each mode is aligned with ω
w_j · ω ≥ |w_j|² > 0.

Decompose: w_j = a_j ê + b_j (aligned + perpendicular).
a_j = w_j · ê = w_j · ω / |ω| ≥ |w_j|² / |ω| > 0.

So: **a_j > 0 for all j** (strict positivity of aligned component).

### 2. Perpendicular cancellation
ω = |ω|ê = Σ(a_j ê + b_j) → Σ b_j = 0.

### 3. Alignment bound
a_j |ω| = w_j · ω ≥ |w_j|² = a_j² + |b_j|².
So: a_j ≥ (a_j² + |b_j|²)/|ω| → |ω| a_j ≥ a_j² + |b_j|².
→ **|b_j|² ≤ a_j(|ω| - a_j)**

This bounds the perpendicular energy PER MODE.

### 4. Total perpendicular energy
Σ|b_j|² ≤ Σ a_j(|ω| - a_j) = |ω|Σa_j - Σa_j² = |ω|² - Σa_j²

(Using |ω| = Σa_j.)

And Σa_j² ≥ (Σa_j)²/N = |ω|²/N (Cauchy-Schwarz).

So: **Σ|b_j|² ≤ (1-1/N)|ω|²**

### 5. Per-mode perpendicular bound
|b_j| ≤ √(a_j(|ω|-a_j)) ≤ |ω|/2 (AM-GM: max of a(|ω|-a) at a=|ω|/2).

## BOUNDING C USING THE ALIGNMENT

C = Σ_{j<k} (w_j·n̂)(w_k·n̂)sin²θ

Decompose: w_j·n̂ = a_j(ê·n̂) + b_j·n̂.

C = Σ [a_j(ê·n̂)+b_j·n̂][a_k(ê·n̂)+b_k·n̂] sin²θ
= Σ a_ja_k(ê·n̂)²sin²θ + (cross terms with b) + (b²terms)

### Aligned contribution (always ≥ 0):
C_aligned = Σ a_ja_k (ê·n̂_{jk})² sin²θ_{jk} ≥ 0

### Perpendicular correction:
C_perp = Σ [a_j(ê·n̂)(b_k·n̂) + a_k(ê·n̂)(b_j·n̂) + (b_j·n̂)(b_k·n̂)] sin²θ

|C_perp| ≤ Σ [a_j|b_k| + a_k|b_j| + |b_j||b_k|] sin²θ (using |ê·n̂|≤1, |b·n̂|≤|b|)

### Bounding the sum

Using constraint 3: |b_j| ≤ √(a_j(|ω|-a_j)).

For the AB terms: Σ a_j|b_k| ≤ Σ a_j √(a_k(|ω|-a_k))

By Cauchy-Schwarz: ≤ √(Σa_j²) √(Σa_k(|ω|-a_k)) = √(Σa²) √(|ω|²-Σa²)

For the BB terms: Σ|b_j||b_k| ≤ (Σ|b_k|)²/2 ≤ (√(N·Σ|b|²))²/2 = NΣ|b|²/2

These bounds are LOOSE. For the worst N=4:
- Σa² ≈ |ω|²/N = |ω|²/4
- Σ|b|² ≈ (3/4)|ω|²
- AB terms: ≈ |ω|/2 × |ω|√3/2 = √3|ω|²/4 ≈ 0.43|ω|²
- BB terms: ≈ 4·3|ω|²/(4·2) = 3|ω|²/2 (way too loose)

The BB term bound is O(N)|ω|² — DIVERGES with N. Too loose.

## THE OBSTACLE

The perpendicular energy Σ|b|² can be up to (1-1/N)|ω|², and the
projection onto pair normals n̂_{jk} can concentrate, making C_perp
comparable to |ω|².

The max condition constrains the TOTAL perpendicular energy but NOT
its distribution across pair normals.

For the KEY LEMMA: need |C_perp| < |ω|²/4 + C_aligned ≤ |ω|²/4.

This requires: the perpendicular correction is bounded by |ω|²/4.

From the data: worst |C_perp|/|ω|² ≈ 0.17 + C_aligned/|ω|² ≈ 0.17 + 0.05 ≈ 0.22.
And 0.22 < 0.25 (= 1/4). But the margin is just 12%.

## STATUS

The max condition w_j·ω ≥ |w_j|² gives:
- a_j > 0 (each mode aligned with ω)
- |b_j|² ≤ a_j(|ω|-a_j) (per-mode perpendicular bound)
- Σ|b|² ≤ (1-1/N)|ω|² (total perpendicular bound)

These are NECESSARY but NOT SUFFICIENT to prove C > -5/16.
The gap: bounding the projection of b_j onto the pair normals n̂_{jk}.

The pair normals n̂_{jk} depend on the k-vectors (fixed geometry).
The b_j components are constrained by Σb_j = 0 and |b_j| ≤ √(a_j(|ω|-a_j)).

## 530. Max condition gives alignment + perpendicular bounds.
## These are necessary but don't close C > -5/16.
## Gap: bound the perpendicular projection onto pair normals.
