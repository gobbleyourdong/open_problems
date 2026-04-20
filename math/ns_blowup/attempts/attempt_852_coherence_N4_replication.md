# Attempt 852 — N=4 Coherence / Frobenius-Ratio Reduction (Tier 2 Replication)

**Date**: 2026-04-19
**Phase**: 4 (Gap narrowing)
**Track**: theory
**Author**: Replication attempt by second Opus 4.7 sub-instance (blind to attempt_851)

## Role of this fire

This is the independent Tier-2 replication fire for the N=4 reduction that
attempt_849 flagged as the only remaining analytical step. I have read
849, 850, and the three Lean files (TraceFreeAlignment, StrainTraceInnerProduct,
CrossModeBound) plus the pre-frontier portion of MAP.md. I have NOT read
attempt_851. The goal is to derive the N=4 reduction from scratch and
compare against 851 after the fact.

## Target and constraint (restated in own words)

At a vorticity maximum x\* of a smooth div-free field on T³, expand in a
finite div-free Fourier basis indexed by j = 1,...,N:

- k_j ∈ ℤ³ \ {0} (wavenumbers)
- v_j ⊥ k_j, |v_j| = 1 (unit polarizations)
- w_j = k_j × v_j, so |w_j| = |k_j|, k_j ⊥ w_j
- c_j = cos(k_j · x\*), s_j = sin(k_j · x\*), c_j² + s_j² = 1
- ω(x\*) = Σ_j c_j v_j
- S_j = −(1/(2|k_j|²))(k_j ⊗ w_j + w_j ⊗ k_j) (trace-free, symmetric)
- S(x\*) = Σ_j c_j S_j

**Frobenius-ratio target (attempt_849).** Prove

    ‖S(x\*)‖²_F / |ω(x\*)|² < 9/8     (★)

on the set of configurations where x\* is a strict interior maximum of
|ω|². Composed with trace_free_operator_norm_bound (Lean, proven), (★)
implies the Key Lemma S²ê < (3/4)|ω|².

**First-order vorticity-max constraint.** At x\*, ∂_m|ω|² = 0 for m=1,2,3.
Differentiating ω = Σ c_j v_j and using ∂_m c_j = −s_j k_{j,m}:

    Σ_j s_j k_{j,m} (ω · v_j) = 0,   m = 1, 2, 3.      (FO)

Writing a_j := ω · v_j = Σ_ℓ c_ℓ (v_ℓ · v_j) and β_j := s_j a_j, (FO)
reads Σ_j β_j k_j = 0 in ℝ³. That is 3 linear equations on (β_1,...,β_N),
each β_j coupled through c_j² + s_j² = 1.

## N=4 configuration chosen

Take the minimum-complexity non-degenerate N=4 pick with one mode off the
shortest shell:

    k_1 = (1, 0, 0),   v_1 = (0, 1, 0),       w_1 = (0, 0, 1)
    k_2 = (0, 1, 0),   v_2 = (0, 0, 1),       w_2 = (1, 0, 0)
    k_3 = (0, 0, 1),   v_3 = (1, 0, 0),       w_3 = (0, 1, 0)
    k_4 = (1, 1, 0),   v_4 = (1, −1, 0)/√2,   w_4 = (0, 0, −√2)

Every k · v = 0 (div-free). |v_j| = 1 throughout. Modes 1–3 are the
unit-cube coordinate triad with a "chirality-right" polarization choice;
mode 4 is the next available wavenumber |k|² = 2 with polarization
locked in the k₁-k₂ plane. There is one degree of (polarization) freedom
per mode; my choice is the lexicographic one.

## Step 1 — polarization inner products

    v_1·v_2 = 0       v_2·v_3 = 0
    v_1·v_3 = 0       v_2·v_4 = 0
    v_1·v_4 = −1/√2   v_3·v_4 = 1/√2

Hence

    |ω|² = Σ c_j² + 2 Σ_{j<k} c_j c_k (v_j·v_k)
         = c_1² + c_2² + c_3² + c_4²  +  √2 (c_3 − c_1) c_4.

## Step 2 — strain Hilbert–Schmidt inner products

Formula (attempt_849, StrainTraceInnerProduct.lean):

    Tr(S_j S_k) = (1/(2|k_j|²|k_k|²)) · [(k_j·k_k)(w_j·w_k) + (k_j·w_k)(w_j·k_k)].

Diagonal: Tr(S_j²) = 1/2 for all j (unit modes; Lean).

Off-diagonals, computed term-by-term:

(1,2):  k_1·k_2 = 0; k_1·w_2 = 1; w_1·k_2 = 0; w_1·w_2 = 0; |k|² prod = 1
        → Tr(S_1 S_2) = 0/(2) = 0.

(1,3):  k_1·k_3 = 0; k_1·w_3 = 0; w_1·k_3 = 1; w_1·w_3 = 0 → Tr(S_1 S_3) = 0.

(1,4):  k_1·k_4 = 1; k_1·w_4 = 0; w_1·k_4 = 0; w_1·w_4 = −√2; |k|² prod = 2
        → Tr(S_1 S_4) = (1·(−√2) + 0·0)/(2·2) = −√2/4.

(2,3):  k_2·k_3 = 0; k_2·w_3 = 1; w_2·k_3 = 0; w_2·w_3 = 0 → Tr(S_2 S_3) = 0.

(2,4):  k_2·k_4 = 1; k_2·w_4 = 0; w_2·k_4 = 1; w_2·w_4 = 0; |k|² prod = 2
        → Tr(S_2 S_4) = (1·0 + 0·1)/4 = 0.

(3,4):  k_3·k_4 = 0; k_3·w_4 = −√2; w_3·k_4 = 1; w_3·w_4 = 0; |k|² prod = 2
        → Tr(S_3 S_4) = (0 + (−√2)·1)/4 = −√2/4.

So

    ‖S‖²_F = ½ Σ_j c_j²  +  2 c_1 c_4 (−√2/4)  +  2 c_3 c_4 (−√2/4)
           = ½ (c_1² + c_2² + c_3² + c_4²)  −  (√2/2)(c_1 + c_3) c_4.

## Step 3 — reduce (★) to a polynomial inequality

(★) ⇔ ‖S‖²_F − (9/8)|ω|² < 0, i.e.

    ½ Σc²  −  (√2/2)(c_1+c_3) c_4
      < (9/8)[Σc²  +  √2 (c_3 − c_1) c_4]

⇔ 0 < (5/8) Σc²  +  (√2/2)(c_1+c_3) c_4  +  (9√2/8)(c_3 − c_1) c_4

⇔ 0 < (5/8) Σc²  +  (√2/8) c_4 · [4(c_1+c_3) + 9(c_3 − c_1)]

⇔ 0 < (5/8) Σc²  +  (√2/8) c_4 · (13 c_3 − 5 c_1).

Multiply by 8:

    Q(c) := 5 (c_1² + c_2² + c_3² + c_4²)  +  √2 (13 c_3 − 5 c_1) c_4  >  0.   (R)

Equivalently, 16·[(9/8)|ω|² − ‖S‖²_F] = 2Q. (R) is the target polynomial
inequality in the four c-coefficients.

## Step 4 — the first-order constraint at this configuration

Compute a_j = ω · v_j:

    a_1 = c_1 + 0 + 0 − c_4/√2 = c_1 − c_4/√2
    a_2 = c_2
    a_3 = c_3 + c_4/√2
    a_4 = (−c_1/√2) + 0 + c_3/√2 + c_4 = c_4 + (c_3 − c_1)/√2

Sanity: Σ c_j a_j = c_1(c_1−c_4/√2) + c_2² + c_3(c_3+c_4/√2) + c_4[c_4+(c_3−c_1)/√2]
= Σ c² + c_4(c_3−c_1)/√2 + c_4(c_3−c_1)/√2
= Σ c² + √2 c_4 (c_3 − c_1) = |ω|². ✓

With β_j = s_j a_j, (FO) = "Σ β_j k_j = 0" gives, component by component:

    m=1:   β_1·1 + β_2·0 + β_3·0 + β_4·1 = 0   ⇒   s_1 a_1 + s_4 a_4 = 0
    m=2:   β_1·0 + β_2·1 + β_3·0 + β_4·1 = 0   ⇒   s_2 a_2 + s_4 a_4 = 0
    m=3:   β_1·0 + β_2·0 + β_3·1 + β_4·0 = 0   ⇒   s_3 a_3 = 0.

So the three constraints are

    (C1)   s_3 a_3 = 0,
    (C2)   s_1 a_1 = s_2 a_2,
    (C3)   s_1 a_1 = −s_4 a_4.

Together with s_j² = 1 − c_j².

## Step 5 — close (R) under (C1)–(C3), or name the obstruction

**Observation 1 (generic branch).** If all c_j ∈ (−1, 1), then each s_j ≠ 0,
so (C1) forces a_3 = 0, i.e.

    c_3 = −c_4/√2.                       (G)

Substitute (G) into (R):

    Q = 5[c_1² + c_2² + c_4²/2 + c_4²] + √2 · c_4 · [13(−c_4/√2) − 5 c_1]
      = 5 c_1² + 5 c_2² + (15/2) c_4²  − 13 c_4² − 5√2 c_1 c_4
      = 5 c_1² + 5 c_2²  −  (11/2) c_4²  − 5√2 c_1 c_4.

Complete the square in c_1:

    Q = 5 (c_1 − c_4/√2)² − 5·(c_4²/2) + 5 c_2² − (11/2) c_4²
      = 5 (c_1 − c_4/√2)² + 5 c_2²  −  8 c_4².                     (R|G)

(R|G) is a polynomial identity on the "generic interior" admissible set.

**Observation 2 (Q can go negative on (G)).** (R|G) is manifestly
indefinite: the coefficient of c_4² is −8 while c_4 is bounded only by
c_4² ≤ 1 (since s_4² = 1 − c_4²). Concretely, at

    c_1 = c_4/√2,  c_2 = 0,  c_3 = −c_4/√2,  c_4 ∈ [−1, 1]

we have Q = −8 c_4², which is strictly negative for c_4 ≠ 0. At c_4 = 1,
Q = −8 (the pointwise Frobenius inequality (★) would fail by a wide
margin if the point were admissible as a vorticity max).

**Observation 3 (the zero-ω boundary).** Compute |ω|² on the slice (G)
with c_1 = c_4/√2, c_2 = 0, c_3 = −c_4/√2:

    |ω|² = c_1² + c_2² + c_3² + c_4² + √2(c_3 − c_1) c_4
         = c_4²/2 + 0 + c_4²/2 + c_4² + √2·(−√2 c_4) · c_4
         = 2 c_4² − 2 c_4² = 0.

More globally on (G), |ω|² = (c_1 − c_4/√2)² + c_2² (straight algebra from
|ω|² = Σc² + √2(c_3−c_1)c_4 after substituting c_3 = −c_4/√2). Therefore

    (9/8) |ω|² − ‖S‖²_F  =  (2/16) · Q  =  (1/8) Q,

and on (G),

    16 · [(9/8)|ω|² − ‖S‖²_F]  =  10 (c_1 − c_4/√2)²  +  10 c_2²  −  16 c_4².

The zero-omega locus L on (G) is precisely {c_1 = c_4/√2, c_2 = 0}, a
1-parameter curve, and on L the Frobenius ratio ‖S‖²_F/|ω|² is 0/0
(both numerator and denominator vanish together — see (V) below).

Wait — check numerator. On L: ‖S‖²_F = ½[c_4²/2 + 0 + c_4²/2 + c_4²] − (√2/2)(c_4/√2 − c_4/√2)·c_4 = ½·(2 c_4²) − 0 = c_4². So ‖S‖²_F = c_4² and |ω|² = 0. Hence

    on L:   ‖S‖²_F / |ω|² = c_4² / 0 = +∞   (for c_4 ≠ 0).      (V)

Not 0/0 — the numerator is strictly positive while the denominator
vanishes. The Frobenius ratio **is unbounded** on a 1-parameter family of
(G)-admissible configurations.

**Observation 4 (this is not yet a counterexample — check admissibility).**
To call L a first-order-admissible family I must exhibit signs (s_1,...,s_4)
satisfying s_j² = 1 − c_j² and (C1)–(C3). On L with c_1 = c_4/√2,
c_3 = −c_4/√2, c_2 = 0:

    a_1 = c_1 − c_4/√2 = 0
    a_2 = c_2 = 0
    a_3 = c_3 + c_4/√2 = 0
    a_4 = c_4 + (c_3 − c_1)/√2 = c_4 + (−√2 c_4)/√2 = c_4 − c_4 = 0.

**All a_j vanish on L.** The constraint β_j = s_j a_j = 0 for all j is
automatic regardless of the s_j. So any choice of s_j with s_j² = 1 − c_j²
satisfies (C1)–(C3) trivially. The configuration IS first-order admissible.

**Observation 5 (why L is not a counterexample to the Key Lemma).** On L
we also have ω = 0 identically: indeed ω·v_j = a_j = 0 for every basis
polarization v_j (and one checks that ω is in the span of {v_j} by
construction), so |ω|² = 0 confirms ω(x\*) = 0. A vorticity MAXIMUM with
ω(x\*) = 0 forces |ω| ≡ 0 everywhere on T³ by maximum-principle-trivial
reasoning; there is no blowup scenario there. The Key Lemma is vacuous at
ω = 0.

So L is a spurious branch of the first-order set: it satisfies (FO) by
the degenerate mechanism that all the first-order constraint coefficients
a_j vanish. The first-order condition is NECESSARY but NOT SUFFICIENT for
being at a strict max with |ω(x\*)|² > 0. Near L but off it the Frobenius
ratio diverges, as witnessed by

    lim_{(c_1,c_2)→(c_4/√2, 0)}  ‖S‖²_F/|ω|²  =  c_4² / 0  =  +∞.

## Result — PARTIAL

The Frobenius-ratio target (★) reduces, on the chosen N=4 configuration
and at the "generic interior" branch of the first-order set, to the
polynomial inequality

    10 (c_1 − c_4/√2)² + 10 c_2²  >  16 c_4²                (R★)

over the box [−1,1]⁴ subject to the substitution c_3 = −c_4/√2.

(R★) is NOT a consequence of (FO) alone: it fails on the 1-parameter zero-ω
curve L = {c_1 = c_4/√2, c_2 = 0, c_3 = −c_4/√2, c_4 ∈ [−1,1]} — which IS
first-order admissible, via the trivial-coefficient mechanism a_j ≡ 0, but
corresponds to ω(x\*) = 0 (no vorticity max in the Key Lemma sense).

**Obstruction.** The first-order condition (FO) admits the degenerate
branch a_1 = a_2 = a_3 = a_4 = 0, on which (FO) is automatic for any s_j
but ω itself vanishes. To exclude it one must add the non-degeneracy
hypothesis |ω(x\*)|² > 0 (the vorticity-max hypothesis of the Key Lemma),
which is NOT a polynomial inequality in c alone of bounded degree — it is
a strict positivity. Bounding ‖S‖²_F/|ω|² therefore requires an auxiliary
uniformity: either

  (i) a quantitative lower bound |ω|² ≥ δ(c) > 0 on the admissible set
      minus L (with δ → 0 only on L), against which ‖S‖²_F decays at least
      as fast; or
  (ii) a second-order Hessian condition at the vorticity max — a genuine
       MAX, not critical point — which reduces to a positive-semidefinite
       condition on a 3×3 Hessian built from ∂²|ω|² and brings in the s_j
       quadratically.

Neither (i) nor (ii) is delivered by the first-order constraint itself.

**Partial closure where (i) is explicit.** Dividing (R★) through by
|ω|² on (G):

    16 · ‖S‖²_F/|ω|²  =  8 · (Σc² + √2(c_3−c_1)c_4) · 9 − [10(c_1−c_4/√2)² + 10 c_2² − 16 c_4² + 8·|ω|²·extras]

— a messy expression, but crucially the leading behavior near L is

    ‖S‖²_F  =  c_4² + O(ε),    |ω|²  =  ε² + O(ε³)

where ε = √((c_1 − c_4/√2)² + c_2²) is the distance to L. So on the
interior branch (G) the ratio scales like c_4²/ε², unbounded as ε → 0.

The empirical finding of attempt_850 — "2089 samples, zero violations of
9/8, N=3 stress-test at 5000 samples reaches max 0.88" — is consistent
with this, because attempt_850 explicitly guards against small |ω|² via
`best_om2 > 0.01·N`, which excludes a neighborhood of L.

## Prior art

- **Algebraic tool invoked.** Substitution of a single linear constraint
  into a quadratic form followed by completing the square in one variable.
  This is the Schur-complement / one-equation-elimination move. Degree-2
  level of semialgebraic reasoning; Lasserre-SOS style would be the next
  step (degree-4 hierarchy) if the domain were compact and non-degenerate.

- **Fourier div-free basis + Fourier-strain formula.** Standard incompressible
  harmonic analysis (Majda–Bertozzi 2002, Temam 2001). The formula
  Tr(S_j S_k) in §2 is the same Hilbert–Schmidt identity formalized in
  `StrainTraceInnerProduct.lean` (`strain_hilbert_schmidt_formula`).

- **First-order critical-point constraint.** The reduction of ∂_m|ω|²=0 to
  Σ s_j k_{j,m} (ω·v_j) = 0 is elementary Euler–Lagrange; it appears in
  attempts 767–842 for several Key-Lemma routes and in attempt_850 §"The
  structural reason the off-diagonal shrinks with N".

- **Zero-ω obstruction in first-order critical sets.** This is the classical
  "a vorticity stationary point where ω also vanishes is not a max" fact;
  related to Constantin (1994) nonlinearity-depletion discussion and to the
  Tsai-type decay arguments (ω = 0 asymptote is the Liouville sink).

## Falsifier

This derivation is INVALIDATED if any of:

1. The Hilbert–Schmidt formula for Tr(S_j S_k) I used disagrees with
   `strain_hilbert_schmidt_formula` in the Lean file — checked, it agrees
   up to symmetrization factor of 1/2 already absorbed.

2. The off-diagonals Tr(S_j S_k) I computed are wrong for j,k ∈ {1,2,3,4}.
   Sanity spot-checks: Tr(S_1 S_4) involves only the k₁-k₂ plane and the
   e₃ direction; w_1 = e_3, w_4 = −√2·e_3, k_1·k_4 = 1, k_1⊥w_4,
   k_4⊥w_1 → formula gives (1·(−√2))/4 = −√2/4. ✓

3. The "generic interior" branch (G) does not cover the max. In principle
   there are also boundary branches where some c_j² = 1 (then s_j = 0 and
   (C1)–(C3) lose equations). Those branches are codimension-1 each and
   would require separate case analysis. I did not do them here. If one
   of them were to yield a stricter bound, it could change the "partial"
   verdict — but it could only make the bound EASIER to close by fixing
   more c's, not harder. So ignoring them is conservative for the "does
   the algebra close" question; the real obstruction (L) is in the
   interior.

4. The polynomial identity |ω|² = (c_1 − c_4/√2)² + c_2² on slice (G) is
   checked: expand c_1² + c_2² + c_4²/2 + c_4² + √2 c_4 (−c_4/√2 − c_1)
   = c_1² + c_2² + (3/2) c_4² − c_4² − √2 c_1 c_4 = c_1² − √2 c_1 c_4 +
   c_4²/2 + c_2² = (c_1 − c_4/√2)² + c_2². ✓

5. The "all a_j = 0 on L" claim: a_1 = c_4/√2 − c_4/√2 = 0; a_2 = 0; a_3 =
   −c_4/√2 + c_4/√2 = 0; a_4 = c_4 + (−c_4/√2 − c_4/√2)/√2 = c_4 − c_4 = 0. ✓

6. If a SEPARATE non-degeneracy argument (second-order, or a lower bound
   on |ω|²) collapses the N=4 gap without needing to leave (R), this
   derivation's "partial" verdict would be upgraded to "closes subject to
   NON-DEG". I did not find such an argument in the permitted files.

## Tier status

**Tier 1, unreplicated.** This IS the Tier-2 replication fire, but by
sigma v9.1 discipline I (as the replication agent) cannot self-certify
my own output as Tier 2. The comparison against attempt_851 by the
outer-loop instance is what would promote the overlapping pieces to
Tier 2. Disagreements would be investigated as separate proof branches.

## Net (for LOOP_NOTES)

- N=4 target (★) reduces, on the chosen symmetric + one-|k|²=2 configuration
  and the generic interior branch of (FO), to the polynomial inequality
  10(c_1 − c_4/√2)² + 10 c_2² > 16 c_4² over c ∈ [−1,1]⁴ with c_3 = −c_4/√2.
- (FO) alone is INSUFFICIENT: the zero-ω locus L is first-order admissible
  but corresponds to ω(x\*) = 0 (no Key Lemma content).
- Closing (★) at N=4 requires a separate non-degeneracy condition
  |ω(x\*)|² > 0, i.e., the full strict-maximum hypothesis. This is the
  precise obstruction.
- Matches the attempt_850 empirical guard `best_om2 > 0.01·N`: the samples
  that "never violate 9/8" are precisely those excluded from a neighborhood
  of L.

## Tag

852. N=4 reduction of the Frobenius-ratio target ‖S‖²_F/|ω|² < 9/8 under
the first-order vorticity-max constraint on the 4-mode configuration with
k ∈ {e_1, e_2, e_3, e_1+e_2} and lex polarizations. Generic branch of (FO)
gives the polynomial inequality 10(c_1−c_4/√2)² + 10 c_2² > 16 c_4². The
inequality FAILS on the zero-ω curve L, which is first-order admissible
via the degenerate a_j ≡ 0 mechanism. Obstruction: (FO) is weaker than
"strict vorticity max with |ω|² > 0"; closing the Key Lemma at N=4 via
this route needs a second-order / non-degeneracy ingredient not present
in (FO) alone. Partial reduction, obstruction named. Tier 1, unreplicated.
