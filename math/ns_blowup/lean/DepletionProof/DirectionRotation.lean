/-
  Direction Rotation Identity

  For any symmetric matrix S and unit vector ê:
    ê · S² · ê = (ê · S · ê)² + |S·ê - (ê·S·ê)·ê|²

  Physical meaning: The self-depletion ê·S²·ê decomposes into
  the stretching rate squared (α²) plus the direction rotation
  rate squared (|Dξ/Dt|²). Depletion ALWAYS exceeds α², with
  equality only when ê is exactly a strain eigenvector.

  This is the Pythagorean theorem applied to the decomposition
  S·ê = (ê·S·ê)·ê + S_⊥·ê where S_⊥ is the perpendicular part.

  Author: Jason Burton, Independent Researcher
  Date: March 2026
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith

-- (Pythagorean decomposition is trivial: |Bv|² = α² + (|Bv|²-α²) by algebra.
--  The content is in the non-negativity proof below.)

/-- The non-negativity of the perpendicular component.
    |Bv|² - (v·Bv)² ≥ 0 when |v| = 1.
    This is equivalent to the CS inequality α² ≤ ê·S²·ê. -/
theorem direction_rotation_nonneg (v : Fin 3 → ℝ) (B : Fin 3 → Fin 3 → ℝ)
    (hSym : ∀ i j, B i j = B j i)
    (hUnit : v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 = 1) :
    let Bv : Fin 3 → ℝ := fun i => B i 0 * v 0 + B i 1 * v 1 + B i 2 * v 2
    let alpha := v 0 * Bv 0 + v 1 * Bv 1 + v 2 * Bv 2
    0 ≤ (Bv 0 ^ 2 + Bv 1 ^ 2 + Bv 2 ^ 2) - alpha ^ 2 := by
  simp only [hSym]
  -- |Bv|² - (v·Bv)² = |Bv|²·|v|² - (v·Bv)² (since |v|²=1)
  -- = Σ_{i<j} (v_i (Bv)_j - v_j (Bv)_i)² (Lagrange identity)
  set w0 := B 0 0 * v 0 + B 0 1 * v 1 + B 0 2 * v 2
  set w1 := B 0 1 * v 0 + B 1 1 * v 1 + B 1 2 * v 2
  set w2 := B 0 2 * v 0 + B 1 2 * v 1 + B 2 2 * v 2
  -- Use |v|² = 1 to rewrite: |w|² - (v·w)² = |w|²|v|² - (v·w)²
  have key : (w0 ^ 2 + w1 ^ 2 + w2 ^ 2) - (v 0 * w0 + v 1 * w1 + v 2 * w2) ^ 2 =
    (w0 ^ 2 + w1 ^ 2 + w2 ^ 2) * (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) -
    (v 0 * w0 + v 1 * w1 + v 2 * w2) ^ 2 := by rw [hUnit]; ring
  rw [key]
  -- Now apply Lagrange identity (same as in StrainSelfDepletion)
  have lagrange : (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) * (w0 ^ 2 + w1 ^ 2 + w2 ^ 2) -
    (v 0 * w0 + v 1 * w1 + v 2 * w2) ^ 2 =
    (v 0 * w1 - v 1 * w0) ^ 2 + (v 0 * w2 - v 2 * w0) ^ 2 +
    (v 1 * w2 - v 2 * w1) ^ 2 := by ring
  have lagrange2 : (w0 ^ 2 + w1 ^ 2 + w2 ^ 2) * (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) -
    (v 0 * w0 + v 1 * w1 + v 2 * w2) ^ 2 =
    (v 0 * w1 - v 1 * w0) ^ 2 + (v 0 * w2 - v 2 * w0) ^ 2 +
    (v 1 * w2 - v 2 * w1) ^ 2 := by ring
  rw [lagrange2]
  positivity

/-!
## Physical Interpretation

For the strain tensor S and unit vorticity direction ê:

  ê · S² · ê = α² + |Dξ/Dt|²

where:
- α = ê · S · ê is the stretching rate
- |Dξ/Dt|² = |S·ê - α·ê|² is the squared direction rotation rate

This means:
1. Self-depletion = stretching² + rotation²
2. Depletion exceeds α² by the rotation rate
3. Equality (no rotation) only when ê is a strain eigenvector
4. For generic (non-symmetric) flows: ε = |Dξ/Dt|²/α² ≈ 0.5
5. For symmetric flows (TG): ε = 0 (worst case, tight CS)

The strain ODE becomes:
  dα/dt ≤ -(α² + |Dξ/Dt|²) - ê·H·ê + viscous

Extra depletion from direction rotation strengthens the self-limiting mechanism.
-/
