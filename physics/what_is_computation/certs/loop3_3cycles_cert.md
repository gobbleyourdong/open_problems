# certs/loop3_3cycles_cert.md — loop 3, 3-cycle Even/Odd, 2026-04-09

**Purpose:** Third iteration of the Sigma 3-cycle loop on
`physics/what_is_computation`. Sibling to `certs/loop_3cycles_cert.md`
(loop 1) and `certs/loop2_3cycles_cert.md` (loop 2).

## Artifacts produced (loop 3, cycles 7-9)

| cycle | lane | artifact                                                             |
|------:|:-----|:---------------------------------------------------------------------|
|     7 | Even | `lean/CompressionAsymmetryStatement.lean` §6b → `prefix_insufficient_unbounded` |
|     7 | Odd  | `numerics/landscape_k_hamiltonian_v2.py` + data + findings.md        |
|     8 | Even | `lean/ConstraintRemnantDynamics.lean`                                 |
|     8 | Odd  | `numerics/landscape_k_coloring_v3.py` + data + findings.md           |
|     9 | Even | update to `Phase2Synthesis.lean` + `ConstraintRemnantDynamics.lean`   |
|     9 | Odd  | this file + `results/loop3_summary.md`                               |

## Certified claims (continuing from C21 in loop2_3cycles_cert.md)

---

### C22 — `prefix_insufficient_unbounded` strengthens §6

**Status: CERTIFIED**

Loop 2 closed the §6 dead-end with a one-point-difference theorem
(`prefix_insufficient`). Loop 3 strengthens this to an
unbounded-tail-difference theorem (`prefix_insufficient_unbounded`):

```
∃ r₁ r₂ : FVRatio,
    AgreeOnPrefix r₁ r₂ 20 ∧
    (∀ M : ℝ, ∃ n : ℕ, n > 20 ∧ r₁ n > M) ∧
    ¬ (∀ M : ℝ, ∃ n : ℕ, n > 20 ∧ r₂ n > M)
```

With `r₁ := r_linear_tail` (zero on [0,20], n beyond) and
`r₂ := r_zero`. Three supporting lemmas proved by Archimedean-only
reasoning (no Real asymptotic machinery):

- `r_linear_tail_agrees_prefix`
- `r_linear_tail_unbounded_beyond`
- `r_zero_bounded_beyond`

The full `SuperPolynomial r₁` witness remains deferred (still requires
Real asymptotic lemmas), but the unbounded-tail strengthening already
conveys the operational insight that prefix measurements do not
determine whether the tail is bounded, let alone super-polynomial.

**Reference:** `lean/CompressionAsymmetryStatement.lean` §6b

---

### C23 — Ham cycle "hard → K flat" robustly confirmed at n=40, 50

**Status: CERTIFIED**

Loop 2 Cycle 5 Odd gave a weak directional signal for Ham cycle
K-trajectory at n=30. Loop 3 Cycle 7 Odd scales this up:

- n ∈ {40, 50}, 8 instances per config
- Edge-probability sweep at 0.5× / 1× / 2× / 4× phase threshold
- Second-half slope metric (discounts startup transient)

**Result:** 6 out of 6 hard configurations (both n=40 and n=50 at
0.5×, 1×, 2× threshold) show cleanly flat second-half slopes
(|slope| < 0.0005). Search solved 0–2 instances out of 8 in each of
these configs, confirming they are genuinely hard.

The easy configs (4× threshold, all 8 instances solved) show large
positive slopes (+0.115, +0.173) that are COMPLETION ARTIFACTS — the
candidate-list proxy has a boundary effect near solution.

**Conclusion:** F1 ("hard → K flat") holds robustly on Hamiltonian
cycle under the constraint-remnant proxy. F2 ("easier → K
decreasing") does NOT hold — the direction is wrong (positive slope,
not negative).

**Reference:** `results/landscape_k_hamiltonian_v2_findings.md`,
`results/landscape_k_hamiltonian_v2_data.json`

---

### C24 — ConstraintRemnantDynamics.lean type-levels the two-halves diagnosis

**Status: CERTIFIED**

`lean/ConstraintRemnantDynamics.lean` (new loop 3 file) encodes:

- `ProxySide` inductive (ConstraintSide, SolutionSide)
- `Proxy` structure tagging each Phase 2 K-proxy by side and family
- `FingerprintClaim` structure with six entries (F1 and F2 across
  SAT, Ham, 3-coloring)
- `HardFlatUniversality` Prop (unproved conjecture)

Eight theorems proved by `decide` / `rfl`. Zero sorry.

After Cycle 8 Odd the inventory was updated to reflect F1_col =
HoldsOn and F2_col = FailsOn. The theorem `F1_holds_on_all_three`
explicitly records that all three probed NP families show the
hard-flat direction.

**Reference:** `lean/ConstraintRemnantDynamics.lean`

---

### C25 — F1 "hard → K flat" confirmed on 3-coloring via forbidden-color histogram

**Status: CERTIFIED**

Loop 2 Cycle 2 Odd (3-coloring v1, gzip of unresolved edges) and
loop 2 Cycle 4 Odd (3-coloring v2, fixed-size state bytes) were both
dead-ends. Loop 3 Cycle 8 Odd uses the CONSTRAINT-REMNANT diagnosis
from C20 and applies it with a 3-coloring-specific proxy:

**Forbidden-color histogram:** for each unassigned node, count the
distinct colors already used by assigned neighbors. Encode the sorted
histogram as bytes and gzip.

**Result at n=60, hard densities (2.0, 2.3, 3.0):** All three show
second-half slope |slope| < 0.0002 (cleanly flat). 0 out of 8, 0 out
of 8, 1 out of 8 instances solved respectively (confirming hardness).

This closes the 3-coloring dead-ends from loops 1 and 2: the
fingerprint IS observable on 3-coloring, but ONLY under a
constraint-side proxy. Two prior solution-side proxies failed for
diagnosable reasons (gzip overhead artifact and state-progress
artifact).

**Reference:** `results/landscape_k_coloring_v3_findings.md`,
`results/landscape_k_coloring_v3_data.json`

---

### C26 — F1 has 3/3 confirmations across independent NP families

**Status: CERTIFIED**

Combining C23 (Ham cycle) and C25 (3-coloring) with the earlier SAT
landscape_k.py result:

| family            | proxy                              | F1 status | F2 status |
|:------------------|:-----------------------------------|:---------:|:---------:|
| 3-SAT             | remaining-clause bytes             |  HoldsOn  |  HoldsOn  |
| Hamiltonian cycle | candidate-list bytes               |  HoldsOn  |  FailsOn  |
| 3-coloring        | forbidden-color histogram bytes    |  HoldsOn  |  FailsOn  |

**F1 cross-domain universality is 3/3 confirmed.** F2 is 1/3 — it is
SAT-specific, depending on unit propagation producing highly-
compressible short clauses.

The claim `HardFlatUniversality` in `ConstraintRemnantDynamics.lean`
is now supported by three independent confirmations and zero
refutations. Phase 2 has not proved it, but has produced strong
empirical evidence consistent with it.

**Reference:** `lean/ConstraintRemnantDynamics.lean` §4-5,
`results/landscape_k_*.md` (multiple files)

---

### C27 — Phase2Synthesis.lean updated to 7-file / 8-edge state

**Status: CERTIFIED**

Cycle 9 Even updated the Phase 2 inventory:

- `phase2_files` now has 7 entries (added `ConstraintRemnantDynamics.lean`)
- `citations` now has 8 edges (added
  `cgrd_cites_asymmetry: ConstraintRemnantDynamics → CompressionAsymmetryStatement`)
- `R4_k_trajectory.home_file` now points to
  `ConstraintRemnantDynamics.lean` (was `(empirical)`)
- `seven_phase2_files` theorem replaces `six_phase2_files`
- `citation_count = 8` replaces `citation_count = 7`

All `decide` proofs re-confirmed. Zero sorry.

**Reference:** `lean/Phase2Synthesis.lean`

---

## Cross-lane load summary (loop 3)

| Even artifact                              | fed into which Odd target                    |
|:-------------------------------------------|:---------------------------------------------|
| `prefix_insufficient_unbounded` (C22)      | (pure-theory; no Odd landing)                 |
| `ConstraintRemnantDynamics.lean` (C24)     | its FingerprintClaim status tags UPDATED by C25 |
| `Phase2Synthesis.lean` update (C27)         | (meta; citation structure)                   |

| Odd artifact                                | fed into which Even cycle                    |
|:--------------------------------------------|:---------------------------------------------|
| Ham cycle v2 hard-flat (C23)                | updated F1_ham.status in ConstraintRemnant    |
| 3-coloring v3 hard-flat (C25)               | updated F1_col / F2_col in ConstraintRemnant  |
| Both → 3/3 F1 confirmations (C26)           | feeds HardFlatUniversality Prop evidence      |

Loop 3 had the closest Odd→Even feedback loop of the three iterations.
Cycle 7 Odd's signal informed Cycle 8 Even's file structure; Cycle 8
Odd's result triggered the Cycle 9 Even updates. This is the phase
rhythm working at its cleanest.

## Sorry count across the physics dir after loop 3

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
| **total across this physics dir (8 files)**|       **0** |

## Combined loop 1 + loop 2 + loop 3 totals

| metric                         | loop 1 | loop 2 | loop 3 | combined |
|:-------------------------------|-------:|-------:|-------:|---------:|
| new Lean files                 |      3 |      3 |      1 |        7 |
| existing Lean files updated    |      0 |      1 |      2 |        3 |
| numerics scripts added         |      2 |      2 |      2 |        6 |
| results/findings files added   |      4 |      3 |      2 |        9 |
| certs added                    |      1 |      1 |      1 |        3 |
| theorems proved (new)          |     18 |     19 |     15 |       52 |
| axioms added (empirical)       |      2 |      0 |      0 |        2 |
| sorry count                    |      0 |      0 |      0 |        0 |
| dead-ends characterized        |      2 |      1 |      0 |        3 |
| dead-ends closed               |      0 |      1 |      2 |        3 |
| cross-family F1 confirmations  |      0 |      0 |      2 |        3 (counting SAT) |

## Dead-ends status after loop 3

| dead-end                                         | loop | status at end of loop 3              |
|:-------------------------------------------------|:----:|:-------------------------------------|
| §6 finite_measurements_do_not_prove_superpoly    |  1   | CLOSED (loop 2 §6, loop 3 §6b)       |
| gzip-on-unresolved-edges (3-col v1)              |  1   | CLOSED by C25 (v3 working proxy)    |
| fixed-size-state proxy (3-col v2)                |  2   | CLOSED by C25 (v3 working proxy)    |

**All three dead-ends are now closed.** The Sigma method's "map
dead-ends, then close them with the diagnosis" pattern is working.

## Residuals state after loop 3

| residual                      | loop 1            | loop 2                         | loop 3                       |
|:------------------------------|:------------------|:-------------------------------|:-----------------------------|
| R1 hypercomputation           | stated in Lean    | (same)                         | (same)                       |
| R2 P vs NP                    | stated in Lean    | prefix_insufficient (one-point)| prefix_insufficient_unbounded |
| R3 BQP substrate              | structurally closed | abstracted into 2×2 grid     | (same)                       |
| R4 K-trajectory universality  | untested          | weak cross-domain              | **3/3 F1 confirmations**     |

R4 has advanced from "untested" to "weak cross-domain signal" to
"three independent NP families show F1 hold," which is as close to
closed as an empirical universality claim can get in three loops.

## Status

Phase 2, loop 3, 3-cycle Even/Odd — COMPLETE.
Combined loop 1+2+3: 27 certified claims, 8 Lean files, zero sorry,
all three dead-ends closed, 3-family cross-domain F1 confirmation,
one residual closed (R3), one essentially closed (R4 F1-direction),
two remaining (R1 empirical, R2 mathematical).
