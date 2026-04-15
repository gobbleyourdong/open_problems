# Attempt 001 — Claim-Backing Audit: medical/ top-level CLINICAL_BRIEF + EVIDENCE_GRADES

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: medical/CLINICAL_BRIEF.md (122 lines) + EVIDENCE_GRADES.md
(171 lines). Other medical/ top-level docs (~13 files, ~2300 lines
total) sampled but not audited this fire.
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: audit log fires 1–26.

## Executive verdict

**These are the two strongest claim-backing documents in the
non-math corpus so far**, matching or exceeding physics/what_is_
time/gap.md's register.

**CLINICAL_BRIEF.md**: thesis in 3 sentences; evidence table with
per-claim grade (A-/B+/B/C/B+/Lean-certified/Not tested) + key
citation; safety concerns with severity (CRITICAL/HIGH/Moderate/
Low-moderate); drug-interaction warnings (itraconazole + colchicine
"fatal" labeled); three alternative proof paths with n + duration;
explicit "Honest Assessment" section with "weakest links."

**EVIDENCE_GRADES.md**: 5-level grading scale (A–E) with canonical
examples per grade; 10 core claims each with Strengths + Weaknesses
+ Verdict + grade-shift history; "Weakest Links ranked by impact if
wrong"; explicit RESOLVED / PARTIALLY RESOLVED strikethroughs showing
the campaign's intellectual history preserved.

The EVIDENCE_GRADES.md **grade-shift table** (pre-bioinformatics vs
post-bioinformatics) is a **live Maps-Include-Noise artifact** —
prior claim grades are preserved while new evidence updates them.
This is sigma method v5 self-applicability in document form.

**🔴 RED count**: 0 (both docs actively audit themselves)
**🟡 YELLOW count**: 5
**🟢 GREEN count**: 12

## YELLOW findings

| # | File / line | Claim | Source gap |
|---|-------------|-------|------------|
| Y185 | CLINICAL_BRIEF L17 | "Tissue concentrations 1.2–4.5x above IC50 at 20mg" via "brain 15x (Bolo 2000 ¹⁹F-MRS), testes 7.5x (Tanrikut 2010)" | Verify Bolo 2000 (¹⁹F-MRS brain fluoxetine) and Tanrikut 2010 (testes) — these are the specific refs resolving the R16 Cmax concern; if they hold, fluoxetine dose adequacy is defensible |
| Y186 | CLINICAL_BRIEF L35 | "Fluoxetine 20mg daily (40–60mg in males for testicular clearance)" | 40-60mg is escalation; Lexapro-class SSRI dose range but needs specific rationale for testicular concentration vs 20mg baseline |
| Y187 | EVIDENCE_GRADES L82 | "GSE293840 (n=168): 6/7 model predictions confirmed" — ME/CFS grade upgraded C- → C | Accession + specific citation; matches fire 13's Y121 concern |
| Y188 | EVIDENCE_GRADES L131 | "the 30% recurrence may not be CVB-driven in all cases" weakness for Claim 6 | Pericarditis recurrence-etiology split (viral vs autoimmune vs idiopathic) — specific ref (Imazio guidelines or COPE trial secondary analysis) |
| Y189 | EVIDENCE_GRADES L76 | "Kühl 2003 (Circulation): IFN-β clears enterovirus from DCM hearts (n=22)" as Grade-B claim | Same as myocarditis audit Y130 — thread PMID 14744960 consistently across subdirs |

## GREEN findings

- **G176** CLINICAL_BRIEF L7 — **thesis in 3 sentences** with
  mechanism + drugs + prediction. Same shape as math/ns_blowup's
  single-sentence-gap statement.
- **G177** CLINICAL_BRIEF L11–30 — **evidence table with per-claim
  grade + specific citation**. A-, B+, B, C, Lean-certified, Not
  tested. Each row is one claim, one grade, one source.
- **G178** CLINICAL_BRIEF L67–75 — **safety-concern table with
  severity rating + mitigation per concern**. "Itraconazole +
  colchicine: CRITICAL — fatal interaction" is exactly the clinical
  rigor this corpus aspires to.
- **G179** CLINICAL_BRIEF L77–92 — **three alternative proof paths
  with n + duration** (n=1 patient 3-6mo; pericarditis RCT n=195
  18mo; ME/CFS cfRNA n=30 16 weeks). Operationalized next-action
  options.
- **G180** CLINICAL_BRIEF L94–109 — **"Honest Assessment"** section
  naming the campaign's progression from "mechanistically sound,
  clinically unproven" to "mechanistically sound, transcriptomically
  validated … **clinically unproven**" — the unproven part is kept
  in the label.
- **G181** CLINICAL_BRIEF L113–122 — **"Where to Start Reading"**
  cross-reference table directing reader to specific subdirs by
  interest (unifying thesis → MEDICAL_PROBLEMS; T1DM cure → t1dm/
  THEWALL; transcriptomic validation → results/pattern_015–017; drug
  safety → DRUG_SAFETY_MATRIX; honest uncertainty → EVIDENCE_GRADES,
  FAILURE_MODES). Directory-entry-point discipline.
- **G182** EVIDENCE_GRADES L5–13 — **5-level grading scale with
  canonical example per grade**: A = Proven in humans replicated
  mechanistically understood (Colchicine pericarditis COPE); B =
  Demonstrated in humans limited replication; C = animal/in vitro;
  D = mechanism plausible no evidence; E = speculative inference.
  This is the math-standard "explicit grading rubric applied
  consistently" pattern.
- **G183** EVIDENCE_GRADES — **every claim** has Strengths bullet +
  Weakness bullet + Verdict one-line. Even Grade A claims have
  Weaknesses stated.
- **G184** EVIDENCE_GRADES L138–148 — **Grade-shifts table** with
  per-claim pre-bioinformatics vs post-bioinformatics grade and
  "what changed" column. This is **explicit Maps-Include-Noise
  compliance at the grade level** — prior grades preserved while
  new evidence updates them.
- **G185** EVIDENCE_GRADES L122–132 — **"Weakest Links ranked by
  impact if the claim is WRONG"** — inverse-prioritized. Not "what
  are we most sure of" but "what breaks most if we're wrong." Sigma-
  method kill-ROI discipline.
- **G186** EVIDENCE_GRADES L156–162 — **RESOLVED / PARTIALLY RESOLVED
  with strikethroughs** of original weakest-link items. Audit trail
  of what was a problem vs what's now fixed. Living document.
- **G187** EVIDENCE_GRADES Claim 5 Grade D+ → C upgrade (L65–67) —
  "the R > D inequality is a framework, not a measured equation …
  neither R nor D is directly measured." This is **honest self-
  downgrade of the campaign's flagship mathematical model**. The
  d(Beta)/dt = R - D framing is labeled D+ → C not A — it's a
  usable framework but not a proven equation. Rare honesty.

## Recommended fixes (ordered)

1. **[P1]** CLINICAL_BRIEF Y185: verify Bolo 2000 ¹⁹F-MRS fluoxetine
   brain accumulation (15×) and Tanrikut 2010 testes fluoxetine
   accumulation (7.5×) — these are the specific references resolving
   R16's Cmax concern. If both hold, the fluoxetine dose-adequacy
   claim is defensible; if either is misattributed or the numbers
   are wrong, R16 reopens.
2. **[P2]** Thread specific references for Y186 (40-60mg testicular
   dose rationale), Y187 (GSE293840 accession), Y188 (pericarditis
   etiology split), Y189 (Kühl 2003 PMID).

## Non-audit observations

- These two docs + t1dm/gap.md + physics/what_is_time/gap.md +
  biology/evolution/PROBLEM.md are the **5 strongest claim-backing
  documents in the non-math corpus**. All 5 share common features:
  single-sentence gap + grade rubric + explicit weaknesses + live
  grade/status updates + cross-subdir references.
- **CLINICAL_BRIEF.md and EVIDENCE_GRADES.md would function as
  standalone artifacts** if the rest of the repo were deleted. A
  physician reading only these two files has enough to evaluate
  whether the protocol is worth pursuing and knows exactly what
  would falsify each claim.
- The **"what changed" column** in EVIDENCE_GRADES L138–148 is a
  template other non-math subdirs could adopt. When a claim moves
  grades, the reason should be recorded in-place with the old grade
  preserved.
- **Remaining medical/ top-level docs to audit**: MEDICAL_PROBLEMS
  (84), PRE_EXPOSURE_PREVENTION (117), PATIENT_ZERO_SCREENING (141),
  CONVERGENCE (158), FAILURE_MODES (160), GEO_DATASET_CATALOG (178),
  DRUG_SAFETY_MATRIX (190), CVB_VACCINE_STRATEGY (204), PREVENTION_
  STRATEGY (235), PATIENT_ZERO_TIMELINE (330, contains R26 WHM),
  DISEASE_DATA_SUMMARY (404). Total ~2300 lines.

## Tag

001 (medical/ top-level). Audited CLINICAL_BRIEF.md + EVIDENCE_
GRADES.md — **the two strongest claim-backing documents in the
non-math corpus**. 0 🔴 (both docs actively audit themselves).
5 🟡 (Bolo 2000/Tanrikut 2010 tissue-PK source verification, 40-
60mg testicular-clearance dose rationale, Kühl/GSE293840 PMID
threading). **12 🟢**: thesis in 3 sentences; grade-per-claim
evidence table; severity-rated safety-concern table with
CRITICAL/HIGH/Moderate labels; three alternative proof paths with
n+duration; Honest Assessment section; directory-entry-point
Where-to-Read cross-ref table; 5-level A–E grading scale with
canonical examples; every claim has Strengths + Weaknesses +
Verdict; **grade-shifts table preserves pre-bioinformatics vs
post-bioinformatics grades with "what changed" column** — live
Maps-Include-Noise; Weakest-Links-ranked-by-impact-if-wrong
(inverse priority); RESOLVED/PARTIALLY RESOLVED strikethroughs;
Claim 5 honest D+ → C grade for the d(Beta)/dt = R - D flagship
inequality model ("neither R nor D is directly measured"). Next
fire: remaining medical/ top-level docs (13 files, ~2300 lines),
biology/evolution attempts, or WHM sweep (pending op go-ahead).
