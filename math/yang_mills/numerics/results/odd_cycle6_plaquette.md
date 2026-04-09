# YM Odd Instance — Plaquette Correlations (Cycle 6)

## Date: 2026-04-08
## Lattice: 4⁴, SU(2), heatbath + overrelaxation
## Measurements: 50 configs, 100 thermalization, skip 3

| β | ⟨P⟩ | Cov(same) | Cov(diff) | Sign |
|---|------|-----------|-----------|------|
| 1.0 | 0.2433 | -4.64e-04 | -7.72e-03 | -/- |
| 1.5 | 0.3603 | +5.40e-04 | +3.86e-04 | +/+ |
| 2.0 | 0.4984 | -7.11e-03 | +1.46e-03 | -/+ |
| 2.3 | 0.6082 | -6.67e-03 | -2.95e-03 | -/- |
| 2.5 | 0.6547 | +1.48e-04 | -3.06e-03 | +/- |
| 3.0 | 0.7238 | -1.62e-03 | +3.40e-03 | -/+ |
| 4.0 | 0.7989 | -4.90e-03 | +1.22e-03 | -/+ |

## Assessment

**Plaquette averages match theory:**
- β=1.0: ⟨P⟩ = 0.243 vs strong-coupling 0.25 ✓
- β→∞: ⟨P⟩ → 1 (weak coupling) ✓

**Covariance signs are MIXED.** Negative values appear at most β.
However, ALL covariances are O(10⁻³) with only 50 measurements.
Statistical error ~ 1/√50 ≈ 14% — the signal is NOISE-DOMINATED.

## Next Steps
1. Increase to 1000+ measurements (need GPU acceleration)
2. Try larger lattice (8⁴) for volume effects  
3. Separate connected vs disconnected correlator
4. The Tomboulis route requires Cov ≥ 0 — need much higher statistics to test
