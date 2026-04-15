# Attempt 007 — Claim-Backing Audit: perioral_dermatitis/ top-level

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: medical/perioral_dermatitis/PROBLEM.md (127 lines), gap.md
(70 lines), THEWALL.md (379 lines — includes Phase 4 dysbiosis
framework cross-pollinations at L198–380).
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: audit log attempts 095–103 (t1dm), dysbiosis attempt_020.

## Executive verdict

POD/ is the **canonical sigma-method behavioral-wall example** (named
in SIGMA_METHOD.md v7 Phase 0 section). Its top-level files reflect
this: PROBLEM.md is clean clinical-facts + differential-diagnosis +
treatment tiers; gap.md states specific mechanistic gaps with testable
predictions; THEWALL.md correctly identifies the wall as caregiver-
compliance with 1-3 week steroid-rebound flare, and contrasts Wall
Type A (steroid rebound) vs Wall Type B (environmental trigger
identification) with diagnostic distinction.

The Phase 4 dysbiosis-framework imports at THEWALL.md L198–380 extend
the molecular mechanism (KLK5/LL-37/NLRP3 triple-rebound, TRPV1
neurogenic burning, zinc deficiency, C. acnes/Loop-4, Urolithin A
mitophagy) with specific compound doses and timing — this is where
most of the audit concerns concentrate.

**🔴 RED count**: 2
**🟡 YELLOW count**: 7
**🟢 GREEN count**: 8

## RED findings

### R25 — THEWALL.md L115–117 (resolution-rate estimates)

**The claim**:
> "Resolution rate with full protocol compliance: estimated >90%
> based on the mechanistic coverage (all four mountains addressed
> simultaneously).
> Resolution rate with typical compliance: estimated 50-70% because
> most caregivers break at week 1-2 and reapply steroids.
> Resolution rate with no intervention beyond stopping steroids: ~60%
> in 6 weeks but with higher recurrence rate because contact triggers
> remain."

**Why load-bearing**: resolution-rate numbers anchor the POD
directory's claim that "the biology is solved" and the remaining work
is behavioral. If the >90% rate is not data-supported, the entire
"research problem closed" framing in the Summary (L188–190) is
overconfident.

**Concern**: all three numbers are labeled "estimated" but presented
alongside specific percentages. No observational-cohort source (POD
clinical registry, dermatology case series, RCT) is cited. The ">90%
based on mechanistic coverage" phrasing implies logical derivation
from the 4-mountain model rather than empirical observation — a model
doesn't give you a resolution rate.

**Required fix**:
1. Either find a POD cohort study or case series to thread (Hall &
   Reichenberg 2010 *J Drugs Dermatol* is a common POD review with
   some rate data; Eichenfield guidelines on pediatric POD may have
   observational rates).
2. Or explicitly label as "model-projected resolution rate,
   unvalidated — the number predicts what SHOULD happen if the
   mechanism is correct, not what has been MEASURED."
3. Replace the "typical compliance 50-70%" and "no intervention ~60%"
   with wider ranges (e.g., "30-70%") or remove the specific numbers
   if no source supports them.

### R26 — THEWALL.md L198–380 (Phase 4 dysbiosis imports — dose
extrapolation to POD without clinical evidence in POD)

**The claim**: multiple specific compound/dose recommendations imported
from dysbiosis/numerics/run_NNN with mechanistic rationale:
- "Topical niacinamide 4% cream BID" (L263–264)
- "Capsaicin 0.025% BID × 4 weeks" (Week 8+, L317–322)
- "Zinc glycinate 25-30mg/day if deficient" (L253)
- "S. salivarius K12 lozenge" (L349–353)
- "Urolithin A supplementation" (L376–377)
- Contraindication: "Blue light phototherapy in perioral POD" (L288–
  297)
- Contraindication: "Chlorhexidine + doxycycline" (L356–360)

**Why load-bearing**: these recommendations are carried as protocol
components in a document classified as "THE WALL" (i.e., the anchor
doc for the directory). A reader taking this as clinical-grade
guidance has specific doses with specific justifications.

**Concern**:
1. Each recommendation has **mechanistic rationale grounded in
   dysbiosis/ numerics** (all 7 run_NNN references verified to exist
   as files in dysbiosis/numerics/).
2. **None have clinical evidence IN POD specifically.** The
   compound/dose pairings come from general dermatology literature
   (niacinamide for rosacea, capsaicin for notalgia paresthetica,
   S. salivarius K12 for oral health) extrapolated to POD via the
   shared dysbiosis framework.
3. The blue-light contraindication in particular (L288–297) is a
   strong clinical claim ("contraindicated in perioral area during
   active POD") that extrapolates from C. acnes porphyrin biology +
   NLRP3 priming — plausible but not demonstrated in POD.
4. Format of these sections as standalone imports with dated update
   stamps ("Updated: 2026-04-12 | ...") preserves the audit-trail
   but the integrated document reads as a unified clinical protocol.

**Required fix**: add a banner at THEWALL.md L198 (start of Phase 4
imports) clarifying that the subsections below are **mechanistic
extrapolations from the dysbiosis framework to POD**, not
POD-specific clinical evidence. Compound/dose specifics are
hypothesis-grade. Same Maps-Include-Noise compliance pattern as
dysbiosis/gap.md's archive pointer.

## YELLOW findings

| # | File / line | Claim | Source gap |
|---|-------------|-------|------------|
| Y113 | THEWALL L233 | "LL-37 rebound → direct TRPV1 agonist (Buhl 2017 J Allergy Clin Immunol)" | Citation partially threaded — should verify exact Buhl/year/journal; Buhl et al. 2017 exists in allergy journals but specific LL-37/TRPV1 paper attribution needs confirmation |
| Y114 | THEWALL L251 | "Acrodermatitis enteropathica produces perioral lesions clinically similar to POD" | Need a dermatology ref (Neldner, Moynahan are foundational); thread |
| Y115 | PROBLEM L116 | "Pimecrolimus has a black box warning … real-world pediatric data over 20+ years show no increase" | Real-world data exists (Sigurgeirsson 2015 *Pediatrics*) but specific ref should be threaded |
| Y116 | gap.md L6 | "No mechanism explains this [clear zone around vermillion]" | Accurate current-state claim — no PubMed search returns a canonical explanation. Preserve as GREEN-for-honesty. |
| Y117 | THEWALL L272–275 | "Topical vitamin E can cause contact dermatitis in perioral zone" | Common clinical knowledge but cite (Perrenoud et al. 1994 on vitamin E patch-test sensitization) |
| Y118 | THEWALL L314–315 | "Azelaic acid weeks 1-4 during steroid withdrawal" — appears in Capsaicin Desensitization timeline | Azelaic acid isn't in the Tier 2 list in PROBLEM.md L80 at the same prominence; internal inconsistency — either promote azelaic acid to Tier 2 explicitly or remove from the timeline |
| Y119 | THEWALL L356–360 | "Chlorhexidine + doxycycline → oral Candida overgrowth risk" | Pharmacology claim; cite specific dental/ID ref |

## GREEN findings

- **G61** PROBLEM.md L43–56 — **Underreported clinical features**
  section with diurnal pattern, environment correlation, mechanical
  amplification, oral habits/toy-mouthing, post-meal worsening. This
  is tacit clinical knowledge converted to explicit diagnostic
  signals — exactly the v5 "Verify Before Acting" discipline applied
  to POD diagnosis.
- **G62** PROBLEM.md L60–67 — differential diagnosis table with
  distinguishing feature per condition. Matches math-standard
  comparison-table format.
- **G63** gap.md — **the clear-zone question is named as an
  unresolved gap** with 4 candidate hypotheses and explicit statement
  "none of these have been tested in POD specifically." This is the
  sigma-method "formalize the dead ends" discipline — the gap is
  preserved without a fake answer.
- **G64** THEWALL.md L42–68 — **Wall Type A (rebound compliance) vs
  Wall Type B (environmental trigger identification)** distinction
  with diagnostic signals that distinguish them. Wall Type B "is
  actually harder" framing correctly identifies that most clinicians
  don't ask the diagnostic questions that Wall B requires.
- **G65** THEWALL.md L104–117 — **week-by-week expected trajectory**
  of the protocol with specific observation markers. Matches
  math-standard "what to observe at each step" precision.
- **G66** THEWALL.md L125–159 — **verbatim written instructions for
  caregivers** to take home. This is the wall-breaking intervention
  as a deliverable, not a research note. Maps-Include-Noise
  compliant (the intervention is a map feature, not a research
  hypothesis).
- **G67** THEWALL.md L163–172 — **structural similarity to other
  iatrogenic rebound cycles** (PPI rebound, decongestant rebound,
  opioid-induced hyperalgesia, topical steroid withdrawal in atopic
  dermatitis). Cross-disease pattern recognition matches sigma
  method's "standing wave across domains" observation.
- **G68** THEWALL.md L198–380 — cross-references to **7 specific
  dysbiosis/numerics/run_NNN_*.md files** (run_015, 024, 025, 038,
  042, 051, 078) — all verified to exist. This is exactly the
  math-standard "cite the specific script / specific theorem" pattern
  translated to dysbiosis-numerics. Despite R26 concern about clinical
  evidence gap, the mechanistic traceability is exemplary.

## Recommended fixes (ordered)

1. **[P0] THEWALL.md L115–117**: add source or explicit "model
   projection, not measurement" label on the 90%/50–70%/60%
   resolution-rate estimates.
2. **[P0] THEWALL.md L198**: add Phase 4 imports banner clarifying
   that the subsections below are mechanistic extrapolations from
   dysbiosis framework to POD, not POD-specific clinical evidence.
3. **[P1] PROBLEM.md L80**: promote azelaic acid to explicit Tier 2
   inclusion or remove from THEWALL.md capsaicin-desensitization
   timeline (Y118 consistency).
4. **[P1] THEWALL.md Y113–Y115, Y117**: thread specific Buhl 2017
   citation, Sigurgeirsson 2015 pimecrolimus safety, Perrenoud 1994
   vitamin E sensitization.

## Non-audit observations

- POD/ is a **clean case study** for the sigma method's v7 Phase 0
  behavioral-wall classification. The directory's documents correctly
  identify that the mechanism is solved, the drugs exist, and the
  wall is caregiver compliance with a counter-intuitive rebound
  flare.
- **Cross-subdir integration works correctly here**: THEWALL.md's
  dysbiosis Phase 4 imports are each marked with source run_NNN and
  date stamp, rather than being silently merged. This preserves the
  map feature structure — a reader can see what came from dysbiosis/
  and when.
- Written caregiver instructions at THEWALL.md L125–159 are a
  **deliverable artifact** rarely seen in research synthesis
  directories. This should be considered for other medical subdirs
  where a patient/caregiver-facing intervention exists (e.g., T1DM's
  PATIENT_ZERO_TIMELINE has similar intent — compare and cross-
  reference).

## Tag

007. First audit pass on medical/perioral_dermatitis/. 2 🔴 (THEWALL
resolution-rate estimates need source or projection-label; Phase 4
dysbiosis imports need banner identifying as extrapolation, not POD-
specific clinical evidence — 7 compound/dose pairings without POD
clinical trials). 7 🟡 (Buhl 2017 LL-37/TRPV1, Sigurgeirsson 2015
pimecrolimus, Perrenoud 1994 vitamin E, azelaic acid internal
consistency). 8 🟢 (underreported diagnostic features; differential
table; gap.md clear-zone-unsolved honesty; Wall-Type-A vs Wall-Type-B
distinction; week-by-week trajectory; verbatim caregiver instructions;
iatrogenic-rebound cross-disease pattern; verified cross-reference to
7 dysbiosis/numerics/ files). **POD/ is a clean Phase-0-behavioral-
wall exemplar**; cross-subdir integration with dysbiosis/ works
correctly with dated stamps on imports. Next fire: other medical
subdir (me_cfs, acne, myocarditis) OR cross-propagate WHM fix
(R22/R24) across t1dm+dysbiosis+POD.
