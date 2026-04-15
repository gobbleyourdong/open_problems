# Attempt 096 — Claim-Backing Audit: attempts 011–020

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: medical/t1dm/attempts/attempt_011 … attempt_020
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: attempt_095_audit_001_to_010.md

## Executive verdict

This decade of attempts shifts from individual-therapy summaries (001–010)
to **multi-mountain synthesis** (regeneration, environmental triggers,
combination protocols). Synthesis work is harder to audit because many
claims are recombinations of sub-claims, each of which needs a source.
The attempts hold up well on the "right mountains identified" level but
accumulate unsourced epidemiological and clinical claims.

**🔴 RED count**: 3
**🟡 YELLOW count**: 18
**🟢 GREEN count**: 5

Two structural concerns worth flagging before the per-item list:

**S1 — prescriptive creep (attempt_013, attempt_018)**: both attempts
present protocols with doses, durations, and titration schedules
(5000-10000 IU/day vitamin D, 1.5M IU/day IL-2, semaglutide 0.25→1mg/wk,
5-day FMD insulin-reduced 50-70%). These are clinical-protocol-grade
specifications in an attempt-doc format. Attempt_013 has an explicit "NOT
medical advice" disclaimer (L49). Attempt_018 does not and concludes
"could be started TOMORROW for a willing patient" (L115). This is not a
claim-backing problem per se; it is a **framing problem**: research
attempts should end at "target X, dose range Y cited-from-paper-Z" not
at "monthly 5-day FMD at 1100→750 kcal with insulin reduced 50-70%." The
RESEARCHER_CONTEXT register permits specificity but the attempts read
more as protocols-for-a-patient than as hypothesis-for-a-trial.

**S2 — sub-claim propagation without re-sourcing**: attempt_020 sources
harmine's 3-8% proliferation to Wang *Nature Medicine* 2015 + Wang *Cell
Metabolism* 2019 (good). But attempt_012 L103 and attempt_015 L39 reuse
the same number without citing the underlying papers. When a figure is
cited once in the corpus, downstream attempts should thread the citation
rather than drop it silently. The math/ equivalent: attempt 849 threads
`CrossModeBound.lean` and `SelfAnnihilation.lean` by name into the
argument, not as vague "we proved this elsewhere."

## RED findings

### R3 — attempt_014 L12 (Extended Honeymoon numerics)
> "~60% of newly diagnosed T1DM enter partial remission.
> Average duration 9 months, range 1 month to 13 years"

**Why load-bearing**: the attempt uses this as one of five "anti-problem"
examples that prove spontaneous resolution exists. The specific numbers
60%/9-mo/13-yr define the envelope of the phenomenon.

**Concern**: these numbers are order-of-magnitude plausible but the
canonical honeymoon literature (Mortensen et al., Hvidøre studies;
Greenbaum et al., TrialNet) reports partial-remission rates of 30–60%
depending on definition (A1c-dose-adjusted vs IDAA1c ≤ 9) with median
duration ~7 months and upper-range ~2 yr (some older case reports have
longer). The "13 years" upper bound is unusually long and may conflate
partial-remission with LADA slow-progression.

**Required fix**: cite a specific source (Mortensen HB et al., Pediatr
Diabetes 2009, or equivalent) with the definition used, OR mark the
range as "anecdotal / case-series," OR replace 13 yr with the
canonical ~2 yr upper bound.

### R4 — attempt_016 L19 (CVB meta-analysis numeric)
> "Meta-analysis of 38 case-control studies: significant association
> between enterovirus infection and T1DM"

**Why load-bearing**: the enterovirus-T1DM link is one of the strongest
claims in Mountain 3. "38 case-control studies" is specific and
verifiable.

**Concern**: Yeung WCG et al., *BMJ* 2011 (PMID: 21292721) is likely the
intended reference (systematic review of ~24–26 studies depending on
inclusion). Craig et al., *Diabetologia* 2019 updated the analysis with
larger numbers. If "38" comes from neither of these, it needs a source.

**Required fix**: thread a specific citation with the exact study count.
If Yeung 2011 is intended, the number should be 24 or 26, not 38.

### R5 — attempt_020 L15 (harmine proliferation rate)
> "Harmine ... induces human beta cell proliferation at rates of
> 3-8% per day in vitro. This is 1000x the normal adult rate."

**Why load-bearing**: the 3-8%/day claim is repeated across attempts
012, 015, 018, 020 and is the entire mechanistic case for the rate-
accelerator arm of the protocol.

**Concern**: Wang et al. *Nature Medicine* 2015 (PMID: 25751815)
reported labelling indices typically in the 0.5–2% range for harmine
alone (dose and timepoint dependent). The 5-8% upper bound cited in
attempt_020 L27 for harmine + GLP-1 (exendin-4) is closer to what the
Wang papers report; the **harmine-alone** 3-8%/day figure is an
overstatement. The dose/time/assay conditions matter enormously.

**Required fix**: split "harmine alone" vs "harmine + GLP-1" vs
"harmine + GLP-1 + TGF-β inhibitor" with specific labelling indices and
assay conditions, all sourced to the Wang 2015/2019 papers.

## YELLOW findings (compressed)

| # | Attempt / line | Claim | Source gap |
|---|----------------|-------|------------|
| Y12 | 011 L9 | "Cheng et al., Cell, 2017" for Longo FMD in T1DM/T2DM mice | Full ref ok but no PMID; mouse model type (STZ vs NOD) and n not stated |
| Y13 | 011 L43 | "~$300 per cycle (ProLon)" | Retail list price no source |
| Y14 | 011 L54 | "Longo's 2014 Cell Stem Cell paper" on HSC regeneration | PMID 24905167 (Cheng et al.) should be threaded |
| Y15 | 012 L64 | "Stanford's 'immune reset' in attempt 008's references" | attempt_008 doesn't actually reference Stanford; cross-ref is stale |
| Y16 | 013 L6 | "Sci Transl Med, 2017, 100 participants" for FMD | Wei et al. *Sci Transl Med* 2017 PMID 28202779; should be threaded |
| Y17 | 013 L11 | "DiRECT trial (Lancet, 2018): 46% T2DM remission at 1yr, ~30% at 5yr" | Lean et al. Lancet 2018 PMID 29221645; 5-yr data is from Lean et al. Lancet Diabetes Endocrinol 2019, different ref |
| Y18 | 013 L18 | "Guo et al., Nature Metabolism, 2020" on keto atrophy | PMID should be threaded; exact claim "chronic keto causes beta cell atrophy" is stronger than Guo et al.'s findings |
| Y19 | 014 L18–19 | "~50% single-autoantibody non-progression, ~25% at 10yr with 2+" | TrialNet / TEDDY; Ziegler et al. JAMA 2013 is the canonical source but numbers differ |
| Y20 | 014 L23 | Identical twin concordance "~50%" | Multiple sources (Kaprio, Hyttinen) disagree; actual concordance is 30–50% depending on cohort and follow-up |
| Y21 | 014 L36 | "LADA patients … CD68+ macrophages + IL-1β (less cytotoxic than CD8+ + TNF-α in classic T1DM)" | Pugliese / In't Veld insulitis work; needs citation |
| Y22 | 016 L23 | "PRV-101, Provention Bio Phase 2" | NCT / trial ID; note Provention Bio was acquired by Sanofi 2023, vaccine program may have renamed |
| Y23 | 016 L73–78 | Vitamin D latitude gradient, "Finland highest … equatorial lowest" | EURODIAB / DIAMOND data; needs ref |
| Y24 | 016 L82 | "TRIGR trial result: NO significant effect on T1DM" | Knip et al. JAMA 2018 PMID 29297081; should be threaded |
| Y25 | 017 L46 | "Zonulin elevated in T1DM and pre-T1DM" | Sapone et al. Diabetes 2006 PMID 16644703; also note zonulin assay validity has been questioned (Fasano revision 2020) |
| Y26 | 017 L45 | "Butyrate depleted in pre-T1DM children" | de Goffau et al. / Kostic et al. TEDDY microbiome work; needs citation |
| Y27 | 018 L33 | "Vitamin D load to 50-70 ng/mL typically 5000-10000 IU/day" | No guideline source; Endocrine Society guidelines recommend lower targets |
| Y28 | 018 L47 | "Low-dose IL-2 (aldesleukin, 1.5M IU/day × 5 days/mo)" | DIABIL-2 trial dose range should be cited |
| Y29 | 019 L33 | "Preclinical proof-of-concept … HLA-G islets survive longer in mouse" | Specific papers needed (Carosella lab work) |
| Y30 | 019 L35 | "HLA-G expressed by some cancers to evade immunity" | Well-established but needs one ref (Rouas-Freiss or similar) |

## GREEN findings (positives)

- **G5** attempt_011 — FMD mechanism (mTOR↓ / AMPK↑ / autophagy↑ / Ngn3+
  reactivation) is internally consistent and maps cleanly to Cheng 2017
  Cell. Good structure: cited paper, named mechanism, testable prediction
  (Ngn3+ in adult pancreas).
- **G6** attempt_011 L60 — correctly flags the STZ-vs-NOD mouse model
  gap (STZ = chemical destruction, not autoimmune; the relevant human
  disease is autoimmune). This is rare honesty in translational claims.
- **G7** attempt_012 — mTOR/AMPK/Ngn3/IGF-1 pathway prose is textbook
  correct. Ricci-flow analogy in the Mountain 2 framing is a useful
  heuristic (sigma method explicitly allows analogies as map features).
- **G8** attempt_014 — the **anti-problem framing itself** is the
  important move: listing five classes of spontaneous-resolution cases
  (extended honeymoon, non-progressors, discordant twins, Deng patient,
  LADA slow-progressors) creates a testable hypothesis (protective
  phenotype is identifiable). Matches sigma method Phase 4.
- **G9** attempt_020 — DYRK1A mechanism via NFAT nuclear translocation
  → cell-cycle gene activation is well-sourced (Wang papers); the Down-
  syndrome chr21 trisomy cross-check is a genuine mechanistic validation.

## Recommended fixes (ordered)

1. **[P0] attempt_020**: split harmine rate claim into
   "harmine-alone / harmine+GLP-1 / harmine+GLP-1+TGF-β" with per-
   condition labelling indices; cite Wang 2015 / 2019 PMIDs.
2. **[P0] attempt_014**: resolve the honeymoon 60%/9-mo/13-yr numbers
   against Mortensen 2009 or equivalent; flag the 13-yr upper bound as
   anecdotal if not supported.
3. **[P0] attempt_016**: replace "38 case-control studies" with the
   actual count from the specific meta-analysis (Yeung 2011 BMJ: ~24;
   Craig 2019 *Diabetologia*: updated larger).
4. **[P1] Cross-attempt threading**: every reuse of the
   FMD (Cheng 2017), HSC reset (Cheng 2014), DIABGAM (Ludvigsson 2008
   NEJM), DiRECT (Lean 2018 Lancet), TRIGR (Knip 2018 JAMA), and Sana
   UP421 (NEJM 2025) citations should keep the citation tag — one sweep
   pass.
5. **[P1] attempt_018**: add a header disclaimer paralleling attempt_013
   L49, OR reframe as "Trial design proposal" rather than "patient
   protocol" with specific doses.
6. **[P2] attempt_015, 018**: cost figures ($10K, $100-200K, $500K
   etc.) should cite or be softened to ranges. Current numbers read as
   specific but come from back-of-envelope estimates.

## Non-audit observations (map features to preserve)

- The Mountain 1/2/3 structure is a genuine multi-mountain attack in the
  sigma sense — three independent angles (replace / regenerate / prevent)
  with a shared endpoint (functional beta cells in a tolerant immune
  environment). The underground connection — GLP-1 is both a beta cell
  growth factor (M2) and a gut hormone (M3) and a drug used clinically
  (M1 adjunct) — is a real standing-wave finding, not a constructed
  pattern.
- Attempt 018 is better understood as a **research synthesis / trial
  design proposal** than an audit target for "claim backing" — many of
  its specific doses are starting-point proposals, not established
  facts. The audit's R-items should not be read as "018 is wrong"; they
  are "018 should label which doses are evidence-based vs proposal."

## Tag

096. Second claim-backing audit pass on t1dm/. Attempts 011–020 shift
from per-therapy summaries to multi-mountain synthesis; more unsourced
epi and clinical numbers (18 🟡), 3 🔴 (honeymoon epi, CVB meta-analysis
count, harmine rate overstatement), 5 🟢 positives. Structural concern:
prescriptive creep in attempt_018. Next fire: t1dm attempts 021–030.
