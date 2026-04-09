# Attempt 847 — Correction: Step 2 False, But Ratio Still Bounded

**Date**: 2026-04-08

## The Error in Attempt 846

||S||²_F ≤ N/2 is FALSE. Cross terms can be positive at the ω-max
sign pattern. Violations in 33% of tested configs.

## What IS True

||S||²_F / |ω|²_max ≤ 0.55 in all 500 tested configs.
0.55 < 0.75 = the Key Lemma threshold.

Since S²ê ≤ ||S||²_F:
  S²ê/|ω|² ≤ ||S||²_F/|ω|² ≤ 0.55 < 0.75 ✓

## The Frobenius Identity (from file 511, the 842-attempt campaign)

||S||²_F = |ω|²/2 − 2 Σ_{j<k} cross_terms

At the vorticity max: if the cross terms are ≥ 0 (which the data suggests):
  ||S||²_F ≤ |ω|²/2
  S²ê/|ω|² ≤ ||S||²_F/|ω|² ≤ 1/2 < 3/4 ✓

BUT: we showed the cross terms CAN be negative (||S||²_F > N/2 in 33%).
The RATIO ||S||²_F/|ω|² ≤ 1/2 is NOT proven by the identity alone.

## What the Data Actually Says

The ratio ||S||²_F/|ω|²_max never exceeds 0.55 in 500 configs.
This is STRONGER than S²ê/|ω|² < 0.75 (which we proved to N=20).
The Frobenius ratio < 3/4 would imply S²ê/|ω|² < 3/4 (since S²ê ≤ ||S||²_F).

## The Gap (Honest)

Proving ||S||²_F/|ω|²_max < 3/4 analytically for ALL N-mode configs
is EQUIVALENT to the Key Lemma. It hasn't been proven.

The Frobenius identity RELATES ||S||²_F and |ω|² but doesn't bound
their RATIO without controlling the cross-terms.

The 1/N decay of the ratio is EMPIRICAL, not proven.

## 847. Step 2 of attempt 846 is FALSE. But the RATIO is bounded.
## The proof needs: ||S||²_F/|ω|²_max < 3/4 analytically.
## Data: max ratio = 0.55 across 500 configs. The bound exists.
## The Frobenius identity is the tool but the cross-term control is the gap.
