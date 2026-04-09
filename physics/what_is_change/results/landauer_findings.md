# Landauer Change — Findings
**Script:** `numerics/landauer_change.py`  
**Data:** `results/landauer_data.json`  
**Date:** 2026-04-09

---

## Setup

Landauer's principle: erasing one bit of information at temperature T costs at least
k_B T ln(2) joules. If physical change = K(S2|S1)-bit update, then every real change
has a thermodynamic floor. We compute this floor for five processes across six orders
of magnitude in physical scale.

Constants used: k_B = 1.380649e-23 J/K, G = 6.674e-11, ħ = 1.054571817e-34 J·s,
c = 2.998e8 m/s, m_proton = 1.673e-27 kg.  
Temperatures: T_body = 310 K, T_room = 298 K, T_cmb = 2.725 K.

---

## Results by process

### 1. Neuron firing (biological, 310 K)
- K-change: **1 bit** (threshold crossed: fire / no fire)
- Landauer floor: **2.97e-21 J**
- Measured ATP cost per action potential: ~2e-12 J
- Slack factor: **6.74e8 x** above Landauer minimum

The biological implementation is ~700 million times less efficient than the
information-theoretic floor. The slack arises from ion-channel specificity,
reversal-potential gradients, and Na+/K+-ATPase reset costs — none of which
encode the 1 bit; all of which dissipate heat.

### 2. DNA base-pair mutation (molecular, 310 K)
- K-change: **2 bits** (log2(4) bases; one nucleotide substitution)
- Landauer floor: **5.93e-21 J**
- Polymerase cost per bp: ~2.14e-19 J (~50 k_B T)
- Slack factor: **36 x** above Landauer minimum

DNA replication is far closer to the Landauer floor than neurons. The ~36x overhead
is proofreading: the polymerase pays ~25x extra to enforce fidelity (error rate ~10^-9
per bp). This is a physical argument for why molecular computation is more thermodynamically
efficient than neural computation: the state space is smaller and the system operates
closer to the information floor.

### 3. Photon absorption at 500 nm (quantum, 298 K)
- K-change: **1 bit** (two-level atom: ground vs. excited state)
- Photon energy: **2.480 eV** = 3.97e-19 J
- Landauer floor: **0.0178 eV** = 2.85e-21 J at 298 K
- Slack factor: **139 x**

Only 0.7% of the photon's energy encodes the K-state transition. The remaining 99.3%
is dissipated as heat (vibrational modes, internal conversion). This makes explicit the
S/K bifurcation from `what_is_information`: the photon carries S-entropy (2.48 eV of
thermal capacity) and K-information (1 bit of which-state). These are not the same
quantity — the K-change has a floor 139x below the actual energy exchange.

### 4. Macroscopic object moving 1 mm (classical, 298 K)
- Thermal de Broglie wavelength for 1g: **1.30e-22 m**
- K-bits at thermal precision: **62.7 bits** → Landauer cost: 1.79e-19 J
- K-bits at 1-µm measurement precision: **10.0 bits** → Landauer cost: 2.84e-20 J

The K-bits of macroscopic motion depend critically on what resolution is used to
specify the new position. At thermal (quantum-limited) precision, a 1mm displacement
encodes 63 bits. At realistic lab measurement (1 µm), it encodes 10 bits. This shows
that K-change is observer-relative in the macroscopic regime: the Landauer cost tracks
the information actually written, not the physical energy of motion (which is many
orders of magnitude larger and mostly conserved, not dissipated).

### 5. Black hole absorbs one proton (cosmological, T_Hawking)

**Setup:** 10 solar mass Schwarzschild black hole; Hawking temperature T_H = 6.17e-9 K.

**Bekenstein-Hawking entropy before:** S = 4πk_B G M² / (ħc) = **1.514e79 bits**

**Delta S (analytic):** ΔS = 4πG(2Mm_p + m_p²) / (ħc ln2) = **2.547e21 bits**

*(Note: naive float subtraction S(M+m_p) - S(M) underflows to zero because M/m_p ~ 10^58
exceeds float64 precision. The algebraic identity (M+m)^2 - M^2 = 2Mm + m^2 was used.)*

**Landauer cost at T_H:** E_L = 2.547e21 bits × k_B × 6.17e-9 K × ln2 = **1.504e-10 J**

**Proton rest-mass energy:** mc² = **1.504e-10 J**

**Landauer / mc² = 1.000** (to four significant figures)

This is not a coincidence. Setting E_L = ΔS_bits × k_B T_H ln2 and substituting the
Bekenstein entropy and Hawking temperature expressions:

```
E_L = [8πGMm / (ħc)] × [ħc³ / (8πGM)] = m c²
```

The factors of M cancel. The Landauer cost at the Hawking temperature of the black hole
entropy change from absorbing a particle equals exactly the rest-mass energy of that
particle. This is a thermodynamic identity: the K-information update to the black hole's
state (measured in Bekenstein bits) costs exactly the rest mass of what fell in — when
evaluated at the horizon's own temperature.

---

## Cross-scale comparison

| Process | Scale | K-bits | E_Landauer (J) | E_actual (J) | Slack |
|---|---|---|---|---|---|
| neuron firing | biological | 1 | 2.97e-21 | 2.00e-12 | 6.7e8 x |
| photon absorption | quantum | 1 | 2.85e-21 | 3.97e-19 | 139 x |
| DNA mutation | molecular | 2 | 5.93e-21 | 2.14e-19 | 36 x |
| macro 1mm (1 µm meas.) | macroscopic | 10 | 2.84e-20 | N/A | N/A |
| BH + proton | cosmological | 2.55e21 | 1.50e-10 | 1.50e-10 | 1.00 x |

The slack factor decreases from biological → molecular → quantum → cosmological.
The black hole is at the Landauer limit: it absorbs exactly the right amount of
energy (mc²) for the K-information update it performs. All other physical processes
overpay — the excess is S-entropy dissipated as heat.

---

## Key findings

### Finding 1: Change has a thermodynamic floor

Every K-information update K(S2|S1) dissipates at least k_B T ln(2) × K(S2|S1) joules.
This is not a design constraint — it is a fundamental bound (Landauer 1961, verified
experimentally by Bérut et al. 2012). Real change is thermodynamically distinguishable
from no change (stopped clock): the stopped clock has K(S2|S1) ≈ 0 and zero Landauer
cost; real change has K(S2|S1) > 0 and non-zero Landauer cost.

### Finding 2: K-bits do not scale with physical size

The physical size of a system does not determine its K-change:
- A proton falling into a stellar black hole encodes 2.55e21 bits of K-change
- A neuron firing encodes 1 bit

The black hole is ~10^31 kg; the neuron is ~10^-11 kg. The 10^42 mass ratio does not
produce a proportional K-ratio. K-change tracks the information content of the
transition, not the mass or energy of the objects involved.

### Finding 3: The BH Landauer identity (exact)

At the Hawking temperature, the Landauer cost of the Bekenstein entropy increase from
absorbing a particle equals mc² for that particle. This connects:
- K-information (Bekenstein bits)
- Thermodynamics (Landauer energy)
- Relativity (rest-mass energy)

The chain is: ΔS_bits × k_B × T_H × ln2 = mc². This is an exact identity, not
a numerical coincidence. It means the black hole horizon encodes arriving mass
as K-information at precisely the thermodynamic rate set by its own temperature.

### Finding 4: Interventionist causation is the preferred theory (R1)

The compression view of change (K(S2|S1) > 0 iff change occurred) is best supported
by interventionist causation (Woodward 2003). The argument from Landauer:

- An intervention IS a bit-erasure event: it replaces one state with another,
  erasing the old state's bits.
- Erasure costs k_B T ln(2) per bit (Landauer bound).
- Therefore: every genuine causal intervention has a thermodynamic signature.
- Regularity theories cannot distinguish a K-change from a K-zero change (stopped clock
  has regular succession of identical states, zero Landauer cost).
- Counterfactual theories come close (would the state have changed if no intervention?)
  but the Landauer formulation gives a stronger operationalisation: the intervention
  is identified by the energy it dissipates, not by a modal claim.

Interventionism + Landauer = thermodynamic operationalisation of causation.

### Finding 5: Phenomenal flow (R3)

Physical change = K-information update at Landauer floor.  
Phenomenal flow = the self-model tracking K-changes at neural overhead (~6.7e8 x floor).

Each cognitive "frame" (neural firing) encodes ~1 bit of K-change at a cost of ~2e-12 J.
The subjective rate of temporal flow tracks the frequency of K-changes: high K-change
rate → time feels fast; low rate (sleep, anaesthesia, boredom) → time slows or stops.
The Landauer floor sets the minimum energy cost for phenomenal change to occur at all:
below ~3e-21 J/bit × (bits per cognitive frame), no information-theoretically distinct
experience can exist. The "grain" of experience has a thermodynamic lower bound.

---

## Sky bridge to what_is_time

From `what_is_time/numerics/entropy_arrow.py`: the thermodynamic arrow is S-increase
and K-decrease over time. From this script: physical change = K-update with Landauer
cost. The two results compose: the direction of time (S-arrow) determines the direction
in which K-changes are permitted to accumulate. The cost of accumulating K-changes
(Landauer energy) is the thermodynamic work that drives the universe away from
equilibrium. Change and time are dual aspects of the same dissipative process.

---

## Numerical notes

- Black hole entropy subtraction required the algebraic identity (M+m)^2 - M^2 = 2Mm + m^2
  because M/m_proton ~ 10^58 exceeds float64 range (~10^15). Direct subtraction
  underflowed to zero; the expanded form is numerically exact.
- Thermal de Broglie wavelength used h = 2πħ (full Planck constant), not ħ.
- All Landauer energies are the MINIMUM (reversible Landauer limit); actual dissipation
  is always higher due to irreversibility.
