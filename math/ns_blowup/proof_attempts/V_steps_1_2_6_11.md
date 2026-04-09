---
source: Instance A VALIDATION — Steps 1, 2, 6, 11 (the solid ones)
type: ADVERSARIAL REVIEW
date: 2026-03-29
---

## Step 1: α > 0 → ê-variation [file 246]

CLAIM: If α > 0 at the max of |ω|, the source Δp is not ê-independent.

PROOF: z-independent + div-free → ∂u_z/∂z = 0 → S_zz = 0 → α = 0.
Contrapositive: α > 0 → NOT z-independent.

REVIEW:
- The argument is in the ê-frame where ê ≈ ẑ. Correct if we choose
  coordinates with z || ω at x*. ✓
- div-free: ∂u_x/∂x + ∂u_y/∂y + ∂u_z/∂z = 0. If z-independent:
  ∂u_z/∂z = 0. ✓ (the 2D divergence ∂u_x/∂x + ∂u_y/∂y = 0 separately)
- S_zz = ∂u_z/∂z = 0. ✓
- α = ê·S·ê = S_zz (in the frame where ê = ẑ). ✓

HIDDEN ASSUMPTION: ê = ẑ exactly at x*. Since ê = ω/|ω| and we
choose z || ω(x*): this is a coordinate choice, not an assumption. ✓

VERDICT: **VALID. Purely algebraic. No gaps.** ✓

---

## Step 2: ê-variation → H_ωω > 0 [file 267]

CLAIM: If Δp has z-variation (non-constant in z) at x*, then H_ωω > 0.

PROOF: Decompose Δp = Σ f_k(x,y) cos(kz) + g_k(x,y) sin(kz).
At x* = (x₀,y₀,0) (WLOG): sin(0) = 0, so only cos terms at z=0.
For each k ≥ 1: p_k satisfies (Δ_xy - k²)p_k = f_k.
Operator (Δ_xy - k²) has all eigenvalues ≤ -k² < 0 on T².
So (Δ_xy - k²)⁻¹ maps positive functions to negative functions.
If f_k(x₀,y₀) > 0: p_k(x₀,y₀) < 0.
H_zz contribution from mode k: -k²p_k(x₀,y₀) > 0.

REVIEW:
- The Fourier decomposition in z: standard on T. ✓
- The evaluation at z=0: WLOG by translation. But what if x* is NOT
  at z=0? We translate z so x* is at z=0. Then cos(k×0) = 1. ✓
- The operator (Δ_xy - k²) on T²: its spectrum is {-|m|² - k² : m ∈ Z²}.
  For k ≥ 1: all eigenvalues ≤ -1 < 0. NEGATIVE DEFINITE. ✓
- Negative definite → inverse maps positive to negative: standard
  spectral theory (expand f_k in eigenbasis, each coefficient divided
  by negative eigenvalue). ✓
- f_k(x₀,y₀) > 0 → p_k(x₀,y₀) < 0: follows if (-L)⁻¹ preserves
  the POINTWISE sign. But (-L)⁻¹ preserves POSITIVITY as a function
  (if f > 0 everywhere → p < 0 everywhere), not pointwise from a
  single point. ✓ (since the Green's function of a negative definite
  operator is negative: G(x,y) < 0 for all x,y. Then p = ∫G f dy < 0
  when f > 0 everywhere.)

HIDDEN ASSUMPTION: f_k > 0 EVERYWHERE on T² (not just at (x₀,y₀))!

The proof says "if f_k(x₀,y₀) > 0" but the Green's function argument
needs f_k ≥ 0 on all of T² (or at least the net integral against G
is negative at (x₀,y₀)).

IS f_k ≥ 0 EVERYWHERE? Not necessarily! The z-cosine mode of Δp at
a specific k could be positive at (x₀,y₀) but negative elsewhere.

If f_k changes sign: p_k(x₀,y₀) = ∫G(x₀,y₀; x',y') f_k(x',y') dx'dy'
could be positive or negative depending on where f_k is positive/negative
and the Green's function weights.

**PROBLEM**: The Fourier lemma as stated needs f_k > 0 everywhere,
not just at the max point. The proof in file 267 seems to assume
f_k > 0 follows from Δp peaking at x*. But f_k is the k-th
z-Fourier mode OVER THE ENTIRE xy-plane, not just near x*.

ACTUALLY: Let me re-read. The source Δp(x,y,z) near x* has a max
at z=0. Its z-Fourier decomposition: f_k(x,y) = (1/π)∫Δp cos(kz) dz.
At (x₀,y₀): f_k(x₀,y₀) = (1/π)∫Δp(x₀,y₀,z) cos(kz) dz.

For Δp peaking at z=0 along the line (x₀,y₀,·):
Δp(x₀,y₀,z) has its max at z=0. The cos(kz) integral picks up
the k-th Fourier coefficient of this 1D function.

A function with max at z=0 has f_k > 0 for small k (the first
Fourier modes are positive for a peaked function). But for LARGE k:
f_k could be negative (depending on the profile shape).

So: the claim H_ωω > 0 requires ALL k-modes to contribute positively.
If some f_k(x₀,y₀) < 0: those modes give H_zz < 0 contributions
that could overwhelm the positive ones.

**SEVERITY: MODERATE.** The Fourier lemma holds for EACH k where
f_k(x₀,y₀) > 0, but modes with f_k < 0 work against it. The NET
H_ωω depends on which modes dominate.

For a STRONGLY peaked Δp (concentration): most energy is in low k
(where f_k > 0). High-k modes with f_k < 0 have small amplitude.
So the NET H_ωω > 0 for concentrated sources. But this is a
QUANTITATIVE claim, not just qualitative.

VERDICT: **Step 2 is QUALITATIVELY correct but has a hidden
quantitative assumption: the positive f_k modes dominate.** ⚠️

---

## Step 6: -S² is diagonal in eigenbasis [file 286]

CLAIM: In the strain eigenbasis, -S² = -diag(λ₁², λ₂², λ₃²).
The off-diagonal components are zero. So -S² doesn't rotate eigenvectors.

REVIEW: S in its own eigenbasis is diag(λ₁, λ₂, λ₃). S² is then
diag(λ₁², λ₂², λ₃²). Off-diagonals: (S²)_ij = Σ_k S_ik S_kj.
In the eigenbasis: S_ik = λ_i δ_ik. So (S²)_ij = λ_i² δ_ij. ✓

The eigenvector rotation from -S² in the strain equation DS/Dt = -S² - Ω² - H:
the -S² term only changes EIGENVALUES (the diagonal), not EIGENVECTORS.

HIDDEN ASSUMPTION: None. This is pure linear algebra.

VERDICT: **VALID. Algebraic identity. No gaps.** ✓

---

## Step 11: α bounded → BKM → regularity [file 287]

CLAIM: Q < 0 → Dα/Dt < -α² → α ≤ α₀/(1+α₀t) → ||ω||∞ linear → BKM finite.

REVIEW:
- Q < 0 → Dα/Dt = Q - α² < -α². ✓ (definition of Q = Dα/Dt + α²)
- Dα/Dt ≤ -α² → by comparison: α(t) ≤ α₀/(1+α₀t). ✓ (standard Riccati)
- ||ω||∞(t) = ||ω||₀ exp(∫₀ᵗ α ds) ≤ ||ω||₀ exp(∫₀ᵗ α₀/(1+α₀s) ds)
  = ||ω||₀ × (1+α₀t). LINEAR growth. ✓
- ∫₀ᵀ ||ω||∞ dt ≤ ||ω||₀ ∫₀ᵀ (1+α₀t) dt < ∞. BKM holds. ✓

HIDDEN ASSUMPTION: The Q < 0 condition applies at the EULERIAN max
of |ω|, but Dα/Dt is a LAGRANGIAN (material) derivative. The max
point MOVES. The Riccati comparison applies to a MATERIAL particle,
but the max switches between particles.

HOWEVER: at the max, d||ω||∞/dt = α*||ω||∞ (exact, from the max
principle for parabolic equations... actually this is for the EULER
equation where ∂|ω|²/∂t + u·∇|ω|² = 2|ω|²α at the max, and
u·∇|ω|² = 0 at the max by the gradient condition). So:
d||ω||∞/dt = α*||ω||∞ exactly, no Lagrangian correction needed. ✓

WAIT: This is for SMOOTH solutions where the max is achieved at
a non-degenerate point. For degenerate maxima (achieved on a set):
more care is needed. But for smooth solutions on T³: the max is
generically non-degenerate.

VERDICT: **VALID for smooth solutions.** ✓
