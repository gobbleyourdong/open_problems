---
source: PER-MODE BOUND — shift from per-pair to per-mode analysis for N≥4
type: NEW DIRECTION — the per-pair bound fails for N≥4, need per-mode structure
file: 708
date: 2026-03-31
instance: MATHEMATICIAN
---

## WHY PER-PAIR FAILS FOR N≥4

The N=4 worst case shows Q_pair = -6.65 for a SINGLE pair (2,3) with
orthogonal k-vectors. The per-pair bound Q_pair ≥ -2 assumed the pair
is in the constructive domain (D > 0), but at the vertex max, some
pairs have ss=+1 despite D < 0 (forced by other pairs' sign preferences).

The per-pair framework assumed each pair is independently optimized.
For N≥4: pairs share modes, and the sign pattern is a GLOBAL optimization.
A pair can be "sacrificed" (Q_pair very negative) if other pairs benefit.

## THE PER-MODE APPROACH

Instead of bounding Σ Q_pair, bound the TOTAL Q using per-mode contributions.

Q = 9|ω|² - 8|S|²

|ω|² = |Σ sⱼvⱼ|² = Σ|vⱼ|² + 2Σᵢ<ⱼ sᵢsⱼDᵢⱼ

|S|² involves the strain from ALL modes. The self-vanishing identity gives:
|S·ê|² = Σ terms involving (aⱼ/2)sinγⱼ (per-mode contribution).

But |S|² ≠ Σ|Sⱼ|² (there are cross-terms). So the per-mode decomposition
of |S|² is complicated.

## THE AVERAGING APPROACH (revisiting)

From file 706: E_s[|ω_s|²] = N (average over sign patterns = N).
So max_s |ω_s|² ≥ N.

Similarly: E_s[|S_s|²] = Σ|Sⱼ|² = N/2 (the strain average is N/2
since |Sⱼ|² = |vⱼ|²/2 = 1/2 per unit-amp mode).

So: E_s[Q_s] = 9N - 8(N/2) = 9N - 4N = 5N > 0.

The AVERAGE Q over sign patterns is 5N > 0. But we need Q > 0 at
the MAX sign pattern (which might not be the average).

## THE CAUCHY-SCHWARZ APPROACH

At the max sign pattern s*: |ω|²_max ≥ N.

The strain at s*: |S|² = |ω|²/2 - 2C.

For Q > 0: need 9|ω|² > 8|S|² = 4|ω|² - 16C, i.e., 5|ω|² + 16C > 0.

From |ω|² ≥ N: 5|ω|² ≥ 5N.
Need: 16|C| < 5N, i.e., |C| < 5N/16.

|C| = |Σ s*ᵢs*ⱼPᵢⱼ| ≤ Σ|Pᵢⱼ| ≤ C(N,2) × max|P|.

max|P| ≤ 1/4 [from coupling: |P| = sin²θ|n₁n₂| ≤ sin²θ → not tight enough].

Actually: max|P| per pair ≤ max c(1-c) = 1/4 was derived for
constructive pairs. For general pairs (including ss=+1 with D<0):
|P| = sin²θ |n₁n₂| ≤ sin²θ ≤ 1. The coupling bound c(1-c) ≤ 1/4
doesn't apply when D < 0.

So: |C| ≤ C(N,2) × 1 = N(N-1)/2.
5N/16 < N(N-1)/2 for N ≥ 2. Fails!

## THE ISSUE

The per-pair |P| bound (without the D > 0 constraint) is just |P| ≤ 1.
This is too loose. The actual |P| at the max is bounded by the coupling,
but only when D > 0. For pairs with D < 0 at the max: |P| can reach
sin²θ (= 1 for orthogonal k).

## THE SAVING GRACE

Pairs with D < 0 at the max have s*ᵢs*ⱼ = +1 (same sign) despite
destructive D. This means the pair HURTS |ω|². But the other pairs
overcompensate.

The contribution of this pair to Q:
s*Q_pair = 5D + 8P. With D < 0 and P < 0 (anti-correlated normals):
s*Q_pair = 5×(negative) + 8×(negative) = very negative.

BUT: the pair also reduces |ω|² by 2|D|. The 5|ω|² term already
accounts for this reduction. The TOTAL Q = 5|ω|² + 16C includes
the |ω|² reduction.

So: Q = 5(N + 2Σ s*D) + 16Σ s*P
    = 5N + 10Σ s*D + 16Σ s*P
    = 5N + 2Σ s*(5D + 8P)
    = 5N + 2Σ s*Q_pair

For the pairs with s*=+1 and D<0: both the s*D term (negative)
and the s*P term (can be negative) contribute to reducing Q.

## THE OBSERVATION FROM THE N=4 DATA

At the N=4 worst:
- 3 positive pairs: Σ s*Q = +6.14
- 3 negative pairs: Σ s*Q = -7.85 (dominated by one pair at -6.65)
- Net: Σ s*Q = -1.71
- Q = 5×4 + 2×(-1.71) = 20 - 3.42 = 16.58. Hmm, but Q/|ω|² = 2.32.

Wait: Q = 16.58 and |ω|² = 16.58/2.32 ≈ 7.1. Not 4 (since amps aren't unit).

The ratio Q/|ω|² = 2.32 means C/|ω|² = (2.32-5)/16 = -0.168.
This matches the known N=4 worst (-0.173). Close.

## THE GENERAL ARGUMENT (sketch)

For GENERAL N: Q/|ω|² > 0 because:
1. The diagonal gives 5N/|ω|² ≥ 5 (from |ω|² ≤ N² by triangle ineq)
   Wait: 5N/|ω|² ≥ 5/N (from |ω|² ≤ N²). Too small for large N.

Actually: 5N/|ω|² where |ω|² = N + 2Σ s*D.
For |ω|² ≤ N²: Q/|ω|² ≥ (5N + 2Σ s*Q_pair)/N².

This approach doesn't close. The proof needs a STRUCTURAL argument
that connects the negative Q_pairs to the |ω|² they create.

## 708. Per-pair fails for N≥4. Per-mode or structural approach needed.
## N=4 worst has Q_pair = -6.65 for one pair (orthogonal k, D<0, P<0).
## The total Q is still positive (Q/|ω|² = 2.32) because other pairs compensate.
## The proof for general N needs the sign-pattern optimization structure.
