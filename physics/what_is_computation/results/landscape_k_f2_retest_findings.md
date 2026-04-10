# landscape_k_f2_retest — Cycle 20 Odd (loop 7) findings

**Date:** 2026-04-09
**Driver:** `numerics/landscape_k_f2_retest.py`
**Data:**   `results/landscape_k_f2_retest_data.json`

## Purpose

Loops 4-5 left F2 ("easier → K decreasing") status as "Untested" for
subset-sum and knapsack because the easy regimes finished in too few
decisions for second-half-slope to be meaningful. Loop 7 retests with
**moderate** regimes designed to produce non-trivially-long searches.

## Setup

- **Subset-sum moderate:** n ∈ {25, 28, 30}, elements 10³..10⁵, target
  = sum of n/4 to n/2 elements (looser than the loop-4 hard regime
  but still requiring search). 8 instances per n.
- **Knapsack moderate:** n ∈ {17, 19, 21}, correlated weight≈value
  items, capacity = sum/2, target = 90% of brute-force optimum (loose
  enough for many subsets to satisfy). record_every=2 because
  moderate knapsack solves quickly.
- **Step budget:** 80,000.

## Raw results

| family       | n  | solved/8 | avg decisions | second-half slope | verdict   |
|:-------------|---:|---------:|--------------:|------------------:|:----------|
| subset-sum   | 25 |      2/8 |        69,776 |         +0.000264 | flat      |
| subset-sum   | 28 |      3/8 |        68,344 |         −0.000042 | flat      |
| subset-sum   | 30 |      5/8 |        53,588 |         +0.000246 | flat      |
| knapsack     | 17 |      8/8 |             8 |         −0.175781 | decreasing? (artifact) |
| knapsack     | 19 |      8/8 |             9 |         −0.039062 | decreasing? (artifact) |
| knapsack     | 21 |      8/8 |            11 |         −0.062500 | decreasing? (artifact) |

## Diagnosis: F2 retest is inconclusive on both families

**Subset-sum:** the "moderate" regime turned out to still be HARD —
2-5 instances out of 8 solved within 80k decisions. The search fills
the recording window, producing F1-flat slopes (|slope| < 0.0003)
rather than F2-decreasing. There is no useful intermediate regime
between "trivially solvable" (loop 4 easy, ~200 decisions) and "fills
the budget" (this loop's "moderate," 50k+ decisions).

**Knapsack:** the moderate regime IS easy — 8/8 solved in 8-11
decisions. The slopes are large negative (-0.18, -0.04, -0.06) but
they reflect the COMPLETION TRANSITION (search finishes, encoded
buffer becomes mostly zeros), not a sustained F2 signal. With only
4-6 records per instance and second-half = 2-3 records, the slopes
are noise-dominated single-step deltas.

**Both families have a "difficulty cliff"** between trivially
solvable and search-fills-budget, with no useful intermediate where
both (a) the search runs long enough to record meaningful slopes
AND (b) the search produces constraint-propagation cascades that
create the F2 decreasing signal.

This is consistent with the loop-7 set-cover finding (C19 Odd):
**F2 holds where the easy regime produces constraint-frontier
SHRINKAGE**. Subset-sum and knapsack backtracking don't naturally
produce this — they enumerate exhaustively without propagation.

## What this changes

**F2 status updates after loop 7 Cycle 20 Odd:**

| family       | loop 6 status | loop 7 status | reason |
|:-------------|:--------------|:--------------|:-------|
| subset-sum   | Untested      | Untested      | Hard regime fills budget; easy regime too short — no testable intermediate |
| knapsack     | Untested      | Untested      | Same difficulty cliff: 8 decisions easy → 80k decisions hard |

The loop 7 retest is a **negative result that refines the set of
testable F2 families**. Subset-sum and knapsack are not in that set
under the standard backtracking + constraint-remnant proxy combo.

## A more nuanced F2 verdict

After loop 7 across all 7 NP families:

| family            | F2 testable?               | F2 verdict |
|:------------------|:---------------------------|:-----------|
| 3-SAT             | yes (DPLL has UP)          |  HoldsOn   |
| Hamiltonian cycle | yes (under loop 3 proxy)   |  FailsOn   |
| 3-coloring        | yes (under loop 3 proxy)   |  FailsOn   |
| subset-sum        | **no testable regime**     |  Untested  |
| knapsack          | **no testable regime**     |  Untested  |
| vertex cover      | yes (sparse degree-1 cascade) | HoldsOn |
| set cover         | yes (clean hard-30 case)   |  HoldsOn   |

**3 of 5 testable families confirm F2** (SAT, vertex cover, set cover).
2 of 5 reject it under their loop-3 proxies (Ham cycle, 3-coloring),
which a redesigned proxy might still flip.

The "subset-sum and knapsack are F2-untestable" finding is a NEW
result of loop 7. It refines the F2 testability question and
explains why those two families are silent on the F2 axis.

## What this loop produces

- **Negative-with-diagnosis:** F2 cannot be cleanly tested on
  subset-sum or knapsack under the standard backtracking +
  constraint-remnant histogram proxy combo. Both families have a
  difficulty cliff with no useful intermediate.
- **Status preserved:** F2_subset_sum and F2_knapsack remain
  "Untested" (not "FailsOn") because the failure is methodological,
  not domain-specific.
- **Refined verdict:** F2 testability requires more than "the family
  is NP-complete." It requires (a) an easy regime with non-trivially-
  long searches AND (b) constraint-propagation cascades during search.

## What this does NOT show

- A POSITIVE F2 result on subset-sum or knapsack with a different
  proxy or generation strategy. These remain Untested, not refuted.
- An 8th NP family.
- Anything new about F1 (which is firmly 7/7 from loop 7 Cycle 19).

## Status

Cycle 20 Odd complete. The Untested→Untested status preservation is
itself a Sigma result: the "Maps include noise" principle applied at
the empirical level. We tried, learned why the test is inconclusive,
and recorded the structural reason. F2 verdict for these two families
will need a different test design in a future loop, or they may
remain Untested as part of Phase 2's permanent state.
