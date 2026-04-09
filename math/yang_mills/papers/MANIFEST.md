# Yang-Mills Paper Arsenal — Full Manifest

> Built: 2026-04-07 | Even Instance Phase 1
> Triple-verify status: equations checked against sources, cross-referenced

## Tier 1: Foundations (must formalize first)

### 1.1 Official Problem Statement
- **Jaffe, Witten** (2000). "Quantum Yang-Mills Theory." Clay Mathematics Institute.
  - Wightman axioms (W1-W7) for gauge-invariant observables
  - Mass gap: Δ = inf{√(p²) : p ∈ Spec(P^μ), p ≠ 0} > 0
  - Any compact simple G. SU(2) suffices for prize.
  - Euclidean alternative via Osterwalder-Schrader reconstruction

### 1.2 Lattice Gauge Theory
- **Wilson** (1974). "Confinement of quarks." Phys. Rev. D 10, 2445.
  - S_W = (β/N) Σ_p Re tr(I - U_p), β = 2N/g²
  - Z = ∫ ∏_ℓ dU_ℓ exp(-S_W)
  - Area law at strong coupling (high-temp expansion)

### 1.3 Osterwalder-Schrader Reconstruction
- **Osterwalder, Schrader** (1973). Commun. Math. Phys. 31, 83-112.
- **Osterwalder, Schrader** (1975). Commun. Math. Phys. 42, 281-305.
  - OS axioms → Wightman axioms
  - Key: reflection positivity ⟨θ̄F · F⟩ ≥ 0

### 1.4 Reflection Positivity on Lattice
- **Osterwalder, Seiler** (1978). Ann. Phys. 110, 440-471.
- **Osterwalder, Seiler** (1980). Commun. Math. Phys. 71, 243-256.
  - Wilson action satisfies OS reflection positivity on lattice
  - Strong coupling confinement (area law)

### 1.5 Asymptotic Freedom
- **Gross, Wilczek** (1973). Phys. Rev. Lett. 30, 1343. (Nobel 2004)
- **Politzer** (1973). Phys. Rev. Lett. 30, 1346. (Nobel 2004)
  - β(g) = -b₀g³ - b₁g⁵ + ..., b₀ = 11N/(48π²) > 0
  - Pure SU(N): coupling → 0 at short distances
  - WHY IT MATTERS: UV control + non-triviality (unlike φ⁴₄)

### 1.6 Glimm-Jaffe Constructive QFT (Template)
- **Glimm, Jaffe** (1981). "Quantum Physics: A Functional Integral Point of View." Springer.
  - φ⁴₂: complete construction, Wightman axioms, mass gap
  - φ⁴₃: construction with mass + coupling renormalization
  - THE template for constructive approach to YM

### 1.7 φ⁴₄ Triviality
- **Aizenman** (1981). Commun. Math. Phys. 86, 1-48.
- **Fröhlich** (1982). Nucl. Phys. B 200, 281.
- **Aizenman, Duminil-Copin** (2021). Annals of Mathematics 194, 163-235.
  - φ⁴₄ continuum limit is FREE (trivial)
  - YM₄ is different: asymptotic freedom ⟹ non-trivial

## Tier 2: Core Technical Results

### 2.1 Balaban's UV Stability Program (13 papers, 1982-1989)
- **Balaban** (1984). Commun. Math. Phys. 95, 17-40. (Propagators I)
- **Balaban** (1984). Commun. Math. Phys. 96, 223-250. (Propagators II)
- **Balaban** (1985). Commun. Math. Phys. 98, 17-51. (Averaging operations)
- **Balaban** (1985). Commun. Math. Phys. 99, 389-434. (Background field propagators)
- **Balaban** (1985). Commun. Math. Phys. 99, 75-102. (Gauge fixing)
- **Balaban** (1985). Commun. Math. Phys. 102, 255-275. (3D UV stability — COMPLETE)
- **Balaban** (1987). Commun. Math. Phys. 109, 249-301. (4D RG I — small field)
- **Balaban** (1989). Commun. Math. Phys. 122, 175-202. (Large field I)
- **Balaban** (1989). Commun. Math. Phys. 122, 355-392. (Large field II)
  - KEY: UV stability for 4D lattice YM (small field regime)
  - Axial gauge fixing + block averaging RG
  - 3D: COMPLETE. 4D: small field done, large field incomplete
  - MISSING: infinite volume, continuum limit, mass gap, OS axioms

### 2.2 Chatterjee Area Law
- **Chatterjee** (2021). Commun. Math. Phys. 385, 1007-1039. arXiv:2006.16229
  - ⟨W(C)⟩ ≤ exp(-c · Area(C)) at strong coupling, any d ≥ 2
  - New probabilistic technique (not cluster expansion)

### 2.3 Cao-Chatterjee
- **Cao, Chatterjee** (2021). arXiv:2111.07778. (3D YM state space)
- **Cao, Chatterjee** (2023). arXiv:2305.04312. (2D torus YM measure)

### 2.4 Mass Gap Numerics
- **Morningstar, Peardon** (1999). Phys. Rev. D 60, 034509. arXiv:hep-lat/9901004
  - SU(3) glueball: 0++ = 1730 ± 50 ± 80 MeV
- **Lucini, Teper, Wenger** (2002). Phys. Lett. B 545, 197. arXiv:hep-lat/0206029
  - SU(2) glueball masses, large-N scaling confirmed

## Tier 3: Modern Approaches

### 3.1 Stochastic Quantization (Hairer School)
- **Hairer** (2014). Inventiones Math. 198, 269-504. arXiv:1303.5113 (Regularity structures)
- **Chandra, Chevyrev, Hairer, Shen** (2022). Publ. Math. IHÉS. arXiv:2006.04987 (2D YM Langevin)
- **Chandra, Chevyrev, Hairer, Shen** (2022). arXiv:2201.03487 (3D YM-Higgs local)
- **Chevyrev** (2022). arXiv:2205.09940 (3D YM local well-posedness)
  - 2D: DONE. 3D: local solutions. 4D: critical — out of reach
  - Requires breakthrough in critical regularity structures

### 3.2 Gribov Problem
- **Gribov** (1978). Nucl. Phys. B 139, 1.
- **Singer** (1978). Commun. Math. Phys. 60, 7.
  - Topological obstruction: no smooth global gauge fixing for non-Abelian theories
  - Affects any gauge-fixed functional integral approach

### 3.3 Lean Formalizations (existing)
- **LeanMillenniumPrizeProblems** — github.com/lean-dojo/LeanMillenniumPrizeProblems
  - `Quantum.lean` (396 lines): Spacetime, CompactSimpleGaugeGroup, GaugeField,
    FieldStrength, YangMillsAction, WightmanAxioms, QuantumYangMillsTheory
  - `Millennium.lean` (128 lines): YangMillsExistenceAndMassGap statement
  - Uses bounded operators (Mathlib lacks unbounded). Simplified Poincaré group.
- **Douglas, Hoback, Mei, Nissim** (2026). arXiv:2603.15770
  - Free bosonic scalar field satisfies Glimm-Jaffe axioms in Lean 4
  - OS axioms proved for free fields. NOT applicable to gauge/interacting theories.
- **PhysLean/HepLean** — github.com/HEPLean/PhysLean
  - Standard Model gauge group, Wick's theorem, tensor index notation
  - NO fiber bundles, connections, curvature, classical YM, or QFT axioms

### 3.4 Instantons
- **Belavin, Polyakov, Schwarz, Tyupkin** (1975). Phys. Lett. B 59, 85.
  - Self-dual solutions: F = *F. Action: S = 8π²|k|/g², k ∈ Z
  - Non-perturbative contributions ~ exp(-8π²/g²)

## Tier 1.5: CRITICAL NEW RESULTS (2025)

### 1.51 Modern Strong-Coupling Mass Gap (SZZ/Nissim program)
- **Shen, Zhu, Zhu** (2023). arXiv:2204.12737
  - PROVED: Mass gap for SU(N), SO(N) at strong coupling (β < c_d)
  - Method: Langevin dynamics + Bakry-Émery criterion (positive Ricci curvature)
- **Nissim** (2025). arXiv:2510.22788
  - Extended SZZ23 to U(N) via U(1)×SU(N) decomposition
  - Three-step proof: cluster expansion (U(1)) + locality + Bakry-Émery (SU(N))
  - **LIMITATION**: Strong coupling only. Cannot reach weak coupling.
  - CORRECTED: NOT "all couplings in 't Hooft limit" — strong coupling only.

### 1.52 Expanded Area Law
- **Cao, Nissim, Sheffield** (2025). arXiv:2505.16585, arXiv:2509.04688
  - Expanded area law regimes via dynamical approach
  - Verifies Durhuus-Fröhlich mass gap condition in certain regimes

### 1.53 SU(2) YM-Higgs Scaling Limit
- **Chatterjee** (2024). arXiv:2401.10507
  - First non-Abelian continuum limit (SU(2) YM-Higgs)

### 1.54 Tomboulis Confinement Claim (Disputed)
- **Tomboulis** (2007). arXiv:0707.2179. Updated: arXiv:1210.1794
  - Claimed: SU(2) in d ≤ 4 confining for all 0 < g < ∞
  - Method: RG decimation with potential-moving bounds
  - **CRITICIZED**: Ito-Seiler (arXiv:0711.4930) found missing steps
  - Status: unresolved gaps, not accepted by community
  - STILL THE CLOSEST ATTEMPT AT GAP A

### 1.55 Tomboulis-Yaffe Inequalities
- **Tomboulis, Yaffe** (1985). Commun. Math. Phys. 100, 313-372
  - Proved: boundary condition insensitivity ⟹ mass gap (for SU(2))
  - Extended to SU(N) by Ito (arXiv:0808.3442)

### 1.56 Fradkin-Shenker Analyticity (Gauge-Higgs)
- **Fradkin, Shenker** (1979). Phys. Rev. D 19, 3682
  - Confinement and Higgs phases analytically connected (no phase boundary)
  - Requires Higgs field — does not apply to pure gauge

## Tier 4: Background / Reference

### 4.1 Lattice Textbooks
- Creutz (1983). "Quarks, Gluons and Lattices." Cambridge.
- Montvay, Münster (1994). "Quantum Fields on a Lattice." Cambridge.
- Rothe (2012). "Lattice Gauge Theories." World Scientific, 4th ed.

### 4.2 Constructive QFT Reviews
- Rivasseau (1991). "From Perturbative to Constructive Renormalization." Princeton.
- Bauerschmidt, Brydges, Slade (2019). "Introduction to a Renormalisation Group Method." Springer LNM 2242.

### 4.3 2D Yang-Mills (SOLVED — reference case)
- Migdal (1975). Zh. Eksp. Teor. Fiz. 69, 810.
- Witten (1991). Commun. Math. Phys. 141, 153-209.
- Sengupta (1992). J. Funct. Anal. 108, 231.
- Lévy (2003). Memoirs AMS 166.

---

## Mathlib4 Coverage Assessment

### Available (use directly)
| Area | Mathlib Module |
|------|---------------|
| Lie algebras (abstract) | `Algebra.Lie.Basic`, `Algebra.Lie.Classical` |
| Lie groups | `Geometry.Manifold.Algebra.LieGroup` |
| Smooth manifolds | Charted spaces, smooth maps, tangent bundles |
| Fiber bundles (topological) | `Topology.FiberBundle.Basic` |
| Vector bundles (smooth) | `Geometry.Manifold.VectorBundle.Basic` |
| Haar measure | `MeasureTheory.Measure.Haar` |
| C*-algebras | Gelfand duality, CFC |
| Spectral theory (bounded) | Compact self-adjoint operators |
| Exterior algebra | `LinearAlgebra.ExteriorAlgebra` |
| Differential forms (normed spaces) | `Analysis.Calculus.DifferentialForm.Basic` |
| Schwartz space | `Analysis.Distribution.SchwartzSpace` |
| Gaussian measures | Recent addition |

### ABSENT (must build)
| Area | Impact |
|------|--------|
| **Principal bundles** | Core object — build from fiber bundles |
| **Connections on bundles** | No covariant derivative, parallel transport |
| **Curvature** | No curvature 2-form at all |
| **Differential forms on manifolds** | Only on normed spaces |
| **Unbounded operators** | No dense domains, no self-adjoint extensions |
| **Spectral theorem (unbounded)** | Critical for proper mass gap |
| **Sobolev spaces W^{k,p}** | Only the GNS inequality |
| **su(n) compact form** | sl, so, sp exist but NOT su(n) |

### Strategic Assessment
**Lattice approach is most tractable for Lean.** Finite-dimensional, combinatorial,
all tools exist in Mathlib. The hard math (continuum limit, mass gap) is the
actual open problem — formalizing the framework gets us to the frontier.
