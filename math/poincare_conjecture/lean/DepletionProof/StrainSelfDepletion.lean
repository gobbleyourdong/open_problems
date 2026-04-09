/-
  Strain Self-Depletion Lemma

  For any symmetric matrix S and unit vector ê:
    (ê · S · ê)² ≤ ê · S² · ê

  This is Cauchy-Schwarz applied to the spectral decomposition.
  Combined with the strain evolution equation, it gives:
    dα/dt ≤ -α² + (pressure + viscous)

  The stretching rate α is SELF-LIMITING: the quadratic self-depletion
  -ê·S²·ê ≤ -α² always dominates for large α.

  Author: the author, Independent Researcher
  Date: March 2026
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith

/-- Quadratic form: ê · S² · ê = |Sê|² for symmetric S.
    Computed as the squared norm of the matrix-vector product. -/
noncomputable def quadFormSq (a : Fin 3 → ℝ) (B : Fin 3 → Fin 3 → ℝ) : ℝ :=
  let Ba : Fin 3 → ℝ := fun i => B i 0 * a 0 + B i 1 * a 1 + B i 2 * a 2
  Ba 0 ^ 2 + Ba 1 ^ 2 + Ba 2 ^ 2

/-- Quadratic form: ê · S · ê -/
noncomputable def quadForm (a : Fin 3 → ℝ) (B : Fin 3 → Fin 3 → ℝ) : ℝ :=
  a 0 * (B 0 0 * a 0 + B 0 1 * a 1 + B 0 2 * a 2) +
  a 1 * (B 1 0 * a 0 + B 1 1 * a 1 + B 1 2 * a 2) +
  a 2 * (B 2 0 * a 0 + B 2 1 * a 1 + B 2 2 * a 2)

/-- **Strain Self-Depletion (Cauchy-Schwarz form).**

    For any symmetric matrix B and vector a:
      (a · B · a)² ≤ |a|² × (a · B² · a)

    When |a| = 1 (unit vector ê):
      α² ≤ ê · S² · ê

    Proof: quadForm a B = a · (Ba) and quadFormSq a B = |Ba|².
    By CS: (a · Ba)² ≤ |a|² |Ba|².

    Equivalently: 0 ≤ |a|²|Ba|² - (a·Ba)² = Σᵢ<ⱼ (aᵢ(Ba)ⱼ - aⱼ(Ba)ᵢ)² -/
theorem strain_self_depletion (a : Fin 3 → ℝ) (B : Fin 3 → Fin 3 → ℝ)
    (hSym : ∀ i j, B i j = B j i) :
    (quadForm a B) ^ 2 ≤
    (a 0 ^ 2 + a 1 ^ 2 + a 2 ^ 2) * quadFormSq a B := by
  unfold quadForm quadFormSq
  simp only [hSym]
  -- The Cauchy-Schwarz inequality (a·v)² ≤ |a|²|v|² where v = Ba.
  -- Equivalent to: |a|²|v|² - (a·v)² = Σᵢ<ⱼ (aᵢvⱼ - aⱼvᵢ)² ≥ 0
  -- We prove the difference is a sum of squares.
  set v0 := B 0 0 * a 0 + B 0 1 * a 1 + B 0 2 * a 2
  set v1 := B 0 1 * a 0 + B 1 1 * a 1 + B 1 2 * a 2
  set v2 := B 0 2 * a 0 + B 1 2 * a 1 + B 2 2 * a 2
  -- Now LHS = (a 0 * v0 + a 1 * v1 + a 2 * v2)²
  -- RHS = (a 0² + a 1² + a 2²) * (v0² + v1² + v2²)
  -- RHS - LHS = (a0*v1 - a1*v0)² + (a0*v2 - a2*v0)² + (a1*v2 - a2*v1)²
  -- RHS - LHS = (a0*v1 - a1*v0)² + (a0*v2 - a2*v0)² + (a1*v2 - a2*v1)²
  -- Suffices to show: LHS + sum_of_squares = RHS, then LHS ≤ RHS.
  have h1 : 0 ≤ (a 0 * v1 - a 1 * v0) ^ 2 := sq_nonneg _
  have h2 : 0 ≤ (a 0 * v2 - a 2 * v0) ^ 2 := sq_nonneg _
  have h3 : 0 ≤ (a 1 * v2 - a 2 * v1) ^ 2 := sq_nonneg _
  -- The key algebraic identity: expanding everything shows
  -- (a0²+a1²+a2²)(v0²+v1²+v2²) - (a0v0+a1v1+a2v2)²
  --   = (a0v1-a1v0)² + (a0v2-a2v0)² + (a1v2-a2v1)²
  -- So RHS - LHS ≥ 0.
  have key : (a 0 ^ 2 + a 1 ^ 2 + a 2 ^ 2) * (v0 * v0 + v1 * v1 + v2 * v2) -
    (a 0 * v0 + a 1 * v1 + a 2 * v2) ^ 2 =
    (a 0 * v1 - a 1 * v0) ^ 2 + (a 0 * v2 - a 2 * v0) ^ 2 +
    (a 1 * v2 - a 2 * v1) ^ 2 := by ring
  -- Lagrange identity rearranged: (a·v)² + cross_terms = |a|²|v|²
  have lagrange : (a 0 * v0 + a 1 * v1 + a 2 * v2) ^ 2 +
    ((a 0 * v1 - a 1 * v0) ^ 2 + (a 0 * v2 - a 2 * v0) ^ 2 +
    (a 1 * v2 - a 2 * v1) ^ 2) =
    (a 0 ^ 2 + a 1 ^ 2 + a 2 ^ 2) * (v0 ^ 2 + v1 ^ 2 + v2 ^ 2) := by ring
  -- The cross terms are ≥ 0 (sum of squares)
  have nonneg : 0 ≤ (a 0 * v1 - a 1 * v0) ^ 2 + (a 0 * v2 - a 2 * v0) ^ 2 +
    (a 1 * v2 - a 2 * v1) ^ 2 := by positivity
  -- LHS + (nonneg thing) = RHS → LHS ≤ RHS
  linarith

/-!
## What This Means for the Proof

The strain evolution at the vorticity maximum x* gives:

  dα/dt = -(ê · S² · ê) - ê · H · ê + ν(ê · ΔS · ê)

where H is the pressure Hessian. By the inequality above:

  -(ê · S² · ê) ≤ -α²     (since |ê| = 1)

Therefore:

  dα/dt ≤ -α² - ê · H · ê + ν(ê · ΔS · ê)

The -α² term makes the stretching rate SELF-LIMITING.
For large α, the self-depletion dominates and forces α to decrease.

Combined with:
- Buaria & Pumir (2023): pressure Hessian opposes stretching at high ω
- Single-mode orthogonality: structural cancellations in Biot-Savart

this constrains the dynamics to prevent sustained stretching at x*.
-/
