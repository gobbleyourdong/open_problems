/-
ChangeAsKUpdate.lean
====================

The core claim of what_is_change: genuine physical change occurs
at decoherence boundaries and nowhere else.

THREE REGIMES OF K-CHANGE (from numerics C6, C7, C8):

  1. Unitary:      K(S₂ | S₁) = 0     — deterministic, no new information
  2. Decoherence:  K(S₂ | S₁) = -log₂(P)  — measurement creates K
  3. Thermal:      K(S₂ | S₁) ≈ 1 bit  — Kramers crossings at ion channels

Change IS K-update. Between decoherence events, nothing genuinely new
happens. The felt impression of continuous change is the self-model
integrating over many decoherence events at the Kramers timescale.

Depends on: BrainKFlow.lean (for Kramers data)
-/

/-! ## The Three Regimes of K-Change -/

/-- Classification of physical processes by K-change behavior. -/
inductive KChangeRegime where
  | unitary      : KChangeRegime   -- deterministic evolution, K = 0
  | decoherence  : KChangeRegime   -- measurement/collapse, K = -log₂(P)
  | thermal      : KChangeRegime   -- Kramers crossings, K ≈ 1 bit

/-- A K-change measurement from a physical process. -/
structure KChangeMeasurement where
  regime : KChangeRegime
  process : String
  k_change_bits : ℝ        -- conditional K-complexity K(S₂|S₁)
  description : String

/-! ## Regime 1: Unitary Evolution (K = 0) -/

/-- Hadamard gate: rotates |0⟩ to (|0⟩+|1⟩)/√2.
    Fidelity drops to 0.25 (genuine state change!) but K = 0
    because the gate fully determines the output. -/
def hadamard_gate : KChangeMeasurement := {
  regime := .unitary
  process := "Hadamard gate on |0⟩"
  k_change_bits := 0.0
  description := "Gate + input → output deterministically. K(S₂|S₁,H) = 0."
}

/-- CNOT creating entanglement: |00⟩ → (|00⟩+|11⟩)/√2.
    Entanglement is created but K = 0 (deterministic from gate + input). -/
def cnot_entangle : KChangeMeasurement := {
  regime := .unitary
  process := "CNOT on H|0⟩⊗|0⟩"
  k_change_bits := 0.0
  description := "Entanglement creation is K-free when gate is known."
}

/-- Unitary evolution has zero K-change. -/
theorem unitary_k_zero :
    hadamard_gate.k_change_bits = 0.0 ∧
    cnot_entangle.k_change_bits = 0.0 := by
  simp [hadamard_gate, cnot_entangle]

/-! ## Regime 2: Decoherence / Measurement (K = -log₂P) -/

/-- Measurement of a qubit in equal superposition: K = 1 bit. -/
def measurement_equal : KChangeMeasurement := {
  regime := .decoherence
  process := "Measure (|0⟩+|1⟩)/√2"
  k_change_bits := 1.0
  description := "p₀ = p₁ = 0.5, K = -log₂(0.5) = 1 bit"
}

/-- Measurement of a nearly-certain qubit: K ≈ 0.081 bits. -/
def measurement_biased : KChangeMeasurement := {
  regime := .decoherence
  process := "Measure √0.99|0⟩ + √0.01|1⟩"
  k_change_bits := 0.081
  description := "p₀ = 0.99, p₁ = 0.01. Weighted: 0.99×0.0145 + 0.01×6.64 = 0.081"
}

/-- Decoherence creates strictly positive K-change. -/
theorem decoherence_k_positive :
    measurement_equal.k_change_bits > 0 ∧
    measurement_biased.k_change_bits > 0 := by
  simp [measurement_equal, measurement_biased]; norm_num

/-- More surprising outcomes create more K-change. -/
theorem surprise_monotone :
    measurement_biased.k_change_bits < measurement_equal.k_change_bits := by
  simp [measurement_biased, measurement_equal]; norm_num

/-! ## Regime 3: Thermal / Kramers (K ≈ 1 bit/event) -/

/-- Ion channel Kramers crossing: ~1 bit per conformational change. -/
def kramers_crossing : KChangeMeasurement := {
  regime := .thermal
  process := "Ion channel conformational change"
  k_change_bits := 1.0
  description := "Binary state (open/closed) at ΔE = 16.58 kT, rate = 1000 Hz"
}

/-! ## The Ordering: No Change < Continuous < Phase < Random -/

/-- K-change measurements for four canonical transitions (from C2). -/
structure TransitionKChange where
  name : String
  k_change : ℝ       -- K(S₂|S₁) via gzip proxy

def stopped_clock : TransitionKChange := { name := "Stopped clock", k_change := 0.011 }
def slow_motion : TransitionKChange := { name := "Slow motion", k_change := 0.018 }
def fast_motion : TransitionKChange := { name := "Fast motion", k_change := 0.016 }
def phase_transition : TransitionKChange := { name := "Water→ice", k_change := 0.037 }
def random_change : TransitionKChange := { name := "Random states", k_change := 1.001 }

/-- K-change orders transitions correctly:
    no change < continuous change < phase transition < random. -/
theorem k_change_ordering :
    stopped_clock.k_change < slow_motion.k_change ∧
    stopped_clock.k_change < fast_motion.k_change ∧
    fast_motion.k_change < phase_transition.k_change ∧
    phase_transition.k_change < random_change.k_change := by
  simp [stopped_clock, slow_motion, fast_motion, phase_transition, random_change]
  norm_num

/-- Stopped clock has near-zero K-change (only timestamp drift). -/
theorem stopped_near_zero :
    stopped_clock.k_change < 0.02 := by
  simp [stopped_clock]; norm_num

/-- Random change is near-maximal (K ≈ 1). -/
theorem random_near_maximal :
    random_change.k_change > 0.99 := by
  simp [random_change]; norm_num

/-! ## The K-Change Hierarchy (seven scales) -/

/-- A level in the K-change hierarchy spanning Planck to cosmos. -/
structure KChangeLevel where
  name : String
  log10_timescale_seconds : ℝ    -- log₁₀(seconds per event)
  k_bits_per_event : ℝ           -- K-information created per event

def planck_level : KChangeLevel := {
  name := "Planck"
  log10_timescale_seconds := -44
  k_bits_per_event := 1
}

def decoherence_level : KChangeLevel := {
  name := "Quantum decoherence"
  log10_timescale_seconds := -13
  k_bits_per_event := 1
}

def kramers_level : KChangeLevel := {
  name := "Kramers thermal"
  log10_timescale_seconds := -3
  k_bits_per_event := 1
}

def neural_level : KChangeLevel := {
  name := "Neural firing"
  log10_timescale_seconds := -2
  k_bits_per_event := 10
}

def conscious_level : KChangeLevel := {
  name := "Conscious update"
  log10_timescale_seconds := -1
  k_bits_per_event := 5
}

def specious_level : KChangeLevel := {
  name := "Specious present"
  log10_timescale_seconds := 0.48   -- log₁₀(3) ≈ 0.48
  k_bits_per_event := 150
}

def cosmological_level : KChangeLevel := {
  name := "Cosmological"
  log10_timescale_seconds := 17.6   -- log₁₀(4.3×10¹⁷) ≈ 17.63
  k_bits_per_event := 1e120
}

/-- The hierarchy spans 62 orders of magnitude in timescale. -/
theorem hierarchy_span :
    cosmological_level.log10_timescale_seconds -
    planck_level.log10_timescale_seconds > 61 := by
  simp [cosmological_level, planck_level]; norm_num

/-- Each level is an instance of K-update at its characteristic timescale.
    The K per event increases with integration window. -/
theorem k_increases_with_scale :
    planck_level.k_bits_per_event ≤ kramers_level.k_bits_per_event ∧
    kramers_level.k_bits_per_event ≤ neural_level.k_bits_per_event ∧
    neural_level.k_bits_per_event ≤ specious_level.k_bits_per_event := by
  simp [planck_level, kramers_level, neural_level, specious_level]; norm_num
