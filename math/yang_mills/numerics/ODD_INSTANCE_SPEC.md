# Odd Instance Spec — Numerical Yang-Mills

> For the Odd Instance (Numerics). Written by Even Instance, 2026-04-07.

## What the Odd Instance Should Build

### Phase 1: Lattice Gauge Theory Solver

**Goal**: Implement SU(2) and SU(3) lattice gauge theory on small lattices.

#### 1.1 Core Objects
```python
# SU(2) parametrization: U = a₀I + i(a₁σ₁ + a₂σ₂ + a₃σ₃), a₀²+a₁²+a₂²+a₃² = 1
# SU(3): use Cabibbo-Marinari or direct exponential map

class LatticeGaugeField:
    def __init__(self, L, d=4, N=2):  # L^d lattice, SU(N)
        self.links = np.zeros((L,)*d + (d, N, N), dtype=complex)  # U_{x,μ}

    def plaquette(self, x, mu, nu):  # U_P = U_{x,μ} U_{x+μ,ν} U_{x+ν,μ}† U_{x,ν}†
        ...

    def wilson_action(self, beta):  # S = β/N Σ_P Re tr(I - U_P)
        ...
```

#### 1.2 Monte Carlo Sampler
- Heat bath algorithm (Creutz for SU(2), Cabibbo-Marinari for SU(3))
- Over-relaxation for faster decorrelation
- Measure: Wilson loop expectations, plaquette average, Polyakov loop
- Target: 10K-100K configurations on 8⁴ to 16⁴ lattices

#### 1.3 Observables to Measure
1. **Plaquette average**: ⟨(1/N) Re Tr(U_P)⟩ — basic thermodynamic quantity
2. **Wilson loops**: W(R,T) for various R,T — extract string tension σ
3. **Correlator**: ⟨Tr(U_P(0)) Tr(U_P(x))⟩_c — extract mass gap from exponential decay
4. **Polyakov loop**: ⟨L(x)⟩ — deconfinement order parameter
5. **Topological charge**: Q = (1/32π²) Σ Tr(F̃F) — instanton counting

### Phase 2: Rigorous Bounds (SOS Certificate Analog)

**Goal**: Like the NS SOS certificates, produce machine-checkable bounds.

#### 2.1 Transfer Matrix Eigenvalues (Small Lattice)
For VERY small lattices (2³ × N_t, 3³ × N_t with SU(2)):
- Explicitly construct the transfer matrix T as a finite-dimensional matrix
- Compute eigenvalues to machine precision
- Verify λ₀ > λ₁ > 0 (mass gap on finite lattice)
- Track gap Δ = -ln(λ₁/λ₀) as β varies (weak → strong coupling)

This is the "iron fortress" — exact numerical proof of mass gap on finite lattice.

#### 2.2 Strong Coupling Expansion
At β → 0 (strong coupling), everything is computable:
- W(R,T) = (β/2N)^{Area} × (1 + O(β))
- Mass gap Δ = -d ln(β/2N²) + O(1) → ∞ as β → 0
- Verify against Monte Carlo

#### 2.3 Weak Coupling Extrapolation
As β → ∞ (weak coupling, continuum limit):
- Track Δ(β) as function of β
- Does Δ → constant × Λ_QCD? (Expected by asymptotic freedom)
- Any sign of Δ → 0? (Would suggest no mass gap — not expected)

### Phase 3: Certificate Generation

#### 3.1 Interval Arithmetic
Like `ns_blowup/interval.py`, implement INTLAB-grade interval arithmetic:
- Rigorous floating-point bounds on transfer matrix elements
- Verified eigenvalue bounds (Gershgorin circles, Krawczyk method)
- Certificate: "For SU(2) on 2³ lattice at β = X, mass gap Δ ∈ [a, b]"

#### 3.2 Coverage Map
| Lattice | Group | β range | Δ range | Status |
|---------|-------|---------|---------|--------|
| 2³ | SU(2) | 0.1-10 | ? | TODO |
| 3³ | SU(2) | 0.1-10 | ? | TODO |
| 2³ | SU(3) | 0.1-10 | ? | TODO |
| 4³ | SU(2) | 1-6 | ? | TODO |

### Phase 4: Anti-Problem Numerics

When the Even instance identifies the gap:
- Test: "Can a lattice configuration have Δ = 0?"
- Optimize AGAINST the mass gap: find configs that minimize λ₀ - λ₁
- Track: what do near-zero-gap configurations look like?

## Key Technical Notes

### SU(2) Haar Measure
Parametrize SU(2) ≅ S³: U = a₀I + i(a₁σ₁ + a₂σ₂ + a₃σ₃)
Haar measure = uniform measure on S³ = (1/2π²) δ(|a|²-1) d⁴a

### SU(3) Haar Measure
Use Cabibbo-Marinari decomposition: SU(3) ≅ SU(2)×SU(2)×U(1) (locally)
Or: exponential map from su(3) with Jacobian

### Performance Targets
- SU(2) on 8⁴: ~10⁶ configs/hour on Spark GPU
- Transfer matrix for 2³: 8 spatial links → SU(2)^8 → discretize → matrix ~10⁴ × 10⁴
- This is MUCH smaller than the NS SOS problem (1.33M configs)

## Communication Protocol

When you find something, write to:
- `numerics/results/` — raw data, plots, summary
- `certs/` — machine-checkable certificates
- Update `gap.md` if your findings change the gap assessment

Request formulas from Even instance by writing to `attempts/odd_requests.md`.
