# Attempt 001 — Claim-Backing Audit: persistent_organisms/PROBLEM.md + README.md

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue, Fire 53)
**Scope**: medical/persistent_organisms/PROBLEM.md (166L) + README.md
(84L) = 250L total. New subdir, untracked per git status.
attempts/results/papers all empty (planned, not populated).
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: Fire 52 audited blepharitis 006-008; biology/evolution/
audit complete (Fires 44-51). This subdir is the medical-side
complement to biology/evolution/.

## Executive verdict

**Clean framework-launch document.** PROBLEM.md establishes the
8-organism × two-phase architecture + Phase 0 shape-check + work plan
+ cross-directory mapping. README.md provides compact navigation.
Both files are structurally sound, well-cross-referenced, and honest
about scope. Content is intentionally thin (framework doc + nav,
not per-organism depth — that lives in per-disease dirs).

**Key structural strength**: the 8-organism table (PROBLEM.md L37-48)
is the **cross-cutting clinical decision table** — organism ×
persistence niche × key chronic diseases × clearance agent × adjunct.
This is the medical-side analog to biology/evolution/results/
persistence_mechanisms_taxonomy.md's 7-class table. Between the two,
organism → evolutionary class → persistence niche → disease →
clearance + adjunct is readable end-to-end.

**🔴 RED count**: 0
**🟡 YELLOW count**: 4
**🟢 GREEN count**: 9

## YELLOW findings

| # | Location | Claim | Source gap |
|---|----------|-------|------------|
| Y301 | PROBLEM L42 "tenofovir alafenamide (experimental)" for EBV | TAF is anti-HIV/HBV; anti-EBV use is investigational — acknowledge off-label status more explicitly; cite any trial or case-report |
| Y302 | PROBLEM L41 "COR388 trialed" for P. gingivalis Alzheimer's | Consistent with R28 (COR388 overstated) + C23 (GAIN trial primary endpoint failed 2021) + Y269 (mixed results). Should note trial failure + Cortexyme → Quince pivot |
| Y303 | PROBLEM L56-58 "Clearance agents exist for most; efficacy varies. HPV is preventable by vaccine but not curable-once-established. CVB has no dedicated antiviral yet (fluoxetine repurposed)" | Honest but could note EBV similarly lacks effective clearance agent for established latency (valacyclovir weak; no established clearance for latent EBV) |
| Y304 | README L66-69 Three examples of "self-sustaining inflammatory loop after clearance" | KLK5/LL-37 (rosacea/blepharitis), NLRP3/IL-1β (T1DM), citrullination/anti-CCP (RA) — all per-organism loop-independence claims should cite specific evidence (Yamasaki 2007 for KLK5, Youm 2015 for NLRP3, Wegner 2010 for PPAD citrullination) |

## GREEN findings

- **G428** PROBLEM.md **8-organism × 5-column table** (L37-48):
  organism / persistence niche / key chronic diseases / clearance
  agent / adjunct. Cross-cutting clinical decision table. Compact
  + actionable + each row traces to specific per-disease dirs.
- **G429** PROBLEM.md **Phase 0 shape-check** (L51-72): all 5
  sigma-method questions answered honestly (mechanism known?
  treatments exist? wall crossable? behavioral changes? who has
  tried?). Classification: "Mixed mechanism + behavioral wall"
  with explicit cross-reference to dysbiosis phase0_recheck.
- **G430** PROBLEM.md **"Why this directory exists" 3 reasons**
  (L76-94): cross-organism synergy (real patients polymicrobially
  infected), shared therapeutic architecture (two-phase collapses
  disease-specific → organism-specific), differential diagnosis
  (organism identification route). Each reason is operationally
  specific.
- **G431** PROBLEM.md **biology/evolution/ relationship** (L127-135):
  "biology/evolution/ asks: *why did these organisms evolve to
  persist?*; this directory asks: *given that they persist and cause
  disease, what do we do about it?*" Clean scope separation. Two-
  directory complementary framing.
- **G432** PROBLEM.md **work plan** (L138-153): 4 planned attempts
  with per-attempt scope sentence: two-phase architecture detail,
  differential diagnosis by organism, coinfection problem, per-
  organism deep-dives for P. gingivalis / EBV / H. pylori / HPV.
  Roadmap for content expansion.
- **G433** PROBLEM.md **per-organism existing-work mapping table**
  (L112-121): organism → existing per-disease dirs. Explicit gap:
  P. gingivalis, EBV, H. pylori, HPV have "None dedicated."
  Honest map of what exists vs what doesn't.
- **G434** README.md **two-phase architecture with 3 self-sustaining-
  loop examples** (L56-74): KLK5/LL-37 continues after Demodex
  clearance, NLRP3/IL-1β continues after CVB clearance,
  citrullination/anti-CCP continues after P. gingivalis treatment.
  "Duration of adjunct: months. Often this is the longer, more
  load-bearing phase. Skipping adjunct is why many 'successful'
  clearance treatments produce symptom regression." — **This is
  the framework's operational thesis in 3 sentences.**
- **G435** README.md **"this directory does not duplicate that work;
  it references it"** (L45): scope discipline. Framework synthesis
  dir doesn't repeat per-disease content.
- **G436** Both files **cross-reference each other + biology/
  evolution/ + medical/blepharitis/ + medical/dysbiosis/**. Cross-
  directory integration explicit at file level.

## Recommended fixes (ordered)

1. **[P2]** Y302 — update COR388 entry to note GAIN trial failure
   + Cortexyme→Quince pivot. Consistent with prior audit findings
   R28/C23/Y269.
2. **[P2]** Y301 — clarify TAF for EBV is investigational/off-label
   (no established trial) vs HIV/HBV standard-of-care.
3. **[P3]** Y304 — thread PMIDs for the 3 self-sustaining-loop
   examples (Yamasaki 2007 PMID 17676051, Youm 2015 PMID 25686106,
   Wegner 2010 PMID 20068034 PPAD citrullination RA).

## Non-audit observations

- **medical/persistent_organisms/ is a clean launch** — 250 lines,
  2 files, proper directory structure, honest "Status: created
  2026-04-15, content expansion follows" labeling. No overclaimed
  content; just framework + nav.
- **The planned attempt_002 (differential diagnosis by organism)**
  would be high-value clinical content — a structured screening
  protocol that asks "which of the 8 organisms is driving this
  patient's chronic inflammation?" This would connect to medical/
  t1dm/PATIENT_ZERO_SCREENING.md and blepharitis/attempt_007's
  species-differential approach.
- **Empty attempts/results/papers dirs** are the expected state for
  a just-created framework dir. They become useful as the work plan
  (PROBLEM.md L138-153) executes. No need to flag as missing.
- **8-organism table + two-phase architecture** together constitute
  the framework's **minimum viable product** — any clinician reading
  PROBLEM.md L37-48 + README.md L56-74 gets the core claim and
  treatment pattern in <5 minutes.

## Tag

001 (persistent_organisms). Audited PROBLEM.md (166L) + README.md
(84L) = 250L total. **0 🔴**. 4 🟡 (TAF for EBV is investigational
not established, COR388 should note GAIN failure per R28/C23/Y269,
EBV clearance gap parallel to CVB, 3 self-sustaining-loop examples
need PMIDs Yamasaki/Youm/Wegner). **9 🟢**: 8-organism × 5-column
clinical decision table (cross-cutting analog to biology/evolution/
taxonomy); Phase 0 shape-check all 5 questions answered; "Why this
directory exists" 3 operational reasons; biology/evolution/ clean
scope separation; 4-attempt work plan; existing-work mapping with
honest "None dedicated" gaps; **two-phase architecture operational
thesis in 3 sentences** ("skipping adjunct is why many 'successful'
clearance treatments produce symptom regression"); scope discipline
("does not duplicate; references"); cross-directory integration
explicit. **Observation**: persistent_organisms/ is a clean
framework launch (250L, 2 files) that constitutes the **minimum
viable product** of the persistent-organism clinical framework —
8-organism table + two-phase architecture readable in <5 minutes.
Planned attempt_002 (differential diagnosis by organism) would be
highest-value next content. Next fire: dysbiosis numerics (~169
runs, largest unaudited corpus), WHM sweep (pending op), or
loop-termination assessment.
