/-
  Single-Mode Orthogonality Lemma for Navier-Stokes Regularity

  For a single Fourier mode of a divergence-free vector field on T³,
  the Biot-Savart strain has zero projection onto the vorticity:

    ω · S · ω = 0

  This is the geometric foundation of the depletion mechanism.
  All vortex stretching in 3D incompressible Navier-Stokes must
  arise from cross-mode interactions, never from self-interaction.

  The proof works over any CommRing, using only:
  - Mathlib's dotProduct (⬝ᵥ) and crossProduct (⨯₃)
  - Mathlib's dot_cross_self / dotProduct_comm
  - The ring tactic

  Author: the author, Independent Researcher
  Date: March 2026
-/

import Mathlib.LinearAlgebra.CrossProduct

open scoped Matrix

variable {R : Type*} [CommRing R]

/-! ## The Strain Quadratic Form

The Biot-Savart strain tensor for a single Fourier mode with wavevector k
and velocity û = k × ω / |k|² is S_ij = (k_i û_j + k_j û_i) / 2.

The quadratic form ω ↦ ωᵢ Sᵢⱼ ωⱼ = ωᵢ (kᵢ ûⱼ + kⱼ ûᵢ) ωⱼ / 2.

We define the *twice* strain form (avoiding division in CommRing):
  twiceStrainForm(a, p, q) = Σᵢⱼ aᵢ (pᵢ qⱼ + pⱼ qᵢ) aⱼ

This equals 2 (a ⬝ᵥ p)(a ⬝ᵥ q), a factorization that is the key
algebraic identity underlying the entire depletion theory. -/

/-- Twice the symmetric strain quadratic form: Σᵢⱼ aᵢ(pᵢqⱼ + pⱼqᵢ)aⱼ.
    Equals 2 × (a · S · a) where S = (p⊗q + q⊗p)/2. -/
def twiceStrainForm (a p q : Fin 3 → R) : R :=
  a 0 * (p 0 * q 0 + p 0 * q 0) * a 0 +
  a 0 * (p 0 * q 1 + p 1 * q 0) * a 1 +
  a 0 * (p 0 * q 2 + p 2 * q 0) * a 2 +
  a 1 * (p 1 * q 0 + p 0 * q 1) * a 0 +
  a 1 * (p 1 * q 1 + p 1 * q 1) * a 1 +
  a 1 * (p 1 * q 2 + p 2 * q 1) * a 2 +
  a 2 * (p 2 * q 0 + p 0 * q 2) * a 0 +
  a 2 * (p 2 * q 1 + p 1 * q 2) * a 1 +
  a 2 * (p 2 * q 2 + p 2 * q 2) * a 2

/-! ## Key Algebraic Identity -/

/-- **Factorization lemma.** The strain form factors as twice the product
    of dot products. This identity is the algebraic heart of the proof. -/
theorem twiceStrainForm_eq (a p q : Fin 3 → R) :
    twiceStrainForm a p q = 2 * (a ⬝ᵥ p) * (a ⬝ᵥ q) := by
  simp only [twiceStrainForm, dotProduct, Fin.sum_univ_three]
  ring

/-! ## Main Theorems -/

/-- **Single-Mode Orthogonality (via divergence-free condition).**

    For k, ω ∈ R³ with k ⬝ᵥ ω = 0 (divergence-free), the Biot-Savart
    strain form vanishes: twiceStrainForm ω k (k ⨯₃ ω) = 0.

    Uses: factorization + divergence-free hypothesis + dotProduct_comm. -/
theorem single_mode_orthogonality (k ω : Fin 3 → R)
    (hdiv : k ⬝ᵥ ω = 0) :
    twiceStrainForm ω k (k ⨯₃ ω) = 0 := by
  rw [twiceStrainForm_eq]
  have h1 : ω ⬝ᵥ k = 0 := by rw [dotProduct_comm]; exact hdiv
  rw [h1]; ring

/-- **Single-Mode Orthogonality (via cross product perpendicularity).**

    The strain form vanishes for ANY k, ω ∈ R³ — no hypothesis needed
    beyond the Biot-Savart structure u = k ×₃ ω.

    This is STRONGER: even without divergence-free, the cross product
    structure of Biot-Savart prevents self-stretching. The divergence-free
    condition provides a *second*, independent mechanism.

    Uses: factorization + Mathlib's `dot_cross_self`. -/
theorem single_mode_orthogonality_unconditional (k ω : Fin 3 → R) :
    twiceStrainForm ω k (k ⨯₃ ω) = 0 := by
  rw [twiceStrainForm_eq]
  have h : ω ⬝ᵥ k ⨯₃ ω = 0 := dot_cross_self k ω
  rw [h]; ring

/-! ## Scope and Limitations

### What this proves
For EACH Fourier mode k of a divergence-free field:
  ω̂(k) · Ŝ(k) · ω̂(k) = 0
i.e., no single mode can stretch its own vorticity.

### What this does NOT prove
- Multi-mode stretching decomposition (planned: StretchingDecomposition.lean)
- Navier-Stokes regularity (requires bounding cross-mode interactions)
- Any claim about the full nonlinear dynamics

### Mathematical context
- Constantin & Fefferman (1993): vorticity direction regularity criterion
- Buaria, Lawson & Wilczek (2024): anti-twist mechanism (Science Advances)
- This lemma: the Fourier-space foundation underlying both results

### Dependencies
- `Mathlib.LinearAlgebra.CrossProduct` (provides `crossProduct`, `dot_cross_self`,
  `dotProduct`, `dotProduct_comm`)
- `twiceStrainForm`: explicit expansion of the standard symmetric outer product
  form Σᵢⱼ aᵢ(pᵢqⱼ + pⱼqᵢ)aⱼ — verifiable by inspection
-/
