# Chen-Hou 2025 Part I: Analysis — Key Findings

Source: arXiv:2210.07191 (Chen-Hou, "Stable nearly self-similar blowup...Part I")
Extracted by: Gemini, cross-verified against NS_FRAMEWORK.md

## 1. Self-Similar Coordinate Transformation

Physical (x,y,t) → self-similar (ρ,η,τ):

- Rescaled time: τ = ∫₀ᵗ 1/C_ω(s) ds
- Rescaled space: ρ = x/C_l(τ), η = y/C_l(τ)
- Vorticity: ω(x,y,t) = C_ω(τ)·ω̃(ρ,η,τ)
- Temperature: θ(x,y,t) = C_l(τ)·C_ω²(τ)·θ̃(ρ,η,τ)

Scaling factors governed by:
- c_l = -(1/C_l)·dC_l/dτ
- c_ω = (1/C_ω)·dC_ω/dτ

## 2. Normalization Constants (VERIFIED ✓)

- c_l = 3.00649898  ← matches NS_FRAMEWORK.md ✓
- c_ω = -1.02942516 ← matches NS_FRAMEWORK.md ✓
- c_l/(-c_ω) = 2.9206 ← matches NS_FRAMEWORK.md value 2.9205600 ✓

Physical meaning:
- Spatial collapse: (T-t)^{c_l/(-c_ω)} ≈ (T-t)³
- Vorticity blowup: (T-t)⁻¹ (γ=1)

## 3. Stability: NOT a Spectral Gap

Linearized operator decomposed: L = L₀ + K

- L₀ (local part): advection + transport, COERCIVE (strong damper)
- K (non-local part): Biot-Savart interactions, FINITE-RANK near origin + small residual

Stability criterion: coercive damping from L₀ strictly dominates
finite-rank perturbations from K. Proven via weighted norms.

NOT spectral gap. NOT eigenvalue problem. It's an INEQUALITY.
→ This maps directly to Lean: prove the inequality, done.

## 4. Function Spaces

NOT standard Sobolev (H^k) or L². These fail due to boundary advection.

Instead: weighted L∞ ∩ C^{1/2} (Hölder)
- Weighted L∞: extracts maximum damping from local transport
- Weighted C^{1/2}: controls non-local Biot-Savart (loses a derivative)
- Weights: singular near origin (suppress boundary advection), grow in far-field (ensure decay)

## 5. Bridge: 2D Boussinesq ↔ 3D Euler

At boundary r=1, 3D axisymmetric Euler maps to 2D Boussinesq on R²₊.
- Swirl velocity u_θ acts as Boussinesq density θ
- Curvature terms (1/r) are O(x) perturbations
- As singularity focuses (spatial scale → 0), curvature terms vanish
- Absorbed as small error in weighted stability analysis

KEY: Proving Boussinesq blowup = proving Euler blowup (at boundary)

## 6. Initial Data

They do NOT use Luo-Hou 2014 or Hou 2022 ICs.
Theorem is existential: "there EXISTS smooth initial data..."

Actual IC = approximate self-similar profile, truncated + smoothed.
Nonlinear stability proven → any smooth data sufficiently close
to this profile in weighted spaces will blow up.

→ PySR finds the profile from our numerical data
→ That profile becomes the constructive IC for the proof

## 7. Part I vs Part II Split

Part I (Analysis):
- Dynamic rescaling formulation
- Weighted L∞ ∩ C^{1/2} spaces defined
- STABILITY LEMMA: "If approximate profile exists such that
  its stability constants satisfy specific strict inequalities,
  then the solution blows up."
- Pure analysis — no numerics

Part II (Rigorous Numerics):
- Computes approximate self-similar profile on refined grid
- Computer-assisted INTERVAL ARITHMETIC
- Rigorously bounds integrals, derivatives, Biot-Savart interactions
- Proves the numerical profile satisfies the Stability Lemma inequalities
- MATLAB code provided for verification

## Our Pipeline Mapping

| Chen-Hou | Our Approach |
|----------|-------------|
| Part I: Stability Lemma | Lean: state the inequality theorem |
| Part II: interval arithmetic | PySR + computer-assisted bounds |
| Approximate profile (numerical) | Dense timeseries → PySR → profile |
| MATLAB verification | Python solver + Lean verification |
| 2D Boussinesq → 3D Euler bridge | Same bridge, Lean-formalized |

## Questions for Part II
1. What interval arithmetic library/method?
2. Exact inequalities from Stability Lemma — list them
3. Grid resolution for approximate profile
4. How are Biot-Savart integrals rigorously bounded?
5. Error tolerance — how tight?
6. MATLAB code availability (mentioned in arxiv comments)
