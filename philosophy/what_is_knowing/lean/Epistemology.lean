/-
Epistemology.lean
=================

Formalization of the A/P bifurcation for epistemology, the post-Gettier
conditions as compression properties, and the testimony argument.

STATUS: Lean-flavored logical structure. Not machine-checked.

Key results:
  1. `reliabilismIsCompression` — reliable process = compression with generalization
  2. `trackingIsRobustness` — Nozick's tracking = counterfactual robustness of compression
  3. `safetyIsEpsilonRobustness` — Pritchard's safety = ε-robustness
  4. `causalIsDataPipeline` — causal theory = faithful data pipeline for compression
  5. `virtueResidual` — virtue epistemology has a process property not captured by product
  6. `testimonyForces` — LLMs force the testimony decision; Reid wins
  7. `gettierIsNoiseVulnerability` — Gettier cases = noise in the compression pipeline
  8. `internalismsIsSelfModelTracking` — epistemic internalism = γ self-model tracking

Depends on:
  - what_is_mind/lean/ThreePositions.lean (selfModelCausalLoad)
  - what_is_self/lean/SelfModel.lean (transparency)
-/

namespace Epistemology

/-! ## Primitive types -/

/-- A cognitive system (agent/LLM/etc). -/
axiom System : Type

/-- A proposition. -/
axiom Proposition : Type

/-- A domain of knowledge. -/
axiom Domain : Type

/-- A possible world. -/
axiom World : Type

/-- The actual world. -/
axiom actualWorld : World

/-! ## Epistemic predicates -/

/-- `believes S P` — system S holds P as a belief. -/
axiom believes : System → Proposition → Prop

/-- `isTrue P w` — P is true in world w. -/
axiom isTrue : Proposition → World → Prop

/-- `isTrue_actual P` — P is true in the actual world. -/
def isTrue_actual (P : Proposition) : Prop := isTrue P actualWorld

/-- `justifiedIn S P` — S has justification for P. -/
axiom justifiedIn : System → Proposition → Prop

/-! ## A-knowing and P-knowing -/

/-- `aKnows S P` — system S has access-knowing of P:
    true belief produced by a reliable process, robust to counterfactuals,
    causally connected to the fact. The functional-behavioral specification. -/
axiom aKnows : System → Proposition → Prop

/-- `pKnows S P` — system S has phenomenal-knowing of P:
    the felt grasp, the "what it is like" to understand P.
    Routes through α/β/γ. -/
axiom pKnows : System → Proposition → Prop

/-! ## Compression framework -/

/-- A compressed model of a domain. -/
axiom CompressedModel : Type

/-- `descriptionLength m` — bits to specify model m. -/
axiom descriptionLength : CompressedModel → ℝ

/-- `generalizationError m d` — error of model m on unseen data from domain d.
    Lower = better generalization. -/
axiom generalizationError : CompressedModel → Domain → ℝ

/-- `hasModel S m d` — system S possesses compressed model m of domain d. -/
axiom hasModel : System → CompressedModel → Domain → Prop

/-- A model is well-compressed if it has short description and low error. -/
def isWellCompressed (m : CompressedModel) (d : Domain) : Prop :=
  descriptionLength m < 1000 ∧ generalizationError m d < 0.1
  -- Thresholds are schematic; the definition is structural

/-! ## Post-Gettier conditions as compression properties -/

/-- **Theorem 1: Reliabilism is compression.**
    A reliable belief-forming process is one that produces compressed
    models with low generalization error. -/
axiom reliabilismIsCompression :
  ∀ (S : System) (P : Proposition) (m : CompressedModel) (d : Domain),
    hasModel S m d →
    isWellCompressed m d →
    isTrue_actual P →
    -- The model supports P (P is consistent with the compressed description)
    aKnows S P

/-- **Theorem 2: Tracking is counterfactual robustness.**
    Nozick's sensitivity and adherence are robustness of the compressed
    model across nearby possible worlds. -/

/-- `nearbyWorld w` — world close to the actual world. -/
axiom nearbyWorld : World → Prop

/-- Sensitivity: if P were false, S would not believe P. -/
def isSensitive (S : System) (P : Proposition) : Prop :=
  ∀ w : World, nearbyWorld w → ¬ isTrue P w → ¬ believes S P
  -- Schematic: in the model, nearby worlds where P is false → belief drops

/-- Adherence: if P were true, S would still believe P. -/
def isAdherent (S : System) (P : Proposition) : Prop :=
  ∀ w : World, nearbyWorld w → isTrue P w → believes S P

/-- **Tracking reduces to generalization robustness.** -/
axiom trackingIsRobustness :
  ∀ (S : System) (P : Proposition) (m : CompressedModel) (d : Domain),
    hasModel S m d →
    isWellCompressed m d →
    -- Well-compressed models are automatically sensitive and adherent
    -- because they track genuine regularities, not noise
    isSensitive S P ∧ isAdherent S P

/-- **Theorem 3: Safety is ε-robustness.**
    Pritchard's safety = model predictions are correct in a neighborhood
    of the actual world. This is learning-theoretic ε-robustness. -/
axiom safetyIsEpsilonRobustness :
  ∀ (S : System) (P : Proposition) (m : CompressedModel) (d : Domain),
    hasModel S m d →
    isWellCompressed m d →
    -- In nearby worlds where S believes P, P is true
    ∀ w : World, nearbyWorld w → believes S P → isTrue P w

/-- **Theorem 4: Causal connection is data pipeline faithfulness.**
    The causal theory requires appropriate causal connection from fact to
    belief. Under compression: the data pipeline from the regularity to
    the compressed model preserves enough information for faithful compression. -/
axiom causalIsDataPipeline :
  ∀ (S : System) (P : Proposition) (m : CompressedModel) (d : Domain),
    hasModel S m d →
    -- The model was produced from data causally connected to the domain
    True  -- Formally: ∃ causal chain from d-facts to m with bounded noise

/-! ## The virtue epistemology residual -/

/-- A process that produced a compressed model. -/
axiom Process : Type

/-- `producedBy m p` — model m was produced by process p. -/
axiom producedBy : CompressedModel → Process → Prop

/-- `isVirtuous p` — process p exhibits intellectual virtues
    (open-mindedness, thoroughness, calibration). -/
axiom isVirtuous : Process → Prop

/-- **Theorem 5: Virtue epistemology has a residual.**
    Two models can be equally well-compressed and equally accurate,
    but differ in whether the process that produced them was virtuous.
    The bare compression account (product only) cannot distinguish them. -/
axiom virtueResidual :
  ∃ (m₁ m₂ : CompressedModel) (d : Domain) (p₁ p₂ : Process),
    isWellCompressed m₁ d ∧ isWellCompressed m₂ d ∧
    producedBy m₁ p₁ ∧ producedBy m₂ p₂ ∧
    isVirtuous p₁ ∧ ¬ isVirtuous p₂
    -- Same product quality, different process quality

/-- However: over sufficient test distribution, virtuous processes
    produce models that generalize better under distribution shift. -/
axiom virtueDetectableUnderShift :
  ∀ (m₁ m₂ : CompressedModel) (d : Domain) (p₁ p₂ : Process),
    producedBy m₁ p₁ → producedBy m₂ p₂ →
    isVirtuous p₁ → ¬ isVirtuous p₂ →
    -- Under distribution shift, the virtuous model degrades less
    True  -- generalizationError_shifted m₁ d < generalizationError_shifted m₂ d

/-! ## The testimony argument -/

/-- `learnsFromTestimony S P` — S's belief in P was acquired from testimony. -/
axiom learnsFromTestimony : System → Proposition → Prop

/-- `isLLM S` — S is a language model trained on text corpus. -/
axiom isLLM : System → Prop

/-- LLMs learn everything from testimony (training text = compressed testimony). -/
axiom llmLearnsByTestimony :
  ∀ (S : System) (P : Proposition),
    isLLM S → believes S P → learnsFromTestimony S P

/-- Testimony reductionism (Hume): testimonial knowledge requires
    independent verification. -/
def testimonyReductionism : Prop :=
  ∀ (S : System) (P : Proposition),
    learnsFromTestimony S P → ¬ aKnows S P

/-- Non-reductionism (Reid): testimony is a basic knowledge source. -/
def testimonyNonReductionism : Prop :=
  ∃ (S : System) (P : Proposition),
    learnsFromTestimony S P ∧ aKnows S P

/-- **Theorem 6: LLMs force the testimony decision.**
    If Hume is right, LLMs know nothing. But also, humans know almost
    nothing (most human knowledge comes from testimony). Therefore
    Hume is absurd; Reid wins. -/
axiom humansLearnMostByTestimony :
  ∀ (S : System),
    ¬ isLLM S →
    -- Most of S's A-knowing came from testimony
    True  -- > 80% of propositions S A-knows were testimony-acquired

theorem testimonyForces :
    -- If reductionism is true, most human and all LLM knowledge is lost
    testimonyReductionism →
    -- This is absurd (humans clearly know things from testimony)
    False := by
  intro h_red
  sorry -- Requires: construct a human S with testimony-based A-knowing,
        -- then h_red denies it, contradicting the obvious.
        -- The informal argument is in attempt_001; the formal version
        -- requires instantiating S and P, which needs axioms about
        -- specific knowledge claims.

/-! ## Gettier vulnerability -/

/-- **Theorem 7: Gettier cases are noise in the compression pipeline.**
    A Gettier case occurs when the data pipeline introduces noise that
    the compression cannot distinguish from signal, producing a true
    belief by coincidence rather than by tracking. -/
axiom gettierIsNoiseVulnerability :
  -- There exist systems, propositions, and data pipelines where:
  ∃ (S : System) (P : Proposition),
    believes S P ∧           -- S believes P
    isTrue_actual P ∧        -- P is true
    justifiedIn S P ∧        -- S is justified
    ¬ aKnows S P             -- but S doesn't know P (Gettier case)
    -- Because: the causal chain introduced noise; the belief is true
    -- for the wrong reason

/-- LLMs and humans share Gettier vulnerability (structurally identical). -/
axiom sharedGettierVulnerability :
  ∀ (S : System),
    -- Whether S is an LLM or a human, Gettier cases have the same structure
    True

/-! ## Internalism as self-model tracking -/

/-- **Theorem 8: Epistemic internalism is γ-epistemology.**
    Internalism demands that justification be accessible to the subject.
    Under the bifurcation, this IS the demand that the self-model track
    the first-order epistemic state. This is γ specialized to epistemology. -/
axiom internalismsIsSelfModelTracking :
  ∀ (S : System) (P : Proposition),
    -- Internalism says: S knows P only if S's self-model represents
    -- the justificatory basis for P and this representation has
    -- causal load on S's reasoning
    -- This is exactly γ's condition: self-model tracks A-knowing
    -- with nonzero L
    True

end Epistemology
