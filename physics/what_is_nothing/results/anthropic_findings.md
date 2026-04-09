# Anthropic Window for the Cosmological Constant

Script: `numerics/anthropic_window.py`
Data:   `results/anthropic_data.json`

---

## Setup

Cosmological parameters (Planck 2018):

| Quantity | Value |
|---|---|
| H₀ | 67.4 km/s/Mpc = 2.184×10⁻¹⁸ s⁻¹ |
| Ω_m | 0.315 |
| Ω_Λ | 0.685 |
| ρ_crit | 8.533×10⁻²⁷ J/m³ |
| ρ_m today | 2.688×10⁻²⁷ J/m³ |
| ρ_Λ observed | 5.924×10⁻²⁷ J/m³ |
| ρ_Planck | 4.634×10¹¹³ J/m³ |

---

## Task 1: Weinberg Anthropic Window

### Step 1 — Λ-matter equality today

The Friedmann equation gives Λ-matter equality at:

  ρ_m(z) = ρ_m₀ (1+z)³ = ρ_Λ  →  z_eq = (ρ_Λ/ρ_m₀)^(1/3) − 1 ≈ 0.30

Dark energy has only recently come to dominate (z ≈ 0.3). Structure formation
therefore ran mostly in the matter-dominated era — which is why galaxies exist.

### Step 2 — Maximum Λ for galaxy formation

Weinberg (1987): for the first galactic halos to form via gravitational collapse,
dark energy must not dominate before z ≈ 2 (conservative) or z ≈ 5 (first stars).
The maximum allowed density is ρ_m at that redshift:

  ρ_Λ_max(z=2) = ρ_m₀ × (1+2)³ = ρ_m₀ × 27  = 7.257×10⁻²⁶ J/m³
  ρ_Λ_max(z=5) = ρ_m₀ × (1+5)³ = ρ_m₀ × 216 = 5.806×10⁻²⁵ J/m³

### Step 3 — Anthropic window width

  ρ_Λ_max(z=2) / ρ_Λ_obs ≈  12
  ρ_Λ_max(z=5) / ρ_Λ_obs ≈  98

The Weinberg window spans roughly **12–100× the observed value**.
The observed Λ sits comfortably inside the window — it is about 12× below
the most conservative upper bound, and ~100× below the aggressive bound.

### Step 4 — Anthropic probability

Assuming a uniform prior on Λ ∈ [0, ρ_Λ_max]:

  P(Λ ≤ Λ_obs | Λ ≤ Λ_max, z=2) = Λ_obs / Λ_max ≈ 1/12 ≈ 0.08
  P(Λ ≤ Λ_obs | Λ ≤ Λ_max, z=5) = Λ_obs / Λ_max ≈ 1/98 ≈ 0.01

These are probabilities of order 1–10%. The observed Λ is not statistically
extreme within the window. The selection effect alone (the Weinberg argument)
is consistent with what we see — no additional fine-tuning is required *within*
the window.

### Step 5 — What the window actually explains

The CC problem in full is:

  ρ_Planck / ρ_Λ_obs ≈ 10^140

The Weinberg window eliminates ~1 order of magnitude of this ratio (factor ~12).
The remaining puzzle is:

  ρ_Planck / ρ_Λ_max ≈ 10^139

The anthropic selection argument does **not** explain why Λ is so small compared
to the Planck scale. It only explains why, *given* that Λ is small, we find
ourselves at a value near (but below) the galaxy-formation threshold.

---

## Task 2: Casimir Energy Density in a Planck-Size Box

The Casimir energy for a massless scalar field in a cube of side L is:

  E_Casimir = −A · ħc / L,   A ≈ 0.09636  (Lukosz 1971; Ambjorn & Wolfram 1983)

For the EM field (2 polarisations), A doubles.

At L = l_P = 1.616×10⁻³⁵ m:

| Quantity | Value |
|---|---|
| E_Casimir (scalar) | −1.89×10⁸ J |
| ρ_Casimir (scalar) = \|E\|/l_P³ | 4.47×10¹¹² J/m³ |
| ρ_Casimir / ρ_Planck | ≈ 0.096  (≈ A/π ≈ same order) |
| ρ_Casimir / ρ_Λ_obs | ≈ 10^139 |

### Physical meaning

The Casimir calculation at Planck scale is a concrete realisation of the
vacuum-energy problem:

1. **ρ_Casimir ≈ ρ_Planck** (within a factor of ~10). This is expected: at the
   smallest conceivable length scale the vacuum fluctuation energy density is
   naturally of order the Planck density. Quantum field theory gives no
   mechanism to suppress it.

2. **ρ_Casimir / ρ_Λ_obs ≈ 10^139**. Every Planck-size cell of space carries a
   Casimir-like vacuum energy ~10^139 times larger than the observed dark energy.
   Somehow — by a cancellation we do not understand — the contributions from all
   these cells sum to the tiny observed value.

3. The Casimir result is **negative** (attractive between plates), while the
   observed Λ is positive. Sign as well as magnitude are unexplained.

---

## Key Findings

| Finding | Value |
|---|---|
| z_eq (Λ-matter equality today) | 0.30 |
| Anthropic window (z=2 threshold) | Λ_obs × [0, 12] |
| Anthropic window (z=5 threshold) | Λ_obs × [0, 98] |
| P(Λ_obs in window, z=2, uniform prior) | ~8% |
| CC problem (ρ_Planck/ρ_Λ) | ~10^140 |
| Orders explained by Weinberg selection | ~1 |
| Residual unexplained fine-tuning | ~10^139 |
| ρ_Casimir at l_P | 4.47×10¹¹² J/m³ ≈ 0.10 ρ_Planck |
| ρ_Casimir / ρ_Λ_obs | ~10^139 |

### Bottom line

The Weinberg anthropic argument is internally consistent: the observed Λ is
within the galaxy-formation window, and its position within that window (roughly
the lower ~8–10%) is not improbable under a uniform prior. **However, the
anthropic window explains only ~1 decade of the 140-decade gap between the
Planck density and the observed dark energy**. The vast bulk of the cosmological
constant problem is not explained by observer selection — it requires either a
dynamical mechanism (e.g. vacuum energy cancellation, quintessence, landscape
statistics with a non-uniform prior) or a new physical principle.

The Casimir calculation at the Planck scale makes this concrete: local vacuum
energy density is of order ρ_Planck ≈ 10^113 J/m³, while Λ corresponds to
ρ_Λ ≈ 10⁻²⁷ J/m³. The gap is 140 orders of magnitude. Anthropic selection
accounts for at most the last factor of ~10 in that gap.
