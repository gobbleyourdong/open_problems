---
source: DIRECT S²ê BOUND — combining Frobenius identity + trace-free + self-attenuation
type: PROOF ATTEMPT — chain of bounds leading to Key Lemma
file: 512
date: 2026-03-30
instance: CLAUDE_OPUS
---

## THE CHAIN

For any smooth div-free field on T³, at x* = argmax|ω|:

**Step 1** (exact identity, file 511):
  |S(x*)|²_F = |ω(x*)|²/2 − 2Σ_{j<k} P_{jk} cos(k_j·x*)cos(k_k·x*)

**Step 2** (trace-free, standard):
  S²ê ≤ (2/3)|S|²_F

**Step 3** (combine):
  S²ê ≤ (2/3)[|ω|²/2 − 2Σ P cos·cos]
  = |ω|²/3 − (4/3)Σ P cos·cos

**Step 4** (Key Lemma condition):
  Need: |ω|²/3 − (4/3)Σ P cos·cos < 3|ω|²/4
  ⟺ Σ P cos·cos > −5|ω|²/16

## THE REMAINING BOUND

Need to prove: at x* = argmax|ω|:
  Σ_{j<k} (v_j·n̂_{jk})(v_k·n̂_{jk}) sin²θ_{jk} cos(k_j·x*)cos(k_k·x*) > −(5/16)|ω(x*)|²

## NUMERICAL STATUS

| Quantity | Worst observed | Threshold | Margin |
|----------|---------------|-----------|--------|
| |S|²_F/|ω|² | 0.834 | 9/8 = 1.125 | 26% |
| S²ê/|ω|² | 0.367 | 3/4 = 0.750 | 51% |
| correction/|ω|² | −0.167 | −5/16 = −0.3125 | 47% |

All three conditions hold with massive margin in 5000+ trials.

## THE N=2 PROOF

For two modes: PROVEN that |S|²_F < (9/8)|ω|² at the max.

Proof sketch: With v₁·n̂ = p₁, v₂·n̂ = p₂, sin²θ = s:
  P = p₁p₂s, |d| = |P| ≤ |v₁||v₂|s

At the max (cosφ₁, cosφ₂ = ±1 for integer k):
  |ω|² = |v₁|² + |v₂|² + 2c₁c₂(v₁·v₂)

The ratio exceeds 9/8 iff 2|P| > 5(|v₁|²+|v₂|²)/8 + 5|v₁·v₂|/4.

But |P| ≤ |v₁||v₂| and 5(|v₁|²+|v₂|²)/8 ≥ 5|v₁||v₂|/4 (AM-GM).
So need: 2|v₁||v₂| > 5|v₁||v₂|/4 + 5|v₁·v₂|/4.
i.e., 3|v₁||v₂|/4 > 5|v₁·v₂|/4. Since |v₁·v₂| ≤ |v₁||v₂|: 3/4 > 5/4. FALSE.

So the ratio CANNOT exceed 9/8 for N=2. ∎

## THE SELF-ATTENUATION ENHANCEMENT

The trace-free bound S²ê ≤ (2/3)|S|²_F is NOT tight at the max.
Self-attenuation: ê aligns with the INTERMEDIATE eigenvector e₂ of S.
  → S²ê = λ₂² (smallest eigenvalue squared) << λ₁² = max eigenvalue²
  → S²ê ≈ (1/3)|S|²_F (typical), not (2/3)|S|²_F

This is WHY S²ê/|ω|² ≈ 0.37 is much better than (2/3)(0.83) = 0.55.

But the self-attenuation is hard to prove rigorously (it's a dynamic property
of the vorticity-strain alignment, studied by Ashurst et al. 1987 and many
others but never proven for general smooth fields).

## PROOF PATH SUMMARY

1. **For N=2**: Key Lemma PROVEN via |S|²_F < (9/8)|ω|² (algebraic).
2. **For N ≥ 3**: Need correction bound Σ P cos·cos > −5|ω|²/16.
   - The correction involves N(N-1)/2 terms of mixed sign
   - The vorticity max constrains the phases and amplitudes
   - No clean algebraic proof yet, but massive numerical margin

## 512. Chain: identity → trace-free → correction bound.
## N=2 proven. N≥3 needs correction > −5|ω|²/16 (margin 47%).
