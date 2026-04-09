# Character Expansion Results — 2026-04-07

## SU(2) Lattice Gauge Theory

### Character Coefficients a_j(β) = I_{2j+1}(β)/I_1(β)

| β | a_0 | a_{1/2} | a_1 | a_{3/2} |
|---|-----|---------|-----|---------|
| 0.5 | 1.000 | 0.1237 | 0.0103 | 0.0006 |
| 1.0 | 1.000 | 0.2402 | 0.0392 | 0.0048 |
| 2.0 | 1.000 | 0.4331 | 0.1337 | 0.0319 |
| 5.0 | 1.000 | 0.7193 | 0.4245 | 0.2099 |
| 10.0 | 1.000 | 0.8542 | 0.6583 | 0.4592 |

All a_j → 1 as β → ∞ (weak coupling). The hierarchy between j values
collapses — this is why the character expansion loses predictive power
at weak coupling.

### 1D Mass Gap (single plaquette transfer matrix)

| β | Δ (exact) | Δ (strong coupling) | ratio |
|---|-----------|---------------------|-------|
| 0.1 | 3.689 | 3.689 | 1.000 |
| 0.5 | 2.090 | 2.079 | 1.005 |
| 1.0 | 1.426 | 1.386 | 1.029 |
| 2.0 | 0.837 | 0.693 | 1.207 |
| 10.0 | 0.158 | — | — |
| 20.0 | 0.077 | — | — |

**Δ > 0 for ALL β > 0.** Monotonically decreasing. Δ ~ 3/(2β) at large β.

### 2D Transfer Matrix (L=2 and L=3, periodic)

Results are IDENTICAL for L=2 and L=3 — expected because in 2D the
transfer matrix factorizes by plaquette (no spatial coupling).

| β | λ₀ | λ₁ | Δ = -ln(λ₁/λ₀) |
|---|----|----|-----------------|
| 1.0 | 1.000 | 0.240 | 1.426 |
| 2.0 | 1.000 | 0.433 | 0.837 |
| 4.0 | 1.000 | 0.658 | 0.418 |
| 8.0 | 1.000 | 0.819 | 0.199 |

### Key Finding
**Finite lattice mass gap Δ > 0 confirmed for ALL tested parameters.**
This is consistent with the Krein-Rutman / Perron-Frobenius theorem
(attempt_004.md).

### Limitations
- 2D YM has no propagating degrees of freedom (topological)
- The "mass gap" in 2D is trivial — not a genuine test
- Need 3D and 4D for the real problem
- 3D/4D requires Monte Carlo or explicit high-dimensional transfer matrix

### For Odd Instance
- Extend to 3D: need to construct transfer matrix with spatial plaquettes
- Implement SU(2) Monte Carlo heat bath for 4D
- Compute glueball correlators for mass gap extraction
- Target: 8⁴ SU(2) lattice, β = 2.0-2.7 (near continuum)
