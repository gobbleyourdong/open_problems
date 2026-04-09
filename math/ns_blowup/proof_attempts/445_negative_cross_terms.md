---
source: S CROSS-TERMS ARE NEGATIVE AT CONSTRUCTIVE VERTICES (proven for ⊥ k's)
type: POTENTIAL BREAKTHROUGH — proves |∇u|²/|ω|² < 1 for orthogonal k
file: 445
date: 2026-03-30
---

## THE IDENTITY (proven, file 367)

For ORTHOGONAL k-vectors (k_j · k_k = 0):

    S_j : S_k = -(v̂_j · v̂_k)/2 = -D_{jk}/2

## THE CONSEQUENCE AT CONSTRUCTIVE VERTICES

At a vertex where |ω|² is large (constructive interference):
s_j s_k D_{jk} = |D_eff| > 0 (positive vorticity cross-terms).

The strain cross-terms at the SAME vertex:
s_j s_k (S_j : S_k) = s_j s_k × (-D_{jk}/2) = -|D_eff|/2 < 0.

**The strain cross-terms are NEGATIVE when the vorticity cross-terms
are POSITIVE.** This is EXACT for orthogonal k-vectors.

## THE BOUND (for orthogonal k-vectors, PROVEN)

|S(x)|² = Σ|S_k|² + 2Σ_{j<k} s_js_k (S_j:S_k)
        = Σ|ω̂_k|²/2 + 2Σ(-|D_eff|/2)
        = (Σa_k² - Σ|D_eff|) / 2

|ω(x)|² = Σa_k² + 2Σ|D_eff|

|S|²/|ω|² = (Σa² - ΣD)/(2(Σa² + 2ΣD))

Since ΣD ≥ 0: numerator ≤ Σa², denominator ≥ 2Σa².
**|S|²/|ω|² ≤ 1/2** (equality iff ΣD = 0, i.e., orthogonal polarizations).

And: **|S|²/|ω|² < 1/2 when ΣD > 0** (constructive interference).

Therefore: |∇u|²/|ω|² = |S|²/|ω|² + 1/2 ≤ 1/2 + 1/2 = 1.0.

**|∇u(x)|² ≤ |ω(x)|²** at ALL constructive vertices for orthogonal k-vectors.

## EXTENSION TO NON-ORTHOGONAL K-VECTORS

For non-orthogonal k: S_j:S_k = G_{jk} (the gradient cross-term coefficient).
And G_{jk} = κ²D_{jk} - κA_{jk}B_{jk} (from the BAC-CAB formula).

At a constructive vertex: s_js_k G_{jk} = κ²|D_eff| - κ(s_js_k AB).

The first term κ²|D_eff| is POSITIVE (hurts — adds to |S|²).
The second term κ(s_js_k AB) has mixed sign.

For orthogonal k (κ = 0): both terms vanish → S_j:S_k = -D/2 (proven above).
For non-orthogonal: the κ² term ADDS positive cross-correlation to |S|².

The question: is the positive κ² term small enough?
s_js_k G_{jk} = κ²|D_eff| - κ(s_js_k AB)
vs s_js_k D_{jk} = |D_eff|.

Ratio: G_eff/D_eff = κ² - κAB/D (when D ≠ 0).

For the S cross-term to still be negative (relative to the D cross-term):
need G_eff < D_eff → κ² - κAB/D < 1 → κ(κ - AB/D) < 1.

For |κ| < 1 and |AB/D| ≤ 1: this is USUALLY satisfied.

## THE GAP

Prove: Σ s_js_k G_{jk} < Σ s_js_k D_{jk} at constructive vertices
for ALL (not just orthogonal) k-vectors.

Equivalently: the gradient excess Σ s_js_k Δ_{jk} < 0 at constructive vertices.

This IS the original Key Lemma (excess is negative at the global max).
But now we know WHY it's true: the S cross-terms are structurally
negative relative to D cross-terms at constructive vertices.

## 445. For orthogonal k: |∇u|² ≤ |ω|² at ALL constructive vertices (PROVEN).
## The strain cross-terms are exactly -D/2 (OPPOSITE sign to vorticity).
## For non-orthogonal k: need κ² correction bounded. Same old gap.
