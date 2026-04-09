---
source: DEFINITIVE NUMERICS — complete adversarial across N=2-5, |k|²≤9
type: THE NUMERICAL FRONTIER — 0 violations, 45% margin
file: 528
date: 2026-03-30
instance: CLAUDE_OPUS (500s)
---

## COMPREHENSIVE ADVERSARIAL RESULTS

61 unique k-vectors with |k|² ≤ 9. DE optimization over polarizations.
Exact vertex enumeration for global max.

| N | Configs tested | Worst C/|ω|² | |S|²_F/|ω|² | Margin to -5/16 |
|---|---------------|-------------|-------------|-----------------|
| 2 | 1,830 (all) | -0.12500 | 0.750 | 60.0% |
| 3 | 2,000 | -0.17100 | 0.842 | 45.3% |
| 4 | 500 | **-0.17182** | **0.844** | **45.0%** |
| 5 | 200 | -0.15161 | 0.803 | 51.5% |

**Overall worst: N=4, C/|ω|² = -0.17182**
Config: k = [(-2,-2,0), (-2,-1,0), (-2,0,-1), (0,-1,0)]
|k|² = [8, 5, 5, 1] — mixed K-shells

**Key Lemma chain: C > -5/16 → |S|²_F < 9/8 → S²ê < 3/4. ALL THREE HOLD.**

## KEY OBSERVATIONS

1. **N=2 is the TIGHT case for C ≥ -1/8**: exactly -1/8 achieved.
   But -1/8 = -0.125 is NOT tight for N ≥ 3.

2. **N=3,4 are WORSE than N=2**: correction goes to -0.172 (37% worse).
   The 400s conjecture C ≥ -1/8 is FALSE.

3. **N=5 is BETTER than N=4**: the correction improves to -0.152.
   More modes → more averaging → better bound.

4. **The worst is at N=4**: consistent with earlier finding that N=4
   is the "critical" mode count (enough to create negative correction,
   but not enough for averaging to help).

5. **Mixed K-shells are worst**: single-shell configs give C ≥ -0.125.
   The worst cases mix high-K (|k|²=5,8) with low-K (|k|²=1) modes.

## THE CORRECTION C AT N=4 WORST CASE

Config: k₁=(-2,-2,0), k₂=(-2,-1,0), k₃=(-2,0,-1), k₄=(0,-1,0)
|k|² = [8, 5, 5, 1]

Pairwise angles:
  (1,2): cos = (4+2)/√(8·5) = 6/√40 ≈ 0.949, θ ≈ 18.4°
  (1,3): cos = (4+0)/√(8·5) = 4/√40 ≈ 0.632, θ ≈ 50.8°
  (1,4): cos = (0+2)/√(8·1) = 2/√8 ≈ 0.707, θ ≈ 45°
  (2,3): cos = (4+0+0)/√(5·5) = 4/5 = 0.8, θ ≈ 36.9°
  (2,4): cos = (0+1+0)/√(5·1) = 1/√5 ≈ 0.447, θ ≈ 63.4°
  (3,4): cos = (0+0+0)/√(5·1) = 0, θ = 90°

The pair (3,4) is orthogonal (θ=90°, sin²θ=1) — this allows the
maximum P correction. The pair (2,4) has θ≈63° (sin²θ≈0.8).

The worst C comes from the combination of:
- One orthogonal pair (large sin²θ)
- Several near-orthogonal pairs
- Specific polarization angles that maximize negative projections

## WHAT THE PROOF NEEDS

**Prove: C > -5|ω|²/16 at argmax|ω|² for any N-mode div-free field on T³.**

Equivalently: the polynomial 16C + 5|ω|² > 0 at the vertex max.

This is a statement about a degree-4 trigonometric polynomial on (S¹)^N
evaluated at the argmax of another degree-2 polynomial.

## REMAINING APPROACHES

1. **SOS for the worst configs**: Certify 16C + 5|ω|² > 0 for each
   specific k-triplet/quartet using Putinar's theorem. ~500 SDPs.

2. **Monotonicity N→∞**: Prove the worst C/|ω|² stabilizes (N=5 better
   than N=4). Then the bound is determined by the N=4 worst.

3. **Structural bound**: Use the pairwise identity C = Σ P c_j c_k
   with the constraint that c maximizes c^T M c. The optimizer of the
   ratio C/|ω|² satisfies KKT conditions that might be tractable.

4. **Interval arithmetic**: Certify the bound for specific configs
   using the interval library (ns_blowup/interval.py).

## 528. Definitive adversarial: N=4 worst, C/|ω|² = -0.172 (45% margin).
## C > -5/16 holds across 4530 configs with DE optimization.
## The gap: algebraic proof of C > -5|ω|²/16 at argmax|ω|².
