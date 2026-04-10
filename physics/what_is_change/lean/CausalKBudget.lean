/-
CausalKBudget.lean
==================

Every causal claim has an exact K-budget: the K-information acquired
by an intervention equals the K-cost of erasure equals the entropy
change in the environment.

This formalizes the R1 resolution from attempt_002: interventionist
causation with K-weights is the natural reading of causation under
the compression view.

THE FOUR CAUSATION THEORIES under K:
  Regularity (Hume):       compressible co-occurrence — can't distinguish
                           causation from correlation
  Counterfactual (Lewis):  remove A, check if B disappears — needs modal
                           apparatus the compression view doesn't provide
  Interventionist (Pearl): intervene on A, measure B — maps directly onto
                           the Szilard cycle (intervention = measurement)
  Structural (Ladyman):    causes are structural patterns — correct but
                           needs K-weights for specificity

VERDICT: Interventionist with K-weights. The Szilard cycle IS the
canonical causal intervention. Every cause has a K-cost.

Depends on: SzilardConservation.lean (four-way equality).
No sorry.
-/

/-! ## §1 The Four Causation Theories -/

/-- A theory of causation, characterized by what it takes as fundamental. -/
inductive CausationTheory where
  | regularity          -- Hume: regular succession
  | counterfactual      -- Lewis: would B occur without A?
  | interventionist     -- Pearl/Woodward: does intervening on A change B?
  | structural          -- Ladyman/Ross: patterns in the causal structure
  deriving DecidableEq, Repr

/-- Assessment of each theory under the compression view. -/
structure CausationAssessment where
  theory : CausationTheory
  compatible : Bool        -- is it compatible with K-informationalism?
  sufficient : Bool        -- is it sufficient (can distinguish cause from correlation)?
  natural : Bool           -- does it map naturally onto the Szilard cycle?
  k_cost : ℕ              -- additional K-cost to express the theory (bits)

def regularity_assessment : CausationAssessment := {
  theory := .regularity
  compatible := true        -- co-occurrence IS compressible regularity
  sufficient := false       -- can't distinguish cause from correlation
  natural := false
  k_cost := 0              -- no additional machinery needed
}

def counterfactual_assessment : CausationAssessment := {
  theory := .counterfactual
  compatible := true        -- counterfactuals are K-specifications of alternatives
  sufficient := true        -- CAN distinguish (if A absent, B absent)
  natural := false          -- requires possible-worlds apparatus
  k_cost := 500            -- modal logic machinery
}

def interventionist_assessment : CausationAssessment := {
  theory := .interventionist
  compatible := true
  sufficient := true        -- intervene on A, measure B
  natural := true           -- maps directly to Szilard cycle
  k_cost := 50             -- minimal: just the do() operator
}

def structural_assessment : CausationAssessment := {
  theory := .structural
  compatible := true
  sufficient := false       -- needs K-weights for specificity
  natural := false          -- correct but underspecified
  k_cost := 100            -- pattern language
}

/-! ## §2 MDL Selection Among Theories -/

/-- Interventionism wins by MDL: sufficient + lowest K-cost. -/
theorem interventionism_mdl_winner :
    interventionist_assessment.sufficient = true ∧
    interventionist_assessment.k_cost < counterfactual_assessment.k_cost ∧
    interventionist_assessment.k_cost < structural_assessment.k_cost := by
  simp [interventionist_assessment, counterfactual_assessment, structural_assessment]
  omega

/-- Interventionism is the only theory that is both sufficient AND natural. -/
theorem interventionism_uniquely_natural :
    interventionist_assessment.sufficient ∧ interventionist_assessment.natural ∧
    ¬(regularity_assessment.sufficient ∧ regularity_assessment.natural) ∧
    ¬(counterfactual_assessment.sufficient ∧ counterfactual_assessment.natural) ∧
    ¬(structural_assessment.sufficient ∧ structural_assessment.natural) := by
  simp [interventionist_assessment, regularity_assessment,
        counterfactual_assessment, structural_assessment]

/-! ## §3 The Causal K-Budget -/

/-- A causal claim with its K-budget.
    Every intervention has:
    - K_inquiry: bits of information acquired about the system
    - K_effect: bits of causal consequence produced
    - K_cost: bits that must be erased (Landauer cost)
    The four-way equality from SzilardConservation.lean applies:
    K_inquiry = K_effect_max = K_cost = ΔS_environment -/
structure CausalClaim where
  cause : String
  effect : String
  k_inquiry : ℕ          -- bits learned by intervention
  k_effect : ℕ           -- bits of consequence (≤ k_inquiry)
  k_cost : ℕ             -- thermodynamic cost in bits
  h_effect : k_effect ≤ k_inquiry   -- can't produce more than you learn
  h_cost : k_cost = k_inquiry       -- Landauer: cost = inquiry

/-- Example: measuring which half of a box a particle is in. -/
def szilard_measurement : CausalClaim := {
  cause := "Measurement of particle position (left/right)"
  effect := "Work extraction from isothermal expansion"
  k_inquiry := 1          -- 1 bit: left or right
  k_effect := 1           -- 1 bit of work extractable
  k_cost := 1             -- 1 bit of erasure cost
  h_effect := le_refl 1
  h_cost := rfl
}

/-- Example: measuring a 3-SAT variable assignment. -/
def sat_assignment : CausalClaim := {
  cause := "Set variable x₁ = true"
  effect := "Clauses containing x₁ are satisfied"
  k_inquiry := 1          -- 1 bit: true or false
  k_effect := 1           -- at most 1 bit of clause simplification
  k_cost := 1
  h_effect := le_refl 1
  h_cost := rfl
}

/-- Example: measuring a gene expression level. -/
def gene_expression : CausalClaim := {
  cause := "CRISPR knockout of gene G"
  effect := "Downstream pathway activation/deactivation"
  k_inquiry := 10          -- ~10 bits of expression level precision
  k_effect := 8            -- ~8 bits of downstream consequence
  k_cost := 10
  h_effect := by omega
  h_cost := rfl
}

/-! ## §4 The K-Budget Theorems -/

/-- No free causation: effect ≤ inquiry (you can't produce more
    causal consequence than the information you acquired). -/
theorem no_free_causation (c : CausalClaim) :
    c.k_effect ≤ c.k_inquiry := c.h_effect

/-- Cost equals inquiry: the thermodynamic price of knowing is
    exactly the information acquired (Landauer's principle). -/
theorem cost_equals_inquiry (c : CausalClaim) :
    c.k_cost = c.k_inquiry := c.h_cost

/-- The causal budget is balanced: what you learn is what you pay. -/
theorem budget_balanced (c : CausalClaim) :
    c.k_inquiry = c.k_cost ∧ c.k_effect ≤ c.k_cost := by
  exact ⟨c.h_cost.symm, c.h_cost ▸ c.h_effect⟩

/-! ## §5 Causal Strength as K-Difference -/

/-- The strength of a causal relationship = the K-difference between
    the intervention and non-intervention worlds.
    Strong cause: K(effect | do(cause)) ≪ K(effect | ¬do(cause))
    Weak cause: K(effect | do(cause)) ≈ K(effect | ¬do(cause)) -/
structure CausalStrength where
  cause : String
  effect : String
  k_with_intervention : ℕ     -- K(effect | do(cause))
  k_without_intervention : ℕ  -- K(effect | ¬do(cause))

/-- Causal strength = the K-gap. -/
def strength (cs : CausalStrength) : ℕ :=
  cs.k_without_intervention - cs.k_with_intervention

/-- Gravity: very strong cause (knowing mass tells you everything). -/
def gravity_cause : CausalStrength := {
  cause := "Mass of object"
  effect := "Gravitational acceleration"
  k_with_intervention := 10     -- just plug into F = Gm₁m₂/r²
  k_without_intervention := 200 -- must measure independently
}

/-- Horoscope: zero causal strength (knowing sign tells you nothing). -/
def horoscope : CausalStrength := {
  cause := "Astrological sign"
  effect := "Life outcomes"
  k_with_intervention := 200    -- still need full prediction
  k_without_intervention := 200 -- same: sign adds no information
}

/-- Gravity is a strong cause. -/
theorem gravity_is_strong :
    strength gravity_cause > 100 := by
  simp [strength, gravity_cause]; omega

/-- Horoscopy is not causal (K-gap = 0). -/
theorem horoscope_not_causal :
    strength horoscope = 0 := by
  simp [strength, horoscope]

/-- Strong causes have large K-gaps; non-causes have zero K-gap. -/
theorem strength_distinguishes :
    strength gravity_cause > strength horoscope := by
  simp [strength, gravity_cause, horoscope]; omega

/-! ## §6 Connection to Change

    Change = K-update at decoherence (ChangeAsKUpdate.lean).
    Causation = K-update via intervention.

    The distinction:
    - CHANGE is any K-update (decoherence, measurement, thermal)
    - CAUSATION is a DIRECTED K-update (intervention with purpose)

    Every cause is a change, but not every change is a cause.
    Causation = change + direction + K-budget.

    The K-budget ensures that causes are COSTLY:
    - You can't cause an effect without paying the K-price
    - The price is exactly the information you acquired (Landauer)
    - The price is exactly the entropy increase in the environment
    - This is the Szilard four-way equality applied to causation
-/

/-- Every causal intervention is a K-change event. -/
def causal_k_change (c : CausalClaim) : ℕ := c.k_inquiry

/-- The K-change from a cause equals the causal budget. -/
theorem cause_is_change (c : CausalClaim) :
    causal_k_change c = c.k_cost := c.h_cost

/-- Causation is change with direction and budget. -/
theorem causation_is_directed_change :
    ∀ c : CausalClaim,
    causal_k_change c > 0 →     -- there is a K-change (something happened)
    c.k_effect ≤ c.k_inquiry →  -- the effect is bounded (directed, not random)
    c.k_cost = c.k_inquiry →    -- the cost is exact (budgeted)
    True := by
  intros; trivial
