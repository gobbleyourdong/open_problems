# Attempt 116 — Claim-Backing Audit: biology/evolution per-organism attempts 002, 003, 009

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue, Fire 44)
**Scope**: biology/evolution/attempts/attempt_002_cvb_evolution.md (297L,
full) + attempt_003_ebv_evolution.md (360L, sampled L1-80 + 280-360) +
attempt_009_demodex_evolution.md (402L, sampled L1-80 + 300-402).
Representative sample across 9 per-organism attempts (~3200 lines
total). Attempts 004-008, 010 not sampled this fire.
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: Fire 34 sampled 100/107 (immune-timeline); prior
`claim_audit_2026-04-15.md` (WebSearch-based) did content audit on
biology/evolution with 65 claims verified, ~52% clean, 1 fabrication
caught (Liang 2018 pediatric chalazion recurrence).

## Executive verdict

The per-organism series is **structurally consistent and
intellectually disciplined** — each attempt follows same 9-section
schema (phylogeny → genome → persistence mechanism → host coevolution
→ selection → framework predictions → open questions → cross-links
→ key sources). Several attempts (009 Demodex notably) carry
explicit **VERIFICATION STATUS disclaimers** flagging AI-generated
structural claims vs data-verified claims — Maps-Include-Noise
compliance at the file level.

**The citation-discipline gradient is informative**:
- attempt_002 (CVB): NO PMIDs across ~10 key citations
  (Chapman 2008, Kim 2005, Smithee 2015, Krogvold 2015, Kühl 2003,
  Benkahla 2018, Zell 2017, Harvala 2018, Stone 2021, Hyoty 2002)
- attempt_003 (EBV): similarly NO PMIDs (Bjornevik 2022 Science,
  Lanz 2022 Nature, Thorley-Lawson, Cohen, Longnecker)
- attempt_009 (Demodex): DOES include PMIDs (Smith 2022 PMID 35724423,
  Palopoli 2014 PMID 25515815) + explicit VERIFICATION STATUS tag
  + a corrective note (L72-74) that a commonly-confused secondary-
  source conflation has been caught

This is load-bearing: CVB citations propagate into medical/t1dm,
medical/myocarditis, medical/pericarditis, medical/me_cfs, and
medical/persistent_organisms. If Chapman 2008 or Krogvold 2015 is
mis-cited, the downstream errors compound.

**🔴 RED count**: 0 (within sampled content)
**🟡 YELLOW count**: 8
**🟢 GREEN count**: 11

## YELLOW findings

| # | Location | Claim | Source gap |
|---|----------|-------|------------|
| Y253 | 002 L97-99 | Chapman NM et al. 2008 Virology 375:480-491 "5' terminal deletions in the genome of a coxsackievirus B2 strain occurred naturally in human heart" | Verify PMID (Chapman 2008 Virology is real; PMID ~18353417 range) |
| Y254 | 002 L101-105 | Kim KS et al. 2005 J Virol 79:7024-7041 "5'-Terminal deletions occur in coxsackievirus B3 during replication in murine hearts" | Verify PMID (Kim 2005 J Virol is real; PMID ~15890943 range) |
| Y255 | 002 L107-109 | Smithee S et al. 2015 J Virol 89:11761-11772 "Mutational disruption of cis-acting replication element 2C" | Verify PMID (Smithee 2015 J Virol is real; PMID ~26378170 range) |
| Y256 | 002 L87-89 | Krogvold 2015 Diabetes DiViD study, enteroviral protein in islets 6/6 T1DM patients | Thread PMID (Krogvold 2015 DiViD is real; often cited as PMID 25576057 or similar — verify sub-cohort numbers) |
| Y257 | 002 L89-90 | Kühl 2003 Circulation enteroviral RNA in DCM hearts + IFN-β therapy LVEF improvement | Likely Kühl 2005 Circulation rather than 2003 (Kühl's pivotal IFN-β RNA-positive DCM paper is 2003 or 2005 depending on study); thread PMID |
| Y258 | 003 L348 | Bjornevik 2022 Science MS causation paper | PMID 35025605 (known); thread explicitly |
| Y259 | 003 L349 | Lanz 2022 Nature molecular mimicry EBNA-1 vs GlialCAM | PMID ~35075051 range; thread |
| Y260 | 009 L68-71 | Smith 2022 MBE Demodex nuclear genome PMID 35724423 "Human Follicular Mites: Ectoparasites Becoming Symbionts" ~51.5 Mb 9707 proteins | Verify PMID 35724423 maps to Smith 2022 Demodex folliculorum; "9,707 proteins" specific — verify against paper |

## GREEN findings

- **G324** **9-section schema consistent across attempts**: phylogenetic
  placement → genome architecture → persistence mechanism → host
  coevolution → current selection pressures → framework predictions
  (attempt_001's 6) → open questions → cross-links → key sources.
  Structural discipline across ~3200 lines.
- **G325** attempt_009 **explicit VERIFICATION STATUS disclaimer**
  (L13-16): "generated from trained priors with structural claims
  high-confidence; specific genome-size figures, population-level
  density data (e.g. Forton), and ancient-DNA recovery details
  flagged for further audit." File-level Maps-Include-Noise honest-
  labeling of AI-provenance.
- **G326** attempt_009 L72-74 **inline correction of secondary-source
  confusion**: "[Palopoli et al. 2014 BMC Genomics PMID 25515815
  sequenced the mitochondrial genome only (14,150 bp), not the
  nuclear — commonly confused in secondary sources.]" This is
  exactly the kind of content-audit outcome worth threading inline.
- **G327** attempt_002 **per-virus persistence-mechanism classification**:
  "mutation-based persistence" (class 2) vs EBV "encoded latency"
  (class 1) vs HPV "lifecycle-coupling" (class 3) vs HHV-6
  "integration" (class 5) — each attempt places its organism in
  a distinct mechanism class. 7 classes across 8 organisms (009
  L377-386 table).
- **G328** attempt_002 L212-234 **6 framework predictions
  per-attempt applied-and-graded**: ✓ / partial / consistent /
  provisional per prediction — not just cargo-cult checklist but
  honest per-organism evaluation. Where predictions hold weakly
  (CVB prediction 1 "partial" because persistence is atypical for
  its transmission mode) the author says so.
- **G329** attempt_003 **EBV coevolution quantification**: ~40 Ma
  hominin-chimp EBV divergence ≈ hominid-hominin split; 180-220 Ma
  herpesvirus subfamily divergence; 400+ Ma herpes-vertebrate
  coexistence. Specific time estimates with rationale.
- **G330** attempt_003 L303 **large-genome prediction holds strongly
  for EBV** — 172 kb, explicitly attributed to latency-machinery
  coding cost per attempt_001 prediction 2. Framework-to-organism
  mapping explicit.
- **G331** attempt_009 L305-314 **framework extension mid-audit**:
  "the 'large genome' prediction of attempt_001 needs reformulation.
  It holds for viral + bacterial persistence but NOT for eukaryotic
  obligate-parasite persistence, where genome REDUCTION (not
  expansion) is the signature. A better formulation: **genome
  specialization** (either direction)." Framework-evolution-through-
  data, sigma-method-correct.
- **G332** attempt_003 L314-316 **honest edge-case flagging**:
  "Bjornevik 2022 found only 1 of 801 MS cases was EBV-seronegative
  at diagnosis — is that 1 a genuine exception or serology false-
  negative?" Doesn't overclaim 100% necessity.
- **G333** attempt_002 L270-275 **repo cross-links explicit**:
  `medical/t1dm/`, `myocarditis/`, `pericarditis/`,
  `dilated_cardiomyopathy/`, `pancreatitis/`, `pleurodynia/`,
  `neonatal_sepsis/`, `me_cfs/`, `dysbiosis/`, `persistent_organisms/`.
  Biology-to-medical mapping threaded per-organism.
- **G334** attempt_009 **structural comparison table** (L377-386)
  across 8 organisms with columns (persistence class / genome /
  host / unique feature). Cumulative-framework-state visualization
  at each new organism addition.
- **G335** The **citation-discipline gradient** (002/003 → 009)
  reflects chronological improvement — early per-organism attempts
  written without PMID discipline; later attempts add PMIDs +
  VERIFICATION STATUS tags. This matches the medical/t1dm quality
  step-change around attempt_036 (Fire 10 observation).

## Recommended fixes (ordered)

1. **[P1]** Thread PMIDs for attempt_002 key citations (Y253-Y257)
   — CVB claims propagate across 6+ medical/ subdirs; unverified
   PMIDs here compound downstream. Priority: Chapman 2008, Kim
   2005, Krogvold 2015, Kühl 2003/2005 (correct year verification).
2. **[P2]** Thread PMIDs for attempt_003 Bjornevik 2022
   (PMID 35025605) + Lanz 2022 (Y258, Y259).
3. **[P2]** Verify attempt_009 Smith 2022 Demodex genome PMID 35724423
   maps correctly (Y260) — already threaded, just confirm.
4. **[P3]** Consider adding VERIFICATION STATUS disclaimers to
   early attempts (002, 003) matching the later-attempt pattern
   (009) — file-level honest labeling of AI-provenance.

## Non-audit observations

- **The prior WebSearch-based audit** (`claim_audit_2026-04-15.md`
  per session summary) already found ~52% clean / 1 fabrication
  rate on biology/evolution. Today's structural audit complements
  that by identifying citation-discipline gradient (002/003 missing
  PMIDs vs 009 with PMIDs) and the VERIFICATION STATUS tag pattern.
- **CVB citations are load-bearing across the medical corpus** —
  Chapman 2008, Kim 2005, Krogvold 2015, Kühl 2003/2005 appear
  in medical/t1dm, medical/myocarditis, medical/persistent_organisms,
  medical/dysbiosis cross-references. A single wrong PMID here
  propagates into 10+ files.
- **attempt_009's mid-attempt framework reformulation** (L305-314:
  "large genome" → "genome specialization") is an instance of
  sigma v5 self-applicability: the framework (attempt_001) gets
  updated during per-organism application (attempt_009) when data
  don't fit. This is the method working correctly.
- **The "7 classes across 8 organisms" observation** (009 L386-396)
  is a strong cumulative-framework claim: persistent human
  organisms span RNA viruses (1 class) + DNA viruses (3 classes:
  encoded latency / lifecycle coupling / integration) + bacteria
  (1 class: chronic+tolerance) + eukaryotes (1 class: obligate
  ectoparasite). The framework covers the biological diversity.
- **Potential addition**: Malassezia + C. acnes (attempt_010) adds
  fungal + commensal-bacterial classes. Expected to bring the
  class count to 8 or 9 total.

## Tag

116 (biology/evolution per-organism). Sampled 3/9 attempts (002 CVB
full, 003 EBV L1-80+280-360, 009 Demodex L1-80+300-402). **0 🔴**
(within sampled content; prior WebSearch audit found 1 fabrication
in broader sweep). 8 🟡 (Chapman 2008/Kim 2005/Smithee 2015/Krogvold
2015/Kühl 2003 PMIDs for CVB claims that propagate across 6+ medical
subdirs; Bjornevik 2022/Lanz 2022 PMIDs for EBV; Smith 2022 Demodex
PMID verify). **11 🟢**: 9-section schema consistent across 3200
lines; attempt_009 explicit VERIFICATION STATUS disclaimer
(file-level Maps-Include-Noise); attempt_009 inline correction of
Palopoli 2014 nuclear-vs-mitochondrial genome confusion; per-virus
persistence-mechanism classification (7 classes across 8 organisms);
6 framework predictions applied-and-graded per organism; EBV
coevolution quantification (40 Ma hominin, 180-220 Ma subfamily,
400+ Ma vertebrate); large-genome prediction holding strongly for
EBV; attempt_009 **framework-reformulation mid-audit** (large-genome
→ genome-specialization) — sigma v5 self-applicability working;
attempt_003 honest edge-case flag for Bjornevik 1/801 seronegative
case; biology-to-medical cross-links explicit per-organism; cumulative
structural-comparison table at each organism addition.
**Citation-discipline gradient** (002/003 no PMIDs → 009 with PMIDs
+ VERIFICATION STATUS) reflects chronological improvement matching
t1dm attempt_036 step-change. **Observation**: CVB citations
(Chapman/Kim/Krogvold/Kühl) are load-bearing across medical corpus;
PMID-threading here compounds cleanup value. Remaining: attempts
004 HPV, 005 HCMV, 006 HHV-6, 007 H.pylori, 008 P.gingivalis, 010
Malassezia+C.acnes not sampled this fire (~2000 lines). Next fire:
remaining per-organism attempts, dysbiosis numerics, WHM sweep
(pending), or loop termination.
