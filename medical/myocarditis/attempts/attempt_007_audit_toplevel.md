# Attempt 007 — Claim-Backing Audit: myocarditis/ + cross-subdir scaffolded-stub survey

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: medical/myocarditis/PROBLEM.md (41 lines), gap.md (100
lines). Plus **breadth survey** of 8 "Phase 0 scaffolded" CVB-family
subdirs (hepatitis, pleurodynia, pancreatitis, aseptic_meningitis,
encephalitis, orchitis, neonatal_sepsis, thyroiditis).
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: audit log fires 1–13.

## Executive verdict

**myocarditis/ has a substantive gap.md with specific quantitative
predictions** from an ODD model (cardiac clearance 4.5 mo, LVEF
recoverable +10–23%, 7/7 T1DM protocol components transfer).
PROBLEM.md is labeled "Phase: 0 (Scaffolded)" — lightweight by
design. The substantive work is in gap.md.

**The 8 Phase-0-scaffolded subdirs** (hepatitis, pleurodynia,
pancreatitis, aseptic_meningitis, encephalitis, orchitis,
neonatal_sepsis, thyroiditis) are intentional stubs for CVB-family
diseases not yet worked by the campaign. They have brief PROBLEM.md
(22–34 lines), minimal gap.md, and a "Phase: 0 (Scaffolded)" marker.
Audit-wise: these should not be treated as research synthesis with
load-bearing claims. They are placeholder scaffolds with the
correct structural form but no deep claims yet.

**🔴 RED count**: 0 (myocarditis); scaffolded stubs not applicable
**🟡 YELLOW count**: 6 (myocarditis)
**🟢 GREEN count**: 8 (myocarditis + overall structural observation)

## YELLOW findings (myocarditis/)

| # | File / line | Claim | Source gap |
|---|-------------|-------|------------|
| Y126 | PROBLEM L14 | "2A protease … Cleaves dystrophin in cardiomyocytes" | Badorff et al. 1999 *Nat Med* PMID 10482120 — canonical cite, thread |
| Y127 | PROBLEM L18 | "Molecular mimicry: cardiac myosin ↔ viral epitopes" | Fairweather / Rose / Cihakova cardiac-autoimmunity work; thread |
| Y128 | gap.md L5 | "Cardiac clearance time: 0.37 years (4.5 months) with full protocol" | ODD model output; cite the specific model file (e.g., `numerics/<ODD-file>.md`) as math-style named-source |
| Y129 | gap.md L11–14 | "Pre-fibrotic: LVEF recoverable (+10-23%)" | Specific numeric range — either ODD output (cite model file) or clinical literature (Caforio / ESC guidelines); thread |
| Y130 | gap.md L9 | "Kühl precedent validated by model: IFN-β equivalent achievable with oral fluoxetine" | Kühl et al. 2003 *Circulation* PMID 14744960 (IFN-β in chronic viral cardiomyopathy); thread |
| Y131 | gap.md L74 | "Most acute myocarditis resolves (60-70%)" | Standard clinical-teaching number; cite ESC position paper (Caforio 2013) or specific cohort study |

## GREEN findings

- **G79** myocarditis gap.md L21–34 — **Critical Difference From
  T1DM** section correctly identifies that the regeneration term is
  ~0 in adult cardiomyocytes, so the "tip the balance" framing
  doesn't directly apply. This is honest cross-disease calibration
  — the protocol transfers partially, not wholly.
- **G80** myocarditis gap.md L52–69 — **Fork A / Fork B / Fork C**
  structure (early intervention / late intervention / prevention)
  with specific criteria for each. Matches sigma's Multiple Mountains
  principle (v2) applied to a single disease's intervention timing.
- **G81** myocarditis gap.md L82–86 — **specific clinical next-step
  for the patient**: cardiac MRI with late gadolinium enhancement
  (LGE) to detect subclinical myocarditis/fibrosis, with LGE-positive
  vs LGE-negative branching. Actionable, specific, clinically
  grounded.
- **G82** myocarditis gap.md L90–100 — **7/7 T1DM protocol components
  with myocarditis-specific benefit** table. Inherited-framework
  application table is explicit and falsifiable.
- **G83** scaffolded-stubs pattern — the 8 Phase-0 subdirs (hepatitis,
  pleurodynia, pancreatitis, aseptic_meningitis, encephalitis,
  orchitis, neonatal_sepsis, thyroiditis) **correctly identify
  themselves as scaffolded** via "systematic approach Phase: 0
  (Scaffolded)" markers. This is Maps-Include-Noise compliant — the
  stubs exist as placeholders without pretending to be deep synthesis.
- **G84** Cross-reference pattern — each scaffolded stub has a
  "Connection to T1DM" section that correctly identifies the shared
  CVB mechanism and what would transfer from the T1DM protocol if
  that subdir were worked. This preserves the campaign's umbrella
  structure even for un-worked diseases.
- **G85** hepatitis/PROBLEM.md L19–21 — pragmatic cross-subdir note:
  "Liver inflammation may impair drug metabolism (relevant for
  itraconazole, fluoxetine dosing)" — practical clinical awareness
  that liver-status affects the protocol's drug components.
- **G86** pleurodynia/PROBLEM.md L18–20 — "A sentinel: if you had
  unexplained chest/rib pain before T1DM diagnosis, it may have
  been pleurodynia" — converts a CVB-family disease into a
  diagnostic historical question for the T1DM case history.

## Recommended fixes (ordered)

1. **[P1] myocarditis/gap.md** Y128–Y130: thread ODD-model file ref
   for the 4.5-mo and +10-23% LVEF numbers; thread Kühl 2003
   Circulation PMID for the IFN-β reference.
2. **[P1] myocarditis/PROBLEM.md** Y126–Y127: thread Badorff 1999
   Nat Med (dystrophin cleavage by 2A protease) and Fairweather/Rose
   work (cardiac myosin mimicry).
3. **[P2] Scaffolded stubs**: none needed at this stage — stubs
   correctly marked. When any of these subdirs are worked beyond
   Phase 0, the audit should revisit.

## Non-audit observations (map features)

- **The scaffolded-stub pattern is a positive**: it preserves the
  campaign's umbrella structure (CVB hits many organs) without
  inflating Phase-0 placeholders into false research synthesis.
  Other campaigns (outside this repo) often have the opposite
  problem — thin content dressed up as full synthesis. The Phase: 0
  marker here is a self-classifying discipline.
- myocarditis/ is **the right structure for a CVB-family subdir**
  once worked past Phase 0: inherits protocol from T1DM, explicitly
  notes where the inheritance breaks (regeneration difference), adds
  disease-specific intervention timing (Fork A/B/C), and provides
  actionable clinical next-step (MRI-LGE).
- The **"keystone disease" claim** (gap.md L5: "Myocarditis is the
  keystone disease in the disease network (pattern 008) — clearing
  cardiac CVB has largest downstream impact") is a strong
  cross-subdir claim that should be audited against the referenced
  dysbiosis/numerics/pattern_008 file in a future fire.

## Audit queue update

Scaffolded-stub subdirs (hepatitis, pleurodynia, pancreatitis,
aseptic_meningitis, encephalitis, orchitis, neonatal_sepsis,
thyroiditis) — mark as **AUDITED-SCAFFOLDED** in AUDIT_LOG.md queue.
No further audit needed until any of them is worked past Phase 0.

Remaining mature medical subdirs to audit:
- eczema/ (4 attempts, 83/55/266 line PROBLEM/gap/THEWALL)
- psoriasis/ (5 attempts, 90/84/240)
- dilated_cardiomyopathy/ (5 attempts, 38/66/131)
- pericarditis/ (4 attempts, 24/40/114)
- infertility/ (4 attempts, 100/81/NA)
- blepharitis/ (new, see MEMORY.md)
- persistent_organisms/ (new, see MEMORY.md)

## Tag

007 (myocarditis). First audit pass on medical/myocarditis/ + breadth
survey of 8 Phase-0-scaffolded CVB-family subdirs. 0 🔴 in myocarditis
(scaffolded stubs not applicable). 6 🟡 (myocarditis: Badorff 1999
dystrophin cleavage, Kühl 2003 IFN-β, Caforio 2013 for acute
myocarditis resolution rate, specific ODD-model file references for
the 4.5-mo and LVEF numbers). **8 🟢**: myocarditis's Critical-
Difference-From-T1DM honesty (cardiomyocyte regeneration ~0), Fork
A/B/C intervention-timing structure, actionable MRI-LGE next step,
7/7 T1DM-protocol transfer table, scaffolded-stubs correctly marked
with "Phase: 0 (Scaffolded)", cross-reference to T1DM protocol in
each stub, hepatitis liver-drug-metabolism note, pleurodynia
"sentinel" framing for T1DM history. **Scaffolded stubs are audit-
complete as stubs — mark 8 subdirs AUDITED-SCAFFOLDED.** Next fire:
eczema OR psoriasis OR dilated_cardiomyopathy.
