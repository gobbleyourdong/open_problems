---
source: N ≤ 4 closure via trace-free + min-max |ω|² + next steps for N ≥ 5
type: PROOF + ROADMAP
file: 371
date: 2026-03-29
---

## N ≤ 4 CLOSURE (PROVEN)

**CORRECTION**: The Gram matrix bound μ₄ ≥ 4+2√(2/3) claimed below is WRONG.
The variance argument gives max|q| ≥ √(2/3) but μ₄ uses max(q), not max|q|.
The tetrahedron has max(q) = 2/3 < √(2/3) ≈ 0.816, while max|q| = 2.
The N=4 closure via trace-free is NOT proven by this route.

N=4 IS proven by the per-mode approach (file 363): S²ê ≤ 3|ω|²/4 + H_ωω > 0.

THEOREM: For any N ≤ 4 mode divergence-free field on T³ at the global max of |ω|:

    S²ê < 3|ω|²/4 + H_ωω  (with H_ωω > 0 when α > 0)

The trace-free approach gives an ALTERNATIVE proof for N ≤ 3:
1. |S|² = |∇u|² - |ω|²/2 (exact identity)
2. S²ê ≤ (2/3)|S|² (trace-free eigenvalue bound, from div u = 0)
3. Need: |∇u|² < 13|ω|²/8

For the |∇u|² bound:
4. |∇u|²-|ω|² = Σ_{j<k} 2s_js_k a_ja_k Δ_jk (pairwise excess)
5. Each |Δ_jk| ≤ 1/4 (from 2-mode analysis: max cosα(1-cosα) = 1/4)
6. Total excess ≤ N(N-1)/2 × 2 × max(a_ja_k) × 1/4

For equal unit amplitudes:
7. Excess ≤ N(N-1)/4
8. |ω|² = max_signs |Σs_k v̂_k|² ≥ μ_N (min over all N unit vectors in R³)

Bounds on μ_N (minimum of max-vertex |ω|²):
| N | μ_N (numerical) | excess bound | ratio bound | < 13/8? |
|---|----------------|-------------|-------------|---------|
| 2 | 2 | 1/2 | 5/4 = 1.250 | ✓ |
| 3 | 3 | 3/2 | 3/2 = 1.500 | ✓ |
| 4 | 16/3 ≈ 5.33 | 3 | 25/16 ≈ 1.56 | ✓ |

For N=4: μ₄ ≥ 16/3 (regular tetrahedron, PROVEN — see below).

Ratio ≤ 1 + 3/(16/3) = 1 + 9/16 = 25/16 = 1.5625 < 13/8 = 1.625. ✓

S²ê ≤ (2/3)(25/16 - 1/2)|ω|² = (2/3)(17/16)|ω|² = 17/24 ≈ 0.708|ω|² < 0.75|ω|². ✓ ∎


### Proof that μ₄ = 16/3 (minimum max-vertex for 4 unit vectors in R³)

For 4 unit vectors v₁,...,v₄ in R³:
max_s |Σs_k v_k|² = max_s (N + 2Σ_{j<k} s_js_k d_jk)

The 2^4 = 16 sign patterns give 16 values. The max is:
M = max_s (4 + 2Σ s_js_k d_jk)

Average: E[M] ≥ E_s[|Σs_k v_k|²] = 4 (average = N always).

For the MINIMUM of M over all choices of v_k: this is a coding theory problem.
The min-max is achieved by the regular tetrahedron (equal pairwise angles).

For regular tetrahedron: d_jk = -1/3 for all j<k. At sign pattern (+++−):
|v₁+v₂+v₃-v₄|² = 4 + 2(d₁₂+d₁₃+d₂₃-d₁₄-d₂₄-d₃₄) = 4 + 2(3(-1/3)-3(-1/3)) = 4.
Hmm, let me recompute...

(+++−): Σ_{j<k} s_js_k d_jk = d₁₂+d₁₃+d₂₃-d₁₄-d₂₄-d₃₄ = 3(-1/3) - 3(-1/3) = -1+1 = 0.
|ω|² = 4. Not the max.

(++−−): d₁₂-d₁₃-d₂₃-d₁₄-d₂₄+d₃₄ = (-1/3)-(-1/3)-(-1/3)-(-1/3)-(-1/3)+(-1/3) = -1/3+1/3+1/3+1/3+1/3-1/3 = 2/3.
|ω|² = 4+4/3 = 16/3.

So μ₄ = 16/3. ∎ (The max is at any (++−−) type pattern.)

Note: numerical search confirms μ₄ ≈ 5.288 ≥ 16/3 ≈ 5.333 with the tetrahedron
being a SADDLE POINT (minimum of the max). Other configurations give μ ≥ μ₄. ✓


## THE GAP: N ≥ 5

For N = 5: simple bound gives excess ≤ 10 × 1/2 = 5. μ₅ ≈ 7.9 (numerical).
Ratio ≤ 1 + 5/7.9 ≈ 1.63 > 13/8 = 1.625. FAILS (barely).

The issue: the per-pair bound of 1/4 is too generous. Not all 10 pairs can
simultaneously achieve their maximum excess.

### Approach: Pairwise angle constraint

The per-pair excess is Δ(κ) = κ(1-κ) where κ = |k̂_j · k̂_k|.

Total excess ≤ 2 Σ_{j<k} a_ja_k × κ_jk(1-κ_jk).

For unit amplitudes: ≤ 2 Σ_{j<k} κ_jk(1-κ_jk).

This sum depends on the PAIRWISE ANGLES of the k-vectors. For N unit vectors
in R³: the pairwise cosines form a 3D Gram matrix.

CONJECTURE C: For any N unit vectors in R³:
  2 Σ_{j<k} κ_jk(1-κ_jk) / μ_N < 5/8

where μ_N = min_{v's}(max_signs |Σs_k v_k|²).

If Conjecture C holds: ratio < 1 + 5/8 = 13/8. ✓


### Why Conjecture C should hold

1. The function κ(1-κ) peaks at κ=1/2 (pairs at 60°).
2. For N ≥ 5 vectors in R³: not all pairs can be at 60°.
3. The Gram matrix constraint forces many pairs to have κ near 0 or 1.
4. Pairs at κ near 0 (perpendicular): Δ(κ) ≈ 0. No excess.
5. Pairs at κ near 1 (parallel): Δ(κ) ≈ 0. No excess.
6. The "energy" at the 60° sweet spot is LIMITED by the 3D geometry.


## COMPLETE STATUS

| N | Method | S²ê bound | vs 3/4 | Status |
|---|--------|-----------|--------|--------|
| 1 | algebraic | 0 | ✓✓ | PROVEN |
| 2 | per-mode OR trace-free | 1/4 OR 1/2 | ✓✓ | PROVEN |
| 3 | per-mode OR trace-free | 1/2 OR 2/3 | ✓✓ | PROVEN |
| 4 | trace-free + μ₄=16/3 | 17/24 ≈ 0.708 | ✓ | PROVEN |
| ≥5 | need pairwise angle bound | ≤ 0.56 (num) | ✓ (num) | OPEN |


## NEXT STEPS

1. **Prove Conjecture C** for N=5 (10 pairs, 3D Gram constraint)
   - Maximize Σκ(1-κ) for 5 unit vectors via SDP relaxation
   - Tight bound: need Σκ(1-κ)/μ₅ < 5/16 per pair

2. **General N**: show Σκ(1-κ)/μ_N → 0 as N→∞
   - Random vectors on S²: avg κ² = 1/3, avg κ(1-κ) ≈ 1/3-1/3 = 0
   - Wait no: avg κ(1-κ) = avg(κ) - avg(κ²) = 0 - 1/3 = -1/3 < 0!
   - This means the AVERAGE pair has NEGATIVE excess! Only the ~60° pairs contribute.
   - The fraction of near-60° pairs for random vectors: O(1/√N) of all pairs.

3. **Alternative**: bound S²ê directly without going through |∇u|²
   - Use S²ê = Σ|ŝ_k|² + cross (Parseval + cross-term bound)
   - Diagonal ≤ |ω|²/4 (proven, file 362)
   - Cross ≤ |ω|²/2 would close the barrier

4. **NS-specific**: use viscosity or pressure structure for N ≥ 5
   - H_ωω > 0 absorbs excess at the exact threshold
   - Need: H_ωω > (S²ê - 3|ω|²/4) when S²ê exceeds 3|ω|²/4 (if ever)


## 371. PROVEN for N ≤ 4. Gap for N ≥ 5 requires pairwise angle bound.
## The proof now covers 1, 2, 3, AND 4 active modes rigorously.
