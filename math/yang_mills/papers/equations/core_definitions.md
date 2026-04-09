# Yang-Mills Core Definitions — Equation Manifest

## 1. Classical Yang-Mills

### 1.1 Gauge Group
G = compact simple Lie group (SU(N) for concreteness, N ≥ 2)
𝔤 = Lie algebra of G
dim(𝔤) = N² - 1 for SU(N)

### 1.2 Connection (Gauge Field)
A = A_μ dx^μ, where A_μ : R⁴ → 𝔤
In components: A_μ(x) = A_μ^a(x) T^a, where T^a are generators of 𝔤
[T^a, T^b] = i f^{abc} T^c (structure constants)

### 1.3 Field Strength (Curvature)
F_μν = ∂_μ A_ν - ∂_ν A_μ + g[A_μ, A_ν]
F_μν^a = ∂_μ A_ν^a - ∂_ν A_μ^a + g f^{abc} A_μ^b A_ν^c

### 1.4 Yang-Mills Action
S[A] = -(1/4) ∫_{R⁴} Tr(F_μν F^{μν}) d⁴x
     = (1/4g²) ∫_{R⁴} |F_A|² d⁴x   (physicist vs geometer convention)

For SU(N): Tr(T^a T^b) = -(1/2) δ^{ab}
So: S[A] = (1/4) ∫ F_μν^a F^{μν,a} d⁴x

### 1.5 Yang-Mills Equations (Euler-Lagrange)
D_μ F^{μν} = 0   (equations of motion)
D_μ = ∂_μ + g[A_μ, ·]   (covariant derivative)

In components: ∂_μ F^{μν,a} + g f^{abc} A_μ^b F^{μν,c} = 0

Plus Bianchi identity: D_{[μ} F_{νρ]} = 0 (automatic from F = dA + A∧A)

### 1.6 Gauge Transformations
A_μ → g A_μ g⁻¹ + g ∂_μ g⁻¹,  g : R⁴ → G
F_μν → g F_μν g⁻¹
S[A^g] = S[A]  (gauge invariance)

## 2. Lattice Gauge Theory (Wilson 1974)

### 2.1 Lattice Setup
Λ = (aZ)⁴ ∩ [0,L]⁴, lattice spacing a, volume L⁴
Links: ℓ = (x, μ), connecting x to x+aê_μ
Link variables: U_ℓ ∈ G (NOT in the Lie algebra)

### 2.2 Plaquette
P_{μν}(x) = U_{x,μ} U_{x+aê_μ,ν} U_{x+aê_ν,μ}⁻¹ U_{x,ν}⁻¹
(ordered product around elementary square)

### 2.3 Wilson Action
S_W[U] = β Σ_P (1 - (1/N) Re Tr(U_P))
β = 2N/g² (for SU(N))

Continuum limit: S_W → (a⁴/4g²) Σ_{x,μ<ν} Tr(F_μν²) + O(a²)

### 2.4 Lattice Partition Function
Z = ∫ ∏_ℓ dU_ℓ exp(-S_W[U])
dU_ℓ = Haar measure on G (normalized: ∫_G dg = 1)

### 2.5 Wilson Loop (Order Parameter)
W(C) = ⟨(1/N) Tr(∏_{ℓ∈C} U_ℓ)⟩

Area law: W(C) ~ exp(-σ Area(C)) ⟹ confinement (σ = string tension)
Perimeter law: W(C) ~ exp(-μ Perimeter(C)) ⟹ deconfined

### 2.6 Continuum Limit
a → 0 with g(a) → 0 (asymptotic freedom):
g²(a) ~ -1/(β₀ ln(aΛ_{QCD}))
β₀ = (11N)/(48π²) for pure SU(N)  (Gross-Wilczek-Politzer)

## 3. Quantum Theory — What Must Be Constructed

### 3.1 Wightman Axioms (Minkowski)
A quantum field theory is specified by:
W1. Hilbert space H with vacuum |Ω⟩
W2. Unitary representation of Poincaré group on H
W3. Spectral condition: p² ≥ 0, p⁰ ≥ 0 for spectrum of P^μ
W4. Field operators φ(f) for test functions f
W5. Locality: [φ(x), φ(y)] = 0 for (x-y)² < 0
W6. Vacuum is cyclic for field algebra
W7. Unique vacuum

### 3.2 Osterwalder-Schrader Axioms (Euclidean)
Equivalent to Wightman via Wick rotation t → -iτ:
OS1. Euclidean covariance (SO(4) rotation + R⁴ translation)
OS2. Reflection positivity: ⟨θf, f⟩ ≥ 0
      (θ = time reflection, this reconstructs the Hilbert space)
OS3. Regularity (growth bounds on correlators)

### 3.3 Mass Gap
Hamiltonian H = generator of time translations
spec(H) = {0} ∪ [Δ, ∞)  with Δ > 0
Equivalently: ⟨Ω|φ(x)φ(0)|Ω⟩ ~ e^{-Δ|x|} as |x| → ∞ (exponential clustering)

In Euclidean: 2-point function G(x) = ⟨φ(x)φ(0)⟩ decays as e^{-Δ|x|}
Mass gap = inverse correlation length: Δ = 1/ξ, where ξ = lim_{|x|→∞} -|x|/ln G(x)

### 3.4 What "Non-trivial" Means
The theory must NOT be a free (Gaussian) theory.
In particular: connected 4-point function must be nonzero.
Equivalently: the S-matrix must be non-trivial (scattering occurs).

## 4. Key Structural Results

### 4.1 Asymptotic Freedom (Gross-Wilczek-Politzer 1973)
β(g) = -β₀ g³ - β₁ g⁵ - ...
β₀ = (11N - 2N_f)/(48π²) > 0 for N_f < 11N/2

For PURE YM (N_f = 0): β₀ = 11N/(48π²) > 0 always.
⟹ Coupling decreases at short distances → UV completion exists
⟹ Lattice → continuum limit should exist (the theory becomes free at a→0)

### 4.2 Confinement (not proved, numerically established)
Color-charged states don't appear in the physical spectrum.
Physical spectrum = color singlets only (glueballs for pure YM).
Lightest glueball mass = the mass gap Δ.

For SU(3): Δ ≈ 1.5 GeV (lattice, Morningstar-Peardon 1999)
For SU(2): Δ ≈ 4.7 / r₀ where r₀ ≈ 0.5 fm (Lucini-Teper 2001)

### 4.3 Instantons (Belavin-Polyakov-Schwarz-Tyupkin 1975)
Self-dual solutions: F = *F (or anti-self-dual: F = -*F)
Action: S = 8π²|k|/g² where k ∈ Z is the topological charge
k = (1/32π²) ∫ Tr(F ∧ F)

These are saddle points, not minima. They contribute to the path integral
non-perturbatively ~ exp(-8π²/g²).

### 4.4 Gribov Problem (Gribov 1978)
Gauge fixing (e.g., Coulomb gauge ∂_i A_i = 0) does NOT uniquely fix the gauge.
There are Gribov copies: distinct gauge fields related by large gauge transformations
that satisfy the same gauge condition.
⟹ Faddeev-Popov procedure is incomplete
⟹ Path integral over gauge-inequivalent configurations is subtle

## 5. Balaban's Program (1982-1989)

### 5.1 Overview
T. Balaban, Comm. Math. Phys. (series of ~13 papers)
"Ultraviolet stability in field theory. The φ⁴₃ model" (template)
"Propagators and renormalization transformations for lattice gauge fields" (1984)
"Averaging operations for lattice gauge theories" (1985)
"Spaces of regular gauge field configurations on a lattice and gauge fixing conditions" (1985)
"Propagators for lattice gauge theories in a background field" (1986)
"Renormalization group approach to lattice gauge field theories" (1987-1989)

### 5.2 Key Achievement
Proved: UV stability of the Wilson lattice gauge theory in 4D.
Meaning: The effective action after integrating out UV modes is bounded,
with bounds uniform in the UV cutoff.

### 5.3 What Was NOT Completed
- Infinite volume limit (thermodynamic limit)
- Verification of OS axioms (reflection positivity in continuum)
- Mass gap
- Reconstruction of Minkowski theory

### 5.4 Why It Stalled
The combinatorial complexity of the RG analysis is enormous.
Each paper handles one step of the RG and is 50-100 pages of estimates.
The full program would require ~2000 pages of closely argued analysis.
Balaban moved on to other problems.

## 6. Dimensions and Scaling

### 6.1 Classical Scaling
In d dimensions: [A_μ] = (d-2)/2, [F_μν] = d/2, [g] = (4-d)/2

d=4: g is dimensionless → classically scale-invariant → quantum theory is marginal
d=3: g has dimension 1/2 → superrenormalizable → easier
d=2: g has dimension 1 → even easier → solved

### 6.2 2D Yang-Mills (SOLVED)
Migdal (1975), Witten (1991, 1992): exact solution via localization
Partition function computed exactly. Area law proved. Mass gap exists.
"Almost trivial" — no propagating degrees of freedom in 2D.

### 6.3 3D Yang-Mills (PARTIAL)
Superrenormalizable: only finitely many divergent diagrams.
Mass gap proved in lattice strong coupling.
Continuum limit: partial results (Magnen-Rivasseau-Sénéor for finite volume).
NOT solved in the Clay sense.

### 6.4 4D Yang-Mills (OPEN)
Marginal: renormalizable but not superrenormalizable.
Asymptotically free: UV is controlled.
IR: strong coupling → nonperturbative → mass gap lives here.
