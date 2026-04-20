# Attempt 851 — N=4 Coherence Derivation from the First-Order Vorticity-Max Constraint

**Date**: 2026-04-19
**Phase**: 4 (Frobenius ratio, narrowing to N=4)
**Track**: theory
**Author**: sub-instance of Opus 4.7 (1M ctx), sigma v9.1 frontier push

---

## The target inequality

At the vorticity maximum x* ∈ T³ expand the vorticity and strain in the
divergence-free Fourier basis,

  ω(x*) = Σⱼ cⱼ vⱼ,   |vⱼ| = |kⱼ| = 1, vⱼ ⊥ kⱼ
  S(x*) = Σⱼ cⱼ Sⱼ,   Sⱼ := −(1/(2|kⱼ|²))(kⱼ ⊗ wⱼ + wⱼ ⊗ kⱼ), wⱼ = kⱼ × vⱼ

with cⱼ = cos(kⱼ·x*), sⱼ = sin(kⱼ·x*).

Introduce the symmetric scalar arrays

  τⱼₖ := Tr(Sⱼ Sₖ),   μⱼₖ := vⱼ · vₖ

(Both τⱼⱼ = 1/2 and μⱼⱼ = 1 by the diagonal identities in
`StrainTraceInnerProduct.lean`.) The Key Lemma Frobenius ratio target
‖S‖²_F/|ω|² < 9/8 expands (attempt 849 §2026-04-15 audit) to

  **(TARGET)**   off_F − (9/8)·off_ω < (5/8) · Σⱼ cⱼ²

where

  off_F := Σ_{j≠k} cⱼ cₖ τⱼₖ,   off_ω := Σ_{j≠k} cⱼ cₖ μⱼₖ.

The vorticity-maximum condition ∇|ω(x*)|² = 0 gives

  **(CONSTRAINT)**   Σⱼ sⱼ (ω · vⱼ) kⱼ = 0   in R³

(three scalar equations), with ω·vⱼ = cⱼ + Σ_{k≠j} cₖ μⱼₖ.

At N ≤ 3 the Key Lemma is already proven in Lean
(`lean/KeyLemmaN2.lean`, `lean/KeyLemmaN3.lean`) and the Frobenius route
is closed at N=3 with margin ~1.26× (attempt_850). The present file
attacks N=4 — the smallest *unclosed* case.

---

## N=4 configuration chosen

I pick the "axis + body-diagonal" quartet:

  k₁ = ê₁,  k₂ = ê₂,  k₃ = ê₃,  k₄ = (1, 1, 1)/√3.

Reason for this choice:

- The first three modes have *orthogonal* wavevectors and pairwise
  τ_{ij} = μ_{ij} = 0 (shown below). So off_F and off_ω collapse to
  cross-terms with k₄ only. This isolates the "new" N=4 physics against
  a clean N=3 base.
- k₄ has nonzero coherence with all of k₁, k₂, k₃ (kᵢ·k₄ = 1/√3). This
  is maximally symmetric under permutation of axes, so the three
  cross-terms k₁k₄, k₂k₄, k₃k₄ contribute in a balanced way.
- x* = (x₁, x₂, x₃) parametrizes cⱼ: c₁ = cos x₁, c₂ = cos x₂,
  c₃ = cos x₃, c₄ = cos((x₁+x₂+x₃)/√3). The fourth phase is *linked* to
  the first three through the irrational number √3; this matters for
  realizability checks.

Fix polarizations:

  v₁ := ê₂,   w₁ = k₁×v₁ = ê₃
  v₂ := ê₃,   w₂ = ê₁
  v₃ := ê₁,   w₃ = ê₂
  v₄ := (1,−1,0)/√2, w₄ = k₄×v₄ = (1,1,−2)/√6.

(v₄ is the unit circular polarization obtained by rotating the unit
dyadic pair (1,−1,0)/√2, (1,1,−2)/√6 in the k₄-plane. Any other v₄
differs by a global rotation in the plane ⊥ k₄ and gives an equivalent
worst-case analysis.)

In matrix form,

  S₁ = −½[[0,0,1],[0,0,0],[1,0,0]],
  S₂ = −½[[0,1,0],[1,0,0],[0,0,0]],
  S₃ = −½[[0,0,0],[0,0,1],[0,1,0]],
  S₄ = −(1/(2√18))·[[2,2,−1],[2,2,−1],[−1,−1,−4]].

**Verify Tr(S_j²)=1/2 for S₄** (diagonal identity, required by
`StrainTraceInnerProduct.lean`): ‖[[2,2,−1],[2,2,−1],[−1,−1,−4]]‖²_F
= 4+4+1+4+4+1+1+1+16 = 36, so Tr(S₄²) = 36/(4·18) = 1/2. ✓

---

## The algebra

### (i) Tabulate the τ's and μ's

By direct Hadamard-product computation (matrix dot product) on the
matrices above:

  τ₁₂ = Tr(S₁ S₂) = 0
  τ₁₃ = Tr(S₁ S₃) = 0
  τ₂₃ = Tr(S₂ S₃) = 0
  τ₁₄ = Tr(S₁ S₄) = (−½)·(1/√18)·(+1) + (−½)·(1/√18)·(+1)
                   = −1/√18 · ½ − 1/√18 · ½ = ... actually recompute

Careful: (S₁)₁₃ = (S₁)₃₁ = −½; all others of S₁ are 0. (S₄)₁₃ = (S₄)₃₁ = +1/(2√18) (from M₁₃ = −1 and the overall sign −1/(2√18)·(−1)).

  τ₁₄ = 2·(−½)·(+1/(2√18)) = −1/(2√18) = −1/(6√2).

Similarly:
  (S₂) off-diagonal (1,2),(2,1) = −½; (S₄)₁₂ = (S₄)₂₁ = −1/(2√18)·(+2)
  = −1/√18. Hence τ₂₄ = 2·(−½)·(−1/√18) = 1/√18 = 1/(3√2) = 2/(6√2).

  (S₃) off-diagonal (2,3),(3,2) = −½; (S₄)₂₃ = (S₄)₃₂ = +1/(2√18).
  Hence τ₃₄ = 2·(−½)·(+1/(2√18)) = −1/(2√18) = −1/(6√2).

For the μ's:
  μ₁₂ = ê₂·ê₃ = 0,  μ₁₃ = ê₂·ê₁ = 0,  μ₂₃ = ê₃·ê₁ = 0,
  μ₁₄ = ê₂·(1,−1,0)/√2 = −1/√2,
  μ₂₄ = ê₃·(1,−1,0)/√2 = 0,
  μ₃₄ = ê₁·(1,−1,0)/√2 = +1/√2.

Prior art used: the Hilbert-Schmidt formula Tr(SⱼSₖ) =
(1/(2|kⱼ|²|kₖ|²))·[(kⱼ·kₖ)(wⱼ·wₖ) + (kⱼ·wₖ)(wⱼ·kₖ)] proven in
`strain_hilbert_schmidt_formula` (StrainTraceInnerProduct.lean). I
computed it component-wise to double-check: both routes agree.

### (ii) Expand off_F and off_ω in these c's

  off_F = 2(c₁c₂τ₁₂ + c₁c₃τ₁₃ + c₂c₃τ₂₃ + c₁c₄τ₁₄ + c₂c₄τ₂₄ + c₃c₄τ₃₄)
        = 2·c₄·(c₁·(−1/(6√2)) + c₂·(2/(6√2)) + c₃·(−1/(6√2)))
        = (c₄/(3√2))·(−c₁ + 2c₂ − c₃)                                 (A)

  off_ω = 2(c₁c₄μ₁₄ + c₂c₄μ₂₄ + c₃c₄μ₃₄)
        = 2·c₄·(−c₁/√2 + 0 + c₃/√2)
        = √2·c₄·(c₃ − c₁)                                             (B)

### (iii) The target inequality, explicit

LHS of (TARGET):

  off_F − (9/8)·off_ω
    = (c₄/(3√2))·(−c₁+2c₂−c₃) − (9/8)·√2·c₄·(c₃−c₁)
    = c₄·[ (−c₁+2c₂−c₃)/(3√2) + (9√2/8)·(c₁−c₃) ]
    = (√2·c₄/24)·[ (−4c₁ + 8c₂ − 4c₃) + (27c₁ − 27c₃) ]       (rescale by √2·24)
    = (√2·c₄/24)·(23c₁ + 8c₂ − 31c₃)                                  (C)

So (TARGET) reads

  **(C')**   (√2/24)·c₄·(23c₁ + 8c₂ − 31c₃)  <  (5/8)·(c₁² + c₂² + c₃² + c₄²).

### (iv) Unconditional worst case — shows the constraint is needed

Without any constraint on (c₁,…,c₄), maximize the LHS of (C') subject
only to ‖c‖² = c₁²+c₂²+c₃²+c₄² = 1. Set L := 23c₁ + 8c₂ − 31c₃. By
Cauchy–Schwarz, |L| ≤ ‖(23,8,−31)‖ · √(c₁²+c₂²+c₃²) = √1554 ·
√(c₁²+c₂²+c₃²). Writing r² := c₁²+c₂²+c₃², the bound LHS ≤
(√2/24)·√1554·|c₄|·r is maximized at r² = c₄² = ½, giving

  LHS_max = (√2·√1554)/(24·2) = √3108/48 ≈ 1.16.

But RHS of (C') at ‖c‖²=1 is 5/8 = 0.625. So the unconditional LHS can
reach **1.86×** the RHS — the inequality (TARGET) is *false* as a pure
algebraic statement without the vorticity-max CONSTRAINT.

**Conclusion.** Any proof of (C') must use the CONSTRAINT
non-trivially. This is the sigma v9.1 "falsifier line" at the
unconditional level: a bare Bessel / coherence argument cannot suffice;
the first-order condition on sⱼ is load-bearing.

### (v) The CONSTRAINT, written out

Recall ω·vⱼ = cⱼ + Σ_{k≠j} cₖμⱼₖ. With the μ's above:

  ω·v₁ = c₁ + c₄·μ₁₄ = c₁ − c₄/√2
  ω·v₂ = c₂ + c₄·μ₂₄ = c₂
  ω·v₃ = c₃ + c₄·μ₃₄ = c₃ + c₄/√2
  ω·v₄ = c₁μ₁₄ + c₃μ₃₄ + c₄ = c₄ + (c₃ − c₁)/√2

The CONSTRAINT Σⱼ sⱼ(ω·vⱼ)kⱼ = 0 has three components (m = 1, 2, 3).
With our k's, component m = 1 collects the kⱼ with k_{j,1} ≠ 0:
that's k₁ (with k_{1,1}=1) and k₄ (with k_{4,1}=1/√3). So

  Comp m=1:  s₁(ω·v₁) + (1/√3)·s₄(ω·v₄) = 0
  Comp m=2:  s₂(ω·v₂) + (1/√3)·s₄(ω·v₄) = 0
  Comp m=3:  s₃(ω·v₃) + (1/√3)·s₄(ω·v₄) = 0

Set λ := −s₄(ω·v₄)/√3. Then

  s₁ · (ω·v₁) = s₂ · (ω·v₂) = s₃ · (ω·v₃) = λ.                       (*)

This is **three scalar equations** that tie the three angles x₁,x₂,x₃
to x₄ = (x₁+x₂+x₃)/√3.

### (vi) Eliminating s via sⱼ² = 1 − cⱼ²

Given the cⱼ's, (*) plus s₁² + c₁² = 1 gives

  s₁² = (1 − c₁²),  s₁² · (ω·v₁)² = λ²
  ⇒  (1 − c₁²)·(c₁ − c₄/√2)²  ≥  λ²    (equality only at c₁² = 1 or s₁=0)

and similarly for j = 2, 3. And for j = 4, s₄² = 1 − c₄² with
s₄·(ω·v₄) = −√3·λ gives

  (1 − c₄²)·(c₄ + (c₃−c₁)/√2)²  ≥  3λ².

Combining, at a vorticity maximum the *single* scalar λ is constrained
by **four** inequalities. Eliminating λ:

  **(D)**  min_{j∈{1,2,3}} (1−cⱼ²)·(ω·vⱼ)²  ≥  (1/3)·(1−c₄²)·(ω·v₄)².

(And each LHS bound is simultaneously the same λ², so they must all
equal one another at the critical point: i.e., at the vorticity max,

  (1−c₁²)·(c₁−c₄/√2)² = (1−c₂²)·c₂² = (1−c₃²)·(c₃+c₄/√2)²
                       = (1/3)·(1−c₄²)·(c₄+(c₃−c₁)/√2)²       .)     (E)

### (vii) Using (E) to bound the LHS of (C')

The LHS of (C') has a linear piece in (c₁, c₂, c₃) weighted by c₄:

  LHS(c₁,c₂,c₃,c₄) = (√2·c₄/24)·(23c₁ + 8c₂ − 31c₃).

Key structural observation: the coefficient vector (23, 8, −31) is
**NOT** proportional to any gradient of the μ's — it's (−1, 2, −1)
(from off_F) plus (27, 0, −27) (from −(9/8)·off_ω), so the "off_F"
direction is (−1, 2, −1) and the "off_ω" direction is (1, 0, −1).

Now (E) has a *symmetry*: the relations for j = 1, 3 are symmetric
under (c₁, c₃) ↔ (−c₃, −c₁) together with c₄ ↔ c₄. Under this
symmetry c₃ − c₁ is anti-symmetric; so off_ω (∝ c₃ − c₁) is
anti-symmetric; and the linear piece (23c₁ − 31c₃) is **NOT**
anti-symmetric, so the symmetric-antisymmetric decomposition
doesn't kill cross-terms cleanly.

However the **μ₂₄ = 0** fact means c₂ does NOT appear in ω·v₂
through c₄-coupling (ω·v₂ = c₂ only). So (E) for j = 2 gives an
*algebraically elementary* relation:

  (1 − c₂²)·c₂² = (1/3)·(1 − c₄²)·(c₄ + (c₃ − c₁)/√2)²           (E₂)

and the LHS of (E₂) is uniformly bounded: (1−c₂²)·c₂² ≤ 1/4 for all
c₂ ∈ [−1, 1] (maximum at c₂² = 1/2).

Therefore

  (1/3)·(1−c₄²)·(c₄ + (c₃−c₁)/√2)² ≤ 1/4
  ⇒ (1−c₄²)·(c₄ + (c₃−c₁)/√2)² ≤ 3/4                                 (F)

This is a hard geometric bound at the vorticity max, coming purely from
the c₂-arm of the CONSTRAINT.

Similarly apply (E₁) and (E₃):
  (1−c₁²)·(c₁ − c₄/√2)² = (1−c₂²)·c₂² ≤ 1/4                          (F₁)
  (1−c₃²)·(c₃ + c₄/√2)² = (1−c₂²)·c₂² ≤ 1/4                          (F₃)

### (viii) Reducing (C') to a concrete scalar inequality

Define a := c₁ − c₄/√2 and b := c₃ + c₄/√2 (the "tilted" coordinates
along ω·v₁ and ω·v₃ axes). Then

  c₁ = a + c₄/√2,  c₃ = b − c₄/√2,  c₃ − c₁ = b − a − √2·c₄.

And LHS of (C') becomes

  (√2·c₄/24)·[23(a + c₄/√2) + 8c₂ − 31(b − c₄/√2)]
    = (√2·c₄/24)·[23a + 8c₂ − 31b + 27√2·c₄]
    = (√2·c₄/24)·(23a + 8c₂ − 31b) + (54/24)·c₄²
    = (√2·c₄/24)·(23a + 8c₂ − 31b) + (9/4)·c₄².                      (G)

RHS of (C'):
  (5/8)(c₁² + c₂² + c₃² + c₄²)
  = (5/8)[(a + c₄/√2)² + c₂² + (b − c₄/√2)² + c₄²]
  = (5/8)[a² + b² + c₂² + c₄² + √2·c₄(a − b) + c₄²]
  = (5/8)[a² + b² + c₂² + 2c₄² + √2·c₄(a − b)]                       (H)

Now (F₁), (F₃), (F) become:

  (1 − (a + c₄/√2)²)·a² ≤ 1/4     (from F₁)                         (F₁')
  (1 − (b − c₄/√2)²)·b² ≤ 1/4     (from F₃)                         (F₃')
  (1 − c₄²)·(c₄ + (b − a − √2·c₄)/√2)² ≤ 3/4
      = (1 − c₄²)·((b − a)/√2)² · (nothing to simplify further)     (F')

Wait, simplify the argument in (F'): c₄ + (b−a−√2·c₄)/√2
  = c₄ + (b−a)/√2 − c₄ = (b−a)/√2.

So (F') simplifies dramatically:
  **(F')   (1 − c₄²)·(b − a)² / 2  ≤  3/4,   i.e., (1 − c₄²)·(b−a)² ≤ 3/2.**

This is a clean inequality in just (a, b, c₄).

### (ix) The reduction: (TARGET) for this N=4 is equivalent to

Using (G), (H), (F₁'), (F₃'), (F'), the target (C') becomes

  **(Q)**  (√2·c₄/24)·(23a + 8c₂ − 31b) + (9/4)c₄²
           <  (5/8)·[a² + b² + c₂² + 2c₄² + √2·c₄(a−b)]

i.e.

  (√2·c₄/24)·(23a + 8c₂ − 31b) − (5√2·c₄/8)·(a − b) + (9/4 − 10/8)c₄²
     <  (5/8)(a² + b² + c₂²)

The c₄² coefficient: 9/4 − 5/4 = 1. So

  **(Q')**  (√2·c₄/24)·(23a + 8c₂ − 31b) − (5√2/8)·c₄·(a − b) + c₄²
            <  (5/8)(a² + b² + c₂²)

Collect the linear-in-(a,b,c₂) piece:
  √2·c₄·[ (23/24)·a + (8/24)·c₂ − (31/24)·b − (5/8)·(a − b) ]
  = √2·c₄·[ (23/24 − 15/24)·a + (1/3)·c₂ + (−31/24 + 15/24)·b ]
  = √2·c₄·[ (8/24)·a + (1/3)·c₂ + (−16/24)·b ]
  = √2·c₄·[ (1/3)·a + (1/3)·c₂ + (−2/3)·b ]
  = (√2/3)·c₄·(a + c₂ − 2b).

So (Q') is:

  **(R)**  (√2/3)·c₄·(a + c₂ − 2b) + c₄²  <  (5/8)(a² + b² + c₂²).

Subject to: (F₁'), (F₃'), (F'), and the scalar interval constraints
|a + c₄/√2| ≤ 1, |b − c₄/√2| ≤ 1, |c₂| ≤ 1, |c₄| ≤ 1 (from
cⱼ ∈ [−1, 1]).

### (x) Quick sanity: worst case of (R) given only |x|≤1 bounds

At the unconstrained max of LHS − RHS, by Cauchy–Schwarz on the (a, c₂,
b) direction (1, 1, −2)/√6:

  (√2/3)·c₄·(a+c₂−2b) ≤ (√2/3)·|c₄|·√6·√(a²+c₂²+b²)
                      = (2√3/3)·|c₄|·√(a²+c₂²+b²)

Set r² := a²+c₂²+b². Then

  LHS ≤ (2√3/3)·|c₄|·r + c₄²,  RHS = (5/8)·r².

Parametrize c₄ = ρ cos θ, r = ρ sin θ with ρ ∈ [0, √2] (from
sum-of-squares bound on an L∞ box):

  LHS − RHS ≤ (2√3/3)·ρ²·cos θ·sin θ + ρ²·cos² θ − (5/8)·ρ²·sin² θ
           = ρ²·[ (√3/3)·sin 2θ + cos² θ − (5/8)·sin² θ ]
           = ρ²·[ (√3/3)·sin 2θ + (1 + cos 2θ)/2 − (5/8)·(1 − cos 2θ)/2 ]
           = ρ²·[ (√3/3)·sin 2θ + (1/2 − 5/16)+ (1/2 + 5/16)·cos 2θ ]
           = ρ²·[ (√3/3)·sin 2θ + 3/16 + (13/16)·cos 2θ ].

Max over θ: amplitude √((√3/3)² + (13/16)²) = √(1/3 + 169/256)
≈ √(0.333 + 0.660) = √0.994 ≈ 0.997. Plus constant 3/16 = 0.1875. So
max bracket ≈ 0.997 + 0.188 = 1.185. With ρ² ≤ 2, max of LHS − RHS ≈
2·1.185 = 2.37 > 0.

So **(R) is NOT unconditionally true on the box** — constraints (F₁'),
(F₃'), (F') are essential.

### (xi) The key simplification from (F')

(F') says (1 − c₄²)(b − a)² ≤ 3/2.

Case analysis on c₄²:
- If c₄² ≥ 1/2: then 1 − c₄² ≤ 1/2, so (b−a)² ≤ 3 unconditionally.
  But more importantly c₄² is bounded below by 1/2, giving a strong
  *positive* RHS contribution via the (c₄² on LHS — wait, c₄² appears
  ON the LHS of (R), not RHS). Actually c₄² contributes *positively*
  to LHS, so large c₄² makes the inequality *harder*.

  In this sub-case, however, the large c₄² also restricts (a, b)
  via (F₁'), (F₃'): (1 − (a + c₄/√2)²)·a² ≤ 1/4 forces either a² small
  or a ± c₄/√2 close to ±1. If c₄ = 1, then c₁ = a + 1/√2 ∈ [−1, 1]
  forces a ∈ [−1 − 1/√2, 1 − 1/√2] and (F₁') reduces to
  (1 − (a + 1/√2)²)·a² ≤ 1/4, achievable only near a = 0 or a = ±(1 − 1/√2).
  That is, c₄ = 1 forces (a, b) into a *small* neighborhood of 0.

- If c₄² < 1/2: then (F') gives (b−a)² < 3/(2·(1−c₄²)) < 3/(2·(1/2)) = 3.
  Combined with |b − a| ≤ 2 (from |a|, |b| ≤ 2 on the extended box),
  (F') effectively bounds (b−a)² by min(4, 3/(1−c₄²)).

This case analysis suggests that (R) ∧ (F₁') ∧ (F₃') ∧ (F') is a
**semialgebraic feasibility problem** in (a, b, c₂, c₄) ∈ R⁴, and the
target (R) is provable by **sum-of-squares certification** on this
compact box. The inequality is polynomial (degree ≤ 4 after
multiplying out the quartic constraints) and the box is compact and
rational, so by Putinar / Lasserre hierarchies the SOS certificate
either exists at some finite degree or a specific violator can be
extracted.

### (xii) Numerical spot-check of (R) under the constraints

Let me check the "(xi) large c₄" corner: c₄ = 1, so (F₁') requires
(1 − (a + 1/√2)²)·a² ≤ 1/4. Try a = 0: then (1 − 1/2)·0 = 0 ≤ 1/4 ✓.
Similarly b = 0 works, and c₂ = 0 works. Then (F') gives
(1 − 1)·(0 − 0)² = 0 ≤ 3/2 ✓. At (a, b, c₂, c₄) = (0, 0, 0, 1):

  LHS of (R) = (√2/3)·1·(0 + 0 − 0) + 1 = 1
  RHS of (R) = (5/8)·0 = 0.

LHS − RHS = 1 > 0. **VIOLATION of (R) at this point.**

Wait — this seems to falsify (TARGET) at N=4. Let me re-examine.

At (a, b, c₂, c₄) = (0, 0, 0, 1): c₁ = 0 + 1/√2 = 1/√2, c₂ = 0,
c₃ = 0 − 1/√2 = −1/√2, c₄ = 1. So Σcⱼ² = ½ + 0 + ½ + 1 = 2.

Let me re-derive LHS and RHS of (C') directly at this c-vector:
  LHS = (√2/24)·1·(23·(1/√2) + 8·0 − 31·(−1/√2))
      = (√2/24)·(23/√2 + 31/√2)
      = (√2/24)·(54/√2)
      = 54/24 = 9/4.

  RHS = (5/8)·2 = 5/4.

LHS > RHS: 9/4 > 5/4 by a margin of 1. **The (TARGET) inequality
FAILS at this point.**

So this cⱼ-configuration, if realizable at a vorticity max, would be a
counterexample.

### (xiii) Is (0, 0, 0, 1) realizable at a vorticity max?

At (a, b, c₂, c₄) = (0, 0, 0, 1): c₁ = 1/√2, c₂ = 0, c₃ = −1/√2, c₄ = 1.

Corresponding x*: x₁ = arccos(1/√2) = π/4 + 2πn or −π/4 + 2πn. Similarly
for x₂, x₃, and x₄ = (x₁+x₂+x₃)/√3.

For c₄ = 1, need (x₁+x₂+x₃)/√3 = 2πm for some integer m.

If x₁ = π/4, x₂ = π/2, x₃ = 3π/4: sum = (π/4 + π/2 + 3π/4) = 3π/2.
Divided by √3: 3π/(2√3) = π√3/2 ≠ 2πm.

Trying x₁ = −π/4, x₂ = ±π/2, x₃ = 3π/4: x₁+x₂+x₃ = −π/4 ± π/2 + 3π/4
= {π, 0}. Divided by √3: {π/√3, 0}. For c₄ = cos(x₄) = 1, need x₄ = 0
mod 2π. So x₁+x₂+x₃ must be 0 mod 2π√3.

Taking x₁+x₂+x₃ = 0: −π/4 + x₂ + 3π/4 = 0 gives x₂ = −π/2, so
c₂ = cos(−π/2) = 0 ✓. With x₁ = −π/4, x₂ = −π/2, x₃ = 3π/4: x₄ = 0.

So the x* = (−π/4, −π/2, 3π/4) *does* realize (c₁, c₂, c₃, c₄) =
(1/√2, 0, −1/√2, 1). Good — so the c-vector is realizable.

**Now check the vorticity-max CONSTRAINT at this x*.**

Compute sⱼ:
  s₁ = sin(−π/4) = −1/√2
  s₂ = sin(−π/2) = −1
  s₃ = sin(3π/4) = +1/√2
  s₄ = sin(0) = 0

And ω·vⱼ:
  ω·v₁ = c₁ − c₄/√2 = 1/√2 − 1/√2 = 0
  ω·v₂ = c₂ = 0
  ω·v₃ = c₃ + c₄/√2 = −1/√2 + 1/√2 = 0
  ω·v₄ = c₄ + (c₃−c₁)/√2 = 1 + (−√2)/√2 = 1 − 1 = 0

The CONSTRAINT Σⱼ sⱼ(ω·vⱼ)kⱼ: every summand is zero because
(ω·vⱼ) = 0 for all j. **The CONSTRAINT is satisfied trivially.**

But then |ω(x*)|² = Σⱼ cⱼ² + off_ω = 2 + 0 − 0 = ... wait.

Actually |ω|² = Σⱼⱼ cⱼ² + 2Σ_{j<k} cⱼcₖ μⱼₖ. Compute:

  |ω|² = c₁² + c₂² + c₃² + c₄² + 2(c₁c₄μ₁₄ + c₃c₄μ₃₄)
       = 2 + 2((1/√2)·1·(−1/√2) + (−1/√2)·1·(1/√2))
       = 2 + 2(−1/2 − 1/2) = 2 − 2 = 0.

**|ω(x*)|² = 0 at this x*.** The point x* is not a vorticity *maximum*
— it's a vorticity *zero*. The trivial satisfaction of the CONSTRAINT
is because ω(x*) = 0: every (ω·vⱼ) vanishes, so the first-order
condition holds vacuously.

We cannot divide by |ω|² = 0. This x* is *not* a valid vorticity max
and (TARGET) does not apply there.

### (xiv) The corrected realizability picture

At a *true* vorticity maximum we must have |ω(x*)|² > 0 AND |ω(x*)|²
is maximized over x ∈ T³. The apparent violator in (xii)–(xiii) lives
at a vorticity zero, not maximum — the first-order condition is met
vacuously (degenerate critical point).

The honest conclusion: **the apparent violation is an artifact of
treating the CONSTRAINT as equality without checking that the point is
a *non-degenerate maximum* (|ω|² > 0 and strictly greater than nearby
values).** Any proof of (C') from the CONSTRAINT needs to
simultaneously impose |ω|² > 0 — i.e., we need to replace the target

  off_F − (9/8)·off_ω  <  (5/8) Σcⱼ²

by the *scale-invariant* equivalent

  (off_F − (9/8)·off_ω) / |ω|²  <  5/8 · (Σcⱼ² / |ω|²).

Since |ω|² = Σcⱼ² + off_ω and we are at |ω|² > 0, the ratio
Σcⱼ² / |ω|² is finite. So the correct target is

  **(C'')**  off_F − (9/8)·off_ω  <  (5/8)·(|ω|² − off_ω)
            = (5/8)·|ω|² − (5/8)·off_ω
            ⇔ off_F − (9/8 − 5/8)·off_ω < (5/8)·|ω|²
            ⇔ off_F − (1/2)·off_ω < (5/8)·|ω|²

Hmm wait, let me recompute. (TARGET) as originally stated is
‖S‖²_F/|ω|² < 9/8, which expands to ‖S‖²_F < (9/8)|ω|². And
‖S‖²_F = (1/2)Σcⱼ² + off_F, |ω|² = Σcⱼ² + off_ω. So

  (1/2)Σcⱼ² + off_F < (9/8)·(Σcⱼ² + off_ω)
  off_F − (9/8)off_ω < (9/8)Σcⱼ² − (1/2)Σcⱼ² = (5/8)Σcⱼ².

So the original (TARGET) as written in the spec IS equivalent to the
Frobenius bound — there's no mismatch. The issue is that when |ω|² = 0
(i.e., Σcⱼ² + off_ω = 0), the original bound ‖S‖²_F/|ω|² < 9/8 has no
content — LHS is 0/0.

At (1/√2, 0, −1/√2, 1), Σcⱼ² = 2 and off_ω = −2 (since off_ω =
√2·1·(c₃−c₁) = √2·(−√2) = −2). So |ω|² = 0, but Σcⱼ² = 2 > 0, and
(TARGET) in the form "off_F − (9/8)·off_ω < (5/8)Σcⱼ²" reads

  off_F − (9/8)·(−2) = off_F + 9/4 < (5/8)·2 = 5/4
  off_F < 5/4 − 9/4 = −1.

Compute off_F at this point: off_F = (c₄/(3√2))·(−c₁ + 2c₂ − c₃)
= (1/(3√2))·(−1/√2 + 0 + 1/√2) = 0. So

  0 < −1:  FALSE.

**The simplified form of (TARGET) is violated.** But ‖S‖²_F = (1/2)·2 +
0 = 1 and |ω|² = 0, so the original Frobenius ratio is 1/0 = ∞, also
"violated" in any scale but trivially because the vorticity vanishes.

So the phase point (c₁,c₂,c₃,c₄) = (1/√2, 0, −1/√2, 1) is a **zero of
|ω|²**, not a vorticity maximum. A vorticity maximum requires |ω|² to
be finite and positive, and maximal.

### (xv) What (xii)–(xiv) show

This concrete N=4 worst-case analysis reveals that (TARGET) as stated
in the spec (and in attempt_849) **is not a proper inequality at
|ω|=0**. It must be supplemented by |ω|² > 0 (equivalently
Σcⱼ² + off_ω > 0), which is a *non-linear* constraint on c.

At |ω| > 0, the CONSTRAINT (first-order vorticity-max) + |ω|² > 0 +
second-order max condition define a *proper* semialgebraic feasible
set. On this set, (TARGET) is empirically supported by 2089 samples
(attempt_850). But my N=4 algebra does NOT close the inequality on
this set — it merely exposes that the "degenerate" corner of phase
space (|ω|→0) is a boundary where the first-order condition is
trivially satisfied and where (TARGET) as written is meaningless.

---

## Result

**Outcome: (B) — partial reduction, with a specific next step.**

The (TARGET) inequality at the chosen N=4 configuration reduces to
(R) in (a, b, c₂, c₄)-coordinates, subject to (F₁'), (F₃'), (F'), box
bounds |cⱼ| ≤ 1 on all four c's, and the **non-trivial additional
condition |ω|² > 0**, i.e., Σcⱼ² + off_ω > 0, i.e.,

  **(NON-DEG)**  (c₁² + c₂² + c₃² + c₄²) + √2·c₄·(c₃ − c₁) > 0
              = a² + b² + c₂² + 2c₄² + √2·c₄(a − b) > 0.

What the reduction gives (concrete "what's left"):

1. The target becomes polynomial of degree 2 in (a, b, c₂, c₄), subject
   to quartic constraint set (F₁'), (F₃'), (F'), box bounds, and the
   positivity (NON-DEG).
2. The compact semialgebraic set is a *box*-relaxation of the true
   phase-space image of T³ under (cos(x₁), cos(x₂), cos(x₃),
   cos((x₁+x₂+x₃)/√3)). It is strictly larger than the true phase
   space — so if (R) is provable on the box it is provable on the
   true space; if it fails on the box, we must tighten with the
   image-manifold equations (which are quadratic: cⱼ² + sⱼ² = 1 and
   cos-sum-angle identities linking c₄ to c₁, c₂, c₃, s₁, s₂, s₃).
3. The degenerate-|ω| boundary is the natural defect for SOS
   certification: SOS certificates on (R) must include multiplication
   by 1/(|ω|² + ε) or equivalent to avoid the boundary. This is
   standard for **Positivstellensatz with strict inequality on an
   open set**.

**Specific Lean-formalizable next step:** prove the N=4 inequality

  **(R*)**  (√2/3)·c₄·(a + c₂ − 2b) + c₄²
            − (5/8)·(a² + b² + c₂²) · 1_{|ω|²>0}  ≤  0

by Lasserre hierarchy / SOS at degree 4 over the semialgebraic set
defined by (F₁'), (F₃'), (F'), box bounds, (NON-DEG). Degree 4 is
feasible because each constraint is degree ≤ 4 and (R*) is degree 2.
Tools: `mathematica`'s `FindInstance` + `Reduce`, or `sostools` in
Matlab, or Julia's `SumOfSquares.jl`. Output is either:

  (a) a sum-of-squares decomposition ⇒ proof, translate to Lean via
      `polyrith`/`nlinarith` once the polynomial inequality is
      isolated, OR
  (b) an explicit (c₁, c₂, c₃, c₄) witnessing violation ⇒ falsifier
      for the (TARGET) inequality at N=4.

**Gain over attempt_849 / 850:** those documents assumed the
5/8-coherence bound holds and only checked it numerically. The present
file *reduces* it at N=4 to a specific degree-≤4 polynomial question
over a named compact semialgebraic set. It also *identifies* the
phase-space boundary (|ω|→0) where the naive form of (TARGET) is
meaningless.

**What this does NOT do:** (i) it does not close (TARGET) at N=4; (ii)
it does not yet supply the SOS certificate; (iii) it does not
generalize beyond this specific 4-mode configuration. A uniform N=4
proof would need to run the reduction over all choices of (k₁,…,k₄)
and (v₁,…,v₄) with the 3+3 rotational degrees of freedom collapsed by
symmetry. The present argument treats one representative with
permutation symmetry k₁↔k₂↔k₃ broken only by the v-choice.

---

## Prior art

**Bessel + coherence framework** from `lean/CrossModeBound.lean` (the
Bessel `(v·e₁)² + (v·e₂)² ≤ 1` that gives |Sⱼvₖ|² ≤ 1/4). This file
uses the *same tool* — a Bessel-style orthogonality argument combined
with a first-order constraint — but transposed from the (cross-mode
cancellation of |Sω|²) setting to the (cross-mode cancellation of
‖S‖²_F vs |ω|²) setting. The adaptation is straightforward as a set of
algebraic identities; the new content is the first-order CONSTRAINT
(E₂)–(F') which Bessel alone does not give.

**Sum-of-squares / Putinar Positivstellensatz** (Lasserre 2001,
Parrilo 2003): the reduction in §(xi)–(xii) casts (R) as a compact
semialgebraic feasibility problem whose nonemptiness is decidable by
SOS at bounded degree. This replaces the (2089 numerical samples of
attempt_850) with a finite certificate search.

---

## Falsifier

A concrete configuration (a, b, c₂, c₄) ∈ R⁴ satisfying (F₁'), (F₃'),
(F'), |cⱼ| ≤ 1 for all implied cⱼ, AND (NON-DEG) at which

  (√2/3)·c₄·(a+c₂−2b) + c₄²  ≥  (5/8)·(a²+b²+c₂²)

would falsify (R) and therefore the (TARGET) inequality at N=4 for this
configuration, contradicting the empirical margin of ~1.28× reported
in attempt_850. This would be a true counterexample to the Frobenius
route at N=4 (not just a vorticity zero). An SOS solver's output at
degree 4 either produces this witness or provides the certificate.

---

## Status

**Tier 1** (single attempt by single sub-instance, unreplicated).
Independent replication would require:

1. A second Opus instance (or human) repeating the (i)–(ix) algebra
   and verifying the (G), (H), (Q), (R) reductions step-by-step.
2. An independent numerical verification (Julia + `SumOfSquares.jl`
   or Python + `picos`) of the SOS feasibility of (R*) at degree 4
   over the named semialgebraic set, OR production of a concrete
   violator at |ω|>0.
3. A Lean 4 `theorem` statement of (R) with its constraints, ready
   for `polyrith` / `nlinarith` once the SOS decomposition is in
   hand, linking to `strain_hilbert_schmidt_formula`
   (StrainTraceInnerProduct.lean) and `trace_free_operator_norm_bound`
   (TraceFreeAlignment.lean).

Tier 2 would be reached when two of the above three are independently
completed. Current state: zero.

**Additional caveat.** This file uses *one* specific N=4
configuration. A genuine "N=4 theorem" would run over all admissible
(kⱼ, vⱼ) pairs with N=4 — modulo global rotations that's a 3(N−1)=9
parameter family. The reduction in §(i)–(viii) was chosen to respect
the symmetry of this particular quartet; generic quartets will give
different coefficients for (A) and (B). The *shape* of the reduction
generalizes; the specific numbers 23, 8, −31 do not.

---

## Tag

**851.** N=4 coherence bound reduces (at the canonical axis +
body-diagonal quartet with v-choices v₁=ê₂, v₂=ê₃, v₃=ê₁,
v₄=(1,−1,0)/√2) to the explicit polynomial (R)
(√2/3)·c₄·(a+c₂−2b) + c₄² < (5/8)(a²+b²+c₂²) over the semialgebraic
set (F₁'), (F₃'), (F'), |·|≤1, |ω|>0. The unconditional worst case
gives LHS ≈ 1.86× RHS, so the vorticity-max CONSTRAINT is load-bearing.
The degenerate |ω|=0 corner is a boundary defect requiring the
(NON-DEG) strict inequality in any SOS certification. Open next step:
Lasserre SOS at degree 4 on (R*) — either closes or falsifies the N=4
Frobenius route.
