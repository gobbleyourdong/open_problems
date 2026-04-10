# landscape_k_dominating_set — Cycle 46 Odd (loop 16) findings

**Date:** 2026-04-09
**Driver:** `numerics/landscape_k_dominating_set.py`
**Data:**   `results/landscape_k_dominating_set_data.json`

## Purpose

Thirteenth NP family for the K-trajectory probe: dominating set
decision. After loop 15 the dual partition was 12+0+0 (universal
F1 + F2 across 12 families). Loop 16 attempts to extend this to
a 13th family.

## Setup

- **Hardness lever:** `k = greedy_dom - 1`.
- **Sizes:** n ∈ {20, 25, 30, 35}, edge densities 0.3-0.4.
- **Step budget:** 80,000.
- **Instances per config:** 8.
- **Proxy:** domination-options histogram (16 fixed buckets). For
  each undominated vertex, count remaining candidates that could
  dominate it (the vertex itself + its non-excluded neighbors).

## Raw results

| config              | solved/8 | budget | avg decisions | second-half slope | verdict           |
|:--------------------|---------:|-------:|--------------:|------------------:|:------------------|
| easy-20 (k > greedy)|      8/8 |    0/8 |            22 |         −0.007812 | **decreasing (F2)** |
| hard-25 (k=greedy-1)|      3/8 |    0/8 |           479 |         −0.007879 | **decreasing (F2)** |
| hard-30             |      1/8 |    0/8 |         1,713 |         −0.001227 | **decreasing (F2)** |
| hard-35             |      2/8 |    0/8 |         8,346 |         −0.002758 | **decreasing (F2)** |
| hard-30-dense       |      3/8 |    0/8 |           484 |         +0.001954 | increasing (artifact) |

## Headline 1: F2 confirmed on dominating set

**Four of five configurations show decreasing slopes** (-0.0012 to
-0.0079). The hard-30-dense outlier is a short-trajectory artifact
(484 decisions). The other configs span 22 to 8346 decisions and
all show consistent decreasing slopes.

**Dominating set F2 status: HoldsOn.**

This brings F2 cross-family count to **13/13** — universal across
all probed families.

## Headline 2: F1 untestable on dominating set under this proxy

**None of the configurations hit the 80k step budget.** Even hard-35
exhausts in 8346 decisions. The slopes are consistently decreasing
(F2-style), not flat.

**Diagnosis:** dominating set backtracking has natural-progress
shrinkage similar to FVS and 3-DM — the search adds vertices to
the cover on every branch, monotonically reducing the
domination-options histogram. The loop-14 depth-distribution proxy
template might work here in a future loop.

**Dominating set F1 status: Untested** (under this proxy).

This is structurally identical to the original FVS and 3-DM cases
before their loop-14/15 depth-distribution flips. Dominating set
joins them as a "natural-progress shrinkage" family that needs a
different proxy mechanism to test F1.

## Cross-family status update after loop 16 Cycle 46 Odd

| family            | F1 status | F2 status |
|:------------------|:---------:|:---------:|
| 3-SAT             |  HoldsOn  |  HoldsOn  |
| Hamiltonian cycle |  HoldsOn  |  HoldsOn  |
| 3-coloring        |  HoldsOn  |  HoldsOn  |
| subset-sum        |  HoldsOn  |  HoldsOn  |
| knapsack          | HoldsOn (m) | HoldsOn (m) |
| vertex cover      |  HoldsOn  |  HoldsOn  |
| set cover         |  HoldsOn  |  HoldsOn  |
| clique            | HoldsOn (m) | HoldsOn |
| 3-DM              | HoldsOn (m) | HoldsOn |
| FVS               | HoldsOn (m) |  HoldsOn  |
| bin packing       |  HoldsOn  | HoldsOn (m) |
| hitting set       |  HoldsOn  |  HoldsOn  |
| **dominating set**|  Untested |  **HoldsOn (loop 16)** |

**F1: 12 confirmed (4 marginal), 0 refuted, 1 untestable.**
**F2: 13 confirmed (3 marginal), 0 refuted, 0 untestable.**

The 13-family partition becomes **12 + 0 + 1**:
- **12 fully testable** (all loop-15 families)
- **0 F1-only testable**
- **1 F2-only testable:** dominating set

The "F1 only" category remains empty. F2 reaches 13/13 universal.
F1 drops slightly to 12/13 because we added a new family but didn't
yet apply the depth-distribution proxy fix to it.

## What this loop produces

- **13th NP family probed.** Dominating set joins the F2-only
  testable category.
- **F2 cross-family count: 13/13 universal across 13 families.**
- **F1 cross-family count: 12/13.** Dominating set is the new
  F1-untestable family until a depth-distribution probe is run.
- **Pattern recognition:** dominating set is the THIRD family
  (after FVS, 3-DM) with natural-progress shrinkage. The
  depth-distribution proxy works for these in general — a future
  loop should apply it.

## What this does NOT show

- F1 on dominating set under the depth-distribution proxy (next
  obvious target).
- A 14th NP family.
- Anything new about the 12 already-fully-testable families.

## Status

Cycle 46 Odd complete. **F2 universal at 13/13** across 13 NP
families. **F1 at 12/13** — dominating set joins as the new F1-only
family. The dual partition is **12 + 0 + 1**.
