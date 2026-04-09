# results/cross_problem_synthesis.md — S/K Bifurcation Across All Physics Problems

**Date:** 2026-04-09
**Scope:** How the S/K bifurcation from what_is_information manifests in all five other physics questions
**Type:** Cross-problem numerical synthesis

## The core finding from what_is_information

The S/K bifurcation: Shannon entropy H (channel capacity, S-information) and Kolmogorov
complexity K (compressibility/structure, K-information) are orthogonal. Once separated:
- Every classical ontology of "information" lands on one side
- The anti-problem (is random noise information?) dissolves
- Physical theories using "information" become ambiguous until they specify which side

## How the bifurcation manifests in the other five physics problems

### what_is_time: the arrow is an S-arrow, not a K-arrow

**Numerical result (entropy_arrow.py):** During gas diffusion:
- H increases: 5.465 → 6.163 bits (+0.698) — S grows
- K-proxy: 0.545 → 0.545 — K stays constant

**Interpretation:** The thermodynamic arrow of time is driven by S-increase. K stays roughly
constant: the macroscopic state description ("all particles in left half" → "uniform in box")
is K-simple in both cases — both are short descriptions. The complexity of the individual
microstates is K-rich throughout.

**Cross-connection:** Time is the dimension along which S grows monotonically (2nd law).
K does not have a temporal arrow in the same way — both initial and final macrostates are
K-simple (though the microstate K evolves differently). The arrow of time is genuinely S-asymmetric.

---

### what_is_nothing: the vacuum is S-rich, K-poor

**Numerical result (vacuum_energy.py):**
- SM Lagrangian: ~2000 chars = ~16 000 bits (K-content of vacuum description)
- Planck-scale modes per m³: ~10^104 (S-content of vacuum fluctuations)
- K/S ratio: ~10^{-101}

**Interpretation:** The quantum vacuum is the most extreme S/K split in physics.
K-description = SM Lagrangian (a few kilobytes). S-content = 10^104 fluctuating modes per m³.
The vacuum is K-poor and S-rich in exactly the same way as π: the generator (laws) is short,
the output (vacuum states) is enormous.

**The cosmological constant problem as an S/K problem:** QFT predicts ρ ~ ρ_Planck because
it SUMS all S modes. The observed ρ_Λ is vastly smaller. The discrepancy is: the S-sum of all
modes gives a prediction 10^120 times too large. If the true physics treats vacuum energy as
a K-quantity (not an S-sum), the discrepancy may be that the SM is doing an S-calculation
when a K-calculation is needed.

---

### what_is_change: K-change is the correct change metric

**Numerical result (zeno_and_change.py, landauer_change.py):**
- K-change metric: K(S2|S1) > 0 ↔ real change
- Stopped clock: K(S2|S1) ≈ 0 (no real K-change)
- DNA mutation: K-change = 2 bits; Landauer cost = 5.93×10^{-21} J; actual cost ~36× above floor
- Neuron firing: K-change = 1 bit; actual cost ~700 million× above floor

**Interpretation:** Physical change is fundamentally a K-information update. The amount of
"change" is measured by K(S2|S1), not by |S(S2) - S(S1)|. S can change without K changing
(e.g., thermal fluctuations: S fluctuates, K stays constant). K-change is the irreversible,
meaningful change.

**Cross-connection to the arrow:** The thermodynamic arrow is S-increase. K-change events
(measurements, decoherence) are qualitatively different — they update what IS the state, not
just how spread out the probability distribution is. S-increase is thermodynamic background;
K-increase is the "events" that constitute change.

---

### what_is_computation: computation is K-manipulation, P vs NP is K-asymmetry

**Numerical result (pnp_compression_asymmetry.py, sat_scaling.py, landscape_k.py):**
- 3-SAT search: doubling period k = 14.24 variables
- Verification: O(n) — K-check is cheap
- Finding: O(2^(n/14.24)) — K-search is expensive
- Hard landscapes: K stays FLAT (K-opaque, no gradient)
- Easy landscapes: K DECREASES (compressible structure → gradient)

**Interpretation:** Computation is K-manipulation. A NP witness is the K-specification of the
solution (few bits). Finding that K-spec requires exponential search through a K-opaque landscape.
The P vs NP question is: is there a K-structure in the search landscape that a polynomial
algorithm can exploit? The landscape K measurements suggest: no, for hard instances.

**Cross-connection to information:** the SAT landscape K-proxy (gzip ratio of remaining clauses)
uses exactly the same measurement tool (gzip) as the sk_plane.py strings. The landscape is
K-opaque in the same sense that a random string is K-opaque: no local compression gradient.

---

### what_is_reality: reality is K-simple (laws), S-complex (history)

**Numerical result (simulation_cost.py, holographic_evolution.py):**
- Physical laws: ~24 000 K-bits (the K-specification of reality)
- Observable universe history: ~10^124 S-bits (holographic bound)
- K/S ratio: 10^{-119}
- S_holo grew from 18 bits (Planck epoch) to 10^124 today

**Interpretation:** Reality is K-poor (laws) and S-rich (history). This is the sharpest
instantiation of the bifurcation: the same "information" that constitutes reality is either
K-trivially small (the laws) or S-astronomically large (the history).

**Cross-connection to all others:** the laws that cause time to have an arrow (S-information),
the laws that make the vacuum have fluctuations (S-rich modes), the laws that make NP hard
(K-opaque landscapes) — all are K-simple. The S-richness of observables is a consequence of
K-simple laws applied to large systems over long times.

---

## Unified pattern: K-simple generators, S-rich outputs

Across all six physics problems, the same pattern:

| System | K-generator | S-output | K/S ratio |
|---|---|---|---|
| Language (what_is_information) | grammar rules | text corpus | ~10^{-3} |
| Arrow of time (what_is_time) | Newton's laws | N-body trajectory | — |
| Vacuum (what_is_nothing) | SM Lagrangian | 10^104 modes/m³ | 10^{-101} |
| Physical change (what_is_change) | laws + initial K | decoherence events | — |
| NP problems (what_is_computation) | problem generator | exponential landscape | — |
| Reality (what_is_reality) | SM + GR (24 KB) | 10^124-bit history | 10^{-119} |

In every case: the K-description of how the system works (the laws, the generator, the program)
is orders of magnitude shorter than the S-content of what the system produces.

**The compression view:** reality is a K-simple program (the SM Lagrangian + GR) running on
a quantum substrate, producing S-rich outputs. The S/K bifurcation IS the distinction between
the program (K) and its outputs (S). Both are legitimately called "information," which is why
the word has been doing two jobs.

## Open cross-problem question

**Is there a physical experiment that distinguishes S-ontology from K-ontology?**

- S-ontology: the universe's information content is the holographic S-bound (10^124 bits).
  Physical laws are just an efficient description of this S-content.
- K-ontology: the universe's information content is the SM Lagrangian (~24 000 bits).
  The S-rich history is an output, not a substrate.

Both are consistent with all current observations (see quantum interpretation underdetermination
result: Copenhagen vs MWI differ by 10^(10^120) with zero observational consequence).

A candidate experiment (from what_is_reality/lv_bounds.py, in progress): if the universe
has a Planck-scale discretization (simulation), photons from cosmological distances should
show energy-dependent speed of light. FERMI-LAT bounds on this would either:
- Confirm Lorentz invariance to Planck precision → S-ontology requires the universe to
  "be" at Planck resolution (10^248-bit simulation), which exceeds the holographic S-bound
- Or admit coarser discretization → K-ontology is consistent (the K-description doesn't
  need Planck precision to reproduce all observations)

This is the experimental signature at the interface of all six physics problems.

## Summary

The S/K bifurcation from what_is_information is not isolated to information theory. It is
the underlying structure of all six physics tier-0 questions:
- Time's arrow: S-arrow (thermodynamic), K-stable (description of macro states)
- Vacuum: S-rich modes (fluctuations), K-simple laws (SM Lagrangian)
- Change: K-updates (measurement/decoherence), S-background (thermal fluctuations)
- Computation: K-search problem (find the witness), S-landscape (exponential state space)
- Reality: K-spec (laws), S-history (holographic bound)

The compression backbone from the philosophy track extends naturally into physics via this bifurcation.
