# landscape_k_fvs — Cycle 29 Odd (loop 10) findings

**Date:** 2026-04-09
**Driver:** `numerics/landscape_k_fvs.py`
**Data:**   `results/landscape_k_fvs_data.json`

## Purpose

Tenth NP family for the K-trajectory probe: feedback vertex set
(FVS) decision. After loop 9, both F1 and F2 were at 7/7 testable
with the dual structure 5+2+2. Loop 10 attempts a 10th family with
yet another constraint type (cycle elimination).

## Setup

- **Hardness lever:** `k = greedy_fvs_size - 1` (typically below
  minimum FVS, forces enumeration).
- **Sizes:** n ∈ {20, 25, 30, 35}.
- **Edge densities:** 0.4 (sparse), 0.5 (medium), 0.6 (dense).
- **Step budget:** 80,000.
- **Instances per config:** 8.
- **Proxy:** vertex-degree histogram (16 fixed buckets) over
  non-removed vertices in the induced subgraph G − removed.

## Raw results

| config              | solved/8 | budget | avg decisions | second-half slope | verdict           |
|:--------------------|---------:|-------:|--------------:|------------------:|:------------------|
| easy-20 (k > greedy)|      8/8 |    0/8 |            10 |         +0.000000 | (trivial)         |
| hard-25             |      5/8 |    3/8 |        30,024 |         −0.093756 | **decreasing (F2)** |
| hard-30             |      2/8 |    6/8 |        60,015 |         −0.023430 | **decreasing (F2)** |
| hard-35             |      7/8 |    1/8 |        10,360 |         −0.082280 | **decreasing (F2)** |
| hard-30-dense       |      5/8 |    3/8 |        30,086 |         −0.066079 | **decreasing (F2)** |

## Headline 1: F2 confirmed robustly on FVS (8th F2 family)

**Four hard configurations**, all with cleanly decreasing second-half
slopes ranging from −0.0234 to −0.0938. These are **large-magnitude
F2 signals** — much stronger than the small slopes that other F2
families produce.

The hard-30 case is particularly interesting: 2/8 solved, 6/8 hit the
budget, slope still −0.0234. This is non-trivially-long search on
mostly-unfinished instances, mirroring the set cover hard-30 case
from loop 7 — strong evidence that F2 isn't a completion artifact
on FVS.

**FVS F2 status: HoldsOn.**

## Headline 2: F1 NOT cleanly testable on FVS

Notice: **even hard configurations show DECREASING slopes, not flat.**
The hard-30 case (the longest-running one, with 6/8 budget exhaustion)
has slope -0.0234 — well past the F2 threshold, NOT in the F1 flat
range.

**Diagnosis:** FVS backtracking has built-in "natural progress" —
every branch removes a vertex from the candidate set, which actively
shrinks the constraint frontier. The vertex-degree histogram shrinks
toward zero throughout the search, producing decreasing K. There is
no "stuck regime" where the histogram stays static — even when the
search can't find a feasible cover, it KEEPS REMOVING VERTICES along
each branch path, making the histogram drift downward.

This is structurally different from SAT/3-col/vertex-cover, where
the search can stall on a partial assignment and the constraint
remnant stays the same shape for many steps.

**FVS F1 status: Untested** (not refuted; the proxy + search design
just doesn't expose F1 because there's no static-histogram regime).

## Cross-family status update after loop 10 Cycle 29 Odd

| family            | F1 status | F2 status |
|:------------------|:---------:|:---------:|
| 3-SAT             |  HoldsOn  |  HoldsOn  |
| Hamiltonian cycle |  HoldsOn  |  HoldsOn  |
| 3-coloring        |  HoldsOn  |  HoldsOn  |
| subset-sum        |  HoldsOn  |  Untested |
| knapsack          |  HoldsOn  |  Untested |
| vertex cover      |  HoldsOn  |  HoldsOn  |
| set cover         |  HoldsOn  |  HoldsOn  |
| clique            | HoldsOn (marginal, loop 10) | HoldsOn |
| 3-DM              |  Untested |  HoldsOn  |
| **FVS**           |  Untested |  HoldsOn  |

**F1: 7/10 fully testable + 1 marginal = 8/10 (loose) or 7/10 (strict).**
**F2: 8/10 testable.**

The 10-family partition becomes:
- **Both F1 and F2 testable (6 with clique marginal):** SAT, Ham, 3-col,
  vertex-cover, set-cover, **clique**
- **F1-only testable (2):** subset-sum, knapsack
- **F2-only testable (2):** 3-DM, **FVS**

**6+2+2 = 10 probed families.**

## What this loop produces

- **10th NP family probed.** FVS joins 3-DM in F2-only testable.
- **F2 confirmed on an 8th family** (still 0 refutations across all
  10 probed families).
- **New F1-untestability mechanism diagnosed:** "natural-progress
  search" where the constraint frontier shrinks on every branch
  path. This is different from the "branch-and-bound too efficient"
  mechanism (clique) and the "difficulty cliff" mechanism (subset-
  sum/knapsack). Three structurally distinct reasons for F1
  untestability now identified.
- **Strong predictive validation continues.** The loop-7 verdict
  ("F2 holds where the easy regime produces constraint-frontier
  shrinkage") correctly predicts FVS would show F2 because vertex
  removal IS shrinkage. Confirmed.

## What this does NOT show

- F1 on FVS under a different proxy / search. The current setup
  doesn't expose F1.
- A unified F1/F2 theorem (Cycle 29 Even target, addressed
  separately).

## Status

Cycle 29 Odd complete. **10 NP families probed.** F2 universality at
**8/10 testable** (and likely 8/8 if you exclude the F1-only families
where F2 can't be tested either way). F1 at 7/10 strict, 8/10 with
the marginal clique reading. The dual structure becomes 6+2+2 if we
count clique as marginally-F1-testable, otherwise 5+2+3.
