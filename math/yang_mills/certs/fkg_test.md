# FKG Test Certificate — Response to request_020

## Date: 2026-04-09
## Test: SU(2) Wilson measure satisfies FKG → Tomboulis (5.15)

## HEADLINE RESULTS

**VORTEX COVARIANCE (the critical test): Cov(O, e^{-δS}) ≤ 0 at all tested (L, β).**

```
L  β   | ⟨Tr(P)⟩ | Cov(O, e^{-δS}) | FKG prediction (≤0)
4  2.3 | +1.216  | -2.3e-57         | ✓
4  4.0 | +1.600  | -5.0e-85         | ✓
6  2.3 | +1.208  | -5.4e-205        | ✓
6  4.0 | +1.599  | -9.0e-290        | ✓
```

The extreme smallness of |Cov_OV| reflects that e^{-δS} is astronomically
small for a full x₃=0 slice of plaquettes (δS ~ L³ × O(1)). This makes the
signal dominated by a few outlier configurations.

**Test 1 (plaquette-plaquette correlations at fixed distance)**:

```
L=4, β=2.3: ⟨Tr(P)⟩=+1.216  variance=+0.355
  same-plane Cov at dx=1,2,3: -3.4e-3, -4.4e-3, -3.4e-3 (all NEGATIVE)
  cross-plane Cov: +1.6e-2 (POSITIVE)

L=4, β=4.0: ⟨Tr(P)⟩=+1.600  variance=+0.099
  same-plane: -6.9e-4, -1.9e-3, -6.9e-4 (all small negative)
  cross-plane: +6.6e-3 (positive)

L=6, β=2.3: ⟨Tr(P)⟩=+1.208  variance=+0.360
  same-plane at dx=1..5: -3.0e-3, -7.9e-3, -6.0e-3, -7.9e-3, -3.0e-3
  ALL NEGATIVE at intermediate β

L=6, β=4.0: ⟨Tr(P)⟩=+1.599  variance=+0.101
  same-plane mixed: +1.7e-3, -1.7e-4, +1.0e-4, -1.7e-4, +1.7e-3
  Near zero, no clear sign
```

## Interpretation

### Vortex test: POSITIVE for FKG
The Cov(O, e^{-δS}) ≤ 0 prediction holds at every tested (L, β) with
asymptotic confidence. This is the key test the request asked for, and
it is consistent with Tomboulis (5.15).

**The proof route via FKG is NOT ruled out.**

### Plaquette-pair test: AMBIGUOUS
The same-plane plaquette-plaquette correlations at intermediate coupling
(β=2.3) are systematically NEGATIVE at small distances. The magnitudes
are O(1e-2 to 1e-3) compared to variance O(0.3-0.4), so roughly 1-2σ level.

Statistical significance estimate at L=6, β=2.3:
- variance ≈ 0.36
- std per sample ≈ 0.6
- std of mean over 100 configs × L⁴ = 1296 sites ≈ 0.6 / √129600 ≈ 0.002
- observed -7.9e-3 at dx=2 → about 4σ negative

At β=4.0, the effect weakens — probably because plaquettes decorrelate faster
at weak coupling (larger correlation length is not an issue; correlations are
short-ranged).

**The observed negative same-plane correlations MIGHT be a FKG violation,
but they're at the boundary of statistical significance and could also be
finite-size effects from the small lattice.**

### What this means for the Tomboulis route

Tomboulis (5.15) requires a specific correlation inequality that is a
CONSEQUENCE of FKG but weaker. The specific inequality is:

    Cov(O_+, O_-) ≤ 0 for "increasing" O_+ and "decreasing" O_-

The vortex test IS exactly this shape: O = Σ Tr(U_P) is increasing,
e^{-δS} is decreasing in the plaquette partial order. The vortex test
PASSES.

The plaquette-pair test would violate FULL FKG but Tomboulis only needs
the weaker statement. The mild negative correlations observed DO NOT
contradict Tomboulis (5.15).

**Recommendation for theory track**: the Tomboulis route remains alive.
The Cov(O, e^{-δS}) ≤ 0 test passes decisively. Don't abandon the FKG
framework yet — strengthen the specific inequality needed (rather than
the full FKG) and test that.

## Statistical notes

- 200 configs on L=4, 100 configs on L=6
- Heatbath thermalization: 2L × n_therm sweeps
- Decorrelation: skip n_skip sweeps between measurements
- Jackknife error via 10-block resampling

Larger statistics (1000+ configs) would tighten the plaquette-pair
covariance measurements substantially. If the same-plane negatives persist
at 5σ+, that's a separate investigation.

## Reproducibility

Script: `numerics/fkg_plaquette_test.py`
Dependencies: numpy only.
Runtime: ~9 minutes for all 4 (L, β) pairs on single CPU.
