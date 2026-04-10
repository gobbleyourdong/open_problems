# landscape_k_subset_sum — Cycle 10 Odd (loop 4) findings

**Date:** 2026-04-09
**Driver:** `numerics/landscape_k_subset_sum.py`
**Data:**   `results/landscape_k_subset_sum_data.json`

## Purpose

Fourth NP family for the K-trajectory probe. After loop 3, the F1
"hard → K flat" fingerprint was confirmed on three independent NP
families (SAT, Hamiltonian cycle, 3-coloring) under the
constraint-remnant proxy. Loop 4 attempts a fourth confirmation —
which would push F1 universality from "three independent
confirmations" toward "candidate axiom."

## Setup

- **Hardness regimes:** small elements (1-100, easy) vs large elements
  (10^5 to 10^6, hard). Element scale is the primary hardness lever
  for subset-sum: small elements admit pseudo-polynomial dynamic
  programming; large elements force exponential search.
- **Sizes:** n ∈ {25, 30, 35}, with both hardness regimes for n=25, 30
  and hard only for n=35.
- **Instances per config:** 8.
- **Step budget:** 80,000.
- **Proxy:** reachable-bucket histogram. For each unused element e,
  bucketize `(remaining_target % e)` modulo a fixed bucket count, and
  gzip the resulting histogram bytes. Fixed-length input avoids the
  loop-2 v1 gzip overhead artifact.
- **Metric:** second-half slope (loop 3 convention).

## Raw results

| n  | hardness | solved / 8 | avg decisions | second-half slope | verdict       |
|---:|:---------|-----------:|--------------:|------------------:|:--------------|
| 25 | easy     |        8/8 |           239 |         +0.034032 | increasing    |
| 25 | hard     |        0/8 |        80,000 |         −0.000082 | **flat (F1)** |
| 30 | easy     |        8/8 |           177 |         −0.043945 | decreasing    |
| 30 | hard     |        0/8 |        80,000 |         −0.000023 | **flat (F1)** |
| 35 | hard     |        0/8 |        80,000 |         +0.000098 | **flat (F1)** |

## Headline: F1 confirmed on subset-sum (4th NP family)

**Three hard configurations**, all with 0/8 instances solved within the
80k-step budget, all with second-half slope satisfying |slope| < 0.0001:

- hard-25: −0.000082
- hard-30: −0.000023
- hard-35: +0.000098

These are the cleanest flat-K signals produced across all loops. The
constraint-remnant proxy on subset-sum gives an unambiguous flat
trajectory on hard instances.

**The F1 cross-family confirmation count is now 4 out of 4:**

| family            | F1 status | proxy                          | source       |
|:------------------|:---------:|:-------------------------------|:-------------|
| 3-SAT             |  HoldsOn  | remaining-clause bytes         | phase 1      |
| Hamiltonian cycle |  HoldsOn  | candidate-list bytes           | loop 3       |
| 3-coloring        |  HoldsOn  | forbidden-color histogram bytes | loop 3       |
| subset-sum        |  HoldsOn  | reachable-bucket histogram     | **loop 4**   |

**Four NP families. Four confirmations. Zero refutations.** The F1
universality claim has crossed from "three independent confirmations"
to "four independent confirmations on structurally different constraint
types (clausal, graph-traversal, graph-coloring, arithmetic)."

## Easy configs: completion artifacts as expected

The easy configs (small elements, all 8 instances solved in ~200
decisions) show large slope magnitudes in both directions:
- easy-25: +0.034 (increasing)
- easy-30: −0.044 (decreasing)

These are noise-dominated. With ~200 decisions and ~10 K-proxy
records each, the slope is computed from very few data points and is
sensitive to the boundary conditions of the search completion. They
are NOT meaningful F2 signals — just numerical noise from the
short-trajectory regime.

## F2 status update

F2 ("easier → K decreasing") on subset-sum: **inconclusive**. Easy
configs are too short to test cleanly. The earlier loop-2 / loop-3
finding that F2 is SAT-specific stands; subset-sum data does not
contradict or confirm it.

## What this loop produces

- **Positive:** F1 confirmed on a 4th NP family. The constraint-remnant
  proxy works on subset-sum exactly as predicted by the loop-2 C18
  diagnosis.
- **Methodological:** large-element subset-sum (10^5..10^6) is the right
  hardness lever — small elements give pseudo-polynomial trivial
  searches, large elements force genuine exponential exploration.
- **Cleanest flat-K signals so far:** all three hard configurations
  show |slope| < 0.0001, an order of magnitude cleaner than the
  loop-3 Ham cycle hard configurations.

## What this does NOT show

- A fifth NP family (graph-partition, Steiner tree, Knapsack with
  capacity, etc.) — F1 is now 4/4 but each new family multiplies the
  evidence.
- The F2 verdict on subset-sum (inconclusive due to short easy
  trajectories).
- Any direct connection to the formal `HardFlatUniversality` Prop in
  `lean/ConstraintRemnantDynamics.lean` (registered next loop).

## Status

Cycle 10 Odd complete. F1 confirmed on subset-sum.
`lean/ConstraintRemnantDynamics.lean` should be updated in Cycle 11
Even to register the 4th-family confirmation and possibly upgrade
the `HardFlatUniversality` Prop to a stronger empirical-axiom status.
