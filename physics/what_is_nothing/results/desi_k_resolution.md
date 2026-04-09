# results/desi_k_resolution.md — DESI 2024 Tension Through K-Information Lens

**Date:** 2026-04-09
**Type:** Analytical synthesis (Phase 3, iteration 13)
**Builds on:** dark_energy_eos_findings.md

## The DESI 2024 Tension

From dark_energy_eos_findings.md:
- ΛCDM (w=-1): χ²(DESI 2024) = 9.30, 3.05σ tension — K = 40 bits
- Running vacuum: χ²(DESI 2024) = 6.09, 2.47σ — K = 40 bits
- Quintessence (typical): χ²(DESI 2024) = 3.80, 1.95σ — K = 280 bits

DESI 2024 sees ~3σ evidence against ΛCDM. Planck 2023 sees w = -1.03 ± 0.03 (consistent with ΛCDM at 1σ).

## The K-Information Occam's Razor

**BIC-equivalent K-MDL principle:** prefer the model with minimum K(model) + K(residuals).

For cosmological data with N_data ≈ 10 000 data points:
- BIC penalty for 1 extra parameter = ln(N_data)/2 ≈ 4.6
- To prefer quintessence (280 bits) over ΛCDM (40 bits): need Δlog(L) > (280-40)/8 = 30 (using 8 bits per bit of K difference... actually BIC uses parameter count, not K-bits)

**Proper K-MDL:** Δlog(L) > ΔK_bits × ln(2) / (2 bits per parameter for typical precision)
- ΔK = 280 - 40 = 240 bits for quintessence
- Required Δlog(L) > 240 × ln(2) / 2 ≈ 83
- Current Δlog(L) = (9.30 - 3.80)/2 = 2.75 (in chi-squared units, so 1.375 in log-L units)
- Conclusion: **1.4 << 83 — not enough evidence to prefer quintessence**

**For running vacuum (same K=40 bits as ΛCDM):**
- ΔK = 0 (same K)
- Required Δlog(L) > 0 (any improvement suffices)
- Observed Δlog(L) = (9.30 - 6.09)/2 = 1.6 > 0
- Conclusion: **running vacuum IS preferred over ΛCDM under K-MDL** (same complexity, better fit to DESI)

## What K-informationalism predicts

Under K-informationalism (MDL applied to physics):

1. **ΛCDM vs Running vacuum:** running vacuum wins (same K=40 bits, better DESI fit)
2. **Running vacuum vs Quintessence:** running vacuum wins (K=40 vs 280 bits, not enough evidence for extra K)
3. **If DESI tension strengthens to 5σ:** then Δlog(L) ≈ 12.5, still below 83 needed for quintessence
4. **What would require quintessence:** Δlog(L) > 83, corresponding to ~13σ DESI tension

**K-informationalism predicts:** the current DESI tension is NOT evidence for a fundamentally new dark energy model. It is consistent with running vacuum (ν ≠ 0 in Λ(t) = Λ₀ + 3ν H²(t)) which has the same K-content as ΛCDM. The DESI data slightly favors the running vacuum interpretation, but not new K-content (no new fields, no new parameters).

## The K-residue of dark energy

The CC problem has four components now (adding DESI):

1. **Technical problem** (real, mechanism-independent): QFT predicts ρ_Planck; observed is ρ_Λ. Gap = 10^70 - 10^139 depending on regularization.

2. **Fine-tuning problem** (prior-dependent): Dissolves under log-uniform prior (P = 56%).

3. **Selection problem** (resolved): Anthropic + landscape → 10^361-10^500 viable vacua.

4. **Evolution problem** (new from DESI): Is ρ_Λ constant or evolving? DESI 2024 suggests running vacuum at ~2.5σ. K-MDL: running vacuum is preferred by data without K-cost increase.

**The K-residue:** if dark energy is running (Λ = Λ₀ + 3ν H²), what mechanism sets ν? The running vacuum model has K=40 bits (ν is one parameter), but ν = 0 (ΛCDM) is even simpler (K=0 for that parameter). The evidence for ν ≠ 0 comes from DESI (2.5σ). At the current evidence level, K-MDL prefers ν = 0 (ΛCDM) but notes that running vacuum is a viable alternative.

## Status

Phase 3, iteration 13. DESI 2024 tension (3σ against ΛCDM) does not meet the K-MDL threshold for adopting quintessence (240 bits of extra K). Running vacuum (same K as ΛCDM, 40 bits) is preferred if the DESI data is taken at face value. The CC problem now has four components; the new DESI component (static vs running Λ) is the most tractable observationally and may be resolved by future DESI data releases.
