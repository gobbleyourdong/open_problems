# Tomboulis (2007) — Technical Analysis

> arXiv:0707.2179 (original), arXiv:0711.4930 (Ito-Seiler critique),
> arXiv:0712.2620 (Tomboulis reply), arXiv:1210.1794 (updated version)

## The Framework: Migdal-Kadanoff Decimation

### Setup
SU(2) Wilson action on hypercubic lattice. Character expansion:

  exp(β/2 · Re Tr(U_P)) = F₀(β) · f_P(U, β)
  f_P = 1 + Σ_{j≠0} d_j c_j(β) χ_j(U)

where c_j(β) = F_j(β)/F₀(β) ∈ [0, 1] (positivity from Bessel function ratios).

### Decimation Step (a → ba)
1. Partition lattice into cells of side ba
2. Remove interior plaquettes (set action to zero)
3. Move removed interaction to boundary: strengthen by ζ₀ per displacement
4. After d-2 moves: each boundary plaquette strengthened by ζ = ζ₀^{d-2}
5. Integrate interior bonds: b² tiling plaquettes merge into one

Maps: {c_j^{(n-1)}} → {c_j^{(n)}} via:
  c_j^{(n)} = ĉ_j^{(n)}^{b²r}
  F̂_j^{(n)} = ∫ dU [f(U, n-1)]^ζ · (1/d_j) χ_j(U)

### Bounds
**Upper** (ζ = b^{d-2}, 0 < r ≤ 1):
  Z_{Λ^{n-1}} ≤ (F₀ᵁ)^{|Λⁿ|} · Z_{Λⁿ}({c_j^U})

**Lower** (ζ = 1, r = 1):
  Z_{Λⁿ}({c_j^L}) ≤ Z_{Λ^{n-1}}

where c_j^L(n) = c_j(n-1)^{b²} (simple power, no strengthening).

### The Interpolation
Parameter α ∈ [0,1] interpolates:
  c̃_j(m, α, r) = (1-w(α)) c_j^L + w(α) c_j^U

Since Z is increasing in each c_j (reflection positivity + c_j ≥ 0),
by IVT ∃ α* ∈ (0,1) such that the decimated Z exactly equals the original.

### The Exact Representation (eq. 3.35)
Z_Λ(β) = [∏_{m=1}^n F̃₀^{|Λ|/b^{md}}] · Z_{Λⁿ}({c̃_j(n, α^{(n)})})

with c_j^L(n) < c̃_j(n, α*) < c_j^U(n) for all j.

## The Gap: Inequality (5.15)

To extract the vortex free energy F^{(-)} = Z^{(-)}/Z, Tomboulis needs
BOTH Z and Z^{(-)} expressed in terms of the SAME interpolation parameter.

This requires: **A ≥ A⁺** where
  A = (d/dα) ln Z / |Λⁿ|    (response of pure theory)
  A⁺ = (d/dα) ln Z⁺ / |Λⁿ|  (response of vortex theory)

### Status of (5.15)
| Regime | Status | Method |
|--------|--------|--------|
| Strong coupling (c_j small) | PROVED | Cluster expansion |
| Weak coupling (c_j near 1) | OPEN | — |
| U(1) d=4 Coulomb phase | Should FAIL | Vortex free, A⁺ → A |
| SU(2) d=4 any β | Should HOLD | Vortices always cost energy |

### The Circular Structure
A > A⁺ ⟺ Z > Z⁺ ⟺ vortices cost energy ⟺ confinement.
The inequality IS the confinement statement, repackaged.
Tomboulis bootstraps from strong coupling (proven) to all β via decimation.

### The Open Question
Does MK decimation PRESERVE A > A⁺?
If yes → proof works → confinement for all β → mass gap.
If no → Tomboulis approach fails at intermediate coupling.

## What This Means for the Mass Gap

Tomboulis's result (if completed) proves CONFINEMENT (area law), not mass gap directly.
But: Chatterjee (2021) proved mass gap ⟹ confinement.
The reverse direction (confinement ⟹ mass gap) is NOT proven in general.

However, for pure SU(2), the string tension σ > 0 (confinement) strongly
suggests Δ > 0 (mass gap), since the lightest glueball mass is related to
the string tension by m ~ √σ.

## Key Equations for Lean Formalization
1. c_j ∈ [0,1] for SU(2) Wilson action (Bessel function property)
2. Z is increasing in each c_j (reflection positivity)
3. MK decimation preserves the character expansion form
4. Upper/lower bound sandwich (eqs. 3.4, 3.7)
5. IVT for interpolation parameter (eq. 3.24)
6. The disputed inequality (5.15)
