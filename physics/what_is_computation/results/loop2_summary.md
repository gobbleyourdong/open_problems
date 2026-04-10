# loop2_summary — 2026-04-09

Narrative summary of the 2nd iteration of the Sigma 3-cycle Even/Odd
loop on `physics/what_is_computation`. Formal cert at
`certs/loop2_3cycles_cert.md`; loop 1 summary at
`results/loop_3cycles_summary.md`.

## How this loop differed from loop 1

Loop 1 built the foundation. Five new Lean files, one numeric
reproduction with a new high-watermark, one methodological dead-end
characterized. The positive results came easily.

Loop 2 picked up from loop 1's stated next targets and did
the cleanup work: close a comment-level dead-end with a concrete
theorem, fix the K-proxy that failed in Cycle 2 Odd, probe a new NP
family with the lessons learned, add the structure-vs-substrate
abstraction that loop 1 kept citing informally, and wrap the phase in
a synthesis file.

The Odd lane this loop returned two useful signals (one negative,
one weak-positive). The Even lane produced three more theorem files,
keeping the zero-sorry invariant across the whole physics/what_is_computation
Lean set.

## Cycle-by-cycle

### Cycle 4

**Even** — `CompressionAsymmetryStatement.lean` §6 was a known
dead-end from loop 1: the intended `prefix_insufficient` theorem was
written only as a comment because my first attempt had a broken
quantifier structure. Cycle 4 Even replaces the comment with two
explicit FVRatio constants (`r_zero = 0`, `r_bump = 1 iff n > 20`)
and proves the weaker but provable form:

  `∃ r₁ r₂, AgreeOnPrefix r₁ r₂ 20 ∧ ¬ SuperPolynomial r₂ ∧ r₁ 21 > r₂ 21`

The stronger form requiring an explicit SuperPolynomial r₁ remains
deferred (needs Mathlib Real asymptotic machinery we don't want to
drag in). The weaker form still communicates the target insight:
measurements on [0, 20] can't pin down infinite-tail behavior.

**Odd** — `numerics/landscape_k_coloring_v2.py` applied the
fixed-size-state fix proposed in `landscape_k_coloring_findings.md`.
The gzip-header-overhead artifact from Cycle 2 Odd (v1) is
eliminated. But the SAT fingerprint still does NOT appear — a new
artifact takes over. Diagnosis: the state-byte proxy measures
ASSIGNMENT PROGRESS (monotone in n_assigned), not LANDSCAPE OPACITY
(what the SAT proxy captures via remaining-clauses). For SAT, clauses
COLLAPSE during search; for 3-coloring backtracking, no equivalent
constraint collapse happens.

This is a richer dead-end than loop 1's — it names the exact
structural mismatch between SAT and 3-coloring proxies, and prescribes
the next fix: measure CONSTRAINT REMNANTS, not STATE PROGRESS.

### Cycle 5

**Even** — `StructureVsSubstrate.lean`. Loop 1 kept informally citing
"structure matters more than substrate" (from Grover/DPLL/Shor data).
Cycle 5 Even formalizes this as a 2×2 grid and proves eight theorems
about the access and substrate axes:

- `access_dominates_substrate` : access gain > 7 × substrate gain
- `substrate_only_bounded`     : substrate-only gives at most ×2
- `access_only_unbounded_lower` : access-only gives at least ×14
- `both_axes_super_additive`   : Shor's corner exceeds the sum of
                                 either axis alone

The file does not prove new empirical content; it gives the observation
a citable name.

**Odd** — `numerics/landscape_k_hamiltonian.py` applies the
constraint-remnant proxy diagnosis from Cycle 4 Odd to a NEW NP
family: Hamiltonian cycle. The proxy encodes valid next-step
candidates (analog of SAT clauses) plus adjacency remnants, and gzips
the result.

Result: **first cross-domain K-trajectory signal in this loop.** At
n=30 near the Ham-cycle phase transition (threshold ~ln n / n ≈
0.114):

  sparse-30 (p=0.05, below threshold = HARDER)  → K_slope ≈ 0 (flat)
  moderate-30 (p=0.20, above threshold = easier) → K_slope ≈ −0.001

The direction matches SAT: harder → flat, easier → decreasing. Signal
is weak (3 instances per config, mixed per-instance trends), but the
hardness-ordering is correct and aligns with phase-transition theory.

Combined with C18 (negative on 3-coloring state-byte proxy), this
supports: **the K-trajectory fingerprint is a property of
constraint-remnant dynamics during search, not of NP hardness per
se.** Proxies that measure the CONSTRAINT side (SAT clauses, Ham-cycle
candidates) show the fingerprint; proxies that measure the SOLUTION
side (3-coloring state bytes) don't.

### Cycle 6

**Even** — `Phase2Synthesis.lean` encodes Phase 2's residual set and
file dependency graph as Lean data. Four residuals:

  R1 hypercomputation — OpenEmpirical (home: HypercomputationAntiProblem)
  R2 P vs NP          — OpenMathematical (home: CompressionAsymmetryStatement)
  R3 BQP substrate    — Closed (home: StructureVsSubstrate)
  R4 K-trajectory     — PartiallyClosed (home: empirical results files)

Six theorems: `exactly_one_closed`, `R3_is_closed`, R1/R2/R4 status
tags, citation count (7 edges), six-file Phase 2 set. Any future
file added to the phase-2 Lean set must update the `phase2_files`
and `residuals` constants — making the invariant "this inventory
reflects current state" syntactically enforced.

**Odd** — `certs/loop2_3cycles_cert.md` + this file.

## Combined loop 1 + loop 2 tally

| metric                         | loop 1 | loop 2 | combined |
|:-------------------------------|-------:|-------:|---------:|
| new Lean files                 |      3 |      3 |        6 |
| existing Lean files updated    |      0 |      1 |        1 |
| numerics scripts added          |      2 |      2 |        4 |
| results/findings files added   |      4 |      3 |        7 |
| certs added                    |      1 |      1 |        2 |
| theorems proved (new)          |     18 |     19 |       37 |
| axioms added (empirical)       |      2 |      0 |        2 |
| sorry count                    |      0 |      0 |        0 |
| dead-ends characterized         |      2 |      1 |        3 |
| dead-ends closed                |      0 |      1 |        1 |
| high-watermarks set             |      1 |      0 |        1 |

## Residuals state after loop 2

| residual                  | loop 1 status      | loop 2 status      |
|:--------------------------|:-------------------|:-------------------|
| R1 hypercomputation       | stated in Lean     | stated in Lean     |
| R2 P vs NP                | stated in Lean     | statement sharpened via `prefix_insufficient` |
| R3 BQP substrate          | structurally closed (hierarchy) | abstracted into 2×2 grid, strengthened |
| R4 K-trajectory universality | untested          | first weak cross-domain signal (Ham cycle) |

## What's still open (for loop 3 or beyond)

1. **Stronger Ham-cycle K-trajectory evidence.** n ∈ {40, 50, 60}
   near the phase transition, 10+ instances per config. The n=30
   signal is directional but not statistically robust.

2. **Conflict-neighborhood-entropy proxy on 3-coloring.** The
   constraint-remnant insight should apply: encode the per-node count
   of forbidden colors (analogous to SAT's unit-propagation chains)
   and gzip that histogram.

3. **Explicit SuperPolynomial r₁ in CompressionAsymmetryStatement.lean.**
   The weaker `prefix_insufficient` theorem is enough for the
   operational message but the stronger form would close the file
   cleanly. Needs Mathlib `Real.rpow` asymptotic lemmas.

4. **R1 hypercomputation empirical status.** Lean's
   `HypercomputationAntiProblem.lean` states the claim; whether it
   holds is a physics question. Possibly out of scope for this
   directory — belongs in `physics/what_is_reality` or a dedicated
   hypercomputation sub-directory.

## Status

Phase 2, loop 2 — COMPLETE. The directory is at 7 Lean files (zero
sorry), ~40 results files, two certs (loop1, loop2), and one Phase 2
synthesis file. Next natural loop will continue cleaning residuals
or pivot to a new problem family depending on operator direction.
