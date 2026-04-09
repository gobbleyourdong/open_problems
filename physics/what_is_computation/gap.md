# gap.md — what_is_computation

**Last updated:** 2026-04-09 (attempt_001 + Odd: pnp_asymmetry, grover, landscape_k)
**Phase:** 2 (compression asymmetry measured, landscape K-trajectory confirmed, Grover simulated)

## The gap, in one sentence

> **Computation is K-information manipulation in finitely-specifiable form. Church-Turing restated is "every physically realizable K-function has a finite K-specification." P vs NP restated is "compression-finding is harder than compression-verifying." Both are genuinely open, both are about the structural limits of compression as a process, and both are now load-coupled to the compression backbone from the philosophy track.**

## Why this is the gap

See attempt_001. The central reframing moves:

1. **Computation = K-manipulation.** A computation takes input states with some S-content and K-content to output states, implementing a function at the K level while consuming thermodynamic resources at the S level.

2. **Church-Turing as compression claim.** "Every effectively calculable function is Turing-computable" becomes "every function whose K-content is finitely specifiable has a finite K-specification as a Turing program." Physical Church-Turing adds the empirical claim that every physically realizable K-function has such a specification.

3. **P vs NP as the compression-asymmetry question.** P ≠ NP conjectures that finding compressions (solutions) is fundamentally harder than verifying compressions (witnesses). Under this reframing, the question is a claim about whether our cognitive situation as compressors is structurally inherent to computation or an artifact of our specific architecture.

4. **Pancomputationalism dissolved.** Physical laws are finite K-specifications (the equations). Physical dynamics are those laws being instantiated over time. Whether instantiating a K-specification counts as "running" it is a question about the word "running," not about physical fact. The strong reading (reality IS a computation) and the weak reading (reality can be modeled as one) differ only in taste.

## Three residual questions

- **R1.** Is physical Church-Turing actually true? Hypercomputation claims (Malament-Hogarth spacetimes, continuum-computing, some quantum gravity proposals) suggest there might be physically realizable processes with non-finite K-content. The literature is speculative but not closed.
- **R2.** Is P ≠ NP? If yes, compression-finding is categorically harder than compression-verifying. If no, insight reduces to checking. The answer has philosophical consequences for what cognition fundamentally does.

**Odd-instance evidence (three results):**
- **pnp_asymmetry:** find/verify ratio reaches 4698× at 3-SAT n=18. Growth is super-polynomial across all three NP problems tested. Formalized in `math/p_vs_np/lean/CompressionAsymmetry.lean` (6 proved theorems, 0 sorry).
- **landscape_k:** Hard SAT instances (clause ratio 4.3) have FLAT K-trajectory during search — the remaining clauses maintain constant gzip-K, providing no gradient. Easy instances (ratio 2.0) show K DECREASING — unit propagation creates compressible structure. **The K-trajectory distinguishes easy from hard: decreasing = easy, flat = hard.** This is the empirical fingerprint of K-opacity.
- **grover:** Quantum search halves the exponent (k=2) but structured classical search (DPLL, k≈14) beats it for problems with exploitable K-structure. The structure/no-structure divide > classical/quantum divide. Compression asymmetry persists in BQP.
- **R3.** What does BQP strictly containing P imply about the substrate-dependence of K-manipulation? Does quantum access a different K-function class, or just a faster path?

**Odd-instance answer (Grover simulation):** BQP gives a halved exponent for unstructured search (doubling period k=2 vs k=1 classical). But **structured classical search (DPLL, k≈14) already provides far larger effective advantage** than Grover for problems with exploitable K-structure. The structure/no-structure divide matters more than the classical/quantum divide. The compression asymmetry (finding >> verifying) persists in BQP: even with Grover, finding costs 2^(n/2) while verifying costs O(n). Physical Church-Turing preserved. R3 is now largely answered: substrate affects the doubling period constant, not the fundamental asymmetry.

## Sky bridges

- **physics/what_is_information** — S/K bifurcation; computation is K-manipulation.
- **physics/what_is_reality** — "is reality a computation" dissolves into "are physical laws finitely K-specifiable and instantiated by dynamics," which is almost tautologically yes.
- **philosophy/what_is_number** — Gödel incompleteness as a theorem about the computably enumerable but undecidable structure of arithmetic truth; compression framed it the same way.
- **philosophy/what_is_mind** — minds are computations; γ specifies what kind of computational structure (self-modeling with causal load) generates phenomenal self-reports.
- **philosophy/what_is_language** — LLMs are computations that compress social regularities via next-token prediction.
- **math/p_vs_np** — the compression reframing of P vs NP is available as a hypothesis the math track's formalization tools could test.

## Status

Phase 1. Second attempt in the physics track; the compression backbone extends from philosophy into physics cleanly through the S/K bifurcation (information) and the K-manipulation framing (computation). Multiple Mountains working as designed — same argument, different base, same residue.
