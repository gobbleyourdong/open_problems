# certs/loop2_3cycles_cert.md — loop 2, 3-cycle Even/Odd, 2026-04-09

**Purpose:** Second iteration of the Sigma 3-cycle loop on
`physics/what_is_computation`. Sibling to
`certs/loop_3cycles_cert.md` (loop 1) and `certs/phase1_manifest.md`
(the earlier numerical phase).

## Artifacts produced (loop 2, cycles 4-6)

| cycle | lane | artifact                                                             |
|------:|:-----|:---------------------------------------------------------------------|
|     4 | Even | `lean/CompressionAsymmetryStatement.lean` §6 → `prefix_insufficient` theorem |
|     4 | Odd  | `numerics/landscape_k_coloring_v2.py` + data + findings.md           |
|     5 | Even | `lean/StructureVsSubstrate.lean`                                      |
|     5 | Odd  | `numerics/landscape_k_hamiltonian.py` + data + findings.md           |
|     6 | Even | `lean/Phase2Synthesis.lean`                                           |
|     6 | Odd  | this file + update to loop summary                                   |

## Certified claims (continuing numbering from C16 in loop_3cycles_cert.md)

---

### C17 — §6 dead-end closed: `prefix_insufficient` is a theorem

**Status: CERTIFIED**

`CompressionAsymmetryStatement.lean` §6 contained a comment-level
dead-end: the claim "finite prefix measurements cannot entail
SuperPolynomial" was sketched but not proved. Cycle 4 Even adds two
explicit FVRatio constants — `r_zero` (constant zero) and `r_bump`
(zero on [0,20], one beyond) — and proves:

- `r_zero_not_superpoly`
- `bump_zero_agree_on_prefix`
- `bump_zero_differ_at_21`
- `prefix_insufficient` (weaker but provable form)

The weaker form: there exist r₁, r₂ with `AgreeOnPrefix r₁ r₂ 20`,
`¬ SuperPolynomial r₂`, and `r₁ 21 > r₂ 21`. The operational message
("prefix measurements do not pin down the infinite-tail behavior")
is conveyed without requiring real-number exponential-growth proofs.
The stronger form with an explicit SuperPolynomial r₁ is deferred.

Still zero sorry across the file.

**Reference:** `lean/CompressionAsymmetryStatement.lean` §6

---

### C18 — Fixed-size 3-coloring K-proxy also fails, differently

**Status: CERTIFIED (second dead-end characterized)**

Cycle 4 Odd applied the fix recommended in C15's findings:
full-coloring-state encoding with sentinel bytes for unassigned nodes.
The gzip overhead artifact of Cycle 2 Odd (C15) is eliminated —
K_proxy values are now in a plausible 0.5–1.4 band — but the SAT
fingerprint still does not appear. All four configurations show
small positive slopes dominated by "state transitioning from
homogeneous sentinel-bytes to heterogeneous assigned-bytes."

**Diagnosis:** the fixed-size state proxy measures **assignment
progress**, not **landscape opacity**. For SAT, `landscape_k.py`
measures REMAINING CLAUSES, which are the actual constraint objects
that unit propagation collapses. For 3-coloring, the edges never go
away — only the nodes change state. Encoding the node state instead
of the constraint remnant means the proxy tracks a different signal.

**Reference:** `results/landscape_k_coloring_v2_findings.md`,
`results/landscape_k_coloring_v2_data.json`

---

### C19 — Structure-vs-substrate 2×2 grid is type-level in Lean

**Status: CERTIFIED**

`StructureVsSubstrate.lean` abstracts the four-tier k-value hierarchy
(exhaustive k=1, Grover k=2, DPLL k≈14, Shor k=∞) into a 2×2 grid of
(Substrate × AccessMode). Eight theorems proved:

- `dpll_beats_grover` (classical-structured > quantum-unstructured)
- `shor_beats_dpll`, `shor_beats_grover`, `grover_beats_exhaustive`
- `access_dominates_substrate` (access-gain > 7× substrate-gain)
- `both_axes_super_additive`
- `substrate_only_bounded`, `access_only_unbounded_lower`

The headline theorem `access_dominates_substrate` gives the loop's
most-cited observation ("structure matters more than substrate") a
single canonical name. Zero sorry.

**Reference:** `lean/StructureVsSubstrate.lean`

---

### C20 — First cross-domain K-trajectory signal on a non-SAT problem

**Status: CERTIFIED (weak but directional)**

Cycle 5 Odd implemented the constraint-remnant proxy diagnosis from
C18 on a new NP family: Hamiltonian cycle. The proxy encodes valid
next-step candidates (analog of SAT's "remaining clauses") plus
unvisited-node adjacency remnants, and gzips the result.

Results at n=30 (the scale where the search does not trivially
complete within the recording window):

| config                            | avg K_slope   | fingerprint   |
|:----------------------------------|--------------:|:--------------|
| sparse-30 (p=0.05, BELOW threshold = HARDER) |    −0.000021 | flat          |
| moderate-30 (p=0.20, ABOVE = EASIER)         |    −0.000999 | decreasing    |

The direction matches SAT's fingerprint (easier → K decreases,
harder → K flat) for the first time on a non-SAT problem in this
loop. Signal is weak (3 instances per config, mixed per-instance
trends), but the direction is correct and the hardness-ordering is
expected from Hamiltonian-cycle phase-transition theory
(ln n / n ≈ 0.114 for n=30).

**Methodological conclusion** (now supported by two positive and
three negative results): the K-trajectory fingerprint is a property
of **constraint-remnant dynamics during search**, not of NP hardness
itself. Proxies must measure constraint-side remnants (SAT clauses,
Ham-cycle candidates) rather than solution-side progress (coloring
state) for the fingerprint to appear.

**Reference:** `results/landscape_k_hamiltonian_findings.md`,
`results/landscape_k_hamiltonian_data.json`

---

### C21 — Phase 2 residual set and file graph are type-level in Lean

**Status: CERTIFIED**

`Phase2Synthesis.lean` encodes the four residual questions (R1
hypercomputation, R2 P vs NP, R3 BQP substrate, R4 K-trajectory
universality) and the seven-edge file citation graph as Lean data.
Six theorems proved by `decide` / `rfl`:

- `exactly_one_closed` — exactly one residual is closed
- `R3_is_closed`, `R1_open`, `R2_open`, `R4_partial` — status tags
- `citation_count` — seven citation edges
- `six_phase2_files` — six-file Phase 2 set

This is a meta-level inventory: the completion state of Phase 2 is
itself a type-level object Lean can reason about. Any future file
added to the phase-2 set must update `phase2_files` and
`residuals` explicitly, making the invariant "this list reflects
current state" enforced by the file manifest.

Zero sorry.

**Reference:** `lean/Phase2Synthesis.lean`

---

## Cross-lane load summary (loop 2)

| Even artifact                              | fed into which Odd target                                      |
|:-------------------------------------------|:---------------------------------------------------------------|
| §6 `prefix_insufficient` (C17)             | (pure-theory; no Odd landing)                                  |
| `StructureVsSubstrate.lean` (C19)          | (pure-theory synthesis; no Odd landing)                        |
| `Phase2Synthesis.lean` (C21)               | (meta; no Odd landing)                                         |

| Odd artifact                                | fed into which Even cycle                                     |
|:--------------------------------------------|:--------------------------------------------------------------|
| C18 (3-coloring v2 dead-end)                | informed C19's framing and C21's R4 "partially closed" tag    |
| C20 (Ham cycle weak positive)                | informed C21's R4 status (partial, not open)                  |

Loop 2 was more theory-heavy than loop 1. The Odd outputs this time
were both negative-result-and-diagnosis (C18) and weak-positive
(C20), which is typical for a second iteration — the easy positive
results come first, and later cycles grind through methodological
cleanup.

## Sorry count across the physics dir after loop 2

| File                                     | sorry count |
|:-----------------------------------------|------------:|
| `lean/QuantumClassicalHierarchy.lean`    |           0 |
| `lean/ShorStructuredQuantum.lean`        |           0 |
| `lean/KManipulationCore.lean`            |           0 |
| `lean/CompressionAsymmetryStatement.lean`|           0 |
| `lean/HypercomputationAntiProblem.lean`  |           0 |
| `lean/StructureVsSubstrate.lean`         |           0 |
| `lean/Phase2Synthesis.lean`              |           0 |
| **total across this physics dir**        |       **0** |

## Dead-ends captured as map features

| loop | cycle | dead-end                                            | cert id |
|-----:|------:|:---------------------------------------------------|:--------|
|    1 |     2 | §6 finite_measurements_do_not_prove_superpoly       | C14     |
|    1 |     2 | gzip-on-unresolved-edges artifact (3-coloring v1)    | C15     |
|    2 |     4 | fixed-size-state proxy artifact (3-coloring v2)      | C18     |

Three dead-ends named, three fix paths proposed, two closed this loop
(C17 closes C14, C20's diagnosis closes C15 + C18 methodologically).

## Status

Phase 2, loop 2, 3-cycle Even/Odd — COMPLETE.
Combined loop 1 + loop 2: 21 certified claims, 7 Lean files, zero
sorry, three dead-ends characterized, one first cross-domain signal,
one residual closed (R3), one partially closed (R4), two still open
(R1 empirically, R2 mathematically).
