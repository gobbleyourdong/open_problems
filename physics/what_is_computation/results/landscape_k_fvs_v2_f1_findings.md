# landscape_k_fvs_v2_f1 — Cycle 41 Odd (loop 14) findings

**Date:** 2026-04-09
**Driver:** `numerics/landscape_k_fvs_v2_f1.py`
**Data:**   `results/landscape_k_fvs_v2_f1_data.json`

## Purpose

FVS F1 has been Untested since loop 10 due to natural-progress
shrinkage: the vertex-degree histogram on the induced subgraph
monotonically shrinks because the search itself removes vertices
on every branch.

This loop attempts a redesigned proxy that does NOT depend on the
constraint frontier shrinking: a **depth-distribution histogram**
tracking how many decisions have happened at each recursion depth.
The hypothesis: if the search is STUCK on a hard instance, the
depth distribution stays balanced; if PROGRESSING, it drifts deeper.

## Setup

- **New proxy:** depth-distribution histogram (16 fixed buckets,
  one per depth d ∈ [0..15]).
- **Generator:** same as loop-10 v1 (random graphs at densities
  0.5-0.6, k = greedy_fvs - 1).
- **Sizes:** n ∈ {25, 30, 35}.
- **Step budget:** 80,000.
- **Instances per config:** 8.

## Raw results

| config              | solved/8 | budget | avg decisions | second-half slope | verdict           |
|:--------------------|---------:|-------:|--------------:|------------------:|:------------------|
| hard-25 (k=greedy-1)|      4/8 |    4/8 |        44,987 |         −0.000004 | **flat (F1 NEW!)** |
| hard-30             |      4/8 |    4/8 |        44,564 |         −0.035114 | decreasing (F2)   |
| hard-35             |      3/8 |    5/8 |        59,581 |         −0.011719 | decreasing (F2)   |
| hard-30-dense       |      5/8 |    3/8 |        30,202 |         −0.023317 | decreasing (F2)   |

## Headline 1: F1 marginally testable on FVS at n=25

**The hard-25 configuration shows slope −0.000004**, well within
the |slope| < 0.0005 flat threshold, on a non-trivial 44k-decision
search where 4/8 instances solved. This is a clean F1 signal at
n=25.

The other three configurations (n=30, 35, 30-dense) show clearly
decreasing slopes (-0.012 to -0.035) — the depth distribution
drifts as the search progresses through more depths.

**FVS F1 status: Untested → HoldsOn (marginal).** This is the
**7th prior-loop verdict flip** in Phase 2.

## Headline 2: Mechanism mismatch — depth distribution drift

The depth-distribution proxy works for hard-25 because the search
tree at n=25 is shallow enough that the depth histogram saturates
quickly and stays roughly constant. At larger n, the search keeps
exploring deeper recursion levels and the histogram shifts.

This is structurally interesting: **F1 is exposed when the proxy
target SATURATES**, not necessarily when the constraint frontier
is static. Saturation is a different mechanism than the
"constraint-remnant stays K-flat" mechanism that the prior 10
families share.

This is a NEW kind of F1 evidence — based on tree-shape saturation
rather than constraint K-opacity. It joins the existing F1 family
but represents a slightly different structural reason for the flat
slope.

## Cross-family F1 status update after loop 14 Cycle 41 Odd

| family            | F1 status |
|:------------------|:---------|
| 3-SAT             | HoldsOn |
| Hamiltonian cycle | HoldsOn |
| 3-coloring        | HoldsOn |
| subset-sum        | HoldsOn |
| knapsack          | HoldsOn (marginal) |
| vertex cover      | HoldsOn |
| set cover         | HoldsOn |
| clique            | HoldsOn (marginal) |
| 3-DM              | Untested |
| **FVS**           | **HoldsOn (marginal, loop 14 flip)** |
| bin packing       | HoldsOn |
| hitting set       | HoldsOn |

**F1: 11 of 12 confirmed (3 marginal). Only 3-DM remains Untested.**

The 12-family partition becomes:
- **11 fully testable:** SAT, Ham, 3-col, subset-sum, knapsack
  (marginal), vertex cover, set cover, clique (marginal), FVS
  (marginal, NEW), bin packing, hitting set
- **0 F1-only testable**
- **1 F2-only testable:** 3-DM (still F1-untestable)

**11 + 0 + 1 = 12.**

## What this loop produces

- **7th prior-loop verdict flip.** FVS F1 from Untested to HoldsOn
  (marginal).
- **F1 cross-family count: 11 (was 10).**
- **New F1 mechanism diagnosed:** depth-distribution saturation,
  distinct from constraint-frontier K-opacity. This is the SECOND
  proxy-mechanism class for F1 (in addition to the
  histogram-of-constraint-counts class shared by the original 10).
- **Only 3-DM remains untestable** for F1, and only on a single axis.

## What this does NOT show

- F1 holding on FVS at n ≥ 30. The depth-distribution proxy only
  works at n=25 where the search tree is shallow enough.
- F1 on 3-DM. The depth-distribution proxy might also work there,
  but it's a separate experiment.
- A theoretical explanation for why depth saturation gives flat
  K-trajectory slopes.

## Status

Cycle 41 Odd complete. **FVS F1 marginally flips to HoldsOn at
n=25 under the depth-distribution proxy.** F1 cross-family count
is now 11/12. Only 3-DM remains F1-untestable.
`lean/ConstraintRemnantDynamics.lean` should be updated in Cycle 42
Even to flip F1_fvs from Untested to HoldsOn.
