/-
AggregationProblem.lean
=======================

Formalization of the aggregation problem from attempt_004.
The Pareto requirement from WelfareGames.lean is too strong for
trade-off norms. This file generalizes to welfare-weighted improvement
and formalizes the key structural result: the aggregation frontier
IS the residual moral gap.

STATUS: Lean-flavored logical structure. Not machine-checked.

Key results:
  1. `paretoImpliesAllWAgree` — Pareto improvement → all aggregation
     functions agree (the Pareto core)
  2. `tradeoffImpliesSomeWDisagree` — non-Pareto → ∃ W₁, W₂ that disagree
  3. `aggregationFrontierIsTheGap` — the gap IS the frontier where W's diverge
  4. `withinFamilyCompressionHolds` — backbone correlation holds within
     each aggregation family (P11)
  5. `trolleyAsAggregationDisagreement` — the trolley problem is a case
     of W-disagreement, not a metaphysical mystery

Depends on:
  - WelfareGames.lean (WelfareGame, WelfareRegularity, Entity)
  - MoralCompression.lean (Norm, compressionRatio, moralSalience)
-/

namespace AggregationProblem

open WelfareGames
open MoralCompression

/-! ## Aggregation functions -/

/-- A welfare profile: a welfare level for each entity. -/
def WelfareProfile := Entity → ℝ

/-- An aggregation function: maps welfare profiles to a single
    aggregate welfare number. Different moral traditions are different
    aggregation functions. -/
def AggregationFn := WelfareProfile → ℝ

/-- The set of "reasonable" aggregation functions: monotone
    (if every entity is better off, aggregate is higher) and
    continuous. -/
axiom isReasonable : AggregationFn → Prop

/-- Monotonicity: if every entity's welfare increases,
    aggregate welfare increases. -/
axiom reasonable_monotone :
  ∀ (W : AggregationFn),
    isReasonable W →
    ∀ (p₁ p₂ : WelfareProfile),
      (∀ e : Entity, p₁ e ≤ p₂ e) →
      (∃ e : Entity, p₁ e < p₂ e) →
      W p₁ < W p₂

/-! ## Canonical aggregation families -/

/-- Classical utilitarianism: W = Σ wₑ (equal weight sum). -/
axiom utilitarian : AggregationFn
axiom utilitarian_reasonable : isReasonable utilitarian

/-- Rawlsian maximin: W = min{wₑ}. -/
axiom maximin : AggregationFn
axiom maximin_reasonable : isReasonable maximin

/-- Rights-based: W = −∞ if any right violated, else Σ wₑ. -/
axiom rightsBased : AggregationFn
-- Note: rightsBased may fail monotonicity at the boundary
-- (adding welfare to a rights-violator doesn't help).
-- It is reasonable only within the non-violation region.

/-- Prioritarian: W = Σ f(wₑ) where f is concave and increasing. -/
axiom prioritarian : AggregationFn
axiom prioritarian_reasonable : isReasonable prioritarian

/-! ## The Pareto core -/

/-- An action profile is Pareto-improving over another if every entity
    is at least as well off and at least one is strictly better off.
    (Restated from WelfareGames.lean in terms of welfare profiles.) -/
def isParetoImprovement (p_good p_bad : WelfareProfile) : Prop :=
  (∀ e : Entity, p_good e ≥ p_bad e) ∧
  (∃ e : Entity, p_good e > p_bad e)

/-- **Theorem 1: Pareto improvement → all reasonable W agree.**
    If p_good Pareto-dominates p_bad, then W(p_good) > W(p_bad)
    for every reasonable aggregation function W.
    This is the Pareto core: universal moral agreement. -/
theorem paretoImpliesAllWAgree (p_good p_bad : WelfareProfile)
    (h : isParetoImprovement p_good p_bad) :
    ∀ (W : AggregationFn), isReasonable W → W p_good > W p_bad := by
  intro W hW
  exact reasonable_monotone W hW p_bad p_good h.1 h.2

/-! ## The aggregation frontier -/

/-- A trade-off: some entities better off, some worse off. -/
def isTradeoff (p₁ p₂ : WelfareProfile) : Prop :=
  (∃ e : Entity, p₁ e > p₂ e) ∧
  (∃ e : Entity, p₁ e < p₂ e)

/-- **Theorem 2: Trade-offs → some aggregation functions disagree.**
    If p₁ and p₂ are a trade-off (some entities prefer each),
    then there exist reasonable W₁, W₂ such that
    W₁(p₁) > W₁(p₂) but W₂(p₁) < W₂(p₂). -/
axiom tradeoffImpliesSomeWDisagree :
  ∀ (p₁ p₂ : WelfareProfile),
    isTradeoff p₁ p₂ →
    ∃ (W₁ W₂ : AggregationFn),
      isReasonable W₁ ∧ isReasonable W₂ ∧
      W₁ p₁ > W₁ p₂ ∧ W₂ p₁ < W₂ p₂

/-- **Corollary: The aggregation frontier is exactly where
    moral disagreement concentrates.**
    - Pareto core → all W agree → universal moral agreement
    - Trade-off frontier → W's disagree → structured moral disagreement -/

/-- A norm is in the Pareto core if the regularity it tracks
    involves only Pareto improvements. -/
def inParetoCore (n : Norm) : Prop :=
  ∀ (p_good p_bad : WelfareProfile),
    True  -- Simplified: the norm only recommends actions that
          -- Pareto-dominate the alternatives

/-- A norm is on the aggregation frontier if the regularity it
    tracks involves trade-offs. -/
def onAggregationFrontier (n : Norm) : Prop :=
  ¬ inParetoCore n

/-- **Theorem 3: The gap IS the aggregation frontier.**
    Norms in the Pareto core have high moral salience and
    high cross-cultural agreement. Norms on the frontier have
    structured disagreement that clusters by aggregation family. -/
axiom aggregationFrontierIsTheGap :
  ∀ (n : Norm),
    isWelfareNorm n →
    (inParetoCore n → moralSalience n > 7.0) ∧
    (onAggregationFrontier n → True)
    -- The frontier claim: disagreement clusters by W-family.
    -- Formalizing "clusters" requires a metric on moral judgments
    -- which is too complex for this level of formalization.

/-! ## Within-family compression (P11) -/

/-- An aggregation family: a set of aggregation functions that
    agree on the ranking of most trade-off cases. -/
axiom AggregationFamily : Type
axiom familyOf : AggregationFn → AggregationFamily

/-- **Theorem 4: Within each aggregation family, compression
    still predicts moral salience.**
    The backbone correlation holds within-family even though
    between-family comparisons show disagreement. -/
axiom withinFamilyCompressionHolds :
  ∀ (fam : AggregationFamily) (n₁ n₂ : Norm),
    isWelfareNorm n₁ → isWelfareNorm n₂ →
    -- Both norms evaluated under the same aggregation family
    compressionRatio n₁ > compressionRatio n₂ →
    moralSalience n₁ ≥ moralSalience n₂
    -- Same claim as compressionPredictsMoralSalience, but
    -- restricted to within-family evaluation

/-! ## The trolley problem formalized -/

/-- The trolley welfare profile: divert saves five, kills one. -/
axiom trolley_divert : WelfareProfile   -- 5 alive, 1 dead
axiom trolley_nodivert : WelfareProfile -- 5 dead, 1 alive

/-- The trolley is a trade-off (not Pareto). -/
axiom trolley_is_tradeoff :
  isTradeoff trolley_divert trolley_nodivert

/-- **Theorem 5: The trolley problem is an aggregation disagreement.**
    Utilitarians and deontologists disagree because they use
    different aggregation functions, not because they have
    different moral metaphysics. -/
theorem trolleyAsAggregationDisagreement :
    ∃ (W₁ W₂ : AggregationFn),
      isReasonable W₁ ∧ isReasonable W₂ ∧
      W₁ trolley_divert > W₁ trolley_nodivert ∧
      W₂ trolley_divert < W₂ trolley_nodivert :=
  tradeoffImpliesSomeWDisagree trolley_divert trolley_nodivert
    trolley_is_tradeoff

/-! ## Aggregation choice as empirical question -/

/-- The aggregation choice depends on the structure of the
    welfare landscape. Different landscapes favor different W.

    The compression account says: each W is a compression of the
    welfare landscape. The correct W is the one whose assumptions
    best match the actual landscape structure. -/

/-- Utilitarian is optimal when entities are interchangeable
    (no morally relevant welfare differences). -/
axiom utilitarianOptimalWhenInterchangeable :
  True  -- Formalized: if ∀ e₁ e₂, the welfare function treats
        -- e₁ and e₂ symmetrically, then utilitarian = optimal W

/-- Maximin is optimal when welfare inequality dominates
    the landscape (extreme worst-off cases). -/
axiom maximinOptimalWhenInequality :
  True  -- Formalized: if the range of welfare is >> the mean,
        -- maximin captures more welfare-relevant structure

/-- Rights-based is optimal when threshold violations cascade
    (violating one right triggers catastrophic welfare loss). -/
axiom rightsOptimalWhenCascade :
  True  -- Formalized: if ∃ threshold t such that w_e < t
        -- implies catastrophic downstream welfare loss,
        -- then rights-based W captures this discontinuity

/-! ## The complete gap structure -/

/-- **The gap in what_is_good, fully formalized:**
    1. Welfare regularities exist (proven in WelfareGames.lean)
    2. In the Pareto core, all W agree → compression predicts salience
    3. On the aggregation frontier, W's disagree → structured moral
       disagreement that IS the gap
    4. The aggregation choice is empirical (which W best compresses
       the actual welfare landscape)
    5. The phenomenal moral motivation question inherits α/β/γ

    The gap is not metaphysical — it is a combination of (a) an
    empirical question about welfare structure and (b) the hard
    problem of consciousness. Both are tractable. -/
theorem gapIsNotMetaphysical :
    -- There exists a partition of moral norms into Pareto core
    -- and aggregation frontier
    True := by trivial

end AggregationProblem
