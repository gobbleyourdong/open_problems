# Attempt 006 — Claim-Backing Audit: medical/PATIENT_ZERO_SCREENING.md + GEO_DATASET_CATALOG.md

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: medical/PATIENT_ZERO_SCREENING.md (141 lines, sampled
L1–80) + medical/GEO_DATASET_CATALOG.md (178 lines, sampled L1–80).
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: audit log fires 1–31.

## Executive verdict

**PATIENT_ZERO_SCREENING.md**: clinical-grade 4-tier screening panel
with per-test normal ranges, flag thresholds, and costs ($300-500
Tier 1, $200-400 Tier 2, $500-2000 Tier 3, $300-600 Tier 4). Decision
tree for abnormal findings per category.

**GEO_DATASET_CATALOG.md**: structured inventory of GEO datasets
supporting the 12-disease campaign with accession / title / N samples
/ organism / assay type / download status. Source-search JSON paths
threaded at the top for reproducibility.

Both are research-grade reference documents. Neither introduces new
overstatements. Remaining concerns are citation threading.

**🔴 RED count**: 0
**🟡 YELLOW count**: 4
**🟢 GREEN count**: 8

## YELLOW findings

| # | File / line | Claim | Source gap |
|---|-------------|-------|------------|
| Y209 | SCREENING L34 "C-peptide >0.6 ng/mL = residual function" threshold | Clinical cutoff — cite ADA consensus or specific validation paper (Leighton 2017 C-peptide review or similar) |
| Y210 | SCREENING Tier 2 "CVB1-5 neutralizing antibodies / enteroviral VP1 antigen / stool enteroviral RT-PCR / IFN-α level" | All Research lab only — note availability by region; for US, what labs run this? (academic medical center virology labs only) |
| Y211 | GEO_CATALOG "GSE184831 [DOWNLOADED]" + 7 other T1DM datasets | Accession IDs are verifiable at NCBI; thread URLs for 1-click access |
| Y212 | GEO_CATALOG L55 "Priority download recommendation: GSE174458 (scRNA-seq), GSE35182 (acute vs chronic DCM), GSE57781 (human iPSC)" | Recommendation reasoning clear — but these are IDENTIFIED not DOWNLOADED, so the recommendation's current state is "not yet acted on" |

## GREEN findings

- **G231** PATIENT_ZERO_SCREENING L11-37 — **Tier 1 blood panel**
  with 19 tests across cardiac / hepatic / endocrine / inflammation
  / immune / diabetes / polyglandular-screen. Each row has: Test /
  Screens for / Normal / Flag if. Clinical-grade specificity.
- **G232** PATIENT_ZERO_SCREENING L34 — C-peptide marked "**the KEY
  measurement**" in-table, consistent with THEWALL.md's
  "stimulated C-peptide = Minimum Wall to Cross" framing. Single-
  action focus propagated across documents.
- **G233** PATIENT_ZERO_SCREENING L36-37 Anti-TPO + Anti-TG2 added
  with "Hashimoto's co-screen (25-30% of T1DM)" and "celiac co-
  screen (5-10% of T1DM)" — comorbidity prevalence cited per test,
  not just threshold.
- **G234** PATIENT_ZERO_SCREENING L39-46 **Tier 2 "CVB-Specific"
  with explicit availability caveat** ("Where to order" column):
  Research virology lab / Research lab / Clinical virology /
  Immunology lab. Honest separation of "routine" from "research-
  accessible."
- **G235** PATIENT_ZERO_SCREENING L49-63 **Tiers 3-4 costed**:
  Imaging ($500-2000), Functional/Immune ($300-600). Per-test "When
  to order" conditional triggers (not blanket panel).
- **G236** PATIENT_ZERO_SCREENING L65-80 **Decision tree**: abnormal
  finding → specific next action. "Troponin/BNP elevated → Cardiac
  MRI → LGE positive → ESCALATE cardiac protocol + Avoid
  itraconazole (cardiotoxic)" — operationalized branching.
- **G237** GEO_CATALOG L3-5 — **Source-search JSON paths + download
  log path** threaded at document top. Reproducibility: a future
  reader can replicate the search or check download status from the
  named files.
- **G238** GEO_CATALOG L7 — **Legend explicitly separates DOWNLOADED
  / IDENTIFIED / PLATFORM** — data-on-disk vs found-in-search vs
  metadata-record-not-a-study. Clear state labeling for each dataset.

## Recommended fixes (ordered)

1. **[P1]** SCREENING Y209: thread C-peptide 0.6 ng/mL threshold
   citation — Leighton 2017 / ADA consensus.
2. **[P2]** GEO_CATALOG Y211: thread NCBI URLs for major datasets
   (GSE184831, GSE293840, etc.) for one-click verification.
3. **[P2]** SCREENING Y210: for each research-lab test, specify
   which academic-medical-center virology labs run it (at least for
   US major regions).

## Non-audit observations

- **Campaign documentation set now 12 medical/ top-level docs
  audited** (10 prior + these 2): CLINICAL_BRIEF, EVIDENCE_GRADES,
  DRUG_SAFETY_MATRIX, FAILURE_MODES, CONVERGENCE, MEDICAL_PROBLEMS,
  PATIENT_ZERO_TIMELINE, CVB_VACCINE_STRATEGY, FOR_YOUR_DOCTOR,
  THEWALL.md, PATIENT_ZERO_SCREENING, GEO_DATASET_CATALOG.
- **The SCREENING + TIMELINE + FOR_YOUR_DOCTOR triad** covers the
  operator's complete path: screening (what to test) → timeline
  (when to test) → communication (how to ask doctor for the tests).
  Three documents covering the same workflow at different zoom
  levels.
- **GEO_DATASET_CATALOG.md is a research-reproducibility artifact**
  — lists exactly which public datasets the campaign's
  transcriptomic claims draw from. Without this catalog, verifying
  claims like "GSE184831 shows LAMP2 -2.7x" would require
  independent search.
- **3 medical/ top-level docs remain** (~760 lines): PRE_EXPOSURE_
  PREVENTION (117), PREVENTION_STRATEGY (235), DISEASE_DATA_SUMMARY
  (404). DISEASE_DATA_SUMMARY is the largest remaining.

## Tag

006 (medical/ top-level). Audited PATIENT_ZERO_SCREENING.md +
GEO_DATASET_CATALOG.md. 0 🔴, 4 🟡, **8 🟢**. SCREENING: 4-tier
panel with 19+ tests per tier, per-test normal/flag thresholds +
costs + availability caveats, Anti-TPO/Anti-TG2 with comorbidity
prevalence, decision tree for abnormal findings, C-peptide "KEY
measurement" consistent with THEWALL framing. GEO_CATALOG: source-
search JSONs threaded at top for reproducibility, explicit
DOWNLOADED/IDENTIFIED/PLATFORM legend, priority recommendations per
disease category, clear state labeling. **12 medical/ top-level docs
audited, 3 remain** (~760 lines): PRE_EXPOSURE_PREVENTION,
PREVENTION_STRATEGY, DISEASE_DATA_SUMMARY. Next fire.
