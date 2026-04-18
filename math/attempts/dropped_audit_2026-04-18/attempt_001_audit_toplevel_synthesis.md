# Attempt 001 — Claim-Backing Audit: math/ top-level synthesis docs

**Date**: 2026-04-15
**Phase**: Audit (first math fire)
**Scope**: math/CLAY_PROBLEMS.md (134L), SEVEN_WALLS.md (153L),
QUANTIFIED_GAPS.md (152L), UNDERGROUND_CONNECTIONS.md (160L, L1-80
sampled). 599L total top-level.
**Standard**: the math/ns_blowup/attempts/attempt_849 file itself, but
turned reflexively on the synthesis layer above it.

## Executive verdict — the gold standard has version drift

The top-level synthesis docs show the **same cross-document
inconsistency pattern** found in biology/evolution/ synthesis notes
during the non-math audit (Fires 48-51). This is not surprising —
parallel synthesis documents drift against each other as each is
updated in isolation. But it is instructive: **the math/ layer that
set the claim-backing standard exhibits the same version-drift
failure mode that the non-math audit flagged.**

**🔴 RED count**: 2
**🟡 YELLOW count**: 4
**🟢 GREEN count**: 9

## RED findings

### R1 — Sorry count contradiction within CLAY_PROBLEMS.md

The document contains an explicit per-problem sorry count table
(L5-16) and a summary Statistics section (L104-119). These don't
match.

**Table sum of sorry counts**:
- Poincaré: 9
- Yang-Mills: 18
- Navier-Stokes: 41
- Hodge: 4
- Riemann: 7
- BSD: 1
- P vs NP: 6
- Liouville: 4
- Prime Numbers: 0
- Philosophy/mind: 2
- Physics/info: 1
- **Sum: 93**

**Statistics section claim** (L113): "Remaining sorry: 6 (all in NS Blowup.lean = the open problem)"

**6 ≠ 93.** The L19 footnote says "math subtotal 755 thms+lemmas, 90
sorry" — still not 6. The "6 remaining sorry" claim is internally
contradicted by the document's own table.

**Required fix**: either (a) the "6 remaining sorry" claim is wrong
and should be updated to reflect the 93-sorry total, or (b) the
per-problem table is stale and should be refreshed, or (c) "6
remaining sorry" refers to a specific goal (the NS Blowup.lean chained
proof) and should be clarified: "6 sorry in the chained NS blowup
proof; 93 total across all authored Lean in the math corpus."

Without the clarification, readers cannot tell whether the work is
closer to done than the data supports.

### R2 — "Poincaré SOLVED" with 9 sorry in the formalization

L7 marks Poincaré as "SOLVED" with "64 / 9" in the "Lean (thms / sorry)"
column — meaning 9 sorry tactics in the Poincaré Lean formalization.

"SOLVED" and "9 sorry" are contradictory at the Lean level. Either:
(a) the mathematical proof is solved (Perelman's proof, independently
rediscovered here) but the formalization has 9 gaps → label should
be "SOLVED (informal), 9 Lean gaps" or "SOLVED — formalization
9/64 incomplete"; or
(b) the formalization is complete and "9 sorry" is a stale count.

The SEVEN_WALLS.md L146 "Poincaré: ✅ SOLVED (12/12 blind), Step 9 closed"
suggests (a) — the informal proof is done but the Lean isn't yet 0
sorry. This is important because "SOLVED" without qualifier conveys
more finality than the Lean state supports.

**Required fix**: add "(informal proof)" or "(formalization
incomplete)" qualifier to the SOLVED label when per-problem sorry > 0.

## YELLOW findings

| # | Location | Claim | Source gap |
|---|----------|-------|------------|
| Y1 | CLAY_PROBLEMS L3 vs L108-110 | "824 Lean theorems+lemmas across 129 files (non-lake)" (top) vs "Total Lean theorems: 862" + "Lean files: 118 across 12 domains" + "Math Lean files: 105" (statistics) | Three different totals for theorems (824 / 862) and files (129 / 118 / 105). Reconcile the numbers or date each as a snapshot. |
| Y2 | CLAY_PROBLEMS L11 vs SEVEN_WALLS L151 | RH numerical certificates: CLAY says "Turing: 689 zeros on critical line, T≤1000" and "Li: λ_n > 0 for n ≤ 1000". SEVEN_WALLS says "668 zeros T=1000, Li n≤200" | Cross-document numerical mismatch: 689 vs 668 zeros; Li 1000 vs 200. Both documents cite RH certificates but give different numbers. |
| Y3 | CLAY_PROBLEMS L9/L43 vs QUANTIFIED_GAPS L37 | NS c(4) bound: "c(4) ≤ 0.561 rigorous" (CLAY + SEVEN_WALLS L148) vs "c(4) ≤ 0.5608" (QUANTIFIED_GAPS) | Precision drift across documents. 0.561 is a rounding of 0.5608. Standardize to the tighter bound. |
| Y4 | CLAY_PROBLEMS L19 | "math subtotal 755 thms+lemmas, 90 sorry" | Doesn't reconcile with the per-problem table sum (485 NS + 74 YM + 64 Poincaré + 20 Hodge + 19 RH + 5 BSD + 78 P vs NP + 7 Liouville + 3 Primes = 755 thms — this matches) AND (41 NS + 18 YM + 9 Poincaré + 4 Hodge + 7 RH + 1 BSD + 6 P vs NP + 4 Liouville + 0 Primes = 90 sorry — this matches). **Actually this DOES reconcile.** But then L113's "6 remaining sorry" definitely doesn't fit either summary. Y4 resolves but R1 stands. |

## GREEN findings

- **G1** **5-wall taxonomy** in SEVEN_WALLS.md: Quantitative /
  Structural / Conceptual / Existential / Meta. Per-type systematic-
  approach effectiveness percentage (100% → 80% → 40% → 20% → 40% →
  10% across Type 0-5). Empirically-grounded per-wall performance
  reporting. **This is the math layer's structural equivalent to
  sigma-method Phase 0 shape-check.**
- **G2** QUANTIFIED_GAPS.md **"the gap IS a number" principle**
  applied across all 7 problems with per-problem number identified:
  YM → GC(β), NS → c(N), RH → Λ (de Bruijn-Newman), BSD → |Ш| /
  regulator agreement digits, Hodge → rank(Hdg²) - rank(Alg²), P vs
  NP → exponent c, Poincaré → κ noncollapsing constant. Each
  problem's central obstruction concretized.
- **G3** UNDERGROUND_CONNECTIONS.md **transfer map** with concrete
  actions (Poincaré→NS via W-entropy analogy named "W_NS(u, f, τ) =
  ∫[τ(|ω|² + |∇f|²) + f - 3] (4πτ)^{-3/2} e^{-f} dx"; YM→RH via
  spectral gap and Bakry-Émery criterion). Cross-problem mathematical
  transfer articulated at mechanism level, not just "they're related."
- **G4** SEVEN_WALLS.md **per-problem wall type** labeled in the
  final Score table: Poincaré SOLVED (W-entropy), Yang-Mills
  Quantitative (GC(β) > 0), NS Quantitative (c(N) = 0.3616 peak),
  Hodge Existential (Weil classes g ≥ 6), BSD Structural (rank-2
  pair missing), RH Conceptual (Li ⟺ RH, no weak cert), P vs NP
  Meta (Liu-Pass bridge). Each cell specific.
- **G5** **Monotone-quantities-win pattern** (SEVEN_WALLS L81-91):
  every solved/near-solved problem has a monotone functional
  (W-entropy, GC, enstrophy); unsolved problems lack one. **Cross-
  problem observation with falsifiable prediction**: if a new
  monotone quantity is found for RH/BSD/P-vs-NP, those problems
  should yield.
- **G6** **Thermodynamic-analogy pattern** across Poincaré/YM/RH
  (SEVEN_WALLS L92-98): "couple the mathematical object to a 'heat
  flow' and find the free energy." Unifies 3 problems under a shared
  technique — testable claim about which problems yield to which
  methods.
- **G7** **Group-symmetry-reduces-to-finite-computation pattern**
  (SEVEN_WALLS L100-108): YM SU(2)/Z₂, Hodge Mumford-Tate, Poincaré
  Thurston 8 model geometries all reduce to finite checks via group
  structure. "When there's no group structure, the method struggles
  — RH, P vs NP." Predicts which problems systematic approach can
  crack.
- **G8** **"One genius insight" bottleneck** honestly labeled per
  problem (SEVEN_WALLS L110-119): Poincaré's W-entropy derived
  retrospectively, YM's GC found by systematic approach, NS's
  Liouville-type estimate NOT yet found, RH's ??? (completely
  unknown), BSD's rank-2 construction (not imagined), Hodge's
  motivic t-structure (conjectured not built), P vs NP's
  barrier-avoiding technique (not invented). **Confirmation-bias-
  audit-compliant per-problem labeling.**
- **G9** SEVEN_WALLS.md **"What the systematic approach IS / does
  NOT"** section (L121-140): explicit scope statement. "It does NOT:
  replace mathematical genius, generate fundamentally new proof
  techniques, prove theorems by computation alone (except for
  quantitative walls). It DOES: find the gap faster, identify where
  genius is needed, build infrastructure, verify genius when it
  arrives." **Scope discipline matching the non-math audit's
  persistent_organisms/ PROBLEM.md standard** (Fire 53).

## Recommended fixes (ordered)

1. **[P0]** R1 — reconcile "6 remaining sorry" claim against the
   93-sorry table sum. Either clarify ("6 sorry in NS Blowup chained
   proof, 93 total across corpus"), or fix whichever is stale.
2. **[P0]** R2 — add "(informal)" or "(formalization incomplete)"
   qualifier to "Poincaré SOLVED" when 9 sorry remain in the Lean.
3. **[P1]** Y1 — reconcile 3 different theorem/file totals in
   CLAY_PROBLEMS (824/862, 129/118/105). Date each snapshot.
4. **[P2]** Y2 — fix RH numerical mismatch across documents (689 vs
   668 zeros; Li 1000 vs 200).
5. **[P2]** Y3 — standardize NS c(4) bound across documents
   (0.561 vs 0.5608).

## Non-audit observations

- **The gold standard has the same version-drift failure as non-math
  syntheses.** Biology/evolution/ synthesis notes (Fires 48-51)
  showed monotonic status-list improvement across 5 files (0/6 ✅ →
  5/6 ✅). The math top-level docs show a parallel pattern — each
  doc was updated independently, producing cross-document
  inconsistencies. **The audit-loop methodology surfaces the same
  failure mode regardless of domain.**
- **SEVEN_WALLS.md's "one genius insight bottleneck"** is the most
  honest assessment in the corpus. Most documents claim their
  method is moving the needle; this one says "the systematic
  approach can identify the NEED for but cannot GENERATE the
  genius insight." Confirmation-bias-audit-compliant at the method-
  claim level.
- **QUANTIFIED_GAPS.md's "gap is a NUMBER" principle** is the
  sharpest claim-backing discipline in the math corpus. Every
  problem gets a specific number as its gap, with current value
  and target. This should be the template for cross-problem
  progress reporting — including for non-math problems once they
  reach Phase 4.
- **The transfer map** in UNDERGROUND_CONNECTIONS.md is a concrete
  falsifiable claim: if the W-entropy analogy gives W_NS with the
  specified form, it either is or isn't monotone under NS flow.
  This is math-standard cross-problem prediction.
- **Reflexive audit observation**: the systematic approach met the
  discipline it set for non-math in three of its own top-level
  claims (5-wall taxonomy, quantified-gaps, transfer map), and
  failed the discipline in the internal-consistency check (sorry
  counts, theorem totals, numerical certificates). This is the
  expected pattern: synthesis-layer strong, record-keeping
  version-drifted.

## Tag

001 (math/ top-level synthesis). 599L sampled. **2 🔴** (sorry
count 6 vs 93 contradiction in CLAY_PROBLEMS; "Poincaré SOLVED"
with 9 sorry — label vs formalization state mismatch). 4 🟡
(824/862 theorem total / 129/118/105 file count disagreement; RH
zeros 689 vs 668 and Li 1000 vs 200 cross-doc; NS c(4) 0.561 vs
0.5608 precision drift; math subtotal 755 thms / 90 sorry). **9 🟢**:
5-wall taxonomy with per-type systematic-approach effectiveness;
"gap is a NUMBER" principle applied across 7 problems; cross-problem
transfer map with concrete actions (W_NS formula, Langevin-to-
Selberg); per-problem wall-type labels; monotone-quantities-win
pattern; thermodynamic-analogy pattern; group-symmetry-reduces-to-
finite-computation; **"one genius insight" bottleneck per-problem
honesty** (confirmation-bias-audit compliant); **"what the method
IS / does NOT"** explicit scope statement. **Reflexive observation**:
the gold-standard reference exhibits the same version-drift failure
mode its own standard flagged in non-math syntheses (Fires 48-51).
**Next fire**: ns_blowup/ (gold standard reference; audit the standard
itself — attempts 001-019 + Lean sorry count + named-theorem
verification for attempt_849 and FinalKeyLemma.lean).
