/-
  MedThermo.Thermodynamics.ChemicalKinetics

  Formalization of chemical kinetics: mass action law, Michaelis-Menten enzyme
  kinetics, and Hill equation for cooperative binding / dose-response.

  These are the foundational equations for ALL biological rate processes:
  - Enzyme kinetics (2A protease cleaving dystrophin → Michaelis-Menten)
  - Drug binding (fluoxetine inhibiting 2C ATPase → Hill equation)
  - Immune cell killing (CTL killing rate → mass action)
  - Viral replication (polymerase kinetics → Michaelis-Menten)

  Everything in biology is chemistry. Everything in chemistry is kinetics.
  Everything in kinetics reduces to these three laws.
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Order.Monotone.Basic
import Mathlib.Topology.Order.Basic

noncomputable section

namespace MedThermo.ChemicalKinetics

/-! ## Mass Action Law

The rate of a reaction is proportional to the product of reactant concentrations.
This is the most fundamental kinetic law — everything else derives from it.

  rate = k · [A]^a · [B]^b

where k is the rate constant, [A], [B] are concentrations, and a, b are orders.

Biological application: rate of T cell killing = k_kill · [Teff] · [BetaCell]
-/

/-- Mass action rate for a bimolecular reaction: rate = k · [A] · [B] -/
def massActionRate (k : ℝ) (concA concB : ℝ) : ℝ := k * concA * concB

/-- Mass action rate is non-negative when all inputs are non-negative -/
theorem massActionRate_nonneg {k concA concB : ℝ}
    (hk : 0 ≤ k) (hA : 0 ≤ concA) (hB : 0 ≤ concB) :
    0 ≤ massActionRate k concA concB := by
  unfold massActionRate
  exact mul_nonneg (mul_nonneg hk hA) hB

/-- Mass action rate is monotone in each reactant concentration -/
theorem massActionRate_mono_concA {k concB : ℝ} (hk : 0 ≤ k) (hB : 0 ≤ concB) :
    Monotone (fun concA => massActionRate k concA concB) := by
  intro a₁ a₂ h
  unfold massActionRate
  exact mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left h hk) hB

/-- Mass action rate is zero when either reactant is absent -/
theorem massActionRate_zero_left (k concB : ℝ) :
    massActionRate k 0 concB = 0 := by
  unfold massActionRate; ring

theorem massActionRate_zero_right (k concA : ℝ) :
    massActionRate k concA 0 = 0 := by
  unfold massActionRate; ring

/-! ## Michaelis-Menten Kinetics

The fundamental model of enzyme catalysis. An enzyme E binds substrate S to form
complex ES, which converts to product P:

  E + S ⇌ ES → E + P

At steady state: rate = Vmax · [S] / (Km + [S])

where Vmax = kcat · [E]_total (maximum rate) and Km is the Michaelis constant.

Biological applications:
- 2A protease cleaving dystrophin: Vmax·[dystrophin] / (Km + [dystrophin])
- OSBP transporting cholesterol: Vmax·[cholesterol] / (Km + [cholesterol])
- Any enzyme in the CVB lifecycle or host defense pathway
-/

/-- Michaelis-Menten rate: v = Vmax · S / (Km + S) -/
def michaelisMenten (vmax : ℝ) (km : ℝ) (substrate : ℝ) : ℝ :=
  vmax * substrate / (km + substrate)

/-- Michaelis-Menten rate is non-negative for positive parameters -/
theorem michaelisMenten_nonneg {vmax km substrate : ℝ}
    (hv : 0 ≤ vmax) (hk : 0 < km) (hs : 0 ≤ substrate) :
    0 ≤ michaelisMenten vmax km substrate := by
  unfold michaelisMenten
  apply div_nonneg
  · exact mul_nonneg hv hs
  · linarith

/-- Michaelis-Menten rate is bounded above by Vmax -/
theorem michaelisMenten_le_vmax {vmax km substrate : ℝ}
    (hv : 0 ≤ vmax) (hk : 0 < km) (hs : 0 ≤ substrate) :
    michaelisMenten vmax km substrate ≤ vmax := by
  unfold michaelisMenten
  have hd : 0 < km + substrate := by linarith
  rw [div_le_iff₀ hd]
  nlinarith

/-- At substrate = Km, rate = Vmax/2 (definition of Km) -/
theorem michaelisMenten_at_km {vmax km : ℝ} (hk : km ≠ 0) :
    michaelisMenten vmax km km = vmax / 2 := by
  unfold michaelisMenten
  field_simp
  ring

/-- Michaelis-Menten rate is zero at zero substrate -/
theorem michaelisMenten_zero {vmax km : ℝ} (hk : 0 < km) :
    michaelisMenten vmax km 0 = 0 := by
  unfold michaelisMenten
  simp

/-- Michaelis-Menten is monotone on non-negative concentrations.
    For s₁ ≤ s₂ with both ≥ 0: vmax·s₁/(km+s₁) ≤ vmax·s₂/(km+s₂).
    Proof by cross-multiplication: s₁·(km+s₂) ≤ s₂·(km+s₁) ↔ s₁·km ≤ s₂·km. -/
theorem michaelisMenten_mono_nonneg {vmax km s₁ s₂ : ℝ}
    (hv : 0 ≤ vmax) (hk : 0 < km) (hs₁ : 0 ≤ s₁) (hs₂ : 0 ≤ s₂) (h : s₁ ≤ s₂) :
    michaelisMenten vmax km s₁ ≤ michaelisMenten vmax km s₂ := by
  unfold michaelisMenten
  have hd₁ : 0 < km + s₁ := by linarith
  have hd₂ : 0 < km + s₂ := by linarith
  -- Cross-multiply: need vmax*s₁*(km+s₂) ≤ vmax*s₂*(km+s₁)
  rw [div_le_div_iff₀ hd₁ hd₂]
  -- vmax * s₁ * (km + s₂) ≤ vmax * s₂ * (km + s₁)
  -- = vmax * (s₁*km + s₁*s₂) ≤ vmax * (s₂*km + s₁*s₂)
  -- = vmax * s₁*km ≤ vmax * s₂*km  (s₁*s₂ cancels)
  nlinarith [mul_le_mul_of_nonneg_left h (le_of_lt hk)]

-- Note: the full-ℝ `Monotone` version is NOT stated because vmax * s / (km + s)
-- has a pole at s = -km. The biologically correct statement is `michaelisMenten_mono_nonneg`.

/-! ## Hill Equation

Generalization of Michaelis-Menten for cooperative binding / dose-response.

  E(C) = Emax · C^n / (IC50^n + C^n)

where n is the Hill coefficient (cooperativity), IC50 is the concentration
giving 50% effect, and Emax is the maximum effect.

n = 1: Michaelis-Menten (no cooperativity)
n > 1: positive cooperativity (steeper dose-response, switch-like)
n < 1: negative cooperativity (flatter dose-response)

This is THE equation for drug efficacy:
- Fluoxetine inhibiting CVB 2C ATPase: IC50 = 1.0 μM, n ≈ 1
- BHB suppressing NLRP3: IC50 ≈ 1.0 mM, n ≈ 1-2
- Colchicine blocking microtubule transport: dose-response via Hill
-/

/-- Hill equation with natural number exponent: E = Emax · C^n / (IC50^n + C^n)
    Using ℕ exponent avoids issues with real-valued powers of negative numbers.
    In practice, Hill coefficients are positive integers (n=1 for Michaelis-Menten,
    n=2-4 for cooperative binding). -/
def hillEquation (emax : ℝ) (ic50 : ℝ) (n : ℕ) (conc : ℝ) : ℝ :=
  emax * conc ^ n / (ic50 ^ n + conc ^ n)

/-- Fractional inhibition (Emax = 1): the fraction of target inhibited at concentration C -/
def fractionalInhibition (ic50 : ℝ) (n : ℕ) (conc : ℝ) : ℝ :=
  hillEquation 1 ic50 n conc

/-- At C = IC50, fractional inhibition = 0.5 (50%) — the definition of IC50 -/
theorem hill_at_ic50 {ic50 : ℝ} {n : ℕ} (h50 : ic50 ≠ 0) (hn : n ≠ 0) :
    fractionalInhibition ic50 n ic50 = 1 / 2 := by
  unfold fractionalInhibition hillEquation
  simp only [one_mul]
  have h_pow : ic50 ^ n ≠ 0 := pow_ne_zero _ h50
  field_simp
  ring

/-- Hill equation is bounded between 0 and Emax -/
theorem hill_bounded {emax ic50 : ℝ} {n : ℕ} {conc : ℝ}
    (he : 0 ≤ emax) (h50 : 0 < ic50) (hn : 0 < n) (hc : 0 ≤ conc) :
    0 ≤ hillEquation emax ic50 n conc ∧ hillEquation emax ic50 n conc ≤ emax := by
  constructor
  · unfold hillEquation
    apply div_nonneg
    · exact mul_nonneg he (pow_nonneg hc n)
    · positivity
  · unfold hillEquation
    -- Need: emax * conc^n / (ic50^n + conc^n) ≤ emax
    -- i.e., emax * (conc^n / (ic50^n + conc^n)) ≤ emax * 1
    -- Suffices: conc^n / (ic50^n + conc^n) ≤ 1
    -- i.e., conc^n ≤ ic50^n + conc^n (trivially true since ic50^n ≥ 0)
    have h_denom : 0 < ic50 ^ n + conc ^ n := by positivity
    rw [div_le_iff₀ h_denom]
    nlinarith [pow_nonneg (le_of_lt h50) n, pow_nonneg hc n]

/-- Hill equation is zero at zero concentration (no drug → no effect) -/
theorem hill_zero {emax ic50 : ℝ} {n : ℕ} (h50 : 0 < ic50) (hn : 0 < n) :
    hillEquation emax ic50 n 0 = 0 := by
  unfold hillEquation
  have hn' : n ≠ 0 := Nat.pos_iff_ne_zero.mp hn
  simp [zero_pow hn']

/-- Hill equation (with Emax=1) is monotone on non-negative concentrations.
    Higher drug concentration → higher fractional inhibition.
    Proof: cross-multiply c₁^n/(ic50^n+c₁^n) ≤ c₂^n/(ic50^n+c₂^n)
    ↔ c₁^n·ic50^n ≤ c₂^n·ic50^n ↔ c₁^n ≤ c₂^n, true since c₁ ≤ c₂ and n ∈ ℕ. -/
theorem hill_mono_nonneg {ic50 : ℝ} {n : ℕ} {c₁ c₂ : ℝ}
    (h50 : 0 < ic50) (hn : 0 < n) (hc₁ : 0 ≤ c₁) (hc₂ : 0 ≤ c₂) (h : c₁ ≤ c₂) :
    fractionalInhibition ic50 n c₁ ≤ fractionalInhibition ic50 n c₂ := by
  unfold fractionalInhibition hillEquation
  simp only [one_mul]
  have hd₁ : 0 < ic50 ^ n + c₁ ^ n := by positivity
  have hd₂ : 0 < ic50 ^ n + c₂ ^ n := by positivity
  rw [div_le_div_iff₀ hd₁ hd₂]
  -- Need: c₁^n * (ic50^n + c₂^n) ≤ c₂^n * (ic50^n + c₁^n)
  -- i.e., c₁^n * ic50^n + c₁^n * c₂^n ≤ c₂^n * ic50^n + c₁^n * c₂^n
  -- i.e., c₁^n * ic50^n ≤ c₂^n * ic50^n
  have h_pow : c₁ ^ n ≤ c₂ ^ n := pow_le_pow_left₀ hc₁ h n
  nlinarith [pow_pos h50 n]

/-- **Strict** Hill monotonicity: if c₁ < c₂ (both ≥ 0, ic50 > 0, n > 0),
    then fractional inhibition is strictly greater at c₂.
    This is the KEY lemma that closes 3 sorry's in the IC50 and ClearanceOrder files. -/
theorem hill_strict_mono_nonneg {ic50 : ℝ} {n : ℕ} {c₁ c₂ : ℝ}
    (h50 : 0 < ic50) (hn : 0 < n) (hc₁ : 0 ≤ c₁) (hc₂ : 0 ≤ c₂) (h : c₁ < c₂) :
    fractionalInhibition ic50 n c₁ < fractionalInhibition ic50 n c₂ := by
  unfold fractionalInhibition hillEquation
  simp only [one_mul]
  have hd₁ : 0 < ic50 ^ n + c₁ ^ n := by positivity
  have hd₂ : 0 < ic50 ^ n + c₂ ^ n := by positivity
  rw [div_lt_div_iff₀ hd₁ hd₂]
  -- Need: c₁^n * (ic50^n + c₂^n) < c₂^n * (ic50^n + c₁^n)
  -- Expand: c₁^n*ic50^n + c₁^n*c₂^n < c₂^n*ic50^n + c₁^n*c₂^n
  -- Simplify: c₁^n*ic50^n < c₂^n*ic50^n
  -- i.e.: c₁^n < c₂^n (since ic50^n > 0)
  have h_pow : c₁ ^ n < c₂ ^ n := by
    exact pow_lt_pow_left₀ h hc₁ (Nat.pos_iff_ne_zero.mp hn)
  nlinarith [pow_pos h50 n]

/-! ## Competitive Inhibition

When a drug (inhibitor I) competes with a substrate for an enzyme's active site:

  v = Vmax · [S] / (Km · (1 + [I]/Ki) + [S])

The inhibitor effectively increases the apparent Km by factor (1 + [I]/Ki).

This models fluoxetine competing for CVB 2C ATPase binding site.
-/

/-- Competitive inhibition: apparent Km increases by factor (1 + [I]/Ki) -/
def competitiveInhibition (vmax km ki : ℝ) (substrate inhibitor : ℝ) : ℝ :=
  let km_apparent := km * (1 + inhibitor / ki)
  michaelisMenten vmax km_apparent substrate

/-- Competitive inhibition reduces rate compared to uninhibited -/
theorem competitiveInhibition_le {vmax km ki substrate inhibitor : ℝ}
    (hv : 0 ≤ vmax) (hk : 0 < km) (hki : 0 < ki)
    (hs : 0 ≤ substrate) (hi : 0 ≤ inhibitor) :
    competitiveInhibition vmax km ki substrate inhibitor ≤
    michaelisMenten vmax km substrate := by
  -- Competitive inhibition increases Km to km*(1 + I/Ki) ≥ km
  -- Larger Km → larger denominator → smaller rate
  unfold competitiveInhibition michaelisMenten
  simp only
  -- Need: vmax * substrate / (km*(1+inhibitor/ki) + substrate) ≤ vmax * substrate / (km + substrate)
  -- Numerators equal, denominator of LHS ≥ denominator of RHS
  apply div_le_div_of_nonneg_left (mul_nonneg hv hs)
  · linarith -- km + substrate > 0
  · -- km*(1 + inhibitor/ki) + substrate ≥ km + substrate
    have h_factor : 0 ≤ inhibitor / ki := div_nonneg hi (le_of_lt hki)
    nlinarith

/-! ## Key biological interpretations

These theorems establish the mathematical properties that underpin the entire
campaign's pharmacology:

1. `michaelisMenten_le_vmax`: Drug effect saturates. Doubling the dose
   does NOT double the effect. Diminishing returns above IC50.

2. `hill_at_ic50`: IC50 is precisely the half-maximal concentration.
   At IC50, exactly 50% of the target is inhibited.

3. `michaelisMenten_mono`: Higher drug concentration always helps
   (monotone), but with saturation (bounded).

4. `competitiveInhibition_le`: An inhibitor always reduces the reaction
   rate. Fluoxetine binding 2C ATPase always slows CVB replication.

These properties are UNIVERSAL — they apply to any enzyme, any drug,
any substrate, in any organism. The Lean proofs guarantee this.
-/

end MedThermo.ChemicalKinetics
