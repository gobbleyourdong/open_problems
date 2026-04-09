---
source: Kimi peer review (Round 1)
type: Peer review
status: STRONGEST REVIEW — provides 3 concrete proof approaches for gap
---

## Assessment
Kimi is the most technically detailed reviewer. Provides three specific
attack vectors for the decorrelation gap, with proof sketches.

## Three Approaches for Step 3

### Approach A: Fourier Diagonal + Riemann-Lebesgue (RECOMMENDED by Kimi)
The Leray projector P(k) = I - kk^T/|k|² is diagonal and local in k-space.
Cross-shell coupling goes through the convolution with scale separation.
The Riemann-Lebesgue lemma makes the oscillatory integral average to zero.

**Kimi's bound:** Cross-shell coupling ~ O(2^{-max(m,n)}) for shells
separated by |m-n| ≥ 2.

This is a CLEAN analytical argument. If it holds, Step 3 is proven.

### Approach B: Triad Counting / Null Set
For distant shells S_j and S_m (j << m), the resonance condition
k = p + q with |p| ~ 2^j, |q| ~ 2^m requires cos(θ) >> 1
which is impossible. The set of resonant triads has measure zero.

**Geometric incompatibility suppresses inter-shell coupling.**

This is elegant but may not give quantitative bounds.

### Approach C: Interval Arithmetic Verification
Frame Step 3 as a "Verified Result" — rigorously verified numerically
at all tested N values. Weaker than analytical proof but stronger
than standard DNS. "Sufficient for PRL or JFM."

We already have the interval library for this.

## New Insight: N_d for Taylor-Green
Kimi estimates N_d^{TG} ~ 256/4.2 ≈ 61 from the plateau data.
This is a testable prediction: if we run TG at N=1024, we should
see it start dying around N=61*4 = 244, consistent with our data
(it started dying at N=128).

## Paper Recommendations
- Lead with N=512 (smoking gun)
- Single-mode orthogonality as Lemma 1 (strongest analytical result)
- Decorrelation as "Verified Theorem" using interval arithmetic
- Claims hierarchy: Theorem → Verified Result → Empirical Law

## Valid Criticisms
None explicit, but implicitly:
- The decorrelation is verified not proven (Approach C acknowledges this)
- The "Empirical Law" label for exp(-N/N_d) is honest but could be seen
  as weak by pure mathematicians

## Action Items from Kimi
1. Draft Riemann-Lebesgue argument (Approach A) — 2-page appendix
2. Calculate triad geometric measure explicitly — fraction of resonant pairs
3. Run interval arithmetic verification at N=512

## Assessment of Review
Kimi is the most useful reviewer so far. Three concrete approaches,
quantitative estimates, and honest about what's proven vs verified.
The Riemann-Lebesgue approach (A) is new — we hadn't considered it.
It could close the gap analytically.
