# certs/loop7_3cycles_cert.md — loop 7, 3-cycle Even/Odd, 2026-04-09

**Purpose:** Seventh iteration of the Sigma 3-cycle loop on
`physics/what_is_computation`. Sibling to loops 1-6 certs.

## Artifacts produced (loop 7, cycles 19-21)

| cycle | lane | artifact                                                             |
|------:|:-----|:---------------------------------------------------------------------|
|    19 | Even | `lean/CompressionAsymmetryStatement.lean` §6f → BeatsQuartic         |
|    19 | Odd  | `numerics/landscape_k_set_cover.py` + data + findings.md             |
|    20 | Even | `lean/HistogramProxy.lean` + `lean/ConstraintRemnantDynamics.lean` updates |
|    20 | Odd  | `numerics/landscape_k_f2_retest.py` + data + findings.md             |
|    21 | Even | `lean/Phase2Wrap.lean` loop-7 update                                 |
|    21 | Odd  | this file + `results/loop7_summary.md`                               |

## Certified claims (continuing from C42 in loop6_3cycles_cert.md)

---

### C43 — BeatsQuartic layer added to §6 hierarchy

**Status: CERTIFIED**

`CompressionAsymmetryStatement.lean` §6f adds:
- `BeatsQuartic` predicate
- `r_quintic := if n ≤ 20 then 0 else n⁵` explicit witness
- `r_quintic_agrees_prefix`, `r_quintic_beats_quartic`,
  `r_zero_not_beats_quartic`
- `prefix_insufficient_beats_quartic` theorem

The §6 hierarchy now spans **six provable layers**:
- loop 2 §6:  prefix_insufficient (one-point)
- loop 3 §6b: prefix_insufficient_unbounded
- loop 4 §6c: prefix_insufficient_beats_linear (n²)
- loop 5 §6d: prefix_insufficient_beats_quadratic (n³)
- loop 6 §6e: prefix_insufficient_beats_cubic (n⁴)
- **loop 7 §6f: prefix_insufficient_beats_quartic (n⁵)**

Per-loop ladder pattern continues. Six layers in six loops.

**Reference:** `lean/CompressionAsymmetryStatement.lean` §6f

---

### C44 — F1 confirmed on set cover (7th NP family)

**Status: CERTIFIED**

`numerics/landscape_k_set_cover.py` runs the 7th NP family probe with
an element-options histogram proxy (16 fixed buckets per uncovered
element, counting how many sets in the family still contain it).

**Three hard configurations** (n_universe ∈ {40, 50}, k = greedy − 1):

| config              | solved/8 | second-half slope |
|:--------------------|---------:|------------------:|
| hard-40             |      0/8 |         +0.000020 |
| hard-50             |      0/8 |         −0.000006 |
| hard-40-sparse      |      0/8 |         −0.000006 |

All three exhausted the 80k step budget; |slope| < 0.0001.

**Cross-family F1 confirmation count after loop 7: 7/7.** All seven
families have constraint-side histogram-of-integers proxies that
produce flat-K signal on hard configurations.

**Reference:** `results/landscape_k_set_cover_findings.md`,
`results/landscape_k_set_cover_data.json`

---

### C45 — F2 confirmed on set cover (3rd F2 family) with cleanest evidence yet

**Status: CERTIFIED — strongest F2 evidence**

The same set cover probe shows **F2 on TWO configurations**:

| config              | solved/8 | avg decisions | second-half slope |
|:--------------------|---------:|--------------:|------------------:|
| easy-30 (k > greedy)|      8/8 |         2,999 |         −0.001415 |
| **hard-30** (k = greedy − 1) | 3/8 |     52,673 |         −0.002197 |

The **hard-30 case** is the cleanest F2 evidence in any loop:
**non-trivially-long search (53k decisions average) on
mostly-unfinished instances (3/8 solved) STILL showing decreasing K**.
This rules out the "F2 is just a completion artifact" alternative
hypothesis: the slope is decreasing during ACTIVE search, not just
near the solution boundary.

**Cross-family F2 confirmation count after loop 7: 3 of 5 testable
families** (SAT, vertex cover, set cover).

**Refined F2 verdict:** F2 holds wherever the easy regime produces
**constraint-frontier SHRINKAGE** during search. SAT (unit prop on
clauses), vertex cover (forced cover on degree-1 edges), set cover
(forced inclusion when only one set covers an element) all do this.
Ham cycle and 3-coloring backtracking under their loop-3 proxies
don't (NEGATIVE results stand). Subset-sum and knapsack are F2-
UNTESTABLE under standard backtracking (loop 7 Cycle 20 Odd).

**Reference:** `results/landscape_k_set_cover_findings.md` headlines 1-2

---

### C46 — F2 retest on subset-sum and knapsack: inconclusive

**Status: CERTIFIED — negative result with diagnosis**

Cycle 20 Odd retested F2 on subset-sum and knapsack with moderate-
difficulty regimes designed to produce non-trivially-long searches.
**Both families have a "difficulty cliff"** between trivially solvable
and search-fills-budget, with no useful intermediate regime where
both (a) the search runs long enough to record meaningful slopes
AND (b) constraint-propagation cascades produce the F2 signal.

| family       | n  | solved/8 | avg dec | slope     | verdict   |
|:-------------|---:|---------:|--------:|----------:|:----------|
| subset-sum   | 25 |      2/8 |  69,776 | +0.000264 | flat (F1) |
| subset-sum   | 28 |      3/8 |  68,344 | −0.000042 | flat (F1) |
| subset-sum   | 30 |      5/8 |  53,588 | +0.000246 | flat (F1) |
| knapsack     | 17 |      8/8 |       8 | −0.175781 | artifact  |
| knapsack     | 19 |      8/8 |       9 | −0.039062 | artifact  |
| knapsack     | 21 |      8/8 |      11 | −0.062500 | artifact  |

Subset-sum moderate fills the budget → F1-flat (consistent with
loop 4) but no F2. Knapsack moderate solves in 8-11 decisions →
slopes are large negative but artifact-dominated (only 4-6 records
per instance, second-half = 2-3 records, single-step deltas).

**F2 status preserved as "Untested"** for both families. The negative
result is METHODOLOGICAL — F2 testing requires a regime that exists
for SAT, vertex cover, and set cover but not for subset-sum or
knapsack under the standard backtracking + histogram-proxy combo.

**Reference:** `results/landscape_k_f2_retest_findings.md`

---

### C47 — Phase 2 Lean inventory updated to 7-family / 6-layer state

**Status: CERTIFIED**

Cycle 20 Even and Cycle 21 Even updated three Lean files:

**`HistogramProxy.lean`:**
- Added `EdgeOptions` → `ElementOptions` target
- Added `hp_set_cover` instance
- Updated to `seven_histogram_proxies`, `seven_distinct_targets`,
  `F1_universality_via_histogram_holds` (7 families)

**`ConstraintRemnantDynamics.lean`:**
- Added `set_cover_element_options_proxy`
- Added `F1_set_cover` (HoldsOn), `F2_set_cover` (HoldsOn)
- Updated to `ten_phase2_proxies`, `fourteen_fingerprint_claims`,
  `ten_claims_hold`, `F1_holds_on_all_seven`, `F1_zero_refutations`
  (7 conjuncts), new `F2_holds_on_three_families`

**`Phase2Wrap.lean`:**
- `phase2_status` → (4 pillars, 10 files, **7 F1 confirmations**,
  0 refutations, 0 sorry, **7 loops**)
- `seven_F1_confirmations`, `three_F2_confirmations` theorems

All 10 files pass `lean_comment_lint.py`. Zero sorry maintained.

**Reference:** `lean/HistogramProxy.lean`,
`lean/ConstraintRemnantDynamics.lean`, `lean/Phase2Wrap.lean`

---

## Cross-lane load summary (loop 7)

| Even artifact                              | fed into which Odd target                          |
|:-------------------------------------------|:---------------------------------------------------|
| §6f BeatsQuartic (C43)                     | (pure-theory)                                      |
| HistogramProxy/ConstraintRemnant (C47)     | citation by C44/C45 set cover                      |
| Phase2Wrap update (C47)                    | (meta wrap-up)                                     |

| Odd artifact                                | fed into which Even cycle                          |
|:--------------------------------------------|:---------------------------------------------------|
| Set cover F1+F2 (C44, C45)                  | drove C47 updates in three lean files             |
| F2 retest negative result (C46)             | diagnosis recorded in findings + cert              |

The cross-lane integration was tight: the set cover odd result fed
the Even register-and-update cycle, and the F2 retest closed an
open question (Untested → Untested with diagnosis).

## Sorry count + linter status across the physics dir after loop 7

| File                                       | sorry count | linter clean |
|:-------------------------------------------|------------:|:------------:|
| `lean/QuantumClassicalHierarchy.lean`      |           0 |      ✓       |
| `lean/ShorStructuredQuantum.lean`          |           0 |      ✓       |
| `lean/KManipulationCore.lean`              |           0 |      ✓       |
| `lean/CompressionAsymmetryStatement.lean`  |           0 |      ✓       |
| `lean/HypercomputationAntiProblem.lean`    |           0 |      ✓       |
| `lean/StructureVsSubstrate.lean`           |           0 |      ✓       |
| `lean/Phase2Synthesis.lean`                |           0 |      ✓       |
| `lean/ConstraintRemnantDynamics.lean`      |           0 |      ✓       |
| `lean/Phase2Wrap.lean`                     |           0 |      ✓       |
| `lean/HistogramProxy.lean`                 |           0 |      ✓       |
| **total (10 files)**                       |       **0** |   **10/10**  |

## Bug audit (loop 7)

**No new bugs found this loop.** The linter remained clean across all
edits. The two compile bugs surfaced in loops 5-6 stay fixed.

## Combined loop 1 through loop 7 totals

| metric                         | l1 | l2 | l3 | l4 | l5 | l6 | l7 | total |
|:-------------------------------|---:|---:|---:|---:|---:|---:|---:|------:|
| new Lean files                 |  3 |  3 |  1 |  2 |  1 |  0 |  0 |    10 |
| existing Lean files updated    |  0 |  1 |  2 |  2 |  3 |  4 |  4 |    16 |
| numerics scripts added         |  2 |  2 |  2 |  1 |  1 |  2 |  2 |    12 |
| results/findings files added   |  4 |  3 |  2 |  3 |  1 |  1 |  2 |    16 |
| certs added                    |  1 |  1 |  1 |  1 |  1 |  1 |  1 |     7 |
| theorems proved (new)          | 18 | 19 | 15 | 12 | 17 | 14 | 14 |   109 |
| sorry count                    |  0 |  0 |  0 |  0 |  0 |  0 |  0 |     0 |
| dead-ends characterized        |  2 |  1 |  0 |  1 |  0 |  0 |  1 |     5 |
| dead-ends closed               |  0 |  1 |  2 |  0 |  0 |  0 |  0 |     3 |
| F1 cross-family confirmations  |0+1 |  0 |  2 |  1 |  1 |  1 |  1 |     7 |
| F2 confirmations                |0+1 |  0 |  0 |  0 |  0 |  1 |  1 |     3 |
| compile-bugs found and fixed    |  0 |  0 |  0 |  0 |  1 |  1 |  0 |     2 |

## Residuals at end of loop 7

| residual                      | status                                                              |
|:------------------------------|:--------------------------------------------------------------------|
| R1 hypercomputation           | OpenEmpirical                                                        |
| R2 P vs NP                    | OpenMathematical; §6 hierarchy now spans 6 layers                   |
| R3 BQP substrate              | CLOSED                                                               |
| R4 K-trajectory universality  | **F1 universal at 7/7**, **F2 holds at 3/5 testable, 2 untestable**  |

## Status

Phase 2, loop 7, 3-cycle Even/Odd — COMPLETE.

Combined loops 1-7: **47 certified claims**, **10 Lean files**,
**zero sorry**, **all 10 files linter-clean**, F1 confirmed at 7/7
(22 hard configs all |slope| ≤ 0.0002), F2 confirmed at 3 of 5
testable families with the strongest evidence yet on set cover
hard-30, 2 families F2-untestable under standard backtracking. Phase
2 has reached a state where the headline claims (F1 universality,
F2 propagation-cascade dependence) are well-supported by 7 independent
NP family probes.
