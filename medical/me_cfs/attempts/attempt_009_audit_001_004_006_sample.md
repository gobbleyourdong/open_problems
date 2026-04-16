# Attempt 009 — Claim-Backing Audit: me_cfs/attempts sample (002, 004, 006)

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue, Fire 57)
**Scope**: medical/me_cfs/attempts/attempt_002_nk_cell_restoration.md
(97L, L1-50), attempt_004_cfrna_validation.md (133L, L1-70),
attempt_006_dysbiosis_framework_import.md (211L, L1-60).
3 of 6 non-audit attempts sampled (~750L corpus).
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md

## Executive verdict

**me_cfs attempts are clinically grounded with quantitative data.**
attempt_004 is the strongest — specific per-gene cfRNA tables from
GSE293840 (n=168) with log2FC + p-values, already data-verified at
Fire 42. attempt_002 provides mechanism + protocol. attempt_006
imports dysbiosis framework with multi-phase HPA model.

**Same PMID-threading gap** as dysbiosis numerics and early
biology/evolution — author+year+journal cited but no PMIDs.

**🔴 RED count**: 0
**🟡 YELLOW count**: 4
**🟢 GREEN count**: 8

## YELLOW findings

| # | Location | Claim | Source gap |
|---|----------|-------|------------|
| Y309 | 002 L9 "Brenu 2011, Hardcastle 2015" NK cytotoxicity 40-60% of normal | Thread PMIDs (Brenu 2011 J Transl Med PMID ~21513514; Hardcastle 2015 J Transl Med PMID ~25705783) |
| Y310 | 002 L41 "Brenner 1999: 6-fold NK increase post-cold" | Specific claim — verify 6-fold; Brenner IKT 1999 Eur J Appl Physiol (cold-water immersion NK mobilization) |
| Y311 | 002 L43 "Irwin 2015: 1 night deprivation = 70% NK drop" | Strong quantitative claim — 70% NK drop after 1 night. Irwin MR is a real sleep-immunity researcher but verify specific 70% figure and year |
| Y312 | 006 L55 "Cleare 2004 review" ME/CFS hypocortisolism | Thread PMID (Cleare 2004 likely Cleare AJ Biol Psychiatry or similar) |

## GREEN findings

- **G447** attempt_004 **per-gene cfRNA tables** with log2FC,
  fold-change, p-values for 7 mitochondrial genes + 4 T-cell
  exhaustion markers + 5 NK cytotoxic machinery genes. Quantitative
  validation against 62 model-predicted target genes. **34/62
  significant at p<0.05, all in predicted direction.**
- **G448** attempt_004 **"first direct molecular evidence for
  cfRNA-detectable mitochondrial dysfunction in ME/CFS"** — MT-ND3
  -0.260 log2FC p=0.0022 across Complex I. 7/12 mt-encoded genes
  significant. Biomarker candidate identified.
- **G449** attempt_004 **canonical T-cell exhaustion quartet** (PD-1/
  LAG3/Tim-3/TIGIT) all elevated simultaneously. "Essentially
  pathognomonic of chronic antigen exposure" (Wherry 2015 framing).
  Already data-verified at Fire 42.
- **G450** attempt_004 **"exhausted sniper" model refinement** —
  perforin +52% p=0.0002 + all 5 NK machinery genes UP. NK cells
  present and armed but can't find targets. Clinical implication:
  "Boosting NK cell numbers won't help ME/CFS if NK cells already
  can't see targets — rely on autophagy for CVB clearance."
  Prediction revision from data.
- **G451** attempt_002 **3-hypothesis structure** for NK failure
  (exhaustion / supply failure / metabolic impairment) with per-
  hypothesis testable assay (NKG2A+Tim-3 expression / NK counts +
  IL-15 / JC-1 + OCR). Falsifiable per-mechanism.
- **G452** attempt_002 **Tier 1 + Tier 2 protocol table** with
  per-intervention NK mechanism + evidence reference. Tier 1 from
  T1DM arsenal; Tier 2 ME/CFS-specific additions. Cross-disease
  protocol inheritance with explicit modifications.
- **G453** attempt_006 **M1↔M8 HPA exhaustion model** with 2-phase
  trajectory: Phase 1 ascending hypercortisolism → Phase 2 descent
  to hypocortisolism. Mechanistic explanation for ME/CFS cortisol
  paradox (hypocortisolism not hypercortisolism). Cross-references
  dysbiosis framework mountains M1/M6/M8.
- **G454** attempt_006 **temporal staging** of ME/CFS cortisol:
  early (0-3yr) normal/elevated → established (>3-5yr) consistently
  low → severe profound hypocortisolism + orthostatic intolerance.
  Testable at multiple timepoints.

## Tag

009 (me_cfs). Sampled 3/6 attempts (002/004/006, ~440L). **0 🔴**.
4 🟡 (Brenu 2011/Hardcastle 2015/Brenner 1999/Irwin 2015/Cleare
2004 PMIDs). **8 🟢**: cfRNA per-gene quantitative tables (34/62
significant all predicted direction); mitochondrial cfRNA biomarker
candidate MT-ND3; canonical T-cell exhaustion quartet (Fire 42
verified); "exhausted sniper" NK model refinement from data;
3-hypothesis NK failure with per-hypothesis assay; cross-disease
protocol inheritance T1DM→ME/CFS; M1↔M8 HPA 2-phase exhaustion
model for cortisol paradox; temporal ME/CFS cortisol staging.
**Observation**: attempt_004 (cfRNA) is the strongest per-attempt
document in me_cfs/ — quantitative data from n=168 with per-gene
statistics. Next fires: cron continues; diminishing returns.
