# Balaban's RG Program — Technical Digest

> Distilled from CMP 95, 96, 98, 99, 102, 109, 122 (1984-1989)
> and Dimock's expository series arXiv:1108.1335, 1212.5562, 1304.0705

## The Setup

Lattice Λ = torus T with spacing η = L^{-K}, block lattices at scales L^{-k}.
Gauge field: U : bonds → G ⊂ U(N). Wilson action:

  A(U) = Σ_p η^{d-4} [1 - Re tr U(∂p)]

## 1. Block Averaging (CMP 98, eq. 15)

For coarse bond c, the averaged configuration is:

  Ū(c) = exp[i · Σ_{x∈B(c₋)} L^{-d} · (1/i) log(U(Γ_{c,x}) U(c)⁻¹)] · U(c)

where Γ_{c,x} is a family of contours from the initial point of c to x.

**Key property**: This is NONLINEAR (group is nonabelian). The average satisfies:
- M({U_j⁻¹}) = M({U_j})⁻¹
- M({uU_jv}) = u M({U_j}) v  (equivariance)
- Linearization: (1/i) log M({e^{iA_j}}) = (1/n) Σ A_j + O(A²)

**Composition** (CMP 98, Prop 2): If |U(∂p) - 1| < α₀η², then
|Ū^k(∂p) - 1| < 2α₀. Averaging PRESERVES regularity.

## 2. Axial Gauge Fixing (CMP 98, eq. 58)

Within each block B(y), fix a spanning tree from center y to all points.
Set U(b) = 1 for all tree bonds. This eliminates one gauge DOF per site.

Hierarchical: at scale j, gauge transformation u_j satisfies:
  (R_{0,y} U')(Γ_{y,x}) = 1 for x ∈ B(y), y ∈ Ω^{(j)}

The transformation u is determined UNIQUELY by these conditions.

## 3. Small Field / Large Field (CMP 109, eq. 1.2)

**Small field condition at scale k**:
  |U(∂p) - 1| < ε₀ · η²  where η = L^{-k}

**Characteristic function** (eq. 2.9):
  χ_k = ∏_b χ({|B'(b)| < ε₁})

Configurations violating the small field condition → large field region.

## 4. Effective Action (CMP 109, eq. 1.3)

After k RG steps:

  A_k(U_k) = -(1/g_k²) A(U_k) + Σ_{j=0}^{k-1} {-β_{j+1}(g_j) A(U_k) + [log Z^{(j)} - log Z^{(j)}(1)]}

**Irrelevant terms** (eq. 0.24-0.29):
  E^{(j)}(U) = Σ_{X∈D_j} E^{(j)}(X, U)
  |E^{(j)}(X, U_k)| ≤ O(1)(L^j η)^{4+α} exp(-κ d_j(X)), α > 0

The power 4+α > 4 = d means these terms are IRRELEVANT in d=4.

## 5. Running Coupling (CMP 109, Theorem 2)

**Beta function** (eq. 5.42):
  β = -(∂²/∂p_μ∂p_ν) Π_{μν}(0) for μ ≠ ν

where Π is the vacuum polarization tensor. This is the one-loop β₀.

**Rigorous bound** (eq. 0.31): For SU(2) in d=4,
  1/g² + β log(L^k ε)⁻¹ ≤ 1/g_k² ≤ 1/g² + β' log(L^k ε)⁻¹

This IS asymptotic freedom: g_k → 0 as k → ∞ (shorter distances), with
rigorous bounds on the remainder. The coupling runs logarithmically.

## 6. THE OBSTRUCTION — Large Field in d=4

### The competition:

**Suppression** per large-field plaquette:
  exp(-(1/g_k²) ε₀² η^{2(d-2)})

For d=4: exp(-c ε₀²/g_k²)

As k → ∞: g_k² ~ 1/(b₀ k log L), so suppression = exp(-c·b₀·k·log L)

**Entropy** (number of possible large-field regions):
  At most exp(c' L^{4k}) plaquettes on the lattice

**The ratio**: exp(-c·b₀·k·log L + c'·L^{4k})

Since L^{4k} >> k·log L for large k, **entropy wins**. The large field
contributions are NOT suppressed fast enough to sum over all scales.

### THIS IS THE GAP.

In d=3: suppression is exp(-c/(g²η²)) with η = L^{-k}, which gives
exp(-c·L^{2k}/g²). This BEATS the entropy exp(c'·L^{3k}) when L^{2k}/g²
grows faster — and it does because the coupling is fixed (superrenormalizable).

In d=4: the running coupling exactly BALANCES the dimensional improvement.
This is the marginal case. The one-loop suppression is polynomial (k·log L)
while entropy is exponential (L^{4k}).

## 7. Dimock's Modernization

### Scalar φ⁴₃ (2011-2013, arXiv:1108.1335 etc.)
- Complete proof using Balaban's methods for superrenormalizable case
- **Key innovation**: RG flow as fixed-point problem in Banach space
- Contraction mapping theorem → existence + uniqueness of the flow
- Non-perturbative: no Feynman diagrams, no order-by-order cancellation

### QED₃ (2017-2021, arXiv:2009.01156)
- Extended to photons + fermions on lattice
- Block averaging for BOTH gauge and fermion fields
- Polymer expansions for fermion determinants
- UV stability in finite volume — complete result

### What Dimock did NOT do:
- 4D gauge theory (the open problem)
- Infinite volume limit (even in 3D gauge)
- Mass gap (for anything)

## 8. Summary: What's Proved vs Open

### PROVED (Balaban 1984-1989):
- UV stability for 3D lattice YM (COMPLETE)
- Effective actions well-defined at each finite RG step in 4D
- Coupling runs per asymptotic freedom (rigorous bounds)
- Small field analysis complete in 4D
- Large field R-operation machinery (papers I, II)

### OPEN:
1. **Infinite RG composition in 4D** — large field entropy vs suppression
2. **Infinite volume limit** — cluster expansion in the continuum
3. **Mass gap** — exponential clustering of correlations
4. **OS axioms** — reflection positivity in the continuum limit
5. **OS reconstruction** — Euclidean → Minkowski

## 9. Sources

| Paper | Year | Citation |
|-------|------|----------|
| Balaban, Propagators I | 1984 | CMP 95, 17-40 |
| Balaban, Propagators II | 1984 | CMP 96, 223-250 |
| Balaban, Averaging | 1985 | CMP 98, 17-51 |
| Balaban, Background field | 1985 | CMP 99, 389-434 |
| Balaban, Gauge fixing | 1985 | CMP 99, 75-102 |
| Balaban, 3D UV stability | 1985 | CMP 102, 255-275 |
| Balaban, 4D RG I | 1987 | CMP 109, 249-301 |
| Balaban, Large field I | 1989 | CMP 122, 175-202 |
| Balaban, Large field II | 1989 | CMP 122, 355-392 |
| Dimock, RG/Balaban I | 2011 | arXiv:1108.1335 |
| Dimock, RG/Balaban II | 2012 | arXiv:1212.5562 |
| Dimock, RG/Balaban III | 2013 | arXiv:1304.0705 |
| Dimock, QED₃ UV stab. | 2021 | arXiv:2009.01156 |
| Douglas, Status report | 2004 | Clay annual report |
