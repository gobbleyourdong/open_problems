# Attempt 002 — Claim-Backing Audit: medical/DRUG_SAFETY_MATRIX.md + FAILURE_MODES.md

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: medical/DRUG_SAFETY_MATRIX.md (190 lines, sampled L1–80)
+ FAILURE_MODES.md (160 lines, sampled L1–60).
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: audit log fires 1–27.

## Executive verdict

**Both docs extend the "5 strongest claim-backing docs" list from
fire 27 — upgraded to 7 strongest.** DRUG_SAFETY_MATRIX.md is
clinical-safety-grade (fatal-interaction warnings, dose adjustments,
interaction-decision tree). FAILURE_MODES.md is the most **sigma-
method-compliant document in the entire non-math corpus** — it
pre-registers failure modes with explicit probability estimates
and action plans per failure.

**FAILURE_MODES.md is the "kill-first" discipline made document**.
Each failure mode has:
- What it means (the hypothesis-negation)
- Impact (what the protocol loses)
- What survives (partial valid results preserved)
- What dies (specific claim killed)
- What we'd do (pre-committed pivot)
- Probability estimate (actual prior, e.g., ~20%, ~30%, ~25%, ~25%)

This is sigma method v5 "Pivot Triggers" (pre-committed action
under each failure condition) applied at the campaign level. Rarest
discipline in the corpus.

**🔴 RED count**: 0 (both docs are self-auditing)
**🟡 YELLOW count**: 4
**🟢 GREEN count**: 12

## YELLOW findings

| # | File / line | Claim | Source gap |
|---|-------------|-------|------------|
| Y190 | DRUG_SAFETY L44 | "DOCUMENTED FATALITIES from this combination exist in the literature" (itraconazole + colchicine) | Specific case reports / FDA MedWatch references should be threaded — the claim is correct in direction (this is a well-known fatal interaction) but the citation line is bare |
| Y191 | DRUG_SAFETY L10 | "Fluoxetine: CYP2D6 hepatic" | Also substrate of CYP2C9, CYP2C19, CYP3A4 (minor), and inhibits CYP2D6 + CYP2C19 + CYP3A4 (weakly) — the table simplification understates the interaction surface; could flag "also CYP2D6 inhibitor" to catch the MAOI risk at multiple axes |
| Y192 | FAILURE_MODES probability estimates (~20%, ~30%, ~25%, ~25%) | Where derived? | Explicit priors are sigma-method-compliant, but their source (expert elicitation? operator judgment? prior-based calculation?) should be labeled |
| Y193 | FAILURE_MODES L45 | "κ_LAMP2 ≈ 0.37" effective autophagy completion rate | Cite the specific ODD model file or numerics script that produces 0.37 — consistent with prior audit findings (GSE184831 LAMP2 -2.7× is cited but the 37% completion rate is a derived parameter) |

## GREEN findings

- **G188** DRUG_SAFETY — **"CRITICAL INTERACTION" boxed section** for
  itraconazole + colchicine with explicit fatality warning and 4-
  option decision tree (A: fluoxetine only + colchicine; B:
  itraconazole only drop colchicine; C: reduce colchicine; D: for
  pericarditis patients choose A). This is **clinical-grade safety
  discipline** — the operator did not bury this as a line in a
  table, they surfaced it with a warning symbol + decision tree.
- **G189** DRUG_SAFETY Supplement stack table with per-supplement
  interactions + concerns. Zinc "reduces copper absorption long-
  term. Add copper 2mg if >3 months" — specific dose-adjustment
  rule. Selenium "Toxicity >400μg/day (don't exceed)" — explicit
  upper limit.
- **G190** DRUG_SAFETY L56–69 "MODERATE RISK" fluoxetine + NSAIDs
  section with explicit mitigations (add PPI, limit NSAID duration,
  monitor GI symptoms). Right level of concern for the actual
  severity.
- **G191** DRUG_SAFETY L74–80 Apremilast interactions section notes
  "Itraconazole (CYP3A4 inhibitor) may increase apremilast levels
  modestly. Monitor GI side effects. Consider reducing apremilast
  to 30mg QD." Same mechanism-aware dose adjustment applied.
- **G192** FAILURE_MODES — **6+ failure modes pre-registered** with
  per-mode probability estimates. FM1 (C-peptide undetectable, 20%),
  FM2 (fluoxetine dose insufficient, 30%), FM3 (CVB not primary
  driver, 25%), FM4 (autophagy hijacking too robust, now 25%
  post-LAMP2), FM5 (ME/CFS heterogeneity).
- **G193** FAILURE_MODES per-mode "What survives" sections —
  protocol components that REMAIN valid even if the specific
  failure mode hits. This is Maps-Include-Noise at the claim level:
  the partial truth is preserved even when the specific claim
  fails.
- **G194** FAILURE_MODES per-mode "What we'd do" sections — pre-
  committed pivot with specific alternative approaches. FM1 pivots
  to stem cell + immune protection pathway (attempts 003/007/008);
  FM3 pivots to teplizumab + immune modulation + FMD (no
  antiviral). These are **pre-committed pivot triggers** per sigma
  v5.
- **G195** FAILURE_MODES L37 "How to detect" for FM3: "start
  fluoxetine → measure C-peptide at 3, 6 months. If C-peptide
  doesn't improve despite expected viral clearance timeline →
  virus wasn't the driver." Explicit falsification protocol with
  timeline.
- **G196** FAILURE_MODES FM4 updated L50–55 with **LAMP2 mitigation
  via trehalose** — when bioinformatics identified the LAMP2 block,
  FAILURE_MODES was updated with the specific mitigation (TFEB
  activation via trehalose). This is **live document updating when
  new evidence changes a failure mode's prognosis** (matches
  EVIDENCE_GRADES grade-shift pattern from fire 27).
- **G197** FAILURE_MODES L55 explicit probability DOWNGRADE: "25%
  (reduced from 35% by LAMP2 mechanism identification — we now
  know exactly what to fix)." Probability updated with mechanism
  clarity, not arbitrary. Bayesian-style update preserved.
- **G198** DRUG_SAFETY "OPTIONS" decision tree (A/B/C/D for
  itraconazole+colchicine) shows **clinical decision aid** under
  conflicting goals (antiviral + anti-inflammatory both needed, can't
  have both at full dose). Decision-under-constraint framing.
- **G199** FAILURE_MODES top-level framing L1–3: "The systematic
  approach formalizes dead ends as theorems. This document pre-
  registers the failure modes." This is sigma method v5 "Define
  pivot triggers BEFORE starting" compliance at the campaign level.

## Recommended fixes (ordered)

1. **[P1]** DRUG_SAFETY Y190: thread specific case-report or MedWatch
   references for the itraconazole+colchicine fatality claim.
   Without a named source, "DOCUMENTED FATALITIES exist" is correct-
   but-floating.
2. **[P2]** DRUG_SAFETY Y191: expand fluoxetine metabolism/
   interaction surface (CYP2D6 inhibitor in addition to substrate;
   other CYPs partially involved).
3. **[P2]** FAILURE_MODES Y192: label the probability estimates'
   derivation source (operator judgment, expert elicitation, prior-
   based calculation).
4. **[P2]** FAILURE_MODES Y193: link κ_LAMP2 ≈ 0.37 to the specific
   ODD model file / numerics script.

## Non-audit observations

- **Updated "strongest claim-backing docs in non-math corpus" list
  to 7**:
  1. math/ns_blowup/attempts/attempt_849 (gold standard)
  2. medical/CLINICAL_BRIEF.md
  3. medical/EVIDENCE_GRADES.md
  4. **medical/DRUG_SAFETY_MATRIX.md** ← new
  5. **medical/FAILURE_MODES.md** ← new
  6. t1dm/gap.md
  7. physics/what_is_time/gap.md
- **FAILURE_MODES.md is sigma-method-exemplary**: pre-registered
  failures + per-failure pivots + probability estimates updated
  live when new evidence arrives. This is the discipline sigma
  method v5 ("pivot triggers defined before starting") aims for.
  Consider extracting the FAILURE_MODES template for use in other
  non-math subdirs (e.g., dysbiosis/, me_cfs/, POD/ could each have
  their own FAILURE_MODES.md).
- **Pattern observation**: medical/ top-level docs all have a clear
  risk/honesty discipline that the per-disease subdir attempts
  often lack. The top-level is MORE rigorous than many of its
  children. This inverts the expected pattern (specialists more
  rigorous than generalists) and suggests the top-level synthesis
  enforces discipline the children can drop into.
- **10 medical/ top-level docs remain un-audited** (~2100 lines):
  MEDICAL_PROBLEMS, PRE_EXPOSURE_PREVENTION, PATIENT_ZERO_SCREENING,
  CONVERGENCE, GEO_DATASET_CATALOG, CVB_VACCINE_STRATEGY, PREVENTION_
  STRATEGY, PATIENT_ZERO_TIMELINE (contains R26 WHM-lockdown),
  DISEASE_DATA_SUMMARY, THEWALL.md, FOR_YOUR_DOCTOR.md.

## Tag

002 (medical/ top-level). Audited DRUG_SAFETY_MATRIX.md +
FAILURE_MODES.md. **Both join the top-tier claim-backing list (now
7 docs total).** 0 🔴. 4 🟡 (itraconazole+colchicine fatality
specific cite, fluoxetine CYP surface broader, probability-
derivation source label, κ_LAMP2 ≈ 0.37 numerics-file link).
**12 🟢**: CRITICAL-INTERACTION decision tree (4-option A/B/C/D),
supplement per-entry upper limits (selenium 400μg), apremilast
dose-reduction rule under itraconazole, **6+ failure modes pre-
registered with probability estimates** (FM1 20%, FM2 30%, FM3
25%, FM4 25% post-LAMP2 update), "What survives" per failure
preserves partial valid results, "What we'd do" pre-committed
pivots (FM1→stem cell pathway, FM3→teplizumab alternative), "How
to detect" explicit falsification protocol with timeline, **live
probability DOWNGRADE with mechanism clarity** (FM4 35%→25%),
clinical-decision-aid under conflicting goals. **Observation:
FAILURE_MODES.md is the most sigma-method-compliant "kill-first"
document in the entire non-math corpus** — pre-registered failure
modes with actual priors and action plans. Remaining medical/
top-level audit: ~10 files / ~2100 lines. Next fire: continue
medical/ / biology attempts / WHM sweep (pending). |
