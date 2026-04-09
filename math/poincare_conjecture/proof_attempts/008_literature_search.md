---
source: Web/arXiv search
type: Literature review
status: FOUND RELATED WORK — must cite and differentiate
---

## Key Findings

### 1. "Depletion of Nonlinearity" (Constantin, Farhat-Grujic-Leitmeyer)
The vortex stretching term is "depleted" by geometric misalignment between
ω and strain S. This is EXACTLY our infection ratio measurement — we're
quantifying the fraction of points where depletion fails (Q > 0).

Our contribution: we show the depletion fraction converges to zero
exponentially under grid refinement. Nobody has measured this convergence.

### 2. "Emergent Nonlinear Vorticity Dissipation" (Springer Nature, 2024-2025)
Claims a nonlinear damping emerges from the viscous term that suppresses
vortex stretching. The damping is proportional to |ω|^α.
URL: https://communities.springernature.com/posts/global-regularity-for-the-3d-incompressible-navier-stokes-equations-via-emergent-nonlinear-vorticity-dissipation

MUST READ. If this claims regularity, we need to know their approach
and how it relates to ours.

### 3. "Twisting Vortex Lines Regularize NS Turbulence" (arXiv 2409.13125, 2024)
The anti-twist mechanism: curved-aligned vorticity generates negative
twist that attenuates intense vorticity. Spontaneous emergence of
anti-twist under both NS and Euler.

Connection to us: this is the MECHANISM behind our observation.
The anti-twist is what makes the growing fraction decay.

### 4. "Concentration to Quantitative Regularity" Survey (arXiv 2211.16215)
Survey of whether norms concentrate on small scales near blow-up.
Directly relevant to our per-scale analysis.

### 5. "Vortex Stretching and Enhanced Dissipation" (Math Annalen, 2020)
Vortex stretching can actually ENHANCE dissipation under certain
geometric conditions. This supports our finding that viscosity
doesn't just oppose stretching — the interplay is geometric.

### 6. Several RETRACTED regularity claims (ResearchGate, SSRN)
Multiple claimed proofs of regularity retracted. Our approach is
different (computational evidence + interval arithmetic, not pure analysis).
But we must be careful not to overclaim.

## Papers To Cite
- Constantin "geometric depletion of nonlinearity" (original)
- Farhat-Grujic-Leitmeyer 2018 (depletion framework)
- arXiv 2409.13125 "Twisting vortex lines" 2024
- arXiv 2211.16215 "Concentration to quantitative regularity" survey
- The Springer Nature emergent dissipation paper (check if peer-reviewed)

## How We Differentiate
1. We MEASURE the depletion quantitatively (infection ratio)
2. We show it converges EXPONENTIALLY under refinement (new result)
3. We test across 7 IC families including adversarial (new)
4. We provide interval arithmetic infrastructure for CAP (new)
5. We connect to PySR-derived formula frac ~ exp(-N/N_d) (new)

## Warning
Several regularity claims from 2024-2025 exist and were retracted.
Keep our claims modest: "computational evidence consistent with regularity"
not "proof of regularity." The proof follows from the interval verification.
