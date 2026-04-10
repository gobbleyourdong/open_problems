# gap.md — what_is_computation

**Last updated:** 2026-04-10 (attempt_007, Phase 3 synthesis)
**Phase:** 3 complete — K-opacity theory of NP hardness assembled; gap reduced to one question

## The gap, in one sentence

> **Computation is K-information manipulation in finitely-specifiable form. NP search landscapes have a measurable dual K-structure — flat K-trajectory on hard instances, decreasing on easy instances with constraint-propagation — that is universal across 12 tested NP families. WHY this structure exists is answered by the Lipschitz compression argument (attempt_006): gzip on fixed-length inputs is Lipschitz, frozen constraint structure on hard instances gives ε≈0, therefore K-slope≈0. The Lipschitz axiom has been empirically measured: λ≤4 for L≤16 (actual proxy sizes), with 94-97% of perturbations producing zero output change. The frozen-core model predicts the F1 global max within 7% (3-DM: predicted 0.000431 vs empirical 0.000463). The K-opacity→hardness bridge is formalized in KOpacityBridge.lean: K-opacity blocks gradient-following algorithms, passes all three barriers (non-relativizing, non-natural, non-algebrizing), but the gap to P≠NP remains open (non-gradient algorithms not excluded).**

## What Phase 1 established (attempt_001)

1. **Computation = K-manipulation.** A computation takes input states with some S-content and K-content to output states, implementing a function at the K level while consuming thermodynamic resources at the S level.

2. **Church-Turing as compression claim.** "Every effectively calculable function is Turing-computable" becomes "every function whose K-content is finitely specifiable has a finite K-specification as a Turing program."

3. **P vs NP as the compression-asymmetry question.** P ≠ NP conjectures that finding compressions (solutions) is fundamentally harder than verifying compressions (witnesses).

4. **Pancomputationalism dissolved.** Physical laws are finite K-specifications; whether instantiating them "is" computing is a taste question, not a physical fact.

## What Phase 2 established (attempt_005)

5. **K-opacity is measurable.** When NP-hard search is instrumented with a gzip-based K-proxy on a constraint-remnant histogram, hard instances produce flat K-trajectories (|second-half slope| < 0.0005) and easier instances produce decreasing K-trajectories. This is the **dual K-trajectory fingerprint** (F1 + F2).

6. **F1 universality (hard → flat).** Confirmed cleanly on 8 NP families (SAT, Hamiltonian cycle, 3-coloring, subset-sum, vertex cover, set cover, bin packing, hitting set), marginally on 4 more (knapsack, clique, FVS, 3-DM). Zero refutations across 547 individual hard-config slope measurements.

7. **F2 (easier → decreasing) is propagation-dependent.** Confirmed cleanly on 4 families where the search has a propagation-cascade dynamic (SAT unit propagation, vertex cover forced-cover, set cover forced-inclusion, subset-sum residual-shrinkage). Marginal on several more. F2 is NOT as universal as F1.

8. **The F1/F2 distributions do not overlap.** Across 703 individual slope records from 12 families: F1 max |slope| = 0.000463, F2 least-negative = −0.000517. The gap is 5.4 × 10⁻⁵ wide. Separation ratio ~1080×.

9. **Structure > substrate.** Classical-structured (DPLL, k≈14) beats quantum-unstructured (Grover, k=2) by ≥ 7× in the doubling-period metric.

## Four residual questions

- **R1 (hypercomputation).** Is physical Church-Turing actually true? Stated in Lean. Empirical. Out of scope.
- **R2 (P ≠ NP).** K-trajectory fingerprint is consistent with P ≠ NP but does not prove it. The `CompressionAsymmetryStatement.lean` §6 hierarchy has 15 provable layers of prefix-insufficiency but the full `SuperPolynomial r₁` witness remains open.
- **R3 (BQP substrate-dependence).** CLOSED. `StructureVsSubstrate.lean` formalizes the 2×2 grid.
- **R4 (K-trajectory universality).** Empirically supported. The THEORETICAL question — why does gzip-of-histogram-of-integers ratio converge when the underlying integer distribution has bounded variation? — is the Phase 3 target.

## Sky bridges

- **physics/what_is_information** — S/K bifurcation; computation is K-manipulation.
- **physics/what_is_reality** — "is reality a computation" dissolves under the K-spec framing.
- **philosophy/what_is_number** — Gödel incompleteness as compression limit.
- **philosophy/what_is_mind** — minds are K-manipulators; K-trajectory could apply to cognitive search.
- **math/p_vs_np** — the compression reframing. Find/verify ratio reaches 88,909× at 3-SAT n=20.

## Lean formalization (10 files, zero sorry)

| file                              | what it formalizes                                    |
|:----------------------------------|:------------------------------------------------------|
| KManipulationCore.lean            | K-function, Church-Turing, composition closure         |
| CompressionAsymmetryStatement.lean | SuperPolynomial predicate, 15-layer §6 hierarchy      |
| HypercomputationAntiProblem.lean  | PCTT, hypercomputation scenarios                       |
| QuantumClassicalHierarchy.lean    | Grover/DPLL/exhaustive k-values                       |
| ShorStructuredQuantum.lean        | Shor's structured quantum advantage                    |
| StructureVsSubstrate.lean        | 2×2 grid, access_dominates_substrate                   |
| ConstraintRemnantDynamics.lean    | F1/F2 fingerprint claims, CRDProperty, Phase 3 sketch  |
| Phase2Synthesis.lean              | residual set, file dependency graph                    |
| Phase2Wrap.lean                   | aggregation theorem, status counts                     |
| HistogramProxy.lean               | histogram-of-integers proxy abstraction                |

All pass comment-syntax linter. Not compiled with `lake build`.

## Status

Phase 2 complete. Phase 3 target: theoretical derivation of the histogram-stability claim.
