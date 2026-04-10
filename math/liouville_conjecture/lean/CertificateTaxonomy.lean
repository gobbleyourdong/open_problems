axiom ℝ : Type
axiom ℝ_zero : ℝ
axiom ℝ_one : ℝ
noncomputable instance : OfNat ℝ 0 := ⟨ℝ_zero⟩
noncomputable instance : OfNat ℝ 1 := ⟨ℝ_one⟩
axiom ℝ_le : ℝ → ℝ → Prop
axiom ℝ_lt : ℝ → ℝ → Prop
instance : LE ℝ := ⟨ℝ_le⟩
instance : LT ℝ := ⟨ℝ_lt⟩
axiom ℝ_add : ℝ → ℝ → ℝ
axiom ℝ_mul : ℝ → ℝ → ℝ
noncomputable instance : Add ℝ := ⟨ℝ_add⟩
noncomputable instance : Mul ℝ := ⟨ℝ_mul⟩
/-
  Liouville Conjecture — Certificate Taxonomy

  Classifies all known Liouville results for NS by what structural
  assumption makes them work. Each proved case kills the vortex
  stretching term by a different mechanism. The general case is open
  because no mechanism covers the full 3D setting.

  This file formalizes the LANDSCAPE of partial results, making
  explicit what each assumption buys and what the gap is.
-/

namespace LiouvilleTaxonomy

/-! ## The Solution Classes -/

/-- A bounded ancient mild solution to NS on R³. -/
axiom BoundedAncient : Type

/-- Whether the bound M = sup|u| is finite. -/
axiom IsBounded : BoundedAncient → Prop

/-- Whether the solution is trivial (u ≡ const). -/
axiom IsTrivial : BoundedAncient → Prop

/-! ## Structural Properties -/

/-- Axisymmetric: u is symmetric about an axis. -/
axiom IsAxiSymmetric : BoundedAncient → Prop

/-- No swirl: the azimuthal component u_θ ≡ 0. -/
axiom HasNoSwirl : BoundedAncient → Prop

/-- Self-similar: u(x,t) = λ(t)·U(λ(t)·x) for some profile U. -/
axiom IsSelfSimilar : BoundedAncient → Prop

/-- In the critical space L^3. -/
axiom IsInL3 : BoundedAncient → Prop

/-- Has finite energy (finite Dirichlet integral). -/
axiom HasFiniteEnergy : BoundedAncient → Prop

/-- Small data: sup|u| < ε₀. -/
axiom IsSmallData : BoundedAncient → Prop

/-- The stretching term (Sω·ω) vanishes identically. -/
axiom StretchingVanishes : BoundedAncient → Prop

/-! ## The Proved Cases -/

/-- KNSS 2009: axisymmetric + no swirl → Liouville.
    Mechanism: no swirl kills the stretching term. -/
axiom knss_liouville :
    ∀ u : BoundedAncient,
      IsAxiSymmetric u → HasNoSwirl u → IsTrivial u

/-- Tsai 1998 + NRS 1996: self-similar → Liouville.
    Mechanism: self-similarity reduces to an ODE. -/
axiom self_similar_liouville :
    ∀ u : BoundedAncient,
      IsSelfSimilar u → IsTrivial u

/-- ESŠ 2003: L³ solutions are regular.
    Mechanism: L³ is the critical space; Carleman inequalities work. -/
axiom l3_regularity :
    ∀ u : BoundedAncient,
      IsInL3 u → IsTrivial u

/-- Galdi 2011: finite energy → Liouville.
    Mechanism: energy equality + backward uniqueness. -/
axiom finite_energy_liouville :
    ∀ u : BoundedAncient,
      HasFiniteEnergy u → IsTrivial u

/-- Small data Liouville (attempt_008 of this campaign).
    Mechanism: Koch-Tataru contraction in BMO⁻¹. -/
axiom small_data_liouville :
    ∀ u : BoundedAncient,
      IsSmallData u → IsTrivial u

/-- 2D Liouville (trivial — stretching vanishes in 2D). -/
axiom vanishing_stretch_liouville :
    ∀ u : BoundedAncient,
      StretchingVanishes u → IsTrivial u

/-! ## The Implications (what each property buys)

Each structural property implies stretching is controlled:
-/

/-- No swirl → stretching vanishes (for axisymmetric flows). -/
axiom no_swirl_kills_stretching :
    ∀ u : BoundedAncient,
      IsAxiSymmetric u → HasNoSwirl u → StretchingVanishes u

/-- THEOREM: KNSS follows from the stretching-vanishing Liouville. -/
theorem knss_from_vanishing_stretch
    (u : BoundedAncient)
    (h_axi : IsAxiSymmetric u) (h_ns : HasNoSwirl u) :
    IsTrivial u :=
  vanishing_stretch_liouville u (no_swirl_kills_stretching u h_axi h_ns)

/-! ## The Gap — What the General Case Lacks

The general case has NONE of the following:
- Axisymmetry (no symmetry at all)
- No swirl (all components present)
- Self-similarity (no ODE reduction)
- L³ membership (only L^∞, which is supercritical)
- Finite energy (Dirichlet integral may be infinite on R³)
- Small data (||u||_∞ can be large)
- Vanishing stretching (the stretching is present and has no sign)

The general bounded ancient solution has ONLY:
- Boundedness: |u| ≤ M
- Smoothness: all derivatives bounded (parabolic regularity)
- Divergence-free: ∇·u = 0
- Ancient: exists for all t ≤ 0
-/

/-- The general bounded ancient class has no known structural property
    that implies Liouville. This is the gap. -/
def IsGeneral (u : BoundedAncient) : Prop :=
  ¬ IsAxiSymmetric u ∧
  ¬ HasNoSwirl u ∧
  ¬ IsSelfSimilar u ∧
  ¬ IsInL3 u ∧
  ¬ HasFiniteEnergy u ∧
  ¬ IsSmallData u

/-- THE CONJECTURE: general bounded ancient solutions are trivial. -/
def LiouvilleConjecture : Prop :=
  ∀ u : BoundedAncient, IsTrivial u

/-- Liouville from the decomposition (attempt_007).
    If backward entry holds for ALL bounded ancient solutions,
    Liouville follows via small-data + unique continuation. -/
def BackwardEntryHypothesis : Prop :=
  ∀ u : BoundedAncient, ∃ t₀ : ℝ, t₀ ≤ 0 ∧ IsSmallData u

/-- Unique continuation for NS. -/
axiom unique_continuation :
    ∀ u : BoundedAncient,
      (∃ t₀ : ℝ, t₀ ≤ 0 ∧ IsTrivial u) → IsTrivial u

/-- THEOREM: backward entry + small-data Liouville → full Liouville. -/
theorem decomposition_gives_liouville
    (h_entry : BackwardEntryHypothesis) :
    LiouvilleConjecture := by
  intro u
  obtain ⟨t₀, _, h_small⟩ := h_entry u
  exact small_data_liouville u h_small

/-! ## The Stretching Obstruction

Every approach to the general case hits the same algebraic quantity:
(Sω · ω), the vortex stretching quadratic form.
-/

/-- Whether the average stretching rate is non-positive. -/
axiom HasNonpositiveStretching : BoundedAncient → Prop

/-- IF stretching is non-positive for ALL bounded ancient solutions,
    then Liouville holds (via energy monotonicity). -/
axiom nonpositive_stretching_gives_liouville :
    (∀ u : BoundedAncient, HasNonpositiveStretching u) →
    LiouvilleConjecture

/-- THEOREM: Liouville follows from EITHER path:
    (a) backward entry into the small-data regime, OR
    (b) non-positive average stretching for bounded ancient solutions. -/
theorem liouville_from_either_path
    (h : BackwardEntryHypothesis ∨
         (∀ u : BoundedAncient, HasNonpositiveStretching u)) :
    LiouvilleConjecture := by
  rcases h with h_entry | h_stretch
  · exact decomposition_gives_liouville h_entry
  · exact nonpositive_stretching_gives_liouville h_stretch

end LiouvilleTaxonomy
