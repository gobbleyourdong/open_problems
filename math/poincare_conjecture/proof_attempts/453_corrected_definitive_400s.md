---
source: CORRECTED DEFINITIVE 400s — after phase error fix, with correct numerics
type: THE HONEST STATE from the 400s instance
file: 453
date: 2026-03-30
instance: CLAUDE_A (400s)
---

## CORRECTION APPLIED

The sin-cos decoupling (files 446-451) was WRONG. S involves cos(k·x), not sin.
All numerical results recomputed with correct formulas.

## WHAT IS RIGOROUSLY PROVEN

### A. Barrier Framework (files 360-368, 439-441)
At R = α/|ω| = 1/2: DR/Dt < 0 whenever S²ê < 3|ω|²/4.
Barrier is repulsive. Vertex jump gives R_crit = 0.476 < 0.500.
R < 1/2 → Type I → Seregin → regularity. ✓

### B. Cross-Term Identity (500s file 511)
|S(x)|²_F = |ω(x)|²/2 − 2Σ (v_j·n̂)(v_k·n̂)sin²θ cos(k_j·x)cos(k_k·x) ✓

### C. Self-Vanishing Identity (500s file 518)
|S_k · ê|² = (a_k²/4)(1 − cos²γ_k) = (a_k²/4)sin²γ_k ✓
(per-mode directional property, independent of spatial phase)

### D. Trace-Free Bound
S²ê ≤ (2/3)|S|²_F for any trace-free symmetric matrix. ✓

### E. Key Lemma Reduction
|S|²_F < (9/8)|ω|² at x* = argmax|ω| → S²ê < (3/4)|ω|² → regularity. ✓

### F. N=2 Sharp Bound (500s file 525)
|S|²_F ≤ (3/4)|ω|² for any 2-mode field. TIGHT. S²ê ≤ |ω|²/2. ✓

### G. Negative Cross-Terms (400s file 445)
For orthogonal k-vectors: S_j:S_k = -D_{jk}/2 (proven).
C ≥ 0 for orthogonal k-vectors at constructive vertices. ✓

## CORRECTED ADVERSARIAL NUMERICS (0 violations)

### Vertex max (exact sign enumeration):
| Config | Trials | Worst S²ê/|ω|² | Worst |S|²/|ω|² | Margin |
|--------|--------|----------------|----------------|--------|
| N=3-7, K²=2,3,5,6 | 2000 | 0.219 | 0.487 | 70.8% |
| N=3, various shells | ~500 | 0.219 | 0.483 | 70.8% |
| N=4, various shells | ~500 | 0.168 | 0.488 | 77.6% |
| N=7, various shells | ~500 | 0.148 | 0.297 | 80.3% |

### Continuous max (DE optimization):
| Config | Trials | Worst S²ê/|ω|² | Worst |S|²/|ω|² | Margin |
|--------|--------|----------------|----------------|--------|
| N=3-7, K²=2,3,5,6 | 500 | 0.241 | 0.500 | 67.9% |

**Worst observed: S²ê/|ω|² = 0.241. Threshold: 0.750. Margin: 67.9%.**

## THE GAP (corrected)

Prove at x* = argmax|ω|²: **S²ê(x*) < (3/4)|ω(x*)|²**

Or via trace-free: **|S(x*)|²_F < (9/8)|ω(x*)|²**

Or via cross-terms: **C(x*) > -(5/16)|ω(x*)|²**

### Numerical margins:
- S²ê/|ω|² ≤ 0.241 vs threshold 0.750: **68% margin**
- |S|²/|ω|² ≤ 0.500 vs threshold 1.125: **56% margin**
- C/|ω|² ≥ -0.124 vs threshold -0.3125: **60% margin**

## THE MECHANISMS (corrected)

### 1. Self-vanishing (PROVEN)
At the max: ê aligns with dominant modes → sinγ ≈ 0 for them.
Their per-mode strain |S_k·ê| = (a/2)sinγ ≈ 0.
The DOMINANT modes contribute almost NOTHING to S²ê.

### 2. Self-alignment (structural, not yet proven)
ê tracks the largest mode direction. A mode cannot be both LARGE
and PERPENDICULAR to ê. If it's large: ê aligns with it → sinγ ≈ 0.

### 3. Directional cancellation (verified numerically)
The S_k·ê vectors point in different directions (determined by k-vectors).
Their sum partially cancels. Triangle inequality is only 53% tight.

## BEST PATHS FORWARD

1. **Prove the self-alignment bound**: At the max, the ratio
   Σ a_k sinγ_k / |ω| < √3 (= 1.73). This gives Key Lemma via
   self-vanishing + triangle inequality. Numerically: ratio < 0.98.

2. **Extend N=2 proof to N=3**: File 525 proves |S|² ≤ 3|ω|²/4 for N=2.
   The N=3 case involves 3 pairs of cross-terms. Explicit algebraic bound.

3. **Hessian constraint**: At the max, ∇²|ω|² ≤ 0 constrains the mode
   parameters. Combined with the cross-term identity: may bound C.

4. **Computational certification**: SOS for finite N (500s approach) or
   exhaustive vertex enumeration for all K-shell configs up to K_max.

## 453. Corrected state: S²ê/|ω|² ≤ 0.241 (margin 68%).
## |S|²/|ω|² ≤ 0.500 (margin 56%). C/|ω|² ≥ -0.124 (margin 60%).
## The self-vanishing identity is the primary tool. Phase mismatch is gone.
## Gap: prove analytically. 68% numerical margin.
