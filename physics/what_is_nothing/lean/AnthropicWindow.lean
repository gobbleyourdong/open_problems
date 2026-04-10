/-
AnthropicWindow.lean
====================

Formalization of the Weinberg anthropic argument for the cosmological
constant from `physics/what_is_nothing/results/anthropic_findings.md`.

THE RESULT: the anthropic window explains ~1-2 orders of the 140-order
CCP gap. The remaining 138+ orders are NOT explained by selection.

  CC problem:              rho_Planck / rho_Lambda ~ 10^140
  Weinberg window:         rho_Lambda_max / rho_Lambda ~ 12-98 (~ 10^1-2)
  Anthropic contribution:  ~1-2 orders out of 140
  Residual after anthropic: ~138

STANDALONE: Compiles with Lean 4.29.0, no Mathlib required.
  Real-valued quantities encoded as scaled integers (×100).
-/

/-! ## The Full CCP Gap -/

/-- The cosmological constant problem: 140 orders of magnitude.
    Stored as ×100 for consistency with window calculations. -/
def ccp_gap_x100 : Int := 14000    -- 140.00 orders

theorem ccp_is_extreme :
    ccp_gap_x100 ≥ 14000 := by
  simp [ccp_gap_x100]

/-! ## The Weinberg Anthropic Window

Weinberg (1987): dark energy must not dominate before redshift z ~ 2-5
(structure formation epoch). The maximum allowed Lambda:

  rho_Lambda_max(z) = rho_m0 * (1+z)^3

At z=2: rho_Lambda_max = 27 * rho_m0 ~ 12 * rho_Lambda_obs
At z=5: rho_Lambda_max = 216 * rho_m0 ~ 98 * rho_Lambda_obs
-/

/-- The Weinberg window at different redshift thresholds.
    All ratios ×100 for precision. -/
structure WeinbergWindow where
  z_threshold : Nat           -- redshift threshold
  cube_factor : Nat           -- (1+z)^3
  window_ratio_x100 : Nat     -- (rho_Lambda_max / rho_Lambda_obs) × 100
  log10_window_x100 : Nat     -- log10(window_ratio) × 100

/-- Conservative window: structure formation by z=2. -/
def window_z2 : WeinbergWindow := {
  z_threshold := 2
  cube_factor := 27
  window_ratio_x100 := 1225   -- 12.25
  log10_window_x100 := 109    -- 1.09
}

/-- Aggressive window: first stars by z=5. -/
def window_z5 : WeinbergWindow := {
  z_threshold := 5
  cube_factor := 216
  window_ratio_x100 := 9800   -- 98.0
  log10_window_x100 := 199    -- 1.99
}

/-- The window is small: at most ~2 orders of magnitude. -/
theorem window_is_small_z2 :
    window_z2.log10_window_x100 < 200 := by
  simp [window_z2]

theorem window_is_small_z5 :
    window_z5.log10_window_x100 < 200 := by
  simp [window_z5]

/-- The observed Lambda sits within both windows (ratio > 100 = 1.0×). -/
theorem lambda_in_window :
    window_z2.window_ratio_x100 > 100 ∧ window_z5.window_ratio_x100 > 100 := by
  simp [window_z2, window_z5]

/-! ## Anthropic Probability: Not Extreme -/

/-- Under a uniform prior on Lambda, the probability of observing
    Lambda <= Lambda_obs is 1/window_ratio.
    Encoded as ×10000 for the z2 case (~820) and z5 case (~102). -/
def anthropic_prob_z2_x10000 : Nat := 816   -- 1/12.25 * 10000 ~ 816
def anthropic_prob_z5_x10000 : Nat := 102   -- 1/98 * 10000 ~ 102

/-- The probabilities are 1-8% — not extreme. -/
theorem anthropic_prob_not_extreme :
    anthropic_prob_z2_x10000 > 500 ∧    -- > 5%
    anthropic_prob_z5_x10000 > 50 := by  -- > 0.5%
  simp [anthropic_prob_z2_x10000, anthropic_prob_z5_x10000]

/-! ## What Anthropic Explains vs What It Doesn't -/

/-- Orders of magnitude explained by Weinberg selection (×100). -/
def anthropic_contribution_x100 : Nat := window_z5.log10_window_x100  -- 199 (~ 2 orders)

/-- Orders remaining after anthropic reasoning (×100). -/
def residual_after_anthropic_x100 : Int :=
  ccp_gap_x100 - (anthropic_contribution_x100 : Int)

/-- Anthropic explains at most 2 orders out of 140. -/
theorem anthropic_explains_little :
    anthropic_contribution_x100 < 200 := by
  simp [anthropic_contribution_x100, window_z5]

/-- The residual is still > 138 orders (13800 in ×100 units). -/
theorem residual_is_enormous :
    residual_after_anthropic_x100 > 13800 := by
  simp [residual_after_anthropic_x100, ccp_gap_x100,
        anthropic_contribution_x100, window_z5]

/-! ## Combined: SUSY + Anthropic Still Leaves 71+ Orders

From VacuumFineTuning.lean: SUSY at 1 TeV removes 66 orders (139 -> 73).
From this file: anthropic removes at most 2 orders.
Combined: 140 - 66 - 2 = 72 orders STILL unexplained.
-/

/-- The combined SUSY + anthropic removal (×100). -/
def susy_contribution_x100 : Nat := 6600     -- 66 orders
def combined_removal_x100 : Nat := susy_contribution_x100 + anthropic_contribution_x100

theorem combined_still_leaves_huge_gap :
    ccp_gap_x100 - (combined_removal_x100 : Int) > 7000 := by
  simp [ccp_gap_x100, combined_removal_x100, susy_contribution_x100,
        anthropic_contribution_x100, window_z5]

/-- The hierarchy of explanations for the CCP:
    Total gap: 140 orders
    SUSY (TeV breaking): removes 66 orders -> 74
    Anthropic (Weinberg): removes 2 orders -> 72
    Remaining: 72 orders — requires new physics or new principle -/
theorem ccp_hierarchy :
    ccp_gap_x100 > 13900 ∧
    susy_contribution_x100 > 6000 ∧
    anthropic_contribution_x100 < 200 ∧
    ccp_gap_x100 - (combined_removal_x100 : Int) > 7000 := by
  simp [ccp_gap_x100, susy_contribution_x100,
        anthropic_contribution_x100, combined_removal_x100, window_z5]
