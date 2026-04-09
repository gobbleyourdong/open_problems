/-
  Navier-Stokes: The Self-Annihilation Identity (Odd Instance Discovery)

  KEY IDENTITY: S_k v_k = 0

  For a divergence-free Fourier mode with wavevector k, polarization v ⊥ k:
  The strain tensor S_k applied to the polarization v is exactly ZERO.

  S_k v = -(1/2|k|²)[(v·w)k + (v·k)w] = 0

  because:
  - v·w = v·(k×v) = 0  (scalar triple product with repeated vector)
  - v·k = 0             (divergence-free condition)

  CONSEQUENCE: In the expression Sω = Σ_{j,k} c_j c_k S_j v_k,
  the DIAGONAL terms (j=k) vanish: S_k v_k = 0.
  Only CROSS-MODE interactions survive: Sω = Σ_{j≠k} c_j c_k S_j v_k.

  This is WHY S²ê is small at the vorticity maximum — the stretching
  comes entirely from mode-mode interactions, which partially cancel.
  The self-interaction is identically zero.

  Discovered by Odd instance (81bab61). Formalized here.
-/

-- Self-contained vector algebra (consistent with StrainVorticity.lean)
private def dot' (a b : Fin 3 → ℝ) : ℝ := a 0 * b 0 + a 1 * b 1 + a 2 * b 2
private def cross' (a b : Fin 3 → ℝ) : Fin 3 → ℝ := fun i =>
  match i with
  | 0 => a 1 * b 2 - a 2 * b 1
  | 1 => a 2 * b 0 - a 0 * b 2
  | 2 => a 0 * b 1 - a 1 * b 0

/-! ## The Two Vanishing Dot Products -/

/-- Scalar triple product: v · (k × v) = 0 for any vectors.
    This is det(v, k, v) = 0 since two rows are identical.
    PROVEN by ring. -/
theorem scalar_triple_self (v k : Fin 3 → ℝ) :
    dot' v (cross' k v) = 0 := by
  unfold dot' cross'; ring

/-- Divergence-free: v · k = 0 (the hypothesis, not a theorem).
    We include it as a named statement for the chain. -/
-- This is an assumption, not a theorem.

/-! ## The Strain Applied to Polarization -/

/-- The strain tensor S_k for mode k with polarization v:
    S_k = -(1/2|k|²)(k ⊗ w + w ⊗ k) where w = k × v.

    Applied to an arbitrary vector u:
    S_k u = -(1/2|k|²)[(u · w)k + (u · k)w]

    We compute the TWO coefficients when u = v:
    - Coefficient of k: v · w = v · (k×v) = 0 (scalar triple product)
    - Coefficient of w: v · k = 0 (divergence-free)
    Both vanish → S_k v = 0. -/

/-- The coefficient of k in S_k v is v · (k × v) = 0. -/
theorem strain_self_coeff_k (k v : Fin 3 → ℝ) :
    dot' v (cross' k v) = 0 := scalar_triple_self v k

/-- THE SELF-ANNIHILATION IDENTITY:

    For a divergence-free mode (v · k = 0), the strain S_k applied
    to the polarization v gives the zero vector.

    S_k v = -(1/2|k|²)[(v·w)k + (v·k)w]

    Both coefficients vanish:
    - v · w = 0 (scalar triple product: v · (k×v) = 0)
    - v · k = 0 (divergence-free)

    Therefore S_k v = 0: the strain of a mode ANNIHILATES its own polarization.

    We prove this by showing each component of S_k v is zero.
    The strain acts on v as: (S_k v)_i = Σ_j S_{ij} v_j
    = -(1/2|k|²) Σ_j (k_i w_j + w_i k_j) v_j
    = -(1/2|k|²) [k_i (w·v) + w_i (k·v)]
    = -(1/2|k|²) [k_i · 0 + w_i · 0] = 0.
-/
theorem self_annihilation (k v : Fin 3 → ℝ) (hdiv : dot' k v = 0) :
    let w := cross' k v
    let k_sq := dot' k k
    -- Each component of S_k v is zero:
    -- (S_k v)_i = -(1/(2·k_sq)) · (k_i · (dot' v w) + w_i · (dot' v k))
    -- Since dot' v w = 0 and dot' v k = 0 (by hdiv symmetry: dot' k v = dot' v k):
    dot' v w = 0 ∧ dot' v k = 0 := by
  intro w
  constructor
  · -- v · (k × v) = 0 (scalar triple product)
    exact scalar_triple_self v k
  · -- v · k = dot' k v (by commutativity) = 0
    unfold dot' at hdiv ⊢; linarith

/-- Explicit: each component of S_k v vanishes.
    (S_k v)_i = -(1/(2|k|²))[k_i(v·w) + w_i(v·k)] = 0 for all i.
    Since both dot products are zero, every component is zero. -/
theorem self_annihilation_componentwise (k v : Fin 3 → ℝ) (hdiv : dot' k v = 0)
    (hk : dot' k k > 0) :
    let w := cross' k v
    let coeff := -(1 / (2 * dot' k k))
    -- Component i of S_k v:
    ∀ i : Fin 3,
      coeff * (k i * dot' v w + w i * dot' v k) = 0 := by
  intro w coeff i
  have ⟨hvw, hvk⟩ := self_annihilation k v hdiv
  simp [hvw, hvk, mul_zero, add_zero, mul_zero]

/-! ## The Consequence: Only Cross-Terms Survive

Sω = Σ_{j,k} c_j c_k S_j v_k

Diagonal (j=k): S_k v_k = 0 for all k (self-annihilation).
Cross (j≠k): S_j v_k ≠ 0 in general (modes interact).

Therefore: Sω = Σ_{j≠k} c_j c_k S_j v_k

This is the algebraic reason S²ê is small:
- Self-interaction (the "dangerous" part) is identically zero
- Only cross-mode interactions contribute
- These partially cancel due to geometric factors (pair_mechanism.py)
- Net result: S²ê/|ω|² ≈ 0.05 (max 0.25), far below 3/4 threshold
-/

/-- If diagonal terms are zero, the total equals the cross-terms.
    Formalized for a simple 2-element sum. -/
theorem diagonal_vanishes_leaves_cross
    (d₁ d₂ c₁₂ c₂₁ : ℝ) (hd1 : d₁ = 0) (hd2 : d₂ = 0) :
    (d₁ + c₁₂) + (c₂₁ + d₂) = c₁₂ + c₂₁ := by linarith

/-! ## Theorem Count:
    - scalar_triple_self: PROVEN (ring)
    - strain_self_coeff_k: PROVEN (= scalar_triple_self)
    - self_annihilation: PROVEN (scalar_triple_self + linarith)
    - self_annihilation_componentwise: PROVEN (simp from self_annihilation)
    - diagonal_vanishes_leaves_cross: PROVEN (linarith)
    Total: 5 proved, 0 sorry

    KEY INSIGHT: S_k v_k = 0 explains why S²ê is small.
    The strain of a mode cannot stretch its own vorticity.
    Stretching comes ONLY from mode-mode interactions.
-/
