# Attempt 009 — Claim-Backing Audit: blepharitis/ + persistent_organisms/ top-level

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: medical/blepharitis/PROBLEM.md (109 lines), gap.md (139
lines); medical/persistent_organisms/PROBLEM.md (165 lines).
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: audit log fires 1–14.

## Executive verdict

Both subdirs are **new (2026-04-15) and already well-structured**.

**blepharitis/** is **the clearest Phase-0-behavioral-wall
classification in the audit so far** — mechanism is done, treatments
work, wall is adoption (ophthalmology doesn't screen for Demodex)
plus patient adherence (6-12 weeks of nightly lid scrubs). gap.md is
organized by Type A (under-deployed, not unknown) / Type B (genuinely
uncertain) / Type C (method gaps) / Type D (adjacent problems) —
better taxonomy than the Mountain framework for a mostly-solved
disease.

**persistent_organisms/** is the **cross-organism synthesis layer**
pulling ~8 persistent organisms into a common two-phase therapeutic
architecture. It's paired with biology/evolution/ (evolutionary side)
with clear scope separation. Table maps each organism to persistence
niche / key diseases / clearance agent / adjunct.

**🔴 RED count**: 1
**🟡 YELLOW count**: 8
**🟢 GREEN count**: 10

## RED findings

### R28 — persistent_organisms/PROBLEM.md L41 (COR388 for Alzheimer's)

**The claim**:
> "*Porphyromonas gingivalis* … Alzheimer's association … Clearance
> agent(s): Professional periodontal therapy, anti-gingipain (COR388
> trialed)"

**Why load-bearing**: COR388 is cited as a clearance-phase option for
P. gingivalis-driven Alzheimer's. If COR388 failed in trial, citing it
as a current option misleads the therapeutic architecture table.

**Concern**: COR388 (atuzaginstat) from Cortexyme/Quince failed the
GAIN trial (Phase 2/3, ~600 patients). Hearing-toxicity signals, no
cognitive benefit on primary endpoint. The development program was
discontinued. Citing it as an active clearance agent in the table,
even with "trialed", understates that it FAILED.

**Required fix**: update to "COR388 (atuzaginstat) failed GAIN Phase
2/3 in 2022 — no cognitive benefit at primary endpoint, hearing-
toxicity concerns; program discontinued. The anti-gingipain concept
remains, but no approved drug exists." Include a citation to the
GAIN trial publication.

## YELLOW findings

| # | File / line | Claim | Source gap |
|---|-------------|-------|------------|
| Y132 | bleph PROBLEM L27 | "Demodex prevalence in chronic blepharitis 70-100%" with 3 refs (Gao 2005, Kheirkhah 2007, Zhao 2012) | Author-year cited without PMID; thread |
| Y133 | bleph PROBLEM L28 | "Post 1963" for age distribution (0 in children → 90% by age 70) | Classical ref, may need updated replication; thread citation |
| Y134 | bleph PROBLEM L35 | "Liang 2018, Kabataş 2017" D. brevis in chalazion | PMIDs; thread |
| Y135 | bleph PROBLEM L40 | "Liang 2014 69% pediatric chalazion Demodex+" | PMID; thread — this is a load-bearing statistic for pediatric framing |
| Y136 | bleph gap.md L37–42 | "Xdemvy phase 3 (Saturn-1/2) cleared collarettes in ~56% of treated eyes at day 43" | Lotilaner/Xdemvy Saturn-1/2 trials (Yeu, Nijm et al.); thread specific trial refs |
| Y137 | pers_org L41 | "Porphyromonas gingivalis … Alzheimer's association" | Dominy et al. 2019 *Sci Adv* is primary ref; thread |
| Y138 | pers_org L42 | "EBV (Bjornevik 2022 causal)" | Already-flagged Y108 in dysbiosis audit; thread PMID 35025605 consistently |
| Y139 | pers_org L45 | "Triple/quadruple antibiotic therapy, bismuth regimens" for H. pylori | ACG 2017 guideline or Maastricht V/VI; thread |

## GREEN findings

- **G87** bleph PROBLEM.md L44–66 — **single-loop diagram** showing
  Demodex density → mechanical+TLR4+Dectin-1 triggers → lid-margin
  inflammation + MGD + chalazion → barrier defect → density ↑ (self-
  reinforcing). Matches sigma-method "stuck system with positive
  feedback" framing.
- **G88** bleph PROBLEM.md L69–84 — **Phase 0 shape-check with
  explicit classification** "BEHAVIORAL WALL with MECHANISTIC
  COMPLETENESS. This is the canonical v7 Phase 0 behavioral-wall
  case. The science is done; the obstruction is clinical recognition
  + patient adherence." Per sigma v7, this is exactly the right
  classification. Method's output should be recognition artifacts
  and adherence scaffolding, not more mechanism runs.
- **G89** bleph gap.md — **Type A/B/C/D taxonomy** (under-deployed /
  genuinely uncertain / method-specific / adjacent problems) is a
  better gap-organizer than mountains-framework for a mostly-solved
  disease. Type A gaps are ADOPTION gaps; Type B gaps are MECHANISTIC
  gaps; Type C gaps are METHOD-LEVEL (no papers file, no numerics, no
  certs); Type D gaps are ADJACENT problems (ocular rosacea, DED,
  seb blepharitis).
- **G90** bleph gap.md L122–132 — **Priority ranking for "if forced
  to pick two items to close next"** with explicit rationale: C2
  numerics (meibography dropout vs treatment-start) because
  reversibility determines urgency; C3 cert (pediatric chalazion
  Demodex attribution) because it's the highest-leverage under-
  recognized finding. Matches sigma's kill-ROI ordering principle.
- **G91** bleph PROBLEM.md L13–18 — **existing-repo-content cross-
  reference table** (dysbiosis run_046 + POD attempt_005) showing
  what the new directory fills between. Avoids duplicating prior
  work.
- **G92** pers_org PROBLEM.md L36–49 — **8-organism table with
  niche, diseases, clearance agent, adjunct columns** — cleanly
  organized synthesis artifact. Matches sigma method's "what's
  proven vs what remains" with specific agents per organism.
- **G93** pers_org PROBLEM.md L74–95 — **three reasons this directory
  deserves its own home**: (1) cross-organism synergy (lid margin
  hosts 5 of 8 organisms), (2) shared two-phase architecture, (3)
  differential-diagnosis route. Each reason is a concrete synthesis
  claim, not a generic "it's important."
- **G94** pers_org PROBLEM.md L111–125 — **relationship-to-existing-
  per-disease-directories table** showing which diseases are
  organism → disease instances of the cross-organism framework. This
  prevents double-coverage and makes the umbrella structure visible.
- **G95** pers_org PROBLEM.md L127–135 — **explicit boundary with
  biology/evolution/**: biology asks "why did these organisms evolve
  to persist?" while medical asks "what do we do about it?" Both
  sides reference each other without collapsing — matches sigma v3
  working-dir discipline (single workspace, multiple roots).
- **G96** pers_org PROBLEM.md L137–154 — **Work plan with 4 numbered
  attempts** — specific synthesis targets with clear titles.
  attempt_003 "the coinfection problem" is particularly sharp —
  "most real patients have 2+ persistent organisms; how to sequence
  or combine treatment."

## Recommended fixes (ordered)

1. **[P0]** pers_org PROBLEM.md L41: correct the COR388 citation to
   reflect GAIN trial failure (R28).
2. **[P1]** bleph PROBLEM.md + gap.md: thread PMIDs for Gao 2005,
   Kheirkhah 2007, Zhao 2012, Liang 2014/2018, Kabataş 2017, Koo
   2012, van Zuuren 2019, Lacey 2007 — 8 refs for one consolidated
   citation pass.
3. **[P1]** bleph gap.md L37: thread Saturn-1/2 lotilaner trial
   citation (Yeu et al. / Nijm et al.).
4. **[P2]** pers_org PROBLEM.md L42: thread PMID 35025605 (Bjornevik
   2022) consistently with dysbiosis audit Y108.
5. **[P2]** pers_org PROBLEM.md L45: thread Maastricht guideline for
   H. pylori triple/quadruple therapy.

## Non-audit observations (map features)

- **blepharitis/ + persistent_organisms/ were created 2026-04-15 and
  already follow the dysbiosis template** (Phase 0 shape-check,
  cross-references, structured gaps, work plans). This is evidence
  that the template is being consistently applied to new subdirs —
  a structural improvement across the non-math corpus.
- **The pairing of medical/persistent_organisms/ + biology/evolution/
  is a clean separation-of-concerns**: clinical consequence +
  treatment (medical) vs evolutionary origin (biology). Other
  meta-frameworks that might span both should consider this pattern.
- **blepharitis/ gap.md's Type A/B/C/D taxonomy** is more expressive
  than the Mountain framework for diseases where the mechanism is
  mostly solved. Consider recommending this taxonomy for other
  behavioral-wall-classified subdirs when they appear.
- **persistent_organisms/'s work plan attempt_003 ("the coinfection
  problem")** is an under-addressed sub-question in the larger
  medical literature. Real patients have 2+ persistent organisms;
  treatment-sequencing logic (e.g., clear P. gingivalis before EBV
  reactivation suppression; or treat Demodex before rosacea
  maintenance) is a legitimate research question.

## Tag

009 (blepharitis). First audit pass on medical/blepharitis/ +
medical/persistent_organisms/. 1 🔴 (COR388 atuzaginstat cited as
P. gingivalis clearance option but GAIN trial failed 2022 —
discontinued; needs update). 8 🟡 (PMID threading for 8 Demodex +
rosacea + synthesis citations; Maastricht for H. pylori guidelines).
**10 🟢**: bleph single-loop diagram; Phase 0 behavioral-wall
classification (canonical v7 case); Type A/B/C/D taxonomy better
than Mountain framework for mostly-solved disease; priority
ranking with kill-ROI rationale; existing-content cross-reference
table; pers_org 8-organism synthesis table; 3-reason argument for
cross-organism framework; per-disease-existing-work mapping;
explicit medical/biology boundary; 4-attempt work plan with
coinfection-problem synthesis target. **Observation**: new subdirs
(created 2026-04-15) already follow the dysbiosis template — the
template is propagating. Next fire: eczema, psoriasis, dilated_cm,
pericarditis, infertility, OR start physics/philosophy (tier-0
subdirs).
