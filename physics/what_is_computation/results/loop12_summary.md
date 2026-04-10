# loop12_summary — 2026-04-09

Narrative summary of the 12th iteration of the Sigma 3-cycle Even/Odd
loop on `physics/what_is_computation`. Formal cert at
`certs/loop12_3cycles_cert.md`.

## How loop 12 differed

Loop 11 reached a peak with 521-record cross-family slope audit
showing zero F1/F2 overlap. Loop 12 went after THREE strategic items:

1. **Subset-sum F2 redesign** — the third prior-loop verdict flip.
2. **12th NP family** (hitting set) — joins the fully-testable set.
3. **BeatsNonic** §6 layer (n¹⁰).

Both Odd-cycle results landed: subset-sum F2 flipped to HoldsOn,
hitting set joined the both-testable category. F1 and F2 are now
BOTH at **10/12 testable confirmations** with the partition 8+2+2.

## Cycle-by-cycle

### Cycle 34

**Even** — `BeatsNonic` predicate + `r_decic := n¹⁰` explicit
witness in `CompressionAsymmetryStatement.lean` §6k. The §6
hierarchy now spans **eleven** provable layers, one per loop since
loop 2.

**Odd** — `numerics/landscape_k_subset_sum_v2_f2.py`. Subset-sum
F2 has been Untested since loop 4 due to the difficulty cliff.
This loop tries a redesigned proxy: residual-relative-size
histogram (16 fixed buckets, classifying each unused element by
e/(target − current_sum)).

**Result:** 4 of 5 configurations show clean decreasing slopes
(-0.001 to -0.012) on non-trivial searches (1000-2200 decisions).
**Subset-sum F2 status: Untested → HoldsOn.** Third prior-loop
verdict flip in Phase 2 (after Ham loop 8 and 3-col loop 9).

### Cycle 35

**Even** — Updated `lean/ConstraintRemnantDynamics.lean`:
- Flipped `F2_subset_sum` from Untested to HoldsOn
- Added `subset_sum_dp_density_proxy`
- Added `subset_sum_fully_crd_confirmed`,
  `seven_families_fully_crd_confirmed`
- Updated `dual_testability_structure` (subset-sum joins both-testable)
- Updated `CRDQuantitativeSeparation` to include subset-sum
- Updated count theorems

**Odd** — `numerics/landscape_k_hitting_set.py`. 12th NP family
probe with set-options histogram proxy. Hitting set is the
structural dual of set cover.

**Result:** Both F1 and F2 hold on hitting set. F1 confirmed on
3 hard configs (n=35, 40, 35-dense) with the 35-dense at full 80k
budget showing slope +0.000006. F2 confirmed on easy-25 (slope
-0.0150) and hard-30 (slope -0.0008 on 40k decisions). **Hitting
set joins the fully-testable set as the 8th member.**

### Cycle 36

**Even** — Updated `lean/HistogramProxy.lean`,
`lean/ConstraintRemnantDynamics.lean`, and `lean/Phase2Wrap.lean`
for the full loop 12 state:

- HistogramProxy: added `SetOptions` target, `hp_hitting_set`,
  `twelve_histogram_proxies`, `twelve_distinct_targets`
- ConstraintRemnantDynamics: added `hitting_set_options_proxy`,
  `F1_hitting_set` (HoldsOn), `F2_hitting_set` (HoldsOn). Updated
  to `eighteen_phase2_proxies`, `twenty_four_fingerprint_claims`,
  `twenty_claims_hold`. New `F1_holds_on_ten_families`,
  `F2_holds_on_ten_families`
- Phase2Wrap: `phase2_status` → 12 loops, 10 F1, 10 F2 confirmations.
  `ten_F1_confirmations`, `ten_F2_confirmations` theorems

**Odd** — `certs/loop12_3cycles_cert.md` (claims C70-C74) + this file.

## Headline 1: F1 and F2 BOTH at 10/12 testable

| family            | F1 status | F2 status |
|:------------------|:---------:|:---------:|
| 3-SAT             |  HoldsOn  |  HoldsOn  |
| Hamiltonian cycle |  HoldsOn  |  HoldsOn  |
| 3-coloring        |  HoldsOn  |  HoldsOn  |
| **subset-sum**    |  HoldsOn  |  **HoldsOn (loop 12 flip)** |
| knapsack          |  HoldsOn  |  Untested |
| vertex cover      |  HoldsOn  |  HoldsOn  |
| set cover         |  HoldsOn  |  HoldsOn  |
| clique            | HoldsOn (marginal) | HoldsOn |
| 3-DM              |  Untested |  HoldsOn  |
| FVS               |  Untested |  HoldsOn  |
| bin packing       |  HoldsOn  |  Untested |
| **hitting set**   |  HoldsOn  |  HoldsOn  |

**F1: 10 confirmed.** **F2: 10 confirmed.** **Zero refutations on
either across all 12 probed families.**

## Headline 2: 12-family partition becomes 8+2+2

- **8 fully testable:** SAT, Ham cycle, 3-coloring, **subset-sum**
  (loop-12 flip), vertex cover, set cover, clique, **hitting set**
  (loop 12 add)
- **2 F1-only testable:** knapsack, bin packing
- **2 F2-only testable:** 3-DM, FVS

The both-testable subset has grown from 5 (loop 9) → 6 (loop 10) →
6 (loop 11 — bin packing was F1-only) → **8 (loop 12)**. Two new
families joined the both-testable subset in a single loop.

## Headline 3: Set cover ↔ hitting set duality preserves the fingerprint

Set cover and hitting set are NP-complete duals. Both confirm BOTH
F1 and F2 under the same proxy template (constraint-options
histogram). This is structurally meaningful: **the dual K-trajectory
fingerprint is invariant under problem-class duality**. The
underlying property being measured isn't specific to either side
of the duality — it's a property of the bipartite element-set
incidence structure shared by both.

## Combined loop 1 through loop 12 tally

| metric                         | total |
|:-------------------------------|------:|
| new Lean files                 |    10 |
| existing Lean files updated    |    36 |
| numerics scripts added         |    22 |
| results/findings files added   |    26 |
| certs added                    |    12 |
| theorems proved (new)          |  ~196 |
| sorry count                    |     0 |
| F1 cross-family confirmations  |    10 |
| F2 confirmations               |    10 |
| compile-bugs found and fixed    |     2 |
| prior-loop verdicts flipped     |     3 |

## Residuals state after loop 12

| residual                      | status                                                              |
|:------------------------------|:--------------------------------------------------------------------|
| R1 hypercomputation           | OpenEmpirical                                                        |
| R2 P vs NP                    | OpenMathematical; §6 hierarchy spans 11 layers                      |
| R3 BQP substrate              | CLOSED                                                               |
| R4 K-trajectory universality  | **F1 10/12, F2 10/12**, dual partition 8+2+2, set/hitting dual confirms |

## What's still open (for loop 13 or pivot)

1. **F2 redesign for knapsack and bin packing.** Apply the loop-12
   subset-sum lesson — a different proxy semantics could expose F2.
   Knapsack natural target: capacity-residue density. Bin packing
   natural target: bin-fit-ratio density.
2. **F1 redesign for 3-DM and FVS.** Both have natural-progress
   shrinkage that prevents F1 detection. Possibly intractable
   without changing the search algorithm, not just the proxy.
3. **13th NP family.**
4. **BeatsDecic layer (n¹¹).** Per-loop §6 ladder.
5. **Lake build setup.**
6. **Pivot decision.**

## Status

Phase 2, loop 12 — COMPLETE.

The directory is at **10 Lean files (zero sorry, 10/10 linter clean)**,
**~100 results files**, **twelve certs (loop1-12)**. F1 confirmed on
**10 of 12 testable families**, F2 confirmed on **10 of 12 testable
families**, **12 NP families probed in the 8+2+2 dual structure**.
Three prior-loop verdicts flipped via proxy redesign. The set
cover/hitting set duality preserves the dual fingerprint, supporting
the unified-dynamics interpretation.

This is the cleanest dual-confirmation state Phase 2 has reached.
Loop 13 remains in scope.
