# results/simulation_cost_findings.md — Reality as Computation: Information-Theoretic Constraints

**Date:** 2026-04-09
**Script:** `numerics/simulation_cost.py`
**Setup:** Bekenstein/holographic bounds, Planck-resolution simulation cost, QM interpretation comparison

## Setup

PROBLEM.md asks: what is reality? One ontology is pancomputationalism — reality is a
computation. The simulation hypothesis is the strong version: we are inside a computation
run by some external agent. This script asks: what are the information-theoretic constraints
on such a computation?

The K-information framing from `what_is_computation` applies: physical laws are finite
K-specifications. If laws + initial conditions specify all observables, reality has a finite
K-description. But the full HISTORY may require much more K-content than the laws.

## Full Results

### Observable universe S-information

| Quantity | Value |
|---|---|
| Observable universe radius | 4.40×10²⁶ m (46.5 billion light years) |
| Ordinary matter energy | 1.50×10⁷⁰ J |
| Bekenstein bound (energy) | 10^100 bits |
| Holographic bound (area) | **10^123.5 bits ≈ 10^124 bits** |
| CMB photon count | 1.47×10⁸⁹ |

The holographic bound sets the maximum S-information storable in the observable universe:
~10^124 bits. This is also the upper bound on any simulation's state size.

### Simulation cost at various precision levels

| Precision | dx (m) | dt (s) | log₁₀(state bits) | log₁₀(total bits) |
|---|---|---|---|---|
| Human neuron | 10⁻⁶ | 10⁻³ | 101 | 122 |
| Cell biology | 10⁻⁹ | 10⁻⁹ | 110 | 137 |
| Atom | 10⁻¹⁰ | 10⁻¹⁵ | 113 | 146 |
| Nuclear | 10⁻¹⁵ | 10⁻²⁴ | 128 | 170 |
| **Planck** | **1.62×10⁻³⁵** | **5.39×10⁻⁴⁴** | **187** | **248** |

Holographic bound: 10^124 bits.

### Physical law K-content

| Theory | Chars | K-bits |
|---|---|---|
| Maxwell equations | ~4 equations | ~32 bits |
| Einstein equations | 1 line | ~8 bits |
| Schrödinger equation | 1 line | ~8 bits |
| Standard Model Lagrangian | ~2000 chars | ~16 000 bits |
| Total (non-redundant) | ~3000 chars | **~24 000 bits** |

Laws: ~24 000 bits. Universe history: ~10^124 bits. Ratio: 10^{119}.

### Quantum interpretation underdetermination

| Interpretation | Real information content | Observational distinction |
|---|---|---|
| Copenhagen | 10^120 bits | identical to MWI |
| Many-worlds | 2^(10^120) ≈ 10^(10^120) bits | identical to Copenhagen |
| QBism | agents' beliefs (epistemic) | identical to both |

## Finding 1: The universe cannot simulate itself at its own resolution

The Planck-resolution simulation requires 10^248 bits. The holographic bound allows only
10^124 bits. The gap is 10^{248−124} = 10^124.

**Precise statement:** any simulation of the observable universe at Planck resolution would
require 10^124 times more information storage than the observable universe itself can contain.
This is not a limit of current technology — it is information-theoretically impossible within
the observable universe's volume.

**Corollaries:**
1. If we are in a simulation, the simulation runs at coarser than Planck precision. The
   simulator does NOT need to track every Planck-scale degree of freedom.
2. A coarser simulation might work. At atomic scale (10^{-10} m), the state has 10^113 bits
   — still below the holographic bound of 10^124 bits. An atom-scale simulation of the
   observable universe for its entire history would need 10^146 bits total — still above the
   bound, but the state at any instant (10^113 bits) is below it.
3. The most relevant question is whether the observed universe is the OUTPUT of a computation
   whose STATE is K-simple — not whether the full computation history fits inside it.

## Finding 2: Laws are K-simple; history is S-complex

Physical laws: ~24 000 bits of K-information.
Observable universe history: ~10^124 bits of S-information.

The ratio is 10^{119}: the history requires ~10^{119} times more information than the laws.

This is structurally identical to the π case from `what_is_information`:
- The GENERATOR (π's formula): O(1) K-bits
- The OUTPUT (π's decimal digits): O(N) bits for N digits
- The STRUCTURE (that the output comes from the generator): captured by the K-description

For the universe:
- The GENERATOR (SM Lagrangian + GR): ~24 000 K-bits
- The OUTPUT (universe history): ~10^124 bits
- The STRUCTURE (that history comes from laws): captured by the K-description

**The K-monist ontology (what_is_computation attempted to dissolve the pancomputationalism question by):**
the laws are the K-specification; the history is the output of running the laws + quantum measurement
randomness. The "computation" is the universe running its own K-specification. The distinction between
"the universe computing itself" and "the universe just being the universe" is one of terminology.

Whether the K-specification (laws) or the S-history is more "real" is the ontological question
PROBLEM.md identifies. The numbers suggest:
- If laws are primary (K-monism): reality is 24 000 bits, replicated locally infinite times.
- If history is primary: reality is 10^124 bits, with the laws being just a short description.

Both interpretations are K-consistent — the laws DO generate the history, and the history DOES
compress to the laws given enough of it. The question is what kind of thing "reality" is.

## Finding 3: Quantum interpretations and underdetermination — the largest numerical gap

Copenhagen vs Many-worlds:
- Copenhagen: 10^120 bits (one outcome per decoherence event)
- MWI: 2^(10^120) ≈ 10^(3×10^119) bits (all branches coexist)

The information-theoretic gap between these two interpretations of quantum mechanics is
incomprehensibly larger than the gap in the cosmological constant problem (10^122 orders).
It is 10^{10^120} vs 10^{120} — a difference of 10^{10^120} in ontological information content.

**Both interpretations are observationally indistinguishable.** The Born rule gives the same
probabilities. No experiment can tell them apart.

**What this demonstrates:** observations underdetermine ontology by a factor of 10^{10^120}.
Two theories can agree on every prediction while differing by more information than the
holographic bound allows to exist in the observable universe. The question "what is reality?"
cannot be answered by observation alone — regardless of what we measure.

This is the sharpest numerical statement of the gap in PROBLEM.md: "observations underdetermine
ontology." It is not just that we haven't measured enough — it is that no measurement could
distinguish Copenhagen from MWI.

## Finding 4: Simulation hypothesis — the specific constraint

The simulation hypothesis says reality is inside a computation by an external simulator.
The information-theoretic constraints:

1. **The simulator's state** must be at least as large as the simulated system's maximum
   K-content at each timestep. At Planck precision: 10^187 bits per timestep — larger than
   what the observable universe can store.

2. **Either:** the simulator runs at coarser precision (e.g., atomic scale: 10^113 bits per
   timestep), OR the simulator is not constrained by the holographic bound (it's outside our
   spacetime, so our holographic bound doesn't apply to it).

3. **The K-simple laws as the simulator:** the most parsimonious simulation hypothesis says
   the "simulator" is just the Standard Model Lagrangian + boundary conditions — 24 000 bits.
   On this reading, the universe IS simulating itself by running its K-simple laws. Whether
   this counts as "being in a simulation" is a question about the word "simulation."

4. **Testable consequence:** if there is an external simulator running at finite precision,
   it should produce discretization artifacts at whatever precision it's using. Candidate
   artifacts: Lorentz invariance violations at Planck scale, pixelation of spacetime.
   No such artifacts have been observed, setting lower bounds on the simulator's precision.

## Sky bridges (numerical)

- **physics/what_is_information** — 10^124-bit holographic bound = maximum S-information.
  Laws = 24 000-bit K-specification. The S/K bifurcation is most visible here.
- **physics/what_is_computation** — the "universe as computation" question from attempt_001
  is made concrete: the computation's STATE is bounded by 10^124 bits; its PROGRAM is ~24 000
  bits. The universe is K-simple in its program, S-complex in its state.
- **physics/what_is_nothing** — the cosmological constant (10^-27 J/m³) is part of the
  boundary conditions (initial/current state), not the laws. It contributes S-information
  to the state but not K-information to the laws.
- **physics/what_is_time** — the holographic bound applies to spatial regions at one time.
  For the full history, the information content grows as more time passes. The early universe
  (low entropy) had much less S-information than today's 10^124-bit bound.

## Next numerical steps

1. **Holographic bound growth over time.** As the universe expands, the Hubble horizon grows.
   Compute S_holographic(t) = π R(t)² c³/(G ħ) as a function of cosmic time t. Plot the
   growth: how did the universe's S-capacity grow from the Big Bang to today? Does it grow
   faster than the number of decoherence events? (Hypothesis: yes — the universe's "RAM"
   grows faster than its computation rate, so it never "fills up.")

2. **Lorentz invariance violation bounds.** If the simulator has Planck-scale discretization,
   photon dispersion relations should show an energy-dependent speed of light:
   v ≈ c(1 − E/E_P). FERMI telescope data (Abdo et al. 2009) bounds this at E/E_P < 10^{-16}.
   Compute what this implies about the minimum simulator precision.

3. **K-content of initial conditions.** The SM Lagrangian has ~24 000 bits. But the laws
   also require initial conditions (the specific values of Λ, baryon asymmetry, etc.).
   Compute the K-content of the standard cosmological initial conditions separately.
   How much of the "program" is in the laws vs the boundary conditions?

## Status

Phase 1 numerics. Three key constraints established:
1. Planck-resolution self-simulation is information-theoretically impossible (exceeds holographic bound by 10^124)
2. Laws are K-simple (~24 000 bits); history is S-complex (~10^124 bits)
3. Copenhagen vs MWI differ by 10^(10^120) in ontological content with zero observational consequence

These three numbers make the reality question precise: reality's K-content is small;
its S-content is bounded; which one is "real" is not empirically decidable.
