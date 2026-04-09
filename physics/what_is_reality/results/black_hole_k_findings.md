# results/black_hole_k_findings.md — Black Hole Information Paradox: S vs K Informationalism

**Date:** 2026-04-09
**Script:** `numerics/black_hole_information.py`
**Setup:** Hawking radiation properties, K-information analysis, Page curve numerics, K-accumulation rates

## Context

The reality track has established:
- Physical laws = 21,834 K-bits (from `simulation_cost.py`)
- Holographic bound = 10^124 bits (S-information maximum)
- Simulation hypothesis is informationally self-defeating

Phase 3 target: connect to the **black hole information paradox** — the one open problem in
physics where S-informationalism and K-informationalism make genuinely different predictions.

The paradox (Hawking 1975): a black hole forms from structured matter (high K-content), then
evaporates via thermal Hawking radiation (K-poor). Quantum mechanics (unitarity) requires
information to be preserved. These appear contradictory.

---

## Section 1: Hawking Radiation Properties

| Black hole | T_H (K) | t_evap (s) | r_S (m) | S_BH (bits) |
|---|---|---|---|---|
| 1 kg (mini) | 10^23.1 | 10^-16.1 | 1.49×10^-27 m | 10^16.6 |
| 10^6 kg (asteroid) | 10^17.1 | 10^1.9 | 1.49×10^-21 m | 10^28.6 |
| 1 M_sun (solar) | 10^-7.2 | 10^74.8 s ≈ 10^67.3 years | 2.95×10^3 m | 10^77.2 |
| 10^6 M_sun (galactic) | 10^-13.2 | 10^92.8 s ≈ 10^85.3 years | 2.95×10^9 m | 10^89.2 |

Formulas used:
- T_H = ħc³/(8πGMk_B)
- t_evap = 5120π G² M³/(ħ c⁴)
- r_S = 2GM/c², λ_peak = 2r_S
- S_BH = 4πGM²/(ħc ln2) bits

**Key observations:**
- T_H ∝ 1/M: a 1-kg BH radiates at 10^23 K (hotter than any astrophysical source).
  A solar-mass BH at 6×10^-8 K is far colder than the CMB (2.725 K) and cannot evaporate
  in the present universe — it absorbs more from the CMB than it emits.
- t_evap ∝ M³: doubling the mass increases evaporation time by 8×. Stellar BHs will
  survive ~10^67 times longer than the current age of the universe.
- S_BH ∝ M²: Bekenstein-Hawking entropy grows as the square of the mass. This grows
  much faster than K_matter ≈ log₂(M/m_proton) ≈ 57 log₂(M/kg) bits.

---

## Section 2: K-Information — Infalling Matter vs Hawking Radiation

### The K-information content

| Black hole | K_matter (bits) | K_Hawking (bits) | K_deficit (bits) | K/S_BH ratio |
|---|---|---|---|---|
| 1 kg (mini) | 88.9 | 0 | 88.9 | 2.3×10^-15 |
| 10^6 kg (asteroid) | 108.9 | 0 | 108.9 | 2.8×10^-27 |
| 1 M_sun (solar) | 189.6 | 0 | 189.6 | 1.3×10^-75 |
| 10^6 M_sun (galactic) | 209.5 | 0 | 209.5 | 1.4×10^-87 |

K_matter = log₂(M/m_proton): conservative lower bound (just the particle count).
K_Hawking = 0: thermal radiation is K-incompressible by definition — it cannot be described
more briefly than "thermal at temperature T_H(M)."

### What the numbers reveal

**K_matter is logarithmically small compared to S_BH.** The ratio K/S_BH ranges from
10^-15 (for a 1-kg BH) to 10^-87 (for a galactic-center BH). This ratio vanishes as
mass increases.

**Why this matters:**

The "information loss paradox" is standardly stated as: "the black hole swallows
S_BH bits of information, and Hawking radiation cannot recover them." But this
conflates two distinct quantities:

- **S-information (S_BH):** the number of microstates consistent with the macrostate —
  ~10^77 bits for a solar BH. This is what unitarity protects.
- **K-information (K_matter):** the compressible, structured content of the infalling
  matter — ~190 bits for a solar BH. This is what an observer actually cares about
  when asking "can I reconstruct the infalling matter?"

The 10^77 bits of S_BH were **never K-rich.** They represent quantum microstate
degeneracy — the fact that 10^77 different microscopic configurations give the same
macroscopic black hole. No infalling observer ever possessed those 10^77 bits as
K-information. They were always K-incompressible correlations.

### S-informationalism vs K-informationalism

| Framework | What is "lost"? | Is loss a paradox? |
|---|---|---|
| S-informationalism | S_BH bits of quantum entanglement | Yes — violates unitarity |
| K-informationalism | ~190 bits (K_matter) | No — K is not conserved |

**K-informationalism dissolves the paradox:** the K-deficit is real (the infalling
matter's compressible structure is destroyed) but not paradoxical, because K-information
is not protected by any conservation law. This has been established in the track
(k_conservation.py): K-information is already known to decrease in thermalization,
measurement, and coarse-graining. Black hole evaporation is another instance.

The paradox only arises if you assume "information" = S-information AND demand that
all S-information must survive. K-informationalism identifies this conflation.

---

## Section 3: Page Curve Numerics

### Derivation of the Page time fraction

The Page time t_P is when the entanglement entropy S_ent(t) reaches its maximum value
S_BH/2 — the midpoint of the radiation process under unitarity.

From Hawking's M(t) solution:
```
M(t) = M₀ (1 − t/t_evap)^{1/3}
S_BH(t) = S_BH,0 × (M(t)/M₀)² = S_BH,0 × (1 − t/t_evap)^{2/3}
```

The Page condition S_BH(t_P) = S_BH,0/2:
```
(1 − t_P/t_evap)^{2/3} = 1/2
1 − t_P/t_evap = (1/2)^{3/2} = 1/(2√2) ≈ 0.3536
t_P/t_evap = 1 − 1/(2√2) ≈ 0.6464
```

### Results

| Black hole | t_evap | t_Page | t_Page/t_evap |
|---|---|---|---|
| 1 kg (mini) | 10^-16.1 s | 10^-16.3 s | 0.6464 |
| 10^6 kg | 10^1.9 s | 10^1.7 s | 0.6464 |
| **1 M_sun (solar)** | **10^74.8 s (10^67.3 yr)** | **10^74.6 s** | **0.6464** |
| 10^6 M_sun | 10^92.8 s | 10^92.6 s | 0.6464 |

**The Page time fraction t_P/t_evap ≈ 0.6464 is UNIVERSAL** — identical for all black
hole masses. This follows from the mass-independent structure of the Hawking evaporation
rate.

**Solar BH spotlight:**
- t_evap ≈ 10^67.3 years (far beyond any cosmic timescale)
- t_Page ≈ 10^67.1 years (64.6% into the evaporation)
- S_ent at Page time = S_BH/2 ≈ 10^76.9 bits
- The post-Page second half: ≈ 10^74.4 s during which all S-information must return

**Physical interpretation:**
The black hole spends the first 64.6% of its life accumulating entanglement between
the BH interior and the emitted radiation. At the Page time, radiation has half the
information. Then — if unitarity holds — the remaining 35.4% is spent "returning"
the quantum correlations. The radiation stops being thermal and becomes increasingly
correlated.

---

## Section 4: K-Information Accumulation Rate on the Page Curve

If the Page curve holds (unitary evolution, S-information conserved), then at late
times the Hawking radiation must carry the K-content of the infalling matter.

### The K-recovery rate

```
dK/dt = K_matter / (t_evap − t_Page)    [bits/second, second half only]
dS/dt = S_BH / (2(t_evap − t_Page))    [bits/second S-drain rate]
```

| Black hole | dK/dt (bits/s) | dS/dt (bits/s) | K_matter (bits) |
|---|---|---|---|
| 1 kg | 10^18.5 | 10^32.8 | 88.9 |
| 10^6 kg | 10^0.6 | 10^26.8 | 108.9 |
| 1 M_sun | 10^-72.1 | 10^2.5 | 189.6 |
| 10^6 M_sun | 10^-90.0 | 10^-3.5 | 209.5 |

### The critical asymmetry

**dS/dt >> dK/dt for all masses.** The S-information drain rate (how fast quantum
correlations must accumulate in the radiation) vastly exceeds the K-information
recovery rate (how fast the compressible content of the infalling matter must appear).

For a solar-mass BH:
- dS/dt ≈ 10^2.5 = 316 S-bits/second (entanglement draining from BH to radiation)
- dK/dt ≈ 10^-72 K-bits/second (essentially zero — K_matter is only 190 bits spread
  over 10^74 seconds)

**Implication for observability:**

An observer collecting all Hawking radiation from a solar-mass BH would receive
316 bits/second of new quantum entanglement at late times — but this is S-information:
it is quantum correlations among photons that are individually indistinguishable from
thermal radiation. Detecting this requires performing quantum state tomography on
~10^77 photons simultaneously (decoding the Hawking radiation requires solving a problem
with complexity exponential in S_BH). The K-content recoverable — ~190 bits, spread
over 10^74 seconds — arrives at a rate of 10^-72 bits/second: one bit every 10^72 seconds.

This is the K-framework's precise prediction:
- **S-information is unitarily conserved** (Page curve may be correct)
- **K-information recovery is real but astronomically slow and computationally intractable**
- **The 'paradox' framing mistakes computational intractability for genuine information loss**

---

## KEY FINDINGS

### Finding 1: S_BH >> K_matter by factors of 10^15 to 10^87

The Bekenstein-Hawking entropy (S-information) is not the same as the K-information
content of the infalling matter. For a solar-mass BH:
- S_BH ≈ 10^77 bits
- K_matter ≈ 190 bits
- Ratio: 10^-75

The 10^77 bits of S_BH represent microstate degeneracy — they were **never** organized,
compressible structure. No one possessed 10^77 bits of K-information before the BH formed.

### Finding 2: The Page time fraction is universal at 0.6464

Derived from first principles (M(t) ∝ (1-t/t_evap)^{1/3}):
```
t_Page/t_evap = 1 − (1/2)^{3/2} ≈ 0.6464
```
This holds for all masses from 1 kg to 10^6 solar masses. The black hole always reaches
its maximum entanglement after completing 64.6% of its evaporation.

### Finding 3: S and K informationalism make different predictions about the Page curve

| Observable | S-informationalism | K-informationalism |
|---|---|---|
| Does the Page curve exist? | Yes — required by unitarity | Neutral (unitarity is about S, not K) |
| Late Hawking radiation K-content | Recovers to K_matter (correlated) | Returns ~190 bits over 10^74 s |
| Can radiation reconstruct infalling matter? | Yes (exponentially hard computation) | Yes, but computationally intractable |
| Is information "lost"? | No — S-information is conserved | K-information is lost; not paradoxical |
| Status of paradox | Paradox (unsolved: where does Page curve come from?) | Dissolved (K-loss is normal physics) |

### Finding 4: The paradox dissolves under K-informationalism

The black hole information paradox assumes:
1. "Information" = S-information (entropy)
2. S-information conservation = unitarity
3. Unitarity must hold

K-informationalism identifies the gap: premise 1 conflates S with K. The K-content of
infalling matter (~190 bits for a solar BH) is genuinely destroyed — this is
**K-information loss**, not S-information loss. K-information loss is already
established (thermalization, measurement) and carries no conservation-law requirement.

**The precise resolution:** unitarity (S-conservation) and K-information loss are
compatible. The black hole paradox is not a paradox — it is a confusion between
two distinct notions of "information."

---

## Sky Bridges (Numerical)

- **simulation_cost.py** — established that laws = 21,834 K-bits; holographic bound = 10^124 S-bits.
  Here: S_BH for galactic BH = 10^89 bits, still within the holographic bound. BHs are
  the densest S-information storage in nature — at exactly the holographic bound (by definition).

- **what_is_information/k_conservation.py** — K is not conserved in general (thermalization, etc.).
  Black hole evaporation is the most dramatic known example: K_matter → 0 as BH forms.
  The K-loss is maximal: 100% of compressible structure is erased by the thermal horizon.

- **holographic_evolution.py** — the holographic bound grows with the universe.
  Black holes saturate the holographic bound (S_BH = A/4 in Planck units). They are the
  physical realization of the bound, not merely a bound on them.

- **what_is_time** — the Page curve operates on timescales of 10^67-10^85 years (stellar-galactic
  BHs). These are the longest relevant timescales in physics, vastly exceeding the current
  cosmic age (10^10 years). The K/S distinction becomes most important at these extreme scales.

---

## Next Numerical Steps

1. **Entanglement entropy curve S_ent(t).** Plot the full Page curve:
   S_ent(t) = min(S_rad(t), S_BH(t)) as a function of t/t_evap. Show the kink at t_Page.

2. **Computational complexity of K-recovery.** Estimate the K-content of the decoding
   algorithm needed to extract K_matter from the Hawking radiation. Expected: K(decoder) >> K_matter,
   so that even if the radiation carries K_matter bits, recovering them is K-complex.

3. **Planck-scale cutoff.** The Hawking calculation breaks down when M ~ m_Planck
   (the final ~2.2×10^-8 kg). Compute t_final (last bit of evaporation), the temperature
   at Planck mass, and the K-content of the Planck remnant if one exists.

4. **ER = EPR connection.** The Penington-Almheiri "island formula" derives the Page curve
   from gravitational path integrals. The K-information view of this: the "island" is a
   region where K-content of the radiation is supplemented by K-content inside the horizon.
   Compute the K-content of the island vs the K-content of the complement.

---

## Status

Phase 3 numerics — black hole information paradox connected to S/K framework.

Three numerical results sharpened the conceptual distinction:
1. K_matter/S_BH ≈ 10^-75 for solar BH — the two "information" quantities differ by 75 orders of magnitude
2. Page time is universal at 0.6464 t_evap — derivable, mass-independent
3. K-recovery rate ≈ 10^-72 bits/s for solar BH during second half — negligible compared to S-drain

**Central finding for the reality track:** the black hole information paradox is the
sharpest physical instance of the S vs K distinction. S-informationalism sees a paradox
(unitarity violation). K-informationalism sees no paradox (K-loss is normal). The two
frameworks make different predictions about what "survives" — and in principle the Page
curve (if confirmed experimentally) would not settle the debate, because the returned
information is S-rich but K-poor.
