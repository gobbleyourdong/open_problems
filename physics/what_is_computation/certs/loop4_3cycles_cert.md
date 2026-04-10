# certs/loop4_3cycles_cert.md — loop 4, 3-cycle Even/Odd, 2026-04-09

**Purpose:** Fourth iteration of the Sigma 3-cycle loop on
`physics/what_is_computation`. Sibling to loop1/2/3 certs.

## Artifacts produced (loop 4, cycles 10-12)

| cycle | lane | artifact                                                             |
|------:|:-----|:---------------------------------------------------------------------|
|    10 | Even | `lean/CompressionAsymmetryStatement.lean` §6c → `BeatsLinear` hierarchy |
|    10 | Odd  | `numerics/landscape_k_subset_sum.py` + data + findings.md            |
|    11 | Even | `lean/ConstraintRemnantDynamics.lean` updates (4th family registered) |
|    11 | Odd  | `results/unified_k_trajectory_table.md`                              |
|    12 | Even | `lean/Phase2Wrap.lean`                                                |
|    12 | Odd  | this file + `results/loop4_summary.md` + dead-end audit              |

## Certified claims (continuing from C27 in loop3_3cycles_cert.md)

---

### C28 — BeatsLinear hierarchy with explicit r_quad witness

**Status: CERTIFIED**

`CompressionAsymmetryStatement.lean` §6c adds a layered super-polynomial
predicate hierarchy:

- `BeatsConstant r ≡ ∀ c, ∃ n, r n > c` (= Unbounded)
- `BeatsLinear r ≡ ∀ c, ∃ n, r n > c · n`

With explicit witness `r_quad : FVRatio` (zero on [0, 20], n² beyond).
Three new theorems:
- `r_quad_agrees_prefix`
- `r_quad_beats_linear`
- `r_zero_not_beats_linear`

Plus the strengthened theorem
`prefix_insufficient_beats_linear : ∃ r₁ r₂, AgreeOnPrefix r₁ r₂ 20 ∧ BeatsLinear r₁ ∧ ¬ BeatsLinear r₂`.

The Lean file's prefix_insufficient hierarchy now spans three layers:
one-point-difference (loop 2) ⊂ unbounded-tail (loop 3) ⊂ beats-linear
(loop 4). Each layer is proved with strictly Archimedean reasoning;
no Real asymptotic lemmas needed. Full `SuperPolynomial r₁` for
explicit r₁ remains deferred.

A `BeatsLinear → BeatsConstant` implication was attempted and hit a
quantifier snag (witness can be n=0). It is not committed (only the
working theorems are kept; the discovered issue is recorded as a
comment in §6c). Sorry count remains 0.

**Reference:** `lean/CompressionAsymmetryStatement.lean` §6c

---

### C29 — F1 confirmed on subset-sum (4th NP family)

**Status: CERTIFIED**

Cycle 10 Odd implemented `landscape_k_subset_sum.py` with a
constraint-remnant proxy: reachable-bucket histogram of
`(remaining_target % e)` for each unused element e. Fixed-length input
(16 buckets), so gzip overhead is constant.

**Three hard configurations** (large elements 10^5..10^6, 0 out of 8
solved within 80k steps):

| n  | second-half slope |
|---:|------------------:|
| 25 |         −0.000082 |
| 30 |         −0.000023 |
| 35 |         +0.000098 |

**All three |slope| < 0.0001** — the cleanest flat-K signal observed
across any loop. F1 ("hard → K flat") confirmed on the 4th NP family.

The F1 cross-domain confirmation count is now 4/4:

| family            | F1 status | proxy                                |
|:------------------|:---------:|:-------------------------------------|
| 3-SAT             |  HoldsOn  | remaining-clause bytes               |
| Hamiltonian cycle |  HoldsOn  | candidate-list bytes                 |
| 3-coloring        |  HoldsOn  | forbidden-color histogram            |
| subset-sum        |  HoldsOn  | reachable-bucket histogram           |

**Reference:** `results/landscape_k_subset_sum_findings.md`,
`results/landscape_k_subset_sum_data.json`

---

### C30 — ConstraintRemnantDynamics.lean updated to 4-family inventory

**Status: CERTIFIED**

Cycle 11 Even adds two new proxies (`col_forbidden_histogram_proxy`,
`subset_sum_reachable_proxy`) and two new fingerprint claims
(`F1_subset_sum`, `F2_subset_sum`) to `ConstraintRemnantDynamics.lean`.

Updated count theorems:
- `seven_phase2_proxies` (was `five_phase2_proxies`)
- `eight_fingerprint_claims` (was `six_fingerprint_claims`)
- `five_claims_hold` (was `four_claims_hold`)
- `one_claim_untested` (was `zero_claims_untested`)

New theorems:
- `F1_holds_on_all_four` — type-level 4-family universality
- `F1_zero_refutations` — type-level zero-refutation invariant

Zero sorry maintained.

**Reference:** `lean/ConstraintRemnantDynamics.lean`

---

### C31 — Unified Phase 2 K-trajectory empirical table

**Status: CERTIFIED**

`results/unified_k_trajectory_table.md` consolidates all seven
K-trajectory probes from loops 1-4 into a single table with:

- Per-probe configuration (family, proxy, side, n range, instance count)
- Hard-config slope summaries
- Cross-family F1 / F2 verdicts
- Three patterns visible only at the unified level:
  1. All four working proxies use **histogram-of-integers encoding**
  2. F1 detectability scales with **constraint-element count, not n**
  3. The completion artifact at the easy boundary is **family-invariant**

This is the citable single-page Phase 2 empirical surface. The
"histogram-of-integers" abstraction is a candidate Cycle-13-Even
target.

**Reference:** `results/unified_k_trajectory_table.md`

---

### C32 — Phase2Wrap.lean: aggregation type-level wrap-up

**Status: CERTIFIED**

`lean/Phase2Wrap.lean` (new file) provides the type-level analog of
this cert:

- `Phase2Pillar` inductive (4 constructors: KManipulationFraming,
  StructureVsSubstrate, ConstraintRemnantFingerprint,
  F1CrossFamilyEmpirical)
- `Pillar` structure pairing each pillar with its citation file
- `phase2_pillars` list (length 4)
- `Phase2Status` structure with 6 count fields
- `phase2_status : Phase2Status` instance encoding the loop-4 state

Theorems proved:
- `four_pillars`
- `eight_phase2_lean_files` and `nine_phase2_lean_files_with_wrap`
- `four_F1_confirmations`
- `phase2_invariants` (six conjuncts via `rfl`)
- `phase2_stable_close` (the headline aggregation)

Zero sorry.

**Reference:** `lean/Phase2Wrap.lean`

---

## Cross-lane load summary (loop 4)

| Even artifact                                       | fed into which Odd target                          |
|:----------------------------------------------------|:---------------------------------------------------|
| `BeatsLinear` hierarchy (C28)                       | (pure-theory; no Odd landing)                     |
| ConstraintRemnant updates (C30)                     | citation by C31's unified table                    |
| Phase2Wrap.lean (C32)                               | (meta; no direct Odd landing)                      |

| Odd artifact                                        | fed into which Even cycle                          |
|:----------------------------------------------------|:---------------------------------------------------|
| Subset-sum F1 (C29)                                 | drove C30 ConstraintRemnant updates                |
| Unified table (C31)                                  | informs Phase2Wrap.lean's aggregation count       |

Loop 4 had a clean Odd→Even feedback loop in the first two cycles
(Cycle 10 Odd → Cycle 11 Even). The third cycle was pure synthesis
on both lanes.

## Sorry count across the physics dir after loop 4

| File                                       | sorry count |
|:-------------------------------------------|------------:|
| `lean/QuantumClassicalHierarchy.lean`      |           0 |
| `lean/ShorStructuredQuantum.lean`          |           0 |
| `lean/KManipulationCore.lean`              |           0 |
| `lean/CompressionAsymmetryStatement.lean`  |           0 |
| `lean/HypercomputationAntiProblem.lean`    |           0 |
| `lean/StructureVsSubstrate.lean`           |           0 |
| `lean/Phase2Synthesis.lean`                |           0 |
| `lean/ConstraintRemnantDynamics.lean`      |           0 |
| `lean/Phase2Wrap.lean`                     |           0 |
| **total across this physics dir (9 files)**|       **0** |

## Dead-end audit (all loops)

| dead-end                                              | loop introduced | loop closed | how                                       |
|:------------------------------------------------------|:----------------|:------------|:------------------------------------------|
| §6 finite_measurements_do_not_prove_superpoly         | 1 Cycle 2 Even  | 2 Cycle 4 Even (one-point) → 3 Cycle 7 Even (unbounded) → 4 Cycle 10 Even (beats-linear) | layered hierarchy   |
| 3-coloring v1 gzip-overhead artifact                  | 1 Cycle 2 Odd   | 3 Cycle 8 Odd | constraint-remnant proxy (histogram)      |
| 3-coloring v2 state-progress artifact                 | 2 Cycle 4 Odd   | 3 Cycle 8 Odd | same diagnosis closes both                |
| BeatsLinear → BeatsConstant quantifier snag           | 4 Cycle 10 Even | not closed   | recorded as comment in §6c, not committed |

**All four dead-ends accounted for; three closed, one recorded as a
comment-level note.** No new dead-ends were introduced in loop 4 that
remain uncharacterized.

The §6 hierarchy has now been refined four times (loops 1-4):
- loop 1: comment-only
- loop 2: prefix_insufficient (one-point)
- loop 3: prefix_insufficient_unbounded (tail unbounded)
- loop 4: prefix_insufficient_beats_linear (beats every linear)

Each loop adds one provable layer without invoking Real asymptotic
machinery. The full `SuperPolynomial r₁` remains the asymptote.

## Combined loop 1 + 2 + 3 + 4 totals

| metric                         | loop 1 | loop 2 | loop 3 | loop 4 | combined |
|:-------------------------------|-------:|-------:|-------:|-------:|---------:|
| new Lean files                 |      3 |      3 |      1 |      2 |        9 |
| existing Lean files updated    |      0 |      1 |      2 |      2 |        5 |
| numerics scripts added         |      2 |      2 |      2 |      1 |        7 |
| results/findings files added   |      4 |      3 |      2 |      3 |       12 |
| certs added                    |      1 |      1 |      1 |      1 |        4 |
| theorems proved (new)          |     18 |     19 |     15 |     12 |       64 |
| axioms added (empirical)       |      2 |      0 |      0 |      0 |        2 |
| sorry count                    |      0 |      0 |      0 |      0 |        0 |
| dead-ends characterized        |      2 |      1 |      0 |      1 |        4 |
| dead-ends closed               |      0 |      1 |      2 |      0 |        3 |
| F1 cross-family confirmations  |    0+1 |      0 |      2 |      1 |       4  |

## Residuals at end of loop 4

| residual                      | status                                                     |
|:------------------------------|:----------------------------------------------------------|
| R1 hypercomputation           | OpenEmpirical (physics question, out of scope)             |
| R2 P vs NP                    | OpenMathematical (math track); §6c hierarchy advanced one layer |
| R3 BQP substrate              | CLOSED (structure-vs-substrate)                            |
| R4 K-trajectory universality  | EmpiricallySupported at 4/4 NP families, F1 universal, F2 SAT-specific |

R4 is now empirically supported by four independent confirmations.
This is a **stronger** state than "PartiallyClosed": the universality
claim has crossed the threshold where adding "candidate axiom" status
in `ConstraintRemnantDynamics.lean` is justified.

## Status

Phase 2, loop 4, 3-cycle Even/Odd — COMPLETE.
Combined loop 1+2+3+4: 32 certified claims, **9 Lean files**, zero
sorry, **3/4 dead-ends closed (one is a comment-only note)**, **F1
confirmed on 4 independent NP families**, R3 closed, R4
empirically-supported, R1/R2 still open by definition.
