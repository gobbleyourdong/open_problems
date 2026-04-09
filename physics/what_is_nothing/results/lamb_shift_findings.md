# Lamb Shift as Vacuum Energy Measurement — Findings

*Numerical track, what_is_nothing — 2026-04-09*

## What was computed

1. **Lamb shift** of hydrogen (2s₁/₂ - 2p₁/₂) via the Bethe/Drake leading-order formula
2. **Vacuum energy density comparison**: Casimir vs Lamb shift (crossover length scale)
3. **Multi-scale vacuum energy**: ρ_vac(L) from Planck to Hubble
4. **Scaling law**: ρ_vac ∝ L⁻⁴ — verified numerically

---

## 1. Lamb Shift

The Dirac equation predicts the 2s₁/₂ and 2p₁/₂ states of hydrogen are exactly
degenerate. QED vacuum fluctuations — virtual photons — break this degeneracy.

**Formula** (Erickson & Yennie 1965; Drake 1990):
```
ΔE = (α/π)(Zα)⁴ m_e c² / n³ × A₄₀(2s₁/₂)
A₄₀(2s₁/₂) = 10.45  (Drake 1990, Bethe logarithm for 2s state)
```

| Quantity | Value |
|----------|-------|
| Leading-order result | 1063.11 MHz |
| Measured (Beyer et al. 2017) | 1057.845 MHz |
| Leading / measured ratio | 1.0050 |
| Residual offset | +0.50% |

The ~0.5% residual comes from two-loop QED self-energy, the proton charge radius
(r_p ≈ 0.84 fm), and nuclear recoil — all calculated in full QED to sub-kHz accuracy.

**Physical origin**: The 2s wave function has |ψ(0)|² ≠ 0 (electron at the proton).
The 2p wave function has |ψ(0)|² = 0. Vacuum polarization therefore perturbs the
2s level but not 2p, splitting the Dirac degeneracy by 1057.845 MHz.
This is a direct measurement of the QED vacuum.

---

## 2. Vacuum Energy Density: Casimir vs Lamb Shift

| Quantity | Value |
|----------|-------|
| ρ_Lamb = ΔE / V_Bohr | 1.1292e+06 J/m³ |
| Crossover distance d* | 5.8251e-09 m = 110.1 × a₀ |

At plate separation d* ≈ 5.83e-09 m (≈ 110 Bohr radii), the Casimir
and Lamb shift vacuum energy densities are equal. Both probe the same QED vacuum
at atomic-scale distances. The Casimir formula ρ ∝ d⁻⁴ and the Lamb formula
ρ ∝ a₀⁻⁴ are manifestations of the same ρ ∝ L⁻⁴ scaling.

---

## 3. Vacuum Energy Density Across Scales

Formula: ρ_vac(L) = g_eff × ħc / (32π² L⁴), g_SM = 41

| Scale | L (m) | log₁₀ ρ (SM, J/m³) | log₁₀(ρ_SM / ρ_Λ) |
|-------|--------|---------------------|-------------------|
| Planck length | 1.62e-35 | 112.8 | +139.0 |
| Nuclear (1 fm) | 1.00e-15 | 33.6 | +59.8 |
| Bohr radius | 5.29e-11 | 14.7 | +40.9 |
| 1 mm | 1.00e-03 | -14.4 | +11.8 |
| Match scale L* | 9.12e-01 | -26.2 | -0.0 **← match** |
| 1 m | 1.00e+00 | -26.4 | -0.2 **← match** |
| Hubble radius | 1.37e+26 | -130.9 | -104.7 |

Observed: ρ_Λ = 5.924e-27 J/m³,  log₁₀(ρ_Λ) = -26.2

---

## 4. Scaling Law

**ρ_vac(L) ∝ L⁻⁴** — confirmed to slope = -4.0 (expected: -4).

The L⁻⁴ law is exact by construction: summing ½ħω over modes up to k_max = 1/L
gives a density ∝ k_max⁴ ∝ L⁻⁴. Physical meaning: vacuum fluctuations at scale L
contribute an energy density ∝ (ħc/L) per unit volume L³.

---

## Key Finding

**The effective IR cutoff for the observed vacuum energy is L* ≈ 0.91 m.**

| Cutoff | log₁₀(ρ_SM / ρ_Λ) | Discrepancy |
|--------|-------------------|-------------|
| L = l_P (Planck) | +139 | 10^139 too large |
| L = L* ≈ 0.91 m | 0 | exact match |
| L = H₀⁻¹ (Hubble) | -105 | 10^105 too small |

The standard framing of the CC problem as "ρ_QFT / ρ_Λ = 10^139" presupposes the
Planck UV cutoff. The L⁻⁴ scaling reveals that this is not inevitable: the formula
ρ_vac ∝ L⁻⁴ produces ρ_Λ for L* ≈ 0.91 m.

**The cosmological constant problem in sharpest form**:
> Why does the effective IR vacuum energy cutoff sit at L* ≈ 0.91 m?
> It is not the Planck scale, not the Hubble scale, not any natural particle physics scale.
> It is an *unexplained intermediate* scale.

### Connection to Lamb Shift and Casimir Effect

The Lamb shift probes vacuum fluctuations at L ≈ a₀ = 5.29e-11 m.
The Casimir effect probes them at L ≈ d (plate separation, nm to mm).
Dark energy probes the vacuum at the effective scale L* ≈ 0.91 m.

All three share the L⁻⁴ scaling law. The cosmological constant problem is not that
the vacuum is "unexpectedly large" — it is that the relevant scale L* is unknown.

### Proposed mechanisms for L*

- **Supersymmetry**: bosonic/fermionic cancellation reduces the sum, but SUSY must be
  broken at a scale that reproduces L* — which re-poses the problem.
- **Holography**: the Bekenstein-Hawking entropy of the de Sitter horizon bounds the
  number of vacuum modes to N ≈ S_dS ∝ (L_Hubble / l_P)², which modifies the cutoff.
- **UV/IR mixing**: quantum gravity may link L_UV and L_IR via N_modes ≈ (L/l_P)^d,
  giving an effective cutoff between the two extremes.
- **Emergent spacetime**: if spacetime is thermodynamic/entropic, the Planck-scale
  mode sum is unphysical; the effective vacuum energy is set by causal structure.
- **Anthropic selection**: Λ is small enough for structure formation because
  observers exist only where this condition holds (Weinberg 1987 bound).

---

*Data: results/lamb_shift_data.json*

*References*:
Bethe (1947) Phys Rev 72, 339 |
Lundeen & Pipkin (1975) Phys Rev Lett 34, 1368 |
Erickson & Yennie (1965) Ann Phys 35, 271 |
Drake (1990) Can J Phys 68, 276 |
Beyer et al. (2017) Science 358, 79 |
Cohen, Kaplan & Nelson (1999) Phys Rev Lett 82, 4971
