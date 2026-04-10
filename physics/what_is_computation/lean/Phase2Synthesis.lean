/-
Phase2Synthesis.lean
====================

Phase 2 Even, Cycle 6 of the 3-cycle what_is_computation loop 2 (2026-04-09).

Ties together the six Lean files in `physics/what_is_computation/lean/`
into a single synthesis object. The goal is not new theorems — every
theorem cited below is already proved in its home file — but to
make the PHASE 2 INVENTORY type-level, so the completion of the phase
is itself an object Lean can see.

The six files:

  KManipulationCore.lean           — the K-framing, Church-Turing
  CompressionAsymmetryStatement.lean — P vs NP in K-vocabulary, prefix insufficiency
  HypercomputationAntiProblem.lean — R1 statement-level
  QuantumClassicalHierarchy.lean   — Grover vs DPLL vs exhaustive
  ShorStructuredQuantum.lean       — Shor + four-tier hierarchy
  StructureVsSubstrate.lean        — the 2×2 structure/substrate grid

No sorry. Mathlib-dependent.
-/

import Mathlib.Data.Nat.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

/-! ## §1 The four residuals from gap.md

    We encode the four open questions (R1, R2, R3, R4 = K-trajectory
    universality) as Lean propositions with tags indicating which file
    carries the canonical statement.
-/

/-- Status tag for each residual question. -/
inductive ResidualStatus where
  | OpenEmpirical        -- physical experiments needed, not provable in Lean
  | OpenMathematical     -- proof belongs to another track
  | Closed               -- closed by one of the phase-2 files
  | PartiallyClosed      -- partial progress this loop
  deriving DecidableEq, Repr

/-- A residual question, tagged with its home file and current status. -/
structure Residual where
  name : String
  home_file : String
  status : ResidualStatus
  deriving Repr

/-- R1: is physical Church-Turing actually true? (hypercomputation) -/
def R1_hypercomputation : Residual :=
  { name := "R1_hypercomputation"
    home_file := "HypercomputationAntiProblem.lean"
    status := ResidualStatus.OpenEmpirical }

/-- R2: is P ≠ NP? (compression asymmetry) -/
def R2_p_vs_np : Residual :=
  { name := "R2_p_vs_np"
    home_file := "CompressionAsymmetryStatement.lean"
    status := ResidualStatus.OpenMathematical }

/-- R3: substrate-dependence of K-manipulation (BQP vs P) -/
def R3_bqp_substrate : Residual :=
  { name := "R3_bqp_substrate"
    home_file := "StructureVsSubstrate.lean"
    status := ResidualStatus.Closed }

/-- R4: K-trajectory fingerprint universality.
    After loop 3 Cycle 8 Odd, the F1 direction (hard → K flat) is
    confirmed on three independent NP families (SAT, Ham cycle,
    3-coloring) under the constraint-remnant proxy. The F2 direction
    (easier → K decreasing) remains SAT-specific. We upgrade the
    status to `PartiallyClosed` for F1+F2 composite, and retain it
    (no stronger tag than "PartiallyClosed" exists yet). -/
def R4_k_trajectory : Residual :=
  { name := "R4_k_trajectory"
    home_file := "lean/ConstraintRemnantDynamics.lean"
    status := ResidualStatus.PartiallyClosed }

/-- The full residual set for physics/what_is_computation. -/
def residuals : List Residual :=
  [R1_hypercomputation, R2_p_vs_np, R3_bqp_substrate, R4_k_trajectory]

/-! ## §2 Phase 2 is in the state "one residual closed, three open" -/

/-- A residual counts as closed iff its status is `Closed`. -/
def isClosed (r : Residual) : Bool :=
  match r.status with
  | ResidualStatus.Closed => true
  | _ => false

/-- The number of residuals closed. -/
def closed_count : ℕ :=
  (residuals.filter (fun r => isClosed r)).length

/-- Exactly one residual is closed at the end of loop 2 (R3: substrate).  -/
theorem exactly_one_closed : closed_count = 1 := by
  -- Elaborates to List.length [R3_bqp_substrate] = 1.
  decide

/-- R3 is the one that is closed. -/
theorem R3_is_closed : isClosed R3_bqp_substrate = true := by
  decide

/-- R1 is open empirically. -/
theorem R1_open : R1_hypercomputation.status = ResidualStatus.OpenEmpirical := rfl

/-- R2 is open mathematically. -/
theorem R2_open : R2_p_vs_np.status = ResidualStatus.OpenMathematical := rfl

/-- R4 is partially closed (this loop). -/
theorem R4_partial : R4_k_trajectory.status = ResidualStatus.PartiallyClosed := rfl

/-! ## §3 File dependency graph

    We encode which files cite which, so the six-file structure is type-level.
-/

/-- A named citation from one Lean file to another. -/
structure FileCitation where
  from_file : String
  to_file : String
  reason : String
  deriving Repr

def core_cites_nothing : FileCitation :=
  { from_file := "KManipulationCore.lean"
    to_file := "(root)"
    reason := "top of the K-framing stack" }

def asymmetry_cites_core : FileCitation :=
  { from_file := "CompressionAsymmetryStatement.lean"
    to_file := "KManipulationCore.lean"
    reason := "CompressionAsymmetryHolds Prop lives in core" }

def hyper_cites_core : FileCitation :=
  { from_file := "HypercomputationAntiProblem.lean"
    to_file := "KManipulationCore.lean"
    reason := "NonComputational predicate lives in core" }

def hierarchy_cites_core : FileCitation :=
  { from_file := "QuantumClassicalHierarchy.lean"
    to_file := "KManipulationCore.lean"
    reason := "K-search strategies are a K-function refinement" }

def shor_cites_hierarchy : FileCitation :=
  { from_file := "ShorStructuredQuantum.lean"
    to_file := "QuantumClassicalHierarchy.lean"
    reason := "four-tier hierarchy extends the three-tier one" }

def structsub_cites_hierarchy : FileCitation :=
  { from_file := "StructureVsSubstrate.lean"
    to_file := "QuantumClassicalHierarchy.lean"
    reason := "2×2 grid is the abstraction of the k-values" }

def structsub_cites_shor : FileCitation :=
  { from_file := "StructureVsSubstrate.lean"
    to_file := "ShorStructuredQuantum.lean"
    reason := "structured-quantum corner uses Shor's k = ∞" }

/-- Loop 3 addition: ConstraintRemnantDynamics cites the asymmetry
    file because FingerprintClaim shares vocabulary with
    FVRatio/SuperPolynomial. -/
def cgrd_cites_asymmetry : FileCitation :=
  { from_file := "ConstraintRemnantDynamics.lean"
    to_file := "CompressionAsymmetryStatement.lean"
    reason := "FingerprintClaim status tags describe FVRatio behavior" }

def citations : List FileCitation :=
  [core_cites_nothing, asymmetry_cites_core, hyper_cites_core,
   hierarchy_cites_core, shor_cites_hierarchy,
   structsub_cites_hierarchy, structsub_cites_shor,
   cgrd_cites_asymmetry]

/-- The dependency graph has exactly 8 edges after loop 3 (counting the
    root self-edge). -/
theorem citation_count : citations.length = 8 := by decide

/-! ## §4 Sorry-free declaration

    The claim that all six files are sorry-free is empirical (depends
    on file contents, not type theory). We record it as a data
    constant rather than a theorem, so any future file added to the
    phase-2 set MUST update this list explicitly.
-/

/-- The set of phase-2 Lean files in this directory. Loop 3 added
    `ConstraintRemnantDynamics.lean`, bringing the count to 7. -/
def phase2_files : List String :=
  [ "KManipulationCore.lean"
  , "CompressionAsymmetryStatement.lean"
  , "HypercomputationAntiProblem.lean"
  , "QuantumClassicalHierarchy.lean"
  , "ShorStructuredQuantum.lean"
  , "StructureVsSubstrate.lean"
  , "ConstraintRemnantDynamics.lean"
  ]

/-- The phase-2 file set has exactly 7 entries (after loop 3). -/
theorem seven_phase2_files : phase2_files.length = 7 := by decide

/-! ## §5 Inventory

    Inductives:
      ResidualStatus (OpenEmpirical, OpenMathematical, Closed,
                      PartiallyClosed)
    Structures:
      Residual (name, home_file, status)
      FileCitation (from_file, to_file, reason)
    Definitions:
      R1_hypercomputation, R2_p_vs_np, R3_bqp_substrate, R4_k_trajectory
      residuals, isClosed, closed_count
      seven citation constants, citations list
      phase2_files
    Theorems proved:
      exactly_one_closed     — decide
      R3_is_closed           — decide
      R1_open, R2_open, R4_partial — rfl
      citation_count         — decide
      seven_phase2_files     — decide  (updated loop 3)
    Sorry count: 0

    What this file closes:
      - Phase 2's residual set is a type-level object, not prose-only
      - The six-file dependency graph is type-level
      - "Exactly one residual is closed" is a theorem

    What this file does NOT close:
      - R1, R2 (still open per their status tags)
      - R4 (partially closed this loop; stronger Ham cycle evidence
        needed per `landscape_k_hamiltonian_findings.md`)
-/
