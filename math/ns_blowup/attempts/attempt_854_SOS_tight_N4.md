# Attempt 854 — Lasserre SOS with (E) as tight equalities on the N=4 attempt_851 configuration

**Date**: 2026-04-19
**Phase**: 4 (Frobenius ratio, N=4 tight-system falsifier / certification)
**Track**: numerics (SDP + projected sampling)
**Author**: sub-instance of Opus 4.7 (1M ctx), sigma v9.1 frontier push

---

## Question

Does the target inequality

  **(TARGET-TIGHT)**  P(c) := (9/8)·|ω|² − ‖S‖²_F  ≥  0

hold on the TIGHT first-order N=4 set at attempt_851's configuration
(k₁=ê₁, k₂=ê₂, k₃=ê₃, k₄=(1,1,1)/√3; v₁=ê₂, v₂=ê₃, v₃=ê₁, v₄=(1,−1,0)/√2)
where the three scalar first-order equations (E₁), (E₂), (E₃) are imposed as
polynomial **equalities** (not the attempt_851 relaxations (F₁'), (F₃'), (F'))?

Attempt_853 ran SOS on the relaxed system and found a violator
`(c₁,c₂,c₃,c₄) = (−1, −4√2/15, +1, −1)` that falsified the relaxation but
fell outside the tight manifold (E). This attempt carries (E) as equalities
to test whether the tight system admits an SOS certificate or a new tight-set
violator.

---

## Tight system setup

**Variables (8 reals):** `c₁, c₂, c₃, c₄, s₁, s₂, s₃, s₄`.

**Sphere equalities (4, each deg 2):**

  `c_j² + s_j² − 1 = 0`   for j = 1, 2, 3, 4.

**Polarization-inner-product inputs (from attempt_851 §(v)):**

  a₁ := ω·v₁ = c₁ − c₄/√2
  a₂ := ω·v₂ = c₂
  a₃ := ω·v₃ = c₃ + c₄/√2
  a₄ := ω·v₄ = c₄ + (c₃ − c₁)/√2

**Vorticity-max first-order equations (E), 3 equalities, each deg 2:**

  (E₁):  s₁·a₁ + (1/√3)·s₄·a₄ = 0
  (E₂):  s₂·a₂ + (1/√3)·s₄·a₄ = 0
  (E₃):  s₃·a₃ + (1/√3)·s₄·a₄ = 0

**Non-degeneracy (inequality, deg 2):**

  |ω|² − ε ≥ 0,   where |ω|² = c₁²+c₂²+c₃²+c₄² + √2·c₄·(c₃ − c₁),  ε = 10⁻³.

**Box (inequalities for Putinar archimedean, redundant with spheres):**

  1 − c_j² ≥ 0 (j=1..4),   1 − s_j² ≥ 0 (j=1..4).

**Target polynomial to certify nonneg:**

  P(c) = (9/8)·|ω|² − ‖S‖²_F
       = (5/8)·(c₁²+c₂²+c₃²+c₄²) + (9√2/8)·c₄·(c₃−c₁) − (c₄/(3√2))·(−c₁+2c₂−c₃).

Expanded, P has 7 monomials (all degree 2):

```
P[c₁²]    = +5/8
P[c₂²]    = +5/8
P[c₃²]    = +5/8
P[c₄²]    = +5/8
P[c₁·c₄]  = −9√2/8 − 1/(3√2)  = −(27/8 + 1/3)·(1/√2)·?  → numerically −1.355288
P[c₂·c₄]  = −2/(3√2)                                      = numerically −0.471405
P[c₃·c₄]  = +9√2/8 + 1/(3√2)                              = numerically +1.826693
```

(`−9√2/8 − 1/(3√2) ≈ −1.591 − 0.236 = −1.827`, but wait: from expansion
`(9/8)·√2·c₄·(c₃ − c₁) − (c₄/(3√2))·(−c₁ + 2c₂ − c₃)`, the c₁·c₄ coefficient
is `−9√2/8 − (−1)/(3√2) = −9√2/8 + 1/(3√2) ≈ −1.591 + 0.236 = −1.355` ✓.
The c₃·c₄ coefficient is `+9√2/8 − (−1)/(3√2) = +9√2/8 + 1/(3√2) ≈ +1.827` ✓.)

The sphere and (E) equalities together are the **tight** first-order system:
(E) requires the three quantities `s_j·a_j` (j=1,2,3) to all equal `−s₄·a₄/√3`,
not merely satisfy the squared-inequality relaxations (F₁'),(F₃'),(F') from
attempt_851. This strictly shrinks the feasible set.

---

## SDP setup

**Tool:** `cvxpy 1.8.2` with `scs 3.2.11`, numpy 2.2.6, scipy 1.16.3, on DGX Spark.

**Lasserre moment relaxation at order d**: the moment matrix M_d(y) is
`C(n+d, d) × C(n+d, d)` where n = 8 variables. Full moment vector has
`C(n+2d, 2d)` entries.

| d | half-monomials (M_d side) | full moments | moment matrix entries | solve time |
|---|---|---|---|---|
| 2 | 45 | 495 | 2025 | ~2 s |
| 3 | 165 | 3003 | 27 225 | ~75 s |

**Equality enforcement:** for each equality polynomial g (deg d_g), every
shifted moment `<g, y·u>` is set to 0 for all monomials u with deg ≤ 2d − d_g.
This is the moment-equivalent of the localizing matrix M_{d − ⌈d_g/2⌉}(g·y) = 0.

**Inequality enforcement:** standard Putinar localizer `M_{d − ⌈d_g/2⌉}(g·y) ⪰ 0`.

Moment matrix M_d ⪰ 0 and normalization `y[monomial 1] = 1`. Objective:
minimize `<P, y>` over feasible y. Optimal value is a **lower bound** on
`min over tight set of P(c)`. If < 0 ⇒ P fails on the tight set; if ≥ 0 ⇒
P ≥ 0 on the tight set (SOS certificate exists).

Code: `~/open_problems/math/ns_blowup/proof_attempts_n4/sos_tight_d6.py`.

---

## Raw results

### Lasserre d=2

```
Status: optimal
Optimal value (lower bound on min P over tight set): −1.3095610181050639
Solve time: ~2.4 s
Moment matrix top eigenvalues: [1.8e−7, 1.9e−7, 1.00, 3.00, 3.01, 7.99]
First-order moments all ≈ 0 (symmetric mixture under c↦−c).
```

### Lasserre d=3

```
Status: optimal
Optimal value: −1.3095610572516325
Solve time: ~75 s (SCS, 48 926 linear constraints; 165×165 moment PSD;
                  nine 45×45 localizer PSDs; seven 495-equality blocks)
Moment matrix top eigenvalues: [1.9e−7, 2.0e−7, 3.01, 7.99, 8.02, 15.96]
First-order moments all ≈ 0.
```

**Stability across degrees:** d=2 and d=3 agree to ~4·10⁻⁸, confirming the
Lasserre relaxation has stabilized. Further moment orders will not close the
gap — the minimum is genuinely ≈ −1.3095611, not an artifact of relaxation
weakness.

### SLSQP on the tight set (independent verification)

Starting from four seeds (sampler min, corner `(−1,0,1,−1,0,1,0,0)`, two
symmetric variants) with SLSQP and equality constraints (4 spheres + 3 E's)
plus NONDEG ≥ 10⁻³:

```
P_min = -1.30956105 at
  (c₁, c₂, c₃, c₄) = (-0.99930243, -0.01094037, +0.99930243, -0.99895346)
  (s₁, s₂, s₃, s₄) = (+0.03734511, +0.99994015, -0.03734511, +0.04573823)
  |omega|^2 = 0.17174230
  constraint residuals: max |sphere| = 2.4e−15, max |E| = 1.4e−17.
```

### Symmetric-ansatz analytic reduction

Set c₁ = −A, c₂ = C, c₃ = A, c₄ = −B (3-param family consistent with the
observed minimizer's symmetry).

- Tight eq Q₁ = Q₄ gives `3 A² − 2 B² = 1`.
- Tight eq Q₁ = Q₂ gives `(1−A²)(A − B/√2)² = (1−C²) C²`.
- `P = (5/4) A² + (5/8)(B² + C²) − (9√2/4)·A·B + (√2/3)·B·C`.

Scalar minimization along this family gives

```
min_{A ∈ (1/√2, 1)} P  =  -1.309561054   at A = 0.999302430,
                                            B = 0.998953861,
                                            C = -0.010936594
                         |omega|² ≈ 0.17174
```

matching the full-dimensional SLSQP and the SDP lower bound to 8 digits.

All four independent computations (SDP d=2, SDP d=3, SLSQP, ansatz) agree:

  **min_{tight set} P  ≈  −1.3095611  <  0.**

---

## Sampling on the tight set

**Strategy.** Parametrize the tight manifold via the three equalities

  (1−c_j²)·a_j²  =  λ²   for j = 1, 2, 3
  (1−c_4²)·a_4²  =  3·λ²  (so all four Q's equal λ²).

Fix (c₂, c₄), set λ² := (1−c₂²)·c₂² (j=2 arm, always in [0, 1/4]), then
for each j ∈ {1, 3} solve the quartic in c_j from `(1−c_j²)(c_j ∓ c₄/√2)² = λ²`
via numpy.roots (real roots in [−1, 1]). Accept if residual
|Q₄ − λ²| < 10⁻⁴, then refine via Newton in c₄ to get |Q₄ − λ²| < 10⁻⁷.

**Runs** (structured grid 300×300 on (c₂, c₄) + 200 000 random (c₂, c₄) seeds):

```
Structured grid: 755 184 candidate points → 5 364 near-tight → 660 refined
Random seeds:    200 000 candidate points → 11 312 near-tight
Total tight-set points with |omega|^2 ≥ 10⁻³: 1 912
Runtime: 18.5 s

min P observed on tight set:  -1.309654   (from the refined grid)
  at (c₁, c₂, c₃, c₄) = (-0.998275, -0.017182, +0.998275, -0.997902)
  |omega|² = 0.171585

P quantiles on tight set:
   0%: -1.309  5%: -1.218  25%: -0.971  50%: +0.375  75%: +1.256
  95%: +2.351  99%: +4.513  100%: +6.071

Fraction of tight-set points with P < 0:  853 / 1912  ≈  44.6%
Fraction of tight-set points with Frobenius ratio ≥ 9/8:  44.6%
Max Frobenius ratio on tight set: 15.39.
```

**Worst-10 tight-set points:**

```
P=-1.30965  |om|²=0.1716  c=(-0.9983, -0.0172, +0.9983, -0.9979)
P=-1.30954  |om|²=0.1717  c=(+0.9994, +0.0100, -0.9994, +0.9991)
P=-1.30954  |om|²=0.1717  c=(-0.9994, -0.0100, +0.9994, -0.9991)
... (all near the (±1, 0, ∓1, ±1) corner, by c ↦ −c symmetry)
```

These all cluster near an interior point of the tight manifold close to
`(c₁, c₂, c₃, c₄) ≈ (−1, 0, +1, −1)`. The exact limit corner gives
P = 15/8 − 9√2/4 ≈ −1.3069805 (not the minimum); the true minimum at
`A ≈ 0.9993, B ≈ 0.9990, C ≈ −0.0109` is slightly deeper at −1.3095611.

---

## Interpretation

**The N=4 Frobenius inequality `‖S‖²_F/|ω|² < 9/8` is FALSE on the tight
first-order set at attempt_851's configuration.**

Four independent methods agree:

1. SDP lower bound (d=2 and d=3, stable to ~10⁻⁷) gives `min P = −1.3096`.
2. Direct SLSQP with equality constraints finds a feasible minimizer with
   `P = −1.30956` and constraint residuals ~10⁻¹⁵.
3. Structured + random sampling with quartic-root projection finds 853 out of
   1 912 tight-set points (≈44.6%) with P < 0, minimum `P = −1.30965`.
4. A symmetric-ansatz 1-parameter reduction gives the same minimum to 8 digits.

The worst-case tight-set point is near
`(c₁, c₂, c₃, c₄) ≈ (−0.999, −0.011, +0.999, −0.999)` with
`|ω|² ≈ 0.172 > 10⁻³` (safely away from the degenerate boundary).
**The violator is genuine, not an |ω|→0 artifact.**

### Does this close / falsify the N=4 Key Lemma?

**At this one configuration, it FALSIFIES the N=4 Frobenius route as formulated
on the 8-variable tight set.** The 9/8 bound cannot be proven from
(sphere equalities + first-order vorticity-max equalities) alone at this
configuration.

**However there is one further step** — the tight 8-variable set is itself
**strictly larger** than the true T³ image of attempt_851's 3-angle
parametrization:

- The tight set treats (c, s) as 8 independent reals with sphere+E.
- The T³ image additionally requires `c_j = cos(k_j · x)` and
  `s_j = sin(k_j · x)` for a **common** `x ∈ T³`, with `k₄ = (1,1,1)/√3`
  making `x₄ = (x₁+x₂+x₃)/√3`.
- The worst violator `(−1, 0, 1, −1, 0, 1, 0, 0)` is NOT in the T³ image:
  it would require `x₁ = π, x₂ = π/2, x₃ = 0` AND
  `(x₁+x₂+x₃)/√3 = 3π/(2√3) ≈ 2.72, cos(2.72) ≈ −0.91 ≠ −1`.

So this attempt **does not directly falsify the N=4 Frobenius bound on T³**,
but it does:

- **Falsify the N=4 Frobenius bound on the tight 8-variable set.** This is a
  stronger falsification than attempt_853's (which lived on the looser
  (F)-relaxation) but is still one rung below the T³-realizable set.
- **Rule out attempt_851's Frobenius route at this configuration.** Any proof
  that works purely from (sphere + first-order vorticity-max equations +
  |ω|² > 0) cannot succeed — the extra T³-link constraints `x_j = arccos(c_j)
  mod 2π` and `x₄ = (x₁+x₂+x₃)/√3` are load-bearing.

The N=4 Frobenius bound on the T³ image may still hold (attempt_850 has 2 089
empirical samples all respecting it with margin ≈ 1.28×), but would need to be
proved via the T³ angle-link equations, which are transcendental (sine-sum
identities linking the four (c_j, s_j) pairs to three independent angles).

### Verdict

**At this one N=4 configuration: falsifies the tight-system route.** Not the
Frobenius bound itself (which lives on a strictly smaller T³-realizable set).
Attempt_851's approach — prove P ≥ 0 from algebraic first-order equations
only — does NOT work here, neither on the (F)-relaxation (attempt_853) nor
on the (E)-tight system (this attempt).

---

## Cross-check

Agent B's relaxation violator `(c₁,c₂,c₃,c₄) = (−1, −4√2/15, +1, −1)` on the
**tight** system:

- Sphere forces `s₁ = s₃ = s₄ = 0` (since c_j² = 1 for j=1,3,4).
- Sphere_2: `s₂² = 1 − 32/225 = 193/225`, so `s₂ = ±√(193/225) ≈ ±0.926 ≠ 0`.
- (E₁): `s₁·a₁ + (1/√3)·s₄·a₄ = 0·a₁ + 0·a₄ = 0`  ✓ (trivially).
- (E₃): `s₃·a₃ + (1/√3)·s₄·a₄ = 0·a₃ + 0·a₄ = 0`  ✓ (trivially).
- (E₂): `s₂·a₂ + (1/√3)·s₄·a₄ = s₂·c₂ + 0 = s₂·(−4√2/15)`.
  With s₂ = ±0.926: `(E₂) = ∓0.349 ≠ 0`.

**Attempt_853's violator FAILS (E₂) as an equality**, as expected. It lived in
the (F₁'), (F₃'), (F') relaxation where (E₂) was replaced by the inequality
`(1−c₂²)·c₂² ≤ 1/4`, which is satisfied (= 32/225·193/225 ≈ 0.122 ≤ 0.25). But
the tight equality `s₂·c₂ = −s₄·a₄/√3 = 0` is violated at this point. Good.

This verifies that the tight system (E) is strictly smaller than the attempt_853
relaxation, and that carrying the tight equalities removes attempt_853's
violator. The new violator reported here (near `(−1, 0, +1, −1)` with
s₂ = ±1) has a different structure (s₁ = s₃ = s₄ = 0 and a₂ = c₂ = 0 make
all three E's trivial) and is not removed by the tight formulation.

---

## Prior art

- **Lasserre (2001)**, "Global Optimization with Polynomials and the Problem
  of Moments", SIAM J. Optim. 11, 796. Moment hierarchy + moment-SOS duality.
- **Parrilo (2003)**, "Semidefinite Programming Relaxations for
  Semialgebraic Problems", Math. Prog. 96, 293. SOS/SDP programming.
- **Putinar (1993)**, Positivstellensatz on compact archimedean modules.
  Here the box constraints |c_j|, |s_j| ≤ 1 plus the sphere equalities make
  the quadratic module archimedean, so tight SOS certificates exist at finite
  degree if P > 0 on the semialgebraic set. We find P is NOT > 0, so no
  certificate exists.
- Attempt_851 (2026-04-19) reduction to (F)-relaxation; attempt_853 (2026-04-19)
  SOS check on (F)-relaxation (violator at `(−1, −4√2/15, +1, −1)`).
- Attempt_850 (earlier) empirical N=4 margin ≈ 1.28× on 2 089 T³ samples —
  those samples live on the T³-realizable set, strictly smaller than the tight
  8-variable set falsified here.

---

## Falsifier

A concrete point on the **tight N=4 set** (8 variables, 4 spheres + 3 E
equalities, |ω|² > 10⁻³) with P < 0:

```
(c₁, c₂, c₃, c₄) = (-0.99930243, -0.01094037, +0.99930243, -0.99895346)
(s₁, s₂, s₃, s₄) = (+0.03734511, +0.99994015, -0.03734511, +0.04573823)

sphere residuals:  max |c_j² + s_j² − 1|   ≤ 2.4 × 10⁻¹⁵
E residuals:       max |E_j|                ≤ 1.4 × 10⁻¹⁷
|ω|²             = 0.17174230
P                = −1.30956105
‖S‖²_F/|ω|²      ≈ 8.8   (vs target < 9/8 = 1.125)
```

To falsify the Frobenius bound on **T³ itself** (not merely on the tight
8-variable set), one would need a violating point `x* ∈ T³` with
`c_j = cos(k_j · x*)`, `s_j = sin(k_j · x*)`, and `x₄ = (x₁+x₂+x₃)/√3`. The
tight-set violator above is NOT of this form — it cannot be realized by any
single `x* ∈ T³` under attempt_851's k-quartet.

---

## Tier

**Tier 1** (single sub-instance, single configuration, single compute run per
degree; two degrees corroborate). Not an independent replication.

For Tier 2: a second agent or Julia+`SumOfSquares.jl`+`Mosek` should reproduce
both the SDP d=3 lower bound `−1.3095611` and the symmetric-ansatz analytic
minimum at A ≈ 0.9993. The symmetric ansatz itself is a pencil-and-paper
1-parameter scalar optimization once (`3 A² − 2 B² = 1`) is substituted.

For a decisive Tier 1 falsification of the N=4 bound on T³, the T³-link
equations `x_j = arccos(c_j), x₄ = (x₁+x₂+x₃)/√3, s_j = sin(x_j)` would need
to be enforced and scanned for violators — this is transcendental, not
polynomial SOS.

---

## Tag

**854.** Lasserre SOS with (E) as equalities at d=2 and d=3 on the 8-var tight
N=4 system (attempt_851 configuration) gives `min P = −1.3095611` (stable
across degrees, matched by SLSQP, matched by projected sampling, matched by
symmetric-ansatz analytic minimum). The attempt_851 + attempt_853 Frobenius
route **fails on the tight set at this configuration** — carrying (E) as
equalities (not (F)-style inequalities) removes attempt_853's violator but
admits a new interior violator at (c₁,c₂,c₃,c₄) ≈ (−0.999, −0.011, +0.999,
−0.999) with |ω|² ≈ 0.172, P ≈ −1.31, Frobenius ratio ≈ 8.8. This does NOT
falsify the N=4 Frobenius bound on T³, but it rules out any purely algebraic
(sphere + first-order) proof at this configuration: the T³ angle-link is
load-bearing. To close N=4 on T³ one must use the transcendental realizability
constraint `x₄ = (x₁+x₂+x₃)/√3`, or pick a different N=4 configuration where
the tight algebraic set is already sufficient.
