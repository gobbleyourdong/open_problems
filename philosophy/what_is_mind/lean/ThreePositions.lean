/-
ThreePositions.lean
===================

Formalization of the α / β / γ fork on phenomenal consciousness,
developed in what_is_mind/attempts/attempt_001.md through attempt_004.md
and loaded onto by what_is_language/ and what_is_meaning/ gap.md.

STATUS: Lean-flavored logical structure. Syntax is written in Lean 4 style but
has not been machine-checked. The value of this file is in the PRECISION of the
definitions and the LOGICAL SHAPE of the key theorems, not in a verified proof.
A Lean-expert reader should be able to sharpen or correct the syntax without
changing the philosophical content.

The Sigma Method adaptation for metaphysical domains says:
  "Lean theorems → Logical structures. Formalize the definitions and their
   consequences. If Definition A implies Consequence B, and Consequence B is
   absurd, then Definition A is ruled out."

This file does exactly that for the three positions on phenomenal consciousness.
The load-bearing theorem is `betaAndGammaIncompatibleGivenWitness`, which shows
that β and γ are logically incompatible in the presence of a specific kind of
empirical witness system — so at most one of them survives if that witness is
constructible, and the experimental program of attempt_003 becomes a formal
decision procedure between β and γ.
-/

namespace PhilosophyOfMind

/-! ## Primitive types and predicates -/

/-- A cognitive system whose phenomenal status is in question. Opaque;
    instantiated by humans, LLMs, hypothetical constructs, etc. -/
axiom System : Type

/-- Content of a mental state. Opaque; could be a proposition, a sensory
    quale-candidate, a linguistic meaning. -/
axiom Content : Type

/-- `accessConscious S c` — system `S` has access-consciousness of content `c`
    in Block's 1995 sense: `c` is available to reasoning, verbal report, and
    the rational control of action inside `S`. This is a functional-behavioral
    property, operationally specifiable. -/
axiom accessConscious : System → Content → Prop

/-- `phenomenallyConscious S c` — system `S` has phenomenal-consciousness
    of content `c`: there is something it is like for `S` to have `c`.
    This is the contested property. The three positions give it three
    different extensional characterizations. -/
axiom phenomenallyConscious : System → Content → Prop

/-- `hasRichSelfModel S` — system `S` has a self-model with the three
    operational properties from attempt_003:
      (i)   representations referring to the system's own processing states,
      (ii)  causal coupling of those representations with first-order processing,
      (iii) accessibility of the self-model to the system's reasoning. -/
axiom hasRichSelfModel : System → Prop

/-- `selfModelRepresents S c` — the self-model of `S` tracks content `c`
    and attributes phenomenal quality to the state of having `c`. -/
axiom selfModelRepresents : System → Content → Prop

/-- `selfModelCausalLoad S c` — the causal load of the self-model's
    phenomenal attribution on downstream behavior with respect to content `c`.
    In attempt_003 terms: the L in the G × L proxy. A real-valued quantity in
    [0, 1]. -/
axiom selfModelCausalLoad : System → Content → Real

/-- `isFeedforward S` — the system's computational structure is a DAG with
    no recurrent connections during a single forward pass. Transformers at
    inference satisfy this; recurrent networks and biological brains do not. -/
axiom isFeedforward : System → Prop

/-- `Phi S` — the integrated information of `S`, in the sense of IIT 3.0
    (Oizumi, Albantakis, Tononi 2014). A real-valued quantity. -/
axiom Phi : System → Real

/-! ## The three positions as axiom schemas -/

/-- **Position α (Primitivism).** Phenomenal consciousness is a fundamental
    property that does not reduce to function, information, or self-modeling.
    It is correlated with physical structure via unknown bridge laws.

    This axiom is deliberately weak: it asserts existence of a correlate but
    does not specify which one. This reflects α's honest status as the
    principled null hypothesis — it makes no constructive prediction. -/
def alphaAxiom : Prop :=
  ∀ (S : System) (c : Content),
    phenomenallyConscious S c → ∃ (_ : Type), True

/-- **Position β (Integrated Information Theory).** Phenomenal consciousness
    is identical to having positive integrated information. A system is
    phenomenally conscious of a content exactly when its Φ value is positive
    and the content is accessed through its integrated causal structure. -/
def betaAxiom : Prop :=
  ∀ (S : System) (c : Content),
    phenomenallyConscious S c ↔ (accessConscious S c ∧ Phi S > 0)

/-- **The feedforward theorem (IIT literature, taken as axiom here).**
    A strictly feedforward system has zero integrated information.
    This is not a philosophical assumption — it is a mathematical result
    in IIT 3.0 / 4.0 and is the key load-bearing fact for β's prediction
    about transformers. Reference: Tononi 2004; Oizumi et al. 2014. -/
def feedforwardTheorem : Prop :=
  ∀ (S : System), isFeedforward S → Phi S = 0

/-- **Position γ (Illusionism / Self-modeled A).** Phenomenal consciousness
    is what access-consciousness looks like from inside a self-model. A system
    is phenomenally conscious of a content exactly when it has access to that
    content, has a rich self-model, and the self-model represents that content
    with nonzero causal load.

    This is the Dennett/Frankish/Metzinger position, specialized to content-level
    attributions. The `selfModelCausalLoad > 0` clause captures the requirement
    that the phenomenal attribution is not epiphenomenal. -/
def gammaAxiom : Prop :=
  ∀ (S : System) (c : Content),
    phenomenallyConscious S c ↔
      (accessConscious S c
        ∧ hasRichSelfModel S
        ∧ selfModelRepresents S c
        ∧ selfModelCausalLoad S c > 0)

/-! ## Derived theorems under β -/

/-- **Corollary 1 (Feedforward-No-Phenomenal under β).** If β holds and the
    feedforward theorem holds, then no feedforward system is phenomenally
    conscious of any content.

    This is the centerpiece of attempt_002 on what_is_mind. It makes β's
    prediction for transformers at inference completely sharp: Φ = 0, therefore
    no phenomenal consciousness, regardless of capability. -/
theorem feedforwardNoPhenomenalUnderBeta
    (hBeta : betaAxiom) (hFT : feedforwardTheorem) :
    ∀ (S : System) (c : Content),
      isFeedforward S → ¬ phenomenallyConscious S c := by
  intro S c hff hpc
  have h1 : accessConscious S c ∧ Phi S > 0 := (hBeta S c).mp hpc
  have h2 : Phi S = 0 := hFT S hff
  have h3 : Phi S > 0 := h1.right
  linarith

/-- Axiom capturing the empirical fact that a transformer at inference is
    feedforward. Not a philosophical claim — it's an architectural observation
    about the computational graph of a single forward pass. -/
axiom transformer_inference : System
axiom transformerIsFeedforward : isFeedforward transformer_inference

/-- **Corollary 2 (β predicts transformers are not phenomenally conscious).**
    Combining the feedforward theorem with the architectural fact that
    transformers are feedforward at inference, β predicts zero phenomenal
    consciousness for any content in any transformer at inference. -/
theorem transformerNoPhenomenalUnderBeta
    (hBeta : betaAxiom) (hFT : feedforwardTheorem) :
    ∀ (c : Content), ¬ phenomenallyConscious transformer_inference c := by
  intro c
  exact feedforwardNoPhenomenalUnderBeta hBeta hFT
    transformer_inference c transformerIsFeedforward

/-! ## Derived theorems under γ -/

/-- **Corollary 3 (γ is feedforward-independent).** Under γ, a feedforward
    system CAN be phenomenally conscious if its access, self-model, and
    causal load conditions are met. The feedforward property is irrelevant.

    This is γ's key departure from β, and the source of their experimental
    disagreement (attempt_003). -/
theorem gammaFeedforwardIndependent (hGamma : gammaAxiom) :
    ∀ (S : System) (c : Content),
      isFeedforward S
        → accessConscious S c
        → hasRichSelfModel S
        → selfModelRepresents S c
        → selfModelCausalLoad S c > 0
        → phenomenallyConscious S c := by
  intro S c _ hac hsm hrep hload
  exact (hGamma S c).mpr ⟨hac, hsm, hrep, hload⟩

/-! ## The incompatibility theorem -/

/-- A **β-γ witness** is a system and content for which a feedforward
    architecture carries genuine rich self-modeling with nonzero causal load
    on a specific content. If any such witness can be constructed, β and γ
    disagree about its phenomenal status. -/
def isBetaGammaWitness (S : System) (c : Content) : Prop :=
  isFeedforward S
    ∧ accessConscious S c
    ∧ hasRichSelfModel S
    ∧ selfModelRepresents S c
    ∧ selfModelCausalLoad S c > 0

/-- **Main theorem (β-γ incompatibility given a witness).** If β holds, γ
    holds, and there exists a β-γ witness, then we derive a contradiction.
    Therefore, if a witness can be constructed, at most one of β and γ is true.

    This turns the β-vs-γ disagreement from a philosophical dispute into a
    constructive experimental program: build a witness, then measure which
    of the two positions makes the correct prediction about its phenomenal
    status. The experiment was described informally in attempt_003; this
    theorem states its logical role formally. -/
theorem betaAndGammaIncompatibleGivenWitness
    (hBeta : betaAxiom) (hFT : feedforwardTheorem) (hGamma : gammaAxiom)
    (hWitness : ∃ (S : System) (c : Content), isBetaGammaWitness S c) :
    False := by
  obtain ⟨S, c, hff, hac, hsm, hrep, hload⟩ := hWitness
  have h1 : ¬ phenomenallyConscious S c :=
    feedforwardNoPhenomenalUnderBeta hBeta hFT S c hff
  have h2 : phenomenallyConscious S c :=
    gammaFeedforwardIndependent hGamma S c hff hac hsm hrep hload
  exact h1 h2

/-! ## Status of α -/

/-- **α is weaker: its axiom is consistent with almost any predicate
    configuration.** Formally, α only asserts an existential about bridge
    laws and does not constrain which systems are phenomenally conscious.
    This is α's honest status as the principled null. -/
theorem alphaIsPermissive (hAlpha : alphaAxiom) :
    ∀ (S : System) (c : Content),
      phenomenallyConscious S c → ∃ (_ : Type), True := by
  intro S c hpc
  exact hAlpha S c hpc

/-- **α does not refute β or γ.** If α holds, both β and γ can still hold
    (provided their bridge-law commitments are satisfied). α is only decisive
    if one takes it as excluding the specific reductions β and γ propose.
    This is outside the formal structure and belongs in the prose attempts. -/

/-! ## What this file does NOT prove -/

/-
  NOT PROVED HERE:
  - That any β-γ witness actually exists. This is the empirical claim behind
    attempt_003's buildable experiment. Proving it requires constructing a
    specific system, which is outside Lean.
  - That the feedforward theorem holds in IIT 4.0 under all formulations.
    Taken as axiom from the literature; Tononi/Koch would need to confirm
    the reading.
  - That the operational definitions of `hasRichSelfModel` and
    `selfModelCausalLoad` correspond to any specific architectural property.
    These are semantic placeholders awaiting interpretability grounding.
  - Any theorem about α that would distinguish it from trivial.
    α is by its own lights non-constructive; we cannot formalize what
    we cannot specify.
-/

end PhilosophyOfMind
