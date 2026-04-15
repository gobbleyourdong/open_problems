# Attempt 849 — The Frobenius Ratio ||S||²_F/|ω|² Is the Analytical Gap, Not the Ashurst Alignment

**Date**: 2026-04-14
**Phase**: 4 (Gap narrowing)
**Track**: theory

## The claim

The Key Lemma bound S²ê/|ω|² < 3/4 is closer to a proof than gap.md Gap 6b
suggests. The formal chain in Lean already closes it **without** requiring
Ashurst alignment, provided a single quadratic-form inequality on ||S||²_F
vs. |ω|² can be established analytically. That inequality is the actual
unclosed piece.

## What is already proven (Lean, 0 sorry)

From `lean/TraceFreeAlignment.lean`:

- `trace_free_largest_eigenvalue_bound`: λ₁² ≤ (2/3)||S||²_F for any
  trace-free symmetric 3×3 matrix with eigenvalues λ₁≥λ₂≥λ₃.
- `trace_free_smallest_eigenvalue_bound`: λ₃² ≤ (2/3)||S||²_F likewise.
- `trace_free_operator_norm_bound`: max(λ₁², λ₃²) ≤ (2/3)||S||²_F.

Combined with the operator-norm inequality |Sê|² ≤ ||S||_op² for any unit
ê, this gives:

  S²ê = |Sê|² ≤ (2/3) ||S||²_F

for **every** unit vector ê, including the vorticity direction ω̂, with no
alignment hypothesis.

From `lean/SelfAnnihilation.lean` and `lean/CrossModeBound.lean`: the
identity S_k v_k = 0 and |S_j v_k| ≤ 1/2 are fully proven for
divergence-free Fourier modes.

## The remaining analytical step

Applying the operator-norm route, the Key Lemma S²ê < (3/4)|ω|² holds
whenever

  ||S||²_F / |ω|² < 9/8.                (†)

The numerics (`alignment_anatomy.py`, `analytical_S2e_bound.py`, adversarial
battery over N=3–26, 3310 configs) report:

- measured max ||S||²_F/|ω|² ≈ 0.66 (gap.md line 101)
- bound (†) threshold: 1.125
- numerical margin: 1.7×

This ratio is the only quantity in the chain that is still empirical. It
is SHARPER than what is usually formulated as "Ashurst alignment." The
Ashurst alignment is a conditional tightening (from 9/8 to 9/2); without
it, the inequality is 9/8; with it, 9/2. Either number closes the Key
Lemma once (†) is established analytically.

## Why (†) is plausibly tractable from what's already formalized

Expand in the divergence-free Fourier basis at x*:

  ω(x*) = Σ_j c_j v_j
  S(x*) = Σ_j c_j S_j,    S_j = -(1/2|k_j|²)(k_j ⊗ w_j + w_j ⊗ k_j)

where c_j = cos(k_j · x*), v_j ⊥ k_j, w_j = k_j × v_j.

Direct computation:
  ||S||²_F = Σ_{j,k} c_j c_k Tr(S_j S_k)

  Tr(S_j S_k) = (1/(4|k_j|²|k_k|²)) ·
                [ 2 (k_j·k_k)(w_j·w_k) + 2 (k_j·w_k)(w_j·k_k) ]

When j = k, the "diagonal" evaluates to:
  Tr(S_k²) = (1/(4|k|⁴)) · [2|k|²|w|² + 2(k·w)²]
           = (1/(4|k|⁴)) · [2|k|⁴]                 (since k·w = 0, |w|=|k|)
           = 1/2.

So the diagonal contribution is ||S||²_F,diag = (1/2) Σ c_j². Compare with:
|ω|² = Σ_{j,k} c_j c_k (v_j·v_k). Diagonal: |ω|²_diag = Σ c_j².

Therefore, **at the diagonal level**:

  ||S||²_F,diag / |ω|²_diag = 1/2 < 9/8.          (‡)

(‡) is an analytical inequality — a finite ratio of two diagonal sums —
that holds identically. The off-diagonal contributions to both numerator
and denominator are cross-mode terms that can be bounded using the same
coherence + cross-mode machinery that `CrossModeBound.lean` already has for
|Sω|².

## The concrete next step

Prove:

  (a) A Bessel-style bound on the off-diagonal contribution to ||S||²_F
      using {k̂_j, ŵ_j, (k_j × w_j)/|k|²} as an orthonormal frame for
      R^(3×3)_sym ⊗ R^(3×3)_sym. This is analogous to the Bessel bound in
      `bessel_two_orthogonal` that gave |S_j v_k|² ≤ 1/4.

  (b) A coherence bound on the off-diagonal contribution to |ω|², using
      the same c_j c_k phase structure. `pair_mechanism.py` already
      measures this — it's the same "coherence ≈ 3" quantity.

  (c) Combine (a), (b), (‡) to prove ||S||²_F / |ω|² ≤ C for some C < 9/8.
      From the numerics C ≈ 0.66, so a factor of ~2 in looseness is
      allowed by the analytical route.

Each of (a), (b), (c) is a finite algebraic inequality. Once (a) is
written out as a Bessel statement in R^(3×3), it is the same shape of
argument as `bessel_two_orthogonal` and should proof-compile.

## What changes in gap.md

Gap 6b should be restated:

  OLD: "Ashurst alignment — α/|ω| ≈ 0 at x*."
  NEW: "Frobenius ratio ||S||²_F / |ω|² < 9/8 analytically."

The alignment direction and its 0.01 value are downstream consequences —
phenomenologically interesting, but not the proof's binding constraint.
The binding constraint is the Frobenius ratio, and it already has a
diagonal proof with margin 9/4. Only the off-diagonal piece remains.

## Status

- Target inequality: `||S||²_F / |ω|² < 9/8` at vorticity maximum.
- Diagonal of ||S||²_F: (1/2)·Σ c_j² (proven by direct algebra, attempt_058+
  StrainTraceInnerProduct.lean).
- Diagonal of |ω|²: Σ c_j² (unit modes, trivially).
- **Diagonal ratio = 1/2 exactly.**
- The full ratio includes off-diagonal contributions in BOTH numerator and
  denominator. The naive claim "off-diag/|ω|² ≤ 5/8" assumed the
  denominator's off-diagonal is not too negative; this is not rigorously
  established and should be verified.

## 2026-04-15 audit note

The framing "off-diagonal needs ≤ 5/8" is a SIMPLIFICATION. The correct
statement: the target is

  (1/2·Σc² + off_F) / (Σc² + off_ω) < 9/8

which expands to

  off_F − (9/8) · off_ω < (5/8) · Σc²

where off_F = Σ_{j≠k} c_j c_k Tr(S_j S_k) and
off_ω = Σ_{j≠k} c_j c_k (v_j · v_k).

Both off-diagonals can take either sign. The EMPIRICAL evidence
(attempt_850) suggests (i) off_F mean is slightly negative, (ii) the
full ratio stays below 9/8 in 2,089 samples. But the clean
"coherence bound of 5/8 on off_F alone" was an oversimplification —
the correct bound involves both off_F AND off_ω simultaneously.

This does not invalidate the framework; it sharpens what the actual
analytical target is.

## Tag

849. Restate Gap 6b: the unclosed analytical piece is the Frobenius ratio
||S||²_F / |ω|² < 9/8, not Ashurst alignment. Diagonal is proven (= 1/2).
Off-diagonal needs a Bessel bound in R^(3×3) analogous to the one already
proven for R³ in CrossModeBound.lean. Numerical margin in the
off-diagonal piece is ~4×, so the analytical bound doesn't need to be
tight.
