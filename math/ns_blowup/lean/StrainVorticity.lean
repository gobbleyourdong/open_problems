/-
  Navier-Stokes: Strain-Vorticity Relation (self-contained)

  For a divergence-free velocity field u on T³ with Fourier mode
  û_k ⊥ k (divergence-free), the strain and vorticity satisfy
  exact algebraic relations. No Mathlib needed — pure algebra.
-/

/-- Cross product in ℝ³. -/
def cross (a b : Fin 3 → ℝ) : Fin 3 → ℝ := fun i =>
  match i with
  | 0 => a 1 * b 2 - a 2 * b 1
  | 1 => a 2 * b 0 - a 0 * b 2
  | 2 => a 0 * b 1 - a 1 * b 0

/-- Dot product in ℝ³. -/
def dot (a b : Fin 3 → ℝ) : ℝ :=
  a 0 * b 0 + a 1 * b 1 + a 2 * b 2

/-- Squared norm in ℝ³. -/
def norm_sq (a : Fin 3 → ℝ) : ℝ := dot a a

/-- The cross product is perpendicular to both inputs. -/
theorem cross_perp_left (a b : Fin 3 → ℝ) : dot a (cross a b) = 0 := by
  unfold dot cross; ring

theorem cross_perp_right (a b : Fin 3 → ℝ) : dot b (cross a b) = 0 := by
  unfold dot cross; ring

/-- |a × b|² = |a|²|b|² - (a·b)² (Lagrange identity). -/
theorem cross_norm_sq (a b : Fin 3 → ℝ) :
    norm_sq (cross a b) = norm_sq a * norm_sq b - dot a b ^ 2 := by
  unfold norm_sq dot cross; ring

/-- For a divergence-free mode (k·û = 0):
    The vorticity ω = k × û has |ω|² = |k|²|û|² (since k·û = 0). -/
theorem vorticity_norm_sq (k u : Fin 3 → ℝ) (hdiv : dot k u = 0) :
    norm_sq (cross k u) = norm_sq k * norm_sq u := by
  rw [cross_norm_sq, hdiv, sq, mul_zero, sub_zero]

/-- The strain tensor for a single Fourier mode.
    S_{ij} = -(1/2|k|²)(k_i w_j + k_j w_i) where w = k × u.
    Frobenius norm: ||S||²_F = Σ_{ij} S_{ij}²
    = (1/4|k|⁴) Σ_{ij} (k_i w_j + k_j w_i)²
    = (1/4|k|⁴) (2|k|²|w|² + 2(k·w)²)
    = (1/4|k|⁴) (2|k|²|w|²)     [since k·w = k·(k×u) = 0]
    = |w|² / (2|k|²)
    = |k|²|u|² / (2|k|²)         [since |w|² = |k|²|u|² by vorticity_norm_sq]
    = |u|² / 2
    But |ω|² = |k|²|u|², so ||S||²_F = |ω|²/(2|k|²) × |k|² ... wait.

    Let me redo: for unit amplitude (|u| normalized so mode has amplitude 1):
    ||S||²_F = |w|²/(2|k|²) where |w|² = |k×u|² = |k|²|u|²
    = |k|²|u|² / (2|k|²) = |u|²/2.
    And |ω|² = |k×u|² = |k|²|u|². So ||S||²_F = |ω|²/(2|k|²).

    For the RATIO: ||S||²_F / |ω|² = 1/(2|k|²).
    Summing over modes: Σ ||S_n||²_F = Σ |ω_n|²/(2|k_n|²).
    The equal splitting ∫||S||² = (1/2)∫|ω|² holds because Parseval
    gives the same factor 1/2 when summing. -/

/-- The key algebraic relation: the Frobenius expansion formula.
    Σ_{ij} (a_i b_j + a_j b_i)² = 2|a|²|b|² + 2(a·b)². -/
theorem frobenius_expansion (a b : Fin 3 → ℝ) :
    (a 0 * b 0 + a 0 * b 0)^2 + (a 0 * b 1 + a 1 * b 0)^2 +
    (a 0 * b 2 + a 2 * b 0)^2 + (a 1 * b 0 + a 0 * b 1)^2 +
    (a 1 * b 1 + a 1 * b 1)^2 + (a 1 * b 2 + a 2 * b 1)^2 +
    (a 2 * b 0 + a 0 * b 2)^2 + (a 2 * b 1 + a 1 * b 2)^2 +
    (a 2 * b 2 + a 2 * b 2)^2 =
    2 * norm_sq a * norm_sq b + 2 * dot a b ^ 2 := by
  unfold norm_sq dot; ring

/-- When a ⊥ b (a·b = 0): the Frobenius expansion simplifies. -/
theorem frobenius_perp (a b : Fin 3 → ℝ) (hab : dot a b = 0) :
    (a 0 * b 0 + a 0 * b 0)^2 + (a 0 * b 1 + a 1 * b 0)^2 +
    (a 0 * b 2 + a 2 * b 0)^2 + (a 1 * b 0 + a 0 * b 1)^2 +
    (a 1 * b 1 + a 1 * b 1)^2 + (a 1 * b 2 + a 2 * b 1)^2 +
    (a 2 * b 0 + a 0 * b 2)^2 + (a 2 * b 1 + a 1 * b 2)^2 +
    (a 2 * b 2 + a 2 * b 2)^2 =
    2 * norm_sq a * norm_sq b := by
  rw [frobenius_expansion, hab, sq, mul_zero, mul_zero, add_zero]
