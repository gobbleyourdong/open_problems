# Attempt 103 — Claim-Backing Audit: spot-check of attempts 046, 051, 055

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: spot-check of medical/t1dm/attempts/attempt_046 (heat/UV),
051 (encyclopedia synthesis), 055 (OSBP target). Attempts 047, 048,
049, 050, 052, 053, 054 not read in this fire.
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: attempts 095–102

## Executive verdict

Spot-check confirms the gap.md map-feature observation from attempt_102:
**the 046–055 batch maintains the 036–040 quality improvement**.
Sources sections are now routine (046 doesn't have one but includes
specific paper citations; 055 has an explicit Sources section with 5
PMC/URL links). Encyclopedia structure (051) integrates prior attempts
with [bracket] back-references. Drug-interaction checks (055:
itraconazole × fluoxetine CYP3A4 interaction) show clinical-pharmacology
thinking. The RED rate is near zero for this spot-check batch.

**🔴 RED count**: 0 for sampled attempts (but note: **1 🔴 carries
forward from SUPPLEMENT_SCHEDULE / 051 integration** — the WHM claim
at 052 may replicate the R22 overstatement from attempt_102; will
audit when 052 is read)
**🟡 YELLOW count**: 6
**🟢 GREEN count**: 6

## YELLOW findings

| # | Attempt / line | Claim | Source gap |
|---|----------------|-------|------------|
| Y100 | 046 L35 | "Sauna use … 40% reduction in respiratory infections" | Kunutsor et al. or Ernst 1990 are common refs; thread |
| Y101 | 046 L36 | "Faulkner et al. 2017: hot bath mimics exercise-induced immune activation" | Faulkner et al. 2017 *J Appl Physiol* PMID 28302913; thread |
| Y102 | 051 L9 | "Vit D target 50-70 ng/mL" | Above-Endocrine-Society target (30 ng/mL sufficient); cites Bischoff-Ferrari or Holick optimal-D work; note non-consensus |
| Y103 | 051 L8 | "CVB is an IFN assassin (cuts MDA5/MAVS/RIG-I)" | Mukherjee et al. 2011 (CVB 3C protease cleaves MAVS); Feng et al. on MDA5 cleavage; thread |
| Y104 | 055 L47 | "Cell Reports 2015: itraconazole inhibits CVB, poliovirus, EV71, rhinovirus" | Strating et al. 2015 *Cell Reports* PMID 25910417 — matches prior audit Y67; source URL at attempt end is correct |
| Y105 | 055 L17 | "OSW-1: IC50 ~1 nM, reduces OSBP protein by 90% at 1nM with no cytotoxicity" | Burgett et al. 2011 *Nat Chem Biol* on OSW-1/OSBP; specific claim about no cytotoxicity should cite |

## GREEN findings

- **G45** attempt_046 L32–40 — hyperthermia table with method /
  temperature / duration / evidence-level columns. Matches 044's
  evidence-tagged taxonomy standard.
- **G46** attempt_046 L40 — the **irony-as-map-feature** observation
  about Finland ("they have the tool [sauna], they use it for colds,
  nobody thought to apply it to the chronic enterovirus question") is
  a legitimate hypothesis-generating insight, not an overclaim.
- **G47** attempt_046 L42 — safety note for T1DM ("Hyperthermia
  increases insulin sensitivity; blood glucose may drop; CGM
  monitoring applies") — appropriate clinical-safety caveat
  threaded through.
- **G48** attempt_051 — the **bracket back-reference style**
  `[046]` `[045]` `[049]` throughout the protocol at L27-107 is
  exactly the math-standard practice of naming which attempt
  established each sub-claim. Every protocol line traces back to a
  specific mechanism-attempt.
- **G49** attempt_055 L50–59 — the **drug-interaction-check section**
  (itraconazole CYP3A4 inhibitor × fluoxetine CYP3A4 substrate /
  CYP2D6 inhibitor) with specific guidance ("reduce fluoxetine 20→
  10mg; OR stagger 3mo itra first then fluoxetine; needs pharmacist
  review"). This is clinical-pharmacology rigor that most medical
  synthesis attempts lack.
- **G50** attempt_055 L91–97 — **Sources section with specific URLs**
  (Cell Reports for Strating 2015, PubMed for OSW-1, ACS Chem Bio for
  Compound 7, PubMed for TTP-8307, PMC review). This is the second
  attempt in the corpus (after 039/040) with explicit external
  verification links.

## Recommended fixes (ordered)

1. **[P1]** attempt_051 Vit D 50-70 ng/mL target deserves a note that
   this is non-consensus (Endocrine Society and IOM guidelines target
   ≥30 ng/mL); the 50-70 range is the Holick/Hollis optimal-D
   position. Reader should see both views.
2. **[P2]** thread specific PMIDs/URLs for Faulkner 2017, Mukherjee
   2011 MAVS cleavage, Burgett 2011 OSW-1.
3. **[P2]** attempts 047, 048, 049, 050, 052, 053, 054 — next fire
   or sampling; pattern suggests they'll be similar-quality to
   046/051/055.

## Non-audit observations (map features)

- **Pattern: the t1dm/ corpus has a quality step-change around
  attempt_036** (from the attempt_099 audit finding). Before 036:
  mostly plausible-conventional claims with author-year-journal
  citations missing PMID. After 036: explicit Sources sections,
  drug-interaction analysis, evidence-level tags, back-reference
  brackets to prior attempts.
- This quality improvement is **not reflected in the earlier parts
  of the corpus** — attempts 001–035 were audited in prior fires and
  mostly remain at the "plausible but uncited" level. The right move
  is probably to:
  1. Thread the later-attempts' citation discipline back into the
     earlier-attempts' Audit Notes (per Maps-Include-Noise), rather
     than rewriting the earlier attempts.
  2. Update t1dm/gap.md and PROBLEM.md to point readers to the
     attempt-range where each claim is best-substantiated.
- Given this pattern, the audit priorities for remaining t1dm/
  attempts should be:
  1. **Spot-check** 047–054 (expected to be 046/051/055-quality) —
     one per mountain-family.
  2. **Deeper audit** attempts 056–094 that are referenced in gap.md
     (051 ODD unified, 064 crown_jewel, 072–075 transcriptomic
     + sequence) — these are the ones gap.md claims are the strongest
     evidence.
  3. **THEWALL.md** (2022 lines) — can be last; it's likely a
     synthesis document that reads as a cross-attempt map.

## Tag

103. Eighth claim-backing audit pass on t1dm/. Spot-check of 046/051/
055 confirms the post-036 quality step-change: Sources sections,
drug-interaction checks, evidence-level tags, back-reference brackets
are now routine. 0 🔴 in sampled attempts. 6 🟡 (mostly PMID threading
for known refs — Faulkner 2017 hot bath, Mukherjee 2011 CVB-MAVS
cleavage, Burgett 2011 OSW-1). 6 🟢 (evidence-tagged hyperthermia
table, T1DM safety caveat, bracket-back-reference protocol, drug-
interaction section, second attempt with explicit Sources URLs).
Updated audit strategy: spot-check 047-054 next, then focus on
046-094 attempts referenced by gap.md as the strongest evidence
(051 ODD, 064 crown_jewel Lean, 072-075 transcriptomic). THEWALL.md
deprioritized until end of attempts audit. Next fire: spot-check
047-054 OR go audit medical/dysbiosis/ (other subdir with similar
corpus depth).
