# Math Claim-Backing Audit Log

> Started 2026-04-15. Running via `/loop 15m` (cron b69bfea8).
> Audits math/ subdirs using the same structural methodology applied
> to non-math (55-fire campaign closed 2026-04-15; case study at
> `~/sigma/case_studies/claim_backing_audit_61_fires_001.md`).

## The standard shifts from non-math

For non-math, the question was "does the claim cite a source?" For
math, it's "does the claim hold up AS math?"

### New verification axes

1. **Named-theorem verification**: grep for claimed Lean theorems in
   their cited files. (Same method as Fire 41 for t1dm Lean.)
2. **Sorry count**: count actual `sorry` tactics in authored Lean
   files (excluding `.lake/packages/`).
3. **Internal consistency**: cross-document numbers must agree
   (theorem counts, sorry counts, certificate values).
4. **Proof-strategy honesty**: "PROVEN" in synthesis docs must match
   actual Lean state (0 sorry in chained goal, or clearly labeled as
   conditional/partial).
5. **Published-math accuracy**: specific named theorems cited from
   literature (Perelman W-entropy, Liu-Pass 2020, Williams 2011, etc.)
   must be real and correctly attributed.

### The audit's reflexive question

**Does the gold-standard reference meet its own gold standard?**
Since all non-math audits used `math/ns_blowup/attempts/attempt_849_
frobenius_ratio_gap.md` as the standard, the math audit has to test
whether math/ actually meets the standard it set.

## Severity ladder

- 🔴 RED: internal contradiction, claimed theorem doesn't exist,
  sorry in a chained "proven" step, misattributed published result
- 🟡 YELLOW: cross-document version drift, number precision mismatch,
  uncited published theorem, "proven" weaker than asserted
- 🟢 GREEN: internal consistency, Lean theorem verified present,
  sorry count matches claim, well-attributed published result

## Fire log

| # | Date | Scope | Result |
|---|------|-------|--------|
| 1 | 2026-04-15 | math/ top-level synthesis (CLAY_PROBLEMS + SEVEN_WALLS + QUANTIFIED_GAPS + UNDERGROUND_CONNECTIONS L1-80) | See `attempts/attempt_001_audit_toplevel_synthesis.md`. **2 🔴** (internal sorry-count contradiction in CLAY_PROBLEMS.md L113-114 "Remaining sorry: 6" vs table sum 86 sorry across 7 problems; "Poincaré SOLVED" with 9 sorry in table — contradictory labels). **4 🟡** (CLAY_PROBLEMS top-of-file "824 thms / 129 files" vs Statistics "862 thms / 118 files" vs "math Lean files: 105" — three inconsistent totals; cross-doc RH numerics mismatch: CLAY "Turing 689 zeros, Li n≤1000" vs SEVEN_WALLS "668 zeros, Li n≤200"; NS c(4) precision drift: "0.561" vs "0.5608"; math subtotal "755 thms+lemmas, 90 sorry" doesn't reconcile with per-problem table). **9 🟢**: 5-wall taxonomy (Quantitative/Structural/Conceptual/Existential/Meta) with per-type systematic-approach effectiveness %; "The gap is a NUMBER" principle with per-problem number identified; **cross-problem transfer map** (Poincaré→NS via W-entropy analogy; YM→RH via spectral gap; YM→Selberg λ₁ transfer concrete action); per-problem wall type labeled; monotone-quantities-win pattern (Poincaré W, YM GC, NS enstrophy); thermodynamic-analogy pattern identified across 3 problems; group-symmetry-reduces-to-finite-computation pattern; "one genius insight bottleneck" honest per-problem labeling; "what the method IS vs does NOT" explicit scope statement (L121-140). |

## Queue

### math/ top-level docs (1 of 1 batches done)
- ✅ CLAY_PROBLEMS.md + SEVEN_WALLS.md + QUANTIFIED_GAPS.md +
  UNDERGROUND_CONNECTIONS.md (L1-80)

### math/ subdirs (0 of 9 done)
- [ ] ns_blowup/ (gold standard reference — audit first)
  - attempts (19 files)
  - Lean (~50 authored files, check sorry count)
  - cross-refs: attempt_849 used as non-math audit standard
- [ ] yang_mills/ (largest — 76 attempts + 23 Lean)
- [ ] riemann_hypothesis/ (10 attempts + 5 Lean)
- [ ] liouville_conjecture/ (10 attempts + 5 Lean)
- [ ] hodge_conjecture/ (9 attempts + 5 Lean)
- [ ] poincare_conjecture/ (8 attempts + 8 Lean) — SOLVED status
- [ ] birch_swinnerton_dyer/ (4 attempts + 2 Lean)
- [ ] p_vs_np/ (3 attempts + 14 Lean)
- [ ] prime_numbers/ (0 attempts + 1 Lean) — Phase 1 stub

### Cross-cutting verification
- [ ] Sorry count across all authored Lean files (exclude .lake/)
- [ ] Theorem/file count reconciliation (CLAY_PROBLEMS has 3 different totals)
- [ ] Named-theorem grep verification for 7 synthesis-cited theorems
  (SurgerySurvival, WeakStrongCoupling, TannakianReformulation,
  RankTwoStructure, CertificateEquivalence, MetaComplexity,
  FinalKeyLemma)
- [ ] Published-theorem attribution check (Perelman, Liu-Pass,
  Williams, OS78, Polymath 15)
