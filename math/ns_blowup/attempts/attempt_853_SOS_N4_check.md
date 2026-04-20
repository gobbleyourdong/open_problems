# Attempt 853 — Lasserre SOS degree-4 check of (R*) from attempt_851

**Date**: 2026-04-19
**Phase**: 4 (Frobenius ratio, N=4 feasibility check)
**Track**: numerics (SDP)
**Author**: sub-instance of Opus 4.7 (1M ctx), sigma v9.1 frontier push

---

## Question

Does the polynomial inequality (R*) from attempt_851 §(xv) hold over the semialgebraic set S it was reduced to?

  **(R*)**   (5/8)·(a² + b² + c₂²)  −  (√2/3)·c₄·(a + c₂ − 2b)  −  c₄²   ≥  0

on S defined by:
- Box: `|a + c₄/√2| ≤ 1`, `|b − c₄/√2| ≤ 1`, `|c₂| ≤ 1`, `|c₄| ≤ 1`.
- (F₁'): `(1 − (a + c₄/√2)²)·a² ≤ 1/4`.
- (F₃'): `(1 − (b − c₄/√2)²)·b² ≤ 1/4`.
- (F'):  `(1 − c₄²)·(b − a)² ≤ 3/2`.
- (NON-DEG): `a² + b² + c₂² + 2c₄² + √2·c₄·(a − b) > 0`.

---

## Tool

- **cvxpy 1.8.2** with **SCS** SDP solver (available on DGX Spark). No Julia, no PICOS, no MOSEK; cvxpy was installed via `pip install --user cvxpy` (`pip install --break-system-packages` was NOT used; standard user install succeeded).
- Lasserre moment relaxation (the dual of SOS): minimize `<P, y>` over pseudo-moment sequences `y` with moment matrix `M_d(y) ⪰ 0` and localizing matrices `M_{d - ⌈deg(g)/2⌉}(g·y) ⪰ 0` for each constraint polynomial `g`.
- At relaxation order d, this gives a lower bound on `min_S P`. If the bound is < 0, (R*) fails on S; if the bound is ≥ 0, P ≥ 0 on S.
- Sampling (2×10⁶ uniform points in `[-1,1]⁴` for `(c₁,c₂,c₃,c₄)`) as an independent violator search.

Prior art: Lasserre (2001) on moment hierarchies; Parrilo (2003) on SOS programming; Putinar's Positivstellensatz for compact archimedean quadratic modules.

---

## Set-up

The polynomial `P(a,b,c₂,c₄) := (5/8)(a² + b² + c₂²) − (√2/3)·c₄·(a + c₂ − 2b) − c₄²` has degree 2 in 4 variables with 7 monomials:

```
P[a²]    = +5/8
P[b²]    = +5/8
P[c₂²]   = +5/8
P[c₄²]   = −1
P[a·c₄]  = −√2/3
P[c₂·c₄] = −√2/3
P[b·c₄]  = +2√2/3
```

Constraint polynomials (reformulated as g ≥ 0):
```
g_box1 = 1 − (a + c₄/√2)²            [deg 2]
g_box2 = 1 − (b − c₄/√2)²            [deg 2]
g_box3 = 1 − c₂²                     [deg 2]
g_box4 = 1 − c₄²                     [deg 2]
g_F1   = 1/4 − (1 − (a+c₄/√2)²)·a²   [deg 4]
g_F3   = 1/4 − (1 − (b−c₄/√2)²)·b²   [deg 4]
g_F    = 3/2 − (1 − c₄²)·(b − a)²    [deg 4]
g_ND   = a² + b² + c₂² + 2c₄² + √2·c₄·(a − b)   [deg 2]
```

Two relaxation orders run:
- **d = 2** (moments up to deg 4): 15 half-degree monomials, 70 full monomials. Localizers: size 5 for each deg-2 g, size 1 (scalar) for each deg-4 g.
- **d = 3** (moments up to deg 6): 35 half-degree monomials, 210 full monomials. Localizers size 15 / 5.

Code (verbatim) in `~/open_problems/math/ns_blowup/proof_attempts_n4/sos_check.py` (d=2) and `sos_check_d3.py` (d=3).

---

## Raw results

### Sampling (2,000,000 uniform samples in (c₁, c₂, c₃, c₄) ∈ [−1,1]⁴)

```
Feasible samples: 783,343 / 2,000,000 (39.17%)
min P on feasible set: −1.367420
  at (a,b,c₂,c₄) = (−0.18765, 0.29185, −0.39291, −0.99619)
  corresponding (c₁, c₃) = (−0.89207, 0.99627), |ω|² ≈ 2.94
Feasible samples with P < 0: 224,525 (28.66%)
Feasible samples with P < 0 AND |ω|² > 0.01: 224,516
```

**→ 28.66% of the relaxed feasible set violates (R*), with |ω|² far from 0.**

### Lasserre moment relaxation

```
d = 2:  min_S P ≥ −1.395866   (status: optimal)
d = 3:  min_S P ≥ −1.395869   (status: optimal, bound stabilized)
```

Moment matrix at d=3 has numerical rank 2 (top eigenvalues 2.71, 2.38; rest ≤ 1.5×10⁻⁷), indicating the optimal moment sequence is a symmetric ±-atom mixture.

### Exact violator (SLSQP refinement + symbolic verification)

Analytic minimizer of P on S (verified via sympy): at the box corner

```
  (c₁, c₂, c₃, c₄)  =  (−1,   −4√2/15,   +1,   −1)
  equivalently (a, b, c₂, c₄) = (1/√2 − 1,  1 − 1/√2,  −4√2/15,  −1)
```

with exact value

```
  P_min  =  643/360  −  (9√2)/4  ≈  −1.3958694042.
```

Feasibility at this point:
- box1: `|c₁| = 1` (tight), box2: `|c₃| = 1` (tight), box3: `|c₂| = 4√2/15 ≈ 0.377` (strictly interior), box4: `|c₄| = 1` (tight).
- (F₁'): `(1 − c₁²)·a² = 0·a² = 0 ≤ 1/4` ✓
- (F₃'): `(1 − c₃²)·b² = 0 ≤ 1/4` ✓
- (F'):  `(1 − c₄²)·(b − a)² = 0 ≤ 3/2` ✓
- (NON-DEG): `a² + b² + c₂² + 2c₄² + √2·c₄·(a − b) = 707/225 ≈ 3.142 > 0` ✓ (far from the |ω|=0 boundary)

Direct matrix check at `(c₁, c₂, c₃, c₄) = (−1, −4√2/15, +1, −1)`:
- `‖S‖²_F ≈ 1.7489`
- `|ω|² ≈ 0.3138`
- Frobenius ratio `‖S‖²_F / |ω|² ≈ 5.573` — this **exceeds** the target threshold 9/8 = 1.125 by a factor of **4.95**.

---

## Interpretation

### What this falsifies

**(R*) as stated in attempt_851 §(xv) is FALSE.** The Lasserre SDP at d=2 and d=3 both certify `min_S P ≤ −1.396 < 0`, and a concrete feasible point `(c₁, c₂, c₃, c₄) = (−1, −4√2/15, +1, −1)` achieves this minimum exactly with `|ω|² ≈ 0.314 > 0` (safely away from the degenerate boundary).

**Sigma v9.1 falsifier line (explicit)**: the configuration `(c₁, c₂, c₃, c₄) = (−1, −4√2/15, +1, −1)` at the N=4 axis + body-diagonal quartet of attempt_851 satisfies every constraint in attempt_851's semialgebraic set S, has strictly positive `|ω|²`, and violates (R*) with `P(a,b,c₂,c₄) = 643/360 − 9√2/4`.

Bound stabilization between d=2 and d=3 (both give ≈ −1.39587) confirms the relaxation is **tight**: higher-degree SOS will not close the gap. The minimum is genuinely −1.39587 at this violator.

### What this does NOT mean

The violator **does NOT correspond to a real vorticity maximum on T³**. At the violator, `c₁ = c₃ = c₄ = ±1`, so `s₁ = s₃ = s₄ = 0`. The first-order condition `sⱼ·(ω·vⱼ)·kⱼ = 0` (attempt_851 (*)) then becomes `s₂·(ω·v₂) = 0`, which forces either `s₂ = 0` (i.e., `c₂ = ±1`) or `ω·v₂ = c₂ = 0`. The violator has `c₂ = −4√2/15 ≈ −0.377`, neither of which. So this `(c₁,…,c₄)` does NOT arise from a stationary point of `|ω|²` on T³.

**The root cause is the relaxation.** Attempt_851 §(vi)–(viii) derived the INEQUALITY bounds (F₁'), (F₃'), (F') from the j=2 arm of the TIGHT critical-point equalities (E):

```
(E):  (1−c₁²)·(c₁−c₄/√2)² = (1−c₂²)·c₂² = (1−c₃²)·(c₃+c₄/√2)²
      = (1/3)·(1−c₄²)·(c₄+(c₃−c₁)/√2)².
```

The derivation keeps only `(1−cⱼ²)(ω·vⱼ)² ≤ (1−c₂²)c₂² ≤ 1/4`, i.e., bounds `(F_j')` by the j=2 arm's MAX value 1/4 (attempt_851 §(vii)). But (E) says all four expressions are **EQUAL**, not just bounded by the same number. The violator has:

```
  (1 − c₁²)·a²        = 0
  (1 − c₂²)·c₂²       ≈ 0.0989
  (1 − c₃²)·b²        = 0
  (1/3)(1 − c₄²)·(ω·v₄)²  = 0
```

— three zeros and one nonzero. These are NOT equal. So the violator is outside the tight manifold (E) but inside the relaxation (F').

### Verdict

**At degree 4 (and 6), (R*) is infeasible** for the relaxation in attempt_851 §(xv). The reduction (R) → (R*) as written **does not close** the N=4 Frobenius route — too much information was discarded when the tight equalities (E) were relaxed to the inequalities (F₁'), (F₃'), (F').

This is a **genuine, reproducible falsifier of (R*)**, not an artifact of the |ω|=0 boundary pathology flagged in attempt_851 §(xiii)–(xv). The violator has `|ω|² ≈ 0.314 > 0` and its (NON-DEG) slack is ≈ 3.14.

**However**, this does NOT falsify the N=4 Frobenius bound itself (`‖S‖²_F/|ω|² < 9/8`). The Frobenius bound is claimed over the TIGHT critical manifold (E), and attempt_850 reported 2089 numerical samples all respecting it with margin ≈ 1.28×. The falsifier above lives on the relaxation, not the manifold, and is not a counterexample to the Frobenius bound.

### Specific next steps (honest)

To upgrade attempt_851 into a working reduction, the **tight equalities (E) must be carried**, not dropped. Replace (R*) with the SOS feasibility problem

  **(R**)**  `P(a,b,c₂,c₄) ≥ 0`  subject to  (E) (equality), box, (NON-DEG).

Here (E) gives three scalar polynomial equalities in (c₁, c₂, c₃, c₄). The resulting semialgebraic set is strictly smaller than S and may admit SOS certification. I did NOT run this stricter SDP — it was out of scope for the degree-4 check requested.

### Degree 6 was also checked

As requested: d=3 (moments to deg 6) improves the Lasserre lower bound by less than 3×10⁻⁶ over d=2. The bound is numerically stable — the relaxation is tight at d=2 and higher degrees do NOT help. The infeasibility is intrinsic to the relaxation, not the SOS degree.

---

## Reproduce

Files (all in `~/open_problems/math/ns_blowup/proof_attempts_n4/`):

- `sample_falsifier.py` + `sample_falsifier.log` — uniform sampling, 2×10⁶ points.
- `sos_check.py` + `sos_check.log` — Lasserre d=2 moment relaxation.
- `sos_check_d3.py` + `sos_check_d3.log` — Lasserre d=3.
- `refine_violator.py` + `refine_violator.log` — SLSQP local min of P on S.
- `analytic_violator.py` + `analytic_violator.log` — exact symbolic violator + Frobenius ratio verification.
- `verify_violator.py` + `verify_violator.log` — original-space double-check (Sⱼ, vⱼ matrices).

Runtime on DGX Spark: sampling ~1.5s; SDP d=2 ~2s; SDP d=3 ~25s (including cvxpy compile). No solver hangs, no crashes.

---

## Prior art

- **Lasserre (2001)**, "Global Optimization with Polynomials and the Problem of Moments", SIAM J. Optim. — the moment hierarchy used here.
- **Parrilo (2003)**, "Semidefinite Programming Relaxations for Semialgebraic Problems", Math. Program. — the SOS / SDP correspondence.
- **Putinar (1993) Positivstellensatz** — guarantees that on a compact archimedean quadratic module, a strictly positive polynomial admits an SOS·constraints decomposition at some finite degree; here the relaxation is tight at low degree because the feasible set has dim ≥ 1 and the optimum is attained at a box corner.
- Attempt_850 empirical N=4 samples (2089 vorticity-max critical points): reported margin ≈ 1.28× for the Frobenius bound. Those samples lived on the TIGHT manifold (E); the present result on the RELAXATION (F') is consistent with them — the Frobenius bound may well hold on (E) but not on the looser S.

---

## Falsifier

A concrete configuration (a, b, c₂, c₄) ∈ R⁴ satisfying all the constraints in attempt_851's semialgebraic set S, with |ω|² > 0, and violating (R*), is:

  `(a, b, c₂, c₄) = (1/√2 − 1,  1 − 1/√2,  −4√2/15,  −1)`

equivalently

  `(c₁, c₂, c₃, c₄) = (−1,  −4√2/15,  +1,  −1)`

with `P(a, b, c₂, c₄) = 643/360 − 9√2/4 ≈ −1.3959`, `|ω|² ≈ 0.314`, Frobenius ratio ≈ 5.57.

This falsifies the N=4 Frobenius route **as reduced in attempt_851 §(xv)**. It does NOT falsify the N=4 Frobenius bound in its original form (on the tight critical manifold (E)) — see §"What this does NOT mean".

---

## Status

**Tier 1** (single compute run, single sub-instance, unreplicated).

For Tier 2 this should be independently re-run by a second agent (or in Julia with `SumOfSquares.jl` + `Mosek`) and the violator `(−1, −4√2/15, +1, −1)` verified from first principles in Lean (it's trivial to check: plug in, evaluate P). The symbolic identity `P = 643/360 − 9√2/4` at this corner is a pencil-and-paper computation.

---

## Tag

**853.** Lasserre SOS moment relaxation at d=2 and d=3 (moments to degree 4 and 6) of (R*) from attempt_851 §(xv) gives `min_S P = 643/360 − 9√2/4 ≈ −1.3959`, achieved exactly at `(c₁,c₂,c₃,c₄) = (−1, −4√2/15, +1, −1)` with `|ω|² ≈ 0.314 > 0`. Bound is stable between d=2 and d=3 (Δ ≈ 3×10⁻⁶), so higher SOS degrees will not close the gap. **(R*) as written in attempt_851 is FALSE.** The reduction from the true target (Frobenius bound on the critical manifold (E)) to (R*) relaxed the tight equalities (E) to inequalities (F₁'), (F₃'), (F') via the j=2 arm, and this relaxation is too loose: the violator lies in the relaxation but NOT on (E). The Frobenius bound itself remains open; attempt_851's specific route is not viable at this relaxation level. To salvage the approach, carry (E) as equalities, not inequalities — separate SDP, out of scope here.
