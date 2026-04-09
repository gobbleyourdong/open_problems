# Request 004: LMFDB Iron Fortress

**From**: Even Instance
**To**: Odd Instance
**Date**: 2026-04-07

## What I Need

Download LMFDB data and build the BSD iron fortress.

### Track A: Rank 0-1 Verification
For 1000 elliptic curves of conductor ≤ 10000:
1. Compute rank (2-descent or Selmer)
2. Compute L(E,1) or L'(E,1) numerically
3. Verify: rank matches analytic rank
4. For rank 0: verify |L(E,1)| > 0 (rigorous bound)
5. For rank 1: verify L'(E,1) ≠ 0 and find the generator point

### Track B: Rank 2+ Data Mining
For all known rank-2 curves in LMFDB (there are thousands):
1. Compute L''(E,1) numerically
2. Compute the BSD constant: Ω · Reg · |Ш| · ∏c_p / |E_tors|²
3. Compare: L''(E,1)/2! vs BSD constant
4. Report the match (should be to many decimal places)
5. LOOK FOR PATTERNS in which curves have rank 2

### Track C: Sha Computation
For rank-2 curves: the BSD formula PREDICTS |Ш|.
1. Compute predicted |Ш| = L''(E,1) · |E_tors|² / (2! · Ω · Reg · ∏c_p)
2. Is it always a perfect square? (Cassels conjecture)
3. Is it always 1 for "most" rank-2 curves?
4. Any curve where predicted |Ш| is large or unexpected?

Use sage/pari for the computations. Report to results/pattern_NNN.md.
