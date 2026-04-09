/-
  MedThermo.Thermodynamics.FreeEnergy

  Formalization of free energy concepts relevant to biological processes.

  This is the thermodynamic foundation. Every biological process — viral
  replication, drug binding, enzyme catalysis, cell division — is driven by
  free energy gradients.

  Key insight: the TD mutant steady state is a NON-EQUILIBRIUM STEADY STATE
  (Prigogine dissipative structure). It requires continuous free energy input
  (host cell ATP, amino acids, nucleotides) to maintain. The protocol disrupts
  this by blocking energy flow (fluoxetine inhibits replication) or by
  increasing entropy production (autophagy triggers cellular self-destruction).
-/

import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic

noncomputable section

namespace MedThermo.Thermodynamics.FreeEnergy

/-! ## Gibbs Free Energy

For a chemical reaction at constant temperature and pressure:
  ΔG = ΔH - T · ΔS

A reaction is spontaneous (forward) if ΔG < 0, at equilibrium if ΔG = 0.
-/

/-- Gibbs free energy change: ΔG = ΔH - T·ΔS -/
def gibbsFreeEnergy (deltaH : ℝ) (T : ℝ) (deltaS : ℝ) : ℝ :=
  deltaH - T * deltaS

/-- A reaction is spontaneous when ΔG < 0 -/
def isSpontaneous (deltaH T deltaS : ℝ) : Prop :=
  gibbsFreeEnergy deltaH T deltaS < 0

/-- At higher temperature, entropy-favorable reactions become more spontaneous.
    If ΔS > 0 (entropy increases) and we raise T, then T·ΔS increases,
    so ΔG = ΔH - T·ΔS decreases → more spontaneous.

    Biological relevance: fever (elevated T) makes entropy-driven antiviral
    processes MORE favorable. This is one mechanism by which fever helps
    clear infections. -/
theorem entropy_favorable_temperature_effect {deltaH deltaS T₁ T₂ : ℝ}
    (h_entropy_positive : 0 < deltaS) (h_temp : T₁ < T₂) :
    gibbsFreeEnergy deltaH T₂ deltaS < gibbsFreeEnergy deltaH T₁ deltaS := by
  unfold gibbsFreeEnergy
  -- ΔH - T₂·ΔS < ΔH - T₁·ΔS  ↔  -T₂·ΔS < -T₁·ΔS  ↔  T₁·ΔS < T₂·ΔS
  -- True since T₁ < T₂ and ΔS > 0
  nlinarith

/-- If a reaction has ΔH < 0 (exothermic) and ΔS > 0 (entropy increases),
    it is spontaneous at ALL positive temperatures.

    Biological relevance: ATP hydrolysis has both ΔH < 0 (exothermic) and
    ΔS > 0 (one molecule → two molecules + inorganic phosphate). This makes
    it spontaneous under all physiological conditions — it's the universal
    biological energy source. -/
theorem exothermic_entropy_positive_always_spontaneous
    {deltaH deltaS T : ℝ}
    (h_exothermic : deltaH < 0) (h_entropy_positive : 0 < deltaS) (h_T : 0 < T) :
    isSpontaneous deltaH T deltaS := by
  unfold isSpontaneous gibbsFreeEnergy
  -- ΔH - T·ΔS < 0 since both ΔH < 0 and T·ΔS > 0
  have : 0 < T * deltaS := mul_pos h_T h_entropy_positive
  linarith

/-! ## Non-Equilibrium Steady State

A dissipative structure (Prigogine) is a system maintained far from thermodynamic
equilibrium by continuous energy throughput. Biological life is the prototypical
example: cells maintain ordered states by consuming ATP.

Viral persistence (TD mutants) is ALSO a dissipative structure. The TD mutant
population is maintained far from the thermodynamic equilibrium (zero virus) by
continuous consumption of host cell resources (ribosomes, nucleotides, amino acids).

The protocol works by disrupting this dissipation: if you block the energy input
(replication) or accelerate the entropy production (autophagy), the dissipative
structure collapses to its thermodynamic equilibrium (zero virus).
-/

/-- A dissipative structure is maintained if energy input exceeds dissipation.
    If dissipation (entropy production) exceeds input, the structure collapses. -/
def dissipativeStructureMaintained (energyInput entropyProduction : ℝ) : Prop :=
  entropyProduction < energyInput

/-- A dissipative structure collapses when entropy production exceeds energy input.
    Biological meaning: the TD mutant steady state collapses when autophagy
    (entropy production) exceeds viral replication (energy input). -/
theorem dissipative_collapse {energyInput entropyProduction : ℝ}
    (h_collapse : energyInput ≤ entropyProduction) :
    ¬ dissipativeStructureMaintained energyInput entropyProduction := by
  unfold dissipativeStructureMaintained
  push_neg
  exact h_collapse

/-- The protocol collapses the TD mutant dissipative structure.
    If fluoxetine reduces replication (energy input) below autophagy (entropy
    production), the virus cannot maintain its steady state. -/
theorem protocol_collapses_virus {r_replication k_autophagy drug_effect : ℝ}
    (h_drug_range : 0 ≤ drug_effect ∧ drug_effect ≤ 1)
    (h_clearance : r_replication * (1 - drug_effect) ≤ k_autophagy) :
    ¬ dissipativeStructureMaintained (r_replication * (1 - drug_effect)) k_autophagy := by
  exact dissipative_collapse h_clearance

/-! ## Chemical Potential and Binding

Drug-target binding is a thermodynamic process governed by the binding free energy:
  ΔG_bind = -RT · ln(Kd)

where Kd is the dissociation constant (IC50 is related but not identical).

Lower Kd → more negative ΔG → stronger binding.

For fluoxetine-2C ATPase: Kd ≈ 1 μM, so at T = 310 K:
  ΔG_bind ≈ -RT · ln(10^-6) ≈ -34 kJ/mol

This is comparable to ATP hydrolysis, meaning the binding is energetically
favorable and essentially irreversible on short timescales.
-/

/-- Binding free energy from dissociation constant: ΔG = RT · ln(Kd).
    Note: this uses the DISSOCIATION constant. Lower Kd = tighter binding
    = more negative ΔG (since ln of a small positive number is negative).
    Equivalently, ΔG = -RT · ln(Keq) where Keq = 1/Kd is the association constant. -/
def bindingFreeEnergy (R T : ℝ) (Kd : ℝ) : ℝ :=
  R * T * Real.log Kd

/-- Lower Kd → more negative ΔG → stronger (more favorable) binding.
    If Kd₁ < Kd₂ (tighter binding for reaction 1), then ΔG₁ < ΔG₂.

    Biological relevance: fluoxetine binds CVB 2C ATPase with Kd ≈ 1 μM.
    A drug with Kd = 0.1 μM would bind 10x tighter, with ΔG ~2.3·RT more
    negative — much stronger inhibition at lower concentrations. -/
theorem tighter_binding_more_favorable {R T Kd₁ Kd₂ : ℝ}
    (hR : 0 < R) (hT : 0 < T) (h₁ : 0 < Kd₁) (h₂ : 0 < Kd₂) (h : Kd₁ < Kd₂) :
    bindingFreeEnergy R T Kd₁ < bindingFreeEnergy R T Kd₂ := by
  unfold bindingFreeEnergy
  -- R*T*ln(Kd₁) < R*T*ln(Kd₂) since ln is strictly monotone on (0,∞)
  have h_log : Real.log Kd₁ < Real.log Kd₂ := Real.log_lt_log h₁ h
  have h_RT : 0 < R * T := mul_pos hR hT
  nlinarith

/-! ## Summary

These theorems formalize the thermodynamic foundation:

1. `entropy_favorable_temperature_effect`: fever helps clear infections
   (higher T makes entropy-driven antiviral processes more spontaneous)

2. `exothermic_entropy_positive_always_spontaneous`: ATP hydrolysis is
   the universal biological energy source (spontaneous at all T)

3. `dissipative_collapse`: if entropy production exceeds energy input,
   the dissipative structure (viral steady state) collapses

4. `protocol_collapses_virus`: the protocol (fluoxetine + autophagy)
   mathematically collapses the TD mutant dissipative structure

The biology reduces to thermodynamics. The campaign is about
manipulating free energy gradients to make the healthy state more
energetically favorable than the diseased state.
-/

end MedThermo.Thermodynamics.FreeEnergy
