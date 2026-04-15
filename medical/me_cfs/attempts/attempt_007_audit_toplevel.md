# Attempt 007 — Claim-Backing Audit: me_cfs/ top-level

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: medical/me_cfs/PROBLEM.md (40 lines), gap.md (122 lines),
THEWALL.md (1719 lines — sampled L1–80 "One Sentence + Three Nested
Walls + biomarker + Protocol start"). anti_problem.md not audited
this fire.
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: audit log fires 1–12.

## Executive verdict

**me_cfs/ has the strongest empirical grounding seen in the non-math
corpus so far.** gap.md invokes a specific transcriptomic dataset
(GSE293840, n=168, 93 ME/CFS vs 75 controls) and reports 7 specific
predictions with effect sizes and p-values, 6 of which confirmed at
p<0.05, 1 of which (FOXP3) honestly labeled "NOT SIGNIFICANT (p=0.10)."
This matches the math-standard pattern from ns_blowup's "measured max
||S||²_F/|ω|² ≈ 0.66 (gap.md line 101)" precision — a named dataset,
a named quantity, a measured value, an honest label on the
non-significant one.

THEWALL.md's "Three Nested Walls" framing (invisible target / mito
damage / what virus) converts a complex clinical presentation into
three falsifiable barriers with protocol-specific answers. The
"What ME/CFS Is Not" list (L29–34) pre-empts common misattributions
with specific molecular evidence.

**🔴 RED count**: 1
**🟡 YELLOW count**: 6
**🟢 GREEN count**: 10

## RED findings

### R27 — PROBLEM.md L4 + gap.md L42 + THEWALL.md L52
("42% CVB-positive in ME/CFS muscle biopsies vs 9% controls")

**The claim**: "Enteroviral persistence (CVB) found in 42% of ME/CFS
patients vs 9% controls" (PROBLEM.md L4); same figure recurs in
gap.md L42 ("42% CVB RNA in muscle biopsies → 58% may have other
triggers") and THEWALL.md L52 ("42% of ME/CFS muscle biopsies are
positive for enteroviral RNA").

**Why load-bearing**: the 42-vs-9 split anchors the "CVB is a major
driver of ME/CFS" hypothesis, the protocol's antiviral-arm
prioritization, and the stratification rationale ("CVB-positive
patients get the full protocol; CVB-negative patients get the
non-antiviral components"). Without this number, the protocol's
structure is unmotivated.

**Concern**: this statistic almost certainly traces to Chia & Chia
2008 *Journal of Clinical Pathology* (PMID 17872383) which reported
VP1 protein in 82% of ME/CFS stomach biopsies vs 20% of controls — or
to subsequent muscle-biopsy work (Douche-Aourik et al. 2003). The
specific "42% / 9%" pairing is not a verbatim match to the canonical
Chia 2008 paper. It may be a subsequent study or a synthesis across
multiple cohorts. Either way, the paper citation is absent across
all three locations where the number is used.

**Required fix**:
1. Thread the specific source paper for 42/9 (likely Chia & Chia
   2008 PMID 17872383, but confirm), or if the 42/9 comes from a
   different study, cite that.
2. If 42/9 is a composite across multiple studies, state that
   explicitly and cite each contributing study.
3. Propagate the citation to all three locations (PROBLEM.md, gap.md,
   THEWALL.md) — a single statistic cited in three places must agree
   on its source.

## YELLOW findings

| # | File / line | Claim | Source gap |
|---|-------------|-------|------------|
| Y120 | PROBLEM L4 | "~2.5M Americans" affected | CDC 2021 estimate (Bateman Horne Center or CDC ME/CFS page); thread |
| Y121 | gap.md L23 | "GSE293840 analyzed 168 samples (93 ME/CFS vs 75 controls)" | Accession verifiable at NCBI GEO; thread URL and confirm sample counts |
| Y122 | gap.md L29 | "STAT1/2/4, IRF1, RIG-I, MDA5 all UP" with no per-gene p-value | Effect-size table should have per-gene effect + p-value; currently grouped as "all UP" — OK as summary but drill-down would match math standard |
| Y123 | gap.md L30 | "PD-1, Tim-3, LAG3, TIGIT all UP" | Same comment — per-checkpoint effect size desirable |
| Y124 | gap.md L32 | "7/12 mt-encoded respiratory genes DOWN" | Which 7? MT-ND3 is cited specifically (-17% p=0.002) but 7/12 is a count without per-gene accounting; list them |
| Y125 | gap.md L96 | "NK cell dysfunction — reduced CD56bright cells" | Fluge/Mella or Brenu et al. NK work; thread |

## GREEN findings

- **G69** gap.md L22–35 — **7-prediction validation table with
  effect sizes + p-values**. Each row is (prediction / result /
  status) with specific numbers (Perforin +52%, MT-ND3 -17% p=0.002,
  NLRP3 +37%, CASP1 +29%, ATG7 +32%). This IS the math standard
  translated to transcriptomics.
- **G70** gap.md L33 — **FOXP3 honestly labeled "NOT SIGNIFICANT
  (p=0.10)"**. When a prediction doesn't confirm, the corpus says so.
  This is sigma-method confirmation-bias-audit compliant — 6/7 is
  accurate, 7/7 would be selection.
- **G71** gap.md L71–79 — **"What Is No Longer a Gap" table** shows
  gap-evolution over the audit life cycle. Maps-Include-Noise
  compliant — resolved gaps are kept as map features, not silently
  removed.
- **G72** gap.md L102–109 — **Post-Exertional Malaise Protocol with
  SAFE/DANGEROUS labels per intervention**. PEM is the hallmark of
  ME/CFS; correctly flagging exercise as DANGEROUS until viral
  clearance is a safety-critical clinical rule (matches v5 Verify-
  Before-Acting principle).
- **G73** THEWALL.md L5 — "**molecular signature is not fatigue, it
  is T cell exhaustion from chronic viral antigen exposure,
  mitochondrial dysfunction from Complex I damage, and NK cells armed
  with killing machinery they can't use**" — one-sentence frame that
  captures the corpus's thesis with specific molecular anchors.
- **G74** THEWALL.md L29–34 — "**What ME/CFS Is Not**" — explicitly
  rules out deconditioning, psychosomatic, simple fatigue, depression,
  each with molecular evidence. Pre-empts common misattributions.
- **G75** THEWALL.md L37–56 — **Three Nested Walls** (invisible
  target, mitochondrial damage, what-virus) each with specific
  protocol answer. Each wall is a distinct mechanism; the protocol
  addresses all three.
- **G76** THEWALL.md L60–67 — **validated biomarker panel MT-ND3 +
  PRF1 + STAT2 cfRNA** with specific criteria: (1) blood draw not
  biopsy, (2) maps to mechanism, (3) should respond to protocol.
  Concrete trial-enabling artifact.
- **G77** THEWALL.md L71–77 — **two critical protocol differences
  from T1DM** (no exercise during antiviral phase, mitochondrial arm
  first priority) — subdirectory protocol INHERITS from t1dm/ but
  explicitly overrides two elements. This is structured inheritance
  with explicit diff — clearer than silent forking.
- **G78** gap.md L120–122 — **"Current Gap Rank: MEDIUM"** is a
  single-token classification of the gap's state. Not "low", not
  "high" — MEDIUM with specific justification ("clinical validation
  remaining"). Sharp framing.

## Recommended fixes (ordered)

1. **[P0]** Thread the Chia & Chia 2008 *J Clin Pathol* PMID (or the
   correct source) for the 42% CVB-positive statistic across
   PROBLEM.md L4, gap.md L42, THEWALL.md L52.
2. **[P1]** Thread CDC/biobank source for 2.5M Americans (Y120).
3. **[P1]** Verify GSE293840 accession and sample counts (Y121) —
   NCBI GEO lookup is cheap.
4. **[P2]** Drill down gap.md L29–30 "all UP" groupings into per-gene
   effect sizes (Y122, Y123).
5. **[P2]** List the specific 7-of-12 mt-encoded genes (Y124).

## Non-audit observations

- me_cfs/ is the first subdir where **population-level transcriptomic
  data has been explicitly matched to the corpus's prior predictions**.
  The 6/7 confirmed / 1/7 not-significant result is a strong positive
  for the corpus's mechanistic model. Other medical subdirs should
  follow this pattern where transcriptomic datasets exist.
- The **"Three Nested Walls" framing** is a generalizable sigma-method
  pattern. When a disease has multiple mechanisms, the walls compose
  rather than compete; each wall is a falsifiable claim; each wall
  has a specific intervention. This template works for any multi-
  mechanism disease.
- The **structured inheritance from t1dm/ protocol with explicit
  diffs** (L71–77) is cleaner than forking without acknowledgment. If
  this pattern were followed across medical subdirs, cross-subdir
  protocol evolution would be easier to track and audit.

## Tag

007. First audit pass on medical/me_cfs/. **me_cfs/ has the strongest
empirical grounding in the non-math corpus so far** — GSE293840 n=168
dataset with 6/7 predictions confirmed at p<0.05 and 1/7 honestly
labeled not-significant. 1 🔴 (42%-vs-9% CVB muscle biopsy statistic
used in three locations without source citation — likely Chia & Chia
2008 J Clin Pathol PMID 17872383 but needs confirmation). 6 🟡 (2.5M
Americans CDC source; GSE293840 accession verification; per-gene
effect sizes inside "all UP" groupings). **10 🟢 — ties with
dysbiosis as highest green count**: 7-prediction validation table
with effect sizes + p-values, FOXP3 honestly labeled not-significant
(confirmation-bias audit pass), "What is no longer a gap" evolution
table, PEM protocol with SAFE/DANGEROUS labels, one-sentence
molecular frame, "What ME/CFS Is Not" pre-empting misattributions,
Three Nested Walls framing, cfRNA biomarker panel, structured protocol
inheritance from t1dm/, "Current Gap Rank: MEDIUM" single-token
classification. Next fire: THEWALL.md deep-dive (1719 lines —
warrants own fire) OR move to acne/myocarditis/dilated_cardiomyopathy.
