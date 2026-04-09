# Attempt 004 — Multiple Mountains Against Three Barriers

**Date**: 2026-04-07
**Phase**: 1 (Multiple Mountains doctrine)
**Track**: theory (Theory)

## The Unique Challenge

P vs NP has THREE barriers that block most proof techniques. Multiple
Mountains doesn't just need different angles on the gap — it needs
mountains that AVOID the barriers entirely.

## Mountain 1: Circuit Complexity (current, stuck at TC⁰)
- Wall: can't prove NEXP ⊄ TC⁰, let alone NP ⊄ P/poly
- Barriers: natural proofs block combinatorial arguments

## Mountain 2: CRYPTOGRAPHY (the empirical mountain)
- Key insight: if P = NP, all public-key crypto breaks instantly.
  RSA, elliptic curve crypto, lattice crypto — ALL broken.
  The entire internet economy is empirical evidence for P ≠ NP.
- The gap from THIS summit: "can we formalize 'crypto works' into a proof?"

**What M2 reveals**: The natural proofs barrier says "if OWFs exist, you
can't use natural proofs." TURN IT AROUND: if we could prove OWFs exist
(even conditionally), we'd get P ≠ NP. The barrier becomes a TOOL:
natural proofs barrier + OWFs exist → P ≠ NP is true (but not by natural proofs).

**Underground connection M1↔M2**: Williams' paradigm uses ALGORITHMS to
prove lower bounds. Crypto provides the HARDNESS ASSUMPTIONS that
algorithms rely on. If we could prove a specific crypto problem is hard
(e.g., factoring requires 2^{n^ε} time), that hardness propagates.

## Mountain 3: LEARNING THEORY (the computational mountain)
- Key insight: PAC learning complexity is tightly connected to circuit
  complexity. If NP ⊂ P/poly, certain concept classes are learnable.
- The gap from THIS summit: "prove specific concept classes are NOT learnable"

**What M3 reveals**: Learning lower bounds avoid the natural proofs barrier
because learning algorithms don't need to be "natural" — they can be
adaptive, randomized, and query-based. The framework is DIFFERENT from
circuit complexity.

## Mountain 4: THERMODYNAMICS (the physics mountain)
- Key insight: Landauer's principle — erasing one bit costs kT ln 2 energy.
  Computation has a thermodynamic cost. If P = NP, you could solve SAT
  using polynomial energy. Does physics constrain this?
- The gap from THIS summit: "does thermodynamics limit computation?"

**Speculative but concrete**: If solving n-variable SAT requires energy
≥ 2^{Ω(n)} × kT ln 2 (exponential erasure), then P ≠ NP follows from
physics. This would be a PROOF FROM PHYSICS, not from mathematics.
The barriers are about mathematical proof techniques — they don't block
physical arguments.

## Mountain 5: META-COMPLEXITY (the frontier mountain)
- Key insight: Liu-Pass (2020): OWFs exist ⟺ time-bounded Kolmogorov
  complexity (Kt) is hard on average.
- The gap from THIS summit: "prove Kt is hard on average"

**What M5 reveals**: This is the NEWEST mountain. It connects crypto (M2)
to complexity theory (M1) through information theory. The barrier analysis:
- Not relativizing (Kt is defined by the INTERNAL structure of computations)
- Not naturalizing (hardness of Kt on average is NOT a "large" property)
- Not algebrizing (Kolmogorov complexity doesn't algebrize)

**M5 survives all three barriers.** It's the most promising mountain.

## The Surrounded Gap

```
M1 Circuit         M2 Crypto
(stuck at TC⁰)     (OWFs → P≠NP)
     \                /
      \    THE GAP   /
       \  P ≠ NP?  /
        \         /
    M5 Meta-complexity
    (Kt hard → OWFs → P≠NP)
        /         \
       /           \
M3 Learning     M4 Thermodynamics
(unlearnability)  (energy lower bounds)
```

**From all 5 mountains**: P ≠ NP is the SAME statement as:
- M1: SAT has no small circuits
- M2: One-way functions exist
- M3: Certain concepts can't be learned
- M4: SAT requires exponential energy (speculative)
- M5: Kt is hard on average

The CHEAPEST intervention (T1DM principle): **M5 (meta-complexity)**.
Liu-Pass already connected OWFs ↔ Kt hardness. If you can prove Kt is
hard on average BY A TECHNIQUE THAT AVOIDS ALL THREE BARRIERS, you get
OWFs, hence P ≠ NP.

Williams' paradigm (M1) + Liu-Pass connection (M5) = the path:
  Faster Kt algorithm → Kt circuit lower bound → OWFs exist → P ≠ NP

## The Honest Caveat

Multiple Mountains helps FRAME the problem but the barriers are REAL.
No mountain has yet produced a proof. The barriers block not just
individual techniques but entire CATEGORIES of argument.

The Multiple Mountains contribution: showing that the SAME gap (P ≠ NP)
is visible from 5 different fields, and the connections between them
(especially M2↔M5 via Liu-Pass) are where progress is likeliest.
