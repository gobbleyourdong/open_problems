# Attempt 002 — Barrier Formalization: What Exactly Is Blocked

**Date**: 2026-04-07
**Phase**: 1
**Instance**: Even (Theory)

## Making the Barriers Precise

### Relativization: Formally

A statement S about complexity classes RELATIVIZES if:
for every oracle A, S^A holds (with oracle access to A).

Baker-Gill-Solovay: ∃A: P^A = NP^A, ∃B: P^B ≠ NP^B.
Therefore: no relativizing proof can settle P vs NP.

**What this ACTUALLY means for proof techniques:**

A proof technique T "relativizes" if it proves statements of the form:
  "For all oracles A, [property about P^A, NP^A, ...]"

Since BGS gives contradictory oracle worlds, T can't prove P=NP or P≠NP.

**Example of non-relativizing result**: IP = PSPACE (Shamir 1992).
There exist oracles where IP^A ≠ PSPACE^A. So Shamir's proof uses
SPECIFIC PROPERTIES of polynomial computations (arithmetization) that
don't survive oracle modifications.

### Natural Proofs: Formally

A proof of "f ∉ C" is (C, s)-NATURAL if it exhibits a property Φ where:
1. **Constructive**: Φ is computable in poly(2^n) time from the truth table
2. **Large**: Pr_{f random}[Φ(f)] ≥ 1/poly(2^n)
3. **Useful**: Φ(f) = true → f ∉ C

Razborov-Rudich: If C ⊇ {PRG outputs} (i.e., C contains pseudorandom
functions), then no (C, s)-natural proof exists with s = superpolynomial.

Since P/poly contains PRG outputs (assuming OWFs): no natural proof of
"NP ⊄ P/poly" exists.

**The escape hatches**:
- Violate constructivity: define a property Φ that is ITSELF hard to compute
- Violate largeness: define Φ that is satisfied by negligibly few functions
- Target a class C that doesn't contain PRGs (e.g., ACC⁰ — Williams' approach)

### Algebrization: Formally

A technique algebrizes if it remains valid when the oracle A is replaced
by a low-degree extension Ã over a finite field.

Aaronson-Wigderson: ∃ algebraic oracle Ã: P^Ã = NP^Ã.
Therefore: no algebrizing technique can prove P ≠ NP.

## The Williams Escape

Williams (2011) proved NEXP ⊄ ACC⁰ via:

1. **Faster satisfiability algorithm**: given an ACC⁰ circuit of size s,
   decide satisfiability in time 2^n / n^ω(1) (slightly subexponential).

2. **The connection theorem**: if C-SAT is solvable in 2^n / n^ω(1),
   then NEXP ⊄ C.

**Why this avoids all three barriers**:
- Not relativizing: the SAT algorithm exploits the STRUCTURE of ACC⁰
  (Beigel-Tarui representation as low-degree polynomials)
- Not natural: the "hard function" is NEXP-complete (not efficiently decidable)
  → violates constructivity
- Not algebrizing: the argument goes through ALGORITHMS, not oracle manipulation

**The bottleneck**: need a faster SAT algorithm for TC⁰ or larger classes.
No such algorithm is known. The Beigel-Tarui representation doesn't extend
to threshold gates.

## What Would a P ≠ NP Proof Look Like?

Based on the barrier analysis, a proof must:
1. Analyze INTERNAL structure of computations (not oracle-based)
2. Use a NON-CONSTRUCTIVE or NON-LARGE hardness property
3. Not rely solely on arithmetization

Candidate structure:
```
Step 1: Prove a faster SAT algorithm for P/poly
        (currently: 2^n brute force. Need: 2^n / n^ω(1))
Step 2: Apply Williams' connection theorem: NEXP ⊄ P/poly
Step 3: Since NP ⊆ NEXP: if NP ⊆ P/poly then NEXP ⊆ P/poly → contradiction
Step 4: Therefore NP ⊄ P/poly → P ≠ NP
```

The bottleneck: Step 1. A faster SAT algorithm for GENERAL polynomial-size
circuits. This is an ALGORITHMIC problem, not a complexity-theoretic one.

## Result

The barriers are precisely formalized. The escape route is Williams'
paradigm: faster algorithms → circuit lower bounds. The bottleneck is
a SPECIFIC ALGORITHMIC PROBLEM (faster SAT for P/poly).

P ≠ NP reduces to an algorithm design challenge, not a proof technique
challenge. The barriers tell us WHERE to push. They don't tell us HOW.
