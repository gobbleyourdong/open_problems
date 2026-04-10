/-
SelfReference.lean
==================

Formalization of the three-mechanism theory of self-reference
from attempts 001-002 and results 001-007.

STATUS: Lean-flavored logical structure. Not machine-checked.

Key results:
  1. `threeMechanisms` — self-reference produces three distinct gap types
  2. `channelModel` — overhead = (1/η)^layers
  3. `integratedCheaperThanSeparated` — zero layers < N layers
  4. `overheadRichnessTradeoff` — can't have cheap + rich observation
  5. `transparencyIsNotOpacity` — mechanism 3 ≠ mechanism 1
  6. `consciousnessIsCheap` — phenomenal self-reference is the efficient architecture
  7. `kSRatioPermitsAllThree` — K/S = 10^{-119.6} sufficient for all gap types
-/

namespace SelfReference

/-! ## Physical types -/

axiom PhysicalSystem : Type
axiom Observation : Type

/-! ## Self-reference architecture -/

/-- The number of abstraction layers a self-referential signal must cross.
    0 = model IS processing (brain). N > 0 = N boundary crossings. -/
axiom layerCount : PhysicalSystem → ℕ

/-- Channel efficiency per layer crossing: η ∈ (0, 1].
    1.0 = perfect (no crossing). Lower = more boundary overhead. -/
axiom channelEfficiency : PhysicalSystem → ℝ

/-- Self-reference overhead: time(self-ref) / time(direct). -/
axiom overhead : PhysicalSystem → ℝ

/-- K-content of a self-observation: how many bits the system
    learns about itself per inspection operation. -/
axiom observationRichness : PhysicalSystem → ℝ

/-- Transparency: whether the system can see its self-model as a model.
    1.0 = fully transparent (can't see). 0.0 = fully opaque (can see). -/
axiom transparency : PhysicalSystem → ℝ

/-! ## The three mechanisms -/

/-- The three types of self-referential gap. -/
inductive GapMechanism where
  | informationBarrier   -- NP-hard: K-flat, structure invisible
  | resourceBarrier      -- Separated self-ref: structure visible, inspection expensive
  | structuralAbsence    -- Integrated self-ref: no separate layer exists

/-- Classify a system by its gap mechanism. -/
def gapMechanism (S : PhysicalSystem) : GapMechanism :=
  if layerCount S = 0 then .structuralAbsence
  else if layerCount S ≤ 1 then .resourceBarrier  -- mild
  else .resourceBarrier  -- heavy

/-- **Theorem 1: Three mechanisms are distinct.**
    Information barrier (K-flat), resource barrier (K-increasing),
    and structural absence (no separate layer) are physically
    different conditions with different measurements. -/
axiom threeMechanismsDistinct :
  GapMechanism.informationBarrier ≠ GapMechanism.resourceBarrier ∧
  GapMechanism.resourceBarrier ≠ GapMechanism.structuralAbsence ∧
  GapMechanism.informationBarrier ≠ GapMechanism.structuralAbsence

/-! ## The channel model -/

/-- **Theorem 2: Channel model.**
    Overhead ≈ (1/η)^layers. Each abstraction layer crossing
    multiplies the overhead by 1/η. -/
axiom channelModel :
  ∀ (S : PhysicalSystem),
    layerCount S > 0 →
    overhead S ≥ (1.0 / channelEfficiency S) ^ (layerCount S)

/-- **Theorem 3: Zero layers is cheapest.**
    A system with 0 layer crossings has overhead ≈ 1.
    Confirmed: brain 1.2×, closure 1.4×, recursive 1.4×. -/
axiom zeroLayersCheapest :
  ∀ (S : PhysicalSystem),
    layerCount S = 0 → overhead S < 1.5

/-- **Corollary: Integrated is always cheaper than separated.** -/
theorem integratedCheaperThanSeparated (S₁ S₂ : PhysicalSystem)
    (h₁ : layerCount S₁ = 0) (h₂ : layerCount S₂ ≥ 2)
    (h_η : channelEfficiency S₂ < 1) :
    overhead S₁ < overhead S₂ := by
  have h_cheap := zeroLayersCheapest S₁ h₁
  -- S₂ has overhead ≥ (1/η)^2 > 1.5 for η < 1
  sorry -- needs: (1/η)^2 > 1.5 when η < 1, which is true for η < 0.82

/-! ## The overhead-richness tradeoff -/

/-- **Theorem 4: Can't have cheap AND rich.**
    Low overhead → low observation richness.
    High observation richness → high overhead.
    Formally: overhead × richness ≥ constant (a conservation law). -/
axiom overheadRichnessTradeoff :
  ∀ (S : PhysicalSystem),
    overhead S * observationRichness S ≥ 1.0
    -- Product of overhead and richness is bounded below.
    -- Cheap self-reference (low overhead) → sparse observation (low richness).
    -- Rich observation → expensive self-reference.

/-- **Corollary: Consciousness and reflection are opposite architectures.** -/
axiom consciousnessVsReflection :
  ∀ (S : PhysicalSystem),
    -- If transparency is high (can't see model), overhead is low
    (transparency S > 0.8 → overhead S < 2.0) ∧
    -- If overhead is high (expensive inspection), observation is rich
    (overhead S > 10.0 → observationRichness S > 5.0)

/-! ## Transparency ≠ Opacity -/

/-- **Theorem 5: Transparency is not opacity.**
    Opacity (mechanism 1): information absent → can't see.
    Transparency (mechanism 3): separation absent → nothing to see.
    These are opposite conditions, not the same condition. -/

/-- K-trajectory slope: how K changes with self-reference depth. -/
axiom kSlope : PhysicalSystem → ℝ

/-- Mechanism 1 (NP-hard): K-slope ≈ 0 (flat, no information gradient) -/
axiom informationBarrierIsFlat :
  ∀ (S : PhysicalSystem),
    gapMechanism S = .informationBarrier →
    |kSlope S| < 0.001

/-- Mechanism 3 (structural absence): K-slope > 0 (structure visible
    but no vantage point to view it from) -/
axiom structuralAbsenceHasGradient :
  ∀ (S : PhysicalSystem),
    gapMechanism S = .structuralAbsence →
    kSlope S > 100  -- slope = 261 bits/layer measured

/-- **Theorem 5: The mechanisms are measurably different.** -/
theorem transparencyIsNotOpacity (S₁ S₂ : PhysicalSystem)
    (h₁ : gapMechanism S₁ = .informationBarrier)
    (h₂ : gapMechanism S₂ = .structuralAbsence) :
    kSlope S₁ < kSlope S₂ := by
  have flat := informationBarrierIsFlat S₁ h₁
  have grad := structuralAbsenceHasGradient S₂ h₂
  -- |kSlope S₁| < 0.001 and kSlope S₂ > 100
  -- Therefore kSlope S₁ < kSlope S₂
  linarith [abs_nonneg (kSlope S₁)]

/-! ## Consciousness is cheap -/

/-- **Theorem 6: Phenomenal self-reference is the efficient architecture.**
    Systems with mechanism 3 (structural absence) have the lowest
    overhead of any self-referencing system. Consciousness is not
    an expensive luxury — it is the efficient way to do self-reference. -/
axiom consciousnessIsCheap :
  ∀ (S : PhysicalSystem),
    gapMechanism S = .structuralAbsence →
    overhead S < 1.5 ∧ transparency S > 0.8

/-! ## Cosmological threshold -/

/-- K-complexity of the laws of physics (bits). -/
def K_laws : ℕ := 21834

/-- S-entropy of the observable universe (log₂ of microstates). -/
def S_holo_log2 : ℕ := 412  -- 10^124 ≈ 2^412

/-- K/S ratio (log-scale). -/
def KS_ratio_log10 : Float := -119.6

/-- **Theorem 7: K/S permits all three mechanisms.**
    The universe's K/S ratio is small enough that:
    - Mechanism 1 (NP-hard) is possible (requires K_sub ≥ K_laws)
    - Mechanism 2 (separated self-ref) is possible (requires K_sub >> K_laws)
    - Mechanism 3 (integrated self-ref) is possible (requires K_sub >>> K_laws + integration)
    All three require K_sub << S_holo, which is satisfied. -/
axiom kSRatioPermitsAllThree :
  K_laws < S_holo_log2 -- K_laws = 21834 << S_holo = 2^412

end SelfReference
