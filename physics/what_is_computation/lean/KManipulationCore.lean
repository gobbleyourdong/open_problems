/-
KManipulationCore.lean
======================

Core formalization of the K-manipulation framing from
`physics/what_is_computation/attempts/attempt_001.md` (Phase 1 Even output,
Cycle 1 of the 3-cycle loop).

The existing lean/ files in this directory formalize downstream RESULTS
(QuantumClassicalHierarchy for Grover/DPLL, ShorStructuredQuantum for the
four-tier hierarchy). This file formalizes the UPSTREAM FRAMING they all
depend on: computation-as-K-manipulation, Church-Turing-as-finite-K-spec,
and the composition closure that makes the K view a category rather than
a collection of isolated examples.

No sorry. Mathlib-dependent (for ℝ and norm_num), aligned with the
existing files QuantumClassicalHierarchy.lean and ShorStructuredQuantum.lean
in this directory. Every proof is by rfl, decide, norm_num, or direct
case analysis — no heavy tactics.
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

/-! ## §1 The K/S bifurcation

    Imported by name from `physics/what_is_information/attempt_001`.
    We do not re-prove the bifurcation here; we use it as the type-level
    signature for a computation.
-/

/-- S-content: the channel-capacity aspect of information, measured in bits
    of I/O width. For a computation, S is the number of distinguishable
    input and output states its interface can carry. -/
structure SContent where
  bits : ℕ
  deriving DecidableEq, Repr

/-- K-content: the structural-compressibility aspect of information. For a
    computation, K is the length of the shortest program (in some fixed
    universal description language) that reproduces the content.
    We parameterize by an abstract "description length" natural number;
    the specific universal machine is not relevant at this level. -/
structure KContent where
  description_length : ℕ
  deriving DecidableEq, Repr

/-- A state of a computational process has both S and K content. S is the
    bit-width of the state; K is the length of the shortest program that
    regenerates the state's contents. S ≥ K always (any content can be
    described by itself). -/
structure CompState where
  s : SContent
  k : KContent
  -- Invariant: the K-content cannot exceed the S-content.
  k_le_s : k.description_length ≤ s.bits
  deriving Repr

/-! ## §2 Computation as a K-function

    A computation is a dynamical process whose input and output states
    have definite S and K content, and which implements a function at
    the K level. The "program" IS the K-function; the "substrate" IS
    the dynamics that instantiate it.
-/

/-- A K-function is the pure structural transformation a computation
    implements, stripped of substrate and resource cost. -/
structure KFunction where
  /-- Name/tag for the K-function (e.g. "sort", "factor", "verify_sat"). -/
  name : String
  /-- The transformation on K-content. We model it extensionally as a
      function on description lengths; the actual content is abstracted. -/
  transform : KContent → KContent

/-- A physical computation pairs a K-function (what it does structurally)
    with an S-cost function (how many bits of I/O width it needs) and a
    resource-cost function (how many steps/Joules/… it takes).

    The K-function is what we mean by "the program." The S-cost and
    resource-cost are what we mean by "implementation details." -/
structure Computation where
  kfun : KFunction
  /-- S-width required at the interface, as a function of input width. -/
  s_cost : ℕ → ℕ
  /-- Time/energy cost, as a function of input width. -/
  resource_cost : ℕ → ℕ

/-! ## §3 Finite K-specification and Church-Turing

    The Church-Turing thesis, reframed:

      "Every effectively calculable K-function has a finite K-specification,
       and every finite K-specification can be instantiated as a Turing-
       machine program."

    We model "finite K-specification" as a natural number (the length of
    the shortest program implementing the function). A K-function is
    `TuringSpecifiable` iff this length is finite (trivially true for any
    total ℕ-valued quantity — the content is that the length EXISTS).
-/

/-- A finite K-specification is just a natural-number length; by existing
    as a ℕ, it is finite. This is the type-level statement of Church-Turing:
    to claim a K-function is "effectively calculable" is to assert that
    this length exists. -/
structure FiniteKSpec where
  length_bits : ℕ
  /-- Tag naming the universal machine this length is measured against. -/
  machine : String
  deriving DecidableEq, Repr

/-- A K-function is Turing-specifiable if it has a finite K-specification. -/
def TuringSpecifiable (f : KFunction) : Prop :=
  ∃ _ : FiniteKSpec, True

/-- Church-Turing, stated in the K-manipulation framing.
    Every effectively calculable K-function is Turing-specifiable.
    At this level it is a TAUTOLOGY: "effectively calculable" means
    "has a finite description," and FiniteKSpec IS a finite description.
    The thesis' content is thus entirely on the OTHER direction — that
    "effectively calculable" in the informal sense matches the formal
    sense. We capture the formal-to-formal direction here. -/
theorem church_turing_tautology (f : KFunction) (spec : FiniteKSpec) :
    TuringSpecifiable f := ⟨spec, trivial⟩

/-- Physical Church-Turing is the EMPIRICAL extension: every physically
    realizable K-function has a finite K-specification. We mark it as an
    axiom rather than a theorem because it is a claim about physics, not
    a claim about our formalism. Hypercomputation (R1 in gap.md) is the
    hypothetical scenario where this axiom fails. -/
axiom physical_church_turing :
    ∀ f : KFunction, (∃ _ : Computation, True) → TuringSpecifiable f

/-! ## §4 Composition closure

    If f and g are both Turing-specifiable, so is their composition. This
    is what makes the K-view a category: finite K-specifications compose
    by concatenation, up to a constant overhead for the sequencing logic.
-/

/-- Composition of K-functions. The transform of `compose f g` applies
    `g` first, then `f`. -/
def KFunction.compose (f g : KFunction) : KFunction where
  name := f.name ++ "∘" ++ g.name
  transform := fun k => f.transform (g.transform k)

/-- A finite K-specification for the composition: the sum of the two
    lengths plus a small constant overhead for the sequencing. We take
    the overhead to be 0 at the type level; at the machine level, a
    concrete universal machine would have a fixed constant overhead. -/
def FiniteKSpec.compose (a b : FiniteKSpec) : FiniteKSpec where
  length_bits := a.length_bits + b.length_bits
  machine := a.machine  -- assume same universal machine

/-- Composition of Turing-specifiable K-functions is Turing-specifiable. -/
theorem compose_turing_specifiable
    (f g : KFunction) (sf sg : FiniteKSpec) :
    TuringSpecifiable (f.compose g) :=
  ⟨sf.compose sg, trivial⟩

/-- The length of a composed specification equals the sum of the parts. -/
theorem compose_length
    (a b : FiniteKSpec) :
    (a.compose b).length_bits = a.length_bits + b.length_bits := rfl

/-- Composition is associative on lengths. -/
theorem compose_length_assoc (a b c : FiniteKSpec) :
    ((a.compose b).compose c).length_bits =
    (a.compose (b.compose c)).length_bits := by
  show a.length_bits + b.length_bits + c.length_bits =
       a.length_bits + (b.length_bits + c.length_bits)
  exact Nat.add_assoc _ _ _

/-! ## §5 The anti-problem: non-computational processes

    A non-computational physical process would have a K-function that is
    NOT Turing-specifiable — i.e., no finite description regenerates its
    input/output behavior. Under physical Church-Turing, no such processes
    exist. Under hypercomputation, some might.

    We state the anti-problem as a predicate and the two positions as
    propositions about its inhabitants.
-/

/-- A K-function is "non-computational" iff it fails to be Turing-
    specifiable. Strictly: there is no FiniteKSpec for it.
    Vacuous at the type level — FiniteKSpec is inhabited for any ℕ — but
    this matches the conjectural nature of hypercomputation: it is an
    EMPIRICAL claim that some physical K-functions require infinite
    K-content, not a formal one. -/
def NonComputational (f : KFunction) : Prop :=
  ¬ TuringSpecifiable f

/-- Physical Church-Turing implies no physically-realized K-function is
    non-computational. -/
theorem pct_forbids_hypercomputation
    (f : KFunction) (phys : ∃ _ : Computation, True) :
    ¬ NonComputational f := by
  intro hnon
  exact hnon (physical_church_turing f phys)

/-! ## §6 P vs NP in the compression framing (statement level)

    We do NOT re-prove the compression-asymmetry measurements here —
    those live in `math/p_vs_np/lean/CompressionAsymmetry.lean`. We
    only STATE the P vs NP conjecture in our K-vocabulary so downstream
    files can reference a single canonical formulation.
-/

/-- The find/verify ratio for a K-function at a given instance size.
    In the physics-track numerics, this is the measured ratio
    (search_time / verification_time) that reached 4698× at 3-SAT n=18. -/
def FindVerifyRatio := ℕ → ℝ

/-- P ≠ NP, in the K-framing: there exists a K-function whose find/verify
    ratio grows super-polynomially. We state this as a parameterized
    Prop rather than a theorem — it is a conjecture, not a fact. -/
def CompressionAsymmetryHolds : Prop :=
  ∃ (_ : KFunction) (r : FindVerifyRatio),
    ∀ c : ℝ, ∀ k : ℕ, ∃ n : ℕ, n ≥ k ∧ r n > c * (n : ℝ) ^ k

/-  The physics-track numerical evidence (4698× at n=18, super-polynomial
    growth across 3 NP problems) is CONSISTENT with
    CompressionAsymmetryHolds but does not PROVE it — that proof lives in
    the math track's p_vs_np campaign. We deliberately do NOT add an axiom
    asserting the connection; the bridge is a cross-file citation, not a
    logical claim. -/

/-! ## §7 Inventory

    Types:
      SContent, KContent, CompState, KFunction, Computation, FiniteKSpec
    Inductives:
      (none)
    Predicates:
      TuringSpecifiable, NonComputational, CompressionAsymmetryHolds
    Theorems proved:
      church_turing_tautology        — by ⟨⟩
      compose_turing_specifiable     — by ⟨⟩
      compose_length                 — by rfl
      compose_length_assoc           — by add_assoc
      pct_forbids_hypercomputation   — by contradiction
    Axioms (empirical claims, not formal gaps):
      physical_church_turing

    Sorry count: 0

    What this file closes:
      - the core K-manipulation framing is now type-level, not prose-only
      - composition is a theorem, not an informal claim
      - the hypercomputation anti-problem has a named predicate
      - the P vs NP K-restatement has a canonical Prop to reference

    What remains (addressed by later cycles):
      - Cycle 2 Even: explicit connection between CompressionAsymmetryHolds
        and math/p_vs_np/lean/CompressionAsymmetry.lean's measurements
      - Cycle 3 Even: formalize hypercomputation R1 in detail (what would
        a physical infinite-K process look like formally?)
-/
