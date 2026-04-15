# Attempt 005 — Claim-Backing Audit: medical/pericarditis/ top-level

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: medical/pericarditis/THEWALL.md (114 lines) + gap.md (40
lines) + PROBLEM.md (24 lines).
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: CONVERGENCE.md flagged pericarditis Tier 1 RCT as "the
most rigorous first trial in the campaign" (fire 29 G204).

## Executive verdict

**pericarditis/THEWALL.md is the strongest per-disease THEWALL
document** — compact (114 lines) but dense with actionable RCT
design specifics. It differs from t1dm/me_cfs THEWALLs (2022/1719
lines with extensive cross-reference catalogs) by being **focused
entirely on the trial case**. This is sigma-method kill-ROI applied
at the disease level: of all 16 diseases, pericarditis is argued to
be the fastest path to human proof, so its THEWALL is organized
around making that trial happen.

Key claims:
- 3-arm RCT: n=65/arm, 195 total, 18-24 months
- Binary primary endpoint: recurrence at 18 months
- ~$500K-1M cost estimate
- Existing cardiology/rheumatology infrastructure
- Prediction: 30% → <5% recurrence

**🔴 RED count**: 0
**🟡 YELLOW count**: 4
**🟢 GREEN count**: 11

## YELLOW findings

| # | File / line | Claim | Source gap |
|---|-------------|-------|------------|
| Y233 | THEWALL L20 "30% RECURRENCE" (colchicine current standard) | COPE (Imazio 2005) + CORP (Imazio 2011) + CORP-2 trial recurrence data; thread PMIDs |
| Y234 | THEWALL L25 "κ_pericardium = 0.55" | ODD-model-derived κ_effective for pericardium; cite specific numerics file (unified_cvb_clearance_v3.py or similar) |
| Y235 | THEWALL L76 "Pericardial mesothelial cells: LAMP2_baseline ≈ 1.5× average" | Specific organ-LAMP2 claim — cite the per-organ LAMP2 measurement (from organ_baseline_lamp2.py?) |
| Y236 | THEWALL L88 "Itraconazole contraindicated if ANY pericardial effusion" | Correct clinical principle (itraconazole negative inotrope risk exacerbates effusion physiology) but thread specific cardiology ref (Ahmad 2001 NEJM itraconazole heart failure black box) |

## GREEN findings

- **G279** THEWALL L4 **one-sentence thesis**: "The pericarditis wall
  is not biology — it's funding and clinical inertia. **Nothing
  blocks this trial except the decision to run it.**" Phase-0-
  behavioral-wall framing applied to a specific trial (not the
  campaign).
- **G280** L8-29 **Biology-Solved block** with mechanism chain
  (CVB-persists → NLRP3 → IL-1β → symptoms) and colchicine-stop-
  reactivation-loop diagnostic for the 30% recurrence. Then
  fluoxetine+FMD+trehalose prediction (30% → <5% recurrence).
- **G281** L41-52 **Complete trial design table** with per-parameter
  row: 3-arm RCT, n=65/arm=195 total, stratification by CVB VP1 IgM,
  primary endpoint recurrence at 18mo (binary), 18-24 mo duration,
  standard cardiology infrastructure, $300/patient drug cost.
  **Trial design is concrete, not hypothetical.**
- **G282** L57-67 **Why-this-trial-first comparison table** vs T1DM
  n=1 and ME/CFS pilot n=30: higher N, binary-vs-continuous
  endpoint, higher generalizability, higher publishability (NEJM vs
  case report), higher regulatory value. Kill-ROI ordering at the
  trial-selection level.
- **G283** L72-84 **LAMP2-corrected trial duration rationale** —
  originally 6-month design (v2), updated to 9-month (v3) after
  LAMP2 finding. Specific math: κ_effective = 1.5/2.7 ≈ 0.55;
  without trehalose 5.5 mo clearance; with trehalose κ ~0.90 →
  3.5 mo; 9-month protocol adds 1-2 month safety buffer "to ensure
  NLRP3 has fully quieted before colchicine withdrawal." Design
  evolved with evidence.
- **G284** L86-88 **Itraconazole safety-exclusion rule**:
  "Itraconazole is contraindicated if there is ANY pericardial
  effusion or constrictive physiology. Pericarditis patients often
  have small effusions. Do NOT add itraconazole to the pericarditis
  protocol. Fluoxetine only for this disease." Disease-specific
  drug-exclusion rule — cross-pollinated from DRUG_SAFETY_MATRIX.
- **G285** L92-100 **Wall-is-funding section**: 3 specific
  bottlenecks (funding $500K-1M, a willing PI, IRB 4-6mo). Each
  bottleneck is identified + solution identified (JDRF/ESC/pharma
  for funding; "one cardiologist in every dept" for PI; standard
  IRB timeline). **Sigma-method Phase-0 behavioral-wall: science
  solved, wall is compliance/action.**
- **G286** L104-112 **What-happens-if-this-trial-succeeds**: 4
  specific downstream consequences (CVB persistence proved; fluoxetine
  as CVB antiviral validated; FMD autophagy additive; cfRNA NLRP3
  as shared biomarker). One trial → cascade of 11 other CVB
  disease trials become "same mechanism, same drug, different
  organ."
- **G287** gap.md L3-5 **"Why This Is the Easiest of the 12"** —
  pericarditis is the only CVB disease where standard treatment
  exists (colchicine), recurrence is documented + measurable,
  adding fluoxetine is low-risk. **Correct identification of the
  highest-feasibility disease** for first trial.
- **G288** gap.md L31-40 **"Convergence: proof-of-concept disease"**
  — 5 features that make pericarditis the simplest first trial.
  "Outcome is binary: recurrence yes/no at 12 months" — binary
  endpoint + well-characterized standard therapy + clearly
  falsifiable.
- **G289** L70 "**If it's negative**: we learn whether the effect
  is CVB-specific (test VP1 IgM-positive subgroup) or whether
  fluoxetine dose is insufficient. Both answers are valuable."
  Pre-committed analysis under negative result — sigma-method
  "formalize dead ends."
- **G290** Compactness (114 lines vs 2022 t1dm / 1719 me_cfs) is
  itself a feature — THEWALL.md's argument is that pericarditis is
  the trial path, so the doc is organized around making that path
  visible. No cross-reference catalog needed because the argument
  is self-contained.

## Recommended fixes (ordered)

1. **[P1]** Thread COPE/CORP/CORP-2 PMIDs for 30% recurrence
   (Y233). These are the anchor clinical-trial references
   validating the standard-of-care and its failure mode.
2. **[P2]** Thread ODD-model file for κ_pericardium = 0.55 (Y234)
   and organ-specific LAMP2 baseline (Y235).
3. **[P2]** Thread Ahmad 2001 NEJM itraconazole cardiotoxicity
   black box reference for the itraconazole-effusion
   contraindication (Y236).

## Non-audit observations

- **pericarditis/THEWALL.md is the audit's strongest per-disease
  THEWALL**. Compact. Focused on one trial. Concrete numbers. No
  speculation. **Exemplary template for any disease where the
  answer is "run the trial."**
- **The 4-tier wall hierarchy gets clearer**: per-disease-trial
  (this doc) → per-disease synthesis (POD behavioral-wall, t1dm
  mechanism-counting catalog, me_cfs stigma wall) → campaign-level
  (medical/THEWALL.md "the wall is a blood draw appointment") →
  meta-framework audits.
- **The claim structure in pericarditis THEWALL is unique**: it's
  one argument ("run this trial"), not a synthesis of many
  mechanisms. This is what "the wall is X, and we know how to
  cross it" looks like when fully worked out.

## Tag

005 (pericarditis). Audited THEWALL + gap. **0 🔴, 4 🟡, 11 🟢**.
**pericarditis/THEWALL.md is the audit's strongest per-disease
THEWALL**: compact (114 lines), focused entirely on the Tier 1
trial case, one-sentence thesis ("Nothing blocks this trial except
the decision to run it"), Biology-Solved mechanism block with 30%-
recurrence-via-colchicine-withdrawal diagnostic, **complete trial
design table** (3-arm RCT, n=195, binary primary endpoint,
18-24 mo duration, $500K-1M cost), why-this-trial-first comparison
(higher N + binary endpoint + generalizability + NEJM-level
publishability vs T1DM n=1 and ME/CFS pilot n=30), LAMP2-corrected
9-month duration rationale (κ=0.55→0.90 with trehalose, +safety
buffer), itraconazole-contraindicated-in-effusion safety-exclusion
rule, wall-is-funding-PI-IRB Phase-0 framing, if-negative pre-
committed analysis, downstream-cascade argument (one trial →
11 CVB disease trials become "same mechanism, different organ").
4 🟡: COPE/CORP PMID threading, κ_pericardium numerics-file, per-
organ-LAMP2 source, Ahmad 2001 NEJM itraconazole cardiotoxicity.
**Observation**: pericarditis/THEWALL is exemplary template for
"the wall is X, we know how to cross it" when the answer is
running a specific trial. Next fire: myocarditis or encephalitis
THEWALL, WHM sweep (pending op), or audit-phase-close synthesis.
