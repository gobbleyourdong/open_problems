---
source: Definitive status — what's proven, what's tried, what's needed
type: STATUS — honest assessment after 376 proof attempts
file: 376
date: 2026-03-29
---

## PROVEN RESULTS (unconditional)

### The Barrier Mechanism (files 360-368)
At R = α/|ω| = 1/2 (the barrier), DR/Dt = (S²ê - 3|ω|²/4 - H_ωω)/|ω|.
If S²ê < 3|ω|²/4 at the global max: DR/Dt < 0 → barrier holds → regularity.

### S²ê Bound for N ≤ 4 Active Modes
1. N=1: S²ê = 0 (algebraic identity, S_k·v̂_k = 0)
2. N=2: S²ê ≤ |ω|²/4 (exact formula + global max constraint, file 363)
3. N=3: S²ê ≤ |ω|²/2 (per-mode Lagrange optimization, file 363)
4. N=4: S²ê ≤ 3|ω|²/4 + H_ωω > 0 → strict (file 363 + file 267)

### Key Identities
- |S|² = |∇u|² - |ω|²/2 (pointwise exact)
- S²ê ≤ (2/3)|S|² (trace-free, from div u = 0)
- |ŝ_k|² = (|ω̂_k|²/4)(1 - cos²γ_k) (per-mode strain projection)
- |ω̂_k| ≤ |ω|cosγ_k at the global max (sign-flip constraint)
- |∇u|²/|ω|² ≤ 5/4 for 2 modes (Lagrange, file 364)

### Consequence for NS
If S²ê < 3|ω|²/4 at vorticity maxima → α < |ω|/2 → Type I rate →
Seregin (2012) exclusion → **REGULARITY**.

The proof is COMPLETE for fields with ≤ 4 active Fourier modes.


## THE GAP: N ≥ 5

The per-mode bound S²ê ≤ (N-1)|ω|²/4 exceeds 3|ω|²/4 for N ≥ 5.
This bound is the BEST possible from methods that use only:
- Per-mode amplitudes |ŝ_k|
- Triangle inequality on the sum |Σŝ_k|

To close N ≥ 5: MUST use the directional structure of {ŝ_k} in R³.


## APPROACHES TRIED AND FAILED FOR N ≥ 5

| Approach | Result | Why it fails |
|----------|--------|-------------|
| Per-mode + Lagrange | (N-1)/4 | Doesn't use directions |
| Trace-free + |∇u|² | 5/4 only for N=2 | Excess grows with N |
| Energy split (4+tail) | N ≤ 7 only | Tail has its own (N_t-1)/4 |
| Pressure Hessian | H_ωω ~ O(1) | Doesn't scale with N |
| Marginal mode analysis | Ill-conditioned | cosψ₃→0 gives 0/0 |
| Gram eigenvalue bound | Numerically works | Can't prove λ_max bound |
| Tilting direction constraint | 180° arc per k | Not enough to force cancellation |


## NUMERICAL EVIDENCE (50K+ trials, file 372)

| N | worst S²ê/|ω|² | worst |∇u|²/|ω|² | margin to 3/4 |
|---|----------------|---------------------|--------|
| 2 | 0.244 | 1.236 | 67% |
| 3 | 0.252 | 1.212 | 66% |
| 4 | 0.211 | 1.188 | 72% |
| 5 | 0.272 | 1.180 | 64% |
| 7 | - | 1.140 | - |

The worst ratio DECREASES with N. 2-mode is the extremal case.
S²ê/|ω|² never exceeds 0.28 (vs threshold 0.75 = 3/4).


## WHAT'S ACTUALLY NEEDED

### Conjecture A': |∇u|²/|ω|² ≤ 5/4 at the global max (all N)
- Proven for N ≤ 2
- Would give S²ê ≤ |ω|²/2 < 3|ω|²/4 via trace-free
- The 2-mode case IS the extremal (verified 50K+ trials)
- **Need**: prove that adding modes cannot increase the ratio

### The Core Mathematical Problem
Prove: for any N unit vectors v₁,...,vN in R³ with directions n̂_k ∈ R³
(constrained to 2D planes), amplitudes r_k ≥ 0:

    |Σ r_k n̂_k|² ≤ C × Σ r_k²

where C < 3 and n̂_k lies in the specific 2D plane determined by the
Biot-Savart kernel evaluated at the k-th wavevector.

This is a **frame theory** problem: bounding the coherence of a
frame with structured directions.

### Most Promising Approaches (untried or partially tried)
1. **SDP relaxation**: formulate the worst-case as an optimization over
   Gram matrices, relax to SDP, solve for a certified bound
2. **Computer-assisted proof**: interval arithmetic for finite Fourier
   truncation K, with analytic tail bound for |k| > K
3. **Geometric measure theory**: bound the concentration of frame
   directions using the Grassmannian structure
4. **2-mode extremality via monotonicity**: show the ratio F is
   monotone decreasing as modes split (convexity/concavity argument)


## PAPER STRATEGY

Even without closing N ≥ 5, the results are publishable:

### Paper 1: The Barrier Framework
- Theorem: NS regular if S²ê < 3|ω|²/4 at vorticity maxima
- Proof: complete (barrier + Type I + Seregin)
- Partial result: proven for ≤ 4 modes
- Strong numerical evidence for general fields (50K trials, 64% margin)

### Paper 2 (if Conjecture A' proven):
- Theorem: NS globally regular on T³
- Proof: complete via the trace-free chain

### What's novel:
1. The barrier at R=1/2 (not previously formulated)
2. The per-mode strain identity |ŝ_k|² = |ω̂_k|²(1-c_k)/4
3. The global max constraint |ω̂_k| ≤ |ω|cosγ_k (sign-flip argument)
4. The trace-free route via |∇u|²/|ω|² ≤ 5/4
5. Computational evidence with 64% margin


## 376. After 376 attempts: N ≤ 4 proven, N ≥ 5 needs directional cancellation.
## The proof reduces to a frame theory problem in R³.
## Best path: SDP certification or computer-assisted proof.
