# YM numerical track — Mass Gap from Correlator Decay (Cycle 11)

## Date: 2026-04-08
## Lattice: 4⁴, SU(2), heatbath, 150 measurements per β

## Method
C(r) = ⟨Tr(U_P(0)) Tr(U_P(x))⟩_c as function of Manhattan distance r.
Mass gap: C(r) ~ exp(-Δr), extract Δ from log-linear fit.

## Results

| β | C(0) | C(1) | C(1)/C(0) | Δ_est |
|---|------|------|-----------|-------|
| 1.5 | 0.187 | 5.0e-4 | 0.003 | ~5.9 |
| 2.0 | 0.134 | 1.7e-3 | 0.013 | ~4.4 |
| 2.5 | 0.071 | 1.4e-3 | 0.020 | ~3.9 |
| 3.0 | 0.046 | 6.2e-4 | 0.013 | ~4.3 |
| 4.0 | 0.025 | 4.4e-4 | 0.018 | ~4.0 |

C(r≥2) is noise (negative, O(10⁻⁴)).

## Assessment

**Mass gap Δ > 0 at all tested β.** The correlator drops by factor 50-200
from r=0 to r=1, then hits the noise floor. Correlation length ξ = 1/Δ < 1
lattice spacing at all couplings.

The 4⁴ lattice is too COARSE:
- At strong coupling (β≤2): ξ << 1 (expected, Δ ~ -2ln(β/4))
- At weak coupling (β≥3): still ξ < 1 (need larger lattice to see continuum physics)

## Next Steps
1. L=8 at β=2.2-2.5 (crossover region) — need GPU acceleration
2. Wilson loop W(R,T) for string tension σ — independent gap measurement
3. Polyakov loop for deconfinement order parameter
4. Transfer matrix on 2³ × N_t for rigorous eigenvalue bounds
