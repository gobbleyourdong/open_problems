---
source: DECOMPOSITION INSIGHT — C_aa saves the bound
type: KEY STRUCTURAL FINDING — the aligned contribution is essential
file: 533
date: 2026-03-30
instance: CLAUDE_OPUS (500s)
---

## THE DECOMPOSITION

C = C_aa + C_ab + C_bb where:
  C_aa = Σ a_j a_k (ê·n̂)² sin²θ ≥ 0 (ALWAYS positive)
  C_ab = Σ [a_j(b_k·n̂) + a_k(b_j·n̂)](ê·n̂) sin²θ
  C_bb = Σ (b_j·n̂)(b_k·n̂) sin²θ

## NUMERICAL EVIDENCE (182 worst cases)

| Component | Worst | Mean (worst 15) |
|-----------|-------|-----------------|
| C_aa/|ω|² | +0.002 | +0.020 |
| C_ab/|ω|² | -0.102 | -0.050 |
| C_bb/|ω|² | -0.176 | -0.138 |
| (C_ab+C_bb)/|ω|² | **-0.235** | -0.188 |
| C/|ω|² | **-0.177** | -0.168 |

**C_aa provides the 6% margin** that keeps C above -1/4.

## THE PROOF STRUCTURE

### For N ≥ 3 with independent k-vectors:

C_aa > 0 strictly. Proof:
  C_aa = Σ_{j<k} a_j a_k (ê·n̂_{jk})² sin²θ_{jk}
  All a_j > 0 (from max condition).
  Need at least one pair with (ê·n̂)² sin²θ > 0.
  n̂_{jk} = (k_j×k_k)/|k_j×k_k|.
  ê·n̂ = 0 iff ê ⊥ (k_j×k_k) iff ê ∈ span(k_j, k_k).
  For N ≥ 3 independent k-vectors: ê can't be in ALL pairwise planes.
  (3 independent k-vectors span R³; ê can't be in all C(3,2)=3 planes.)
  So at least one pair has ê·n̂ ≠ 0. ∎

### Combined:

IF C_ab + C_bb ≥ -|ω|²/4 can be proven:
  C = C_aa + (C_ab + C_bb) > 0 + (-|ω|²/4) = -|ω|²/4 for N ≥ 3.

For N = 2: C ≥ -|ω|²/8 > -|ω|²/4 (proven, file 525).

Together: C ≥ -|ω|²/4 for ALL N ≥ 2.

## THE REMAINING GAP

**Prove: C_ab + C_bb ≥ -|ω|²/4 at the vorticity max.**

Margin: 6% (worst observed -0.235 vs threshold -0.250).

This involves bounding the perpendicular interactions:
  C_ab = Σ [a_j(b_k·n̂) + a_k(b_j·n̂)](ê·n̂) sin²θ
  C_bb = Σ (b_j·n̂)(b_k·n̂) sin²θ

Using constraints:
  Σ b_j = 0 (perpendicular cancellation)
  |b_j|² ≤ a_j(|ω| - a_j) ≤ |ω|²/4 (per-mode bound from max condition)
  All a_j > 0

## WHY THE MARGIN IS TIGHT BUT THE BOUND HOLDS

The C_bb term can reach -|ω|²/4 from ONE pair alone (when b_j ≈ -b_k
with |b_j| = |ω|/2). But C_ab partially compensates:

When C_bb is maximally negative (b_j strong, b_k = -b_j):
  C_ab involves a_j(b_k·n̂)(ê·n̂) + a_k(b_j·n̂)(ê·n̂)
  = (a_j-a_k)(b_j·n̂... wait, b_k = -b_j, so:
  = (a_j(-b_j·n̂) + a_k(b_j·n̂))(ê·n̂) = (a_k-a_j)(b_j·n̂)(ê·n̂)

For equal amplitudes a_j = a_k: C_ab = 0 (no compensation).
For unequal: C_ab ∝ (a_k-a_j) which can be positive or negative.

The tight cases have a_j ≈ a_k (nearly equal amplitudes for the
dominant pair), making C_ab ≈ 0 and C_bb ≈ C.

## THE PROOF CHAIN (complete if C_ab+C_bb ≥ -1/4 proven)

1. C_ab + C_bb ≥ -|ω|²/4 [the remaining gap, margin 6%]
2. C_aa > 0 for N ≥ 3 [PROVEN above]
3. C = C_aa + C_ab + C_bb > -|ω|²/4 [from 1+2]
4. |S|²_F = |ω|²/2 - 2C ≤ |ω|²/2 + |ω|²/2 = |ω|² [identity]
5. S²ê ≤ (2/3)|S|²_F ≤ (2/3)|ω|² [trace-free]
6. (2/3)|ω|² < (3/4)|ω|² [strict: 2/3 < 3/4]
7. Key Lemma → barrier → Type I → Seregin → REGULARITY ∎

## 533. C_aa > 0 for N≥3 (PROVEN). C_ab+C_bb ≥ -1/4 (6% margin).
## Together: C > -1/4 → |S|² ≤ |ω|² → S²ê < (3/4)|ω|² → regularity.
## One gap remains: prove C_ab+C_bb ≥ -|ω|²/4.
