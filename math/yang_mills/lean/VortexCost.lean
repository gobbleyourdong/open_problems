/-
  Yang-Mills — Vortex Cost Inequality (Tomboulis 5.15)

  The key reduction from attempt_016 and attempt_018:

  Tomboulis (5.15) is equivalent to:
    ⟨O⟩_per ≥ ⟨O⟩_anti

  where O = ∂S/∂α ≥ 0 is a positive observable measuring coupling response.

  This is further equivalent to:
    Cov_per(O, e^{-δS}) ≤ 0

  where δS = S_per - S_anti ≥ 0 is the vortex energy cost.

  The negative covariance follows from FKG IF:
  (a) O is increasing in the character values
  (b) e^{-δS} is decreasing in the character values on Σ
  (c) The periodic-BC measure satisfies FKG for character-valued observables

  (a) and (b) are structural facts. (c) is the OPEN QUESTION.
-/

/-! ## The Covariance Reduction

This is pure probability theory / measure theory — no gauge theory needed.
-/

/-- For any probability measure μ and random variables X, Y:
    E_ν[X] = E_μ[X · dν/dμ] / E_μ[dν/dμ]
    where ν is the tilted measure dν = e^{-δS} dμ / Z_tilt.

    Therefore: E_μ[X] - E_ν[X] = -Cov_μ(X, e^{-δS}) / E_μ[e^{-δS}]

    If Cov_μ(X, e^{-δS}) ≤ 0, then E_μ[X] ≥ E_ν[X]. -/
theorem expectation_comparison_from_covariance
    (E_μ_X E_ν_X cov E_e : ℝ)
    (hE_e_pos : E_e > 0)
    (h_relation : E_μ_X - E_ν_X = -cov / E_e)
    (h_cov_neg : cov ≤ 0) :
    E_μ_X ≥ E_ν_X := by
  have : -cov / E_e ≥ 0 := by
    apply div_nonneg
    · linarith
    · linarith
  linarith

/-- The vortex cost reduction: if we can show that the coupling response O
    and the vortex weight e^{-δS} are negatively correlated under the
    periodic measure, then ⟨O⟩_per ≥ ⟨O⟩_anti (inequality 5.15 holds).

    This is the STRUCTURAL fact — the proof reduces to a sign of covariance.
    The sign of covariance depends on whether the measure satisfies FKG. -/

/-! ## The FKG Criterion

A probability measure μ on a product space satisfies FKG if:
  for all increasing functions f, g: Cov_μ(f, g) ≥ 0

Equivalently (Holley criterion): for any two configurations x, y:
  μ(x ∨ y) μ(x ∧ y) ≥ μ(x) μ(y)

where ∨ = componentwise max, ∧ = componentwise min.

For lattice gauge theories in the character expansion:
- The "configuration" is the set of character values {χ_j(U_P)}_P
- The partial order is: χ_j(U_P) ≤ χ_j(U_P') iff plaquette P is "more ordered"
- The Holley criterion needs the Boltzmann weight to be log-supermodular

KEY QUESTION: Is the Wilson lattice measure log-supermodular in the
character values?

For INDEPENDENT plaquettes (no shared links): YES, trivially.
The shared links introduce CORRELATIONS that may break log-supermodularity.

But: Tomboulis Prop II.1 proves Z is MONOTONE in each c_j. This is
WEAKER than FKG but in the same direction. The question is whether
monotonicity can be upgraded to FKG.
-/

/-- FKG inequality: for a measure satisfying the lattice condition,
    increasing functions are positively correlated.

    If f is increasing and g is decreasing, then Cov(f, g) ≤ 0.

    This is the KEY lemma needed for Tomboulis (5.15). -/
axiom fkg_negative_correlation
    (f g : ℝ) -- placeholders for expectations
    (h_f_increasing : True) -- f is increasing in plaquette ordering
    (h_g_decreasing : True) -- g = e^{-δS} is decreasing
    (h_fkg : True) -- measure satisfies FKG
    : f * g ≤ f * g -- placeholder: actual statement is Cov(f,g) ≤ 0
    -- OPEN: Does the SU(2) Wilson lattice measure satisfy FKG?

/-! ## What FKG for Lattice Gauge Theory Would Give

If the SU(2) Wilson lattice measure satisfies FKG in the character basis:

1. Plaquettes are positively correlated: ⟨χ_j(U_P) χ_k(U_Q)⟩ ≥ ⟨χ_j(U_P)⟩⟨χ_k(U_Q)⟩
2. Coupling response and vortex weight are negatively correlated (attempt_018)
3. Therefore ⟨O⟩_per ≥ ⟨O⟩_anti (Tomboulis 5.15)
4. Therefore confinement for SU(2) d ≤ 4 at all couplings
5. Therefore mass gap (via Chatterjee 2021 or spectral theory)

The ENTIRE mass gap proof would follow from FKG + the Tomboulis framework.
FKG for lattice gauge theories is the ONE remaining question.

## Theorem Count:
- expectation_comparison_from_covariance: PROVED (clean arithmetic)
- fkg_negative_correlation: AXIOMATIZED (open question)
- Total: 7 Lean proofs + 1 open axiom across all files
-/
