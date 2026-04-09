---
source: WHY 3+ modes can't exceed 5/4 — the vertex jump mechanism
type: KEY INSIGHT — the global max vertex changes when modes are added
file: 374
date: 2026-03-29
---

## THE PUZZLE

At the optimal 2-mode config (F₀ = 5/4):
- Some 3rd modes have dF/dε > 0 (positive marginal derivative)
- But the ACTUAL 3-mode ratio is always < 5/4 (verified 50K+ trials)
- How? The marginal analysis is misleading!

## THE RESOLUTION: VERTEX JUMP

The global max of |ω|² is at the vertex with signs (s₁,...,sN) that maximize
Σs_js_k a_ja_k D_{jk}. When a 3rd mode enters (a₃ > 0):

1. The NEW global max vertex may have DIFFERENT signs than the 2-mode vertex
2. At the new vertex: the ratio F is evaluated with different phase factors
3. The new vertex typically has HIGHER |ω|² (more modes contribute) but
   LOWER excess (the sign pattern doesn't align with the excess)

### Numerical demonstration:

Optimal 2-mode: k₁=(-2,-2,0), k₂=(-2,0,-2) at 60°. F = 5/4 at (s₁,s₂)=(+,+).

Adding k₃=(2,-1,1) with ε=0.01:
- At the OLD vertex (+,+,*): F ≈ 1.25 + small correction
- At the NEW global-max vertex: F = 0.747 (the max JUMPED!)
- The 3rd mode's self-term ε² and cross-terms create a DIFFERENT vertex
  with much higher |ω|² and lower ratio.

Even at ε=0.01: the vertex jump reduces F by ~40%.

## THE STRUCTURAL REASON

### Sign pattern constraint (3 modes, 3 pairs)

For N=3: the excess is EXCESS = Σ_{(j,k)} 2s_js_k a_ja_k Δ_{jk}.

For ALL three pair-excesses to be positive simultaneously:
sign(Δ₁₂) × sign(Δ₁₃) × sign(Δ₂₃) = +1 (NECESSARY).

If this product is -1: at least one pair has NEGATIVE excess at the
global-max vertex → cancellation → F < 5/4.

### The pair-excess sign

Δ_{jk} = -sin²α_{jk} sinβ_{jk} sinγ_{jk} where α is the k-vector angle
and β, γ are polarization cross-angles.

The sign of Δ depends on the geometry of ALL modes simultaneously (through
the sign pattern that maximizes |ω|²). The three excess signs are NOT
independent — they're linked by the shared sign pattern (s₁,s₂,s₃).

### Dilution effect

Even when all pair-excesses are positive:

For N=2: EXCESS/|ω|² = 2a₁a₂Δ₁₂/(a₁²+a₂²+2a₁a₂D₁₂).
Maximum at a₁=a₂, D₁₂→0: 2Δ₁₂/2 = Δ₁₂ ≤ 1/4. Ratio = 5/4. ✓

For N=3 (all equal amps): EXCESS/|ω|² = 2(Δ₁₂+Δ₁₃+Δ₂₃)/(3+2(D₁₂+D₁₃+D₂₃)).
|ω|² ≥ 3 (from vertex average argument). Total excess ≤ 3×1/2 = 3/2.
Ratio ≤ 1 + (3/2)/3 = 3/2 = 1.5. Already < 13/8 = 1.625 ✓ but > 5/4 = 1.25.

BUT: the true ratio is ~1.21 because:
(a) Not all Δ achieve their max simultaneously
(b) The optimal |ω|² is > 3 when D's are positive (global max favors constructive D's)
(c) The sign pattern for max |ω|² doesn't align with max excess

## THE PROOF STRATEGY

Instead of proving F ≤ 5/4 for N ≥ 3, prove the WEAKER (but sufficient)
bound F < 13/8 = 1.625.

From file 371_N4_closure: for N ≤ 4, this is PROVEN via:
- N ≤ 3: per-mode bound gives S²ê ≤ |ω|²/2 (file 363)
- N = 4: per-mode + H_ωω > 0 (file 363)

For N ≥ 5: need either
(a) Prove F = |∇u|²/|ω|² < 13/8 (trace-free approach)
(b) Prove S²ê < 3|ω|²/4 directly

For (a): the per-pair excess Δ_{jk} ≤ 1/4. With N modes:
Total excess ≤ N(N-1)/2 × 2 × (max a_ja_k) × 1/4.

At the global max: |ω|² ≥ μ_N (min-max over N unit vectors).

F ≤ 1 + [N(N-1)/2 × 1/2] / μ_N = 1 + N(N-1)/(4μ_N).

From file 371: μ_N grows at least linearly with N (for random vectors: μ_N ~ N).
The excess grows as N², but the amplitude per mode is 1/N (normalized), so
the actual excess per pair is ~ 1/N². Total excess ~ N² × 1/N² ~ 1. Constant!

So F → 1 as N → ∞. The worst case is at small N.

For fixed amplitudes (not normalized): N(N-1)/(4μ_N).
μ_N for the regular simplex: μ_N ~ 4N/3 (from the tetrahedron pattern).
F ≤ 1 + N(N-1)/(4×4N/3) = 1 + 3(N-1)/16.

For N=5: F ≤ 1 + 12/16 = 1.75. Just above 13/8 = 1.625. Doesn't close!

Better bound on μ_N is needed. Or: use the fact that not all pairs achieve
max excess simultaneously.

## CURRENT STATE

The proof for N ≤ 4 is COMPLETE (via file 363 + H_ωω).

For N ≥ 5: the 5/4 bound holds numerically (50K trials, worst = 1.236 for N=2).
The vertex jump mechanism explains WHY it holds: adding modes shifts the
global max to a vertex with more constructive |ω|² and less excess.

Closing N ≥ 5 formally requires either:
1. A sharper bound on Σ|Δ_{jk}| accounting for geometric constraints
2. A proof that the global-max vertex has bounded excess/|ω|² ratio
3. A completely different approach (e.g., L² methods, pressure structure)

## 374. Vertex jump = the mechanism. 2-mode is extremal because 1 pair can't be
## diluted. 3+ modes: global max jumps to high-|ω|² vertex with low excess/|ω|².
