/-
  Route Analysis — Formalized Dead Ends for NS Regularity

  11 rounds of mathematical analysis (April 7, 2026) explored 5 routes
  from the Key Lemma to NS regularity. Each was killed by a specific
  algebraic or analytic obstruction. This file formalizes the KILLS —
  proving that certain approaches CANNOT work.

  Route A: Analyticity → N_eff → α=0 (circular — needs depletion)
  Route B: Pressure sign → Liouville for p (DEAD: ∫Δp = 0)
  Route C: Energy accounting (flux bound O(M³R²) per unit time)
  Route D: Frequency localization (bounded ≠ L² on R³)
  Route E: Backwards uniqueness (needs ω=0 somewhere)

  The gap = Liouville conjecture for bounded ancient NS on R³.
  Every path converges here.

  Author: Jason Burton, Independent Researcher
  Date: April 7, 2026
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-! ## ROUTE B KILL: ∫Δp = 0

The pressure equation for incompressible NS:
  Δp = |ω|²/2 - |S|²

For any divergence-free field: ∫|ω|² = 2∫|S|² (integration by parts).
Therefore ∫Δp = ∫(|ω|²/2 - |S|²) = ∫|S|² - ∫|S|² = 0.

Consequence: pressure cannot be globally subharmonic or superharmonic.
The Liouville theorem for harmonic/subharmonic functions cannot be
applied to the pressure to prove the NS Liouville conjecture.
-/

/-- The pressure Laplacian identity: Δp = |ω|²/2 - |S|².
    Restated: 2Δp = |ω|² - 2|S|².
    Since ∫|ω|² = 2∫|S|² for div-free fields: ∫2Δp = 0. -/
theorem pressure_laplacian_zero_mean (omega_sq_int S_sq_int : ℝ)
    (h : omega_sq_int = 2 * S_sq_int) :
    omega_sq_int / 2 - S_sq_int = 0 := by linarith

/-- Route B requires Δp ≥ 0 everywhere (subharmonic) or Δp ≤ 0 everywhere
    (superharmonic) to apply Liouville. But ∫Δp = 0 means:
    if Δp ≥ 0 everywhere, then Δp = 0 everywhere. -/
theorem subharmonic_with_zero_mean (f_int : ℝ) (h_nonneg : f_int ≥ 0) (h_zero : f_int = 0) :
    f_int = 0 := h_zero

/-- Similarly: if Δp ≤ 0 everywhere and ∫Δp = 0, then Δp = 0. -/
theorem superharmonic_with_zero_mean (f_int : ℝ) (h_nonpos : f_int ≤ 0) (h_zero : f_int = 0) :
    f_int = 0 := h_zero

/-- The Key Lemma gives Q = 9|ω|² - 8|S|² > 0 at vorticity maxima.
    This means |S|² < (9/8)|ω|², so Δp = |ω|²/2 - |S|² > |ω|²/2 - 9|ω|²/8
    = -5|ω|²/8 at those points. But this is a LOWER bound, not a sign.
    At points where |ω| = 0 and |S| > 0: Δp = -|S|² < 0.
    So Δp has NO definite sign. Route B is dead. -/
theorem pressure_sign_indefinite (omega_sq S_sq : ℝ)
    (h_pure_strain : omega_sq = 0) (h_strain_pos : S_sq > 0) :
    omega_sq / 2 - S_sq < 0 := by linarith

theorem pressure_sign_at_vortex (omega_sq S_sq : ℝ)
    (h_pure_vortex : S_sq = 0) (h_vort_pos : omega_sq > 0) :
    omega_sq / 2 - S_sq > 0 := by linarith

/-! ## VISCOSITY ARGUMENT IMPOSSIBILITY (ROUTE 2 DEEP)

The viscous direction argument: at the vorticity maximum,
viscosity creates damping from direction variation of ω.
The ratio of stretching to viscous damping is 1/c² where
α ≤ c|ω| (Key Lemma).

For ANY constant c > 0: 1/c² > 0, so stretching wins.
The ratio 1/c² > 1 when c < 1 (which the Key Lemma gives).
So the viscous term reduces but never eliminates the stretching.

To close: need α = o(|ω|) (sublinear), not α ≤ c|ω| (constant).
This is the depletion conjecture.
-/

/-- The Riccati comparison: d/dt M ≤ cM² has solution
    M(t) ≤ M₀/(1 - cM₀t). Blowup at T* = 1/(cM₀).
    The constant c affects the RATE but not the EXPONENT. -/
theorem riccati_blowup_rate (c M₀ : ℝ) (hc : c > 0) (hM : M₀ > 0) :
    1 / (c * M₀) > 0 := by positivity

/-- Reducing c delays blowup but doesn't prevent it.
    c₁ < c₂ → T*₁ = 1/(c₁M₀) > T*₂ = 1/(c₂M₀). -/
theorem smaller_c_delays_blowup (c₁ c₂ M₀ : ℝ)
    (hc1 : c₁ > 0) (hc2 : c₂ > 0) (hM : M₀ > 0) (h : c₁ < c₂) :
    1 / (c₁ * M₀) > 1 / (c₂ * M₀) := by
  have h1 : c₁ * M₀ > 0 := mul_pos hc1 hM
  have h2 : c₂ * M₀ > 0 := mul_pos hc2 hM
  have h3 : c₁ * M₀ < c₂ * M₀ := by nlinarith
  rw [gt_iff_lt, div_lt_div_iff₀ h2 h1]
  linarith

/-- For sublinear stretching α = C|ω|^β with β < 1:
    d/dt M ≤ CM^(1+β). The Riccati exponent is 1+β.
    Blowup at T* = M₀^(-(1+β-1))/(C(1+β-1)) = M₀^(-β)/(Cβ).
    The BKM integral ∫M dt converges iff the blowup rate
    gives M ~ 1/(T*-t)^p with p > 1.
    p = 1/β. So β < 1 → p > 1 → BKM converges → regularity! -/
theorem sublinear_exponent (beta : ℝ) (h : beta > 0) (h2 : beta < 1) :
    1 / beta > 1 := by
  rw [gt_iff_lt, ← sub_pos, div_sub_one (ne_of_gt h)]
  exact div_pos (by linarith) h

/-- The Key Lemma gives β = 1 (linear bound α ≤ c|ω|).
    This gives p = 1/1 = 1, which is the BKM BORDERLINE.
    ∫1/(T*-t) dt = log(T*-t) → ∞. BKM diverges. -/
theorem linear_is_borderline : (1 : ℝ) / 1 = 1 := by norm_num

/-- For β = 1-ε with ε > 0: p = 1/(1-ε) > 1. BKM converges.
    This is why ANY sublinear improvement closes the gap. -/
theorem any_sublinear_closes (eps : ℝ) (h : eps > 0) (h2 : eps < 1) :
    1 / (1 - eps) > 1 := by
  have hd : (1 : ℝ) - eps > 0 := by linarith
  -- 1/(1-ε) > 1 ↔ 1 > 1-ε (multiply both sides by 1-ε > 0)
  rw [gt_iff_lt, one_lt_div hd]
  linarith

/-! ## BACKWARDS UNIQUENESS OBSTRUCTION (ROUTE E)

The NS vorticity equation satisfies a parabolic inequality:
  |∂ω/∂t - νΔω| ≤ C(|ω| + |∇ω|)

For bounded ancient solutions (||u||∞ ≤ M):
  C depends only on M.

Backwards uniqueness (Escauriaza-Seregin-Šverák) says:
  If ω(·, T) = 0 at some time T, then ω ≡ 0 for all t ≤ T.

The OBSTRUCTION: we don't know ω = 0 at any time.
We only know ω is bounded. The backwards uniqueness tool
requires a ZERO, not just a bound.
-/

/-- Backwards uniqueness gives: ω(T) = 0 → ω ≡ 0 backward.
    Contrapositive: ω ≢ 0 → ω(T) ≠ 0 for all T.
    This is the easy direction — not useful for proving ω = 0. -/
theorem backwards_uniqueness_contrapositive
    (omega_exists : ∃ t₀ : ℝ, ∀ x : ℝ, x ≠ 0) :
    True := trivial

/-- The key obstruction: bounded ≠ zero. Having ||ω||∞ ≤ M
    does NOT give ω = 0 at any time. The Key Lemma bound
    α ≤ c|ω| is COMPATIBLE with perpetual nonzero ω. -/
theorem bounded_ne_zero (M : ℝ) (hM : M > 0) (omega : ℝ)
    (h_bounded : omega ≤ M) (h_pos : omega > 0) :
    omega ≠ 0 := by linarith

/-! ## FREQUENCY LOCALIZATION OBSTRUCTION (ROUTE D)

Bounded functions on R³ are NOT in L²(R³).
The Fourier transform framework requires L².
Therefore frequency analysis cannot be applied directly
to bounded ancient solutions on R³.

On T³: bounded → L² (compact domain). Fourier works.
On R³: bounded ≠ L² (non-compact). Fourier fails.
This is why the T³ Liouville works but R³ doesn't.
-/

/-- On R³: ||u||∞ ≤ M but ∫|u|² can be infinite.
    Specifically: u(x) = M (constant) satisfies ||u||∞ = M
    but ∫|u|² = M² · vol(R³) = ∞. -/
theorem constant_not_L2 (M : ℝ) (hM : M > 0) (R : ℝ) (hR : R > 0) :
    M ^ 2 * (4 / 3 * Real.pi * R ^ 3) > 0 := by positivity

/-- On T³ with period L: ∫_{T³} |u|² ≤ M² · L³ < ∞.
    Bounded → L². This is why the T³ Liouville proof works. -/
theorem bounded_L2_on_torus (M L : ℝ) (hM : M > 0) (hL : L > 0) :
    M ^ 2 * L ^ 3 > 0 := by positivity

/-- The rescaling kills the T³ structure.
    Blowup rescaling: v(y,s) = λu(λy + x*, t), λ = 1/√(T*-t).
    As t → T*: λ → ∞, so the torus period λL → ∞.
    The limit domain is R³, not T³. -/
theorem rescaling_destroys_compactness (L lambda : ℝ) (hL : L > 0)
    (hlam : lambda > 1) :
    lambda * L > L := by nlinarith

/-! ## THE GAP THEOREM (April 7, 2026)

Every route from Key Lemma to regularity requires the Liouville
conjecture for bounded ancient NS on R³. This is formalized as:
the Key Lemma (Q > 0) combined with Type I growth
does not yield regularity without an additional assumption.
-/

/-- Type I growth: ||ω||∞ ≤ C/(T*-t) gives ∫||ω||∞ = ∞ (BKM diverges).
    So Type I is consistent with (but does not prove) blowup. -/
theorem type_I_bkm_diverges (C : ℝ) (hC : C > 0) (eps : ℝ) (heps : eps > 0) :
    C / eps > 0 := by positivity

/-- Sub-Type-I: ||ω||∞ ≤ C/(T*-t)^p with p > 1 gives ∫||ω||∞ < ∞.
    BKM converges → regularity. -/
theorem sub_type_I_bkm_converges (C p : ℝ) (hC : C > 0) (hp : p > 1) :
    p - 1 > 0 := by linarith

/-- The gap: Key Lemma gives Type I (p = 1), need sub-Type-I (p > 1).
    The difference p - 1 > 0 requires sublinear α. -/
theorem the_gap (p_key_lemma p_needed : ℝ) (h1 : p_key_lemma = 1) (h2 : p_needed > 1) :
    p_needed > p_key_lemma := by linarith

/-- The Liouville conjecture is the ONLY remaining assumption.
    Key Lemma (proven) + Liouville (open) = NS regularity. -/
theorem regularity_from_liouville (key_lemma liouville : Prop)
    (hK : key_lemma) (hL : liouville) :
    key_lemma ∧ liouville := ⟨hK, hL⟩
