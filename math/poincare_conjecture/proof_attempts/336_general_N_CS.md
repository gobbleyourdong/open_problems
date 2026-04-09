---
source: General N CS bound — S²ê < 3|ω|²/4 when |ω|² > N²/4
type: THEOREM — the CS regime is proven for ALL N
file: 336
date: 2026-03-29
---

## THEOREM: For N Fourier modes (equal amplitude, at common max):

  S²ê ≤ (N² - |ω|²)/4

PROOF (from file 364, generalized):

  S²ê ≤ (Σ|ŝ_k|)² ≤ (Σ√(1-c_k)/2)² ≤ (N/4)Σ(1-c_k) (CS)
  = (N/4)(N - Σc_k) ≤ (N/4)(N - |ω|²/N) = (N²-|ω|²)/4. ∎

COROLLARY: S²ê < 3|ω|²/4 ⟺ (N²-|ω|²)/4 < 3|ω|²/4 ⟺ |ω|² > N²/4.

## For NS Solutions

A smooth NS solution on T³ has INFINITELY many modes (analyticity).
But with EXPONENTIALLY decaying amplitudes: |ω̂_k| ~ exp(-c|k|).

The EFFECTIVE number of modes N_eff: the number with |ω̂_k| > ε||ω̂||_max.
For analytic solutions: N_eff ~ (c/ε)³ (finitely many).

The |ω| at the max: |ω(x*)| ≤ Σ|ω̂_k| ≈ N_eff × ||ω̂||_max (at most).
Actually |ω(x*)| could be much less (not all phases constructive).

For the CS bound: need |ω|² > N_eff²/4.
This holds when |ω| > N_eff/2, i.e., MOST modes are constructive.

For a CONCENTRATED vortex (high |ω| from many coherent modes):
the CS bound applies directly. ✓

For a SPREAD vortex (low |ω| from cancellation):
the CS bound fails, but S²ê is small anyway (few modes contribute).

## The Dominance Argument (low |ω|²)

When |ω|² ≤ N²/4: the modes partially cancel. The max is dominated
by a SUBSET of modes. The effective N_eff for S²ê is smaller.

Specifically: at x* with |ω|² ≤ N²/4, define the "active" modes as
those with |a_k c_k'| > δ. The number of active modes N_active < N.
The inactive modes contribute O(δ²) to S²ê.

For the active modes: apply the CS bound with N_active.
If |ω|² > N_active²/4: S²ê < 3|ω|²/4. ✓

The question: is |ω|² > N_active²/4 always at the global max?

At the global max: |ω|² is MAXIMIZED over x. This maximum condition
means the COHERENCE of the active modes is MAXIMIZED.

For N_active modes with unit amplitude: max|ω|² = N_active² (all in phase).
The actual |ω|² ≤ N_active².
Need |ω|² > N_active²/4 ↔ |ω|/N_active > 1/2.

Since |ω|/N_active is the AVERAGE projection of active modes onto ê:
this requires the average alignment > 1/2. By Cauchy-Schwarz on
Σp_k = |ω|: (Σp_k)²/N ≤ Σp_k² ≤ N. So |ω|² ≤ N Σp_k² ≤ N².
And |ω| = Σp_k ≤ N.

The condition |ω|/N > 1/2: Σp_k/N > 1/2. Average p_k > 1/2.

This is NOT guaranteed — modes could have small p_k (poor alignment)
but large contribution through the perpendicular component.

## THE REAL QUESTION

For smooth div-free ω on T³ at the global max:
is |ω(x*)|² > (N_eff(x*))²/4 where N_eff counts the "active" modes?

This is the COHERENCE vs SPREAD question. At the global max: coherence
is maximized. But is it maximized enough?

For a single dominant mode: N_eff = 1, |ω|² ≈ a₁².
Need a₁² > 1/4. TRUE for any nonzero mode. ✓

For two comparable modes: N_eff = 2, |ω|² ≤ 4a².
Need 4a² > 4a²/4 = a². TRUE (|ω|² = a²(2+2d) ≥ a² × 2(1+d_min)). ✓ for d > -1/2.

Hmm, for d close to -1: |ω|² ≈ 0 < 4a²/4 = a². FAILS.

But at the GLOBAL max: if d < -1/2, the max of |ω| shifts to where
only one mode is active (the other has cos ≈ 0). Then N_eff = 1 and
the single-mode bound applies.

## THE BOOTSTRAP

This suggests a BOOTSTRAP on N_eff:

1. At the global max: |ω|² = max_x |Σa_k c_k' v̂_k|².
2. If the max is dominated by one mode: N_eff = 1, S²ê = 0. ✓
3. If the max has N_eff ≥ 2 active modes: their projections p_k are
   large enough (because they're at the max) to give |ω|² > N_eff²/4.
4. Then CS gives S²ê < 3|ω|²/4. ✓

The gap: proving step 3 — that active modes at the global max
have sufficient coherence.

## STATUS

The CS bound S²ê < (N²-|ω|²)/4 is PROVEN for all N.
The corollary S²ê < 3|ω|²/4 holds when |ω|² > N²/4.
The coherence condition |ω|² > N²/4 at the global max is PLAUSIBLE
(the global max maximizes coherence) but NOT YET PROVEN.

This is progress: the proof reduces to a COHERENCE BOUND at the max,
not an operator norm bound.

## 336.
