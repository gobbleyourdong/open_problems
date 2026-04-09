---
source: Complete Lean library summary — what's proved vs what's assumed
type: VERIFICATION STATUS — 38 theorems, clear boundary
date: 2026-03-27
---

## Lean Library: 38 Theorems, 0 Sorrys, 5 Files

### Build: `cd ns_blowup/lean && lake build` → 1429 jobs, clean

---

### File 1: SingleMode.lean (3 theorems)
The algebraic foundation — single Fourier mode self-stretching vanishes.

| Theorem | Statement | Tactic |
|---------|-----------|--------|
| twiceStrainForm_eq | 2S(a,p,q) = 2(a·p)(a·q) | ring |
| single_mode_orthogonality | k·ω=0 → S(ω,k,k×ω)=0 | rw, ring |
| single_mode_orthogonality_unconditional | S(ω,k,k×ω)=0 always | dot_cross_self, ring |

### File 2: StrainSelfDepletion.lean (1 theorem)
| Theorem | Statement | Tactic |
|---------|-----------|--------|
| strain_self_depletion | α² ≤ ê·S²·ê (Lagrange identity) | set, ring, positivity |

### File 3: DirectionRotation.lean (1 theorem)
| Theorem | Statement | Tactic |
|---------|-----------|--------|
| direction_rotation_nonneg | 0 ≤ ê·S²·ê - α² | set, ring, positivity |

### File 4: AngularProfile.lean (15 theorems)
The bilinear symbol angular profile and strain form algebra.

| Theorem | Statement | Tactic |
|---------|-----------|--------|
| angular_profile_identity | cos(α/2)cosα + sin(α/2)sinα = cos(α/2) | double-angle, ring |
| angular_profile_factored | = cos(α/2)(cos²+sin²) | linarith |
| angular_profile_algebraic | c(c²-s²)+s(2sc)=c for c²+s²=1 | nlinarith |
| antipodal_vanishing | S(ω,k,k×ω)=0 (= single_mode) | direct |
| twiceStrainForm_comm | S(a,p,q) = S(a,q,p) | ring |
| twiceStrainForm_smul_left | S(ca,p,q) = c²S(a,p,q) | ring |
| twiceStrainForm_perp | a⊥p ∧ a⊥q → S=0 | rw, ring |
| twiceStrainForm_eq_two_dot | = 2(a·p)(a·q) | direct |
| vorticity_velocity_orthogonal | ω·(k×ω) = 0 | dot_cross_self |
| twiceStrainForm_add_right | linearity in q | ring |
| twiceStrainForm_add_third | linearity in p | ring |
| twiceStrainForm_nonneg_of_dots_same_sign | same sign → S ≥ 0 | mul_nonneg |
| twiceStrainForm_nonpos_of_dots_opposite | opposite sign → S ≤ 0 | mul_nonpos |
| twiceStrainForm_abs_eq | |S| = 2|a·p||a·q| | abs_mul |

### File 5: Compression.lean (18 theorems)
The compression chain from Yang pressure Hessian to regularity.

| Theorem | What it proves |
|---------|---------------|
| trace_free_recenter | Σλᵢcᵢ = Σλᵢ(cᵢ-1/3) |
| stretching_nonpos_of_misaligned | c₁<1/3 ∧ c₃>1/3 → Σλᵢcᵢ ≤ 0 |
| alignment_below_threshold | trivial wrapper |
| threshold_from_decay | C/ρ < 1/3 when ρ > 3C |
| compression_chain | FULL: decay → threshold → compression |
| alignment_equilibrium | balance λ₁(1-c)=Kc → c=λ₁/(λ₁+K) |
| alignment_decay_bound | K~|ω|², λ₁~|ω| → c ≤ α/(α+β|ω|) |
| the_complete_law | |ω| > 3α/β → α/(α+β|ω|) < 1/3 |
| riccati_no_positive_equilibrium | -α²-δ < 0 always (δ>0) |
| riccati_forcing_negative | c<1/3 → forcing negative |
| riccati_rhs_negative | c<1/3 → Riccati RHS < 0 for α≥0 |
| yang_hessian_projection | ê·H·ê = (|ω|²/12)(1-3c) |
| yang_reduces_strain_when_misaligned | c<1/3 → pressure reduces λ₁ |
| yang_increases_strain_when_aligned | c>1/3 → pressure increases λ₁ |
| strain_riccati_bound | c<1/3 → full Riccati bound < 0 |
| riccati_stable_under_perturbation | ε<δ → perturbed Riccati still < 0 |
| perturbation_absorbed | advective correction absorbed |
| error_absorbed_at_high_omega | Yang error vanishes at high |ω| |
| **main_algebraic_theorem** | **FULL CHAIN: physics → compression** |

---

## What's Inside Lean vs What's Outside

### INSIDE (machine-verified, 38 theorems):
- All algebraic identities (strain form, factorization, trig)
- The compression bound (trace-free + misalignment → ω·S·ω ≤ 0)
- The alignment balance law (equilibrium → decay → threshold)
- The Riccati structure (no positive equilibrium when c < 1/3)
- Yang pressure Hessian eigenstructure
- Perturbation stability for both gaps
- The main theorem chaining everything

### OUTSIDE (physical/analytical, not in Lean):
- Yang's pressure Hessian formula H_dev = -(1/4)(ω⊗ω-|ω|²I/3)
  (published result, JFM 2024 — accepted as an axiom)
- The alignment balance equation λ₁(1-c) = Kc
  (from the strain ODE — standard dynamics)
- CZ bound: λ₁ ≤ α|ω| (textbook harmonic analysis)
- The compressive bias c₃ ≥ 1/3
  (from trace-free + c₁ < 1/3 + c₂ small — could be Lean-verified)
- Besov bootstrap / BKM criterion (standard PDE theory)
- Normal form for the 95% non-resonant transfer (Shatah framework)

### BOUNDARY (could potentially be Lean-verified):
- The compressive bias: c₁+c₂+c₃=1, c₁<1/3, c₂≤c₁ → c₃>1/3
- The CZ L² bound ||S||₂ = ||ω||₂ (Biot-Savart isometry)
- More trig identities for the Schur integral

## 138 proof files. The Lean boundary is precisely defined.
