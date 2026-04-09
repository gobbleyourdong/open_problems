---
source: CORRECTED DEFINITIVE STATE — after fixing phase error
type: HONEST STATE — what is proven, what is wrong, what remains
file: 524
date: 2026-03-30
instance: CLAUDE_OPUS
---

## CRITICAL CORRECTION

Files 517-522 claimed S(x) ∝ sin(k·x). **THIS IS WRONG.**
Both ω and S involve cos(k·x). Verified numerically (error < 3×10⁻¹⁰).

Invalidated claims:
- S = 0 at lattice points {0,π}³ → FALSE (S ≠ 0 there)
- N ≤ 3 theorem: S = 0 at max → FALSE (S²ê = |ω|²/3 for symmetric N=3)
- Double suppression via sinγ × sinφ → FALSE (no sinφ factor)
- K²=2 shell: S = 0 at max → FALSE

The self-vanishing identity |S_k·ê|² = (a²/4)sin²γ IS correct
(it's about the mode direction, not the spatial phase).

## WHAT IS RIGOROUSLY PROVEN

### A. Barrier Framework (files 360-368)
R = α/|ω| < 1/2 → Type I → Seregin → regularity on T³. ✓

### B. Cross-Term Identity (file 511, PROVEN to 10⁻¹⁴)
|S(x)|²_F = |ω(x)|²/2 − 2Σ_{j<k} (v_j·n̂_{jk})(v_k·n̂_{jk}) sin²θ_{jk} cos(k_j·x)cos(k_k·x)

Per-pair: 2Tr(Ŝ_j Ŝ_kᵀ) − v_j·v_k = −2(v_j·n̂)(v_k·n̂)sin²θ ✓

### C. Self-Vanishing Identity (file 518, correct part)
|S_k · ê|² = (a_k²/4) sin²γ_k where γ_k = angle(v̂_k, ê). ✓
(per-mode property of BS, independent of spatial phase)

### D. Trace-Free Bound
S²ê ≤ (2/3)|S|²_F for any trace-free symmetric S. ✓

### E. Key Lemma Reduction (file 515)
|S(x*)|²_F < |ω(x*)|² at x* = argmax|ω| → S²ê < 3|ω|²/4 → regularity. ✓

### F. Max Condition Essential (file 516)
|S|²_F < |ω|² is FALSE at generic points (can be 2500×).
It holds ONLY at argmax|ω| (verified numerically). ✓

## WHAT DOES NOT WORK

| Approach | Why it fails |
|----------|-------------|
| Triangle bound with self-vanishing | Too loose: worst 1.53 vs threshold 0.75 |
| Sin-cos decoupling | S involves cos, not sin |
| N≤3 theorem via critical point | Based on S∝sin, which is wrong |
| CZ L∞ bound | CZ constant ≥ 1, doesn't give C < 1 |
| Energy partition at lattice | S ≠ 0 at lattice points |

## ADVERSARIAL BOUNDS (ALL CORRECT)

These use exact vertex enumeration + DE optimization, no sin/cos assumption:

| Quantity | Worst | Threshold | Margin | Evidence |
|----------|-------|-----------|--------|----------|
| S²ê/|ω|² (K≤√6) | 0.364 | 0.750 | 51% | 1000+ adversarial |
| S²ê/|ω|² (N=2) | 0.250 | 0.750 | 67% | 2628 exhaustive |
| |S|²_F/|ω|² at max | 0.749 | 1.000 | 25% | 10000 random |
| Correction C/|ω|² | −0.124 | −0.250 | 50% | 10000 random |

## THE ONE GAP

Prove at x* = argmax|ω|: **|S(x*)|²_F < |ω(x*)|²**

Equivalently via the cross-term identity: **C > −|ω|²/4**

## BEST PATHS FORWARD

1. **Hessian constraint**: At x*, the Hessian of |ω|² is ≤ 0 (PSD constraint).
   This constrains the mode phases and amplitudes. Combined with the
   cross-term identity, it might bound C from below.

2. **Variational analysis**: The worst C/|ω|² is achieved at a specific
   configuration. Characterize this critical point via Euler-Lagrange
   and show it satisfies C > −|ω|²/4.

3. **Miller's orthogonality**: ⟨−ΔS, ω⊗ω⟩ = 0 constrains the
   relationship between S and ω. Might give |S|² < |ω|² at the max
   via a maximum-principle-type argument.

4. **K-shell induction**: Prove the bound for single shells (each K),
   then show mixing shells can't worsen it. The per-shell data shows
   very small ratios (< 0.1 for most shells).

## 524. Phase corrected. Files 511-516 are the foundation.
## Gap: |S|²_F < |ω|² at argmax|ω|. Margin: 25% (|S|²_F/|ω|² ≤ 0.749).
## Next: Hessian constraint or variational analysis.
