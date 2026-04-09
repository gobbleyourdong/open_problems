# results/k_lower_bound_argument.md — The K Lower Bound: Why It Requires Complexity Theory

**Date:** 2026-04-09
**Type:** Analytical argument (Phase 3 synthesis)
**Addresses:** R1 — What physical quantities bound K in a region?

## The state of the problem

From k_conservation.py: K is NOT conserved. It can go up, down, or stay constant.
From sk_bekenstein_bounds.py: K is bounded above by S_holo.
From k_spec_completeness.py: the laws of physics have K ≈ 21 834 bits.

**What's missing:** a TIGHT LOWER BOUND on K for physically realizable states.

## Why thermodynamics cannot give the tight bound

The 2nd law gives a monotone lower bound on S: S increases in isolated systems.
This makes the S lower bound "tight" in the following sense: you know the minimum S
a state can have after time t (it cannot be less than the initial S).

For K, there is no analogous monotonicity:
- k_conservation.py: sort(random) changes K from 1.00 to 0.056 (94% decrease in one step)
- The minimum K that a state can reach is 0 (all-zeros), achievable in one erasure step
- There is no monotone lower bound on K from thermodynamics alone

**K lower bound cannot be derived from thermodynamics.**

## What computational complexity provides

### The Kolmogorov lower bound (string-theoretic)

For a specific string x: K(x) ≥ n/log(n) in the worst case for random strings (LZ78 lower bound).
This is a WORST-CASE lower bound for specific strings, not a physical bound.

### The circuit complexity lower bound (computational)

For a function f: {0,1}^n → {0,1}, the circuit complexity CC(f) is the minimum number of
gates in a boolean circuit computing f. Circuit complexity provides a lower bound on K:

> K(f) ≥ CC(f) / (n log n)   [up to constant factors]

This is a lower bound on the description length via the circuit complexity of the function.

For PHYSICAL STATES: if a state |ψ⟩ is the output of a quantum circuit of depth d on n qubits,
then K(ψ) ≥ Ω(d × n) bits. The MORE computational steps needed to generate the state, the
HIGHER its K-content.

### The physical realization constraint

**Physical Church-Turing:** every physically realizable state |ψ⟩ can be prepared by a finite
quantum circuit. If the preparation circuit has depth d and width n qubits, then:

K(ψ) ≤ d × n × log(gate count)   [upper bound from circuit description]
K(ψ) ≥ Ω(d × n / log(n × gate count))   [lower bound from circuit complexity theory]

For a physically realizable state, K(ψ) is bounded between the circuit complexity bounds.
This is NOT a tight bound — it depends on the specific state.

## The gap: why no tight physical K-bound exists

For the holographic S-bound, the bound is TIGHT: a black hole at the Bekenstein bound saturates
the S-bound exactly. Every quantum of S corresponds to a specific physical configuration.

For K, no such tight bound exists because:
1. K depends on the specific computational process generating the state, not just the state itself
2. Two states with the same S_holo can have vastly different K (sorted vs random bytes)
3. The K of a state is reference-frame-dependent (changing the description language changes K)

**Consequence for R1:** the tight lower bound on K in a physical region requires knowing:
(a) What physical process generated the state (the generator, not just the state)
(b) The computational complexity of that generator
(c) The minimum circuit depth for any generator of that state class

This is precisely the content of computational complexity theory. Until we can solve problems
like: "what is the minimum circuit depth to prepare a quantum state of hydrogen atom configuration n?"
we cannot give tight K lower bounds.

## A specific open question

**The hydrogen atom K lower bound:** what is the K-content of the ground state |1s⟩ of hydrogen?

Upper bound: |1s⟩ = (1/√π)(1/a₀)^{3/2} exp(-r/a₀) — this is a K-simple expression (~200 bits).
Lower bound: K(|1s⟩) ≥ ? (unknown, requires circuit complexity of preparing this exact state)

The upper bound is trivial (just write the formula). The lower bound requires knowing:
how many quantum gates are needed to prepare |1s⟩ starting from |00...0⟩?

This is an open question in quantum computing (state preparation complexity). If the answer
is Ω(n) gates for n-bit precision approximation, then K(|1s⟩) ≥ Ω(n) bits, which gives
a tight bound (matching the upper bound from the formula).

## Connection to the black hole information paradox

The BH information paradox is exactly about K-information:
- Infalling matter has K > 0 (structured, compressible)
- Hawking radiation is thermal: K ≈ 0 (structureless, maximally random)
- Is K conserved across the horizon?

From k_conservation.py: K is NOT conserved in general (sort, noise injection change K by ~100%).
So the paradox phrased as "K must be conserved" is false — K doesn't have to be conserved.

The real question is: is UNITARY EVOLUTION K-conservative?
- Unitary evolution on a CLOSED system: quantum information is preserved
- But K is not S-information — it is ALGORITHMIC information
- Unitary evolution of a pure state preserves the STATE but may change K
  (because K depends on which description is shortest, which changes under rotation)

**Conclusion for BH paradox:** the paradox only bites if you think K must be preserved.
If K is not conserved (k_conservation.py: it isn't), then Hawking radiation's K ≈ 0
is compatible with the infalling matter having K > 0. No paradox under K-informationalism.

The paradox IS REAL under S-informationalism: S-information (the von Neumann entropy) must
be preserved by unitary evolution. The question is: where does the S-information go?

**This is the experimental discriminant for S vs K informationalism (R2 of what_is_reality):**
- If S-informationalism: BH information paradox is REAL, must be resolved (Page curve)
- If K-informationalism: BH information paradox is DISSOLVED (K need not be preserved)

## Testable prediction

Under K-informationalism: late-time Hawking radiation should NOT show K-structure recovery.
The thermal K ≈ 0 prediction should hold for the entire evaporation process.

Under S-informationalism: late-time Hawking radiation MUST show K-structure recovery (Page curve).
The thermal K ≈ 0 prediction breaks down at the Page time.

**If black hole radiation can be measured with enough precision to detect the K-transition
at the Page time, this would be the experimental discriminant between S and K informationalism.**

In practice: for astrophysical black holes, the Page time vastly exceeds the age of the universe.
For Planck-mass black holes, the Page time ≈ evaporation time ≈ 10^{-44} s. Unobservable.

**The experimental signature is real but inaccessible.** The discriminant exists in principle;
it cannot be measured with current or foreseeable technology.

## Status

This analytical argument:
1. Confirms: K lower bound requires computational complexity theory, not thermodynamics
2. Connects: K-conservation result → BH information paradox resolution under K-informationalism
3. Proposes: BH late-time Hawking radiation K-structure as the S vs K informationalism discriminant
4. Identifies: the gap is the circuit complexity of physically preparing quantum states

The gap is now precisely characterized: it requires quantum circuit complexity lower bounds
for physically realizable states. This is an active research frontier in theoretical computer science.
