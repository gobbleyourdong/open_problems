---
source: PHASE CORRECTION — S involves cos(k·x), NOT sin(k·x)
type: ERROR CORRECTION — files 517-522 built on incorrect premise
file: 523
date: 2026-03-30
instance: CLAUDE_OPUS
---

## THE ERROR

Files 517-522 claimed: "S(x) = Σ S_k sin(k·x)" (strain in sine space).

**THIS IS WRONG.** Verified numerically to 2.7×10⁻¹⁰:

For ω(x) = Σ v_k cos(k·x) on T³ (div-free, v_k ⊥ k):
- Velocity: u(x) = -Σ (k × v_k) sin(k·x) / |k|²  [sine space ✓]
- Gradient: ∇u ∝ cos(k·x)  [derivative turns sin to cos ✓]
- **Strain: S(x) = sym(∇u) = Σ Ŝ_k cos(k·x)  [COSINE space]**

Both ω and S involve cos(k·x). The "sin-cos decoupling" does NOT exist.

## CONSEQUENCES: WHAT IS INVALIDATED

| Claim | File | Status |
|-------|------|--------|
| S ∝ sin(k·x) | 518 | **WRONG** |
| S = 0 at lattice points {0,π}³ | 519,520 | **WRONG** (S ≠ 0) |
| N ≤ 3 theorem (S = 0 at max) | 519 | **WRONG** (S²ê = |ω|²/3 for symmetric N=3) |
| Double suppression (sinγ × sinφ) | 518,520 | **WRONG** (no sinφ factor) |
| K²=2 shell: S = 0 at max | 520 | **WRONG** (S ≠ 0 at lattice points) |

## WHAT REMAINS CORRECT

| Result | File | Status |
|--------|------|--------|
| Self-vanishing: \|S_k·ê\|² = (a²/4)sin²γ | 518 | ✓ (direction property, not phase) |
| Cross-term identity: \|S\|²_F = \|ω\|²/2 - 2C | 511 | ✓ (PROVEN, verified to 10⁻¹⁴) |
| Barrier framework | 360s | ✓ |
| Adversarial bounds (S²ê/\|ω\|² ≤ 0.364) | 513 | ✓ |
| Key Lemma reduces to \|S\|²_F < \|ω\|² | 515 | ✓ |
| Max condition essential | 516 | ✓ |

## THE ACTUAL N=3 SYMMETRIC CASE

k₁=(1,0,0), k₂=(0,1,0), k₃=(0,0,1), cyclic polarizations:
ω(0) = (1,1,1), |ω|² = 3, S²ê = 1, S²ê/|ω|² = 1/3 < 3/4 ✓

The bound HOLDS but S is NOT zero. The strain is fully present at
the max, just bounded by the self-vanishing identity.

## CORRECTED STATE

The proof gap remains exactly as stated in files 511-516:
**Prove |S(x*)|²_F < |ω(x*)|² at x* = argmax|ω|.**

The cross-term identity and adversarial bounds are the foundation.
The self-vanishing identity is an additional tool.
The sin-cos "double suppression" is a mirage.

## 523. Phase correction: S involves cos, not sin. Files 517-522
## are built on an error. The correct framework is files 511-516.
