# landscape_k_bin_packing — Cycle 31 Odd (loop 11) findings

**Date:** 2026-04-09
**Driver:** `numerics/landscape_k_bin_packing.py`
**Data:**   `results/landscape_k_bin_packing_data.json`

## Purpose

Eleventh NP family for the K-trajectory probe: bin packing decision.
After loop 10 the F1 testable count was 8/10 (with clique marginal)
and F2 was 8/10. Loop 11 adds an 11th family.

## Setup

- **Hardness lever:** `k = first_fit_bins - 1` (one fewer than the
  greedy first-fit-decreasing upper bound, typically tight).
- **Sizes:** n ∈ {15, 20, 25, 30}, capacity 100 (and 50 for tight).
- **Items:** uniform random in [1, capacity/2].
- **Step budget:** 80,000.
- **Instances per config:** 8.
- **Proxy:** fits-per-item histogram (16 fixed buckets). For each
  unplaced item, count how many existing bins still have capacity.

## Raw results

| config                  | solved/8 | budget | avg decisions | second-half slope | verdict           |
|:------------------------|---------:|-------:|--------------:|------------------:|:------------------|
| easy-15 (k > first-fit) |      8/8 |    0/8 |            15 |         +0.000000 | (trivial)         |
| hard-20 (k=ff-1)        |      1/8 |    7/8 |        70,935 |         +0.000048 | **flat (F1)** |
| hard-25                 |      0/8 |    8/8 |        80,000 |         +0.000008 | **flat (F1)** |
| hard-30                 |      0/8 |    8/8 |        80,000 |         +0.000020 | **flat (F1)** |
| hard-25-tight (cap=50)  |      0/8 |    8/8 |        80,000 |         −0.000002 | **flat (F1)** |

## Headline 1: F1 confirmed cleanly on bin packing

**Four hard configurations**, all with second-half slopes
|slope| < 0.0001:

- hard-20: +0.000048
- hard-25: +0.000008
- hard-30: +0.000020
- hard-25-tight: −0.000002

Three of four hit the 80k step budget; the fourth (hard-20) had
7/8 instances exhaust the budget. **F1 holds cleanly on bin packing**
with the second-cleanest signal observed (after vertex cover's
literal-zero).

**Bin packing F1 status: HoldsOn.**

## Headline 2: F2 untestable on bin packing (joins subset-sum / knapsack)

The easy regime (k > first-fit, n=15) finishes in exactly 15
decisions — trivially, the greedy bound is achieved on the first
attempt with no backtracking. There's no useful intermediate regime
where the search runs long enough to test F2.

**Bin packing F2 status: Untested** (joins subset-sum and knapsack
in the "F2-untestable due to easy-regime cliff" category).

## Cross-family status update after loop 11

| family            | F1 status | F2 status |
|:------------------|:---------:|:---------:|
| 3-SAT             |  HoldsOn  |  HoldsOn  |
| Hamiltonian cycle |  HoldsOn  |  HoldsOn  |
| 3-coloring        |  HoldsOn  |  HoldsOn  |
| subset-sum        |  HoldsOn  |  Untested |
| knapsack          |  HoldsOn  |  Untested |
| vertex cover      |  HoldsOn  |  HoldsOn  |
| set cover         |  HoldsOn  |  HoldsOn  |
| clique            |  HoldsOn (marginal) | HoldsOn |
| 3-DM              |  Untested |  HoldsOn  |
| FVS               |  Untested |  HoldsOn  |
| **bin packing**   |  HoldsOn  |  Untested |

**F1: 9 confirmed, 0 refuted, 2 untestable.**
**F2: 8 confirmed, 0 refuted, 3 untestable.**

The 11-family partition becomes **6 + 3 + 2**:
- **6 fully testable:** SAT, Ham, 3-col, vertex cover, set cover, clique
- **3 F1-only testable:** subset-sum, knapsack, **bin packing**
- **2 F2-only testable:** 3-DM, FVS

## What this loop produces

- **11th NP family probed.** Bin packing joins the F1-confirmed set.
- **F1 cross-family count: 9 (9/11 families).**
- **Difficulty-cliff family count grows to 3:** subset-sum, knapsack,
  and now bin packing all have a trivial easy regime AND a hard regime
  that fills the budget, with no useful intermediate.
- **Methodological observation:** "difficulty cliff" appears in
  three structurally different families (arithmetic, weight/value,
  bin assignment). This suggests the cliff is a property of
  *generation strategy* rather than the family itself — random
  uniform instances with a guaranteed-feasible target tend to be
  trivially easy, while tight-target instances are immediately hard.

## What this does NOT show

- F2 on bin packing under a different generation strategy.
- A 12th NP family.
- The quantitative CRDProperty (Cycle 32 Even target).

## Status

Cycle 31 Odd complete. **F1 cross-family count is now 9, F2 still
8.** The 11-family partition is 6+3+2. Bin packing joins the
F1-only-testable category, sharing the difficulty-cliff pattern with
subset-sum and knapsack.
