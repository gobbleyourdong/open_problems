# Attempt 848: Formalizing the c(4) Certificate + Weakened Key Lemma Chain

## Date: 2026-04-09

## Inputs from the numerical track

Three new results required formalization:

1. **Rigorous c(4) certificate** (`certs/c4_rigorous_cert.md`): for the
   worst-case k-quadruple `{[-1,0,0], [-1,1,1], [1,0,1], [1,1,1]}`,
   the maximum S²ê/|ω|² over polarization angles and optimal sign patterns
   is rigorously bounded by **0.561 < 0.750** via per-sign dominance grid
   with Lipschitz correction.

2. **T ≤ 0 hypothesis refuted** (`attempts/t_sign_verification.md`):
   the N=4 worst case has T_total = +1.972 > 0. The existing chain in
   `SingleModeOrthogonality.lean` that assumes T ≤ 0 pointwise cannot
   activate at the worst case.

3. **Pointwise monotone decrease NOT verified** (`attempts/monotone_decrease_verdict.md`):
   c(9) and c(11) show apparent increases (likely measurement artifacts from
   fewer k-tuples sampled, but not rigorously excluded). Average trend is
   clearly decreasing: c(4)=0.362, c(13)=0.170 (-53%).

## Theoretical consequence

The Key Lemma chain must be reformulated:

| Old (refuted) | New (working) |
|---------------|---------------|
| c(4) < 3/4 (conditional) | c(4) ≤ 0.561 < 3/4 (rigorous via grid+Lipschitz) |
| c(N+1) ≤ c(N) pointwise | sup_{N ≥ 4} c(N) ≤ C < 3/4 for some bound C |
| T ≤ 0 at vertex max | T has no universal sign; use direct eigenvalue path |

The correct reformulation: `bounded supremum` instead of `pointwise monotone`.
This is weaker and still closes the Key Lemma for all N ≥ 4.

## Lean changes required

1. **N4WorstCase.lean**: add axiom `c4_certified : c(4) ≤ 0.561` from the
   rigorous certificate.

2. **MonotoneDecrease.lean**: replace `complete_key_lemma_conditional` which
   requires pointwise monotone decrease with a version requiring only
   bounded supremum. The induction becomes a case split on N=2,3,4 and
   a bound-lookup for N ≥ 5.

3. **ProofChain.lean**: add a top-level theorem assembling the proven
   c(2), c(3), c(4) bounds + the conjectural supremum bound → Key Lemma
   for all N ≥ 2.

## Status

All three are formalizable with the existing infrastructure.
The framework closes once the numerical certificates are axiomatized.

The ONE remaining gap: prove `sup_{N ≥ 5} c(N) ≤ 0.362` (or any value < 3/4).
Data strongly supports this but it's not yet rigorous for N ≥ 5.
For N=5 through N=13, the vertex method gives empirical values well below 0.362.
For N ≥ 14: asymptotic argument needed (c(N) → 0).
