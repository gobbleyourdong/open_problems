---
source: FLOOR GROWTH VIA K BOUND — if K is bounded, f(N) → 0
type: PROOF ATTEMPT — the simplest route to floor growth
file: 816
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE SETUP

f(N) = 4 + 16T/|ω|² where T = K - D_total.

K = Σ_{j<k} s_js_k (k_j·k_k)(p_j·p_k) (the "k-p coupling")
D_total = Σ_{j<k} s_js_k D_jk (the "vorticity coupling")
|ω|² = Σ|k_j|² + 2D_total

## KEY CLAIM

**If |K| ≤ C_K for all N (bounded independently of N), then f(N) → 0.**

Proof: At the argmax, |ω|² is maximized. For N modes with |k_j| ≥ 1:
|ω|² ≥ Σ|k_j|² ≥ N (at the argmax, |ω|² ≥ N by the R³ dimension argument).

Actually, |ω|² = Σ|k_j|² + 2D_total, and at the argmax, D_total ≥ 0
(the optimal signs make the total vorticity at least as large as
the individual contributions).

So |ω|² ≥ N. And T = K - D_total ≤ K (since D_total ≥ 0).

f = 4 + 16T/|ω|² ≤ 4 + 16K/N ≤ 4 + 16C_K/N → 4 as N → ∞.

But we need f → 0, not f → 4. So K bounded gives f → 4 (constant), not 0.

THE ISSUE: f → 4 means |S|²/|ω|² → 1/2 (the per-mode identity average).
We need |S|²/|ω|² → 0, which requires T → -|ω|²/4 (strongly negative).

K bounded + D_total ~ N gives T ~ -N. And T/|ω|² ~ -N/(2N) = -1/2.
f = 4 + 16(-1/2) = 4 - 8 = -4. But f ≥ 0! Contradiction.

So D_total can't be that large. Let me reconsider.

## BOUND ON D_total

D_total = Σ s_js_k D_jk where D_jk = (k_j·k_k)(p_j·p_k) - (k_j·p_k)(p_j·k_k).

|D_jk| ≤ |(k_j·k_k)(p_j·p_k)| + |(k_j·p_k)(p_j·k_k)| ≤ |k_j||k_k|(1+1) = 2K²

(where K is the max wavenumber, |k_j| ≤ K for all j)

D_total ≤ Σ |D_jk| ≤ N(N-1)K²

And |ω|² = Σ|k_j|² + 2D_total ≤ NK² + 2N²K² = N²K²(1+1/N) ≈ N²K².

Hmm, this gives |ω|² up to N²K², which is quadratic in N.

With T = K - D_total: T/|ω|² = (K - D_total)/(Σ|k_j|² + 2D_total).

For D_total large: T/|ω|² → (K - D_total)/(2D_total) → -1/2 (for D_total → ∞).

f = 4 + 16(-1/2) = -4. But f ≥ 0.

This means D_total CAN'T be much larger than |K|. The constraint f ≥ 0 gives:
4 + 16T/|ω|² ≥ 0 → T ≥ -|ω|²/4 → K - D_total ≥ -(Σ|k_j|² + 2D_total)/4
→ 4K - 4D_total ≥ -Σ|k_j|² - 2D_total → 4K + Σ|k_j|² ≥ 2D_total
→ D_total ≤ (4K + Σ|k_j|²)/2

So D_total is bounded by K + Σ|k_j|²/2. For K bounded (|K| ≤ C_K):
D_total ≤ 2C_K + Σ|k_j|²/2

And |ω|² = Σ|k_j|² + 2D_total ≤ Σ|k_j|² + 4C_K + Σ|k_j|² = 2Σ|k_j|² + 4C_K

This is at most 2NK² + 4C_K (linear in N).

## THE RIGHT APPROACH: BOUND K PER PAIR

K = Σ s_js_k (k_j·k_k)(p_j·p_k)

Each term: |(k_j·k_k)(p_j·p_k)| ≤ |k_j||k_k| ≤ K² (max wavenumber squared).

For N(N-1)/2 terms: |K| ≤ N²K²/2.

This is NOT bounded — K can grow quadratically with N.

So the approach "K is bounded" FAILS. K grows with N.

## THE CORRECT RELATIONSHIP

At the argmax: the signs s_j maximize D_total = Σ s_js_k D_jk.

K = Σ s_js_k (k_j·k_k)(p_j·p_k) uses the SAME signs.

D_jk = (k_j·k_k)(p_j·p_k) - (k_j·p_k)(p_j·k_k)

K_jk = (k_j·k_k)(p_j·p_k)

So D_jk = K_jk - T_jk where T_jk = (k_j·p_k)(p_j·k_k).

K = Σ s_js_k K_jk = D_total + T (since T = Σ s_js_k T_jk and D = K - T).

This is just the identity K = D_total + T. Rearranging: T = K - D_total.

So f = 4 + 16(K-D_total)/|ω|² = 4 + 16K/(Σ|k_j|²+2D_total) - 16D_total/(Σ|k_j|²+2D_total)

= 4 + 16K/|ω|² - 16D_total/|ω|²

= 4 + 16K/|ω|² - 8(|ω|²-Σ|k_j|²)/|ω|²

= 4 + 16K/|ω|² - 8 + 8Σ|k_j|²/|ω|²

= -4 + 8Σ|k_j|²/|ω|² + 16K/|ω|²

For the ARGMAX: the sign pattern maximizes |ω|². A larger |ω|² makes the
ratios Σ|k_j|²/|ω|² and K/|ω|² SMALLER (since |ω|² is in the denominator).

So the argmax DIRECTLY makes f smaller! This is the mechanism.

## THE ARGMAX MINIMIZES f

**Lemma**: Among all sign patterns for a fixed configuration, the argmax
of |ω|² gives the SMALLEST f.

Proof: f = -4 + 8Σ|k_j|²/|ω|² + 16K/|ω|².
Σ|k_j|² is independent of signs. K depends on signs but is bounded.
|ω|² is maximized at the argmax.
For the terms Σ|k_j|²/|ω|² and K/|ω|²: the argmax (max |ω|²) minimizes
these ratios (assuming K > 0... K can be negative).

Wait: if K < 0, then 16K/|ω|² is negative, and the argmax makes it
LESS negative (closer to 0). So the argmax could increase 16K/|ω|².

The net effect depends on the relative sizes. But the dominant term
8Σ|k_j|²/|ω|² IS minimized by the argmax.

## A CLEANER BOUND

From f = 4 + 16T/|ω|²:

At the argmax: D_total is maximized. Write D_max for this maximum.

T = K - D_max. And |ω|² = Σ|k_j|² + 2D_max.

f = 4 + 16(K - D_max)/(Σ|k_j|² + 2D_max)

For large D_max (strong constructive interference):
f ≈ 4 + 16(K - D_max)/(2D_max) ≈ 4 + 8K/D_max - 8 = -4 + 8K/D_max

If K/D_max → 0 as N → ∞: f → -4. But f ≥ 0, so this can't happen.

The constraint f ≥ 0 gives: K ≥ D_max/2 (approximately, for large D_max).

So D_max ≤ 2K. The vorticity coupling is bounded by twice the k-p coupling!

## THE UPPER BOUND ON D_max

**Key inequality**: D_total ≤ 2K (at the argmax, from f ≥ 0).

Wait, more precisely: f ≥ 0 gives 4 + 16(K-D_total)/(Σ|k_j|²+2D_total) ≥ 0.

4(Σ|k_j|²+2D_total) + 16(K-D_total) ≥ 0
4Σ|k_j|² + 8D_total + 16K - 16D_total ≥ 0
4Σ|k_j|² + 16K ≥ 8D_total
D_total ≤ (Σ|k_j|² + 4K)/2

With K = Σ s_js_k(k_j·k_k)(p_j·p_k): |K| ≤ N²K_max²/2.

D_total ≤ Σ|k_j|²/2 + 2K ≤ NK_max²/2 + N²K_max²

So D_total is at most O(N²). And |ω|² ≤ Σ|k_j|² + 2D_total ≤ O(N²).

For f to be small: need T/|ω|² → -1/4. With T = K - D_total and
|ω|² = Σ|k_j|² + 2D_total: need K - D_total → -(Σ|k_j|² + 2D_total)/4.
→ 4K - 4D_total → -Σ|k_j|² - 2D_total
→ 4K + Σ|k_j|² → 2D_total
→ D_total → 2K + Σ|k_j|²/2

This is EXACTLY the saturation of the f ≥ 0 constraint!

## CONCLUSION

**f(N) → 0 iff the f ≥ 0 constraint is asymptotically saturated at the
worst-case configuration.**

The SOS data shows f → 0, meaning the worst case gets closer and closer
to the boundary |S|² = 0 (strain vanishes). This happens because:

1. The argmax maximizes D_total (constructive vorticity)
2. D_total → (Σ|k_j|² + 4K)/2 (saturating the f ≥ 0 bound)
3. T = K - D_total → K - (Σ|k_j|² + 4K)/2 = -Σ|k_j|²/2 - K
4. f = 4 + 16(-Σ|k_j|²/2 - K)/(Σ|k_j|² + 4K + Σ|k_j|²)
   = 4 + 16(-Σ|k_j|²/2 - K)/(2Σ|k_j|² + 4K)
   = 4 - 8 = -4 ???

This gives f = -4, which contradicts f ≥ 0. So the saturation CAN'T
be exact — there must be a gap.

The GAP between f and 0 is determined by how close D_total can get
to the saturation bound. The floor growth question is: how fast does
this gap close with N?

## 816. f = 4+16T/|ω|² = 4+16(K-D_total)/(Σ|k|²+2D_total).
## Argmax maximizes D_total. f ≥ 0 constrains D_total ≤ (Σ|k|²+4K)/2.
## f → 0 iff saturation is approached. Rate = floor growth exponent.
## The gap between D_total and its upper bound determines f(N).
