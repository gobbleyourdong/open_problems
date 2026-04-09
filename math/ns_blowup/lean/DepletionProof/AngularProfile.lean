/-
  Angular Profile of the NS Bilinear Symbol

  The key trigonometric identity underlying the Schur test bound θ₀ = 2/3:

    cos(α/2) * cos(α) + sin(α/2) * sin(α) = cos(α/2)

  This identity determines the operator norm of the restricted bilinear
  symbol P_ξ · Ŝ(ξ-η) · P_η to be exactly cos(α/2)/2, where α is the
  angle between wavevectors ξ and η.

  The proof uses standard double-angle formulas:
    cos(α) = cos²(α/2) - sin²(α/2)
    sin(α) = 2 sin(α/2) cos(α/2)

  Author: the author, Independent Researcher
  Date: March 2026
-/

import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

open Real

/-- **The Key Identity.**
  cos(α/2) * cos(α) + sin(α/2) * sin(α) = cos(α/2)

  This determines the angular profile f(α) = cos(α/2)/2 of the
  NS bilinear symbol, which yields the Schur test bound θ₀ = 2/3. -/
theorem angular_profile_identity (α : ℝ) :
    cos (α / 2) * cos α + sin (α / 2) * sin α = cos (α / 2) := by
  -- Use double-angle formulas: cos α = 2cos²(α/2) - 1, sin α = 2sin(α/2)cos(α/2)
  have hcos : cos α = 2 * cos (α / 2) ^ 2 - 1 := by
    have : α = 2 * (α / 2) := by ring
    rw [this, cos_two_mul]
    ring
  have hsin : sin α = 2 * sin (α / 2) * cos (α / 2) := by
    have : α = 2 * (α / 2) := by ring
    rw [this, sin_two_mul]
  rw [hcos, hsin]
  ring

/-- **Corollary.** The angular profile satisfies the factored form. -/
theorem angular_profile_factored (α : ℝ) :
    cos (α / 2) * cos α + sin (α / 2) * sin α =
    cos (α / 2) * (cos (α / 2) ^ 2 + sin (α / 2) ^ 2) := by
  have := angular_profile_identity α
  rw [sin_sq_add_cos_sq (α / 2), mul_one] at *
  linarith

/-- **Direct algebraic proof** using cos²+sin²=1. -/
theorem angular_profile_algebraic (c s : ℝ) (hpyth : c ^ 2 + s ^ 2 = 1) :
    c * (c ^ 2 - s ^ 2) + s * (2 * s * c) = c := by
  nlinarith [sq_nonneg c, sq_nonneg s]

/-- **Antipodal Vanishing (algebraic core).**
  When the strain wavevector q is parallel to the projection direction k,
  the projected strain quadratic form vanishes. This is because:
  - The strain Ŝ(q) with q ∥ k has entries only in the k-row and k-column
  - The projection P_k = I - k̂⊗k̂ kills both the k-row and k-column
  - Therefore P_k · Ŝ(q) · P_k = 0

  Algebraically: for the strain form with q = k and û = k × ω̂ / |k|²,
  the quadratic form ω̂ · Ŝ · ω̂ = 0 for any ω̂ ⊥ k (div-free).
  This follows directly from single_mode_orthogonality when p = k
  (the strain mode equals the vorticity mode wavevector).

  In the bilinear symbol context: M(ξ̂, -ξ̂) = 0 because the strain
  mode q = ξ - (-ξ) = 2ξ is parallel to ξ, reducing to the single-mode case.
-/
theorem antipodal_vanishing (k ω : Fin 3 → R) :
    twiceStrainForm ω k (k ⨯₃ ω) = 0 :=
  single_mode_orthogonality_unconditional k ω

/-!
## Context

The angular profile f(α) = cos(α/2)/2 arises as the operator norm of
the restricted bilinear Biot-Savart symbol:

  ||P_ξ · Ŝ(ξ-η) · P_η||_op = cos(α/2) / 2

where α = ∠(ξ̂, η̂) and P_k = I - k̂⊗k̂ is the div-free projection.

The Schur test then gives:
  θ₀ = I / (4π × max_f) = (4π/3) / (2π) = 2/3

where I = 2π ∫₀^π cos²(α/2) sin(α/2) dα = 4π/3.

The identity `angular_profile_identity` is the key step in deriving
f(α) = cos(α/2)/2 from the explicit strain symbol computation.

### What this proves
- The factorization that determines the angular profile
- Verified for the algebraic core (c, s with c²+s²=1)

### What this does NOT prove
- The Schur integral I = 4π/3 (needs Mathlib integration theory)
- The Schur test bound (needs operator theory)
- NS regularity (needs the full proof architecture)
-/

/-- **Strain form symmetry.** The twice-strain form is symmetric in p and q.
    This is because S = (p⊗q + q⊗p)/2 is symmetric. -/
theorem twiceStrainForm_comm (a p q : Fin 3 → R) :
    twiceStrainForm a p q = twiceStrainForm a q p := by
  simp only [twiceStrainForm]
  ring

/-- **Strain form bilinearity in the first argument.**
    twiceStrainForm (c • a) p q = c² • twiceStrainForm a p q -/
theorem twiceStrainForm_smul_left (a p q : Fin 3 → R) (c : R) :
    twiceStrainForm (fun i => c * a i) p q = c * c * twiceStrainForm a p q := by
  simp only [twiceStrainForm]
  ring

/-- **The strain form vanishes when a ⊥ p AND a ⊥ q.**
    If a · p = 0 and a · q = 0, then twiceStrainForm a p q = 0.
    This follows from the factorization: 2(a·p)(a·q) = 0. -/
theorem twiceStrainForm_perp (a p q : Fin 3 → R)
    (hp : a ⬝ᵥ p = 0) (hq : a ⬝ᵥ q = 0) :
    twiceStrainForm a p q = 0 := by
  rw [twiceStrainForm_eq]
  rw [hp, hq]
  ring

/-- **Strain form Cauchy-Schwarz.** The factored form gives a natural bound:
    |twiceStrainForm a p q| ≤ 2 |a·p| |a·q| ≤ 2 |a|² |p| |q|
    Here we prove the factored equality which is the algebraic basis. -/
theorem twiceStrainForm_eq_two_dot (a p q : Fin 3 → R) :
    twiceStrainForm a p q = 2 * (a ⬝ᵥ p) * (a ⬝ᵥ q) :=
  twiceStrainForm_eq a p q

/-- **Cross product orthogonality restated.**
    For any k, ω: ω · (k × ω) = 0. This is dot_cross_self from Mathlib.
    Included here for completeness of the depletion theory. -/
theorem vorticity_velocity_orthogonal (k ω : Fin 3 → R) :
    ω ⬝ᵥ (k ⨯₃ ω) = 0 :=
  dot_cross_self k ω

/-- **Strain form additivity in the second argument.**
    twiceStrainForm a p (q₁ + q₂) = twiceStrainForm a p q₁ + twiceStrainForm a p q₂
    This is multi-mode decomposition: the strain from multiple modes adds linearly. -/
theorem twiceStrainForm_add_right (a p q₁ q₂ : Fin 3 → R) :
    twiceStrainForm a p (fun i => q₁ i + q₂ i) =
    twiceStrainForm a p q₁ + twiceStrainForm a p q₂ := by
  simp only [twiceStrainForm]
  ring

/-- **Multi-mode decomposition.**
    The strain form from a sum of velocities decomposes into a sum of individual
    contributions. This is the algebraic basis for the shell-by-shell analysis:
    T(j) = Σ_{j'} T(j,j'), where each T(j,j') involves the strain from shell j'. -/
theorem twiceStrainForm_add_third (a p₁ p₂ q : Fin 3 → R) :
    twiceStrainForm a (fun i => p₁ i + p₂ i) q =
    twiceStrainForm a p₁ q + twiceStrainForm a p₂ q := by
  simp only [twiceStrainForm]
  ring

/-- **Strain form sign from dot products.**
    The sign of the strain form is determined by the signs of a·p and a·q.
    If a·p and a·q have the same sign → strain form ≥ 0 (stretching).
    If a·p and a·q have opposite signs → strain form ≤ 0 (compression).
    This is the algebraic root of why the resonant region can be compressive. -/
theorem twiceStrainForm_nonneg_of_dots_same_sign (a p q : Fin 3 → R)
    (hp : 0 ≤ a ⬝ᵥ p) (hq : 0 ≤ a ⬝ᵥ q) :
    0 ≤ twiceStrainForm a p q := by
  rw [twiceStrainForm_eq]
  apply mul_nonneg
  · apply mul_nonneg
    · exact two_nonneg
    · exact hp
  · exact hq

/-- **Strain form nonpositive when dot products have opposite signs.**
    This is the COMPRESSIVE case — the algebraic mechanism behind
    the resonant sign flip at high vorticity intensity. -/
theorem twiceStrainForm_nonpos_of_dots_opposite (a p q : Fin 3 → R)
    (hp : 0 ≤ a ⬝ᵥ p) (hq : a ⬝ᵥ q ≤ 0) :
    twiceStrainForm a p q ≤ 0 := by
  rw [twiceStrainForm_eq]
  apply mul_nonpos_of_nonneg_of_nonpos
  · apply mul_nonneg
    · exact two_nonneg
    · exact hp
  · exact hq

/-- **Strain form absolute bound.**
    |twiceStrainForm a p q| = 2 |a·p| |a·q|.
    Combined with Cauchy-Schwarz |a·p| ≤ |a||p|, this gives
    |twiceStrainForm| ≤ 2|a|²|p||q| (the dimensional worst case).
    The depletion θ₀ = 2/3 < 1 comes from the angular averaging
    on S² being strictly less than this worst case. -/
theorem twiceStrainForm_abs_eq (a p q : Fin 3 → ℝ) :
    |twiceStrainForm a p q| = 2 * |a ⬝ᵥ p| * |a ⬝ᵥ q| := by
  rw [twiceStrainForm_eq]
  rw [abs_mul, abs_mul]
  congr 1
  exact abs_of_nonneg two_nonneg
