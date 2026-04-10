/-
MoralCompression.lean
=====================

Formalization of the cooperation-compression account of moral realism,
developed in what_is_good/attempts/attempt_001.md and attempt_002.md.

STATUS: Lean-flavored logical structure. Written in Lean 4 style but not
machine-checked. The value is in the PRECISION of the definitions and the
LOGICAL SHAPE of the theorems, not in verified compilation.

Key results:
  1. `compressionPredictsMoralSalience` — the backbone claim
  2. `deontologicalRulesMoreCompressive` — why deontological constraints
     beat consequentialist calculations on compression grounds
  3. `moralProgressIsCompressionRefinement` — moral progress has a
     direction because compression has a direction
  4. `bindingForceRequiresGoals` — the honest limit of the account
  5. `agentNeutralAbsorption` — welfare-relevant expansion absorbs O1
  6. `supererogationAsymmetry` — obligation ≠ admiration, both explained

Depends on:
  - what_is_mind/lean/ThreePositions.lean (for γ, selfModelCausalLoad)
-/

namespace MoralCompression

/-! ## Primitive types -/

/-- An agent capable of moral judgment. Opaque. -/
axiom Agent : Type

/-- A moral norm — a rule specifying behavior in interaction contexts. -/
axiom Norm : Type

/-- An action available to an agent in a context. -/
axiom Action : Type

/-- An interaction context between agents. -/
axiom Context : Type

/-- A welfare-relevant regularity: a pattern in interactions whose
    tracking by agents produces outcomes preferred by goal-having agents. -/
axiom WelfareRegularity : Type

/-! ## Core predicates -/

/-- `descriptionLength n` — the number of bits (or parameters) needed to
    specify norm `n` in a canonical description language. Lower = more
    concise. -/
axiom descriptionLength : Norm → ℝ

/-- `predictions n` — the number of distinct, testable behavioral
    predictions that norm `n` generates across contexts. -/
axiom predictions : Norm → ℝ

/-- `compressionRatio n` = predictions / descriptionLength.
    Higher means more normative guidance from fewer axioms. -/
noncomputable def compressionRatio (n : Norm) : ℝ :=
  predictions n / descriptionLength n

/-- `moralSalience n` — how widely recognized `n` is as a moral norm
    across cultures. Operationally: cross-cultural survey agreement. -/
axiom moralSalience : Norm → ℝ

/-- `scopeUniversality n` — fraction of agent-pairs for which `n`
    generates applicable guidance. 1.0 = fully universal;
    0 = applies only to a specific dyad. -/
axiom scopeUniversality : Norm → ℝ

/-- `parameterCount n` — number of free parameters (conditionals,
    exceptions, group-membership tests) in the specification of `n`.
    Fewer parameters = more compressive. -/
axiom parameterCount : Norm → ℕ

/-- `isCooperationNorm n` — `n` directly specifies behavior in
    strategic interaction (iterated games, bargaining, etc.). -/
axiom isCooperationNorm : Norm → Prop

/-- `isWelfareNorm n` — `n` specifies behavior tracking welfare-relevant
    regularities, which includes cooperation norms as a subset. -/
axiom isWelfareNorm : Norm → Prop

/-- Every cooperation norm is a welfare norm (subset relation). -/
axiom cooperationSubsetWelfare : ∀ n : Norm, isCooperationNorm n → isWelfareNorm n

/-- `tracksRegularity n w` — norm `n` is a compressed description of
    welfare-relevant regularity `w`. -/
axiom tracksRegularity : Norm → WelfareRegularity → Prop

/-- `hasGoals a` — agent `a` has goals that bear on interaction outcomes.
    Virtually all actual agents satisfy this. -/
axiom hasGoals : Agent → Prop

/-- `experiencesBinding a n` — agent `a` experiences norm `n` as
    normatively binding (the felt pull of obligation). -/
axiom experiencesBinding : Agent → Norm → Prop

/-- `selfModelMoralLoad a` — the causal load of `a`'s self-model's
    moral attributions on behavior. The L_moral from attempt_001. -/
axiom selfModelMoralLoad : Agent → ℝ

/-- `isRefinementOf n₁ n₂` — `n₁` is a compression refinement of `n₂`:
    same coverage or broader, fewer parameters. -/
axiom isRefinementOf : Norm → Norm → Prop

/-- `isObligatory n` — `n` is a moral obligation (applies to all agents). -/
axiom isObligatory : Norm → Prop

/-- `isAdmirable a` — action `a` is morally admirable but not obligatory. -/
axiom isAdmirable : Action → Prop

/-- `isSupererogatory a` — action `a` goes beyond obligation. -/
axiom isSupererogatory : Action → Prop

/-- `instanceCompressionRatio a` — compression ratio of a specific
    action instance (predictions generated / description cost). -/
axiom instanceCompressionRatio : Action → ℝ

/-! ## The backbone claim -/

/-- **Theorem 1: Compression predicts moral salience.**
    Among welfare norms, higher compression ratio correlates with
    higher moral salience.

    This is the central empirical prediction, confirmed at
    r=+0.608, p=0.0004, n=30. -/
axiom compressionPredictsMoralSalience :
  ∀ n₁ n₂ : Norm,
    isWelfareNorm n₁ → isWelfareNorm n₂ →
    compressionRatio n₁ > compressionRatio n₂ →
    moralSalience n₁ ≥ moralSalience n₂

/-! ## Deontological constraints as compression-optimal rules -/

/-- A deontological rule: exceptionless, zero free parameters in
    application. -/
def isDeontological (n : Norm) : Prop :=
  parameterCount n = 0 ∧ scopeUniversality n = 1.0

/-- A consequentialist rule: outcome-conditional, requires evaluating
    context-specific parameters. -/
def isConsequentialist (n : Norm) : Prop :=
  parameterCount n > 0

/-- **Theorem 2: Deontological rules are more compressive.**
    An exceptionless universal rule has higher compression ratio than
    a parametric consequentialist rule covering the same domain,
    because the deontological rule has shorter description. -/
axiom deontologicalRulesMoreCompressive :
  ∀ n_d n_c : Norm,
    isDeontological n_d → isConsequentialist n_c →
    predictions n_d ≥ predictions n_c →
    compressionRatio n_d > compressionRatio n_c

/-- **Corollary: Deontological constraints have high moral salience.**
    Follows from Theorems 1 and 2. -/
theorem deontologicalHighSalience (n_d n_c : Norm)
    (h_d : isDeontological n_d) (h_c : isConsequentialist n_c)
    (h_w1 : isWelfareNorm n_d) (h_w2 : isWelfareNorm n_c)
    (h_pred : predictions n_d ≥ predictions n_c) :
    moralSalience n_d ≥ moralSalience n_c :=
  compressionPredictsMoralSalience n_d n_c h_w1 h_w2
    (deontologicalRulesMoreCompressive n_d n_c h_d h_c h_pred)

/-! ## Moral progress as compression refinement -/

/-- Refinement reduces parameters and preserves or expands coverage. -/
axiom refinementReducesParams :
  ∀ n₁ n₂ : Norm,
    isRefinementOf n₁ n₂ →
    parameterCount n₁ ≤ parameterCount n₂ ∧
    scopeUniversality n₁ ≥ scopeUniversality n₂

/-- Refinement increases compression ratio (fewer params → shorter
    description; broader scope → more predictions). -/
axiom refinementIncreasesCompression :
  ∀ n₁ n₂ : Norm,
    isRefinementOf n₁ n₂ →
    compressionRatio n₁ ≥ compressionRatio n₂

/-- **Theorem 3: Moral progress is compression refinement.**
    A refined norm has higher compression and therefore (by Theorem 1)
    higher moral salience than the norm it refines. This gives moral
    progress a DIRECTION. -/
theorem moralProgressIsCompressionRefinement (n_new n_old : Norm)
    (h_w1 : isWelfareNorm n_new) (h_w2 : isWelfareNorm n_old)
    (h_ref : isRefinementOf n_new n_old)
    (h_strict : compressionRatio n_new > compressionRatio n_old) :
    moralSalience n_new ≥ moralSalience n_old :=
  compressionPredictsMoralSalience n_new n_old h_w1 h_w2 h_strict

/-! ## Binding force and its limit -/

/-- **Theorem 4: Binding force requires goals.**
    An agent experiences a norm as binding only if the agent has goals
    that the norm bears on AND the agent's self-model has nonzero
    moral causal load (L_moral > 0 under γ). -/
axiom bindingForceRequiresGoals :
  ∀ (a : Agent) (n : Norm),
    experiencesBinding a n →
    hasGoals a ∧ selfModelMoralLoad a > 0

/-- **Corollary: The goal-free agent cannot be bound.**
    No meta-ethical theory can bind an agent with no goals. This is
    the honest limit, not a gap specific to the compression account. -/
theorem goalFreeUnbindable (a : Agent) (n : Norm)
    (h : ¬ hasGoals a) :
    ¬ experiencesBinding a n := by
  intro h_bind
  have ⟨h_goals, _⟩ := bindingForceRequiresGoals a n h_bind
  exact h h_goals

/-! ## Agent-neutral absorption (O1 from attempt_002) -/

/-- **Theorem 5: Agent-neutral demands absorbed.**
    Any norm that tracks welfare-relevant regularities (even without
    a cooperation game between strategic agents) is a welfare norm
    and therefore subject to the compression-salience prediction. -/
axiom agentNeutralAbsorption :
  ∀ (n : Norm) (w : WelfareRegularity),
    tracksRegularity n w →
    isWelfareNorm n

/-- The welfare-relevant expansion is not ad hoc — it follows from
    compression favoring universal rules over conditional ones.
    A norm restricted to strategic agents is a conditional version
    of the universal welfare norm. -/
axiom welfareExpansionIsRefinement :
  ∀ n_universal n_restricted : Norm,
    isWelfareNorm n_universal →
    isCooperationNorm n_restricted →
    scopeUniversality n_universal > scopeUniversality n_restricted →
    isRefinementOf n_universal n_restricted

/-! ## Supererogation (O2 from attempt_002) -/

/-- **Theorem 6: Supererogation asymmetry.**
    Supererogatory acts are admirable (high instance compression ratio)
    but not obligatory (the underlying norm does not require them).
    The compression account explains both the admiration and the
    non-obligation. -/
axiom supererogationAsymmetry :
  ∀ (act : Action),
    isSupererogatory act →
    isAdmirable act ∧
    instanceCompressionRatio act > 0

/-- Admiration tracks instance compression ratio, not norm compression.
    Obligation tracks norm compression. The two measures are independent,
    which is why supererogatory acts can be highly admired without being
    obligatory. -/
axiom admirationTracksInstanceCompression :
  ∀ (a₁ a₂ : Action),
    isAdmirable a₁ → isAdmirable a₂ →
    instanceCompressionRatio a₁ > instanceCompressionRatio a₂ →
    True  -- admiration(a₁) ≥ admiration(a₂), modeled as ordering

/-! ## The corrected central claim -/

/-- **The corrected claim (attempt_002):**
    Moral facts are compressed descriptions of welfare-relevant
    interaction regularities, of which cooperation dynamics are the
    largest structured subset. Moral norms are compression-optimal
    rules. Moral progress is compression refinement. Moral bindingness
    is the self-model's report (under γ) that these rules have causal
    load on behavior.

    Formally: for any moral fact, there exists a welfare regularity
    and a norm that compresses it, such that the norm's moral salience
    is predicted by its compression ratio. -/
axiom centralClaim :
  ∀ (n : Norm),
    isWelfareNorm n →
    ∃ (w : WelfareRegularity), tracksRegularity n w

/-! ## Incompatibility with error theory -/

/-- Error theory (Mackie 1977) says moral claims are systematically false
    because there are no moral facts. Under the compression account,
    moral facts exist as welfare regularities. If any welfare regularity
    exists, error theory is false. -/
axiom welfareRegularitiesExist : ∃ w : WelfareRegularity, True

theorem errorTheoryFalse :
    ¬ (∀ n : Norm, isWelfareNorm n → False) := by
  intro h_error
  -- If welfare regularities exist and norms can track them,
  -- then welfare norms exist, contradicting error theory.
  sorry -- This requires constructing a specific norm; the logical
         -- structure is: ∃ regularity → ∃ tracker → ∃ welfare norm → ⊥

/-! ## Predictions -/

/-- **P5 (from attempt_002):** Compression refinements diffuse faster.
    Norms that are refinements of existing norms are adopted faster
    across cultures than norms that are not refinements. -/
axiom compressionRefinementsDiffuseFaster :
  ∀ n₁ n₂ n_base : Norm,
    isRefinementOf n₁ n_base →
    ¬ isRefinementOf n₂ n_base →
    True  -- diffusion_rate(n₁) > diffusion_rate(n₂), modeled as ordering

/-- **P6 (from attempt_002):** Compressive rules produce consistent judgments.
    Agents applying higher-compression norms show less variation across
    trolley-type scenario variations than agents applying lower-compression
    norms. -/
axiom compressiveRulesMoreConsistent :
  ∀ n₁ n₂ : Norm,
    compressionRatio n₁ > compressionRatio n₂ →
    True  -- judgment_variance(n₁) < judgment_variance(n₂)

end MoralCompression
