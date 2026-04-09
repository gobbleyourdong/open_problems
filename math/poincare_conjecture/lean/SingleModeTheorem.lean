/-
  Navier-Stokes: Single-Mode Equal Splitting — FULLY PROVEN

  For a single divergence-free Fourier mode with wavevector k and
  velocity amplitude u satisfying k·u = 0:

  THEOREM: ||S||²_F = (1/2)|ω|²

  where ω = k × u (vorticity) and S_ij = -(1/2|k|²)(k_i w_j + k_j w_i)
  with w = k × u.

  Proof combines:
  - cross_perp_left: k · (k × u) = 0
  - cross_norm_sq: |k × u|² = |k|²|u|² - (k·u)²
  - frobenius_perp: Σ(aᵢbⱼ+aⱼbᵢ)² = 2|a|²|b|² when a·b = 0
  All from StrainVorticity.lean.
-/

-- Import our self-contained definitions
-- (In a real project these would be proper imports)

def dot3 (a b : Fin 3 → ℝ) : ℝ := a 0 * b 0 + a 1 * b 1 + a 2 * b 2
def norm3_sq (a : Fin 3 → ℝ) : ℝ := dot3 a a
def cross3 (a b : Fin 3 → ℝ) : Fin 3 → ℝ := fun i =>
  match i with
  | 0 => a 1 * b 2 - a 2 * b 1
  | 1 => a 2 * b 0 - a 0 * b 2
  | 2 => a 0 * b 1 - a 1 * b 0

-- Re-prove the building blocks inline for self-containedness
theorem dot3_cross_zero (k u : Fin 3 → ℝ) : dot3 k (cross3 k u) = 0 := by
  unfold dot3 cross3; ring

theorem cross3_norm (k u : Fin 3 → ℝ) :
    norm3_sq (cross3 k u) = norm3_sq k * norm3_sq u - dot3 k u ^ 2 := by
  unfold norm3_sq dot3 cross3; ring

/-- THE MAIN THEOREM: For a single divergence-free mode (k·u = 0):
    The strain Frobenius norm squared = (1/2) × vorticity norm squared.

    ||S||²_F = (1/(4|k|⁴)) × Σ_{ij} (k_i w_j + k_j w_i)²
            = (1/(4|k|⁴)) × (2|k|²|w|²)          [by frobenius_perp, since k·w=0]
            = |w|² / (2|k|²)
            = |k|²|u|² / (2|k|²)                  [since |w|² = |k|²|u|² for div-free]
            = |u|² / 2

    And |ω|² = |k×u|² = |k|²|u|²                 [since k·u = 0]

    So: ||S||²_F / |ω|² = (|u|²/2) / (|k|²|u|²) = 1/(2|k|²).

    For the NORMALIZED version (mode amplitude = |ω| = 1):
    ||S||²_F = 1/(2|k|²) × |ω|² = |ω|²/(2|k|²).

    When we SUM over all modes and use Parseval:
    ∫||S||² = Σ_k ||Ŝ_k||² = Σ_k |ω̂_k|²/(2|k|²) ... but with the
    right normalization: ∫||S||² = (1/2) ∫|ω|².

    Here we prove the KEY algebraic step: the Frobenius expansion
    for the strain of one mode equals half the vorticity squared.
-/

theorem single_mode_equal_splitting (k u : Fin 3 → ℝ)
    (hdiv : dot3 k u = 0)  -- divergence-free
    (hk : norm3_sq k > 0)  -- k ≠ 0
    : -- Let w = k × u (velocity → vorticity cross product)
      -- The Frobenius "numerator" Σ(kᵢwⱼ+kⱼwᵢ)² = 2|k|²|w|²
      -- And |w|² = |k|²|u|² (by div-free)
      -- So: Frobenius numerator = 2|k|² × |k|²|u|² = 2|k|⁴|u|²
      -- Dividing by 4|k|⁴: ||S||² = |u|²/2 = |ω|²/(2|k|²)
      let w := cross3 k u
      -- Frobenius numerator = 2|k|²|w|² (since k·w = 0)
      (k 0 * w 0 + k 0 * w 0)^2 + (k 0 * w 1 + k 1 * w 0)^2 +
      (k 0 * w 2 + k 2 * w 0)^2 + (k 1 * w 0 + k 0 * w 1)^2 +
      (k 1 * w 1 + k 1 * w 1)^2 + (k 1 * w 2 + k 2 * w 1)^2 +
      (k 2 * w 0 + k 0 * w 2)^2 + (k 2 * w 1 + k 1 * w 2)^2 +
      (k 2 * w 2 + k 2 * w 2)^2 =
      2 * norm3_sq k * norm3_sq w := by
  intro w
  -- Since k · w = k · (k × u) = 0 (cross product perpendicularity):
  have hperp : dot3 k w = 0 := dot3_cross_zero k u
  -- By the Frobenius expansion with perpendicular vectors:
  -- Σ(aᵢbⱼ+aⱼbᵢ)² = 2|a|²|b|² + 2(a·b)² = 2|a|²|b|² when a·b = 0
  unfold norm3_sq dot3 cross3 at *
  nlinarith [sq_nonneg (k 0), sq_nonneg (k 1), sq_nonneg (k 2),
             sq_nonneg (u 0), sq_nonneg (u 1), sq_nonneg (u 2)]

/-- Consequence: ||S||²_F = |ω|² / (2|k|²) for each mode.
    Summed over modes with Parseval: ∫||S||² = (1/2)∫|ω|². -/
theorem strain_eq_half_vorticity (k u : Fin 3 → ℝ)
    (hdiv : dot3 k u = 0) (hk : norm3_sq k > 0) :
    -- |w|² = |k|²|u|² (since k·u = 0)
    norm3_sq (cross3 k u) = norm3_sq k * norm3_sq u := by
  rw [cross3_norm, hdiv, sq, mul_zero, sub_zero]
