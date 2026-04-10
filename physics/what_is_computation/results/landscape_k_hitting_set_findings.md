# landscape_k_hitting_set — Cycle 35 Odd (loop 12) findings

**Date:** 2026-04-09
**Driver:** `numerics/landscape_k_hitting_set.py`
**Data:**   `results/landscape_k_hitting_set_data.json`

## Purpose

Twelfth NP family for the K-trajectory probe: hitting set decision.
This is the structural DUAL of set cover (selects elements to hit
all sets, vs set cover which selects sets to cover all elements).
After loop 12 Cycle 34 Odd (subset-sum F2 flip), both F1 and F2
were at 9/11. This loop adds a 12th family.

## Setup

- **Hardness lever:** `k = greedy_hitting_set - 1`.
- **Sizes:** n_universe ∈ {25, 30, 35, 40}, n_sets ≈ 2 × n_universe,
  set_size ≈ 4-5.
- **Step budget:** 80,000.
- **Instances per config:** 8.
- **Proxy:** set-options histogram (16 fixed buckets). For each unhit
  set, count how many of its elements are still in the candidate
  pool (not excluded).

## Raw results

| config              | solved/8 | budget | avg decisions | second-half slope | verdict           |
|:--------------------|---------:|-------:|--------------:|------------------:|:------------------|
| easy-25 (k > greedy)|      8/8 |    0/8 |           140 |         −0.015046 | **decreasing (F2)** |
| hard-30 (k=greedy-1)|      4/8 |    4/8 |        40,925 |         −0.000788 | **decreasing (F2)** |
| hard-35             |      3/8 |    5/8 |        58,325 |         −0.000098 | **flat (F1)** |
| hard-40             |      3/8 |    5/8 |        54,547 |         −0.000344 | **flat (F1)** |
| hard-35-dense       |      0/8 |    8/8 |        80,000 |         +0.000006 | **flat (F1)** |

## Headline 1: Hitting set is in the BOTH-TESTABLE category

**F1 evidence (3 hard configs):** hard-35, hard-40, hard-35-dense
all show |slope| < 0.0005, with hard-35-dense (the only
fully-budget-exhausted config) showing the cleanest +0.000006.

**F2 evidence (2 easier configs):** easy-25 (slope -0.0150) and
hard-30 (slope -0.0008, intermediate regime with 4/8 solved at
40k decisions). The hard-30 case is the strongest F2 signal —
non-trivially-long search showing decreasing slope.

**Hitting set joins the FULLY-TESTABLE set.** Both F1 and F2 hold
on hitting set under the set-options histogram proxy. This is the
**8th family in the both-testable category** after loop 12.

## Cross-family status update after loop 12 Cycle 35 Odd

| family            | F1 status | F2 status |
|:------------------|:---------:|:---------:|
| 3-SAT             |  HoldsOn  |  HoldsOn  |
| Hamiltonian cycle |  HoldsOn  |  HoldsOn  |
| 3-coloring        |  HoldsOn  |  HoldsOn  |
| **subset-sum**    |  HoldsOn  |  **HoldsOn (loop 12 Cycle 34 Odd flip)** |
| knapsack          |  HoldsOn  |  Untested |
| vertex cover      |  HoldsOn  |  HoldsOn  |
| set cover         |  HoldsOn  |  HoldsOn  |
| clique            |  HoldsOn (marginal) | HoldsOn |
| 3-DM              |  Untested |  HoldsOn  |
| FVS               |  Untested |  HoldsOn  |
| bin packing       |  HoldsOn  |  Untested |
| **hitting set**   |  HoldsOn  |  HoldsOn  |

**F1: 10 confirmed, 0 refuted, 2 untestable.**
**F2: 10 confirmed, 0 refuted, 2 untestable.**

The 12-family partition becomes:
- **8 fully testable:** SAT, Ham, 3-col, subset-sum (loop 12 flip),
  vertex cover, set cover, clique, hitting set
- **2 F1-only testable:** knapsack, bin packing
- **2 F2-only testable:** 3-DM, FVS

**8 + 2 + 2 = 12.**

## Headline 2: Set cover and hitting set both confirm both halves

Set cover and hitting set are mathematical DUALS, and BOTH show the
full F1+F2 dual fingerprint. This is structurally meaningful: the
constraint-remnant fingerprint is invariant under the set-cover ↔
hitting-set duality, suggesting the underlying dynamics is a
property of "minimum-cover problems on bipartite element-set
incidence" rather than of either side individually.

## What this loop produces

- **12th NP family probed.** Hitting set joins the fully-testable set.
- **F1 cross-family count: 10 (was 9).**
- **F2 cross-family count: 10 (was 9 after subset-sum flip).**
- **Dual structural symmetry confirmed:** set cover and hitting set,
  which are NP-complete duals, both confirm F1+F2 with the same
  proxy template (constraint-options histogram).

## What this does NOT show

- F2 on knapsack or bin packing under proxy redesign (next obvious
  targets — apply the loop-12 lessons from subset-sum).
- F1 on 3-DM or FVS under different search strategies.

## Status

Cycle 35 Odd complete. **F1 at 10/12, F2 at 10/12.** Both halves of
the dual fingerprint are at maximal confirmation across testable
families. `lean/HistogramProxy.lean`,
`lean/ConstraintRemnantDynamics.lean`, `lean/Phase2Wrap.lean` should
all be updated in Cycle 36 Even to register hitting set as the 12th
proxy/family.
