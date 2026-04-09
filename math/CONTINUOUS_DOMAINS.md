# Continuous Domain Proof Techniques — For the Sigma Method

## The Problem

Prove f(x) > 0 for all x ∈ S where S is continuous (not discrete).

## Five Methods

### Method 1: Grid + Lipschitz
- Bound the Lipschitz constant L = sup|∇f|
- Check f on grid with spacing h < f_min / L
- If f(grid) > Lh everywhere: f > 0 everywhere

**Applicability:** Low-dimensional continuous parameters (c ∈ [0,1] for YM).

### Method 2: Polynomial Enclosure (Taylor Models)
- f(x) = p(x) + [-ε, ε] where p is polynomial, ε is rigorous remainder
- Prove p(x) > ε by polynomial root analysis or interval sweep

**Applicability:** Functions with known Taylor expansions (analytic functions).

### Method 3: Radii Polynomial (Verified PDE)
- Approximate solution ū of F(u) = 0
- Bound residual ||F(ū)||, inverse ||DF⁻¹||, nonlinearity ||D²F||
- Contraction mapping → exact solution exists near ū

**Applicability:** PDE solutions (NS Leray profile, YM effective action).

### Method 4: Galerkin + Tail Bound
- f = f_N (N modes) + f_tail (rest)
- Prove f_N > δ by finite computation
- Prove |f_tail| < δ by analytical decay bound
- f > 0 follows

**Applicability:** Spectral problems (YM character expansion, NS Fourier, RH Dirichlet series).

### Method 5: Compactification
- Map R^n → S^n or bounded domain
- Prove positivity on the compact domain (which IS finite)

**Applicability:** Noncompact domains (R³ for NS, R⁴ for YM continuum limit).

## Application to Each Millennium Problem

### Yang-Mills: Method 4 (Galerkin + Tail)
- f_N = GC computed with j_max = N in the character expansion
- f_tail = contribution of j > N representations
- Tail bound: |f_tail| ≤ Σ_{j>N} (2j+1)|c_j(β)| (super-exponential decay in j)
- At j_max = 3: tail < 10⁻⁶ for β ≤ 4
- f_N = GC_mf = 1/2 - c²/4 (at leading order) → f_N > 1/4
- Correction δ at finite j_max: bounded by one-loop integral
- The NUMBER: |δGC| < 1/4

### Navier-Stokes: Method 4 (Galerkin + Tail) already done
- SOS certificates on N modes + spectral tail bound
- 1.33M certificates for N ≤ 13
- Tail bound from Sobolev decay
- Gap: the SOS floor DECREASES with N — need it to stabilize

### Riemann Hypothesis: Method 1 (Grid + Lipschitz) for Turing verification
- Z(t) on a grid, spacing < π/log(T/2π)
- Lipschitz from Z'(t) bound
- Also: Method 4 for Li coefficients (finite zeros + tail)

### BSD: Method 1 (Grid over conductor families)
- Discrete in conductor, continuous in L-value
- Grid = all curves of conductor ≤ N
- Lipschitz not needed (discrete domain)

### Hodge: Method 4 (Galerkin on representation theory)
- Finite MT groups per dimension (Galerkin)
- Higher dimensions = tail (induction on g)
