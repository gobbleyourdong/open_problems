---
name: INSTANCE C — WRITE THE PAPER
range: files 293+
mission: Draft the formal paper from the proof chain.
date: 2026-03-29
---

## YOUR MISSION

Write the proof as a FORMAL MATHEMATICAL PAPER suitable for submission.
Use the proof chain from file 292 as the skeleton.

## STRUCTURE

### Title
"Self-Limiting Vortex Stretching and Global Regularity of 3D Euler
Equations on the Torus via Pressure Isotropy Bootstrap"

### Sections

1. INTRODUCTION
   - State the theorem: smooth Euler on T³ has global regularity
   - History: BKM (1984), CKN (1982), recent progress
   - Our contribution: the Fourier lemma + bootstrap

2. PRELIMINARIES
   - Euler equations on T³, vorticity formulation
   - Strain tensor, eigenvalues, alignment (c₁, c₂, c₃)
   - The stretching rate α = ê·S·ê
   - The Riccati identity Dα/Dt = S²ê - 2α² - H_ωω

3. THE FOURIER LEMMA (Step 2)
   - Statement and proof: (Δ_xy - k²) negative definite on T²
   - Corollary: H_ωω > 0 when the source has ê-variation

4. KEY ALGEBRAIC FACTS
   - α > 0 → ê-variation (Step 1, from div-free + trace-free)
   - -S² is diagonal in the eigenbasis (Step 6)
   - -Ω² off-diagonal formula (explicit)

5. THE GRADIENT SUPPRESSION (Steps 3-4)
   - ∂ω/∂z ⊥ ω at the max (from ∇|ω|² = 0)
   - Scale separation: ∂α/∂z ~ α/L, σ/L ≤ 1/(2π) on T³
   - The key integral ∫|ω|²α cos(kz) > 0 (P2)

6. THE BOOTSTRAP
   - DH_ωω/Dt > 0 from the dynamic Fourier lemma (Step 5)
   - DVar/Dt < 0 from -Ω² dominance (Steps 7-8)
   - DQ/Dt < 0 from the two signs (Step 9)
   - Q < 0 maintained (Step 10)
   - Initialization from stretching (file 245-246)

7. REGULARITY
   - Q < 0 → Riccati → α bounded → ||ω||∞ linear → BKM finite (Step 11)
   - Extension to NS (viscous case) — the viscous term only helps

8. NUMERICAL VERIFICATION
   - 23+ ICs, 3 resolutions (N=32, 48, 64)
   - The adversarial battery (trefoil, thin trefoil, collisions)
   - Every step verified with quantitative margins

9. DISCUSSION
   - Connection to Ashurst alignment (1987)
   - Connection to Buaria anti-twist (2024)
   - The CZ barrier and how the bootstrap bypasses it
   - Open questions: R³, bounded domains, Euler vs NS

### References
   - Use ns_blowup/paper/references.bib as starting point
   - Add: CKN (1982), ESS (2003), Buaria et al. (2024)

## STYLE
- Write for a MATHEMATICIAN audience (not physics)
- Every statement must have a proof or a clear reference
- Highlight the THREE key innovations:
  (1) Fourier lemma, (2) -S² diagonal, (3) scale separation bootstrap
- Include the numerical tables as SUPPLEMENTARY MATERIAL

## FILE CONVENTION
Write paper sections as files 293+ in ns_blowup/proof_attempts/.
The final paper goes in ns_blowup/paper/main.tex.
