/-
  Challenge file for Comparator verification.

  These are the theorem STATEMENTS only (with sorry).
  The Solution is in DepletionProof/SingleMode.lean.

  To verify with Comparator:
    lake env comparator config.json

  This certifies that the Solution proves exactly these statements,
  using only permitted axioms [propext, Classical.choice, Quot.sound].
-/

import Mathlib.LinearAlgebra.CrossProduct

open scoped Matrix

variable {R : Type*} [CommRing R]

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

/-- Factorization: the strain form equals twice the product of dot products. -/
theorem twiceStrainForm_eq (a p q : Fin 3 → R) :
    twiceStrainForm a p q = 2 * (a ⬝ᵥ p) * (a ⬝ᵥ q) := by
  sorry

/-- Single-mode orthogonality with divergence-free hypothesis. -/
theorem single_mode_orthogonality (k ω : Fin 3 → R)
    (hdiv : k ⬝ᵥ ω = 0) :
    twiceStrainForm ω k (k ⨯₃ ω) = 0 := by
  sorry

/-- Single-mode orthogonality — unconditional (no hypothesis needed). -/
theorem single_mode_orthogonality_unconditional (k ω : Fin 3 → R) :
    twiceStrainForm ω k (k ⨯₃ ω) = 0 := by
  sorry
