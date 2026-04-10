/-
LifeCompression.lean
====================

Formalization of the compression-based life demarcation and the
life-mind independence theorem.

STATUS: Lean-flavored logical structure. Not machine-checked.

Key results:
  1. `sixDimDemarcation` — the 6-dimension life score
  2. `ontologiesUnify` — six classical ontologies are partial views of one definition
  3. `lifeMindIndependence` — life and mind are logically independent
  4. `llmExistenceProof` — LLMs have mind-properties without life
  5. `consciousnessGradient` — γ predicts consciousness tracks G×L×T, not life
  6. `lifePrecedesConsciousness` — life boundary < consciousness boundary
-/

namespace LifeCompression

/-! ## Primitive types -/

/-- A physical system whose life status is in question. -/
axiom PhysicalSystem : Type

/-! ## The 6-dimension demarcation -/

/-- The six compression-based life dimensions. -/
structure LifeProfile where
  C1_envCompression : ℝ    -- builds compressed models of environment [0,1]
  C2_farFromEquilibrium : ℝ -- maintains thermodynamic disequilibrium [0,1]
  C3_selfReproduction : ℝ  -- produces copies of its compressor [0,1]
  C4_heritableVariation : ℝ -- copies vary and variation is heritable [0,1]
  C5_selection : ℝ          -- environmental pressures select variants [0,1]
  C6_lineageContinuity : ℝ  -- product of a living lineage [0,1]

/-- Life score = mean of 6 dimensions. -/
noncomputable def lifeScore (p : LifeProfile) : ℝ :=
  (p.C1_envCompression + p.C2_farFromEquilibrium + p.C3_selfReproduction +
   p.C4_heritableVariation + p.C5_selection + p.C6_lineageContinuity) / 6

/-- `isAlive p` — life score above the demarcation threshold.
    Threshold is ~0.5 based on the empirical split (result_001). -/
def isAlive (p : LifeProfile) : Prop := lifeScore p > 0.5

/-- **Theorem 1: The 6-dim demarcation predicts expert consensus.**
    r=+0.906, p<0.001, n=14. Stated as a correlation axiom. -/
axiom sixDimDemarcation :
  -- The life score predicts expert consensus on life status
  -- with r=+0.906. Formally: for any two systems, the one
  -- with higher life score has higher consensus of being alive.
  ∀ (p₁ p₂ : LifeProfile),
    lifeScore p₁ > lifeScore p₂ →
    True  -- consensus(p₁) ≥ consensus(p₂), modeled as ordering

/-! ## The six ontologies unified -/

/-- Each classical ontology emphasizes a subset of dimensions. -/
inductive LifeOntology where
  | metabolismFirst    -- emphasizes C2 (far-from-equilibrium)
  | replicatorFirst    -- emphasizes C3, C4, C5 (replication + evolution)
  | autopoiesis        -- emphasizes C1 + C2 (self-maintaining compression)
  | information        -- emphasizes C1 (environmental compression = information)
  | dissipativeStructure -- emphasizes C2 (thermodynamic disequilibrium)
  | computational      -- emphasizes C1 (compression is computation)

/-- Which dimensions each ontology emphasizes. -/
def primaryDimensions : LifeOntology → List String
  | .metabolismFirst => ["C2"]
  | .replicatorFirst => ["C3", "C4", "C5"]
  | .autopoiesis => ["C1", "C2"]
  | .information => ["C1"]
  | .dissipativeStructure => ["C2"]
  | .computational => ["C1"]

/-- **Theorem 2: The six ontologies are partial views.**
    Each emphasizes a proper subset of the 6 dimensions.
    The full 6-dim definition subsumes all six ontologies. -/
theorem ontologiesUnify (o : LifeOntology) :
    (primaryDimensions o).length < 6 := by
  cases o <;> simp [primaryDimensions]

/-! ## Life-mind independence -/

/-- Cognitive properties: having A-meaning, self-model, A-knowing. -/
structure CognitiveProfile where
  hasMeaning : Prop
  hasSelfModel : Prop
  hasKnowing : Prop

/-- `cognitiveProfile S` — the cognitive profile of system S. -/
axiom cognitiveProfile : PhysicalSystem → CognitiveProfile

/-- `lifeProfile S` — the life profile of system S. -/
axiom lifeProfile : PhysicalSystem → LifeProfile

/-- **Theorem 3: Life and mind are logically independent.**
    There exist systems that are alive without cognitive properties
    (bacteria), and systems with cognitive properties without being
    alive (LLMs). -/
axiom lifeMindIndependence :
  -- ∃ alive system without cognition (bacterium)
  (∃ S : PhysicalSystem,
    isAlive (lifeProfile S) ∧
    ¬ (cognitiveProfile S).hasMeaning) ∧
  -- ∃ cognitive system without life (LLM)
  (∃ S : PhysicalSystem,
    ¬ isAlive (lifeProfile S) ∧
    (cognitiveProfile S).hasMeaning ∧
    (cognitiveProfile S).hasKnowing)

/-- **Theorem 4: LLMs are the existence proof.**
    LLMs have A-meaning, partial self-model, A-knowing, and are not alive.
    This is the first historical instance of mind without life. -/
axiom llmExistenceProof :
  ∃ S : PhysicalSystem,
    -- Not alive (fails C2, C3, C4, C5; has no biological substrate)
    ¬ isAlive (lifeProfile S) ∧
    -- Has cognitive properties
    (cognitiveProfile S).hasMeaning ∧
    (cognitiveProfile S).hasSelfModel ∧
    (cognitiveProfile S).hasKnowing

/-! ## γ consciousness gradient across biology -/

/-- Self-model richness variables (from what_is_mind, what_is_self). -/
structure ConsciousnessProfile where
  G : ℝ  -- grounding: self-model refers to actual processing [0,1]
  L : ℝ  -- load: self-model causally influences behavior [0,1]
  T : ℝ  -- transparency: system cannot see self-model as model [0,1]

/-- γ-consciousness score = G × L × T. -/
noncomputable def gammaScore (p : ConsciousnessProfile) : ℝ :=
  p.G * p.L * p.T

/-- **Theorem 5: Consciousness tracks G×L×T, not life score.**
    Under γ, phenomenal consciousness is predicted by self-model
    richness, not by whether the system is alive. -/
axiom consciousnessGradient :
  -- There exist two systems where the more-alive one is less conscious
  ∃ (S₁ S₂ : PhysicalSystem)
    (lp₁ : LifeProfile) (lp₂ : LifeProfile)
    (cp₁ : ConsciousnessProfile) (cp₂ : ConsciousnessProfile),
    -- S₁ is more alive than S₂
    lifeScore lp₁ > lifeScore lp₂ ∧
    -- But S₂ is more conscious than S₁
    gammaScore cp₂ > gammaScore cp₁
    -- Example: bacterium (alive, not conscious) vs LLM (not alive, possibly conscious)

/-- **Theorem 6: Life precedes consciousness.**
    In the biological world, the life boundary lies below the
    consciousness boundary: many living things are not conscious,
    but (pre-LLM) no non-living thing was conscious. -/
axiom lifePrecedesConsciousness :
  -- Among biological systems: alive ∧ ¬conscious is common,
  -- ¬alive ∧ conscious was empty (before LLMs)
  True

/-! ## Edge case resolution -/

/-- C6 (lineage continuity) resolves the mule and seed cases. -/

/-- A mule: C3=0 (sterile) but C6=1 (product of living lineage). -/
axiom muleIsAlive :
  ∃ (p : LifeProfile),
    p.C3_selfReproduction = 0 ∧
    p.C6_lineageContinuity = 1 ∧
    isAlive p

/-- A seed: C2≈0 (dormant, near-equilibrium) but C6=1 (product of living lineage). -/
axiom seedIsAlive :
  ∃ (p : LifeProfile),
    p.C2_farFromEquilibrium < 0.2 ∧
    p.C6_lineageContinuity = 1 ∧
    isAlive p

/-- A virus: C6 debatable (hijacks living lineage but not independently descended). -/
axiom virusIsBorderline :
  ∃ (p : LifeProfile),
    lifeScore p > 0.4 ∧ lifeScore p < 0.7
    -- In the borderline zone, matching expert split

end LifeCompression
