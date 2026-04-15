# Attempt 058 — Audit: What Is Actually Proven About GC ≥ 0

**Date**: 2026-04-14
**Phase**: 5 (Self-check / confirmation-bias audit on the GC program)
**Track**: theory

## Why this attempt

The GC > 0 program has three strong claims currently spread across attempts
050, 053, 056, pattern_061, and numerics/gc_exact_polynomial.py:

1. **Strong coupling**: GC ~ 3c³/2 > 0 at small c (cluster expansion).
2. **Weak coupling**: GC ~ C/β² + O(1/β³) with C > 0 (two-loop lattice PT).
3. **All β** via mean-field: GC_mf = 1/2 − c²/4 > 1/4, plus a fluctuation
   bound |δGC| ≤ C/β covering the correction from MF to the full lattice.

Pattern_061's summary table and gc_exact_polynomial.py's "COMPLETE PROOF
STRUCTURE" present this as effectively complete. A confirmation-bias audit
(SIGMA_METHOD v7) is warranted before moving to Lean formalization.

## The audit

### Claim 1 (strong coupling, 3c³/2) — surface count is under-derived

attempt_050 arrives at "chair O(c³) ~ 5c³" from an informal area-3 surface
count: "4(d−2) + 2 ≈ 10 distinct area-3 tilings, each contributing c³/2, total
~5c³." The exact enumeration is not written out. Mid-attempt the derivation
also emits a "wait, that gives NEGATIVE covariance? Let me recompute"
moment for Cov, and the final reconciliation (that Cov ~ O(c²) × positive
small) relies on comparing a 5c³ bound to a hand-waved "positive small".

What is actually rigorously established by attempt_050: the sign of the
LEADING O(c³) term in a specific cluster expansion is positive assuming a
specific surface-counting inequality that has not been proven.

**Gap**: write out the area-3 surface enumeration for SU(2) d=4 chair vs
plaquette×plaquette explicitly, as a finite combinatorial statement, and
verify it against a small-lattice symbolic computation. Target: a single
inequality of the form
  `N_chair(3) / d_{1/2} − [N_P(3) + N_Q(3)] / d_{1/2}² > 0`
where N_L(k) is the number of area-k surfaces bounded by L. This is the
Lean-target form of the strong-coupling step.

### Claim 2 (weak coupling, two-loop) — cancellation at O(g²) is clean, sign at O(g⁴) is not explicit

attempt_056 cleanly shows:
- At O(g²), the ⟨Tr(F²)⟩ terms cancel exactly.
- At O(g²) the remainder is (g²/2)⟨Tr(F_P F_Q)⟩, which vanishes by lattice
  symmetry for cross-plane plaquettes.
- At O(g⁴), GC is driven by a two-loop graph that the attempt describes
  as "proportional to |G(k)|² × C_A × N > 0" with C_A = 2 (SU(2)).

What is missing:
- The explicit vertex-factor computation. The attempt does not actually
  compute the sign of the vertex contraction; it argues "positive kernel"
  by appealing to |G(k)|² and the absolute value of f^{abc}f^{abc}. The
  vertex contraction can carry signs from the phase factors of the
  plaquette geometry (cross-plane P,Q sit in different planes, so the
  ordering of their F tensors matters).
- pattern_061's fit GC = 2.64/β² − 5.46/β³ has C ≈ 2.64. attempt_056
  estimates C ≈ 0.96. The two differ by ~2.7×. Either the explicit
  computation is not done or the data is being fitted in a regime where
  higher orders dominate.

**Gap**: do the explicit two-loop vertex contraction for the cross-plane
chair, with signs tracked. Is C actually positive, and what is its exact
value? Until this is done, "GC > 0 at weak coupling PROVEN" is aspirational.

### Claim 3 (mean field + fluctuation bound) — this is the most fragile one

`numerics/gc_exact_polynomial.py`'s `gc_one_link_exact(c)` returns
`GC_mf = 1/2 − c²/4`. The script's "COMPLETE PROOF STRUCTURE" uses this
as the backbone. Two problems:

**(a) The MF formula does not match the full-lattice β → ∞ limit.**

At β → ∞, every link is the identity. Direct computation of the full-lattice
GC gives:
- (1/2)⟨Tr(chair)⟩ = (1/2) · Tr(I) = 1.
- (1/4)⟨Tr(P)⟩⟨Tr(Q)⟩ = (1/4) · 2 · 2 = 1.
- GC(β=∞) = 1 − 1 = **0**, not 1/4.

The `gc_one_link_exact` formula is a single-link model with external
staples held at Ω̂ = (1,0,0,0). It computes a different quantity from the
full-lattice GC; specifically, it does not capture the ⟨Tr(P)⟩² = 4 term
that drives the −1 in the weak-coupling limit. The identification
"GC_lattice = GC_mf + δGC with GC_mf > 1/4" is therefore not the
decomposition it claims to be.

**(b) The fluctuation bound |δGC| ≤ C/β is empirically falsified.**

Using pattern_061's data and the script's GC_mf formula:
| β | GC_mf (c_MF ≈ 1 − 3/(12β)) | GC_MC | δGC |
|---|---|---|---|
| 4 | ≈ 0.264 | 0.059 | −0.205 |
| 6 | ≈ 0.260 | 0.047 | −0.213 |
| 8 | ≈ 0.257 | 0.036 | −0.221 |

|δGC| is roughly CONSTANT (~0.22) across β = 4–8. A bound of the form
|δGC| ≤ C/β would require |δGC| to shrink linearly with 1/β. It doesn't.
This confirms (a): the discrepancy isn't a fluctuation correction, it's a
systematic mis-identification of what `gc_one_link_exact` is computing.

### Net: what is actually proven

Stripped to the rigorously established statements:

1. GC > 0 on 4⁴ lattices at β = 2.0, 2.3, 3.0, 4.0, 6.0, 8.0 by direct MC
   (pattern_041, pattern_061). This is an empirical fact, not a proof.
2. ∫ f^{abc}f^{abc} > 0 for SU(2). This is trivial (= 6 for SU(2)).
3. Fierz decomposition GC = (1/2)⟨Tr(chair)⟩ − (1/4)⟨Tr P⟩⟨Tr Q⟩ is
   algebraic.
4. At strong coupling, the leading O(c²) terms in chair and plaq×plaq
   MATCH (both c²/2), so GC starts at O(c³). The SIGN of the O(c³) term
   is positive IF the surface-count inequality above holds.
5. At weak coupling, the O(g²) terms cancel. The sign at O(g⁴) is
   conjecturally positive.

The mass gap therefore still reduces to: **prove GC > 0 at intermediate β
by methods stronger than "MC says so."**

## What this changes

- **Downgrade the claim "GC > 0 is proven" in pattern_061 and
  gc_exact_polynomial.py to "GC > 0 is numerically certified and
  structurally plausible; two explicit finite computations close it."**
- **The two finite computations** are:
  (i) The area-3 surface inequality (strong coupling).
  (ii) The two-loop vertex contraction with tracked signs (weak coupling).
- **The intermediate interval** is where the current machinery actually
  can't reach yet. Cluster expansion is said to converge up to β ≈ 2.5
  (from OS 1978 with SU(2) d=4 radius); two-loop PT is credible for
  β ≥ 4 once (ii) is done. The interval β ∈ [2.5, 4] needs interval
  arithmetic on the exact character expansion — this is `gc_exact_2x4.py`
  and `gc_interval_arithmetic.py` territory, not the flawed
  `gc_exact_polynomial.py` decomposition.

## Recommendations

1. Retire `gc_one_link_exact` as a proof component. Its output is a
   consistent single-link functional but is NOT the lattice GC.
2. Re-audit `gc_exact_2x4.py` for whether its exact 2⁴ computation gives a
   rigorous lower bound on GC across a β grid.
3. Formalize the strong-coupling O(c³) surface count as a finite
   combinatorial inequality, target-state for Lean.
4. Do the explicit two-loop sign computation; reconcile with pattern_061
   fit (C = 2.64 vs analytic estimate ≈ 0.96).

## Tag

058. Audit of the GC > 0 program identifies one structural error
(gc_one_link_exact does not compute lattice GC) and two underdeveloped
bridges (surface-count inequality, two-loop vertex sign). GC > 0 remains
numerically robust but is NOT analytically proven across all β. Next
iteration: either verify 2⁴ exact computation spans the relevant β grid,
or write out the surface-count inequality in finite form.
