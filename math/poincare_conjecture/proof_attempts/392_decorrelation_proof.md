---
source: THE DECORRELATION ARGUMENT — L(s*) is bounded because L ⊥ Y
type: PROOF ATTEMPT — the analytical path to closing for all N
file: 392
date: 2026-03-29
---

## THE SETUP

Two quadratic forms on {±1}^N:
- Y(s) = s^T M_Y s = Σ D_{jk} s_js_k (vorticity coherence)
- X(s) = s^T M_X s = Σ Δ_{jk} s_js_k (gradient excess)

Both have zero diagonal and E[Y] = E[X] = 0 (over uniform random s).

The regression: L(s) = X(s) - c·Y(s) where c = Cov(X,Y)/Var(Y).
By construction: **E[L(s)·Y(s)] = 0** (L and Y are decorrelated).

The sign pattern: s* = argmax_s Y(s) (maximizes |ω|²).

The bound: R(s*) = 1 + 2X(s*)/(N+2Y(s*)) = 1 + 2(L(s*)+c·Y(s*))/(N+2Y(s*)).

Since c < 0: the c·Y(s*) term is NEGATIVE (helps).

**Need: L(s*) is bounded** (not too large positive).

## THE DECORRELATION PRINCIPLE

**CLAIM**: Since L ⊥ Y (decorrelated) and s* maximizes Y:
the value L(s*) is "typical" — bounded by O(σ_L), not by max(L).

**INTUITION**: s* is chosen for Y, not for L. From L's perspective,
s* looks like a "random" sign pattern. The decorrelation ensures that
conditioning on Y = max doesn't bias L upward.

**FORMAL STATEMENT** (to be proven):

For decorrelated quadratic forms L, Y on {±1}^N with E[LY] = 0:

    L(argmax Y) ≤ C₁ · σ_L + C₂ · (cumulant correction)

where σ_L² = Var(L) and the cumulant correction → 0 as N → ∞.

## THE GAUSSIAN ANALOGY

If L and Y were JOINTLY GAUSSIAN and independent (not just uncorrelated):

    L(argmax Y) ~ N(0, σ_L²) (independent of Y)

So L(s*) would be O(σ_L) with probability 1 - e^{-t²/2} (sub-Gaussian tail).

For RADEMACHER quadratic forms: not Gaussian, but APPROXIMATELY Gaussian
for large N (by the fourth moment theorem / CLT for U-statistics).

The correction: for degree-2 Rademacher chaos, the Berry-Esseen bound gives:

    sup_t |P(L(s)/σ_L ≤ t) - Φ(t)| ≤ C / √(r_eff(M_L))

where r_eff = ||M_L||_F² / ||M_L||_op² ≈ 2 (our key finding!).

With r_eff ≈ 2: the correction is O(1/√2) ≈ 0.7. LARGE (not small).

So the Gaussian approximation is NOT accurate for our r_eff.

## THE DIRECT BOUND (without Gaussian approximation)

**APPROACH**: Use the Hanson-Wright inequality CONDITIONALLY.

Fix Y(s*) = Y_max. Among all sign patterns s with Y(s) = Y_max:
how large can L(s) be?

The set S_max = {s ∈ {±1}^N : Y(s) = Y_max} has |S_max| = small
(typically 2-4 patterns achieve the same max, from sign symmetry).

On S_max: L(s) takes specific values. We need: max_{s ∈ S_max} L(s) is bounded.

Since |S_max| is small (O(1), not exponential in N):
max_{s ∈ S_max} |L(s)| ≤ max over O(1) values ≈ same as a typical value.

**THIS IS THE KEY**: The argmax set is SMALL. There are only O(1) sign patterns
achieving the max of Y. So L(s*) is just L evaluated at ONE (or a few) specific
sign patterns — not the max of L over exponentially many patterns.

## THE FORMAL BOUND

For a SINGLE fixed sign pattern s₀ (not chosen by L):

    E[|L(s₀)|] = 0 (zero mean)
    E[L(s₀)²] = σ_L² = 2||M_L||_F²
    E[L(s₀)⁴] = ... (fourth moment, computable)

The value L(s₀) is a fixed number (not random). But if s₀ is determined by Y
(through argmax), the expected value of L(s₀) over the ensemble of mode
configurations is related to the correlation structure.

**The correct perspective**: over the ENSEMBLE of mode configurations
(random k-vectors and polarizations), both s* and L(s*) are random.
The decorrelation E[LY] = 0 holds for EACH configuration (not just on average).

For a SPECIFIC configuration: L(s*) is a fixed number. The bound must hold
for ALL configurations.

## THE MAXIMUM-BASED BOUND

From the Hanson-Wright data:

max(L) = max_s L(s) ≤ C√N × ||M_L||_F (from r_eff ≈ 2 + HW union bound)

But L(s*) ≤ max(L) trivially. The question: is L(s*) << max(L)?

From the data:
| N | max(L)/Y_max | max(L)/(worst) | L(s*)/Y_max (actual) |
|---|-------------|----------------|---------------------|
| 5 | 0.80 | - | 0.08 |
| 8 | 0.58 | - | 0.05 |
| 20 | 0.42 | - | 0.02 |

L(s*)/Y_max is 10× smaller than max(L)/Y_max! The decorrelation suppresses
L(s*) by ~10× compared to the worst case.

## THE SMOKING GUN: L(s*) vs max(L)

The ratio L(s*)/max(L) ≈ 0.1 (from the data). This 10× suppression IS
the decorrelation effect: s* doesn't "see" L because L ⊥ Y.

If I can prove: L(s*) ≤ (1/K) × max(L) for some K ≥ 2:
then the bound closes (since max(L)/Y_max ≤ 0.80 and we need < 1.75).

Even L(s*) ≤ max(L) (trivially) gives R < 1.75 for N ≥ 5!

Wait — let me recheck. From the parallel session's data:
max(L)/Y_max worst = 0.797 (N=5).
Threshold: 5/4 + |c| = 1.25 + 0.50 = 1.75.
0.797 < 1.75. **IT ALREADY CLOSES!**

## THE REALIZATION

**max(L)/Y_max < 5/4 + |c| is ALREADY satisfied** (worst = 0.80 vs threshold 1.75).

This means: even the WORST-CASE max(L) (not just L(s*)) satisfies the bound!

The proof doesn't NEED the decorrelation suppression! The trivial bound
L(s*) ≤ max(L) combined with max(L)/Y_max < 1.75 closes the barrier!

**R ≤ 1 + 2(max(L) + c·Y_max)/(N+2Y_max) ≤ 1 + 2(0.80·Y_max - 0.50·Y_max)/(N+2Y_max)**
**= 1 + 2(0.30·Y_max)/(N+2Y_max) ≤ 1 + 0.30 = 1.30 < 13/8 = 1.625. ✓**

The question: is max(L)/Y_max < 1.75 PROVABLE for all N?

From the data: it DECREASES with N (0.80 at N=5, 0.42 at N=20).
For the CLT regime: max(L)/Y_max → σ_L/σ_Y ≈ 0.39 (always < 1.75).

## STATUS

The bound max(L)/Y_max < 5/4 + |c| closes the barrier.
Numerically: max(L)/Y_max ≤ 0.80 (worst at N=5), threshold = 1.75.
The margin is 55-76% (N=5 to N=20).

Proving max(L)/Y_max ≤ C < 5/4 + |c| for all N requires:
1. Bound max(L) from above (Hanson-Wright + r_eff ≈ 2)
2. Bound Y_max from below (min-max of vorticity, μ_N)
3. Show the ratio is universally bounded

## 392. max(L)/Y_max < 1.75 ALREADY CLOSES (margin 55%).
## The decorrelation gives further 10× suppression (L(s*) << max(L)).
## Proving max(L)/Y_max bounded requires Hanson-Wright + μ_N bound.
