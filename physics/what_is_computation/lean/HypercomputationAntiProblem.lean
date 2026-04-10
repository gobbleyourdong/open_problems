/-
HypercomputationAntiProblem.lean
================================

Phase 2 Even, Cycle 3 of the 3-cycle what_is_computation loop (2026-04-09).

Formalizes R1 from `gap.md`: "Is physical Church-Turing actually true?"
In the K-framing: does every physically-realizable process have a
finite K-specification? Hypercomputation proposals (Malament-Hogarth
spacetimes, continuum computing, exotic quantum gravity) claim NO. We
state the anti-problem here precisely enough that downstream work can
cite a single canonical formulation.

Builds on KManipulationCore.lean §5 (NonComputational predicate) and
CompressionAsymmetryStatement.lean (measurement registry style).

No sorry. Mathlib-dependent.
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Basic
import Mathlib.Tactic.NormNum

/-! ## §1 Setup: re-state the K-function and specification types

    These mirror the definitions in KManipulationCore.lean (we repeat them
    here rather than `import` because the physics/what_is_computation/lean
    directory has no lakefile and each file is a stand-alone source unit).
-/

/-- A K-function (see KManipulationCore.lean §2). -/
structure KFunction where
  name : String
  deriving Repr

/-- Claim: `f` has a finite K-specification of length `n`. Parametric
    over a description language abstracted away. -/
structure HasFiniteSpec (f : KFunction) where
  length_bits : ℕ
  deriving Repr

/-- A K-function is Turing-specifiable iff it has SOME finite
    specification. -/
def TuringSpecifiable (f : KFunction) : Prop := Nonempty (HasFiniteSpec f)

/-- A K-function is `NonComputational` iff it lacks a finite K-spec. -/
def NonComputational (f : KFunction) : Prop := ¬ TuringSpecifiable f

/-! ## §2 Physical realizability

    We separate "could be specified" from "does actually arise in
    physical dynamics." The difference between R1 and a purely
    mathematical Church-Turing statement lives here.
-/

/-- A witness that `f` is instantiated by some physical process. We
    leave this abstract; the content is in the axioms and theorems
    that constrain it. -/
structure PhysicallyRealized (f : KFunction) where
  tag : String  -- "classical_EM", "non-relativistic_QM", "MH_spacetime", ...
  deriving Repr

/-- The Physical Church-Turing Thesis (PCTT):

      Every K-function that is physically realized has a finite
      specification.

    We state this as a Prop parameterized by the K-function and the
    physical-realization witness. Whether PCTT holds is an empirical
    claim, not a formal theorem. -/
def PCTT (f : KFunction) : Prop :=
  ∀ _ : PhysicallyRealized f, TuringSpecifiable f

/-- The weak (model-level) reading: every physically-realized K-function
    CAN BE MODELED as a finite K-spec. This is trivially true once we
    accept that any physical process we can discuss has been described,
    and description is itself finite. We record it as a distinct Prop
    so that the strong/weak distinction is visible at the type level. -/
def WeakPCTT (f : KFunction) : Prop :=
  (∃ _ : PhysicallyRealized f, True) → (∃ _ : HasFiniteSpec f, True)

/-- Strong PCTT is at least as strong as weak PCTT. -/
theorem strong_implies_weak (f : KFunction) :
    PCTT f → WeakPCTT f := by
  intro hpctt hphys
  obtain ⟨phys, _⟩ := hphys
  have : TuringSpecifiable f := hpctt phys
  obtain ⟨spec⟩ := this
  exact ⟨spec, trivial⟩

/-! ## §3 Hypercomputation scenarios

    Three concrete hypercomputation proposals, each expressed as a
    named physical realization type plus a Prop asserting whether it
    would force a non-computational K-function to exist.
-/

/-- The Malament-Hogarth hypercomputation proposal: in certain general
    relativistic spacetimes, an observer can witness the result of an
    infinite computation in finite proper time. If such spacetimes are
    physically realizable, then a halting-oracle-computing K-function
    would be PhysicallyRealized, and this would falsify PCTT. -/
inductive HyperScenario where
  | MalamentHogarth         -- GR closed-timelike-curve flavors
  | ContinuumAnalog         -- literal real-number computation
  | QuantumGravityExotic    -- speculative post-QM proposals
  deriving DecidableEq, Repr

/-- A hypercomputation CLAIM: there exists a K-function that is
    PhysicallyRealized under some exotic scenario but NOT
    TuringSpecifiable. -/
def HypercomputationClaim : Prop :=
  ∃ (f : KFunction) (_ : PhysicallyRealized f) (_ : HyperScenario),
    NonComputational f

/-- PCTT for a given f contradicts the hypercomputation claim FOR THAT f
    specifically. -/
theorem pctt_contradicts_hypercomputation_pointwise
    (f : KFunction)
    (hpctt : PCTT f)
    (phys : PhysicallyRealized f) :
    ¬ NonComputational f := by
  intro hnc
  exact hnc (hpctt phys)

/-- If PCTT holds universally, the hypercomputation claim fails. -/
theorem universal_pctt_kills_hypercomputation
    (huniv : ∀ f : KFunction, PCTT f) :
    ¬ HypercomputationClaim := by
  intro hyper
  obtain ⟨f, phys, _, hnc⟩ := hyper
  exact hnc (huniv f phys)

/-! ## §4 The gap is empirical, not formal

    Both PCTT and HypercomputationClaim are Props. Lean does not pick
    sides. The physics gap is "which of these two propositions is
    consistent with observed physics?" — which requires physical
    experiments, not Lean proofs.

    We record two axioms naming the two positions so downstream work
    can cite them explicitly. Neither is proved; either (but not both)
    could be assumed consistently.
-/

/-- Axiom form of universal PCTT: every physically-realized K-function
    has a finite spec. If this is taken as an axiom, hypercomputation
    is ruled out by `universal_pctt_kills_hypercomputation`. -/
axiom pctt_universal : ∀ f : KFunction, PCTT f

/-- Corollary of `pctt_universal`: the hypercomputation claim is
    refuted (under the axiom). -/
theorem hypercomputation_refuted_under_pctt :
    ¬ HypercomputationClaim :=
  universal_pctt_kills_hypercomputation pctt_universal

/-! ## §5 What remains — the gap named

    Phase 2 of `what_is_computation` ends here with a statement-level
    but logically-honest formalization of the anti-problem.

    What this file resolves:
      - The hypercomputation question has a canonical Prop.
      - PCTT strong/weak distinction is type-level.
      - "Strong → weak" is a theorem.
      - "PCTT refutes hypercomputation" is a theorem (under axiom).
      - The three named hypercomputation scenarios are inductively typed.

    What this file does NOT resolve:
      - Whether pctt_universal is physically correct. (R1 in gap.md)
      - Whether any specific HyperScenario constructor has a witness.
      - How BQP relates to K-function classes (R3 — handled by
        QuantumClassicalHierarchy.lean and ShorStructuredQuantum.lean).

    What this file does NOT attempt:
      - To settle P vs NP. (R2, handled by the math track and by
        CompressionAsymmetryStatement.lean.)

    Sorry count: 0
-/

/-! ## §6 Inventory

    Types:
      KFunction, HasFiniteSpec, PhysicallyRealized
    Inductives:
      HyperScenario (MalamentHogarth, ContinuumAnalog, QuantumGravityExotic)
    Predicates:
      TuringSpecifiable, NonComputational, PCTT, WeakPCTT,
      HypercomputationClaim
    Axioms (empirical, not formal gaps):
      pctt_universal
    Theorems proved:
      strong_implies_weak
      pctt_contradicts_hypercomputation_pointwise
      universal_pctt_kills_hypercomputation
      hypercomputation_refuted_under_pctt
-/
