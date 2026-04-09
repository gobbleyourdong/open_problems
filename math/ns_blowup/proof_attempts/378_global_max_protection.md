---
source: THE GLOBAL MAX PROTECTS — S²ê/|ω|² ≤ 0.08 at max even when Lagrange gives 0.8
type: KEY FINDING — the mechanism that prevents violation at the global max
file: 378
date: 2026-03-29
---

## THE DEFINITIVE TEST

Constructed the N=5 Lagrange-optimal config on the integer lattice:
- k-vectors: (-1,-3,2), (-3,2,-2), (-2,-1,-2), (-2,1,-2), (-3,-2,-2)
- v̂_k: projected ideal pentagonal directions onto planes ⊥ k_k
- Deviation from ideal: ≤ 0.009 (very close to Lagrange optimum)

### Results at EVERY vertex:

| Sign pattern | |ω|² | S²ê/|ω|² | |∇u|²/|ω|² | Type |
|-------------|-------|-----------|------------|------|
| (1,1,1,-1,-1) | **8.64** | **0.082** | 1.16 | GLOBAL MAX |
| (1,-1,1,-1,-1) | 1.44 | **0.774** | 2.35 | secondary |
| (-1,1,-1,1,1) | 1.44 | **0.774** | 2.35 | secondary |

At the GLOBAL MAX (|ω|² = 8.64): S²ê/|ω|² = 0.082 ≪ 0.75 ✓✓✓
At secondary vertices (|ω|² = 1.44): S²ê/|ω|² = 0.774 > 0.75 ✗

**The barrier bound is VIOLATED at secondary vertices but NEVER at the global max!**

## THE MECHANISM: SIGN PATTERN MISMATCH

The Lagrange config achieves S²ê/|ω|² = 0.8 at the sign pattern where
ALL modes are at the optimal angle γ* = arccos(1/√5).

But this sign pattern gives |ω|² ≈ N = 5 (modest).

The GLOBAL MAX sign pattern gives |ω|² = 8.64 > 5 (much higher).
At this pattern: the modes add constructively for |ω|² but the excess
terms CANCEL for S²ê. The ratio drops from 0.8 to 0.08 (10× reduction!).

### Why the global max suppresses S²ê:

1. **High |ω|²**: The global max vertex has maximal vorticity coherence.
   All modes add constructively along ê. This makes the denominator large.

2. **Excess cancellation**: The signs that maximize |ω|² DON'T maximize
   the gradient excess. Different pairs contribute excess with different
   signs at the global-max vertex. The NET excess is small.

3. **Directional spread**: At the global max, the effective d̂_k directions
   (which depend on the sign pattern through the definition of ê) are
   SPREAD in 3D. The constructive sum that builds |ω|² forces the ŝ_k
   to point in diverse directions.

## FORMAL STATEMENT

CONJECTURE (Global Max Protection): For any N-mode div-free field on T³,
at the global maximum x* of |ω| (i.e., the vertex s* = argmax_s |ω|²(s)):

    S²ê(s*) / |ω|²(s*) < 3/4

This holds even when:
- The Lagrange bound (N-1)/4 exceeds 3/4 (for N ≥ 5)
- Secondary vertices have S²ê/|ω|² > 3/4
- The per-mode amplitudes saturate the sign-flip constraint

## WHAT MAKES THE GLOBAL MAX SPECIAL

At the global max vertex s* = argmax |ω|²(s):

|ω|²(s*) = N + 2 max_s Σ s_js_k D_{jk}

This is the MAXIMUM of a quadratic form over {±1}^N. By the max condition:
|ω|²(s*) ≥ N (average over all sign patterns).

The EXCESS at s*: X(s*) = 2Σ s*_js*_k Δ_{jk}.

Key property: s* is chosen to maximize Σs_js_k D_{jk}, NOT Σs_js_k Δ_{jk}.

For the ratio: R(s*) = 1 + X(s*)/|ω|²(s*).

Since |ω|²(s*) ≥ N (from the max condition) and X(s*) is NOT maximized
(misaligned objective): R(s*) < R_max = 1 + max(X)/min(|ω|² at max).

## THE KEY INEQUALITY

At the global max: |ω|²(s*) = N + 2Y* where Y* = max_s Σs_js_k D_{jk}.

The excess: X(s*) = 2Σs*_js*_k Δ_{jk}. Since Δ = G - D:
X(s*) = 2Σs*_js*_k G_{jk} - 2Σs*_js*_k D_{jk} = (|∇u|²-N) - (|ω|²-N) = |∇u|²-|ω|².

So: R(s*) = |∇u|²/|ω|² = 1 + (|∇u|²-|ω|²)/|ω|².

At the global max: |ω|² is LARGE (≥ N + 2Y*). And |∇u|²-|ω|² is BOUNDED
(the excess doesn't grow as fast as |ω|²).

## NUMERICAL VERIFICATION OF R(s*) < 5/4

From 50K trials (file 372): worst R(s*) = 1.236 for N=2.
For N ≥ 3: all R(s*) < 1.22.

The global max condition ensures: the sign pattern that maximizes |ω|²
produces small excess relative to |ω|². This is the PROTECTION mechanism.

## PROOF PATH

To prove R(s*) < 5/4 (or even < 13/8):

1. Lower bound |ω|²(s*) ≥ f(N) (e.g., μ_N from coding theory)
2. Upper bound |X(s*)| ≤ g(N) at the SPECIFIC sign pattern s*
3. Show f grows faster than g

Step 2 is the key: bounding the excess at a sign pattern that was NOT
chosen to maximize excess. This is a CONDITIONAL EXPECTATION problem:

E[X | Y = max] = ? (where X = excess, Y = vorticity coherence)

If X and Y are negatively correlated: E[X|Y=max] < E[X] = 0. DONE.

If X and Y are uncorrelated: E[X|Y=max] ≈ 0. Also done (small excess).

The correlation: Cov(X,Y) = E[XY] = 4Σ Δ_{jk}D_{jk}.

For the Lagrange config: Δ and D have specific relationship
(Δ = -sin²α sinβsinγ while D = cosα cosβ cosγ + sinβsinγcosΦ).
The correlation depends on the geometry.

Numerically: at the global max, the excess is ~10% of |ω|² (R ≈ 1.1),
while the bound allows up to 25% (R = 5/4). The protection is substantial.

## 378. THE GLOBAL MAX PROTECTS: S²ê/|ω|² = 0.08 at max vs 0.77 at secondary.
## The sign pattern that maximizes |ω|² suppresses the excess.
## Proof needs: conditional expectation bound on excess given max vorticity.
