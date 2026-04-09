/-
  MedThermo.CellBiology.ImmunePrivilege

  Formalization of barrier transport for immune-privileged sites.

  The biology: certain tissues (brain, testes, eyes, placenta, pancreatic islets)
  have physical barriers restricting immune cell access. The blood-brain barrier
  (BBB), blood-testis barrier (BTB), and blood-retinal barrier all use tight
  junctions between endothelial cells to create a sealed compartment.

  These sites are "immune-privileged" not because they lack immunity entirely,
  but because antibody and T cell access is severely restricted. This makes them
  CVB reservoirs — viruses that reach these sites can persist indefinitely.

  The mathematics: barrier transport follows Fick's law of diffusion. The flux
  across a barrier depends on permeability × concentration gradient. Small
  lipophilic molecules (like fluoxetine) can cross, but large charged molecules
  (antibodies, T cells) cannot.

  Key insight: the protocol relies on LIPOPHILIC drugs (fluoxetine, BHB) precisely
  because they can cross where immune cells cannot. This is why the protocol
  succeeds where immune-based treatments fail for immune-privileged reservoirs.
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic

noncomputable section

namespace MedThermo.CellBiology.ImmunePrivilege

/-! ## Fick's Law of Diffusion

For a barrier separating two compartments with concentrations c_source and c_target:
  J = P · (c_source - c_target)

where J is the flux across the barrier and P is the permeability coefficient.

The permeability P depends on:
  - Lipophilicity of the molecule (higher logP → higher P for lipid bilayers)
  - Molecular size (smaller → higher P)
  - Charge (uncharged → higher P)
  - Active transport (can enhance or oppose passive diffusion)
-/

/-- Fick's law flux: J = P · (c_source - c_target) -/
def fickFlux (permeability c_source c_target : ℝ) : ℝ :=
  permeability * (c_source - c_target)

/-- At equilibrium (no concentration gradient), flux is zero -/
theorem equilibrium_zero_flux (P c : ℝ) :
    fickFlux P c c = 0 := by
  unfold fickFlux; ring

/-- Flux is positive (source → target) when source concentration exceeds target -/
theorem flux_positive_when_gradient_positive {P c_source c_target : ℝ}
    (hP : 0 < P) (h : c_target < c_source) :
    0 < fickFlux P c_source c_target := by
  unfold fickFlux
  exact mul_pos hP (by linarith)

/-- Flux is monotone in permeability: higher P → higher flux (at fixed gradient) -/
theorem flux_mono_permeability {c_source c_target : ℝ} {P₁ P₂ : ℝ}
    (h_gradient : 0 ≤ c_source - c_target) (h_P : P₁ ≤ P₂) :
    fickFlux P₁ c_source c_target ≤ fickFlux P₂ c_source c_target := by
  unfold fickFlux
  exact mul_le_mul_of_nonneg_right h_P h_gradient

/-! ## Immune Cell Exclusion

Immune cells (T cells, antibodies) have effectively zero permeability across
intact BBB/BTB. Their concentration in privileged compartments is dominated
by local production, not systemic delivery.

Drugs with high lipid solubility (fluoxetine, BHB, small uncharged molecules)
have high permeability and reach privileged compartments via passive diffusion.
-/

/-- Permeability categories (abstract): drug vs immune cell -/
structure BarrierPermeabilities where
  /-- Permeability for fluoxetine (high due to lipophilicity, pKa 10.05) -/
  P_fluoxetine : ℝ
  /-- Permeability for BHB (moderate, small molecule) -/
  P_BHB : ℝ
  /-- Permeability for antibodies (near zero) -/
  P_antibody : ℝ
  /-- Permeability for T cells (near zero, except via active diapedesis) -/
  P_Tcell : ℝ
  /-- All permeabilities are non-negative -/
  all_nonneg : 0 ≤ P_fluoxetine ∧ 0 ≤ P_BHB ∧ 0 ≤ P_antibody ∧ 0 ≤ P_Tcell
  /-- Drugs cross; immune cells don't -/
  drug_dominates : P_antibody < P_fluoxetine ∧ P_Tcell < P_fluoxetine

/-- **The Privileged Site Access Theorem.** For a fixed concentration gradient,
    fluoxetine crosses the barrier more efficiently than antibodies.
    This is the mathematical basis for why the protocol works in immune-privileged
    sites where antibody-based treatments fail. -/
theorem fluoxetine_beats_antibody_at_barrier
    (perms : BarrierPermeabilities)
    (c_plasma c_tissue : ℝ)
    (h_gradient : 0 ≤ c_plasma - c_tissue) :
    fickFlux perms.P_antibody c_plasma c_tissue ≤
    fickFlux perms.P_fluoxetine c_plasma c_tissue := by
  apply flux_mono_permeability h_gradient
  exact le_of_lt perms.drug_dominates.1

/-! ## Steady-State Concentration in Privileged Compartment

For a well-mixed privileged compartment receiving drug via Fick diffusion
and losing drug via elimination (first-order):
  dC_tissue/dt = P · (C_plasma - C_tissue) / V - k_elim · C_tissue

At steady state (dC/dt = 0):
  P · (C_plasma - C_tissue) / V = k_elim · C_tissue
  P · C_plasma / V = C_tissue · (k_elim + P / V)
  C_tissue = P · C_plasma / (V · k_elim + P)

For high permeability (P large): C_tissue → C_plasma (equilibration)
For low permeability (P small): C_tissue → 0 (no penetration)
For zero elimination (k_elim = 0): C_tissue → C_plasma (complete equilibration)
-/

/-- Steady-state tissue concentration under Fick diffusion and first-order elimination.
    Parameters: permeability P, compartment volume V, elimination rate k_elim,
    plasma concentration c_plasma. -/
def steadyStateTissueConc (P V k_elim c_plasma : ℝ) : ℝ :=
  P * c_plasma / (V * k_elim + P)

/-- For positive parameters, the steady-state tissue concentration is non-negative -/
theorem steadyStateConc_nonneg {P V k_elim c_plasma : ℝ}
    (hP : 0 ≤ P) (hV : 0 < V) (hk : 0 ≤ k_elim) (hc : 0 ≤ c_plasma) :
    0 ≤ steadyStateTissueConc P V k_elim c_plasma := by
  unfold steadyStateTissueConc
  apply div_nonneg
  · exact mul_nonneg hP hc
  · have : 0 ≤ V * k_elim := mul_nonneg (le_of_lt hV) hk
    linarith

/-- Steady-state concentration is bounded above by plasma concentration.
    The tissue can never accumulate MORE drug than is in plasma (for passive diffusion
    without active transport or lysosomotropic trapping). -/
theorem steadyStateConc_le_plasma {P V k_elim c_plasma : ℝ}
    (hP : 0 ≤ P) (hV : 0 < V) (hk : 0 ≤ k_elim) (hc : 0 ≤ c_plasma) :
    steadyStateTissueConc P V k_elim c_plasma ≤ c_plasma := by
  unfold steadyStateTissueConc
  have hVk : 0 ≤ V * k_elim := mul_nonneg (le_of_lt hV) hk
  have h_denom_pos : 0 < V * k_elim + P ∨ (V * k_elim + P = 0) := by
    rcases lt_or_eq_of_le (le_of_lt hV) with _ | _
    · by_cases hPP : 0 < P
      · left; linarith
      · push_neg at hPP
        have hP0 : P = 0 := le_antisymm hPP hP
        by_cases hkk : 0 < k_elim
        · left; nlinarith
        · push_neg at hkk
          have hk0 : k_elim = 0 := le_antisymm hkk hk
          right; rw [hP0, hk0]; ring
    · left; linarith
  rcases h_denom_pos with h_pos | h_zero
  · rw [div_le_iff₀ h_pos]
    -- P * c_plasma ≤ c_plasma * (V*k_elim + P)
    -- ↔ P * c_plasma ≤ c_plasma * V*k_elim + c_plasma * P
    -- ↔ 0 ≤ c_plasma * V*k_elim  (true)
    nlinarith
  · rw [h_zero]; simp; exact hc

/-! ## Why Lysosomotropic Drugs Break the Upper Bound

The `steadyStateConc_le_plasma` theorem shows passive diffusion alone can't
accumulate drug above plasma levels. But fluoxetine DOES reach 15x plasma in
brain (measured by ¹⁹F-MRS).

How? Lysosomotropic trapping adds an EFFECTIVE sink: drug entering the cell
gets protonated in acidic lysosomes and can't leave. This is a one-way trap,
which the simple Fick model doesn't capture. The effective permeability is
asymmetric: in is normal, out is blocked.

This is why fluoxetine's tissue concentrations are 2-15x higher than the
simple steady-state model predicts. The IC50 reconciliation (in IC50.lean)
is the proper treatment — just note here that passive Fick diffusion alone
is insufficient to explain the observed accumulation.
-/

/-! ## Biological Interpretation

1. `equilibrium_zero_flux`: At equilibrium, no net drug movement. This is
   when steady state is reached.

2. `flux_positive_when_gradient_positive`: Drug flows from plasma into tissue
   as long as plasma concentration is higher. This is why continuous dosing
   maintains therapeutic levels.

3. `flux_mono_permeability`: Higher permeability = more drug crosses per unit
   time. Fluoxetine (high P) reaches brain quickly; antibodies (low P) don't.

4. `fluoxetine_beats_antibody_at_barrier`: The mathematical statement of why
   the protocol works in immune-privileged sites. Small lipophilic drugs
   cross barriers that block immune-based treatments.

5. `steadyStateConc_nonneg` + `steadyStateConc_le_plasma`: Simple passive
   diffusion gives tissue concentrations bounded by plasma. Lysosomotropic
   trapping is NEEDED to explain the observed 2-15x tissue/plasma ratios.
-/

end MedThermo.CellBiology.ImmunePrivilege
