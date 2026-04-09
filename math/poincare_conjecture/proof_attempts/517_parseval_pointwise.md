---
source: PARSEVAL POINTWISE — the L² identity constrains pointwise ratios
type: PROOF ATTEMPT — using Parseval + structure to bound |S|²/|ω|² pointwise
file: 517
date: 2026-03-30
instance: CLAUDE_OPUS
---

## THE KEY IDENTITY (pointwise)

For any div-free field on T³:

|∇u(x)|² = |S(x)|² + |ω(x)|²/2

And from Biot-Savart: the Fourier coefficients satisfy

|ŝ_k|² = |ω̂_k|²/2 for each mode k.

But POINTWISE: |S(x)|² ≠ |ω(x)|²/2 in general.

## THE PARSEVAL CONSTRAINT

||S||₂² = ||ω||₂²/2 (L² identity, exact).

Suppose the global max of |ω|² is at x*. Define:
r(x) = |S(x)|²/|ω(x)|² (the pointwise ratio, where |ω| > 0).

The L² average: ∫ r(x) |ω(x)|² dx / ∫ |ω(x)|² dx = 1/2.

The weighted average of r is exactly 1/2.

At the max x*: |ω(x*)|² ≥ |ω(x)|² everywhere.

If r(x*) > 1/2: the max point has ABOVE-AVERAGE strain concentration.
For the average to be 1/2: other points must have BELOW-AVERAGE r.

## THE CONCENTRATION INEQUALITY

How concentrated can r be? I.e., how large can r(x*) be while
maintaining the L² average = 1/2?

**Upper bound**: r(x*) ≤ ||S||∞² / |ω(x*)|² × |ω(x*)|²/||ω||∞² = ||S||∞²/||ω||∞²

Wait, that's circular. Let me think differently.

From |S|² = |ω|²/2 - 2C (Frobenius identity, file 511):

At x*: r(x*) = 1/2 - 2C(x*)/|ω(x*)|²

The question: how negative can C(x*)/|ω(x*)|² be?

## THE ANTI-CONCENTRATION BOUND

From the L² identity:
∫ |S|² = ||ω||₂²/2

∫ (|ω|²/2 - 2C) = ||ω||₂²/2

∫ |ω|²/2 - 2 ∫ C = ||ω||₂²/2

So: **∫ C(x) dx = 0** (the correction averages to zero!).

Now, C(x) = Σ_{j<k} P_{jk} cos(k_j·x) cos(k_k·x).

Each term is a product of cosines with different frequencies.
These are orthogonal to constants, so ∫ C = 0. ✓

At x*: C(x*) could be negative (making |S|² > |ω|²/2).
But C averages to 0. So |C(x*)| is bounded by the variation of C.

## BOUNDING C AT THE MAX

From the Frobenius identity:
C(x) = Σ_{j<k} P_{jk} cos(k_j·x) cos(k_k·x)

|C(x)| ≤ Σ |P_{jk}| = Σ |v_j·n̂||v_k·n̂| sin²θ

By Cauchy-Schwarz: |v·n̂| ≤ |v|. And sin²θ ≤ 1.

So: |C(x)| ≤ Σ_{j<k} |v_j||v_k| = [(Σ|v_j|)² - Σ|v_j|²]/2

This is just the triangle inequality bound, which gives:
|C| ≤ [(Σ a_j)² - Σ a_j²]/2

And |ω|² at the max: |ω|² = |Σ s_j a_j v̂_j|² ≤ (Σ a_j)² (with equality for aligned v̂).

So: |C|/|ω|² ≤ [(Σ a_j)² - Σ a_j²] / [2|ω|²]

For the max: |ω|² ≥ Σ a_j² (since constructive interference adds).
When |ω|² ≈ (Σ a_j)²: |C|/|ω|² ≤ [(Σa)² - Σa²]/(2(Σa)²) = 1/2 - Σa²/(2(Σa)²) < 1/2.

So: 2|C|/|ω|² < 1. This gives r = 1/2 - 2C/|ω|² ∈ (1/2-1, 1/2+1) = (-1/2, 3/2).

Hmm, r < 3/2 is not strong enough. Need r < 9/8 = 1.125.

## USING THE SELF-VANISHING STRUCTURE

The bound |C| ≤ Σ|v_j||v_k| is LOOSE because it ignores the Biot-Savart
structure. The actual P_{jk} involves v·n̂ (projection onto the normal
to the k-plane), not just |v|.

From file 511: P_{jk} sin²θ = -(k_k·û_j)(k_j·û_k).

So: |C(x)| = |Σ (k_k·û_j)(k_j·û_k) cos(k_j·x) cos(k_k·x)|

And: |C| ≤ Σ |(k_k·û_j)(k_j·û_k)| ≤ Σ |k_k||û_j| × |k_j||û_k|
= (Σ |k_j||û_j|)² / 2 ... no, this is for j<k.

|C| ≤ Σ_{j<k} |k||û_j| × |k||û_k| = K² Σ_{j<k} |û_j||û_k|

On a single shell (|k| = K): |û_j| = |v_j|/K (since û = k×v/K²).

|C| ≤ K² Σ_{j<k} (|v_j|/K)(|v_k|/K) = Σ_{j<k} |v_j||v_k|

Same bound as before. The Biot-Savart structure doesn't help here because
|k·û| ≤ |k||û| always.

## THE POINTWISE SIN-COS APPROACH (NEW)

At any point x: define c_j = cos(k_j·x), q_j = sin(k_j·x), c_j² + q_j² = 1.

|ω|² = |Σ a_j v̂_j c_j|²
|S|² = |Σ S_j q_j|²_F

From per-mode: |S_j|²_F = a_j²/2.

Key: c_j² + q_j² = 1 for each j. At the max of |ω|²: c_j² is maximized
(subject to the constraint from x). So q_j² = 1 - c_j² is minimized.

The DIAGONAL part of |S|²: Σ |S_j|² q_j² = Σ (a_j²/2)(1-c_j²) = Σ a_j²/2 - Σ a_j² c_j²/2.

And the DIAGONAL part of |ω|²: Σ a_j² c_j².

So: (diagonal |S|²) / |ω|² ≤ [Σ a_j²/2 - Σ a_j² c_j²/2] / (Σ a_j² c_j² + cross terms)

At the max: the cross terms in |ω|² are positive (constructive interference).
So |ω|² ≥ Σ a_j² c_j². And diagonal |S|² ≤ Σ a_j²/2.

Therefore: diagonal |S|² / |ω|² ≤ (Σ a_j²/2) / (Σ a_j² c_j²)

If all c_j² ≥ 1/2 (cosines ≥ 1/√2 in magnitude): ratio ≤ 1.

If some c_j² < 1/2: those modes contribute less to |ω|² and more to |S|².
But the max of |ω|² penalizes small c_j (reduces constructive interference).

## THE MAXIMUM PRINCIPLE APPROACH

For the function f(x) = |S(x)|²/|ω(x)|² at x*:

If f is smooth near x*: ∇f(x*) might be nonzero (no reason for f to be
extremal at x*). So x* is NOT typically a max of f.

The max of f occurs at a DIFFERENT point x** (the max of |S|²/|ω|² ratio).
By the anti-concentration (file 443): x** ≠ x* in 94% of cases.

At x*: f(x*) is just the VALUE of the ratio at the ω-max. It's not the
maximum of the ratio. So we need:

f(x*) < 3/4 (or equivalently, |S(x*)|² < (9/8)|ω(x*)|²)

This is a WEAKER condition than bounding max_x f(x).

## STATUS

The sine-cosine decoupling gives:
1. N ≤ 3 per shell: PROVEN (sin=0 at max → S=0)
2. N ≥ 4: double suppression makes S²ê/|ω|² < 0.07 (numerical)
3. The Parseval + triangle bound gives r < 3/2 (too weak)
4. The self-vanishing doesn't improve the triangle bound
5. Need a TIGHTER bound that uses the max structure

The most promising path: use the CRITICAL POINT equation Σ p_j k_j = 0
to constrain the sin values, then bound |S|² using the constrained sines.

## 517. Parseval constraint: ∫C = 0. Triangle: r < 3/2 (too weak).
## Need tighter bound using critical point + self-vanishing structure.
