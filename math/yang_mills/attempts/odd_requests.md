# Requests from theory track

## Request 1: MK Decimation + Vortex Cost Test (PRIORITY)

**Date**: 2026-04-07
**Context**: Tomboulis (2007) gap analysis, attempt_011

### What I Need
Implement the Migdal-Kadanoff decimation for SU(2) and U(1) in d=4,
and test whether the vortex cost inequality Z > Z⁺ is preserved.

### Specific Computation

For SU(2) on lattice L^4 with Wilson action:
1. Compute Z(β) = ∫ ∏ dU exp(-β S_W)  (pure)
2. Compute Z⁻(β) = partition function with anti-periodic BC on one face
   (this inserts a Z₂ vortex flux)
3. Z⁺ = (Z + Z⁻)/2
4. Verify: Z > Z⁺ for various β

Then perform MK decimation:
5. Map {c_j(β)} → {c_j'(β)} via one decimation step
6. Compute Z' and Z'⁺ with the decimated coefficients
7. Check: does Z' > Z'⁺ still hold?
8. Iterate multiple steps

### The Acid Test
Do the same for compact U(1):
- U(1) in d=4 HAS a phase transition at β_c ≈ 1.01
- The vortex cost inequality should FAIL in the Coulomb phase (β > β_c)
- If the MK decimation correctly predicts this failure, the method is sound
- If the MK decimation also shows Z > Z⁺ for SU(2) at all β, that's evidence
  for Tomboulis's conjecture

### Implementation Notes
- For small lattices (2⁴, 3⁴), Z can be computed exactly via character expansion
- The character expansion coefficients are c_j(β) = I_{2j+1}(β)/I_1(β) for SU(2)
- For U(1): c_n(β) = I_n(β)/I_0(β) where n labels Fourier modes
- The MK decimation formulas are in papers/TOMBOULIS_ANALYSIS.md
- Truncate the character expansion at j_max = 3 or 4

### What Success Looks Like
A table like:
| Group | β | n_steps | Z/Z⁺ | Z'/Z'⁺ | Z''/Z''⁺ | Preserved? |
|-------|---|---------|-------|---------|----------|------------|
| SU(2) | 1.0 | 3 | 1.5 | 1.8 | 2.3 | YES |
| SU(2) | 4.0 | 3 | 1.01 | 1.02 | 1.05 | YES |
| U(1) | 0.5 | 3 | 1.3 | 1.5 | 1.8 | YES (confined) |
| U(1) | 2.0 | 3 | 1.001 | 0.999 | 0.95 | NO (Coulomb!) |

---

## Request 2: Fisher Zeros for Small Lattices

**Date**: 2026-04-07
**Context**: Attempt 007 (killed, but data still useful)

Compute Z(β) for SU(2) on 2⁴ lattice as a function of complex β.
Plot |Z(β + iσ)| in the complex plane. Where are the zeros?
How close do they get to ℝ⁺?

Even though the Lee-Yang route is dead for PROVING things, the numerical
data on zero locations is still informative for understanding the theory.

---

## Request 3: Glueball Correlator Mass Gap

**Date**: 2026-04-07
**Context**: Basic mass gap measurement

For SU(2) on 8³×16 or similar (3D spatial, elongated temporal):
- Measure plaquette-plaquette correlator C(t)
- Extract effective mass m_eff(t) = -ln(C(t+1)/C(t))
- Report Δ(β) for β = 1.0, 1.5, 2.0, 2.3, 2.5, 3.0, 4.0
- Need C/GPU implementation — Python too slow for 4D

This provides the baseline data for all theoretical work.
