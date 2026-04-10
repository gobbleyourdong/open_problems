# lake_build_audit — Phase 2 compilation test

**Date:** 2026-04-09
**Tool:** `lake build` with Lean 4.29.0 + Mathlib v4.29.0
**Directory:** `physics/what_is_computation/lean/`

## Setup

Added `lakefile.toml` and `lean-toolchain` to the lean/ directory.
Ran `lake update` to fetch Mathlib (8058 cached oleans decompressed).
Then built each of the 10 Lean files individually.

## Pre-build fixes

Two files (`QuantumClassicalHierarchy.lean`, `ShorStructuredQuantum.lean`)
were missing their Mathlib imports entirely — they used `ℝ` and
`norm_num` without `import Mathlib.Data.Real.Basic`. Fixed by adding
the imports.

One file (`KManipulationCore.lean`) had `deriving Repr` on structures
containing function types (`KContent → KContent`, `ℕ → ℕ`), which
Lean 4 can't synthesize `Repr` for. Fixed by removing `deriving Repr`
from those two structures.

## Build results

| File                              | Status  | Errors                                    |
|:----------------------------------|:--------|:------------------------------------------|
| KManipulationCore.lean            | **OK**  | 1 warning (unused variable)                |
| CompressionAsymmetryStatement.lean | **FAIL** | 5 errors (unsafe Repr, tactic failures)   |
| HypercomputationAntiProblem.lean  | **OK**  | clean                                      |
| QuantumClassicalHierarchy.lean    | **FAIL** | 2 errors (noncomputable defs)              |
| ShorStructuredQuantum.lean        | **OK**  | clean                                      |
| StructureVsSubstrate.lean        | **FAIL** | 2 errors (unsafe Repr)                     |
| ConstraintRemnantDynamics.lean    | **FAIL** | 5 errors (decide/omega failures, type mismatch) |
| Phase2Synthesis.lean              | **OK**  | clean                                      |
| Phase2Wrap.lean                   | **OK**  | clean                                      |
| HistogramProxy.lean               | **OK**  | clean                                      |

**5 compile, 5 fail.** The failures fall into three categories:

### Category 1: `deriving Repr` on structures with `ℝ` fields (2 files)

`CompressionAsymmetryStatement.lean` (Measurement has `ratio : ℝ`)
and `StructureVsSubstrate.lean` (Strategy has `doubling_period : ℝ`)
both derive `Repr` on structures containing `ℝ` fields. In Lean 4,
`Real.instRepr` is marked `unsafe`, so `deriving Repr` fails at the
kernel level.

**Fix:** remove `deriving Repr` from these structures (same fix as
KManipulationCore's function-type issue).

### Category 2: `noncomputable` definitions (1 file)

`QuantumClassicalHierarchy.lean` defines `advantage_ratio` and
`quantum_find_verify_ratio` as computable `def`s that divide reals.
Real division is `noncomputable` in Lean 4 / Mathlib.

**Fix:** mark these definitions as `noncomputable def`.

### Category 3: Tactic proof failures (2 files)

`CompressionAsymmetryStatement.lean` has tactic failures in the §6
prefix-insufficiency proofs (likely `exists_nat_gt` name changed or
tactic state changed). `ConstraintRemnantDynamics.lean` has
`decide`/`omega` failures on some of the larger count theorems
(likely the list operations exceed the timeout or the fingerprint
claim list is too large for `decide` to handle efficiently).

**Fix:** requires per-theorem debugging. The tactic proofs were
written without compilation testing and some assume Mathlib lemma
names or tactic behaviors that differ from the actual Lean 4.29
state.

## Assessment

The "zero sorry" claim made across 16 loops was accurate — no
`sorry` is used. But **"zero sorry" ≠ "compiles cleanly"**. Five
of ten files have real type errors that would need fixing.

The **Category 1 and 2 fixes are trivial** (remove `Repr`, add
`noncomputable`). The **Category 3 fixes require tactic debugging**
which is the actual work — some proof sketches may need rewriting.

The files that DO compile (KManipulationCore, HypercomputationAntiProblem,
ShorStructuredQuantum, Phase2Synthesis, Phase2Wrap, HistogramProxy)
represent the SOLID core. The files that fail are the ones with the
most accumulated edits across many loops.

## Verdict

The "source-only convention" obscured real compilation issues for
15 loops. The comment-syntax linter caught comment-balance bugs but
not type errors, noncomputable-def issues, or tactic failures.
Future Lean work on this directory should compile after every edit.
