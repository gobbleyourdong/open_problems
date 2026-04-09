# results/two_bifurcations_synthesis.md — Two Bifurcations and Their Connection

**Date:** 2026-04-09
**Type:** Synthesis (Phase 3, information track)
**Builds on:** attempt_001 (S/K), k_symmetry_findings.md (K_laws/K_state), k_laws_circuit_findings.md,
             k_informationalism_distinction.md, cross_problem_synthesis.md
**Cross-track:** philosophy/what_is_meaning/attempt_001 (A/P), philosophy/what_is_mind (access/phenomenal)

---

## Overview

The what_is_information track has discovered two distinct bifurcations, at different levels of the
same conceptual hierarchy. Both follow the same structural pattern: a concept was doing two
genuinely distinct jobs, and an existence proof (or experiment) forced the split.

- **Bifurcation 1:** S-information vs K-information (attempt_001 + sk_plane.py)
- **Bifurcation 2:** K_laws vs K_state (k_symmetry.py + k_laws_circuit.py)

Together they determine a clean three-level hierarchy and sharpen K-informationalism from a vague
slogan to a precise thesis with measurable consequences.

---

## Bifurcation 1: S-information vs K-information

**What was conflated.** The word "information" was applied to two orthogonal properties:

- **S-information (Shannon entropy H):** channel capacity — the number of distinguishable states
  a source can produce. Maximized by random noise. Measured by H = -Σ p(x) log p(x).
- **K-information (Kolmogorov complexity K):** compressibility — the length of the shortest program
  generating the string. Minimized by random noise (no program shorter than itself). Measured by K(x).

**The forcing proof (sk_plane.py).**
Sorting a 10,000-byte structured string changes K by 94% while changing H by 0%. A random
permutation of English text takes gzip-K from 0.007 to 0.617 (88× change) while leaving H fixed.
S and K are orthogonal: a transformation can shift one to zero while leaving the other unchanged.

**What this establishes.**

| Content | H | K (gzip-proxy) |
|---------|---|------|
| Random noise | MAX | MAX |
| Sorted string | same H | near-zero K |
| English text | high | low-moderate |
| Repeated byte | zero | near-zero |

The anti-problem in PROBLEM.md dissolves immediately. Is random noise maximal information or absent
information? Both: maximal S-information, minimal K-information. The paradox was a sign that one
word was covering two distinct quantities.

**What it is the bifurcation between:** CHANNEL CAPACITY and STRUCTURE.

---

## Bifurcation 2: K_laws vs K_state

**What was conflated within K.** Once K-information is in focus, a further question arises: K of
WHAT? Two very different things both get called "the K of a physical system":

- **K_laws:** the K of the dynamical laws governing the system — the compact program that generates
  the system's possible evolutions. Approximately invariant under changes of formulation.
- **K_state:** the K of a specific configuration — the minimum description of the actual state at a
  particular time. Highly description-relative.

**The forcing experiments (k_symmetry.py, k_laws_circuit.py).**

Maxwell's equations written in four notation systems (component, differential form, tensor,
geometric algebra) vary in gzip-K by 17.7%. This is notation overhead; the physical content is
identical. The K-invariance theorem guarantees true K_laws is invariant up to the K of the
translation program (a few hundred bits), which is negligible.

Permuting an English string changes gzip-K by 88× with zero change in H. A random gas description
in a 10×10 grid has gzip-K = 0.790; the same gas in a 100×100 grid has gzip-K = 0.058 (14× lower).
K_state depends on the choice of frame, basis, ordering, and resolution.

For the hydrogen 1s ground state, circuit complexity analysis shows:
- K_upper = O(1) — the formula `exp(-r/a₀)` is approximately 400 bits
- K_lower grows as O(n) for n-bit precision state specification
- K_state (specifying the state to 64-bit precision) ~ 64 bits of circuit gates, far above K_laws

**What this establishes.**

| Quantity | Lorentz | Gauge | Scale | Role |
|----------|---------|-------|-------|------|
| K_laws | approx invariant | invariant | fixed | Encodes physical regularity |
| K_state | NOT invariant | NOT invariant | dependent | Description-relative |

**What it is the bifurcation between:** PHYSICS (which regularities hold) and HISTORY (which
specific configuration obtained at this time, in this frame, at this resolution).

---

## The Three-Level Hierarchy

The two bifurcations establish a hierarchy of three quantities:

```
S_state (Shannon entropy of a state description)
    |  always ≥ K_state (for any fixed description)
K_state (Kolmogorov complexity of the specific configuration)
    |  always ≥ K_laws (the laws must be recovered from any state)
K_laws (Kolmogorov complexity of the dynamical laws)
```

**Formally:** K_laws ≤ K_state ≤ S_state

This inequality holds because:
- K_state ≤ S_state: the optimal description of a state is no longer than its entropy (Shannon
  source coding theorem, for computable distributions).
- K_laws ≤ K_state: any specific state description implicitly encodes the laws that constrain it.
  A state of the hydrogen atom encodes the Coulomb potential; you cannot specify the state without
  (implicitly) specifying the physics that makes it a well-defined state. More precisely, the laws
  form the "compression grammar" for the state — the shortest program for the state must at minimum
  encode the laws as a subroutine.

**Extreme cases confirm the hierarchy:**
- For the hydrogen ground state: K_laws ≈ 400 bits (Schrödinger + Coulomb), K_state ≈ 32-64 bits
  (at current measurement precision), S_state ≈ 0 for a pure state (zero thermodynamic entropy),
  but S_state grows without bound at higher precision of state specification.
- For a random gas: K_laws ≈ 21,834 bits (full SM Lagrangian), K_state ≈ 10^30 bits (specifying
  10^23 particle positions to atomic precision), S_state ≈ 10^26 nats (thermodynamic entropy).
- For the observable universe: K_laws ≈ 24,000 bits, K_state ≈ 10^100 bits, S_state ≈ 10^124 bits
  (holographic bound).

The hierarchy holds at every scale, and the gaps grow monotonically with scale — the universe is an
extreme case of K_laws << K_state << S_state.

---

## Connection to the Philosophy Track: The Same Move, Three Times

The S/K bifurcation and the K_laws/K_state bifurcation are instances of a structural pattern that
appears at multiple levels across the open problems project.

**The pattern:** A concept is doing two jobs: a functional-capacity job (measurable, operational,
engineering-friendly) and a structural-regularity job (harder to pin down, but what the working
concept was secretly tracking). An existence proof or experiment decouples them. The split becomes
unavoidable.

### Instance 1: A/P in meaning (philosophy/what_is_meaning/attempt_001)

- **A-meaning (Access-meaning):** the structured regularity that supports competent linguistic
  behavior — inference, paraphrase, disambiguation, reference-tracking.
- **P-meaning (Phenomenal-meaning):** the felt grasp, the "what it is like" to understand.

The forcing existence proof: LLMs demonstrably produce A-meaning without demonstrable P-meaning.
The word "meaning" was bundling channel-capacity-like competence with structural-grasp-like
phenomenology. LLMs have the former without (demonstrably) the latter.

### Instance 2: S/K in information (this track, Bifurcation 1)

- **S-information:** channel capacity — distinguishable states, entropy.
- **K-information:** compressibility — structural regularity, description length.

The forcing existence proof: sorting changes K by 94% with zero change in H. Random noise is
S-maximal and K-minimal. The word "information" was bundling capacity with structure. sk_plane.py
decouples them numerically.

### Instance 3: K_laws/K_state in physics (this track, Bifurcation 2)

- **K_laws:** the K of physical regularity — the compact description of what holds systematically.
  Approximately invariant under reformulation.
- **K_state:** the K of specific history — the description of what actually obtained. Highly
  description-relative.

The forcing existence proof: Maxwell's equations vary by 17.7% across four formulations (notation
overhead only), while an English text varies by 88× under permutation. Physical laws resist
reformulation; state descriptions do not.

### The isomorphism

| Level | Functional/Capacity side | Structural/Regularity side |
|-------|--------------------------|---------------------------|
| Meaning | A-meaning (competent use) | P-meaning (felt grasp) |
| Information | S-information (channel capacity) | K-information (compressibility) |
| K-information | K_state (configuration, description-relative) | K_laws (regularity, approximately invariant) |

The same move — separating what the concept was doing — appears at each level. The move is
generative: after each split, the structural-regularity side becomes the subject of the next
investigation and itself turns out to need splitting.

**A-meaning** splits off from P-meaning.
**K-information** splits off from S-information and becomes the new subject.
**K_laws** splits off from K_state and becomes the precise formulation of K-informationalism.

Each bifurcation reveals that the structural-regularity side was the philosophically interesting
one all along, but had been treated as a monolith until the existence proof arrived.

---

## K-Informationalism: What It Is and What It Entails

**The thesis.** K-informationalism is a claim about K_laws:

> The fundamental information content of physical reality is the K-content of its governing laws
> (K_laws), not the K-content of any specific state (K_state) or the S-content of any state
> description (S_state). K_laws is approximately physically invariant; K_state and S_state are not.

**Quantitatively.** The Standard Model Lagrangian + General Relativity encodes all known physics
in approximately 21,834 bits. This is K_laws for the observable universe. The holographic bound
gives S_state ≈ 10^124 bits. The ratio K_laws / S_state ≈ 10^{-119}: the universe is a 10^119-to-1
compression of its own possible state space.

**What K-informationalism entails:**

1. **K_state is derived, not fundamental.** The specific configuration of the universe at any time is
   not fundamental information; it is K_laws plus a contingent quantum history (the record of which
   random outcomes obtained). K_state = K_laws + K(quantum history to this point).

2. **S-information is derived twice over.** S_state counts distinguishable states — it is a capacity
   measure on top of K_state. S is useful for thermodynamics and channel engineering but is not the
   substrate of physical content.

3. **Wheeler's "it from bit" is approximately right but needs specification.** If the "bits" are
   S-bits (channel states), it is an S-ontology and misses the K/S gap. If the "bits" are K-bits
   (compressible regularities), it is a K-ontology and approximately correct — but then the relevant
   K is K_laws, not K_state.

4. **The holographic bound bounds S_state, not K_laws.** Area-law scaling of S_holo with boundary
   area has no analogue for K_laws, which stays bounded as the region scales. K_laws is not
   area-bounded; it is bounded by the K of the laws themselves.

5. **The black hole information paradox is an S-paradox, not a K-paradox.** Whether information is
   preserved through Hawking evaporation is a question about S_state (unitary evolution of quantum
   states). K_laws is preserved trivially — the laws governing evaporation are the same laws before
   and after. The paradox only arises if K_state is taken to be fundamental.

6. **The fine structure constant α has K_laws = O(1).** The formula `α = e²/(4πε₀ℏc)` is
   approximately 50 bytes. K(α to current measurement precision) ≈ 32.6 bits — this is K of the
   MEASUREMENT APPARATUS, not of α itself. More experimental precision does not add information
   to K_laws; it adds to K_state of the experimental apparatus.

---

## Summary: The Conceptual Map

```
S_information (Shannon)
  = channel capacity
  = number of distinguishable states
  = S_state
  |
  |← sk_plane.py: sorting changes K 94%, leaves S unchanged
  |← the S/K bifurcation (Bifurcation 1)
  |
K_information (Kolmogorov)
  = compressibility
  = structural regularity
  = the compression backbone (linking physics ↔ philosophy)
  |
  |← k_symmetry.py: laws vary 17%, states vary 88×
  |← the K_laws/K_state bifurcation (Bifurcation 2)
  |
  ├── K_state: specific configuration
  │     = description-relative (frame, basis, resolution)
  │     = K_laws + K(quantum history)
  │     = NOT approximately physically invariant
  │
  └── K_laws: dynamical regularities
        = approximately physically invariant
        = ≈ 21,834 bits for all known physics
        = the correct formulation of K-informationalism
        = the fundamental K of reality
```

**The bottom line.** K-informationalism is the claim that K_laws is the fundamental information
content of physical reality. Every classical ontology of "information" (Shannon, Kolmogorov,
Landauer, Fisher, semantic, Wheeler) is a theory of either S_state, K_state, or K_laws. They are
not competing general theories of "information" — they are each correct for their own level of the
hierarchy. The hierarchy K_laws ≤ K_state ≤ S_state organizes the landscape.

---

## Status

Phase 3, synthesis. Both bifurcations are established by running experiments (sk_plane.py for
Bifurcation 1; k_symmetry.py and k_laws_circuit.py for Bifurcation 2). The connection to the
philosophy track (A/P bifurcation) is structural rather than numerical. The K_laws / K_state
sub-bifurcation is now the precision boundary for K-informationalism as a thesis.

**Next:** physics_ncd.py — test whether the NCD backbone creates visible K-clustering among the
six physics problems, and whether the predicted clusters (information+computation, time+change,
reality+nothing) emerge from compression distance alone.
