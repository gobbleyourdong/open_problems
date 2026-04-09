---
source: Instance A VALIDATION — attacking Steps 7-10 (the bootstrap)
type: ADVERSARIAL REVIEW
date: 2026-03-29
---

## The Bootstrap Structure

Step 7: Q < 0 → isotropy ratio R < 1 → -Ω² dominates -H in eigenvector rotation.
Step 8: -Ω² dominates → DVar/Dt < 0 (variance decreasing).
Step 9: DQ/Dt = DVar/Dt - DH_ωω/Dt < 0 (since DVar < 0, DH_ωω > 0).
Step 10: Q < 0 at T₀, DQ/Dt < 0 when Q ≥ 0 → Q stays negative.

## Attack 1: Circularity check.

The bootstrap: Q < 0 → (stuff) → DQ/Dt < 0 → Q stays < 0.

Is this circular? NO if the INITIALIZATION (Q < 0 at T₀) is independent.

File 245 (Instance B): "The initialization Q(T₀) < 0 comes from the
transient dynamics: starting from any smooth IC, Q becomes negative
within O(1/||ω||∞) time."

CHECK: Is this proven or measured?

From our data (file 192): Q < 0 at 100% of post-transient times.
But we DON'T have a proof that Q becomes negative from an arbitrary IC.

At t = 0 for a general smooth IC: Q could be positive (file 190:
random NS ICs have Q > 0 at 43% of points).

The INITIALIZATION needs: Q(T₀) < 0 at the max for some T₀ < T*.

CLAIM: For smooth solutions, Q < 0 must hold at the max at SOME time.

JUSTIFICATION: The eigenvector tilting (Steps 6-8) drives Var → 0.
As Var → 0: Q = Var - H_ωω → -H_ωω < 0 (since H_ωω > 0 from Step 2).

But: the tilting RATE depends on Q < 0 (through the bootstrap).
If Q > 0 initially: the tilting might not work (the bootstrap hasn't
started yet).

HOWEVER: Step 2 gives H_ωω > 0 ALWAYS (from the Fourier lemma,
independent of Q). And Steps 6-8 show: even WITHOUT the bootstrap,
74% of the variance compression is ALGEBRAIC (from -Ω² alone, file 241).

The algebraic 74% gives: DVar/Dt < 0 at 64% of measurements
(file 241) WITHOUT needing Q < 0. Over time: Var decreases on average.

As Var ↓: Q = Var - H_ωω decreases (since H_ωω > 0). Eventually
Q < 0 at the max. This is the initialization.

VERDICT: The initialization is PLAUSIBLE but not rigorous. It relies
on the 74% algebraic compression being enough to drive Var below
H_ωω without the bootstrap. This is measured but not proven.

## Attack 2: Does the bootstrap self-close?

Step 7 uses: Q < 0 → R < 1 → ||H off-diagonal|| bounded.

The connection Q < 0 → R < 1: Q = Var - H_ωω < 0 means H_ωω > Var.
And H_ωω = Δp/3 + H_dev,ωω. So H_dev,ωω > Var - Δp/3.

This gives a LOWER bound on H_dev,ωω (more positive than Var - Δp/3).
It does NOT directly give R < 1 (which is |H_dev,ωω| < Δp/3).

WAIT: R = |H_dev,ωω|/(Δp/3). For Q < 0:
H_ωω = Δp/3 + H_dev,ωω > Var ≥ 0.
So: H_dev,ωω > -Δp/3 (lower bound).
And: H_dev,ωω < Δp/3 - Var + H_dev,ωω... this is circular.

Actually: Q < 0 means Var < H_ωω = Δp/3 + H_dev,ωω.
If H_dev,ωω is negative: H_ωω = Δp/3 - |H_dev,ωω| > Var ≥ 0.
So: |H_dev,ωω| < Δp/3 → R < 1. ✓

If H_dev,ωω is positive: H_ωω = Δp/3 + H_dev,ωω > Var.
R = H_dev,ωω/(Δp/3) > 0. R could be > 1 if H_dev,ωω > Δp/3.

PROBLEM: Q < 0 does NOT imply R < 1 when H_dev,ωω > 0.
Because Q < 0 means H_ωω > Var, but H_ωω could be large
because H_dev,ωω is large and positive (R > 1).

Example: Δp/3 = 10, H_dev,ωω = +20 → H_ωω = 30. R = 20/10 = 2 > 1.
And Var could be 25 → Q = 25 - 30 = -5 < 0. But R = 2 > 1!

So Q < 0 AND R > 1 is POSSIBLE. The bootstrap Step 7 assumes
Q < 0 → R < 1, which is FALSE.

## SEVERITY: HIGH

Step 7 has a logical error: Q < 0 does NOT imply R < 1.
The isotropy ratio R and the quantity Q are not directly linked
in the way the proof claims.

## RECOMMENDATION: Step 7 needs a different condition than R < 1.
## The proof needs to bound the -H off-diagonal WITHOUT using R < 1.
