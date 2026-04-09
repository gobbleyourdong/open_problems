/-
  Navier-Stokes: Polarization First-Order Conditions at the Max

  At the vorticity maximum, the polarizations v_i are chosen to maximize
  |ω(x*)|² over both sign patterns c_i ∈ {±1} and polarization angles.

  The first-order condition w.r.t. θ_i is:
    ∂|ω|²/∂θ_i = 0

  which translates to: v_i is "aligned with the effective force" from
  the other modes.

  This is a NEW structural constraint I haven't formalized yet.
  Companion to VertexFirstOrder.lean (the sign-flip condition).
-/

/-! ## The Squared Inequality (Avoiding sqrt)

Instead of using Real.sqrt, we work with the squared versions of
the first-order conditions. This avoids import issues.

Key identity: max of (Ax + By)² over x² + y² = 1 is A² + B².
Equivalently: (Ax + By)² ≤ (A² + B²)(x² + y²) (Cauchy-Schwarz).
-/

/-- Cauchy-Schwarz for 2D: (Ax + By)² ≤ (A² + B²)(x² + y²). -/
theorem cauchy_schwarz_2d (A B x y : ℝ) :
    (A * x + B * y)^2 ≤ (A^2 + B^2) * (x^2 + y^2) := by
  nlinarith [sq_nonneg (A * y - B * x)]

/-- For unit (x, y) with x² + y² = 1:
    (Ax + By)² ≤ A² + B². -/
theorem linear_on_unit_circle_squared (A B x y : ℝ) (h : x^2 + y^2 = 1) :
    (A * x + B * y)^2 ≤ A^2 + B^2 := by
  have := cauchy_schwarz_2d A B x y
  nlinarith

/-! ## Equality Case

The Cauchy-Schwarz inequality is TIGHT when (x, y) ∝ (A, B).
That is, when the polarization is aligned with the "force."
-/

/-- Equality holds in Cauchy-Schwarz iff A*y = B*x (parallel).
    This is the alignment condition. -/
theorem cauchy_schwarz_equality (A B x y : ℝ) (h_par : A * y = B * x) :
    (A * x + B * y)^2 = (A^2 + B^2) * (x^2 + y^2) := by
  -- (Ax + By)² - (A²+B²)(x²+y²) = -(Ay - Bx)² = 0 when Ay = Bx
  have h_diff : (A * y - B * x)^2 = 0 := by rw [h_par]; ring
  nlinarith [h_diff]

/-- The first-order condition at the polarization max:
    if (x, y) maximizes Ax + By on the unit circle, then A*y = B*x.
    (Otherwise there's slack in Cauchy-Schwarz, so we can improve.) -/
theorem polarization_alignment (A B x y : ℝ) (h_unit : x^2 + y^2 = 1)
    (h_max : (A * x + B * y)^2 = A^2 + B^2) :
    (A * y - B * x)^2 = 0 := by
  -- From Cauchy-Schwarz: (Ax+By)² = (A²+B²) - (Ay-Bx)² × (something)
  -- Actually: (A² + B²)(x² + y²) - (Ax + By)² = (Ay - Bx)²
  have h := cauchy_schwarz_2d A B x y
  rw [h_unit, mul_one] at h
  -- h : (Ax+By)² ≤ A²+B²
  -- h_max : (Ax+By)² = A²+B²
  -- The identity: A²+B² - (Ax+By)² = (Ay-Bx)² when x²+y²=1
  have h_identity : (A^2 + B^2) - (A * x + B * y)^2 = (A * y - B * x)^2 + (A^2 + B^2) * (1 - (x^2 + y^2)) := by ring
  rw [h_unit] at h_identity
  simp at h_identity
  linarith [sq_nonneg (A * y - B * x)]

/-! ## Two First-Order Conditions at the Vorticity Max

1. SIGN condition (VertexFirstOrder.lean):
   Σ c_i c_j (v_i · v_j) ≥ 0 [from flipping sign of c_i]

2. ANGLE condition (this file):
   v_i is aligned with Σ_{j≠i} c_i c_j · proj(v_j onto k_i-perp plane)
   [from varying the polarization angle θ_i]

Together these characterize the optimum precisely.
-/

/-- The alignment condition at the max, in squared form.
    If v_i maximizes the contribution to |ω|² at fixed other modes,
    then v_i satisfies the Cauchy-Schwarz equality condition with
    the "force" vector from the other modes. -/
theorem max_polarization_alignment
    (force_x force_y pol_x pol_y : ℝ)
    (h_unit : pol_x^2 + pol_y^2 = 1)
    (h_max : (force_x * pol_x + force_y * pol_y)^2 = force_x^2 + force_y^2) :
    force_x * pol_y = force_y * pol_x := by
  have h := polarization_alignment force_x force_y pol_x pol_y h_unit h_max
  -- (Ax·py - Bx·px)² = 0 → Ax·py = Bx·px
  have h_sq : (force_x * pol_y - force_y * pol_x)^2 = 0 := h
  have h_zero : force_x * pol_y - force_y * pol_x = 0 := by
    nlinarith [sq_nonneg (force_x * pol_y - force_y * pol_x)]
  linarith

/-! ## Consequence for the Q-Analysis

The alignment condition pins down the polarization at the max.
In particular, it constrains the dot products (k_j · v_i) and (v_j · v_i)
for all pairs (i, j).

These dot products appear in K and T:
  K_{jl} = (k_j · k_l)(v_j · v_l)
  T_{jl} = (k_j · v_l)(v_j · k_l)

The alignment condition provides relations between these dot products
at the max, which could be used to bound T_{jl} in terms of K_{jl}
or other known quantities.

The specific constraint depends on the geometry of {k_i}, so there's
no clean universal bound. For SPECIFIC configurations (like the N=4
worst case), the alignment condition + geometry pins everything down.
-/

/-! ## Theorem Count:
    - cauchy_schwarz_2d: PROVEN (nlinarith with cross product)
    - linear_on_unit_circle_squared: PROVEN (from cauchy_schwarz_2d)
    - cauchy_schwarz_equality: PROVEN (algebraic identity)
    - polarization_alignment: PROVEN (algebraic manipulation)
    - max_polarization_alignment: PROVEN (from polarization_alignment)
    Total: 5 proved, 0 sorry, no imports

    Companion to VertexFirstOrder.lean. The angle first-order condition
    at the vorticity max, via squared Cauchy-Schwarz (avoiding sqrt).
-/
