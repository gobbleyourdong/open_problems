---
source: PER-PAIR BOUND — P/D ratio constrained by the Biot-Savart geometry
type: KEY ANALYSIS — understanding what limits C from reaching -5/16
file: 460
date: 2026-03-30
instance: CLAUDE_A (400s)
---

## THE WORST CASE STRUCTURE (K²=5)

C/|ω|² = -0.166 at the worst N=3 config:

| Pair | cos θ | sin²θ | P | D | P/D | s_j s_k | Contribution to C |
|------|-------|-------|-----|-----|-----|---------|-------------------|
| (0,1) | 0.80 | 0.36 | +0.049 | -0.458 | -0.11 | -1 | -0.049 (negative) |
| (0,2) | 0.80 | 0.36 | -0.041 | +0.458 | -0.09 | +1 | -0.041 (negative) |
| (1,2) | 0.40 | 0.84 | +0.534 | +0.458 | +1.17 | -1 | -0.534 (negative) |

Total C = -0.049 - 0.041 - 0.534 = -0.624. |ω|² = 3.756. C/|ω|² = -0.166.

**The dominant contribution** comes from pair (1,2) where P/D = 1.17 > 1.

## THE P/D RATIO

P_{jk} = (v_j·n̂)(v_k·n̂) sin²θ
D_{jk} = v_j · v_k

Decompose: D = (v_j·n̂)(v_k·n̂) + v_j^∥ · v_k^∥
So: P = sin²θ × [D - v^∥ · v^∥]

P/D = sin²θ × [1 - (v^∥·v^∥)/D]

For D > 0 and v^∥·v^∥ < D: P/D < sin²θ < 1.
For D > 0 and v^∥·v^∥ > D: P becomes negative. P/D < 0.
For D > 0 and v^∥·v^∥ < 0: P > sin²θ D. P/D > sin²θ.

The case P/D > 1 requires: sin²θ [1 - (v^∥·v^∥)/D] > 1.
i.e., 1 - v^∥·v^∥/D > 1/sin²θ.

For sin²θ = 0.84: need 1 - v^∥·v^∥/D > 1.19.
i.e., v^∥·v^∥/D < -0.19.
i.e., v^∥·v^∥ < -0.19 D (in-plane dot product OPPOSITE sign to total D).

This is achievable when v_j and v_k project onto opposite sides of the k-plane
but their normal components align. The normal alignment gives D > 0 while
the in-plane gives v^∥·v^∥ < 0.

## THE CONSTRAINT ON C

At the max vertex: C = Σ P_{jk} s_j s_k.
The signs s_j maximize |ω|² = Σ a_j² + 2 Σ s_j s_k D_{jk}.

For |ω|² to be maximal: the sign pattern makes Σ s_j s_k D_{jk} maximal (constructive).

The same sign pattern determines C = Σ s_j s_k P_{jk}. Since P_{jk} ≠ D_{jk}:
the constructive sign pattern for D doesn't guarantee C > 0.

## BOUNDING C/|ω|² FROM BELOW

C/|ω|² = Σ s_j s_k P_{jk} / (Σ a_j² + 2 Σ s_j s_k D_{jk})

Define: ρ = Σ s_j s_k P_{jk} (the correction numerator)
        ω² = Σ a_j² + 2 Σ s_j s_k D_{jk} (the vorticity denominator)

Need: ρ/ω² ≥ -5/16.
Equivalently: ρ + 5ω²/16 ≥ 0.
i.e., Σ P s_js_k + (5/16)(Σ a² + 2Σ D s_js_k) ≥ 0.
i.e., Σ [P + 5D/8] s_js_k + 5Σa²/16 ≥ 0.
i.e., Σ [P_{jk} + (5/8)D_{jk}] s_js_k ≥ -5Σa²/16.

Define Q_{jk} = P_{jk} + (5/8)D_{jk}. Then need:
Σ Q_{jk} s_js_k ≥ -5Σa²/16.

Now: Q = P + (5/8)D = sin²θ (v·n̂)(v·n̂) + (5/8)(v·v)
   = sin²θ [D - v^∥·v^∥] + (5/8)D
   = [sin²θ + 5/8] D - sin²θ (v^∥·v^∥)

For sin²θ ≤ 1: sin²θ + 5/8 ≥ 5/8.
And: |v^∥·v^∥| ≤ |v_j^∥| |v_k^∥| ≤ a_j a_k (since v^∥ is part of v).

So: Q ≥ (5/8)D - sin²θ a_j a_k ≥ (5/8)D - a_j a_k.

For D ≥ 0 (constructive pair): Q ≥ -a_j a_k (since (5/8)D ≥ 0).
For D < 0 (destructive pair): Q ≥ (5/8)D - a_j a_k.

At the global max: Σ s_j s_k D_{jk} is maximized. So most pairs have s_j s_k D > 0.

The PROBLEM: Q can be negative for destructive pairs (where s_j s_k D < 0).

But: the total Σ Q s_j s_k = Σ P s_j s_k + (5/8)Σ D s_j s_k
   = C + (5/8)(|ω|² - Σa²)/2 = C + 5(|ω|²-Σa²)/16.

Need this ≥ -5Σa²/16.
i.e., C + 5|ω|²/16 - 5Σa²/16 ≥ -5Σa²/16.
i.e., C ≥ -5|ω|²/16. ← This is the KEY LEMMA ITSELF.

So the Q reformulation is EQUIVALENT to the Key Lemma. No free lunch.

## THE NUMERICAL INSIGHT

The worst C/|ω|² = -0.166 occurs at a specific geometric configuration.
The gap from -5/16 = -0.3125 is 47%.

The PHYSICAL reason: at the max of |ω|², the constructive interference
makes D cross-terms POSITIVE. The P cross-terms involve a sin²θ reduction
that LIMITS how much P can exceed D. The geometry of the K-shell
constrains the angles and projections, preventing C from reaching -5/16.

For a PROOF: need to formalize this geometric constraint. The most
promising path is to bound the per-pair |P - sin²θ D| and sum over pairs,
using the constraint that the sign pattern maximizes |ω|².

## 460. Per-pair analysis: P/D can exceed 1 (at 1.17 for K²=5).
## The Q reformulation is equivalent to the Key Lemma (no shortcut).
## The 47% margin comes from the geometric constraints of the K-shell.
## Formal proof needs to exploit the sign-pattern optimization + geometry.
