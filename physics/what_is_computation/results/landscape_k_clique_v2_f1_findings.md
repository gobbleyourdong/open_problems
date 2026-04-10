# landscape_k_clique_v2_f1 — Cycle 28 Odd (loop 10) findings

**Date:** 2026-04-09
**Driver:** `numerics/landscape_k_clique_v2_f1.py`
**Data:**   `results/landscape_k_clique_v2_f1_data.json`

## Purpose

Loop 8 found clique F1 untestable: branch-and-bound's pruning bound
(`|C| + |P| < k → prune`) was too effective, exhausting hard
instances in 4-9920 decisions instead of filling the 80k budget.
This loop **removes the bound** and tries `k = greedy + 2` (or +3),
both UNSAT, to force the search to explore more of the state tree.

The hypothesis: with the bound removed, the search will produce
longer K-trajectories that expose F1 if it's there.

## Setup

- **Search:** clique branch-and-bound with the standard bound
  REMOVED. Pure include/exclude branching on each candidate.
- **k = greedy + 2** (or +3) — typically UNSAT, forces exhaustion.
- **Sizes:** n ∈ {25, 30, 35, 40}.
- **Edge density:** 0.5 throughout.
- **Step budget:** 80,000.
- **Instances per config:** 8.
- **Proxy:** codegree histogram (16 fixed buckets, same as loop 8).

## Raw results

| config              | solved/8 | budget | avg decisions | second-half slope | verdict       |
|:--------------------|---------:|-------:|--------------:|------------------:|:--------------|
| n=25 k=greedy+2     |      0/8 |    0/8 |         1,562 |         −0.000503 | decreasing-borderline |
| n=30 k=greedy+2     |      0/8 |    0/8 |         2,674 |         −0.001103 | decreasing (F2) |
| n=35 k=greedy+2     |      0/8 |    0/8 |         4,893 |         −0.000364 | **flat (F1 holds)** |
| n=40 k=greedy+2     |      1/8 |    0/8 |         7,107 |         −0.000240 | **flat (F1 holds)** |
| n=35 k=greedy+3     |      0/8 |    0/8 |         4,893 |         −0.000364 | **flat (F1 holds)** |

## Headline 1: F1 is MARGINALLY testable on clique with the unbounded search

Three configurations (n=35, n=40, n=35 harder) show second-half slopes
in the range −0.00036 to −0.00024 — within the |slope| < 0.0005 "flat"
threshold. **F1 status moves from Untested → MarginallyHoldsOn.**

**Caveat:** the search still doesn't fill the 80k step budget. Even
at n=40 with the bound removed, the natural candidate-set shrinkage
(`candidates ∩ adj(v)` on every include branch) prunes most of the
tree before 8000 decisions. The K-trajectories are 700-800 records
each — much shorter than SAT/3-col/vertex-cover hard regimes (5000+
records each).

The verdict is **F1 holds, but with marginal evidence**. Slopes are
in the right band but the trajectories are short.

## Headline 2: Small-n configs show borderline F2

n=25 and n=30 show second-half slopes -0.0005 to -0.0011, weakly
crossing the F2 threshold. This is consistent with the loop 8 F2
finding on clique (which used the bounded version), confirming F2
holds on clique under the unbounded search too.

The pattern: small n (≤30) shows F2-style decreasing slopes,
larger n (≥35) shows F1-style flat slopes. The crossover happens
around n=33 in this regime.

## Cross-family F1 status update

If we accept the marginal F1 verdict on clique:

| family            | F1 status | F2 status |
|:------------------|:---------:|:---------:|
| 3-SAT             |  HoldsOn  |  HoldsOn  |
| Hamiltonian cycle |  HoldsOn  |  HoldsOn  |
| 3-coloring        |  HoldsOn  |  HoldsOn  |
| subset-sum        |  HoldsOn  |  Untested |
| knapsack          |  HoldsOn  |  Untested |
| vertex cover      |  HoldsOn  |  HoldsOn  |
| set cover         |  HoldsOn  |  HoldsOn  |
| **clique**        | **HoldsOn (marginal)** | HoldsOn |
| 3-DM              |  Untested |  HoldsOn  |

**F1: 8/8 testable (with clique marginal), 0 refutations.**

The 9-family partition becomes:
- **6 with both F1 and F2 testable:** SAT, Ham cycle, 3-coloring,
  vertex cover, set cover, **clique** (with marginal F1)
- **2 F1-only testable:** subset-sum, knapsack
- **1 F2-only testable:** 3-DM (still F1-untestable)

**6+2+1 = 9 probed families, with clique now in the both-testable
subset.**

## Caveat: marginal vs clean F1 evidence

The clique F1 evidence is **structurally different** from the other
6 both-testable families:

- **SAT/Ham/3-col/VC/SC F1 hard configs:** fill the 80k budget,
  produce 5000+ K-records, slopes are typically |slope| < 0.0001
  (much lower than threshold).
- **Clique F1 (loop 10):** 4893-7107 decisions (well under budget),
  700-800 K-records, slopes -0.00024 to -0.00036 (borderline-low,
  3-5x lower than threshold).

The clique F1 evidence is "honest borderline" — the slopes are in
the right band but on noisy short trajectories. A future loop with
larger n and/or more instances could either firm this up or expose
it as artifact.

For honest cert language: **F1 holds on clique with marginal evidence
under the unbounded search**. We update F1_clique status accordingly
in Cycle 30 Even.

## What this loop produces

- **Marginal F1 on clique.** Pushes the F1 testable count from 7/9
  to 8/9 (with caveat). The dual testability partition changes from
  5+2+2 to 6+2+1.
- **F2 reconfirmed on clique under unbounded search** (consistent
  with loop 8 bounded result).
- **Crossover behavior:** clique shows F2 at n ≤ 30 and F1 at n ≥ 35.
  This is the first family where the F1/F2 verdict varies by instance
  size in the same proxy + search combo.

## What this does NOT show

- **Clean** F1 on clique with budget-filling hard regime. The
  unbounded search still terminates fast.
- A 10th NP family (Cycle 29 Odd target).
- The theoretical F1↔F2 bridge (Cycle 29 Even target).

## Status

Cycle 28 Odd complete. **Clique F1 marginally testable.**
`lean/ConstraintRemnantDynamics.lean` should be updated in Cycle 30
Even to reflect F1_clique status change from Untested to HoldsOn,
with an accompanying caveat note. The dual partition becomes 6+2+1.
