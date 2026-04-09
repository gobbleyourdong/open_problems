# Attempt 001 — Route Survey and Problem Decomposition

**Date**: 2026-04-07
**Phase**: 0 → 1 (Paper Arsenal)
**Instance**: Even (Theory)

## Approach
Map the entire proof landscape before attempting anything. Identify every known route,
every known obstruction, and the minimal set of things that need to be true.

## The Proof Landscape

### Route 1: Constructive QFT (Balaban program)
**Idea**: Lattice → renormalization group → continuum limit → OS axioms → mass gap.

**Status**: Most advanced route. Balaban (1982-1989) proved UV stability for pure YM
on a finite lattice in 4D. The program was never completed (infinite volume limit,
OS axioms, mass gap all remain).

**Key papers**: Balaban series (Comm. Math. Phys., ~13 papers), Magnen-Rivasseau-Sénéor.

**Obstruction**: The RG analysis is extraordinarily complex. Each RG step requires
controlling gauge-invariant effective actions on block-spin variables. The combinatorics
explode. Balaban alone couldn't finish in a career.

**Sigma Method fit**: HIGH. This is a systematic program. Each step can be formalized.
The obstruction is complexity, not impossibility.

### Route 2: Stochastic Quantization
**Idea**: YM as a stochastic PDE (Langevin equation). Use Hairer-type regularity
structures or paracontrolled calculus.

**Status**: 2D done (Chevyrev-Shen 2023?), 3D partial progress. 4D: singular SPDE,
requires renormalization beyond current technology.

**Key papers**: Parisi-Wu (1981), Hairer (2014 Fields Medal), Chevyrev-Shen, Chandra-Hairer.

**Obstruction**: 4D YM is "supercritical" for regularity structures. The renormalization
problem is essentially the same as Route 1.

**Sigma Method fit**: MEDIUM. More modern technology, but the 4D barrier is the same.

### Route 3: Operator Algebra / Axiomatic QFT
**Idea**: Construct the theory abstractly via its algebra of observables, then prove
spectral gap from algebraic properties.

**Status**: Beautiful framework but almost no concrete results for non-Abelian gauge theories.

**Obstruction**: Too abstract without Route 1 or 2 providing the concrete construction.

**Sigma Method fit**: LOW for construction, potentially HIGH for mass gap (if Route 1 gives the theory).

### Route 4: Lattice + Computer-Assisted Proof
**Idea**: Use rigorous computer-assisted bounds on lattice gauge theory to prove
mass gap at finite lattice spacing, then take the continuum limit.

**Status**: Lattice Monte Carlo gives overwhelming numerical evidence. Rigorous bounds
are much harder. Chatterjee (2020s) has some rigorous lattice results.

**Obstruction**: The gap between numerical evidence and rigorous proof is vast.
Monte Carlo is NOT a proof. Need interval arithmetic on partition functions.

**Sigma Method fit**: HIGH for Odd instance. This is the SOS certificate analog.

### Route 5: Topological / Geometric
**Idea**: Use the topology of the space of connections (moduli space) to constrain
the spectrum. Donaldson theory, instantons, monopoles.

**Status**: Beautiful mathematics but hasn't led to mass gap. Instantons give
tunneling amplitudes, not spectral gaps.

**Obstruction**: The connection between topological invariants and the physical
spectrum is indirect.

**Sigma Method fit**: LOW for direct proof, HIGH for understanding structure.

## Assessment

**Primary route**: Route 1 (Balaban/constructive). This is the only route with
a complete (if unfinished) program. Everything else either feeds into it or
assumes its output.

**Secondary route**: Route 4 (lattice + computer). The Odd instance should pursue this.

**The Even instance should**:
1. Build the paper arsenal (Balaban's 13 papers are the core)
2. Formalize the lattice gauge theory definitions in Lean
3. Formalize the RG framework
4. Attempt to complete Balaban's program (or identify exactly where it breaks)

## Result
Not a proof attempt — this is the route survey. Phase 1 begins.
