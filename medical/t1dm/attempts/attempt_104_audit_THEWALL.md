# Attempt 104 — Claim-Backing Audit: t1dm/THEWALL.md (2022 lines)

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: medical/t1dm/THEWALL.md (2022 lines, deferred since Fire 9).
Sampled L1-80 (framework/thesis section) + L1000-1060 (mid-document
cross-references run_122–125) + L1970-2021 (tail cross-references
run_166–170). Full line-by-line audit NOT performed — document is too
large and largely consists of cross-reference inclusions from
dysbiosis/numerics/ runs.
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: audit log fires 1-34.

## Executive verdict

**t1dm/THEWALL.md has a dual structure**:

1. **Lines 1–~100**: the disease-level THEWALL document proper —
   one-sentence thesis, unified model, Lean theorem (crown_jewel in
   InequalityReversal.lean), evidence table with confidence grades,
   narrowed-to-three-things wall (primary = blood draw; mechanistic
   = FOXP1 restoration + trehalose flux; clinical = validation).

2. **Lines ~100–2022**: **~50+ cross-reference sections** importing
   specific mechanism findings from dysbiosis/numerics/run_NNN files
   into T1DM-relevant context. Each run section has consistent
   structure: Relevance tag (HIGH/MODERATE), numbered mechanistic
   findings, dated tag line.

This structure means the audit covers TWO different document types:
- Top: THEWALL-style synthesis (like POD/THEWALL, dysbiosis/THEWALL,
  medical/THEWALL, me_cfs/THEWALL)
- Bottom: a structured cross-reference catalog importing ~50 dysbiosis
  numerics runs

**🔴 RED count**: 1 (cumulative mechanism-counting claim)
**🟡 YELLOW count**: 6
**🟢 GREEN count**: 11

## RED findings

### R35 — T1DM THEWALL cumulative "Nth β cell death/dysfunction mechanism" counting

**The claim pattern**: multiple cross-reference sections label
newly-imported mechanisms as "15th β cell death mechanism" (run_122
NLRP1), "27th dysfunction mechanism" (run_167 GATA3), "28th β cell
death mechanism" (run_168 IRF1), etc.

**Why load-bearing**: a cumulative count of 15-28+ distinct β-cell
death/dysfunction mechanisms is a strong claim. Used across the
document as a counting frame for how much mechanism coverage the
dysbiosis framework has absorbed.

**Concern**: it's unclear whether these are genuinely 28 distinct
mechanisms, or whether they represent overlapping pathways counted
separately. For example:
- NLRP1 pyroptosis (run_122, "15th")
- NLRP3 pyroptosis (canonical, pre-counted)
- NLRC5 HLA-I surge → CTL killing (run_169)
- IRF1 → iNOS → NO (run_168, "28th")
- T-bet → IFN-γ autocrine (run_166)
- Perforin/granzyme CTL (run_162)

Several of these share downstream effectors (GSDMD, caspase-1, NO,
mitochondrial permeabilization) and differ mainly in the upstream
priming signal. Counting them as "28 distinct mechanisms" may
inflate the mechanistic surface area.

**Required fix**: add a **Mechanism-Counting Methodology** note near
the first use (or in gap.md's resolved-gaps section) specifying how
mechanisms are counted: by upstream receptor, by downstream
effector, by transcription factor node, etc. Without this, "28
distinct mechanisms" is a claim a skeptical reader cannot verify.
Alternative: replace "28th mechanism" counting with "mechanism #Nth
to be characterized in the framework" (sigma-method discovery
counting, not nature-of-β-cell-death counting).

## YELLOW findings

| # | Section / line | Claim | Source gap |
|---|----------------|-------|------------|
| Y222 | L26 "crown_jewel theorem (InequalityReversal.lean, 0 sorry)" | Confirm Lean file exists and theorem name matches `grep -n "crown_jewel" medical/lean/InequalityReversal.lean` |
| Y223 | L44 "R(0.30) ≈ 0.01063 >> D(0.30) ≈ 0.00090 (12× margin)" | Thread the numerics script that produces these specific values; verify parameter substitutions |
| Y224 | L54 "Butler 2005: 72% of patients with >50-year T1DM retain detectable beta cells (refined from 88%)" | Refined number — cite Meier 2005 Diabetologia PMID 16205881 and specify which sub-cohort the 72% applies to |
| Y225 | L1001 "Johnson 2018 Cell" for DPP4i DPP8/9 safety differential | Specific citation — thread PMID; "Johnson 2018 Cell" could be wrong journal (drug mechanism papers often in *Cell Reports*) |
| Y226 | L1015 "Cooper 2008 Nat Genet BACH2 rs3757247 T1DM GWAS top-7 non-MHC locus" | Barrett et al. 2009 is the canonical early T1DM-GWAS paper; Cooper 2008 may be correct for BACH2 — verify PMID |
| Y227 | L2018 "Perone 2006 NOD prevention Gal-1 → 78% T1DM-free at 25 weeks vs 5% controls" | Specific effect size — thread PMID (Perone 2006 J Immunol or Diabetes); 78% NOD prevention is a strong claim |

## GREEN findings

- **G257** L4-6 **One-sentence thesis**: "The body has been regenerating
  beta cells for your entire life with this disease. It never
  stopped. The wall is not biology — it's that nobody told you to
  clear the virus that's been winning the arms race." Emotional +
  mechanistic + actionable.
- **G258** L8-19 **Unified model block** — CVB persists → 2A protease
  DMD -32x → FOXP1 -67x → LAMP2 -2.7x → chronic immune activation →
  D > R → disease; BUT R > 0 always (Butler 72%/50yr). 4-step
  causal chain + 1 counter-claim.
- **G259** L22-47 **crown_jewel Lean theorem block** with: formal
  conditions (IF D(B_threshold) < R(B_threshold) AND D(1) > R(1)
  THEN B* exists and is stable), current state R ≈ 0.8D, goal R > D
  at B = 0.30, numerical bound R(0.30) >> D(0.30) 12× margin, 7
  protocol mechanisms targeting specific terms.
- **G260** L51-66 **Evidence table with CONFIDENCE column + CHANGE
  column**. CHANGE column shows grade evolution (what's new, what's
  unchanged, what's upgraded). Live document tracking.
- **G261** L68-80 **"Wall Narrowed to Three Things"**: PRIMARY (one
  blood draw, $80, 5-day turnaround) + MECHANISTIC (FOXP1
  restoration timeline + TD autophagy flux, 2 uncertainties labeled
  "not blockers") + CLINICAL (validation trial). Explicit wall-
  ranking.
- **G262** Cross-reference sections (run_122 through run_170+)
  maintain consistent structure: **Relevance tag (HIGH/MODERATE)**,
  numbered mechanistic findings, dated cross-reference tag at
  bottom. Structural discipline across ~50 imports.
- **G263** **run_125 harmine rosacea contraindication** — "the
  framework's first explicit drug/supplement contraindication
  arising from dual-disease mechanistic analysis." Dual-disease
  reasoning producing a concrete clinical rule (harmine
  contraindicated in T1DM+rosacea patients). This is the kind of
  actionable cross-disease finding the unified framework is
  supposed to produce.
- **G264** **run_123 BACH2 Vitamin A recommendation** — specific
  mechanism-based intervention for rs3757247 risk allele carriers
  (retinyl palmitate → RAR-α/RXR → BACH2 ↑ → Treg identity
  reinforced). Complementary to calcitriol (different receptor).
  Stratification-aware personalization.
- **G265** L1001 **DPP4 inhibitor drug-class differentiation**:
  sitagliptin (DPP4-selective) vs saxagliptin/alogliptin (DPP8/9
  off-target → NLRP1 activation). Clinical prescribing
  recommendation derived from molecular mechanism. Actionable for
  LADA/T1DM patients.
- **G266** Cross-references consistently include **bridge lines to
  prior runs** (e.g., "run_147 bridge" for PARP-1/NAD⁺ from
  run_168's IRF1/iNOS section). Explicit cross-subdir cross-links
  threaded.
- **G267** **R35 concern aside**, the ~50 mechanism imports each
  have specific papers cited, specific effect sizes, specific
  therapeutic implications. Individually grade-able; collectively
  the mechanism-counting inflation risk (R35) is the main concern.

## Recommended fixes (ordered)

1. **[P0]** Add **Mechanism-Counting Methodology note** per R35 —
   specify whether "28th β-cell death mechanism" counts upstream
   receptors, downstream effectors, transcription factor nodes, or
   discovery order. Current use risks inflating the mechanistic
   surface area.
2. **[P1]** Verify Lean file `crown_jewel` theorem existence +
   0-sorry status (Y222). This is the document's central formal
   claim.
3. **[P2]** Thread PMIDs for key cross-references: Butler 2005
   Diabetologia (Y224), Cooper 2008 Nat Genet BACH2 (Y226), Perone
   2006 Gal-1 NOD (Y227), Johnson 2018 DPP4i (Y225).

## Non-audit observations

- **THEWALL.md's size (2022 lines) is unusual** for a synthesis
  document. It's actually two documents: (a) ~100-line synthesis
  at top, (b) ~1900-line cross-reference catalog below. These could
  be split into THEWALL.md + THEWALL_CROSSREFS.md for cleaner
  navigation.
- **The ~50 cross-reference imports function as the mechanistic
  backbone** — each dysbiosis/numerics/run_NNN finding flows back
  into T1DM context through THEWALL.md. This is the
  "cross-pollination" process documented in CROSS_POLLINATION.md
  (referenced in MEDICAL_PROBLEMS.md L79).
- **The cross-reference pattern is a sigma-method Maps-Include-Noise
  artifact at the mechanism-corpus level** — individual numerics
  runs would be hard to find (stored in dysbiosis/numerics/), but
  THEWALL.md catalogs their T1DM-relevant takeaways. A T1DM
  researcher reading THEWALL.md gets the full mechanism cross-ref
  without having to traverse the dysbiosis/numerics/ directory.
- **me_cfs/THEWALL.md (1719 lines) likely has similar structure** —
  synthesis top + cross-reference catalog bottom. Audit approach
  should be the same sampling pattern.

## Tag

104 (t1dm/THEWALL.md). Sampled 3 of 50+ sections in the 2022-line
document. **1 🔴 R35**: cumulative "Nth β-cell death/dysfunction
mechanism" counting (NLRP1 15th, GATA3 27th, IRF1 28th, etc.) may
inflate the mechanistic surface area — different runs share
downstream effectors (GSDMD, iNOS, mitochondrial permeabilization)
with different upstream primers; a mechanism-counting-methodology
note would clarify whether the count is by receptor/effector/TF/
discovery order. 6 🟡 (Lean file verification, specific effect-size
numerics script threading, Butler 2005 sub-cohort specification,
Cooper 2008/Johnson 2018/Perone 2006 PMID threading). **11 🟢**:
one-sentence thesis; unified model with 4-step causal chain + R > 0
counter-claim; **crown_jewel Lean theorem block** with formal
conditions + numerical bound + 7 protocol mechanisms; evidence
table with CONFIDENCE + CHANGE columns (grade evolution tracked);
**wall narrowed to three things** (primary blood draw, mechanistic 2
uncertainties, clinical validation); ~50 cross-reference imports
with consistent structure (Relevance tag + numbered findings +
dated tag); **harmine rosacea contraindication** from dual-disease
mechanistic analysis; **BACH2 Vitamin A stratification** for
rs3757247 carriers; **DPP4 inhibitor drug-class differentiation**
(sitagliptin preferred over saxagliptin/alogliptin in T1DM).
**Observation**: THEWALL.md is dual-structure (synthesis + cross-
reference catalog); me_cfs/THEWALL.md likely similar. Consider
splitting THEWALL.md + THEWALL_CROSSREFS.md for navigability. Next
fire: me_cfs/THEWALL.md or R33 cross-disease framework audit or
WHM sweep (pending).
