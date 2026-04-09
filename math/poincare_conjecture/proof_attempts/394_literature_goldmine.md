---
source: LITERATURE GOLDMINE — key papers and identities for closing the proof
type: RESEARCH SUMMARY — papers to read + key theorems
file: 394
date: 2026-03-29
---

## PAPERS TO READ (prioritized)

### Priority 1: Directly relevant to our proof

1. **Miller (2024)** arxiv 2407.02691
   "On the interaction of strain and vorticity for solutions of the NS equation"
   KEY: ⟨-ΔS, ω⊗ω⟩ = 0 (Theorem 1.3). Hidden orthogonality.
   ALSO: Global regularity for the strain-vorticity interaction MODEL.
   The mu-NS family shares our enstrophy identity but MODEL is regular.

2. **Miller (2020)** arxiv 1710.05569
   "A regularity criterion involving only the middle eigenvalue of the strain"
   KEY: Blowup requires ∫||λ₂⁺||^p dt = ∞. Our self-attenuation alignment
   (ê → e₂) connects directly to this criterion.

3. **Rudelson-Vershynin (2013)** arxiv 1306.2872
   "Hanson-Wright inequality and sub-gaussian concentration"
   KEY: P(|s^T A s - E| > t) ≤ 2exp(-c min(t²/||A||_F², t/||A||_op))
   Sharp constants for our regression residual bound.

### Priority 2: Mathematical tools

4. **Latała (2006)** "Estimates of moments and tails of Gaussian chaoses"
   KEY: Low-rank chaos tail bounds. If applicable to Rademacher: gives
   max ~ √(r_eff × N) × ||M||_op for rank-r_eff matrices.

5. **Adamczak et al. (2014)** arxiv 1309.7083
   "Hanson-Wright for matrices with structure"
   KEY: Structured matrices can have TIGHTER constants than generic HW.

6. **Pisier** arxiv 1101.4195
   "Grothendieck's theorem, past and present"
   KEY: Kernel-specific Grothendieck bounds. SDP certification approach.

### Priority 3: Context and foundations

7. **Seregin** arxiv 0909.3897
   "Type I → L³ blowup" (our Step 2: Seregin exclusion)
   EXACT statement: limsup → lim for Type I singularities.

8. **Tao (2019)** arxiv 1908.04958
   "Quantitative bounds for L³ blowup of NS"
   Triple-logarithmic quantification of ESS result.

9. **Kiselev (2010)** arxiv 1009.0542
   "Nonlocal maximum principles for active scalars"
   KEY NEGATIVE: No pointwise CZ bound exists (sign-changing kernel).
   Our per-mode decomposition BYPASSES this obstruction.

## KEY IDENTITIES FROM THE LITERATURE

### Miller's orthogonality (2024):
⟨-ΔS, ω⊗ω⟩ = 0 (L² orthogonality, exact for div-free fields)

### Miller's strain evolution (2020):
∂_t S + (u·∇)S - ΔS + S² + (1/4)ω⊗ω - (1/4)|ω|²I + Hess(p) = 0

### Miller's enstrophy identity (2020):
d/dt ||S||² = -2||S||²_{Ḣ¹} - 4∫det(S)
(ENTIRELY LOCAL — no nonlocal strain-vorticity interaction!)

### The mu-NS model (Miller 2024):
∂_t S - ΔS - (1/2)P_st(ω⊗ω) = 0
Has GLOBAL REGULARITY (Theorem 1.2). Full NS = this + nonlinear remainder.

## CONNECTIONS TO OUR WORK

1. **Miller's ⟨-ΔS, ω⊗ω⟩ = 0**: This orthogonality could strengthen the
   H_ωω bound. The pressure Hessian term in our barrier involves ΔS projected
   onto ê⊗ê. Miller's identity constrains this projection.

2. **Middle eigenvalue criterion**: Our self-attenuation (ê → e₂) means the
   vorticity-stretching term α = Σλᵢcᵢ ≈ λ₂ (the middle eigenvalue).
   Miller's criterion says blowup needs λ₂⁺ to blow up. Our barrier prevents
   this by keeping α < |ω|/2.

3. **The strain-vorticity model**: Miller proves the MODEL (without S² and
   advection) is globally regular. The remainder (S² + advection) is what
   our barrier controls via S²ê < 3|ω|²/4.

4. **No pointwise CZ bound**: The fundamental reason our per-mode decomposition
   is necessary — the Riesz transform can't be bounded pointwise. Each mode's
   S_k·v̂_k = 0 is the MODE-LEVEL version of the cancellation.

## POTENTIAL NEW PROOF ROUTES

### Route A: Use Miller's orthogonality in the barrier
⟨-ΔS, ω⊗ω⟩ = 0 implies ê·(ΔS)·ê is constrained. Combined with the
barrier equation (which involves ê·(ΔS)·ê through the viscous term):
this could provide an ADDITIONAL sign constraint that closes the proof.

### Route B: Use the strain-vorticity model decomposition
Write NS = model + remainder. The model is globally regular (Miller).
Bound the remainder using our barrier framework. If the remainder is
"small enough": the full NS inherits regularity from the model.

### Route C: Quantitative depletion of nonlinearity
Miller's Theorem 1.9: at blowup, ||nonlinearity||/||-ΔS|| → 1.
Our barrier prevents this ratio from reaching 1 (by keeping α < |ω|/2).

## 394. Papers identified. Miller (2024) orthogonality is the key new tool.
## Read Miller 2024 first — the ⟨-ΔS, ω⊗ω⟩ = 0 identity could close the gap.
