# Yang-Mills Existence and Mass Gap

## Statement
Prove that for any compact simple gauge group G, a non-trivial quantum Yang-Mills theory exists on R⁴ and has a mass gap Δ > 0.

## Status: OPEN (Clay Millennium Prize, $1M)

## Precise Formulation (Jaffe-Witten)

### What "exists" means
Construct a quantum field theory satisfying the **Osterwalder-Schrader axioms** (Euclidean) or equivalently the **Wightman axioms** (Minkowski) whose classical limit is the Yang-Mills Lagrangian.

The OS axioms (Euclidean path integral formulation):
- **(OS0)** Regularity: Schwinger functions S_n are distributions
- **(OS1)** Euclidean covariance: SO(4) × R⁴ invariance
- **(OS2)** Reflection positivity: ⟨Θf, f⟩ ≥ 0 for test functions supported in t > 0
- **(OS3)** Symmetry: S_n invariant under permutations
- **(OS4)** Cluster property: S_n(x₁,...,x_n) → S_k(x₁,...,x_k)S_{n-k}(x_{k+1},...,x_n) as separation → ∞

### What "mass gap" means
The energy spectrum of the Hamiltonian H (reconstructed via OS → Wightman → H) satisfies:
- The vacuum |Ω⟩ has energy 0
- The next eigenvalue is Δ > 0 (no continuous spectrum starting at 0)
- Δ > 0 is the **mass gap**

Equivalently: the two-point correlator decays EXPONENTIALLY:
  ⟨O(x)O(0)⟩ ~ e^{-Δ|x|} as |x| → ∞

### What "Yang-Mills" means
Classical Lagrangian: L = -(1/4g²) Tr(F_μν F^μν)
Field strength: F_μν = ∂_μ A_ν - ∂_ν A_μ + [A_μ, A_ν]
Connection: A_μ(x) ∈ Lie(G) (gauge field)
Gauge group: G compact simple (e.g., SU(2), SU(3))

The quantum theory is the "path integral" ∫ DA e^{-S[A]} weighted by the Euclidean action S = ∫ L d⁴x, made rigorous.

## Key Objects

| Object | Lives in | Dimension | Role |
|--------|----------|-----------|------|
| A_μ(x) | Lie(G)-valued 1-form | 4 × dim(G) | Gauge connection |
| F_μν(x) | Lie(G)-valued 2-form | 6 × dim(G) | Curvature / field strength |
| U_μ(x) | G | dim(G) | Lattice link variable (≈ e^{iaA_μ}) |
| S[A] | R | 1 | Euclidean action |
| ⟨O⟩ | R or C | 1 | Expectation value (Schwinger function) |
| Δ | R₊ | 1 | Mass gap |

## Known Results

### Solved cases
- **2D YM**: Completely solved (Migdal 1975, Sengupta 1997, Lévy 2003, Driver-Hall-Kemp 2017). No mass gap in 2D (confining in a different sense).
- **3D YM**: Partial. Balaban UV stability. Chatterjee free energy leading term. Construction incomplete.
- **Lattice 4D YM**: Wilson (1974) defined it. Mass gap seen in Monte Carlo. Rigorous: Osterwalder-Seiler (1978) proved OS axioms for lattice at fixed coupling.

### The frontier (4D continuum)
- **Balaban (1984-1989)**: Proved UV stability of 4D lattice YM via RG block-spin. The deepest analytical result. ~1400 pages across 12 papers. Does NOT construct the continuum limit.
- **Chatterjee (2019)**: Leading term of YM free energy on lattice at weak coupling. First rigorous computation of a YM quantity in 4D.
- **Cao-Chatterjee (2023)**: Wilson loop expectations at weak coupling.
- **Magnen-Rivasseau-Sénéor (1993)**: Partial construction via cluster expansion.

### Why 4D is special
- **Asymptotic freedom**: g²(a) → 0 as a → 0 (Gross-Wilczek-Politzer, 1973). The coupling vanishes in the UV. This is WHY the theory should exist (UV complete).
- **Marginal dimension**: In 4D, YM is exactly renormalizable (borderline). In d < 4, super-renormalizable (easier). In d > 4, non-renormalizable (doesn't exist).
- **Confinement**: Non-perturbative phenomenon. No perturbative proof possible. Must come from the lattice or a non-perturbative construction.

## The Sigma Method Pipeline

### Phase 0: Map the space (CURRENT)
- Literature survey of all approaches
- Precise gap analysis (what exactly is open)
- Identify computational certification targets
- Set up Lean axiom framework

### Phase 1: Computational certification
- Lattice SU(2) mass gap measurement (GPU)
- Transfer matrix spectral gap for small lattices
- Interval arithmetic verification of lattice OS axioms
- Adversarial search for obstructions

### Phase 2: Algebraic identities
- Find exact relations in lattice YM (analog of Frobenius cross-term)
- Gauge-invariant Ward identities
- Relate lattice spectral gap to continuum mass gap

### Phase 3: Analytical proof architecture
- Identify the ONE gap (analog of NS Tsai gap)
- Build multiple proof chains
- Lean formalization of proven components

### Phase 4: Close the gap or document the wall honestly

## Analogies to NS (from 842 attempts)

| NS concept | YM analog |
|------------|-----------|
| Fourier modes on T³ | Lattice link variables U_μ(x) ∈ G |
| Galerkin approximation | Lattice gauge theory (finite DOF) |
| Galerkin regularity (trivial) | Lattice OS axioms (Osterwalder-Seiler) |
| Continuum limit | a → 0 limit with asymptotic freedom |
| Key Lemma (α < 3|ω|/4) | Mass gap Δ > 0 on lattice (Monte Carlo) |
| SOS certificates | Transfer matrix spectral gap (interval arith) |
| BKM criterion | OS axioms → Wightman → mass gap |
| The Tsai gap (1/|y| → 1/|y|^{1+ε}) | Lattice → continuum (a → 0 with bounds uniform in a) |

## Critical Difference from NS

NS is a **gap** problem: the proof architecture exists (Key Lemma → Type I → KNSS → Leray → Tsai → NRS → regularity), and ONE step is missing (Tsai's ε).

YM is a **construction** problem: no one has built the object yet. The proof architecture itself must be invented. The closest analog is Glimm-Jaffe's φ⁴ construction, but YM has gauge symmetry (infinite-dimensional redundancy) that φ⁴ doesn't.

The sigma method's computational-first approach is well-suited: build the lattice object, measure everything, let the data tell you what theorem to prove.

## Sigma Method Phase: 0 (Mapping)
