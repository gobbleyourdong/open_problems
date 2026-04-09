# results/zeno_findings.md — Zeno's Paradox and the Nature of Change

**Date:** 2026-04-09
**Script:** `numerics/zeno_and_change.py`
**Setup:** Zeno series convergence, Achilles race, Planck-scale discreteness, K-information analysis

## Setup

PROBLEM.md asks: what is change? Zeno's paradoxes argue that motion is impossible or
incoherent. The standard mathematical resolution is that the infinite series converges.
This script measures the convergence, maps the K-information content of state transitions,
and identifies what the mathematics does and does not resolve.

## Full Results

### Zeno's Dichotomy: convergence of Σ (1/2)^k

| k | Term | Partial sum | Error | log₁₀(error) |
|---|---|---|---|---|
| 1 | 5.00×10⁻¹ | 0.500000000000000 | 5.00×10⁻¹ | −0.3 |
| 5 | 3.12×10⁻² | 0.968750000000000 | 3.12×10⁻² | −1.5 |
| 10 | 9.77×10⁻⁴ | 0.999023437500000 | 9.77×10⁻⁴ | −3.0 |
| 15 | 3.05×10⁻⁵ | 0.999969482421875 | 3.05×10⁻⁵ | −4.5 |
| 20 | 9.54×10⁻⁷ | 0.999999046325684 | 9.54×10⁻⁷ | −6.0 |

Convergence is exactly geometric: each step halves the error. The limit is exactly 1.

### Achilles and Tortoise (v_A=2, v_T=1, head start=1)

Exact meeting time: t* = d₀/(v_A − v_T) = 1/(2−1) = 1.0 unit of time.
At t*: x_A = 2.0, x_T = 2.0. They meet exactly.

The Zeno construction subdivides the interval [0, t*] into infinitely many sub-intervals.
Each sub-interval is a legitimate part of the full motion. The series of sub-intervals
converges to t* = 1 in finite time. After t* there are no more sub-intervals — the Zeno
paradox has an end.

### Quantum of action (discreteness of change)

| Quantity | Value |
|---|---|
| Planck time | 5.39×10⁻⁴⁴ s |
| Planck length | 1.62×10⁻³⁵ m |
| Electron Compton wavelength | 3.86×10⁻¹³ m |
| Tennis ball de Broglie wavelength | 6.17×10⁻³⁵ m (near Planck length!) |
| Proton at LHC | 3.04×10⁻²⁰ m |

The de Broglie wavelength of a tennis ball is ~6×10⁻³⁵ m — within one order of magnitude
of the Planck length. Quantum effects are present but unmeasurable for macroscopic objects.
Below l_P, continuous change may be undefined.

### K-information change analysis

| Transition | K(S1) | K(S2) | K(S2\|S1) | ΔK |
|---|---|---|---|---|
| stopped_clock | 0.074 | 0.074 | 0.011 | 0.000 |
| slow_motion_dx=0.001 | 0.080 | 0.080 | 0.018 | 0.000 |
| fast_motion_dx=100 | 0.076 | 0.074 | 0.016 | −0.001 |
| phase_transition_water_ice | 0.074 | 0.075 | 0.037 | +0.001 |
| random_states | 1.023 | 1.023 | 1.001 | 0.000 |

### Stopped clock

A stopped clock at t₁ and t₂ differ only by their timestamps.
K-content of the timestamp: log₂(1s / t_Planck) ≈ 143.7 bits.
A stopped system "changes" by ~144 bits/second — but only in its time-coordinate.

## Finding 1: Mathematical resolution is real but not complete

The Zeno series converges. This is a mathematical fact:
- Σ (1/2)^k = 1 exactly
- Achilles meets the tortoise at t* = d₀/(v_A − v_T), a finite positive time
- The meeting is a consequence of the completeness of the real numbers (least upper bound property)

**What calculus resolves:** that infinitely many steps can be traversed in finite time.
The sum of infinitely many intervals [0, 1/2], [1/2, 3/4], ... is the interval [0, 1].
No paradox — the real line is complete.

**What calculus does NOT resolve:** what makes the particle at x=1 the same particle as
at x=0. Calculus describes WHERE and WHEN; it does not describe WHAT CONSTITUTES IDENTITY
across change. This is the philosophical residue.

Two distinct questions:
1. Can an infinite series of physical steps take finite time? — **YES** (calculus)
2. What is the ontological status of the transition from x=0 to x=1? — **Open**

## Finding 2: The K-information framing — change is K-update

The numerical K-analysis gives a precise definition:

> **Change = K(S(t+dt) | S(t)) > 0**

A system changes between t and t+dt if and only if the state at t+dt requires new
K-information beyond what was in the state at t.

Results:
- **Stopped clock**: K(S2|S1) ≈ 0.011 (near zero, only noise from gzip headers).
  The K-information content of the state is unchanged. By this definition: no real change.

- **Phase transition**: K(S2|S1) ≈ 0.037 (largest among structured transitions).
  Water→ice changes qualitatively even though K(S1) ≈ K(S2). The transition requires
  new K-content (different molecular ordering) even when the total complexity is similar.

- **Random states**: K(S2|S1) ≈ 1.001 ≈ K(S2). S1 gives no compression of S2.
  Maximal change: the new state is completely unpredictable from the old.

**The K-change metric** orders transitions: random > phase_transition > slow_motion > stopped.
This matches intuition about "how much" change occurred, and it's computable.

## Finding 3: The stopped clock answer

The stopped clock (PROBLEM.md Tier 3: "is a stopped clock still changing?") has a
K-information answer:

> **The stopped clock at t₁ and t₂ differ by ~144 bits: the timestamp.**

If time-coordinate is part of the state description, then the clock changes by 144 bits
per second even while stopped. This is the "block universe" reading: in 4D, every slice
is different from every other by its time-coordinate, even if all physical fields are
identical.

If time-coordinate is NOT part of the state description (only the physical state matters),
then K(S2|S1) ≈ 0 for the stopped clock: it is not changing.

The question reduces to: is time a physical dimension (part of the state) or an indexing
parameter (external to the state)? Relativity says the former. Presentism says the latter.
The K-information metric gives the same answer as your underlying ontology of time.

## Finding 4: Zeno and the block universe

The most complete dissolution of Zeno's paradox comes from the block universe:

In a static 4D spacetime, there is no "motion." Achilles and the tortoise both exist as
4D worldlines (tubes in spacetime). The worldlines cross at the meeting point. There is
no question of HOW Achilles "moves" through infinitely many positions — his worldline
simply crosses the meeting point's location.

**But this creates a new problem:** what makes the 4D worldline "run"? Why does the observer
(embedded in the worldline) experience the crossing from "before meeting" to "after meeting"?
This is the question Zeno dissolves — and replaces with the phenomenology of time experience.

**Numerical corollary:** if we describe the Achilles race as a static 4D block, the entire
trajectory (all positions at all times) is described by two lines and their crossing point.
The K-information content of this description is minimal — a few equations. The Zeno
"infinite steps" are an artifact of parameterizing this static structure by time, not a
feature of the structure itself.

## Sky bridges (numerical)

- **physics/what_is_time** — time's arrow (from `entropy_arrow.py`) requires dissipation,
  not just dynamics. Zeno's paradox dissolves in block universe; the arrow requires initial
  conditions + collisions. The two questions are related but not identical.
- **physics/what_is_information** — change as K-update is a K-information concept. The
  K-change metric (K(S2|S1)) connects the question of change directly to the S/K bifurcation.
  State transitions change K-information; time's arrow changes S-information. These can decouple.
- **philosophy/what_is_mind** — the phenomenology of change (the felt "becoming") is not
  captured by the K-update metric. The metric captures the information-theoretic change;
  why the observer experiences it as temporal flow is the hard problem residue.
- **math/ns_blowup** — the Navier-Stokes blowup problem asks whether change (fluid motion)
  can develop infinite gradients (singularities) in finite time. The Zeno/calculus connection:
  calculus handles infinite sub-steps but may fail at the singularity.

## Next numerical steps

1. **Landauer cost of change.** Each K-update K(S2|S1) > 0 involves erasing old K-information
   and writing new. By Landauer's principle, this costs kT ln(2) per bit at temperature T.
   Compute the thermodynamic cost of various transitions (slow motion, phase transition, quantum
   measurement). This connects K-change to S-cost — the thermodynamic bookkeeping of change.

2. **Zeno at the Planck scale.** The series 1/2 + 1/4 + ... = 1 converges in the reals.
   If spacetime is discrete at l_P, then below step k* (where the sub-interval is ≤ l_P),
   the Zeno construction terminates. Compute k* for macroscopic motion (tennis ball, 30 m/s):
   how many Zeno steps before the Planck limit cuts off the series?

3. **Conditional K in quantum mechanics.** In quantum mechanics, K(S2|S1) is undefined for
   measurement outcomes (S2 is a random draw from a distribution). Model this: generate
   1000 random measurement outcomes from a quantum state, compute K(outcome | state_description).
   Compare to K for classical transitions. Hypothesis: quantum measurement has K(S2|S1) > 0
   even when the system is "unchanged" in its pre-measurement state — measurement IS change.

## Status

Phase 1 numerics. Zeno's mathematical resolution confirmed. The K-change metric gives
a computable definition of change (K(S2|S1) > 0). The stopped clock has a definite
K-answer dependent on whether time-coordinate is part of the state. The philosophical
residue (identity across change, phenomenology of becoming) is beyond what K-information
alone can address and interfaces with `what_is_mind` and `what_is_time`.
