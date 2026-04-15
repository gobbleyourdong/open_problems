# Attempt 008 — Claim-Backing Audit: me_cfs/THEWALL.md (1719 lines)

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: medical/me_cfs/THEWALL.md (1719 lines, deferred since Fire
13). Sampled L1-100 (synthesis) + L91-150 (wall + Phase 4 update) +
L1660-1719 (tail cross-references run_165-170).
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: audit log fires 1-35 (t1dm/THEWALL.md audit in fire 35
identified the same dual-structure pattern).

## Executive verdict

**me_cfs/THEWALL.md has the same dual structure as t1dm/THEWALL.md**:

1. **Lines 1–~115**: synthesis document (One Sentence + Disease in
   One Diagram + What ME/CFS Is Not + Three Nested Walls + First
   Validated Biomarker + Protocol + The Numbers + The Wall)

2. **Lines 116–1719**: **~50+ cross-reference sections** importing
   the same run_NNN mechanism findings from dysbiosis/numerics/
   that appear in t1dm/THEWALL.md — but with ME/CFS-specific
   interpretation (same run numbers, different disease-
   application). Example: **run_166 T-bet/TBX21** appears in both
   t1dm (β-cell Th1-rate-limiting gate) and me_cfs (**"eighth NK
   functional gate"**).

**R35 (mechanism-counting inflation) from t1dm fire 35 applies here
too**: me_cfs THEWALL uses "eighth NK gate", "double-deficit" (IRF1 +
T-bet), and similar cumulative counting frames. Different disease-
applications of the same mechanism library use different counting
systems (t1dm counts β-cell death mechanisms; me_cfs counts NK
functional gates).

**🔴 RED count**: 1 (propagated R35 mechanism-counting to me_cfs)
**🟡 YELLOW count**: 5
**🟢 GREEN count**: 11

## RED findings

### R36 — Propagation of R35 (mechanism-counting inflation) to me_cfs

**The claim pattern**: me_cfs/THEWALL.md uses cumulative counts
analogous to t1dm:
- run_166 "NK T-bet = eighth NK functional gate"
- run_168 "NK IRF1 + T-bet double-deficit" (counting transcriptional
  co-requirements)
- run_167 "GATA3-atopic-comorbidity" (MCAS overlap)
- Earlier in the doc: "second PEM mechanism" (TRPV1 central
  sensitization, L136)

**Why load-bearing**: same as t1dm — if "eighth NK gate" counts
receptor-based exhaustion mechanisms, but "double-deficit" counts
transcriptional co-requirements, the count is mixing levels. The NK
exhaustion phenotype in ME/CFS is characterized by ~3–4 known
mechanistic categories; counting to "eighth" suggests more
discrimination than the literature supports.

**Required fix**: cross-reference the proposed **Mechanism-Counting
Methodology note** from t1dm R35. If adopted in one THEWALL, it
should be consistent across disease-specific THEWALL documents that
share the underlying dysbiosis/numerics/ mechanism library. Both
t1dm and me_cfs can reference the same methodology note.

## YELLOW findings

| # | Section / line | Claim | Source gap |
|---|----------------|-------|------------|
| Y228 | L93 "2.5 million Americans affected" | CDC estimate — should cite Institute of Medicine (IOM) 2015 report or Jason et al. 2020 cross-sectional estimates |
| Y229 | L98 "Fastest clinical signal: cfRNA panel + NK cytotoxicity at 6 months" | Timeline is reasonable for protein-turnover + cfRNA kinetics; thread citation to pattern_017 GSE293840 analysis that derived 6mo timeline |
| Y230 | L106 "42% of patients" CVB-ME/CFS subset | Chia & Chia 2008 J Clin Pathol (PMID 17872383) — thread consistently with Fire 13 Y120/Y121 finding |
| Y231 | L133 "NLRP3 +37% in ME/CFS PBMCs (documented)" | GSE293840 source — thread accession |
| Y232 | L141 "LDN (low-dose naltrexone) 1.5-4.5mg/day" for TRPV1 sensitization | Bolton & Younger 2018 or similar — specific dose range cited by multiple LDN-ME/CFS studies but primary source should be threaded |

## GREEN findings

- **G268** L4 **One-sentence thesis** (from Fire 13 audit, G73):
  "molecular signature is not fatigue, it is T cell exhaustion from
  chronic viral antigen exposure, mitochondrial dysfunction from
  Complex I damage, and NK cells armed with killing machinery they
  can't use."
- **G269** L28-34 **"What ME/CFS Is Not"** — explicitly rules out
  deconditioning, psychosomatic, simple fatigue, depression, each
  with molecular evidence. Pre-empts common misattributions.
- **G270** L35-56 **Three Nested Walls** (invisible target / mito
  damage / what-virus) each with specific protocol answer.
- **G271** L58-66 **MT-ND3 + PRF1 + STAT2 cfRNA biomarker panel** —
  criteria specified (blood draw not biopsy; maps to mechanism;
  responds to protocol).
- **G272** L69-89 **Protocol (ME/CFS Adapted)** with two critical
  differences from T1DM (no exercise during antiviral phase;
  mitochondrial arm first-priority) — structured inheritance with
  explicit diff. From Fire 13 G77.
- **G273** L91-98 **"The Numbers"** section: 2.5M Americans, 0 FDA-
  approved treatments, 0 validated biomarkers (until GSE293840), 40+
  years controversy, $170/month, 6-month fastest-signal timeline.
  Quantitative status summary.
- **G274** L100-112 **"The Wall" section** — 3 concrete actions
  (stool enteroviral PCR $200; mitochondrial-arm protocol start
  this week; 30-patient pilot with cfRNA endpoint). Closes with
  "The wall is stigma and nihilism. The science is not." — sigma
  Phase-0 behavioral-wall framing.
- **G275** L116-154 **Phase 4 Update with cross-pollination from
  dysbiosis campaign**: M1↔M8 HPA exhaustion mechanism for ME/CFS
  hypocortisolism + three non-responder loops (NLRP3/pyroptosis,
  HERV-W, HPA) + TRPV1 central sensitization as PEM mechanism +
  Protocol Additions table (colchicine, omega-3 4g, LDN).
- **G276** L147 **Safety note inline with protocol addition**:
  "Colchicine 0.5mg BID: **NEVER combine with itraconazole (fatal
  CYP3A4)**" — drug-interaction warning at the protocol-line level,
  not just in DRUG_SAFETY_MATRIX.md. Redundant safety messaging
  (Maps-Include-Noise at the warning level).
- **G277** Cross-reference sections (run_165-170 sampled) maintain
  consistent structure: **Relevance tag** (HIGH/MODERATE/
  **LOW-MODERATE**/**MODERATE (CAUTION)**), numbered mechanistic
  findings, dated cross-reference tag. Same discipline as t1dm/
  THEWALL.md.
- **G278** run_170 **Gal-1 ME/CFS contraindication** analogous to
  t1dm's harmine rosacea contraindication — "systemic Gal-1 therapy
  CAUTION in EBV-driven ME/CFS" because EBV-B cells upregulate
  LGALS1 for immune evasion (opposite valence to what Gal-1 therapy
  targets). **Another dual-disease-mechanism-derived clinical
  contraindication** emerged from the cross-pollination process.

## Recommended fixes (ordered)

1. **[P0]** R36: apply the Mechanism-Counting Methodology note
   (recommended in t1dm fire 35 R35) as a shared note across both
   t1dm/THEWALL.md and me_cfs/THEWALL.md (and any other disease-
   THEWALL docs with cumulative counting). Single source of truth
   rather than per-disease interpretation.
2. **[P1]** Thread 2.5M Americans source (IOM 2015), 42% CVB rate
   (Chia 2008 PMID 17872383) consistently across me_cfs docs and
   with t1dm cross-refs.
3. **[P2]** Thread Bolton & Younger 2018 LDN-ME/CFS or similar for
   the LDN dose range.

## Non-audit observations

- **Confirmation of dual-structure pattern across disease-THEWALL
  docs**: t1dm (2022 lines), me_cfs (1719 lines), and likely
  others (medical/pericarditis, medical/myocarditis, etc. if they
  have THEWALL.md) share the synthesis + cross-reference-catalog
  structure. The catalog imports the same dysbiosis/numerics/
  run_NNN findings interpreted per-disease.
- **The cross-pollination mechanism works** — mechanism discoveries
  in dysbiosis/numerics/ propagate to disease-specific THEWALL
  docs. Observed in both t1dm (harmine rosacea contraindication,
  BACH2 Vitamin A stratification, DPP4 sitagliptin preference) and
  me_cfs (Gal-1 EBV contraindication, LDN for TRPV1 sensitization,
  colchicine for NLRP3 loop 2) — actionable clinical rules
  emerging from the cross-disease synthesis.
- **The Gal-1 EBV contraindication in me_cfs is structurally
  identical to the harmine rosacea contraindication in t1dm** —
  both are dual-disease mechanistic analyses producing OPPOSITE
  valence for the same intervention depending on underlying
  disease. This is a genuine signal of the framework's clinical
  utility when applied properly.
- **The 3 disease-THEWALL docs + medical/THEWALL.md** (campaign-
  level) form a 4-tier wall hierarchy:
  1. Per-disease (t1dm, me_cfs, POD, dysbiosis, myocarditis,
     aseptic_meningitis, encephalitis, and other disease-THEWALLs)
  2. Campaign-level (medical/THEWALL.md: "the wall is a blood draw
     appointment")
  3. Framework-level (sigma method v7 Phase 0 behavioral-wall
     classification)
  4. Audit-level (K_FRAMEWORK_AUDIT, α_β_γ_FRAMEWORK_AUDIT, R33
     cross-disease Treg-NLRP3 audit recommended)

## Tag

008 (me_cfs/THEWALL.md). **Same dual-structure pattern as
t1dm/THEWALL.md**: ~115-line synthesis + ~1600-line cross-reference
catalog. **1 🔴 R36**: propagated R35 mechanism-counting inflation
to me_cfs's "eighth NK gate", "double-deficit" counting frames;
recommend shared Mechanism-Counting Methodology note across disease-
THEWALL docs. 5 🟡 (2.5M CDC/IOM source, 42% CVB Chia 2008 PMID,
GSE293840 accession for NLRP3 +37%, LDN Bolton/Younger 2018, fastest-
signal timeline threading). **11 🟢**: one-sentence molecular-
signature thesis; What-ME/CFS-Is-Not pre-emption; Three Nested Walls
framework; MT-ND3+PRF1+STAT2 cfRNA biomarker panel; protocol
inherited-from-T1DM-with-explicit-diffs (no exercise + mito first);
The Numbers quantitative summary (2.5M, 0 FDA-approved, 0
biomarkers-until-GSE293840, 40yr controversy, $170/mo); The-Wall-is-
stigma-and-nihilism Phase-0 behavioral-wall framing; **Phase 4
update with 3 non-responder loops + TRPV1 PEM mechanism**; inline
**colchicine+itraconazole fatal-interaction warning** (redundant
safety at protocol line, not just in DRUG_SAFETY_MATRIX);
cross-reference consistent-structure across ~50 imports; **Gal-1
EBV contraindication** from dual-disease mechanistic analysis
(structurally parallel to t1dm harmine-rosacea contraindication,
validates the cross-pollination mechanism). **Observation**: 4-tier
wall hierarchy emerging across the campaign (per-disease THEWALLs →
medical-campaign THEWALL → sigma Phase-0 classification → audit-
level framework audits). Next fire: R33 cross-disease framework
audit, or WHM sweep execute (pending op), or remaining per-disease
THEWALL docs (pericarditis, myocarditis, encephalitis). |
