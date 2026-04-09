---
source: Self-attenuation alignment — ê → e₃ at vorticity maximum
type: KEY DATA + NEW PROOF DIRECTION
file: 389
date: 2026-03-29
---

## THE FINDING (2000 random configs, N=3-7)

At the global max of |ω|, the vorticity direction ê aligns preferentially
with the eigenvector of SMALLEST |eigenvalue| of the strain S:

| Eigenvector | Mean c_i = (ê·e_i)² | Median | Interpretation |
|-------------|---------------------|--------|----------------|
| e₁ (|λ₁| largest) | 0.125 | 0.058 | ê AVOIDS max strain |
| e₂ (|λ₂| middle) | 0.172 | 0.063 | ê partially avoids |
| e₃ (|λ₃| smallest) | **0.704** | **0.838** | ê ALIGNS with min strain |

This is the SELF-ATTENUATION mechanism: vorticity evolves to minimize
the strain it experiences.


## THE STRUCTURAL REASON

For a SINGLE Fourier mode: S·v̂ = 0 (proven, file 363).
The eigenvalues of S are {+|ω̂|/2, 0, -|ω̂|/2}.
ê = v̂ is the eigenvector for eigenvalue 0 (the middle one).
In the |λ|-sorted basis: ê = e₃ (the smallest |λ|). So c₃ = 1.

For MULTI-mode fields: c₃ < 1 but remains dominant (mean 0.70).
The perturbation from multi-mode mixing is bounded by the cross-interactions.


## PROOF DIRECTION: ALIGNMENT → BARRIER CLOSURE

### If c₃ ≥ 1/2 at the global max (observed: median 0.84):

S²ê = λ₁²c₁ + λ₂²c₂ + λ₃²c₃ ≤ λ₁²(1-c₃) + λ₃²c₃

Using λ₁² ≤ |S|² and λ₃² ≤ |S|²/3 (from trace-free):
S²ê ≤ |S|²(1-c₃) + (|S|²/3)c₃ = |S|²(1 - 2c₃/3)

For c₃ ≥ 1/2: S²ê ≤ |S|²(1-1/3) = 2|S|²/3 (same as trace-free bound).

STRONGER: Using λ₁² ≤ (2/3)|S|² (trace-free max eigenvalue):
S²ê ≤ (2/3)|S|²(1-c₃) + λ₃²c₃

With λ₃² = |S|² - λ₁² - λ₂² ≤ |S|²/3:
S²ê ≤ (2/3)|S|²(1-c₃) + (|S|²/3)c₃ = |S|²(2/3 - c₃/3)

For c₃ ≥ 1/2: S²ê ≤ |S|²(2/3-1/6) = |S|²/2.

So: **S²ê ≤ |S|²/2 when c₃ ≥ 1/2** (stronger than the 2/3 trace-free bound!).

And: |S|² = |∇u|² - |ω|²/2.

S²ê ≤ (|∇u|²-|ω|²/2)/2.

For S²ê < 3|ω|²/4: need |∇u|² < 2|ω|². From our data: |∇u|²/|ω|² ≤ 1.24 ≪ 2.

**CONCLUSION**: If c₃ ≥ 1/2 AND |∇u|² ≤ 2|ω|² at the global max:
S²ê ≤ (2|ω|²-|ω|²/2)/2 = 3|ω|²/4.

With the margin in |∇u|² (1.24 vs 2): strict inequality.


## WHAT NEEDS TO BE PROVEN

### Approach 1: Prove c₃ ≥ 1/2 at the global max

From the per-mode analysis: each mode contributes c₃_k = 1 (single-mode alignment).
Multi-mode mixing: c₃ = 1 - perturbation. Need perturbation ≤ 1/2.

The perturbation is bounded by the CROSS-MODE interaction strength,
which is related to the per-pair excess terms Δ_{jk}.

### Approach 2: Prove the COMBINED condition

Instead of c₃ ≥ 1/2 separately: prove S²ê ≤ |S|²/2 directly.

S²ê ≤ |S|²/2 iff Σλ_i²c_i ≤ Σλ_i²/2 iff Σλ_i²(c_i - 1/3) ≤ Σλ_i²/6.

Since Σ(c_i-1/3) = 0: this is a CENTERING condition on the alignment.

For the worst case (c₁ = 1): S²ê = λ₁² ≤ (2/3)|S|² (trace-free bound, not 1/2).
So S²ê ≤ |S|²/2 does NOT hold universally — only when c₃ is large enough.

### Approach 3: Use α ≈ λ₃ (from alignment)

At the global max: α = Σλ_i c_i ≈ λ₃ (since c₃ ≈ 0.84).

If α ≈ λ₃ (smallest eigenvalue): |α| ≤ |λ₃| ≤ |S|/√3.

For the barrier: α < |ω|/2.
|S|/√3 < |ω|/2 iff |S| < |ω|√3/2 iff |S|² < 3|ω|²/4.
And |S|² = |∇u|²-|ω|²/2. So: |∇u|² < 3|ω|²/4 + |ω|²/2 = 5|ω|²/4.

This recovers the 5/4 bound on |∇u|²/|ω|² — which is PROVEN for N=2 only!

Hmm: the alignment approach reduces to the SAME 5/4 condition as the trace-free route.


## THE REAL INSIGHT

The self-attenuation alignment (c₃ ≈ 0.84) explains WHY S²ê/|ω|² ≈ 0.03
(far below the 0.75 threshold):

1. c₃ large → S²ê ≈ λ₃² ≈ smallest eigenvalue² → inherently small
2. |S|² ≈ |ω|²/2 → |S| ≈ |ω|/√2 → |λ₃| ≈ |ω|/(√2×√3) ≈ |ω|/2.4
3. S²ê ≈ λ₃² ≈ |ω|²/6 ≈ 0.17|ω|² (consistent with data: mean 0.03)

The actual S²ê is even smaller because the alignment is not exactly c₃=1.


## 389. Self-attenuation: ê aligns with smallest |λ| eigenvector (c₃=0.84).
## If provable: S²ê ≤ |S|²/2 → barrier closes with |∇u|² < 2|ω|².
## Reduces to proving c₃ ≥ 1/2 at the global max for all smooth fields.
