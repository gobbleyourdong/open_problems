---
source: Evan Miller (2024/2026) arXiv:2407.02691 — Pure and Applied Analysis 8:247-272
type: GAME CHANGER — strain-vorticity decomposition + global regularity of SVI model
date: 2026-03-26
---

## The Key Results

### 1. The Orthogonality Identity (Theorem 3.1)
⟨-ΔS, ω⊗ω⟩ = 0
Laplacian of strain is L²-orthogonal to vorticity outer product. EXACT.

### 2. Strain-Vorticity Interaction Model has GLOBAL REGULARITY (Theorem 1.2)
The model equation that keeps ONLY the strain-vorticity interaction
(dropping strain self-amplification and advection) is globally regular.
The dangerous part is ISOLATED.

### 3. The Dangerous Part
Q = P_st((u·∇)S + S² + (3/4)ω⊗ω)
Blowup requires ||Q||/||-ΔS|| ≥ 1 near T* (Theorem 1.9).

### 4. Eigenfunction Distance Criterion (Theorem 1.12)
If strain stays close to a Laplacian eigenfunction:
∫₀ᵀ inf_ρ ||-ρΔS - S||^p_{L^q} dt < ∞ → regularity

### 5. Quantitative Endpoint (Theorem 1.13)
Blowup requires: limsup inf_ρ ||-ρΔS - S||_{L^{3/2}} ≥ 2(π/2)^{4/3} ≈ 3.85

## Why This Changes Everything

Miller SEPARATES the NS nonlinearity into:
- **Benign part**: strain-vorticity interaction (globally regular)
- **Dangerous part**: strain self-amplification + advection (Q)

The proof reduces to: BOUND Q.

This is LOCAL/DIFFERENTIAL structure (passes Tao's barrier).
CZ bounds can't distinguish benign from dangerous. Miller's decomposition can.

## Connection to Our Work

Our Lean lemma (single-mode orth) is the MODE-LOCAL version of Miller's
GLOBAL orthogonality. Miller extends it to cross-mode + Laplacian-weighted.

Our strain self-depletion (α² ≤ ê·S²·ê) constrains the S² part of Q.
Miller isolates S² as the dangerous term — our lemma bounds it.

The eigenfunction distance criterion is COMPUTATIONALLY TESTABLE.
We can measure inf_ρ ||-ρΔS - S||_{L^{3/2}} on our solver.
If it stays below 3.85 → regularity verified for that IC.
