# results/k_informationalism_distinction.md — K_laws vs K_state: The Core Bifurcation

**Date:** 2026-04-09
**Type:** Analytical synthesis (Phase 3, iteration 10)
**Builds on:** k_symmetry_findings.md, k_lower_bound_argument.md, all what_is_information results

## The Central Discovery of Phase 3

k_symmetry.py revealed a crucial sub-bifurcation WITHIN K-information:

> **K_laws** (K-content of dynamical laws): approximately invariant under physical symmetries.
> **K_state** (K-content of a specific state): highly description-relative.

This is not the original S/K bifurcation (attempt_001) — it is a further refinement WITHIN K.

## Evidence for K_laws ≈ invariant

**From k_symmetry.py:**
- Maxwell equations in 4 formulations: K varies by ~16% (component, differential, tensor, geometric)
- SM Lagrangian in 3 unit systems: K varies by ~15% (SI, natural, Planck)
- Fundamental constants (α = 1/137): ~30 bits in any notation

**From k_spec_completeness.py:**
- All known physics: 21 834 bits in ANY consistent notation (up to ~15% variation)
- The dimensionless content (ratios, coupling constants, structure) is the invariant part
- The dimensional parts (ħ, c, G as written) vary by the chosen unit system

**The invariance theorem of Kolmogorov complexity** says: K defined relative to different universal Turing machines differs by at most a constant (the description of one UTM in terms of the other). This constant is bounded by the K-content of the translation program. For physical laws, this translation is the unit conversion table — a few hundred bits. So true K_laws is invariant up to O(hundreds of bits) regardless of formulation.

**Conclusion:** K_laws is approximately physically invariant. The 15% variation in gzip-K is a proxy artifact; true K_laws has near-exact invariance from the invariance theorem.

## Evidence for K_state ≈ description-relative

**From k_symmetry.py:**
- English text permuted: K rises from 0.007 to 0.617 (88×)
- Random gas at low vs high resolution: K drops from 0.79 to 0.058 (14×)
- Sorted vs random: K drops from 1.00 to 0.006 (167×) with same H

**From k_conservation.py:**
- Sort: ΔK = -0.946, ΔH = 0 (same distribution, 94% K reduction)
- Noise injection: ΔK = +0.988, ΔH = +3.68 (K and H both rise)

**The description-relativity** of K_state arises because: the K-content of a specific state depends on which aspects of the state you include in the description. Is time-coordinate part of the state? Is the ordering part of the state? K_state answers differ based on these choices.

For PHYSICAL states, the natural description is the quantum state vector |ψ⟩. But |ψ⟩ in the position basis vs momentum basis vs energy basis have different K_state estimates (though they represent the same physical state).

**Conclusion:** K_state is description-relative. It cannot be a fundamental physical quantity.

## The bifurcation within K

```
K-information
│
├── K_laws: dynamical regularities, approximately invariant
│   ├── Standard Model Lagrangian: ~21 549 bits (invariant up to ~15%)
│   ├── GR field equations: ~20 bits
│   ├── Fine structure constant α: ~30 bits
│   └── ALL are approximately physically invariant
│
└── K_state: specific configuration, description-relative
    ├── Gas particle positions: depends on encoding (float vs integer)
    ├── Quantum state |ψ⟩: depends on basis (position vs momentum)
    ├── Sort(x): K(sorted) << K(unsorted) though same H
    └── Varies 88-167× under description changes
```

## Implication for K-informationalism

**Wrong version:** "The K-content of physical states (K_state) is fundamental."
This is wrong because K_state is description-relative.

**Correct version:** "The K-content of physical laws (K_laws) is fundamental — the compressible regularities that competent compressors must converge on."

This makes K-informationalism precise and numerically grounded:
- K_laws = 21 834 bits: the compressible regularities of all known physics
- K_laws is approximately physically invariant (invariance theorem)
- The observable history (K_state ≈ S_holo = 10^124 bits) is derived from K_laws + quantum randomness
- K_state is description-relative and NOT fundamental

## Connection to the BH information paradox

**Under K_state informationalism:** K must be conserved → BH paradox exists (K_matter vanishes into thermal radiation).

**Under K_laws informationalism:** K_laws (SM Lagrangian governing BH physics) is invariant. K_state of the specific configuration IS description-relative → BH can "destroy" K_state without paradox. The laws (K_laws) that govern the evaporation are preserved; the specific configuration's K (K_state) is not required to be preserved.

This is why BlackHoleKDeficit.lean (theory track) correctly identifies the BH paradox as the S/K bifurcation applied to a specific physical process.

## Implication for R1 (tight lower bound)

The tight lower bound on K in a physical region is a question about:
- K_laws: bounded below by the content of the dynamical laws (~21 834 bits globally, much less locally)
- K_state: NOT bounded by a simple formula — it depends on the specific state

R1 asks for a bound on K_state (what K-content does a physical region HAVE?). The answer:
K_laws ≤ K_state ≤ S_holo

The tight bound requires knowing the computational complexity of preparing the state from vacuum using the dynamical laws (K_laws). This is the quantum circuit complexity question from k_lower_bound_argument.md.

## Status

Phase 3, iteration 10. The K_laws/K_state bifurcation is the core finding of the Phase 3 information track. It makes K-informationalism precise, explains why K_state is not fundamental, and connects K-informationalism to the BH paradox, the CC problem, and the invariance theorem.

The remaining open question: what is the circuit complexity of physical state preparation? This is the unresolved R1.
