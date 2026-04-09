# Mechanism Sweep — Cosmological Constant Problem

*Numerical track, what_is_nothing — 2026-04-09*

---

## Preamble: Context from Prior Results

Before evaluating candidate mechanisms, four numbers from preceding analyses constrain any proposed solution:

| Quantity | Value | Source |
|---|---|---|
| ρ_Λ observed | 5.924×10⁻²⁷ J/m³ | Planck 2023 |
| ρ_QFT (Planck cutoff, full SM) | 9.1×10¹¹² J/m³ | sm_vacuum_energy.py |
| Gap (ρ_QFT / ρ_Λ) | 10^139.2 | sm_vacuum_energy.py |
| Gap in dim-reg (EW scale) | 10^70 | renormalization_findings.md |
| Weinberg anthropic window | ρ_Λ ≤ 30 × ρ_Λ_obs | anthropic_findings.md |
| L* (vacuum cutoff scale) | 0.91 m (tautological from ρ_Λ) | lambda_scale_findings.md |
| Spearman ρ (linear vs log-uniform rankings) | −0.20 (priors scramble ordering) | lambda_scale_findings.md |
| FTE(Λ, log-uniform) | 1.63 | cc_prior_findings.md |
| FTE(α, log-uniform) | 1.18 | lambda_scale_findings.md |

The L* ≈ 0.91 m observation is a tautology: L* is constructed from ρ_Λ itself via
`L* = (g_SM ħc / 32π² ρ_Λ)^(1/4)`, so L*/L_Λ = (32π²/g_SM)^(1/4) ≈ 1.67 exactly —
a pure numerical ratio with no independent physical content. The FTE similarity between
Λ and α under log-uniform prior means that, on that prior, the CC is no more surprising
than the fine structure constant. The Spearman rank correlation −0.20 means that prior
choice nearly reverses which constants look most fine-tuned — the ranking is prior-dominated,
not physics-dominated.

---

## Part 1 — Electroweak Symmetry Breaking and the Higgs Contribution

### Higgs potential parameters

Below T_EW ≈ 160 GeV the Higgs field acquires a vacuum expectation value v = 246 GeV.
The tree-level potential is:

    V(φ) = −μ²|φ|² + λ|φ|⁴

At the minimum φ_min = v/√2:

    V(φ_min) = −μ⁴ / (4λ)

The Higgs boson mass m_H = 125 GeV and vev v = 246 GeV fix the parameters:

    λ = m_H² / (2v²) = (125)² / (2 × 246²) ≈ 0.129
    μ² = λ v² = 0.129 × (246)² ≈ 7813 GeV²  →  μ ≈ 88 GeV

Substituting:

    V(φ_min) = −μ⁴ / (4λ) ≈ −(88 GeV)⁴ / (4 × 0.13) ≈ −1.15 × 10⁸ GeV⁴

### Conversion to SI

Using GeV_J = 1.602×10⁻¹⁰ J/GeV and ħc = 0.197327×10⁻¹⁵ GeV·m:

    1 GeV⁴ = (GeV_J)⁴ / (ħc)³ = 8.576 × 10⁷ J/m³

Therefore:

    |V(φ_min)| ≈ 1.15 × 10⁸ GeV⁴ × 8.576 × 10⁷ J/m³/GeV⁴
               ≈ 9.9 × 10¹⁵ J/m³

### Ratio to observed ρ_Λ

    |V(φ_min)| / ρ_Λ_obs = 9.9 × 10¹⁵ / 5.924 × 10⁻²⁷ ≈ 1.67 × 10⁴²

    log₁₀(|V(φ_min)| / ρ_Λ_obs) ≈ 42.2

The Higgs VEV contributes a negative vacuum energy of magnitude ~10^42 times the
observed dark energy density. This is a separate EW-scale contribution to the CC problem,
independent of the UV divergence discussed in renormalization_findings.md.

### Relation to dim-reg gap

The dim-reg result (renormalization_findings.md) gives a gap of 10^70 at μ = M_Z = 91 GeV.
The Higgs VEV contribution at ~(88 GeV)⁴ gives a gap of 10^42. These are different objects:

- **Dim-reg gap (10^70)**: the quantum loop correction to the vacuum energy, coming from
  integrating out virtual massive particles (top, W, Z, Higgs) up to scale μ.
- **Higgs VEV gap (10^42)**: the classical tree-level contribution from the Higgs condensate
  sitting at the bottom of its Mexican-hat potential.

Both must be cancelled to obtain the observed ρ_Λ. The tree-level Higgs contribution
of 10^42 × ρ_Λ is actually *smaller* than the loop correction (10^70 × ρ_Λ) — but it
is a qualitatively distinct source term that any complete mechanism must also address.

The full EW-scale cancellation requirement:

    |Λ_bare + V_Higgs(φ_min) + ρ_loop| ≤ ρ_Λ_obs

where each of the three terms on the left is many orders of magnitude larger than
the right-hand side. The Higgs VEV is the intermediate term: larger than ρ_Λ by 10^42,
but smaller than the loop correction by 10^28.

---

## Part 2 — The Six Candidate Mechanisms

For each mechanism we state: what it predicts, what it requires, the residual gap after
applying it, and a verdict.

---

### Mechanism A: SUSY Breaking at the TeV Scale

**Prediction:** If supersymmetry is exact, every SM boson is paired with a fermionic
superpartner of equal mass. Bose and Fermi zero-point energies cancel exactly:

    ρ_SUSY_exact = 0

When SUSY is broken at scale m̃, the residual is:

    ρ_residual ≈ N_eff × m̃⁴ / (16π²)

For the MSSM with N_eff = 118 and m̃ = 1 TeV (the LHC naturalness target):

    ρ_residual ≈ 1.32 × 10⁴⁷ J/m³    (from susy_findings.md)
    Gap vs ρ_Λ: 10^73.4

**What it requires for an exact match:** m̃ ≈ 0.5 meV — 18 orders of magnitude below
the LHC exclusion limit of ~1 TeV. The LHC has directly excluded superpartners below
~1 TeV, so the required SUSY-breaking scale is excluded by 73 orders of magnitude in
energy density.

**The residual gap:** 10^60 × ρ_Λ even for the most optimistic pre-LHC expectation
of m̃ ~ EW scale; 10^73 at the actual LHC bound.

**Verdict: FAILS.** SUSY provides the correct *mechanism* (exact cancellation) but
requires an unmotivated SUSY-breaking scale 18 orders of magnitude below electroweak.
The mechanism is real but the required parameter is excluded. SUSY shifts the CC
problem from "why is Λ_bare small?" to "why is m̃ at the meV scale?" — no improvement
in K-content.

---

### Mechanism B: Dimensional Regularization (UV Divergence Removed)

**Prediction:** In dimensional regularization (MS-bar), the vacuum energy integral is
UV-finite. Massless particles contribute exactly zero (no mass scale available). Only
massive particles contribute:

    ρ_dimreg(μ) = Σ_i sign_i × n_i × m_i⁴ / (64π²) × [ln(μ²/m_i²) + 3/2]

At μ = M_Z = 91.2 GeV:

    ρ_dimreg ≈ −4.6 × 10⁴³ J/m³    gap = 10^70

**What it requires for an exact match:** tune the renormalization scale μ to
μ ≈ Λ_obs^(1/4) ≈ 2.3 meV, so that the log term ln(μ²/m_i²) produces a near-exact
cancellation with the Λ_bare counterterm. This is manifestly a fine-tuning: adjusting
μ is adjusting the answer by hand.

**The tuning problem:** the problem is relocated, not solved. Instead of fine-tuning
Λ_bare against ρ_QFT at Planck scale (1 part in 10^140), one fine-tunes the MS-bar
counterterm against the EW-scale loop contributions (1 part in 10^70). Dim-reg halves
the exponent of the problem; it does not close it.

**Verdict: FAILS.** Dim-reg is a regularization choice, not a physical mechanism.
The EW-scale gap of 10^70 is the correct statement of the CC problem in UV-finite
field theory, but the gap itself is unresolved. Any physical prediction requires
fixing μ — and fixing μ to match ρ_Λ is circular (it would require knowing ρ_Λ
in advance). The 10^70 gap at EW scale is the hard-core technical problem.

---

### Mechanism C: Anthropic Selection (Weinberg 1987) + String Landscape

**Prediction:** In a landscape of ~10^500 vacua (Bousso-Polchinski flux construction),
the distribution of Λ values is dense enough that:

- Under a uniform prior: ~10^361 vacua satisfy ρ_Λ ≤ 30 × ρ_Λ_obs (the Weinberg window)
- Under a log-uniform prior: ~56% of all vacua already sit in the window

An observer selection effect (Weinberg 1987) explains why we find ourselves in a
galaxy-forming vacuum: structure formation requires Λ ≤ 30 × ρ_Λ_obs approximately.

**What it explains:**
- Why, *given that Λ is small*, we observe a value near but below the galaxy-formation
  threshold — this is explained (it is an anthropic selection effect)
- Why the landscape has enough vacua to populate the window — this is explained
  (10^361 vacua in window is vastly more than needed)

**What it does not explain:**
- *Why* the QFT vacuum energy is cancelled at all: the mechanism producing the
  140-decade gap between ρ_Planck and ρ_Λ_obs is not identified
- The measure problem: which of the 10^361 window vacua do we inhabit, and with
  what probability? (The landscape measure problem remains unsolved)
- Why the prior is log-uniform rather than linear: this 1.58-bit choice determines
  whether the CC appears fine-tuned at all (cc_prior_findings.md)

**Residual gap:** anthropic selection accounts for ~1 decade of the 140-decade gap
(the Weinberg factor of ~30). The remaining 139 decades require a cancellation
mechanism or a non-linear prior.

**Verdict: INCOMPLETE.** The landscape + anthropic argument is numerically viable and
internally consistent. It explains observer selection, not cancellation. It is not a
mechanism in the sense of "a dynamical process that drives Λ to its observed value."
It is a statistical framework that shifts the question from "why is Λ small?" to "why
do we find ourselves in one of the window vacua?" — a legitimate reframing, but not
a physical explanation of the cancellation.

---

### Mechanism D: Dynamical Dark Energy (Quintessence)

**Prediction:** The cosmological "constant" is not constant — it is a slowly rolling
scalar field φ with potential V(φ). The effective dark energy density evolves:

    ρ_DE(t) = ½ φ̇² + V(φ)

If V(φ) is chosen so that ρ_DE ≈ ρ_matter at the present epoch, the coincidence
problem (why ρ_Λ ≈ ρ_matter today?) is addressed by tracker solutions that attract
the field toward ρ_DE ~ ρ_matter regardless of initial conditions.

**Observational signature:** quintessence predicts an equation of state w = p/ρ ≠ −1.
Current constraint (Planck 2023 + BAO):

    w_0 = −1.03 ± 0.03

Quintessence is compatible with current data at ~1σ. The simplest models predict
small but nonzero |w + 1|, testable with future surveys (DESI, Euclid, Roman).

**What it requires:** a scalar field with mass m_φ ≈ H_0 ≈ 10⁻³³ eV — an extraordinarily
light field, lighter than any known fundamental scalar by 33 orders of magnitude relative
to the electron mass. The potential must be finely tuned to be flat enough that φ rolls
slowly over a Hubble time. This re-introduces a hierarchy problem for the scalar potential.

**What it does not explain:** quintessence does not explain why the large QFT vacuum
energy (~ρ_Planck) is absent. It requires ρ_QFT to be separately cancelled (by some
unknown mechanism) and then adds a slowly-evolving remnant. The CC problem is still
present; quintessence adds an additional dynamical component on top.

**Verdict: SPECULATIVE, NOT RULED OUT.** Quintessence is a consistent phenomenological
framework. It is not a mechanism for the 10^140-gap cancellation, but it provides an
alternative interpretation of the residual small dark energy as a dynamical field rather
than a true constant. Observationally viable at current precision; testable with w
measurement to ~1% level. A detection of w ≠ −1 at >3σ would rule out a true Λ
and would require a field description — but would not solve the CC problem.

---

### Mechanism E: Unimodular Gravity

**Prediction:** In unimodular gravity, the determinant of the metric is fixed
(√(−g) = 1 or a fixed density). The consequence is that the cosmological constant
enters as an integration constant of the equations of motion, not as a coupling to
the vacuum energy:

    G_μν = 8πG T_μν^(traceless) + Λ g_μν

where Λ is a free integration constant, not determined by ρ_vac. In unimodular gravity,
vacuum energy does not gravitate — the trace of T_μν decouples from the metric. This
would dissolve the CC problem: ρ_QFT can be arbitrarily large without affecting
spacetime curvature.

**What it requires:** modify GR by fixing the volume form. This is a gauge choice in
classical GR (diffeomorphism invariance is reduced to special diffeomorphisms with unit
Jacobian). At the classical level, unimodular gravity is equivalent to GR up to the
treatment of Λ. At the quantum level, the equivalence may break down — loop corrections
in unimodular quantum gravity are not fully established.

**The remaining problem:** unimodular gravity does not predict Λ — it merely demotes it
from a vacuum energy to an integration constant. The question "why is Λ small?" becomes
"why did the universe start with a small integration constant?" — which requires a
separate boundary condition or initial-condition explanation. The problem is reframed,
not resolved.

**Observational status:** unimodular gravity makes identical predictions to GR at the
classical level. No test has discriminated between the two below the ~1% level of
cosmological dynamics. Quantum corrections and GW observations could in principle
distinguish them, but no current data does so.

**Verdict: UNTESTED.** Unimodular gravity offers a genuine conceptual dissolution of the
CC problem (vacuum energy does not gravitate) at the cost of accepting Λ as an
unexplained integration constant. It is mathematically consistent, observationally
indistinguishable from GR at current precision, and quantum-mechanically not fully
established. The most K-efficient of the candidate mechanisms — it requires no new
fields, no new parameters, and potentially no new K-content beyond a reinterpretation
of the GR gauge group.

---

### Mechanism F: Running Vacuum Model

**Prediction:** The cosmological "constant" runs with the Hubble rate H(t):

    Λ(t) = Λ_0 + 3ν (H²(t) − H₀²)

where ν is a dimensionless parameter typically of order 10⁻³ to 10⁻². The H² dependence
is motivated by renormalization group (RG) running of the vacuum energy in quantum field
theory in curved spacetime, analogous to how coupling constants run with energy scale.

**What it fits:** the model introduces two free parameters (Λ_0 and ν). For ν ~ 10⁻³
it can fit current BAO and Planck data comparably to ΛCDM. It predicts a slightly
evolving effective equation of state, consistent with w_0 ≈ −1.

**What it does not explain:** the running vacuum model is a phenomenological
parametrization, not a dynamical mechanism. It does not:
- Explain why the QFT zero-point energy is absent from Λ
- Predict the value of ν from first principles
- Reduce to a known UV-complete theory in the appropriate limit

The ν parameter absorbs the mismatch between the QFT prediction and observation but
does not explain it. The model's success at fitting data is evidence of flexibility,
not mechanism.

**Relation to dim-reg:** the RG interpretation of running Λ is structurally similar to
the μ-dependence found in dim-reg (renormalization_findings.md). Just as tuning μ in
dim-reg can move the gap around without closing it, tuning ν in the running vacuum model
can shift the effective Λ without explaining its magnitude.

**Verdict: PHENOMENOLOGICAL.** The running vacuum model is a useful parametrization for
fitting cosmological data and may provide phenomenological evidence for vacuum evolution.
It is not a mechanism for the CC problem and introduces free parameters without
theoretical foundation. It may be the low-energy effective description of a deeper
mechanism, but the mechanism itself is unidentified.

---

## Part 3 — Comparative Summary Table

| Mechanism | Residual Gap vs ρ_Λ | Key Requirement | Status |
|---|---|---|---|
| SUSY at TeV | 10^73 × ρ_Λ | m̃ ≈ 0.5 meV (excluded by LHC by 10^18 in mass) | FAILS |
| Dim-reg (EW scale) | 10^70 × ρ_Λ | μ tuned to meV (fine-tuning relocated, not removed) | FAILS |
| Anthropic + landscape | 10^139 × ρ_Λ (uncancelled) | Log-uniform prior + measure solution | INCOMPLETE |
| Quintessence | uncancelled + w ≠ −1 | m_φ ~ H_0 ~ 10^{-33} eV (ultra-light scalar) | SPECULATIVE, NOT RULED OUT |
| Unimodular gravity | Λ = integration constant | Λ unexplained but does not gravitate | UNTESTED |
| Running vacuum | tunable | ν free parameter, no first-principles derivation | PHENOMENOLOGICAL |

No mechanism currently explains the 10^70–10^140 gap from first principles without
introducing a fine-tuning of comparable magnitude elsewhere.

---

## Part 4 — K-Content of Each Mechanism

### The K-efficiency criterion

A mechanism M solves the CC problem if it:

1. Explains why ρ_vac^QFT ≈ 10^113 J/m³ cancels to leave ρ_Λ = 5.924×10⁻²⁷ J/m³
2. Does so without fine-tuning — no adjustment of O(1) in 10^70 decimal places (EW scale)
   or O(1) in 10^140 decimal places (Planck scale)

Define K(M) as the bits needed to specify mechanism M beyond what Standard Model + GR
already require. The ideal mechanism has K(M) ≈ 0 and correct prediction.

### K-content table

| Mechanism | K(M) extra bits | Prediction quality | K-verdict |
|---|---|---|---|
| SUSY (exact, m̃ = 0) | 0 extra bits (already in MSSM if correct) | ρ_Λ = 0 exactly (wrong sign) | Wrong prediction |
| SUSY (broken, m̃ at meV) | ~60 bits (specifying m̃/M_Planck ratio) | ρ_Λ = ρ_Λ_obs (tautological — m̃ set by ρ_Λ) | Fine-tuned |
| Anthropic + landscape | 1661 bits (flux address, landscape_findings.md) + 1.58 bits (prior choice) | Viable selection, not cancellation | K-expensive, incomplete |
| Unimodular gravity | 0 extra bits (reinterpretation of GR gauge group) | Λ = integration constant | K-free, untested |
| Quintessence | ~100 bits (potential V(φ), initial conditions) | w ≠ −1, ρ_DE(t) | K-moderate, untested as mechanism |
| Running vacuum | ~30 bits (ν value) | Λ(H) fit, no first-principles ν | K-cheap, phenomenological |

### The K-efficiency landscape

**Most K-efficient viable mechanism:** Unimodular gravity. K(M) = 0 extra bits beyond a
reinterpretation of the GR gauge structure. It requires no new fields, no new particles,
no new energy scales. The cost is accepting Λ as a boundary condition rather than a
dynamical output — which may or may not be philosophically satisfying.

**Most K-expensive mechanism:** Anthropic + landscape. K(M) = 1661 bits (the flux
configuration) plus 1.58 bits (prior choice) plus the unsolved landscape measure problem.
The landscape is K-expensive precisely because it must be large enough to cover the CC
fine-tuning — it requires 10^500 vacua, specified by 500 flux integers.

**The K-minimal ideal:** A mechanism with K(M) ≈ 0 that correctly predicts ρ_Λ from
SM + GR inputs alone. This would require discovering a symmetry or dynamical attractor
in SM + GR that drives Λ to its observed value. No such mechanism currently exists.

### K-residue of the CC problem

Applying the framework from cc_prior_findings.md (three components of the CC problem):

| Component | Status | K-residue |
|---|---|---|
| (b) Fine-tuning problem | Prior artifact — dissolves under log-uniform | ~1.58 bits (prior choice) |
| (c) Why-this-Λ | Resolved by landscape + anthropic (numerically) | ~460 bits (window address) |
| (a) Technical gap: cancellation mechanism | **Unresolved** | Unknown |

The hard residue is component (a): no mechanism explains why ρ_QFT cancels to leave
ρ_Λ_obs without requiring a comparable fine-tuning elsewhere. The K-content of the
solution to (a) is currently unknown — it could be 0 bits (if unimodular or an
undiscovered symmetry) or ~1000 bits (if a landscape mechanism) or intermediate.

---

## Part 5 — What is Missing

The mechanism sweep reveals a consistent pattern across all candidates:

**Every mechanism that achieves the right magnitude introduces a new tuned quantity
of comparable K-content to the original problem.**

| Mechanism | Problem before | Problem after |
|---|---|---|
| SUSY | fine-tune Λ_bare to 1 in 10^140 | fine-tune m̃ to 1 in 10^73 |
| Dim-reg | fine-tune Λ_bare at Planck scale | fine-tune counterterm at EW scale |
| Anthropic | fine-tune Λ among 10^140 choices | unsolved measure problem + prior choice |
| Quintessence | unexplained Λ | ultra-light scalar with m_φ ~ H_0 |
| Unimodular | vacuum energy gravitates | Λ is an initial condition |
| Running vacuum | unexplained Λ | unexplained ν |

This pattern suggests that no solution exists within the current framework of
quantum field theory + general relativity. A satisfactory mechanism would likely require:

1. **A new symmetry** that forces ρ_vac = 0 (or ρ_vac = ρ_Λ_obs) dynamically, without
   fine-tuning. No known symmetry accomplishes this: Lorentz invariance allows but does
   not require zero vacuum energy; SUSY gives zero only in the unbroken limit; conformal
   symmetry is explicitly broken by massive particles.

2. **A non-QFT description of the vacuum** in which the question "what is the vacuum
   energy?" does not arise in the same form. This might emerge from quantum gravity
   (e.g. in loop quantum gravity or causal dynamical triangulations, where the vacuum
   is discrete and the continuum limit suppresses UV divergences differently), but
   no concrete prediction of ρ_Λ from these frameworks currently exists.

3. **A dynamical attractor** that drives Λ → ρ_Λ_obs as the universe evolves, without
   requiring a finely-tuned initial condition. Quintessence is the closest attempt, but
   it does not address the 10^70-gap problem at the EW scale — it merely parametrizes
   the residual.

---

## Relation to gap.md

gap.md R1: *"The cosmological constant problem — vacuum energy off by ~120 orders of
magnitude. Real physics, not metaphysics; belongs to a follow-up attempt if the track extends."*

This mechanism sweep is the numerical realization of R1. Its main findings for gap.md:

1. **The gap is 10^70 (EW scale) to 10^140 (Planck scale)** depending on regularization.
   The EW number is the robust one: a dim-reg computation gives 10^70, insensitive to
   unknown Planck-scale physics.

2. **Six candidate mechanisms fail or are incomplete.** None provides a K-efficient,
   testable, untested-but-consistent mechanism for the cancellation.

3. **The cleanest reformulation:** what symmetry or geometric constraint of SM + GR
   forces ρ_vac = ρ_Λ_obs without fine-tuning? Unimodular gravity offers one reframing
   (Λ is a constant of integration, not a vacuum energy) but does not provide a
   prediction. The K(M) = 0 solution, if it exists, is structurally of this type.

4. **The fine-tuning severity is prior-dependent** (Spearman ρ = −0.20 between linear
   and log-uniform rankings). The Higgs VEV contributes a tree-level gap of 10^42 —
   smaller than the loop correction (10^70) but not addressable by any of the six
   mechanisms reviewed here either.

---

*Data dependencies:*
- `results/susy_data.json` (susy_cancellation.py)
- `results/renormalization_data.json` (renormalization_comparison.py)
- `results/anthropic_data.json` (anthropic_window.py)
- `results/landscape_data.json` (string_landscape.py)
- `results/cc_prior_data.json` (cc_prior_analysis.py)
- `results/lambda_scale_data.json` (lambda_scale.py)

*References:*
Weinberg (1987) PRL 59, 2607 — anthropic window |
Bousso & Polchinski (2000) JHEP 0006:006 — landscape of flux vacua |
Henneaux & Teitelboim (1989) Phys.Lett. B222 — unimodular gravity |
Sola (2013) J.Phys. A46 — running vacuum model |
Ratra & Peebles (1988) PRD 37, 3406 — quintessence |
Martin (2012) CRASPh 13, 566 — review of CC problem |
Planck 2023 (Aghanim et al.) A&A 641, A6 — w_0 constraint |
