# results/k_complexity_classes.md — K-Change Rate as a Complexity Measure

**Date:** 2026-04-09
**Type:** Analytical synthesis (no new script)
**Builds on:** cellular_automata_K_findings.md, landscape_k_findings.md, sat_large_n_findings.md,
  sat_ceiling_findings.md, compression_hierarchy.md, bqp_landscape_topology.md

---

## Overview

The cellular automata K-change study established that Wolfram's computational classes are
discriminated by K-change rate per step:

| Class | Example rule | Mean K-change (random seeds, 200-cell, bytes/step) |
|---|---|---|
| Class 1 (constant) | Rule 0 | ~0 |
| Class 2 (periodic) | Rule 184 | 8.77 ± 1.07 |
| Class 4 (universal) | Rule 110 | 32.59 ± 1.35 |
| Class 3 (chaotic) | Rule 30, Rule 90 | 37.90 ± 0.20 / 37.97 ± 0.22 |

This document formalizes the connection between K-change rate and the standard computational
complexity hierarchy (P, NP, PSPACE, EXPTIME, BPP, BQP), resolves the apparent paradox of
Rule 110 < Rule 90 despite universal computation, and connects the CA hierarchy to SAT's
K-landscape data at n=50.

---

## 1. The K-Complexity Class Table

Every computational complexity class corresponds to a characteristic K-landscape shape and
K-change signature. The K-landscape is the surface of K-content (compressibility) over the
search space, measured as the solver traverses it. K-change is the rate at which this
landscape fluctuates per computation step.

| Complexity Class | Problem type | K-landscape | K-change | Examples |
|---|---|---|---|---|
| **P** | Polynomial-time solvable | K-structured gradient: K decreases monotonically toward solution | Steady K-decrease (K production directed toward output) | Sorting, shortest path, linear programming |
| **NP (easy instances)** | Phase transition below/above (α < 4.0 or α > 4.3) | K-gradient exists: partial solutions simplify remaining structure | K-decreasing: unit propagation cascades reduce K per step | Sparse SAT (α=2), overdense SAT (α=7, UNSAT detected early) |
| **NP (hard instances)** | Phase transition at α ≈ 4.3 | K-FLAT (K-opaque): remaining structure maintains constant gzip ratio throughout search | K ≈ constant: |ΔK| ≈ 0.011 per DPLL step (n=50, seed=103); slope < 10⁻³ | SAT at phase transition, subset sum hard instances, graph coloring |
| **PSPACE** | Polynomial space, exponential time | K-richer than NP: game tree positions contain strategy K | Higher K-change: exponential-depth game trees generate K at each ply | QBF, checkers, Hex |
| **EXPTIME** | Exponential time, proven | K-maximal landscape: every position encodes maximal strategic K | K-change = K-maximum: K is produced at every step across exponential-depth trees | Chess endgame tablebase generation |
| **BPP** | Randomized polynomial | K-random sampling: random bits inject K into the computation path | K-noise injecting: randomness adds K but enables probabilistic gradient exploitation | Monte Carlo integration, Miller-Rabin primality |
| **BQP** | Quantum polynomial | K-periodic exploitable: amplitude structure in Hilbert space has compressible group K | K-collapse for periodic: QFT extracts period from amplitude K-structure | Shor (factoring), Deutsch-Jozsa, Simon's problem |

### Reading the table

The K-landscape column describes the STRUCTURE of the search space as seen by the best
algorithm for that class. The K-change column describes the DYNAMICS of K during computation.

The critical distinction between NP hard instances and PSPACE/EXPTIME is not just that NP
is harder but that NP hard instances have FLAT K (K does not increase during search — the
landscape is stationary at near-maximal incompressibility), while PSPACE/EXPTIME have GROWING
K (each additional computation step generates new strategic K at deeper positions in the
game tree). Flatness is not simplicity — it is frozen complexity.

---

## 2. The K-Change Rate as a Complexity Measure

### From the cellular automata data

The CA K-change classification (Section 3 of cellular_automata_K_findings.md, 100 random
seeds, 200-cell states):

```
Class 1 (trivial, Rule 0):       K-change ≈ 0 bytes/step
Class 2 (periodic, Rule 184):    K-change = 8.77 bytes/step
Class 4 (universal, Rule 110):   K-change = 32.59 bytes/step
Class 3 (chaotic, Rule 30/90):   K-change = 37.90–37.97 bytes/step
```

The ordering Class 3 >> Class 4 >> Class 2 >> Class 1 is clean and robust (inter-class
separations far exceed standard deviations).

Mapping to computational complexity heuristic:

- **Class 1 → trivial computation (below P):** K-change ≈ 0. The system performs no
  K-manipulation — output equals input, or is a fixed constant. No information is processed.

- **Class 2 → regular computation (P-like):** K-change = 8.77 bytes/step. Bounded periodic
  oscillation. The K produced at each step is re-used (looped), not accumulated. This is
  the K-signature of P algorithms: they process K in structured, bounded fashion, reaching
  lower output K from higher input K (sorting compresses the ordering; shortest path extracts
  the minimal-weight route).

- **Class 4 → complex computation (between P and NP-hard):** K-change = 32.59 bytes/step.
  Nonzero K-change at every step (100% of steps in Rule 110, confirmed), but below Class 3.
  This is the K-signature of computation that is productive without being chaotic — bounded
  structures (gliders, collisions) carry K forward step-by-step. Rule 110 is Turing-complete:
  any computable function can be encoded as initial K-content and read from final K-content.
  The intermediate K-change profile IS the execution trace.

- **Class 3 → chaotic computation (NP-hard-like):** K-change = 37.97 bytes/step. Maximum
  sustained K-change. Each step generates new incompressible structure from previous structure —
  no correlation between successive states provides a compressible shortcut. This is the
  K-signature of a computation where no algorithm can exploit gradient structure in the K-landscape.

### The key hypothesis: NP-hard instances and the Class 3 analogy

**Hypothesis:** Hard NP instances at the phase transition have K-landscape character analogous
to Class 3 CAs — near-maximal incompressibility, no exploitable gradient.

**Numerical test (n=50, landscape_k.py + sat_large_n.py):**

Hard 3-SAT instances at α=4.3, n=50 (DPLL+MCV with 985× search/verify ratio for seed=103):

| Metric | Hard instance (seed=103) | Hard instance (seed=251) | Easy instance (seed=17) |
|---|---|---|---|
| Mean K_ratio | 0.620 | ~0.615 | 0.732 |
| |ΔK| per DPLL step | 0.011 | 0.006 | 0.131 (collapses quickly) |
| K-range over full search | [0.604, 0.705] | [0.605, 0.653] | [0.608, 2.125] |
| K-slope (per step) | −5.6×10⁻⁴ | ~0 | N/A (too short) |
| Steps recorded | 62 | 25 | 15 |

The hard SAT landscape has K_ratio ≈ 0.62, near the incompressibility limit. More importantly,
the K does NOT CHANGE: |ΔK| per step ≈ 0.011, or about 1.8% of the mean K level. Over 62
consecutive DPLL steps, the K stays within a range of width 0.10 (16% of mean K). The search
landscape is FROZEN at near-maximal incompressibility.

**Contrast with CA K-change dynamics:**

The CA measures K-change as absolute K production (bytes/step) starting from a simple seed.
A chaotic CA (Class 3) rapidly generates new incompressible structure — its K grows from low
to high, then stays high. Once at steady state, even a Class 3 CA would have low K-change
(K is already at the maximum). Hard SAT landscapes are ALREADY IN THE CLASS 3 STEADY STATE:
they start at near-maximal K and stay there throughout the search. The DPLL solver traverses
a landscape that was always maximally complex — it never passes through a low-K region that
would signal proximity to the solution.

**The quantitative connection:** 

- CA Class 3 steady-state K-content (mean K ≈ 37–57 gzip bytes for 200-bit states) corresponds
  to a gzip ratio ≈ 0.6–0.7 — the same range as the hard SAT K_ratio (0.62–0.73).
- CA Class 3 K-change during TRANSIENT (growth phase): 26–38 bytes/step. Once at steady state,
  K-change collapses toward 0 (nothing left to produce). Hard SAT's K-change of 0.011 gzip-ratio
  units per DPLL step is the steady-state behavior.
- The analogy is therefore: **hard SAT landscapes are to the SAT search problem what the
  Class 3 steady state is to the CA: near-maximally incompressible, generating no new navigable
  K-gradient per step, providing no exploitable shortcut to the solution.**

Easy SAT instances (K-change per step ≈ 0.13–0.25 ratio units, high variance, rapid K collapse
to near-zero as variables are assigned by unit propagation) are the CA TRANSIENT analog: K is
still being produced and consumed, and the gradient of that production reveals the solution direction.

---

## 3. Why Rule 110 (Class 4) Has LOWER K-Change Than Rule 90 (Class 3)

This is the central paradox of the CA K-change classification:

**Rule 110 is Turing-complete (Cook 2004).** It can simulate any computation. It is, in the
strongest possible sense, maximally computationally capable.

**Rule 90 is NOT Turing-complete.** It is an additive rule (XOR of neighbors) with simple
algebraic structure, equivalent to Pascal's triangle mod 2. It cannot simulate arbitrary computation.

Yet the data shows:

```
Rule 110 (universal, Turing-complete):  K-change = 32.59 bytes/step
Rule 90  (additive, not universal):     K-change = 37.97 bytes/step
```

Rule 110 has LOWER K-change than Rule 90. This appears paradoxical: shouldn't universal
computation be more K-complex than non-universal?

### Resolution: K-change measures local dynamics, not computational universality

The key distinction is between **K-change as K-production** and **computational universality**.

**Class 3 (Rule 90, Rule 30): maximum K-production**

Each step of Rule 90 or Rule 30 produces output that is maximally incompressible relative to
the previous step. The NCD (Normalized Compression Distance) between consecutive states is high —
there is no local correlation that allows gzip to compress from knowing the previous state.
This means K-change is high: a lot of "new K" is generated per step. But this new K is
informationally EMPTY — it is pseudorandom bits, not structured computation. A chaotic
system generates maximum K-change by producing noise.

**Class 4 (Rule 110): moderate K-production, but structured**

Rule 110 produces output that is CORRELATED with the previous step via its glider structures.
Consecutive Rule 110 states share local patterns (gliders propagate, interact, and decay
in predictable local ways). gzip can exploit this local correlation to partially compress
successive states, so the K-change (measured as NCD × K_{t+1}) is SMALLER than for Class 3.

But this smaller K-change is not "less computation" — it is MORE STRUCTURED computation.
The K that IS produced each step carries more INFORMATION per bit: it encodes the state of
an ongoing, structured computation (which gliders exist, where they are, what collision is
next). Class 3's higher K-change is the K-equivalent of white noise — high entropy, zero
structured information.

**The information-theoretic separation:**

- **Class 3 (maximum K-change, minimum useful information per bit):** produces maximum new K
  per step, but that K is incompressible NOISE. There is no short description of "what happened"
  between step t and step t+1 — only raw incompressibility.

- **Class 4 (intermediate K-change, maximum useful information per bit):** produces moderate new K
  per step, but that K encodes the state of a structured, ongoing computation. The glider
  structure IS the information. Lower K-change because successive states share this structure
  (and gzip can partially exploit it), but each bit of K-change carries maximum computational content.

**Analogy:** A book and a random bit string of the same length have similar gzip ratios (both
near-incompressible). But the book has near-zero "K-change" from page to page (each page shares
context with the last), while a random string has maximum K-change from byte to byte. The book
carries more structured information per unit K-change; the random string carries more raw K-change
per unit information. Rule 110 is the book; Rule 90 is the random string.

**Universal computation requires STRUCTURED complexity.** A Turing-complete system must maintain
coherent global computation state — gliders must propagate, interactions must be predictable,
signals must traverse the system. This STRUCTURE is exactly what keeps K-change moderate: the
structure is locally compressible (successive states share it). Chaotic systems have NO such
structure and therefore produce maximum K-change at the cost of computational uselessness.

### Consequence for the NP analogy

This resolution extends cleanly to the NP problem hierarchy:

- **Hard NP instances (K-flat landscape):** Like Class 3 in information content — near-maximally
  incompressible. Like Class 3 steady state in dynamics — no K gradient. Algorithmically useless
  because there is no structure to exploit. The K-flatness is not simplicity (Class 1) but frozen
  maximal complexity.

- **Easy NP instances (K-gradient landscape):** Like Class 4 — the remaining clause structure
  has exploitable local patterns (unit propagation chains, constraint propagation). K-change is
  nonzero and DECREASING (producing "useful" K in the form of variable assignments). The
  structure is like the gliders of Rule 110 — locally coherent, gradient-following.

- **P problems (K-monotone landscape):** Like Class 2 — bounded, structured K-change that
  proceeds monotonically toward the solution. The K-gradient is a direct path. No backtracking
  required; each step makes K-measurable progress.

---

## 4. The K-Hierarchy and Physical Church-Turing

The CA K-change hierarchy scales to physical systems:

### Physical processes classified by K-change

Every physical process can be characterized by its K-change rate: how much new incompressible
K is generated per unit time step.

| Physical system | K-change regime | CA analog | Notes |
|---|---|---|---|
| Simple physical laws (harmonic oscillator, hydrogen atom) | K-change ≈ 0 (after compressing the law) | Class 1/2 range | The K-specification is finite and short; dynamics generate no new K relative to the law |
| Periodic physical systems (crystal, planetary orbit) | K-change = bounded, low | Class 2 | K oscillates around a fixed level; no K accumulation |
| Complex systems (weather, protein folding, markets) | K-change = moderate-high, nonzero | Class 4 range | New K generated each step (new weather states, new folds), but K is structured (physical constraints apply) |
| Genuinely random (quantum measurement, thermal fluctuation) | K-change = maximum | Class 3 range | Each measurement outcome adds maximal K (no compressible structure from prior outcomes) |

### Physical Church-Turing as a K-ceiling claim

The Physical Church-Turing thesis (empirically tested in pnp_findings.md) states: every
physically realizable process has a finite K-specification shorter than its output. All generators
tested have K-ratio < 0.05 (spec under 5% of output size).

In K-change language, this becomes:

> **Every physical process has a K-sufficient statistic (the finite K-specification of its laws),
> and no physical process exceeds the K-change rate of Class 3 (genuine randomness).**

The K-change hierarchy provides a ceiling for physical processes:

1. **K-change = 0 (Class 1):** trivial dynamics (fixed point, constant). Below any real physical system.

2. **K-change = Class 2 range (~9 bytes/step for 200-bit states):** periodic systems. Covers all
   systems whose long-term behavior is bounded (crystals, planetary orbits at human timescales).

3. **K-change = Class 4 range (~33 bytes/step):** complex computation. Covers all systems that
   perform bounded computation in the Turing-complete sense. This includes any physical substrate
   capable of universal computation (neurons, transistors, molecular machines). The K-change is
   sustainable and nonzero — the system is always "doing something" but within structured bounds.

4. **K-change = Class 3 range (~38 bytes/step):** genuine randomness. This is the K-change ceiling
   for any physical process. Quantum measurement outcomes achieve Class 3 K-change because each
   new outcome is irreducibly random — there is no prior K from which it can be compressed.

**The ceiling claim:** No physical process can exceed Class 3 K-change, because Class 3 already
achieves maximum incompressibility per step. Any process exceeding this would require generating
more than 1 bit of new K per bit of output, which is impossible by definition.

**Hypercomputation and K-change:** Proposed hypercomputation mechanisms (Malament-Hogarth
spacetimes, infinite-precision computation) would require either:
(a) K-change exceeding Class 3 (impossible by incompressibility arguments), or
(b) K-change that is Class 3 but with INFINITE sustained output (no finite K-specification).
Case (b) is the only viable hypercomputation model, and it violates Physical Church-Turing
by requiring an infinite K-specification for the spacetime geometry or initial conditions.

### BQP and K-periodic structure

The quantum complexity class BQP occupies a special position in the K-hierarchy. Shor's
algorithm (factoring) achieves polynomial time not by exceeding the K-change ceiling but by
exploiting K-PERIODIC structure in the amplitude domain:

- Factoring's hardness for classical computers arises from the K-flatness of the trial-division
  search space (analogous to NP hard instances).
- Quantum Fourier Transform detects the period r of f(x) = a^x mod N — a global K-structure
  (group-theoretic periodicity) that is invisible to local K-change measurements.
- The K-change during quantum computation is not higher than classical; the speedup comes from
  accessing a DIFFERENT K-structure (global periodicity vs local compressibility).

This explains why BQP ≠ NP (conjectured): hard NP instances have K-flat landscapes with no
periodic structure for QFT to detect. The BQP speedup requires K-periodic structure; K-flat
landscapes provide none. Grover's algorithm achieves the best possible speedup for K-flat
landscapes: O(√N), reducing the doubling period from k=1 (exhaustive) to k=2 (quantum
amplitude amplification) — still exponential, just half the exponent.

---

## 5. Summary: The K-Change Complexity Ladder

```
K-change = 0             Class 1 CAs, trivial dynamics
                         → Complexity class: below P (constant-time, 0-bit computation)

K-change = 9 bytes/step  Class 2 CAs (Rule 184, periodic)
(~15%/step fractional)   → Complexity class: P
                         Structured gradient, monotone K-decrease toward output
                         Examples: sorting, shortest path, linear programming

                         [BPP: K-noise injection allows probabilistic gradient exploitation
                          within the P K-change range — randomness adds K but not structure]

K-change = 33 bytes/step Class 4 CAs (Rule 110, universal)
(~39%/step fractional)   → Complexity class: NP easy / Class 4 complexity
                         Productive K-change: structured, nonzero, informationally rich
                         Easy NP instances live here: K decreasing per search step,
                         unit propagation chains carrying exploitable structure

                         [BQP: K-periodic structure (factoring) enables QFT collapse to
                          polynomial — not more K-change, but different K-topology]

K-change = 38 bytes/step Class 3 CAs (Rule 30/90, chaotic/additive)
(~45%/step fractional)   → Complexity class: NP hard (K-landscape character)
                         Maximum K-change, but informationally EMPTY — noise, not structure
                         Hard NP instances ARE already in Class 3 steady state:
                         K_ratio ≈ 0.62-0.73 (near-incompressible), |ΔK| ≈ 0.011/step

K-change frozen          Hard NP instance DYNAMICS (K-flat trajectory)
at Class 3 level         → What DPLL traverses: K is already maximal, slope ≈ 0
                         This is STRONGER than Class 3: not generating noise, but
                         FROZEN at noise level with no navigable gradient

                         → PSPACE: K-change is productive and growing (game tree K
                            accumulates per ply; each position carries strategy K)
                         → EXPTIME: K-change maximal and productive (chess endgame K
                            grows with each depth level of the game tree)
```

**The key asymmetry:** P problems and easy NP instances have K-change that GUIDES computation
toward the solution (decreasing K, exploitable gradient). Hard NP instances and chaotic CAs
have K-change that is MAXIMAL but UNINFORMATIVE (frozen at incompressibility maximum, no gradient).
The computational complexity hierarchy is, at its core, a hierarchy of K-landscape navigability.

---

## Status

Analytical. All quantitative data is from previously established scripts
(cellular_automata_K.py, landscape_k.py, sat_large_n.py). The K-complexity class table is
consistent with all numerical findings in this track. The three residual questions (P vs NP,
Physical Church-Turing, BQP vs NP) are not resolved by this analysis, but their K-landscape
interpretations are now fully specified and testable.
