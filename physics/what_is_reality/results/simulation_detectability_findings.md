# Simulation Detectability Findings

**Script:** `numerics/simulation_detectability.py`
**Date:** 2026-04-09
**Builds on:** `lv_bounds.py` (GRB 090510 bound), `simulation_cost.py` (Planck-resolution cost)

---

## Setup

Two established results drive this analysis:

1. **LIV bound** (lv_bounds.py): Linear Lorentz invariance violation ruled out by GRB 090510
   (Abdo et al. 2009). Requires E_P_sim ≥ 7.1659 × E_P, i.e., cell size ≤ 0.1395 × l_P.

2. **Simulation cost** (simulation_cost.py): Planck-resolution simulation of the observable
   universe requires 10^185 bits of state — exceeding our holographic budget of 10^124 bits
   by a factor of 10^61.

The question here: what are the implications for an *external* simulator, and what detectability
signatures would a nearly-undetected simulator produce?

---

## 1. External Simulator Memory Requirements

If the simulator is external to our universe, it is not subject to our holographic bound.
Its minimum required memory is set by the state it must track:

| Quantity | Value |
|---|---|
| Planck-resolution state (our universe) | 10^185 bits |
| Our holographic budget | 10^124 bits |
| Excess | 10^61 |

**The external simulator must hold at least 10^185 bits — equal to 10^61 times the entire
information capacity of the universe it is simulating.**

In concrete terms: 10^185 bits = 10^61 "observable-universe-equivalents" of memory. The
simulator's memory bank would require 10^61 universes' worth of storage just to hold one
instant of our universe at Planck resolution.

This is not a fine-tuning problem — it is a structural constraint. No matter how advanced
the simulator, the minimum state size is set by the number of Planck cells in our observable
universe, which is fixed by geometry.

**Corollary:** an external simulator that is not subject to *any* holographic bound can, in
principle, have this memory. The holographic bound is a property of our spacetime, not a
universal law. This means the simulation hypothesis is not *ruled out* by information
theory — but it does require the simulator to live in a very different kind of spacetime
from ours.

---

## 2. LIV Time Delay Signatures

**Formula (linear LIV, n=1):**

```
Δt = (L/c) × ΔE / E_P_sim
```

where L is luminosity distance, ΔE the photon energy spread, and E_P_sim the effective
Planck energy of the simulator's lattice.

### 2a. GRB 090510 (Abdo et al. 2009)

| Parameter | Value |
|---|---|
| Luminosity distance L | 7.3 × 10^26 m |
| Energy spread ΔE | 31 GeV |
| Observed upper bound Δt | 0.86 s |
| Required E_P_sim | ≥ 7.1659 × E_P |

At E_P_sim = E_P_min = 7.1659 × E_P, the predicted delay is **Δt = 0.863 s** — just
at the FERMI detection threshold. The simulator using exactly the minimum allowed
E_P_sim is *marginally consistent* with observation.

### 2b. Cell-size exclusion table (GRB 090510)

| Cell size | E_P_sim / E_P | Δt (s) | FERMI status |
|---|---|---|---|
| 0.05 × l_P | 20.00 | 0.31 | allowed |
| 0.10 × l_P | 10.00 | 0.62 | allowed |
| 0.14 × l_P | 7.16 | 0.87 | EXCLUDED |
| 0.50 × l_P | 2.00 | 3.09 | EXCLUDED |
| **1.00 × l_P** | **1.00** | **6.18** | **EXCLUDED** |
| 1.01 × l_P | 0.99 | 6.24 | EXCLUDED |
| 7.20 × l_P | 0.14 | 44.51 | EXCLUDED |

**Key result: Even Planck-resolution cells (1 × l_P) are excluded.** The detected
delay would be 6.18 s against a 0.86 s limit. Cells at any multiple of l_P or larger
are ruled out. The simulator's cell must be *sub-Planckian*: ≤ 0.1395 × l_P.

This means the simulation hypothesis, if true, requires the simulator to work at a
resolution finer than the Planck scale of our universe — not just at it.

**The FERMI exclusion boundary:**
- Cells ≥ 0.1395 × l_P = 2.255 × 10^-36 m → EXCLUDED
- Equivalently: E_P_sim < 7.1659 × E_P → EXCLUDED

### 2c. Future γ-ray telescope (ΔE = 100 GeV, L = 10 Gpc, Δt_threshold = 0.01 s)

| Parameter | Value |
|---|---|
| L | 3.086 × 10^32 m (10 Gpc) |
| ΔE | 100 GeV |
| Detection threshold Δt | 0.01 s |
| Sensitivity bound E_P_sim | ≥ 8.43 × 10^8 × E_P |
| Maximum allowed cell | 1.19 × 10^-9 × l_P |

A future telescope would probe E_P_sim down to ~8 × 10^8 × E_P, excluding cells
larger than ~10^-9 × l_P. If such a telescope returns a null result, the simulator's
cell must be ≤ 10^-9 × l_P — i.e., at least a billion times finer than our Planck
length.

**At 1.01 × l_P cells, the future telescope would measure Δt ≈ 8.5 × 10^6 s
(~100 days) — spectacularly detectable.** Any simulator using cells within 10 orders
of magnitude of l_P would be immediately visible to a 10 Gpc, 100 GeV instrument.

---

## 3. The Sharpened Constraint

Combining both results:

| Constraint | Requirement | Source |
|---|---|---|
| LIV undetected (FERMI) | Cell ≤ 0.14 × l_P | GRB 090510 |
| Holographic budget | State ≤ 10^124 bits | Bekenstein |
| Planck-resolution state | 10^185 bits needed | simulation_cost.py |

If cell = 0.14 × l_P:
- Cells per dimension: r_obs / (0.14 × l_P) = 7.14 × r_obs / l_P
- State bits ∝ (7.14)^3 × 10^185 ≈ 10^186 bits — essentially unchanged from Planck cost

Whether cells are at l_P or 0.14 × l_P, the memory requirement is ~10^185 bits —
still 10^61 times our holographic budget. The LIV constraint and the memory constraint
reinforce each other: the simulator must both be sub-Planckian (LIV) and external
(memory). Both conditions simultaneously point to a simulator radically beyond our
spacetime.

---

## Implication for K-Informationalism

The simulation detectability result contributes a precise statement to the K-informationalism
thesis:

**If we are in a simulation, it must be:**

1. External to our spacetime (to have 10^61 times our holographic memory)
2. Sub-Planckian in cell size (to evade GRB 090510's LIV constraint)
3. Outside the reach of any experiment within our universe (since its substrate
   is not subject to our physics)

**The simulation hypothesis is therefore:**
- Not ruled out by information theory (an external simulator can have arbitrary memory)
- Not ruled out by LIV experiments (a sub-Planckian simulator leaves no observable trace)
- Empirically inaccessible (the simulator, if external, does not interact with our observables)

This is precisely the structure K-informationalism predicts for the "Level 0" question
(see `reality_multilevel_K.md`): the question of whether K_laws is the output of an
external computation is **metaphysically well-formed but empirically inaccessible**.
The simulation detectability calculation gives that statement a precise numerical meaning:
"inaccessible" means the simulator would have to be external, sub-Planckian, and leave
no LIV signature detectable within our spacetime.

---

## Status

All numbers consistent with `lv_bounds_data.json` and `simulation_cost_data.json`.
The key numerical advances in this file:

- **10^61**: how many "universes-worth" of memory the external simulator needs
- **0.1395 × l_P**: the maximum cell size consistent with GRB 090510
- **6.18 s**: the LIV delay Planck-resolution cells would have produced (vs 0.86 s limit)
- **8.5 × 10^6 s**: delay from 1.01 × l_P cells at a 10 Gpc, 100 GeV future telescope
