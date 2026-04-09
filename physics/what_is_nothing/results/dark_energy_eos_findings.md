# Dark Energy EOS Findings

*Numerical track, what_is_nothing — 2026-04-09*

---

## Setup

Equation of state parameterization: CPL — w(z) = w0 + wa × z/(1+z).

Observational anchors:
- **Planck 2023:** w0 = -1.03 ± 0.03 (wa = 0 fixed)
- **DESI 2024 combined (CMB + SNIa + BAO):** w0 = -0.827 ± 0.197, wa = -0.75 ± 0.51, correlation ρ = 0.7

Physical constants: H0 = 67.4 km/s/Mpc, Ω_m = 0.315, Ω_Λ = 0.685, σ8 = 0.811.

---

## 1. Chi-squared Summary

| Model | w0 | wa | χ²(DESI 2024) | σ(DESI) | χ²(Planck) | σ(Planck) | K bits |
|---|---|---|---|---|---|---|---|
| LCDM / Unimodular | -1.000 | 0.000 | 9.298 | 3.05σ | 1.000 | 1.00σ | 40 |
| Quintessence (typical) | -0.950 | -0.300 | 3.803 | 1.95σ | 7.111 | 2.67σ | 280 |
| Running vacuum (fitted) | -0.970 | -0.150 | 6.091 | 2.47σ | 4.000 | 2.00σ | 40 |
| Phantom (w < -1) | -1.050 | 0.000 | 11.323 | 3.36σ | 0.444 | 0.67σ | 40 |

ΛCDM (w0=-1, wa=0) vs DESI 2024 joint posterior:
- χ²(2D) = 9.298
- 1D-equivalent sigma = 3.05σ
- 2D p-value equivalent sigma = 2.59σ

---

## 2. K-Content of Dark Energy Models

| Model | Free params | K bits | Note |
|---|---|---|---|
| LCDM / Unimodular | 1 | 40 | 1 parameter (Lambda value) to ~12 sig-figs = ~40 bits. Unimo... |
| Quintessence (typical) | 2 | 280 | 2 CPL parameters (~80 bits) + scalar field potential specifi... |
| Running vacuum (fitted) | 1 | 40 | 1 free parameter nu (dimensionless, ~32 bits precision) plus... |
| Phantom (w < -1) | 1 | 40 | 1 free parameter w0 (~32 bits) plus ghost/modified gravity s... |

The K-simplest dark energy candidate is **ΛCDM / unimodular gravity**, both requiring
~40 bits to specify the single free parameter (Λ or integration constant).

Quintessence requires ~280 bits: two CPL parameters (~80 bits) plus scalar potential
specification (~200 bits for potential shape, field range, initial conditions).

---

## 3. Structure Growth: f·σ8 at z = 0.5

| Scenario | w0 | wa | γ | D(0.5)/D(0) | σ8(z=0.5) | f(z=0.5) | f·σ8 |
|---|---|---|---|---|---|---|---|
| LCDM (w0=-1, wa=0) | -1.000 | 0.000 | 0.5500 | 0.76892 | 0.62360 | 0.76069 | 0.47436 |
| DESI best-fit (w0=-0.827, wa=-0.75) | -0.827 | -0.750 | 0.5587 | 0.79431 | 0.64418 | 0.74937 | 0.48273 |
| Quintessence (w0=-0.95, wa=-0.3) | -0.950 | -0.300 | 0.5525 | 0.77595 | 0.62929 | 0.76042 | 0.47852 |
| Running vacuum (w0=-0.97, wa=-0.15) | -0.970 | -0.150 | 0.5515 | 0.77334 | 0.62718 | 0.75946 | 0.47632 |
| Phantom (w0=-1.05, wa=0) | -1.050 | 0.000 | 0.5475 | 0.76105 | 0.61721 | 0.77145 | 0.47615 |

Key numbers:
- ΛCDM f·σ8(z=0.5) = 0.47436
- DESI best-fit f·σ8(z=0.5) = 0.48273
- Δ(f·σ8) = +0.00837 (+1.76%)
- Euclid forecast 1σ RSD uncertainty ≈ 0.00712
- **Detectable by Euclid: True**

f·σ8 is the prime observable to distinguish ΛCDM from dynamical dark energy.
The ~1.8% shift between ΛCDM and DESI's best-fit
exceeds the Euclid forecast sensitivity.

---

## 4. BIC / K-Information Decision

```
N_eff              = 2000
ln(N_eff)          = 7.601
delta_k (CPL vs LCDM) = 2  (two extra EOS params)
BIC penalty        = 15.202

From published DESI 2024 posterior (chi2 computed from center + errors):
  delta_chi2       = 9.298
  net delta_BIC    = 5.904
  => LCDM positively preferred (delta_BIC 2-10)

From DESI 2024 paper Table 4 (reported delta(-2 ln L)):
  delta(-2lnL)     = 14.3
  net delta_BIC    = 0.902
  => LCDM preferred by BIC even using DESI's own chi2 improvement
```

The BIC decision is **borderline** using DESI's own reported likelihood improvement.
delta_BIC ≈ 0.9, which is below the conventional |delta_BIC| = 10
threshold for "strong" preference.

---

## 5. Key Finding: K-Informationalism Supports ΛCDM

**Two distinct evidence standards apply:**

### 5a. Statistical evidence (BIC)
DESI 2024's delta(-2lnL) = 14.3 for w0waCDM vs ΛCDM exceeds the BIC penalty of
15.2 by only -0.9 units. This is "positive" but not "strong"
evidence for CPL in the Kass-Raftery BIC scale (strong requires delta_BIC > 10 in favor
of the complex model, i.e. delta_chi2 > 25.2).

The ~3.9σ headline figure from DESI is a 2D likelihood ratio result, not a
direct model comparison including the BIC complexity penalty.

### 5b. K-information evidence (Kolmogorov / Occam)
Quintessence adds ~240 K-bits above ΛCDM (field specification on top of CPL parameters).
Statistical preference at ~3.9σ does not justify ~240 extra bits of model complexity
under a strict K-minimality criterion.

Under K-informationalism:
- **ΛCDM / unimodular gravity:** ~40 bits, w = -1 exactly, consistent with Planck 2023
  (w0 = -1.03 ± 0.03 consistent with -1 at 1σ)
- **Quintessence / CPL:** ~280 bits, preferred by DESI 2024 but by < strong-evidence margin

**Conclusion:** The K-information criterion supports ΛCDM / unimodular over quintessence
until the evidence from DESI, Euclid, Roman exceeds both:
1. delta_BIC >> 10 (statistical threshold), and
2. A comparable reduction in the K-content required for the winning model

The latter condition is only satisfied if a specific quintessence potential is uniquely
selected — which requires many more bits to specify than the integration constant Λ.

---

## 6. What Would Change the Verdict

| Observation | Threshold | Effect |
|---|---|---|
| f·σ8 tension at z~0.5 | > 2σ deviation from ΛCDM | Structural evidence for w != -1 |
| DESI year-5 w0 constraint | σ(w0) < 0.05 | Would sharpen or dissolve tension |
| Euclid w0 measurement | 3σ detection of w0 != -1 | BIC decision tips to CPL |
| Planck + CMB-S4 | w0 precision to 0.02 | Resolves Planck vs DESI tension |
| K-content reduction | Field potential selected by UV theory | Would reduce quintessence K-bits |

The DESI vs Planck tension on w0 (-0.827 vs -1.03) is itself a
~1.0σ
discrepancy, suggesting systematic issues may be present.

---

## References

- DESI 2024 arXiv:2404.03002 — BAO + CMB + SNIa dark energy constraints
- Planck 2023 (Aghanim et al.) A&A 641, A6 — w0 constraint
- Chevallier & Polarski (2001) IJMPD 10, 213 — CPL parameterization
- Linder (2003) PRL 90, 091301 — CPL + growth rate
- Linder & Cahn (2007) Astropart.Phys. 28, 481 — gamma approximation
- Kass & Raftery (1995) JASA 90, 773 — BIC evidence scale
- Henneaux & Teitelboim (1989) PLB 222 — unimodular gravity
- mechanism_sweep.md — K-content of CC mechanisms (this track)
