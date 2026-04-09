---
source: Paper outline — organizing 126 proof files into a manuscript
type: PAPER STRUCTURE
date: 2026-03-26
---

# Shell Depletion, Phase Scrambling, and the Self-Limiting
# Enstrophy Cascade in Three-Dimensional Navier-Stokes

## Authors
Jason Burton, Independent Researcher

## Abstract (~200 words)
We investigate the mechanism of enstrophy transfer in the 3D incompressible
Navier-Stokes equations through a combination of rigorous harmonic analysis,
Littlewood-Paley shell decomposition, and large-scale pseudospectral
computation. We establish a closed-form angular profile f(α) = cos(α/2)/2
for the bilinear Biot-Savart symbol restricted to divergence-free fields,
yielding an exact Schur test bound θ₀ = 2/3 on the intra-shell transfer
ratio. Through systematic numerical experiments across multiple initial
conditions and resolutions, we identify a two-mechanism self-limiting
structure: (1) non-resonant triadic interactions (95% of transfer) are
decorrelated by advective sweeping at frequency ~2^j, and (2) the remaining
resonant residual near flow stagnation points exhibits a compressive sign
flip at high vorticity intensity, actively opposing the enstrophy cascade.
We propose a three-pillar proof architecture for global regularity based on
energy bounds, normal form transformation, and the intensity-dependent
compressive mechanism. Machine-verified algebraic lemmas (Lean 4) and 85+
floating-point verification runs support the framework.

---

## 1. Introduction (3 pages)

### 1.1 The Problem
- 3D NS global regularity (Clay Millennium Prize)
- Vorticity formulation, BKM criterion
- Why existing approaches fail (Tao barrier, CZ limits)

### 1.2 Our Approach
- Littlewood-Paley shell analysis of enstrophy transfer
- Novel: bilinear symbol angular profile + phase scrambler mechanism
- Three-pillar architecture: energy + normal form + compressive sign flip

### 1.3 Main Results
- Theorem A: f(α) = cos(α/2)/2 (bilinear symbol, standalone)
- Theorem B: θ₀ = 2/3 (Schur test bound)
- Computational Finding C: two-mechanism self-limiting cascade
- Conditional Theorem D: if Lemma 3 (compressive flip) holds → regularity

### 1.4 Outline

---

## 2. Preliminaries (3 pages)

### 2.1 Notation and Function Spaces
- T³ periodic domain, Sobolev/Besov spaces
- Littlewood-Paley decomposition, shell notation

### 2.2 The Vorticity Equation
- ∂_t ω + u·∇ω = ω·∇u + ν∆ω
- Biot-Savart law, Leray projection

### 2.3 Shell Enstrophy Balance
- E_j, T(j,j'), diagonal vs off-diagonal transfer
- BKM in shell language

### 2.4 Classical Results
- Energy inequality, BKM criterion, Fujita-Kato local existence
- CZ bounds, Bernstein inequalities

---

## 3. The Bilinear Symbol (5 pages) — STANDALONE PUBLISHABLE

### 3.1 Definition
- M(ξ̂,η̂) = P_ξ · Ŝ(ξ-η) · P_η (restricted bilinear symbol)
- Rotational invariance: depends only on angle α = ∠(ξ̂,η̂)

### 3.2 The Angular Profile
- **Theorem 3.1**: f(α) = cos(α/2)/2
- Proof: explicit coordinates ξ̂=ẑ, η̂=(sinα,0,cosα)
- Key identity: cos(α/2)cosα + sin(α/2)sinα = cos(α/2)
  (Lean-verified: AngularProfile.lean)
- Both singular values equal cos(α/2)/2

### 3.3 The Schur Test
- **Theorem 3.2**: θ₀ = 2/3
- Schur integral: I = 2π∫cos²(α/2)sin(α/2)dα = 4π/3
- u-substitution proof (3 lines)

### 3.4 Properties
- Diagonal vanishing: M(ξ̂,ξ̂) = 0 (Lean: SingleMode.lean)
- Antipodal vanishing: M(ξ̂,-ξ̂) = 0 (new lemma)
- Connection to single-mode orthogonality

### 3.5 Comparison to Literature
- Improves dimensional CZ constants for intra-shell interactions
- Comparison to Budden's spectral gap (different approach, same problem)

---

## 4. The Phase Scrambler (5 pages)

### 4.1 Shell ODE Model
- Constant θ < 1: blows up for ANY θ > 0
- θ(j) ~ 2^{-j}: bounded (critical decay rate)
- **The diagonal is the ONLY blowup mechanism**

### 4.2 Decomposing the NS Nonlinearity
- Stretching alone vs advection alone vs full NS
- Table: j=3 stretching +462%, advection +337%, full NS −51%
- The cancellation IS the pressure (Leray projector)

### 4.3 Oscillation Frequency
- θ(j,t) oscillates with frequency ~ 2^j
- Data: 0.2→0.8→1.1→1.7 Hz (j=1→4)
- Anti-twist cycles: growth → peak → collapse

### 4.4 Peak θ is Bounded
- max θ ≈ 0.013 across all shells and times
- 40× below Schur worst case 2/3

---

## 5. The Normal Form Architecture (5 pages)

### 5.1 Resonant/Non-Resonant Decomposition
- Sweeping frequency Ω = k·u_{<j}
- Non-resonant: |Ω| ≥ c·2^j (95% of transfer)
- Resonant: |Ω| < c·2^j (5% near stagnation points)
- Data table: resonant fraction by shell

### 5.2 The Normal Form Corrector
- Define B_j to absorb non-resonant oscillations
- Modified enstrophy Ẽ_j = E_j - B_j
- 2^{-j} gain from the corrector (dividing by Ω ~ 2^j)
- Reference: Shatah (1985), adapted to dissipative setting

### 5.3 The Resonant Residual
- 5% of transfer, near stagnation points
- Spatial disjointness: IC-dependent (works for TG, not KP)
- Must handle differently → Pillar 3

---

## 6. The Compressive Sign Flip (5 pages) — THE NEW MECHANISM

### 6.1 Discovery
- Resonant stretching turns NEGATIVE at high |ω|
- Data: KP j=3 S_res = −3.95e+04 (while S_total = +1.52e+04)
- TG t=5: j=2,3 flip at |ω| ≈ 17

### 6.2 Intensity Threshold
- Sign flip activates at |ω|_max ≈ 13-17
- Resolution-independent (N=32 and N=64 both show it)
- Correlates with pressure Hessian crossover at ρ ≈ 12

### 6.3 Physical Mechanism
- Quasi-2D geometry: k·u ≈ 0 → triads flattened
- Isotropic pressure dominates deviatoric at high |ω|
- Net compression in the resonant quasi-2D plane
- Alignment data: cos²(ω,e₁) = 0.307 (resonant) vs 0.343 (non-resonant)

### 6.4 The Self-Limiting Feedback Loop
- |ω| ↑ → local Re ↑ → stretching flips negative → |ω| stabilizes
- Turbulence IS the regularity mechanism
- Laminar→turbulent transition at each shell prevents blowup

### 6.5 Universality
- Confirmed for TG (t=5), KP (t=3), JB vortex (t=3)
- The flip correlates with INTENSITY, not IC geometry
- Activates precisely when standard bounds would fail

---

## 7. Proof Architecture (3 pages)

### 7.1 Three Pillars
- Pillar 1: Energy bounds for j ≤ j* (standard)
- Pillar 2: Normal form for non-resonant 95% (2^{-j} gain)
- Pillar 3: Compressive sign flip for resonant 5% (self-limiting)

### 7.2 The Bootstrap
- At each shell j: the transfer is either swept (→ normal form)
  or stuck (→ compressive)
- No escape route for sustained supercritical stretching

### 7.3 Remaining Analytical Steps
- Formalize the normal form for NS on T³
- Prove the compressive sign flip from the quasi-2D pressure geometry
- Connect the three pillars in a Besov bootstrap → BKM

---

## 8. Computational Validation (5 pages)

### 8.1 Pseudospectral Solver
- Method: RK4, 2/3 dealiasing, periodic T³
- Resolutions: N=16,32,64,128,256

### 8.2 Resolution Convergence
- 50 seeds N=128, 20 seeds N=256: all ratio 1.0000
- JB vortex: converged across N=64/128/256

### 8.3 Shell Transfer Data
- Resolution-independent at N=64 and N=128
- Diagonal depletion: 3-5%, off-diagonal decay: 0.65

### 8.4 Phase Scrambler Validation
- Decomposition data, oscillation frequencies
- Sign flip threshold, resolution independence

---

## 9. Lean Formalization (2 pages)

### 9.1 Machine-Verified Lemmas
1. single_mode_orthogonality (SingleMode.lean)
2. strain_self_depletion (StrainSelfDepletion.lean)
3. direction_rotation_nonneg (DirectionRotation.lean)
4. angular_profile_identity (AngularProfile.lean)

### 9.2 Verification Pipeline
- Lean 4 + Mathlib, lake build (1429 jobs)
- Comparator certification, standard axioms only

### 9.3 Limitations
- PDE analysis beyond current Lean/Mathlib capability
- Algebraic core verified, functional analysis traditional

---

## 10. Discussion (2 pages)

### 10.1 Comparison to Other Approaches
- Budden: spectral gap (static, 7% margin)
- Chen-Hou: computer-assisted Euler blowup (different equation)
- Our approach: dynamic, uses NS-specific structure

### 10.2 The Physical Picture
- Turbulence prevents blowup (not causes it)
- The NS equations are self-regulating
- Implications for turbulence theory

### 10.3 Open Problems
- Rigorous proof of compressive sign flip (Lemma 3)
- Computer-assisted proofs with interval arithmetic
- Extension to non-periodic domains

---

## Appendices

### A. Proof of Theorem 3.1 (Angular Profile)
Full coordinate computation

### B. Shell Transfer Data Tables
Complete N=64, N=128 matrices

### C. Lean Source Code
All 4 verified theorems

---

## References (~30 papers)
Constantin-Fefferman, Beale-Kato-Majda, Buaria-Lawson-Wilczek,
Miller, Kang-Protas, Chaves-Santos-Ferreira, Budden,
Shatah, Germain-Masmoudi-Nakanishi, Bony, ...

## 127 proof files. Paper structure complete.
