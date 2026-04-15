# Attempt 101 — Claim-Backing Audit: attempt 043

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: medical/t1dm/attempts/attempt_043_the_complete_picture.md
(357 lines — warranted its own audit fire)
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: attempts 095–100

## Executive verdict

Attempt_043 is the t1dm/ directory's most complete synthesis to date —
merging all four (now five) mountains with the patient-specific timeline
and proposing a single $1,200 bloodwork panel as the gap-closer. It
introduces **one genuinely novel hypothesis** (D-lactate as a hidden
glucose-production multiplier in T1DM) and one **mechanism error**
worth correcting (humans DO have D-LDH, encoded by LDHD).

The synthesis structure is exemplary; the individual claims have mixed
sourcing. Because this is the "complete picture" attempt, errors and
overstatements here propagate to every downstream attempt that cites
043. High-impact audit target.

**🔴 RED count**: 3
**🟡 YELLOW count**: 9
**🟢 GREEN count**: 6

## RED findings

### R18 — attempt_043 L37–46, L143–162 (D-LDH / D-lactate mechanism)

**The claim**:
> "D-lactate: NOT efficiently processed by human L-LDH (humans have
> L-lactate dehydrogenase, not D-lactate dehydrogenase) … D-lactate
> triggers gluconeogenesis but ISN'T consumed by the process → NET
> RESULT: excess glucose production"

**Why load-bearing**: the D-lactate hypothesis is a genuinely new
Mountain-6 mechanism introduced in 043. The entire "D-lactate →
gluconeogenesis without consumption → excess glucose → beta cell
stress" chain rests on this premise. If the premise is wrong, the
mechanism collapses.

**Concern**:
1. **Humans DO have D-lactate dehydrogenase**: encoded by the LDHD
   gene, located in the mitochondrial matrix. (Flick & Konieczny 2002
   *J Biol Chem*; de Bari et al. 2002; Drabkin et al. 2018
   demonstrated LDHD's physiological role.) LDHD oxidizes D-lactate to
   pyruvate using FAD. Humans are NOT D-LDH-null; they have a
   mitochondrial D-LDH.
2. D-lactate CAN be converted to pyruvate (by LDHD) and then enter
   gluconeogenesis. It IS a gluconeogenic substrate, though less
   efficient than L-lactate because LDHD capacity is rate-limited.
3. The mechanism "triggers gluconeogenesis but isn't consumed" is
   logically self-defeating: gluconeogenic substrates ARE consumed in
   the process of making glucose. The attempt likely means "D-lactate
   accumulates because LDHD capacity is exceeded, and in the
   meantime…"; but the framing as written is mechanistically wrong.
4. D-lactic acidosis is a real clinical syndrome (short bowel
   syndrome, Petersen 2005 *NEJM*) but occurs at >3 mmol/L serum
   D-lactate — three orders of magnitude higher than the subclinical
   levels that would be produced by ordinary gut dysbiosis. The
   "subclinical D-lactate" driving T1DM hypothesis is not supported by
   the clinical D-lactic-acidosis literature.

**Required fix**:
1. Correct the D-LDH claim: humans have mitochondrial LDHD (D-lactate
   dehydrogenase); the issue is **rate-limitation** of LDHD capacity,
   not absence.
2. Re-mechanism the D-lactate effect: if D-lactate enters the liver,
   it IS metabolized (by LDHD → pyruvate → glucose or back to
   lactate-glucose cycle); the "trigger without consumption" framing
   should be replaced by "LDHD-limited metabolism may shift the
   lactate-pyruvate equilibrium" or similar.
3. Mark the "D-lactate-driven T1DM" hypothesis as **novel to this
   attempt** — no published T1DM literature supports subclinical
   D-lactate as a pathogenic factor. This is hypothesis-generating,
   not hypothesis-supported.
4. Thread D-lactic-acidosis-syndrome literature (Petersen 2005 NEJM,
   Uribarri 1998) to contextualize when D-lactate elevation is
   clinically meaningful.

### R19 — attempt_043 L69–74, L212 (CVB → thyroid → Hashimoto's)

**The claim**:
> "CVB also infects THYROID (CAR receptor expressed there too) … Same
> persistence mechanism in thyroid tissue. Hashimoto's thyroiditis
> (autoimmune thyroid disease) … Three diagnoses from one virus: T1DM
> + thyroiditis + high cholesterol"

**Why load-bearing**: this claim unifies three co-occurring diagnoses
(T1DM, Hashimoto's, hyperlipidemia) under a single CVB-persistence
cause. If established, it implies the antiviral protocol treats all
three simultaneously. If not, each condition needs separate
consideration.

**Concern**:
1. **CAR (CXADR) IS expressed in thyroid tissue** — this part is
   correct (Fechner et al. 1999; protein atlas confirms).
2. **CVB causing Hashimoto's in humans is hypothesis, not finding.**
   There are scattered reports of enteroviral RNA in thyroid tissue of
   Graves' disease or Hashimoto's patients (Akeno et al., Tozzoli et
   al.) but these are exploratory; causal link is not established. The
   polyendocrine autoimmune clustering (APS-II/III) is explained by
   shared HLA risk alleles and Treg deficit independent of any single
   pathogen.
3. The **"three diagnoses from one virus"** framing overstates to the
   point of being misleading. Other explanations for T1DM+Hashimoto
   co-occurrence (~17–30%) are at least as well-supported as single-
   virus causation.

**Required fix**: restate as hypothesis ("CAR expression in thyroid
raises the possibility that CVB may also persist there; enteroviral
RNA has been detected in some Hashimoto's tissue samples but causal
link is not established"). Acknowledge the HLA-shared-risk alternative.

### R20 — attempt_043 L165–172 (L. acidophilus producing D-lactate in
yogurt / probiotics — "paradoxically")

**The claim**:
> "Lactobacillus acidophilus (in yogurt, probiotics — paradoxically) …
> These thrive on fermentable carbohydrates. On keto: starved. On
> carbs: fed."

**Why load-bearing**: the Stage-1b-protocol recommends REPLACING
"D-lactate producers" with L. rhamnosus GG + L. plantarum 299v at
L276–277. If the species classification is wrong, the probiotic
substitution is mis-targeted.

**Concern**:
1. **L. plantarum produces DL-lactate (racemic), not L-only.** This is
   well-established (most L. plantarum strains carry both L-LDH and
   D-LDH isozymes). Recommending L. plantarum 299v as an "L-lactate-
   only strain" is incorrect.
2. L. rhamnosus GG is predominantly L-lactate-producing but not
   exclusively.
3. Heyrovská / Åhrne / Vesa strain-level surveys exist; the
   recommendation should cite specific strains with verified lactate
   stereochemistry, not blanket species claims.
4. The "yogurt/probiotics paradoxically" framing implies yogurt is
   harmful in T1DM — a strong dietary claim that is not supported at
   the level of subclinical D-lactate dysbiosis.

**Required fix**:
1. Correct the lactate-stereochemistry attribution for L. plantarum
   (DL, not L-only).
2. If the probiotic substitution is retained, cite strain-specific
   lactate profiles from a published survey (Axelsson 2004 or similar).
3. Remove the "yogurt paradoxically harmful" framing unless supported
   by specific T1DM-yogurt-risk literature (which, per attempt 016's
   TRIGR note, is inconclusive).

## YELLOW findings

| # | Attempt / line | Claim | Source gap |
|---|----------------|-------|------------|
| Y81 | 043 L51, L218 | "Butler 2021: stressed beta cells produce more neoantigens" | Butler's canonical papers are 2005 *Diabetologia* (Meier et al.) and 2006 *Diabetologia* (89-year-old). "Butler 2021" isn't a recognized specific ref — may be Zaldumbide et al. or a newer neoantigen paper. Source or correct citation. |
| Y82 | 043 L80 | "Beta cells: ~60-80% remaining (based on low insulin needs)" | N=1 inference; mark as estimate not measurement |
| Y83 | 043 L131 | "C-peptide likely still 0.5-0.9" | N=1 prediction carried from attempt_028 (Y44); already logged |
| Y84 | 043 L196–197 | "Rifaximin (gut-specific, minimal systemic absorption)" — as targeted anti-D-lactate therapy | Rifaximin is used clinically for D-lactic acidosis in short-bowel-syndrome patients — IF that indication is cited, claim is supported; without, it's an off-label extrapolation |
| Y85 | 043 L249 | "25-OH Vitamin D Likely 15-30 (insufficient)" | N=1 prediction from attempt_031 Y47; consistent with prior |
| Y86 | 043 L267 | "Stage 1b probiotics: L. rhamnosus GG + L. plantarum 299v" | See R20; requires strain-level source |
| Y87 | 043 L295 | "Teplizumab NOW effective because: virus cleared, ADE reduced, D-lactate normalized, gut balanced, Tregs restored by butyrate" | Compound assertion — each sub-claim has its own uncertainty; compound confidence should be the product, not the sum |
| Y88 | 043 L334–344 | The 8-test gap table is well-framed, but test costs ($200–300 for VP4 IgG, D-lactate, 16S) are retail estimates — source when ordering |
| Y89 | 043 L220 | "BHB (from keto/fasting) → SUPPRESSES inflammation + PROTECTS beta cells" | Inherits attempt_029 G13; Youm 2015 *Nat Med* for NLRP3; Shimazu 2013 *Science* for HDAC; thread refs |

## GREEN findings

- **G34** attempt_043 L235 — "After 61 years: STILL HAPPENING (88% of
  patients)" — properly cites the Butler 2005 population finding as
  population-level (88% of 42), correcting the N=1 framing error from
  attempt_027 (R9 in attempt_097_audit). The audit-corrected phrasing
  made it into this attempt.
- **G35** attempt_043 L334–345 — the "8-test gap table" at the end
  converts the synthesis's loose ends into a priced, enumerable
  checklist. Each unknown has a measurement and a cost. This matches
  math-standard "what proven vs what remains" with an explicit
  experiment/measurement column.
- **G36** attempt_043 L140–172 — the D-lactate hypothesis, while
  incorrect in its D-LDH claim (R18), is properly **offered as a
  hypothesis** with a listed path for falsification (serum/urine/stool
  D-lactate assay, 16S microbiome sequencing). This is good hypothesis
  hygiene even when the mechanism is wrong.
- **G37** attempt_043 L87–112 — the "keto as accidental multi-mountain
  protocol" block at L87–112 cleanly enumerates WHY keto worked across
  M1/M2/M3/M4/D-lactate. Each row is a testable claim linked to
  specific mechanisms from prior attempts. Internal cross-reference
  structure is math-standard: claim → mechanism → citation path.
- **G38** attempt_043 L356 — "The gap is not a concept. The gap is
  $1,200 of bloodwork." Converts the 43-attempt synthesis into a
  single-action item. Matches math-standard "the binding analytical
  piece is (†); everything else reduces to verifying (†)" framing.
- **G39** attempt_043 L316–328 — the "Cheap Path (No Rx Required)"
  subsection correctly separates supplements-that-are-safe from
  prescriptions-with-trade-offs. Implicit risk-calibration: default to
  safer interventions; add prescriptions conditional on data. This
  matches sigma-method "structural enforcement over instruction" (v5
  principle).

## Recommended fixes (ordered)

1. **[P0] attempt_043**: correct the D-LDH claim (R18). Humans have
   mitochondrial LDHD. Re-frame the D-lactate mechanism accordingly.
   Mark the "subclinical-D-lactate-drives-T1DM" link as novel
   hypothesis with no published T1DM support.
2. **[P0] attempt_043**: restate the CVB→thyroid→Hashimoto's chain
   (R19) as hypothesis with alternative (HLA-shared-risk) explanation
   for the APS-II/III co-occurrence.
3. **[P0] attempt_043**: correct the L. plantarum lactate-
   stereochemistry (R20). If probiotic substitution is retained, cite
   strain-level sources.
4. **[P1] attempt_043**: resolve the "Butler 2021" citation (Y81) —
   either point to a specific 2021 paper from Butler's lab or correct
   to Butler 2005.
5. **[P2] attempt_043**: thread Youm 2015 *Nat Med* + Shimazu 2013
   *Science* for BHB's NLRP3 and HDAC mechanisms (Y89).
6. **[P2] attempt_043**: the compound-teplizumab-effectiveness
   assertion (Y87) should be stated as conditional probability — each
   precondition reduces uncertainty, the combined statement should
   acknowledge multiplicative uncertainty.

## Non-audit observations (map features)

- Attempt_043 is the correct **synthesis anchor** for the t1dm/
  corpus. Future readers who come in cold should start here, not at
  attempt_001. Recommend that t1dm/gap.md and t1dm/README.md point to
  043 as the current synthesis with the audit-log flags noted.
- The **D-lactate hypothesis is a genuine research idea** even if the
  specific D-LDH mechanism claim is wrong. The observation that
  carb-reintroduction after 5 years of keto produced disproportionate
  insulin demand IS worth explaining; D-lactate is one candidate among
  several (proinsulin:C-peptide ratio, hepatic insulin resistance from
  lipid redistribution, CGM postprandial glucose excursion patterns).
  Keep the hypothesis; correct the mechanism; add competing hypotheses.
- The **$1,200 bloodwork framing** is the attempt's strongest
  contribution. The 8-test list is actionable, costed, and maps each
  test to a specific binary decision in the protocol. This is the
  kind of "gap-as-checklist" output that other non-math subdirs should
  emulate.

## Tag

101. Sixth claim-backing audit pass on t1dm/. Attempt_043 is the
synthesis anchor for the directory. 3 🔴: (i) D-LDH claim is wrong —
humans have mitochondrial LDHD; the "D-lactate triggers gluconeogenesis
without being consumed" framing is mechanistically self-defeating; the
entire subclinical-D-lactate-drives-T1DM link is a novel hypothesis
with no published T1DM support; (ii) CVB→thyroid→Hashimoto's
"three-diagnoses-one-virus" overstates a hypothesis as unified
explanation; (iii) L. plantarum is DL-lactate-producing (not L-only),
so the Stage-1b probiotic substitution is mis-specified. 9 🟡 (Butler
2021 citation gap, Youm 2015/Shimazu 2013 BHB refs, rifaximin source,
compound-teplizumab-effectiveness uncertainty). 6 🟢 (Butler 2005
population finding correctly restated (audit-corrected), 8-test gap
table, hypothesis hygiene, keto multi-mountain cross-reference, "gap
is $1,200 of bloodwork" sharp framing, "Cheap Path" risk-calibrated
subsection). Next fire: t1dm/attempts 046-055 or start t1dm/top-level
(PROBLEM.md, gap.md, THEWALL.md, README.md).
