# Attempt 856 — Lasserre SOS with polynomial angle-link at attempt_852's N=4 config

**Date**: 2026-04-19
**Phase**: 4 (Frobenius ratio, N=4 tight-system SOS with integer-lattice angle-link)
**Track**: numerics (SDP + T³ critical-point scan)
**Author**: sub-instance of Opus 4.7 (1M ctx), sigma v9.1 frontier push
**Tier**: 1 (single sub-instance, one clean run per degree; T³ scan cross-check)

---

## Question

At **attempt_852's configuration** (k₁=ê₁, k₂=ê₂, k₃=ê₃, k₄=(1,1,0);
v₁=ê₂, v₂=ê₃, v₃=ê₁, v₄=(1,−1,0)/√2), with the T³ angle-link imposed as
polynomial equalities (valid here because k₄ = k₁ + k₂ is integer-lattice):

  c₄ = c₁c₂ − s₁s₂ (cos-sum identity)
  s₄ = s₁c₂ + c₁s₂ (sin-sum identity)

does Lasserre SOS close the N=4 Frobenius bound
**P(c) := (9/8)|ω|² − ‖S‖²_F ≥ 0** on the tight first-order set, or does a
new violator emerge that's realizable on T³?

Three outcomes:
- **(CLOSE)**: SOS certificate → genuine Tier-1 advance.
- **(VIOLATE)**: new violator with all constraints (sphere + first-order +
  angle-link + NON-DEG).
- **(INCONCLUSIVE)**: solver can't decide at tractable degree.

---

## Setup (from attempt_852 §1–§4)

### Target polynomial (all degree 2)

From attempt_852:
- |ω|² = c₁² + c₂² + c₃² + c₄² + √2·(c₃ − c₁)·c₄
- ‖S‖²_F = ½·(c₁² + c₂² + c₃² + c₄²) − (√2/2)·(c₁ + c₃)·c₄
- **P(c) = (5/8)·(c₁² + c₂² + c₃² + c₄²) + (√2/8)·c₄·(13·c₃ − 5·c₁)**

Six monomials:
```
  P[c₁²] = +5/8      P[c₂²] = +5/8      P[c₃²] = +5/8      P[c₄²] = +5/8
  P[c₁·c₄] = −5√2/8 ≈ −0.8839
  P[c₃·c₄] = +13√2/8 ≈ +2.2981
```

(Sanity: numerical identity P = (9/8)|ω|² − ‖S‖²_F verified to 0.00e+00.)

### Polarization inner products / strain traces (from attempt_852 §1–§2)

Nonzero polarization products: v₁·v₄ = −1/√2, v₃·v₄ = +1/√2.
Nonzero strain Hilbert–Schmidt inner products: Tr(S_j²) = 1/2 (j=1..4),
Tr(S₁S₄) = −√2/4, Tr(S₃S₄) = −√2/4. All others zero.

### First-order equations (from attempt_852 §4)

At this configuration the linear system Σ_j β_j k_j = 0 with β_j = s_j·a_j
decouples to three scalar equalities:
- (C1): s₃·a₃ = 0
- (C2): s₁·a₁ − s₂·a₂ = 0
- (C3): s₁·a₁ + s₄·a₄ = 0

where a_j = ω·v_j:
- a₁ = c₁ − c₄/√2
- a₂ = c₂
- a₃ = c₃ + c₄/√2
- a₄ = c₄ + (c₃ − c₁)/√2

### Full tight system, 8 real variables c_{1..4}, s_{1..4}

Polynomial equalities (9 total):
```
sphere_j: c_j² + s_j² − 1 = 0              (j=1..4; sphere₄ is implied by the rest)
AL_c:     c₄ − (c₁ c₂ − s₁ s₂) = 0         (polynomial angle-link)
AL_s:     s₄ − (s₁ c₂ + c₁ s₂) = 0         (polynomial angle-link)
FO_1:     s₃ · a₃ = 0
FO_2:     s₁ · a₁ − s₂ · a₂ = 0
FO_3:     s₁ · a₁ + s₄ · a₄ = 0
```

Polynomial inequality (NON-DEG):
```
|ω|² − 10⁻³ ≥ 0
```

Box inequalities (redundant with spheres, kept for Putinar archimedeanness):
```
1 − c_j² ≥ 0,  1 − s_j² ≥ 0  (j=1..4)
```

Objective: minimize `<P, y>` over Lasserre-feasible moments y.

---

## SDP size

| d | half-monos (M_d side) | full moments | localizer size | solve time |
|---|---|---|---|---|
| 2 | 45 | 495 | 9 (for each of 9 ineqs) | ~2 s |
| 3 | 165 | 3003 | 45 (for each of 9 ineqs) | ~73 s |

Total constraints: 3 170 (d=2), 49 916 (d=3). Each equality `g` of degree dg
contributes `C(n + 2d − dg, 2d − dg)` shifted-moment equations.

**Tool:** cvxpy 1.8.2 + SCS 3.2.11, numpy 2.2.6, DGX Spark.

---

## Raw results

### d=2
```
Status: optimal
Optimal value (lower bound on min P over tight set): −1.1638646747992845
Solve time: 2.2 s
Moment matrix top eigenvalues: [~2e−7, ~3e−7, 2.92, 2.99, 3.01, 5.71]
First-order moments: E[c] ≈ (0, 0.0864, 0, 0) — symmetric mixture (sign-flip invariance)
```

### d=3
```
Status: optimal
Optimal value: −1.1638645968529282
Solve time: 73.2 s
Moment matrix top eigenvalues: [~2e−8, ~2e−8, 7.22, 7.60, 7.65, 10.30]
First-order moments: E[c₂] = +0.0864, all others ≈ 0 — same symmetric mixture
```

**Stability:** d=2 and d=3 agree to ~8·10⁻⁸. The Lasserre relaxation has
stabilized at **min P ≈ −1.16386**. Higher-degree relaxations will not close
the gap: the minimum is genuine.

### T³ critical-point scan (independent verification)

Script: `~/open_problems/math/ns_blowup/proof_attempts_n4/scan_852_critpoints.py`.

At attempt_852's config, k₄ = k₁ + k₂ is integer-lattice so
ω(x) = Σ cos(k_j·x) v_j is **strictly 2π-periodic on T³**. This means every
point of the tight 8-var set **is** of the form (c(x), s(x)) for some x ∈ T³.
The FO equations are exactly ∇|ω|²(x) = 0.

Procedure:
1. 64³ grid sweep of ‖∇|ω|²‖² on T³.
2. BFGS refinement of 3 500 seeds (3 000 smallest-‖grad‖² grid points + 500
   random) minimizing ‖grad‖² to 1e-6 accuracy.
3. Deduplicate and classify each critical point by Hessian eigenvalues.

**Found 60 unique T³ critical points** of |ω|²:
- **6 true local maxima** (Hessian NSD, |ω|² > 0). Max Frobenius ratio
  over maxima: **0.8536 < 9/8 = 1.125** (margin ≈ 0.27).
- **8 degenerate minima** of |ω|² (|ω|² = 0 — not vorticity maxima).
- **46 saddles**.

Sorted by P ascending, the worst critical point is a saddle:
```
x* = (2.12799032, 1.48429993, 0.0)  (refined ‖grad‖² = 1.35e−16)
c = (−0.52881, +0.08639, +1.00000, −0.89125)
s = (+0.84874, +0.99626,  0.00000, −0.45351)

|ω|² = 0.154490        (NON-DEG ✓, far above 10⁻³)
‖S‖²_F = 1.337666
Frobenius ratio = 8.6586
P = −1.16386476

Hessian eigenvalues = (−0.7396, +1.7168, +4.3892)  — 1 negative, 2 positive: index-2 saddle
```

This matches the Lasserre SOS bound **to 6 digits**. The moment-matrix-symmetric
Lasserre atom is the set {x*, its 3 sign-flipped copies at (x₁+π, x₂+π, x₃),
(x₁, x₂+π, x₃+π), etc.} — all saddles with the same (|ω|², ‖S‖²_F, P).

**Verification of the 8-var tight system at x*:**
```
Sphere residuals:  max |c_j² + s_j² − 1|   ≤ 2.2e−16
AL_c, AL_s:        max |c₄ − (c₁c₂−s₁s₂)|  = 0
                       |s₄ − (s₁c₂+c₁s₂)|  = 1.7e−16
FO_1 (C1):         |s₃ a₃|                 ≤ 5.7e−10  (because s₃ ≈ 0 at refined x)
FO_2 (C2):         |s₁ a₁ − s₂ a₂|         ≤ 4.5e−9
FO_3 (C3):         |s₁ a₁ + s₄ a₄|         ≤ 5.7e−9
```

All residuals ≤ 10⁻⁸ after BFGS refinement. **The saddle is on the 8-var
tight set.**

### Bulk T³ sampling cross-check

10⁶ uniform random (x₁, x₂, x₃) ∈ [0, 2π)³ samples, compute c(x) and P(c(x)):
```
min P over 10⁶ T³ samples: −1.2467
max P over 10⁶ T³ samples: +5.6817
quantiles (0, 5, 50, 95, 100): [−1.247, −0.629, +0.983, +3.688, +5.682]
```

These samples satisfy sphere + angle-link automatically but NOT first-order.
They form a superset of the tight set. Min P = −1.247 is MORE negative than
the tight-set min (−1.164), confirming that the FO constraint strictly tightens
the bound (from −1.25 to −1.16), but does not make it non-negative. Consistent.

---

## Verdict — VIOLATE

**The Lasserre SOS at degrees 2 and 3 on the tight system with polynomial
angle-link returns `min P = −1.16386 < 0`, stably.**

A concrete **realizable** violator exists on T³: x* = (2.128, 1.4843, 0) is a
genuine critical point of |ω|² on T³ at attempt_852's configuration, with
Frobenius ratio ≈ 8.66 and P = −1.164. All sphere + angle-link + first-order
equations are satisfied to float64 precision.

The polynomial angle-link DOES tighten the bound compared to attempt_854's
(no-angle-link) SOS: from attempt_854's −1.3096 down to −1.1639. So the
angle-link IS load-bearing in the right direction — but not by enough to
change sign.

### Why the bound stays negative: saddle-vs-max distinction

The violator at x* is a **saddle**, not a local max. Hessian eigenvalues
(−0.74, +1.72, +4.39) show one descent direction and two ascent directions.
At a true local max of |ω|², the Hessian would be NSD (all eigenvalues ≤ 0).

- **True local maxima of |ω|² on T³:** max Frobenius ratio = 0.8536 < 9/8.
  (6 such maxima found.)
- **All critical points of |ω|² on T³:** max Frobenius ratio = 8.66 at the
  saddle x*. Going unbounded on |ω|² → 0 cusps.

The first-order equations (gradient = 0) are strictly weaker than the
maximum condition (gradient = 0 AND Hessian ≤ 0). The tight algebraic set
in 8 variables contains saddle points, which drag P negative.

### Does this kill the Frobenius route at attempt_852's config?

**No.** It rules out any proof that uses only
(sphere + angle-link + first-order) — the three-condition algebraic set
is strictly larger than the set of vorticity MAXIMA, by exactly the saddles.
To close the Key Lemma via Frobenius at this config, one needs a
**second-order Hessian condition** to exclude saddles.

At a vorticity max x* ∈ T³, the 3×3 Hessian of |ω|² is NSD. Writing
H = −2 Σ_j c_j(Mv c)_j k_j⊗k_j + 2 K^T diag(s) Mv diag(s) K, the NSD
condition is the quadratic polynomial constraint
```
max eigenvalue of H(c, s) ≤ 0
```
i.e. `t · 1 − H ⪰ 0` for some t ≤ 0, or equivalently three non-trivial
polynomial matrix-PSD constraints. These are degree-2 polynomial SDP
constraints in (c, s), and can be added to Lasserre.

This is the natural next fire: attempt_857 = Lasserre SOS with
(sphere + angle-link + first-order + Hessian-NSD). Predicted outcome:
bound closes.

### What this closes

**At attempt_852's one configuration, the Frobenius route FAILS on the
algebraic-tight system** (sphere + angle-link + first-order + NON-DEG)
with polynomial angle-link. This is a sharper falsification than
attempt_854's (whose violator wasn't T³-realizable); the present violator
is a genuine T³ critical point, just not a MAX.

The empirical T³ max-ratio of 0.8536 (from the 6 true local maxima at this
config) is 0.27 below 9/8. That's the "real" bound at this configuration.
The Key Lemma at this configuration holds with 0.27 margin **once the
vorticity-max condition is imposed (second-order)**, consistent with
attempt_855's independent grid-scan finding of max ratio 0.727 at
attempt_851's configuration.

---

## Prior art

- **Lasserre (2001)**, "Global optimization with polynomials and the problem
  of moments," SIAM J. Optim. 11, 796. Moment hierarchy + moment-SOS duality.
- **Parrilo (2003)**, "Semidefinite programming relaxations for semialgebraic
  problems," Math. Prog. 96, 293. SOS/SDP programming.
- **Putinar (1993)**, Positivstellensatz on compact archimedean quadratic
  modules. Our box + sphere constraints make the quadratic module archimedean,
  so tight SOS certificates exist at finite degree *if* P > 0. We find
  P < 0 at a feasible atom, so no such certificate can exist.
- **Attempt_852** (2026-04-19) — reduction of P to the polynomial inequality
  10(c₁ − c₄/√2)² + 10 c₂² > 16 c₄² on the generic branch; identified the
  zero-ω boundary L as a spurious first-order branch. Our tight 8-var
  saddle x* is distinct from L (|ω|² = 0.154 ≫ 0).
- **Attempt_853** (2026-04-19) — SOS on attempt_851's config with (F)-relaxation:
  violator at (−1, −4√2/15, +1, −1), P ≈ −1.7.
- **Attempt_854** (2026-04-19) — SOS on attempt_851's config with (E) as
  equalities but NO angle-link (k₄ = (1,1,1)/√3 is irrational, so link is
  transcendental): min P = −1.3096, violator not T³-realizable as a max.
- **Attempt_855** (2026-04-19) — T³ grid scan at attempt_851's config: all
  true local maxima have ratio ≤ 0.727 < 9/8. This attempt's T³ scan at
  attempt_852's config: ratio ≤ 0.854 < 9/8 at 6 true maxima.
- **Euler–Lagrange second-variation theory** — the Hessian condition needed
  to upgrade "critical point" to "local max" is standard PDE-maximization
  theory. In the finite-dim Fourier truncation here it's a polynomial SDP
  constraint.

---

## Falsifier

Concrete point on the **tight set** (8 variables, 4 spheres + 2 angle-link +
3 first-order, NON-DEG satisfied, T³-realizable) with P < 0:

```
x* = (2.12799032, 1.48429993, 0.00000000)   ∈ T³  (integer-lattice)
c = (−0.52880671, +0.08638858, +1.00000000, −0.89125214)
s = (+0.84874228, +0.99626152,  0.00000000, −0.45350813)

Equality residuals:
  max |sphere_j|   ≤ 2.2e−16
  max |AL_c|, |AL_s| ≤ 1.7e−16
  max |FO_1|       ≤ 5.7e−10  (via s₃ = 0)
  max |FO_2|, |FO_3| ≤ 5.7e−9
  |ω|²             = 0.154490  (NON-DEG ≥ 10⁻³ ✓)
  ‖S‖²_F           = 1.337666
  Frobenius ratio  = 8.6586    (vs target < 9/8 ≈ 1.125)
  P(c)             = −1.16386  (matches Lasserre d=3 bound to 6 digits)

Hessian of |ω|² at x*: eigenvalues (−0.7396, +1.7168, +4.3892)
  → x* is a SADDLE, not a local maximum of |ω|².
```

This single T³ point is **the** witness: Lasserre SOS certifies no
nonnegativity certificate can exist on the tight algebraic set without an
additional constraint that excludes saddles (i.e., a second-order /
Hessian-NSD condition).

The derivation is INVALIDATED if:
1. The T³ 8-tuple (c(x*), s(x*)) does not satisfy all 9 equalities — checked
   to ≤ 10⁻⁸ (bound by BFGS tolerance).
2. The Hessian classification is wrong — spot-checked vs numerical 2nd
   differences in `t3_realizability_final.py` (sign-correct, per attempt_855).
3. The Lasserre bound is a solver artifact — two degrees (d=2, d=3) agree to
   8 digits, matches T³ scan to 6 digits, matches 10⁶-sample T³ bulk min
   order-of-magnitude. Artifact ruled out.

---

## Tier

**Tier 1** (single sub-instance). Same discipline as attempt_854. To upgrade
to Tier 2:
- Reproduce the Lasserre bound −1.16386 with Julia `SumOfSquares.jl` + Mosek
  (different toolchain) — pending.
- Reproduce the T³ saddle x* = (2.128, 1.484, 0) via an independent numerical
  critical-point solver — partially pending (scan + BFGS + Hessian all here,
  but second Opus sub-instance has not re-run).

The pencil-and-paper match to attempt_852's §4 decomposition (generic branch
+ zero-ω curve L) is a Tier-1.5 cross-check: the L = {c₁ = c₄/√2, c₂ = 0,
c₃ = −c₄/√2} curve is different from the saddle here (we have c₂ = 0.086,
c₃ = 1, c₄ = −0.891, so c₁ ≠ c₄/√2), so our violator is on the "generic
interior" branch, not on L. Attempt_852 predicted the algebra would close
under NON-DEG on the generic branch, but our saddle shows the generic branch
contains saddles that violate P (at moderate |ω|² > 0), not just the L curve.
This refines attempt_852's diagnosis: the obstruction is **saddles**, not
just the zero-ω curve.

---

## Tag

**856.** Lasserre SOS at d=2 and d=3 on the 8-var tight system (4 spheres + 2
polynomial angle-link AL_c/AL_s + 3 first-order FO_1/2/3 + NON-DEG |ω|² ≥
10⁻³) at attempt_852's N=4 configuration (k₄=(1,1,0) integer-lattice) returns
**min P = −1.16386** stable across degrees. The witness is a true T³
critical point of |ω|²: x* = (2.128, 1.484, 0) is an index-2 saddle (Hessian
eigenvalues −0.74, +1.72, +4.39) with Frobenius ratio ≈ 8.66 and |ω|² =
0.1545 ≫ 10⁻³. **Polynomial angle-link is NOT sufficient** to close
Frobenius at N=4 via algebra: saddles remain admissible. True local maxima
at this config have max Frobenius ratio 0.854 < 9/8 (margin 0.27), so the
Key Lemma at N=4 at this config HOLDS under the full max condition; the
missing ingredient is Hessian-NSD (second-order). Next fire: attempt_857
— Lasserre SOS with Hessian-NSD added as polynomial matrix-PSD localizer.
Verdict: **VIOLATE** the tight algebraic set, **CONFIRM** the bound on the
true-max set (independent T³ grid scan).

---

## Files

- `~/open_problems/math/ns_blowup/proof_attempts_n4/sos_polylink_d3.py`
  — Lasserre SDP builder (cvxpy + SCS), d=2 and d=3
- `~/open_problems/math/ns_blowup/proof_attempts_n4/sos_polylink_d2.log`
  — d=2 solver output
- `~/open_problems/math/ns_blowup/proof_attempts_n4/sos_polylink_d3_run.log`
  — d=3 solver output
- `~/open_problems/math/ns_blowup/proof_attempts_n4/scan_852_critpoints.py`
  — T³ grid + BFGS critical-point scanner with analytic grad+Hessian at
  attempt_852 config
- `~/open_problems/math/ns_blowup/proof_attempts_n4/scan_852_critpoints.log`
  — 60 critical points, 6 true maxima, 46 saddles, worst-P saddle identified
- `~/open_problems/math/ns_blowup/proof_attempts_n4/scan_852_critpoints.npz`
  — raw data (c, s, ratios, P, classification) for all 60 critical points
- `~/open_problems/math/ns_blowup/proof_attempts_n4/verify_852_violator.py`
  — residual verification at refined x* + 10⁶-sample T³ bulk cross-check
- `~/open_problems/math/ns_blowup/proof_attempts_n4/verify_852_violator.log`
  — residuals ≤ 10⁻⁸, bulk min P = −1.247

---
