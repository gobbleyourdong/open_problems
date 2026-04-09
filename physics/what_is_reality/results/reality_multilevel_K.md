# Reality at Three K-Levels: A Formal Statement

**Date:** 2026-04-09
**Track:** what_is_reality — K-informationalism synthesis
**Depends on:** k_informationalism_thesis.md, simulation_detectability_findings.md,
  lv_bounds_findings.md, simulation_cost_findings.md

---

## The Central Claim

Reality is not a single thing described at a single level of information. It operates
simultaneously at three distinct K-levels, each with a different information-theoretic
character, a different origin, and a different role in constituting what we call "reality."

---

## Level 0: K_laws — The Dynamical Laws

**K = 21,834 bits**
**Source:** Standard Model Lagrangian + General Relativity (k_spec_completeness.py)
**Character:** Approximately physically invariant (~15% variation across unit systems; see k_symmetry.py)

### What it specifies

K_laws is the compressed regularity stack — the full set of dynamical laws governing
all known physical interactions:

| Component | Bits |
|---|---:|
| SM Lagrangian structure | 21,549 |
| SM 19 free parameters | 186 |
| GR 3 parameters (G, Λ, Ω_k) | 20 |
| ΛCDM initial conditions (6 params) | 44 |
| Symmetry breaking choices | 35 |
| **Total** | **21,834** |

### Role

K_laws specifies WHICH regularities govern the system. Given K_laws, the evolution of any
initial state is determined (up to quantum measurement outcomes). K_laws is the "program"
of which the universe is the output.

### Physical invariance

The 21,834-bit figure is approximately unit-independent. The dominant content —
dimensionless coupling constants α, α_s, sin²θ_W — is exactly unit-invariant. The
~15% variation across SI, natural, and Planck unit systems is gzip-noise from text
encoding, not genuine K variation.

### What it does NOT specify

K_laws does not specify which particular quantum state the system is in, nor does it
specify measurement outcomes. It specifies the rules; it does not determine the game's
particular history.

---

## Level 1: K_state — The Quantum Configuration

**K_laws ≤ K_state ≤ S_holo**
**Source:** K_laws + initial conditions + quantum measurement outcomes
**Character:** Description-relative — K_state depends on the choice of description language

### What it specifies

K_state is the information needed to specify the current quantum configuration of the
system, given K_laws. It is bounded below by K_laws (you need at least the laws to
describe any state) and above by S_holo (the holographic ceiling on all accessible
information).

In practice, K_state grows as the universe's history accumulates measurement outcomes
and decoherence events. Each quantum measurement adds at most one bit of genuine
K_state that was not determined by K_laws.

### Description-relativity

K_state is not language-independent. The same physical configuration has different
K_state values under different description languages, reference frames, or
coarse-graining choices. This is not a defect — it is the correct behavior for
K-information, which always measures "complexity relative to a description language."

The description-relativity of K_state is why K-informationalism is not the claim
that "reality is K_state bits" — that claim would be ill-defined. Instead,
K-informationalism claims that K_laws (which IS approximately language-independent
for the reasons above) is primary.

### Role

K_state specifies WHICH state the system is in, given K_laws. It is the "current
memory contents" of the computation whose program is K_laws.

---

## Level 2: S_holo — Observable Distinguishable States

**S = 10^124 bits**
**Source:** Holographic principle: S = A × c³/(4Għ) for the observable universe
**Character:** Language-independent — counts physical microstates, not descriptions

### What it specifies

S_holo is the upper bound on the number of distinguishable physical configurations
accessible from outside a region. It is set by the area of the region's boundary
(the Hubble horizon for our observable universe), not by its volume.

| Quantity | Value |
|---|---|
| Observable universe radius | 4.40 × 10^26 m |
| Boundary area | 2.43 × 10^54 m² |
| S_holo | 10^124 bits |

### Language-independence

Unlike K_state, S_holo does not depend on a description language. It counts physical
microstates — the number of distinct configurations the region could be in as measured
by an outside observer. This is a physical quantity, not an information-theoretic one.

### Role

S_holo is the upper bound on information accessible from outside the region. It is not
the information the region "actually has" — it is the maximum distinguishable information
an external observer can receive from the region. This is why it governs:

- The information paradox (what an observer outside a black hole can receive)
- The simulation cost (how many bits must be stored to simulate the region)
- The compression ratio: K_laws / S_holo = 21,834 / 10^124 ≈ 10^{-120}

---

## The Three-Level Structure

```
Level 0: K_laws = 21,834 bits
         "The program"
         Approximately physically invariant
         Specifies WHICH regularities govern

         ↓ generates (via quantum evolution + measurement outcomes)

Level 1: K_state
         K_laws ≤ K_state ≤ 10^124 bits
         "The current memory contents"
         Description-relative
         Specifies WHICH state given the program

         ↓ bounded by

Level 2: S_holo = 10^124 bits
         "The RAM ceiling"
         Language-independent
         Upper bound on externally-accessible distinguishable information
```

The compression ratio K_laws / S_holo = 10^{-120} is the sharpest numerical
statement of K-informationalism: the laws of physics are 10^120 times simpler
than the history they generate.

---

## Where the Open Questions Live

### The Simulation Question (Level 0)

"Is K_laws the output of a simulation program running in some external hardware?"

This question operates at Level 0. It asks whether the 21,834-bit regularity stack
was *itself* the output of a computation by an external agent.

**Why it is metaphysically meaningful:** the question is well-formed. K_laws is a
finite object; it could, in principle, be the output of a shorter program running on
external hardware. This is exactly the Kolmogorov framework applied one level up.

**Why it is empirically inaccessible:** any external simulator would have to:

1. Be outside our spacetime (to hold 10^61 times our holographic memory — see
   simulation_detectability_findings.md)
2. Use sub-Planckian cells (to avoid LIV detection — cell ≤ 0.1395 × l_P)
3. Leave no observable signature within our Level 2 boundary

The simulator operates outside Level 2. No experiment within our spacetime can
access it. The simulation question is therefore *empirically inaccessible* in the
strong sense: not merely "we haven't looked hard enough," but "the simulator, if
it exists, leaves no signature accessible to any observer within our S_holo."

**Numerical precision:** the claim "empirically inaccessible" has a precise meaning here.
The LIV bound tells us that any detectable simulator signature would require cells
≥ 0.1395 × l_P. Such cells are already excluded (they produce Δt ≥ 0.86 s at GRB
090510). An undetected simulator must use sub-Planckian cells — which means its
physical substrate has an energy scale ≥ 7.2 × E_P, i.e., it operates at physics
beyond our Planck scale. Such physics is, by construction, outside the regime of
any measurement our S_holo can receive.

### The Information Paradox (Levels 1–2)

"When a black hole evaporates, does Level 1 (K_state) information escape as Level 2
(S) radiation?"

This question operates at the boundary of Levels 1 and 2. It asks whether the
specific quantum configuration of infalling matter (K_state) is encoded in the
Hawking radiation (S-observable).

**K-informationalism's answer:** K_state *can* be destroyed. The black hole
evaporation can erase the specific quantum measurement outcomes that constitute
K_state (Level 1) without violating any fundamental law at Level 0 (K_laws).
K_laws does not require K_state to be preserved — it is quantum measurement
outcomes that produced K_state in the first place, and those are not required
to be reversible.

**S-informationalism's answer:** Level 2 must be preserved by unitarity. S_holo
is a count of physical microstates, and unitary evolution preserves the number of
distinguishable microstates. Information must escape in Hawking radiation.

**The stakes numerically:** if a solar-mass black hole evaporates, it destroys a
K_state that could be as large as S_Bekenstein(M_sun) ≈ 10^77 bits. K-informationalism
says those 10^77 bits are simply gone — they were quantum measurement outcomes, not
part of K_laws, and their destruction is not a violation of anything at Level 0.
S-informationalism says they must re-emerge, encoded in ~10^67 Hawking photons
with extraordinarily subtle correlations (see black_hole_k_findings.md).

---

## K-Informationalism: The Formal Position

K-informationalism is the claim that **Level 0 is ontologically primary**.

More precisely:

1. **K_laws is real in the strongest sense.** The 21,834-bit regularity stack is not
   a description of reality — it IS the fundamental structure of reality. It is the
   one object in the universe that is approximately language-independent, compression-stable,
   and physically invariant.

2. **K_state is real but derivative.** The specific quantum configuration is real —
   it causes things — but it is constituted by K_laws operating on quantum measurement
   outcomes. It is not separately "fundamental." When K_state is destroyed (black hole
   evaporation, decoherence), no fundamental structure is lost.

3. **S_holo is a bound, not an ontology.** The holographic entropy is the ceiling on
   what an external observer can distinguish — it is an epistemological fact about
   observation, not an ontological fact about what exists. Reality is not "10^124 bits
   stored somewhere."

4. **The simulation question is Level 0 self-referential.** Asking whether K_laws is
   itself computed is asking whether the fundamental structure of reality is the output
   of a deeper fundamental structure. This is meaningful but empirically inaccessible:
   by definition, the Level -1 structure (the simulator) leaves no signature in Level 2.

---

## Summary Table

| Level | Name | Value | Origin | Character | Role |
|---|---|---|---|---|---|
| 0 | K_laws | 21,834 bits | SM + GR | Approx. physically invariant | Specifies WHICH regularities |
| 1 | K_state | K_laws to 10^124 bits | K_laws + QM outcomes | Description-relative | Specifies WHICH state |
| 2 | S_holo | 10^124 bits | Holographic principle (area) | Language-independent | Upper bound on observable info |

**Open questions by level:**

| Question | Level | Status |
|---|---|---|
| Is K_laws itself computed? (simulation) | Level 0 | Empirically inaccessible |
| Does K_state escape black holes? (information paradox) | Levels 1–2 | Technically open |
| Is K_laws the minimal description of reality? | Level 0 | Confirmed (21,834 bits computed) |
| Can K_state exceed S_holo? | Levels 1–2 | No — S_holo is the ceiling |
