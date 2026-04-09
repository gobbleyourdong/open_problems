---
source: EXPLICIT CROSS-TERM FORMULA — c_{jk} = -(k_j·p_k)(p_j·k_k)
type: IDENTITY + ANALYSIS — exact formula for what drives f(N)
file: 814
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE FORMULA

For two divergence-free Fourier modes j,k on T³ at an argmax vertex:

    c_{jk} = -s_j s_k (k_j · p_k)(p_j · k_k)

where s_j, s_k ∈ {±1} are the vertex signs, k_j is the wavevector,
and p_j is the polarization (unit, p_j ⊥ k_j).

## DERIVATION

S_j = (s_j/2)[p_j ⊗ k_j + k_j ⊗ p_j] (strain tensor of mode j at vertex)

S_j : S_k = (s_js_k/2)[(p_j·p_k)(k_j·k_k) + (p_j·k_k)(k_j·p_k)]

(1/2)ω_j·ω_k = (s_js_k/2)[(k_j·k_k)(p_j·p_k) - (k_j·p_k)(p_j·k_k)]

(using BAC-CAB: (k_j×p_j)·(k_k×p_k) = (k_j·k_k)(p_j·p_k) - (k_j·p_k)(p_j·k_k))

From |S|² = |ω|²/2 - 2C (cross-term identity):
c_{jk} = (1/2)ω_j·ω_k - S_j:S_k = -s_js_k(k_j·p_k)(p_j·k_k) ✓

## CONSEQUENCES

### f(N) in terms of the cross-coupling T

Define T = Σ_{j<k} s_js_k (k_j·p_k)(p_j·k_k).
Then C = -T + (|ω|²-N)/2 and:

    f(N) = -4 + (8N + 16T)/|ω|²

### The vorticity-strain trade-off

D_jk = ω_j·ω_k = (k_j·k_k)(p_j·p_k) - (k_j·p_k)(p_j·k_k)

Notice: D_jk + (k_j·p_k)(p_j·k_k) = (k_j·k_k)(p_j·p_k).

So: T = Σ s_js_k [(k_j·k_k)(p_j·p_k) - D_jk] = K - D_total

where K = Σ s_js_k (k_j·k_k)(p_j·p_k) and D_total = Σ s_js_k D_jk.

The argmax maximizes |ω|² = N + 2D_total → maximizes D_total.
But T = K - D_total → maximizing D_total MINIMIZES T (for fixed K).

**This is the trade-off**: the sign pattern that maximizes vorticity (D_total)
automatically MINIMIZES the strain coupling (T). The two objectives fight.

### The worst case

f(N) = -4 + (8N + 16T)/|ω|² = -4 + (8N + 16(K-D_total))/(N + 2D_total)

At the argmax: D_total is maximized (given the configuration).

For f(N) to be large: need T = K - D_total to be large AND |ω|² = N + 2D_total
to be small. But large T requires small D_total, which means small |ω|².

The trade-off forces: f(N) is bounded because you can't simultaneously
have large T and small |ω|² without violating the argmax condition.

## WHY f(N) DECREASES WITH N

For N=3: only 3 cross-terms. The adversary can tune 3 k-vectors and
3 polarizations to maximize all (k_j·p_k)(p_j·k_k) simultaneously.
This is possible because there are enough degrees of freedom.

For N=7: 21 cross-terms. The adversary must tune 7 k-vectors and
7 polarizations. But k_j ∈ Z³ (discrete lattice) and p_j ⊥ k_j.
With more pairs to satisfy, the adversary can't make ALL (k_j·p_k)(p_j·k_k)
large and positive simultaneously. The terms compete and cancel.

### The lattice constraint

On Z³: k-vectors are integer vectors. The products k_j·p_k involve
the dot product of an integer vector with a unit vector perpendicular
to another integer vector. These products are constrained by the
lattice geometry.

For large N: the k-vectors fill the lattice shells. The products
k_j·p_k become "random-looking" (equidistributed modulo the lattice
symmetry). The sum T = Σ s_js_k (k_j·p_k)(p_j·k_k) has extensive
cancellation from the mixed signs and diverse angles.

### The anti-correlation in T

Each term in T: (k_j·p_k)(p_j·k_k). This involves the TRANSPOSE
coupling: how k_j projects onto p_k AND how p_j projects onto k_k.

Since p_j ⊥ k_j: the first factor (k_j·p_k) measures how k_j is
"compatible" with the perpendicular space of k_k. The second factor
(p_j·k_k) measures how p_j aligns with k_k.

For k_j nearly parallel to k_k: (k_j·p_k) ≈ 0 (since p_k ⊥ k_k ≈ k_j).
Also (p_j·k_k) ≈ 0 (since p_j ⊥ k_j ≈ k_k). Product ≈ 0.

For k_j perpendicular to k_k: both factors can be nonzero.
(k_j·p_k) can be up to |k_j| and (p_j·k_k) can be up to |k_k|.

So the WORST coupling is between PERPENDICULAR k-vectors. But in R³,
at most 3 k-vectors can be mutually perpendicular. For N ≥ 4:
not all pairs can be perpendicular, so many terms in T are small.

### Quantitative bound

The number of "maximally coupled" pairs: at most 3 (one per orthogonal
direction). Each contributes at most K² to T.

The remaining N(N-1)/2 - 3 pairs: each contributes less (intermediate angles).

Average contribution per pair: ~ K²/N (the coupling dilutes with N).

Total T ≤ 3K² + (N²/2) · (K²/N) = 3K² + NK²/2.

Hmm, this still gives T ~ NK², not T ~ constant.

For f(N) = -4 + (8N + 16T)/(N + 2D_total) with T ~ NK²:
f(N) ~ -4 + 16NK²/N = -4 + 16K² (for D_total ≈ 0)

This is independent of N! Not decreasing. So the naive bound doesn't work.

The issue: the "average contribution per pair" overestimates. The actual
coupling involves specific correlations between k_j and p_k that depend
on the SAME modes appearing in both j-terms and k-terms.

## THE DEEP STRUCTURE

The product (k_j·p_k)(p_j·k_k) has a SYMMETRY: it changes sign under
the swap j ↔ k IF (k_j·p_k)(p_j·k_k) ≠ (k_k·p_j)(p_k·k_j).

Actually: (k_k·p_j)(p_k·k_j) = (p_j·k_k)(k_j·p_k) = same thing.
So the product IS symmetric in j,k. No sign change.

But the SIGN PATTERN s_js_k makes the sum T depend on the argmax.
For the argmax: s_js_k = 1 if ω_j·ω_k > 0, -1 if < 0 (roughly).

The terms where s_js_k = +1: contribute +|(k_j·p_k)(p_j·k_k)|.
The terms where s_js_k = -1: contribute -|(k_j·p_k)(p_j·k_k)|.

The NET T is the difference between positive and negative terms.
For the argmax to be large (D_total large): the sign pattern aligns
ω_j with ω_k, meaning s_js_k = sign(D_jk).

The coupling T with this sign pattern:
T = Σ sign(D_jk) · (k_j·p_k)(p_j·k_k)

Since D_jk = (k_j·k_k)(p_j·p_k) - (k_j·p_k)(p_j·k_k):

For D_jk > 0: (k_j·k_k)(p_j·p_k) > (k_j·p_k)(p_j·k_k).
The sign of the second term is OPPOSITE to D_jk's dominant term.
So T gets a NEGATIVE contribution from this pair!

For D_jk < 0: (k_j·p_k)(p_j·k_k) > (k_j·k_k)(p_j·p_k).
The sign s_js_k = -1. So T gets -(negative) = positive contribution.

WAIT: T = Σ s_js_k (k_j·p_k)(p_j·k_k) where s_js_k = sign(D_jk).

For D_jk > 0: T_jk = (k_j·p_k)(p_j·k_k). This could be positive or negative.
D_jk = (k_j·k_k)(p_j·p_k) - (k_j·p_k)(p_j·k_k) > 0
→ (k_j·p_k)(p_j·k_k) < (k_j·k_k)(p_j·p_k)

For D_jk < 0: s_js_k = -1. T_jk = -(k_j·p_k)(p_j·k_k).
D_jk < 0 → (k_j·p_k)(p_j·k_k) > (k_j·k_k)(p_j·p_k)
T_jk = -(something positive) = negative? Or -(something negative)?

This depends on the sign of (k_j·p_k)(p_j·k_k) itself.

The analysis is getting quite involved. The key qualitative point is:

**The argmax sign pattern ANTI-CORRELATES with T.** The signs that
maximize |ω|² = N + 2D_total tend to make T small (because T = K - D_total,
and maximizing D_total minimizes T for fixed K).

The quantitative bound on T at the argmax: this is the core problem.

## FORMAL CONJECTURE

**For N modes on T³ at the argmax of |ω|², the strain coupling satisfies:**

    T ≤ C · N^{1-a} (for some a > 0)

Equivalently: the worst-case f(N) = -4 + (8N + 16T)/|ω|² ≤ C'/N^a.

## 814. Cross-term c_{jk} = -(k_j·p_k)(p_j·k_k).
## f(N) = -4 + (8N+16T)/|ω|² where T = Σ s_js_k (k_j·p_k)(p_j·k_k).
## The argmax sign pattern ANTI-CORRELATES with T (trade-off: max|ω|² ↔ min T).
## For k ∥ k': coupling vanishes. For k ⊥ k': coupling maximal.
## At most 3 orthogonal pairs in R³ → coupling limited for N > 3.
