# Attempt 117 — Claim-Backing Audit: biology/evolution per-organism attempts 004, 007, 010

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue, Fire 45)
**Scope**: biology/evolution/attempts/attempt_004_hpv_evolution.md (344L,
sampled L1-90 + 280-344) + attempt_007_helicobacter_pylori_evolution.md
(366L, sampled L1-70 + 310-366) + attempt_010_malassezia_cutibacterium
_evolution.md (424L, sampled L1-80 + 370-424). Combined with Fire 44
(attempts 002, 003, 009), **6 of 9 per-organism attempts sampled**
across the biology/evolution/ series.
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: Fire 44 established citation-discipline gradient
(002/003 no PMIDs → 009 with PMIDs + VERIFICATION STATUS).

## Executive verdict

Fire 45 **reinforces and refines Fire 44's gradient finding**:

| Attempt | VERIFICATION STATUS tag | PMIDs in key sources | Inline audit-corrections |
|---------|------------------------|---------------------|-------------------------|
| 002 CVB | No | No | No |
| 003 EBV | No | No | No |
| 004 HPV | **Yes** | No (explicit "verify before clinical / manuscript use") | No |
| 007 H. pylori | **Yes** | No in key-sources | No |
| 009 Demodex | **Yes** | **Yes** (Smith 2022, Palopoli 2014) | **Yes** (Palopoli nuclear-vs-mito) |
| 010 Malassezia+C.acnes | **Yes** | **Yes** (Xu 2007 PMID 18000048, Wang 2015 PMID 25737592, Dagnelie 2019 PMID 31299116, Dréno 2018 PMID 29894579) | **Yes** (Tomida 2013 phylotype misattribution corrected) |

The series **progressively adopts math-standard citation practices**
within its own development cycle. attempt_010 is the strongest —
explicit "Key references (corrected 2026-04-15 audit)" section at
the bottom with the correction preserved inline (Maps-Include-Noise
compliance).

**🔴 RED count**: 0 (within sampled content)
**🟡 YELLOW count**: 5
**🟢 GREEN count**: 9

## YELLOW findings

| # | Location | Claim | Source gap |
|---|----------|-------|------------|
| Y261 | 004 L300 | zur Hausen Nobel Prize 2008 HR-HPV→cervical cancer | Verify — zur Hausen Nobel was 2008 Physiology/Medicine shared with Barré-Sinoussi + Montagnier |
| Y262 | 004 L302 | Gardasil 9 pivotal trial "Joura EA et al. various 2015+" | Thread specific PMID (Joura 2015 NEJM PMID 25693011 likely); vaccine-efficacy percentages in main body should attach to source |
| Y263 | 007 L366 | Maixner 2016 Science (Iceman H. pylori) | PMID 26744408 (verify); Iceman strain identified as hpAsia2 – hpNEAfrica hybrid |
| Y264 | 007 L366 | Linz 2007 Nature (H. pylori phylogeography) | PMID 17287725 (Linz 2007 Nature — "An African origin for the intimate association between humans and Helicobacter pylori") |
| Y265 | 010 L415 | Scholz & Kilian 2016 IJSEM 66(11):4422-4432 Cutibacterium rename | PMID ~27902180 range — thread explicitly (other entries in this ref list have PMIDs) |

## GREEN findings

- **G336** attempt_004 **"verify before clinical/manuscript use"
  explicit disclaimer** (L297-308): per-attempt honest labeling of
  AI-provenance at file level. Separates structural claims (high-
  confidence) from specific-number claims (audit-loop-flagged).
- **G337** attempt_004 L322-338 **updated attempt_001 claim**: adds
  "(b) lifecycle compartmentalization (→ small genome, but
  restricted to epithelial hosts)" to the framework's original
  "large-genome" prediction. HPV's 8 kb genome with epithelial-
  lifecycle persistence refines the framework. Parallels Fire 44
  finding of attempt_009 framework-reformulation mid-audit.
- **G338** attempt_007 **H. pylori phylogeography table** (L55-63):
  7 strain populations with human-population associations — out-
  of-Africa migration, Asian → Americas, Asian → Oceania — plus
  ~60,000 year coevolution bound. Clean structural biology-to-
  human-migration mapping.
- **G339** attempt_007 L308-311 **"attenuated-live H. pylori strain
  engineering has been proposed; no clinical deployment"** — honest
  status labeling of therapy frontier.
- **G340** attempt_007 L318-324 H. pylori two-phase protocol fits
  the cross-organism framework with **disease-specific complication
  flagged** (hypochlorhydria destabilizes reflux control). Framework-
  fits-most-organisms but per-organism-adjustments are named.
- **G341** attempt_010 L410-425 **"Key references (corrected
  2026-04-15 audit)"** section with Tomida 2013 phylotype-scheme
  misattribution caught and corrected inline ("Earlier write-up
  cited Tomida 2013 for the phylotype scheme; corrected — Tomida
  2013 is strain-level genomics, not the phylotype nomenclature").
  **File-level Maps-Include-Noise**: audit-correction preserved
  with old-vs-new rationale, not silently overwritten.
- **G342** attempt_010 **per-reference citation quality** — Xu 2007
  PMID 18000048, Wang 2015 PMID 25737592, Dagnelie 2019 PMID
  31299116, Dréno 2018 PMID 29894579. Specific numeric claims
  (IA1 84-96% in acne vs 36-42% healthy skin) attached to specific
  PMIDs. Math-standard citation discipline in final attempt.
- **G343** attempt_010 **ecosystem-level framing rationale**
  (L20-28): "Malassezia and C. acnes are typically treated in
  different clinical and research communities... Evolutionarily
  they are parallel stories... Treating them together in one
  attempt makes the ecosystem-level pattern visible." Explains
  why two organisms share one attempt — per-attempt scope-rationale
  honesty.
- **G344** attempt_010 L382-399 **"What's next for biology/evolution"
  section** — 4 specific synthesis directions named (meta-theorem
  taxonomy, therapeutic-convergence, host-immunity coevolution,
  comparative-timeline H.pylori-declining-vs-P.gingivalis-rising).
  Kill-ROI roadmap for future work.

## Recommended fixes (ordered)

1. **[P1]** Back-propagate attempt_010's inline-audit-correction
   pattern to attempts 002/003/004/007 — add "Key references
   (corrected 2026-04-15 audit)" sections with PMIDs. High value
   because CVB/EBV citations propagate across the medical corpus.
2. **[P2]** Thread PMIDs for attempt_004 (Joura 2015 Gardasil 9
   pivotal) + attempt_007 (Linz 2007 Nature PMID 17287725; Maixner
   2016 Science PMID 26744408) + attempt_010 Scholz 2016 Cutibacterium.
3. **[P3]** Consider a meta-attempt (attempt_011 or results/) that
   formalizes the 7 persistence-mechanism classes taxonomy per
   attempt_010's proposed follow-up.

## Non-audit observations

- **Fire 44 + Fire 45 together cover 6/9 per-organism attempts**
  (002 CVB, 003 EBV, 004 HPV, 007 H. pylori, 009 Demodex, 010
  Malassezia+C.acnes). Remaining: 005 HCMV, 006 HHV-6, 008
  P. gingivalis — ~1050 lines. Expected to fit the same gradient
  (early = no PMIDs, later = PMIDs + VERIFICATION STATUS + inline
  corrections).
- **attempt_010 is the exemplar for the per-organism series**. Its
  "Key references (corrected 2026-04-15 audit)" section is the
  single best example in the entire non-math corpus of file-level
  Maps-Include-Noise compliance — earlier misattribution (Tomida
  2013 phylotype) preserved with correction and rationale.
- **The PMID gradient is data about the authorship process itself**:
  the attempts were written in order (002 → 010), and citation
  discipline improved over the series. This is sigma v5 self-
  applicability visible in the artifact trail. The improvement
  pattern matches medical/t1dm attempt_036 quality step-change
  (Fire 10 observation) — different subdirs, same
  discipline-improvement pattern, same rough chronology.
- **The prior WebSearch-based audit** (per session summary) found
  1 fabrication (Liang 2018 pediatric chalazion recurrence) in the
  broader biology/evolution sweep. Today's structural audits
  (Fire 44 + 45) identified the **PMID-discipline gradient** as a
  compounding-error risk — if early attempts (002/003) have wrong
  citations that the WebSearch audit didn't catch (because author+year+
  journal was verifiable without PMID), those errors propagate to
  medical/ cross-references. Back-propagating attempt_010's pattern
  is the highest-leverage fix.

## Tag

117 (biology/evolution per-organism). Sampled 3 additional attempts
(004 HPV L1-90+280-344, 007 H.pylori L1-70+310-366, 010 Malassezia+
C.acnes L1-80+370-424). Combined with Fire 44, **6/9 per-organism
attempts now audited**; remaining 005 HCMV / 006 HHV-6 / 008
P. gingivalis (~1050 lines). **0 🔴** (within sampled content). 5 🟡
(zur Hausen Nobel 2008 verify, Joura 2015 Gardasil 9 pivotal PMID,
Maixner 2016 Science Iceman PMID, Linz 2007 Nature H. pylori PMID,
Scholz 2016 Cutibacterium PMID). **9 🟢**: attempt_004 "verify before
clinical/manuscript use" explicit disclaimer + updated-attempt_001-
claim refinement (HPV 8kb + epithelial-lifecycle persistence refines
framework); attempt_007 phylogeography table with 7 strain-populations
↔ human-migration mapping + 60ky coevolution bound; attempt_007
honest "no clinical deployment" status labeling for H. pylori
attenuated-vaccine; attempt_010 **"Key references (corrected
2026-04-15 audit)" section** — single best example in non-math
corpus of file-level Maps-Include-Noise (Tomida 2013 phylotype
misattribution preserved-and-corrected); attempt_010 per-reference
PMIDs for Xu 2007 / Wang 2015 / Dagnelie 2019 / Dréno 2018 with
specific IA1 84-96% vs 36-42% claims source-attached; attempt_010
ecosystem-level scope rationale; attempt_010 kill-ROI roadmap
(meta-taxonomy, therapeutic-convergence, host-immunity-coevolution,
comparative-timeline). **Gradient pattern confirmed across 6/9
attempts**: 002/003 (no PMIDs, no disclaimer) → 004 (disclaimer
only) → 007 (disclaimer, no PMIDs in key-sources) → 009/010 (both
+ inline corrections). **Highest-leverage fix**: back-propagate
attempt_010's inline-audit-correction pattern to attempts 002/003/004/
007 with PMIDs — CVB/EBV citations propagate across medical/
corpus; fixes compound. Next fire: remaining per-organism 005/006/008,
dysbiosis numerics, WHM sweep (pending op), or loop termination.
