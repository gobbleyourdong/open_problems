# P vs NP — Gap Assessment

## Phase: 0 → 1 (Paper Arsenal in progress)

## The Problem

Is P = NP? Can every problem whose solution is quickly VERIFIABLE
also be quickly SOLVABLE?

Consensus: P ≠ NP (almost universally believed, no proof).

## The Three Barriers

Every natural proof attempt is BLOCKED by at least one barrier:

### Barrier 1: Relativization (Baker-Gill-Solovay 1975)
There exist oracles A, B such that P^A = NP^A and P^B ≠ NP^B.
**Blocks**: any proof technique that "works relative to an oracle."
Most techniques from recursion theory and diagonalization relativize.

### Barrier 2: Natural Proofs (Razborov-Rudich 1997)
If one-way functions exist (a standard crypto assumption), then no
"natural" proof can show P ≠ NP.
A proof is "natural" if it exploits a CONSTRUCTIVE, LARGE property
of the Boolean function computed by the NP problem.
**Blocks**: most combinatorial circuit lower bound arguments.

### Barrier 3: Algebrization (Aaronson-Wigderson 2009)
There exist algebrizations (low-degree extensions) of oracles where
P^A = NP^A and others where P^A ≠ NP^A.
**Blocks**: techniques that use arithmetization (the IP = PSPACE method,
algebraic techniques in general).

### What Survives All Three?

Very few techniques. The known survivors:
- **GCT** (Geometric Complexity Theory): uses algebraic geometry,
  doesn't relativize, not natural, not algebrizing
- **Ryan Williams' connections**: algorithmic results → lower bounds,
  avoids barriers by being CONSTRUCTIVE in a non-natural way
- **Proof complexity**: propositional proof system lower bounds

## The Structural Difference from Other Millennium Problems

| Other problems | P vs NP |
|---------------|---------|
| Prove a specific object has a property | Prove a NEGATIVE (no fast algorithm) |
| Analysis, algebra, geometry | Theory of computation |
| Continuous mathematics | Discrete / combinatorial |
| Can verify computationally | Can't even formalize the question cleanly |
| One equation/statement | Involves ALL problems in NP simultaneously |

P vs NP is the ONLY Clay problem that asks for a NEGATIVE result
(no polynomial-time algorithm exists for SAT). Proving non-existence
is fundamentally harder than proving existence.

## Route Map (Initial)

### Route 1: Circuit Complexity ★★★★
Prove super-polynomial lower bounds on circuits computing SAT.
- Best known: NEXP ⊄ ACC⁰ (Williams 2011)
- Need: NP ⊄ P/poly (equivalent to P ≠ NP for circuits)
- The MAIN approach. But stuck below TC⁰.

### Route 2: GCT (Mulmuley-Sohoni) ★★★
Algebraic geometry attack on VP vs VNP (algebraic analog).
- Reduce to representation theory of symmetric groups
- Need: multiplicity obstructions (specific irreps in permanent vs determinant)
- Status: the "occurrence obstructions" don't suffice (BIP 2019)

### Route 3: Proof Complexity ★★★
Show no polynomial-size propositional proof of "SAT is in P" exists.
- Would prove P ≠ NP if we could show it for ALL proof systems
- Known: resolution, cutting planes, bounded-depth Frege have
  exponential lower bounds for specific tautologies
- Need: lower bounds for GENERAL proof systems (seems impossible)

### Route 4: Algorithms → Lower Bounds (Williams) ★★★
Ryan Williams showed: faster algorithms for certain problems IMPLY
circuit lower bounds. This flips the problem:
- Instead of proving circuits are weak, prove algorithms are strong
- NEXP ⊄ ACC⁰ follows from a faster algorithm for ACC⁰ satisfiability

### Route 5: Independence? ★
Could P vs NP be independent of ZFC?
- Possible in principle (no known obstruction)
- Would mean: no proof exists, the question is "meaningless" in ZFC
- Most researchers think this is unlikely but can't rule it out

## What the Sigma Method Can Do

Unlike the other Clay problems, P vs NP has:
- **No numerical certificates** (you can't "verify" P ≠ NP computationally)
- **No iron fortress** (there's no sequence of increasingly strong evidence)
- **No gradient correlation** (no single quantity to compute)

The Sigma Method is WEAKEST here because:
1. The problem is a NEGATIVE (non-existence of algorithms)
2. Three barriers PROVABLY block most natural approaches
3. No computational component (you can't brute-force non-existence)

**What CAN be done**: Map the barrier landscape precisely. Identify which
techniques survive all three barriers. Study GCT and Williams' connections
as the only approaches that aren't barrier-blocked.

## The Honest Assessment

P vs NP is likely the HARDEST of all Millennium Problems because:
1. It requires proving a negative (no algorithm exists)
2. Three barriers block most proof techniques
3. No computational or numerical evidence can help
4. The problem might be INDEPENDENT of ZFC

The Sigma Method can MAP the space but has the least traction here.
The problem may require fundamentally new mathematical foundations
(like Grothendieck's schemes for the Weil conjectures, or Perelman's
entropy for Poincaré).

## Status
- [ ] Paper arsenal built
- [ ] Barriers analyzed in detail
- [ ] Surviving approaches identified
- [ ] Lean definitions started
