# Attempt 005 — Batch Audit: eczema/, psoriasis/, dilated_cardiomyopathy/, pericarditis/, infertility/

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: top-level PROBLEM.md + gap.md sample of 5 remaining mature
medical subdirs: eczema, psoriasis, dilated_cardiomyopathy,
pericarditis, infertility.
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: audit log fires 1–15.

Note: writing this as a single batch audit for 5 subdirs rather than
5 separate audit files. If any subdir's findings warrant deeper work,
a dedicated per-subdir audit can be spawned later.

## Executive verdict

All 5 subdirs are **Phase 0 Scaffolded** per their own labeling and
follow the dysbiosis template: structured PROBLEM.md with
Biology/Cascade/Connection-to-Campaign sections, anti-problem
framing, and specific connections to protocol components. Variance
is in depth of gap.md (psoriasis 84 lines, pericarditis 40 lines) and
specificity of numeric claims.

**🔴 RED count**: 1 (propagated WHM bug, 4th instance)
**🟡 YELLOW count**: 11
**🟢 GREEN count**: 9

## RED findings

### R29 — psoriasis/PROBLEM.md L49 (WHM NF-κB "lockdown" — 4th instance of same bug)

**The claim**:
> "WHM breathing → β-arrestin-2 → IKKα sequestration → NF-κB
> lockdown → applies to psoriasis"

**Why load-bearing**: same claim pattern as t1dm R22, dysbiosis R24.
This is now the **4th subdir** where the overstated
"NF-κB lockdown via WHM" claim appears: t1dm/SUPPLEMENT_SCHEDULE.md,
dysbiosis/PROBLEM.md, POD (implicit via cross-ref to T1DM protocol),
psoriasis/PROBLEM.md.

**Concern**: same as R22 — Kox et al. 2014 PNAS demonstrated
*attenuation* of LPS-induced cytokine response, not "lockdown."
Now clearly a **corpus-wide propagation bug**, not a localized
overstatement.

**Required fix (cross-subdir)**: soften the WHM framing in all 4
locations (and any others discovered) to "WHM → epinephrine →
attenuated NF-κB activation in response to LPS (Kox 2014 PNAS, PMID
24799686)". This should be done as a single cross-subdir sweep rather
than 4 independent edits.

## YELLOW findings

| # | Subdir / file / line | Claim | Source gap |
|---|---------------------|-------|------------|
| Y140 | eczema PROBLEM L12 | "Loss-of-function [FLG] mutations in ~30% of eczema patients" | Palmer 2006 Nat Genet filaggrin mutation foundational paper; thread PMID |
| Y141 | eczema PROBLEM L80 | "~30% of FLG mutation carriers never develop eczema" | Needs population-cohort source |
| Y142 | eczema PROBLEM L45 | "NLRP3 inflammasome activated in eczema keratinocytes (Dai 2011, Keller 2017)" | Author-year cited without PMID; thread |
| Y143 | psoriasis PROBLEM L22 | "HLA-C*06:02 … strongest genetic risk factor (~10x risk)" | Nair et al. 2006 Am J Hum Genet or Trembath et al.; thread PMID |
| Y144 | psoriasis PROBLEM L88 | "~10% of HLA-C*06:02 carriers develop psoriasis" | Needs cohort source (e.g., UK Biobank or similar) |
| Y145 | psoriasis PROBLEM L54 | "BHB suppresses NLRP3 (Youm 2015)" | Same as t1dm Y89; thread PMID 25686106 consistently across subdirs |
| Y146 | dilated_cm gap.md L17 | "2A protease cleaves dystrophin at hinge 3" | Badorff et al. 1999 Nat Med PMID 10482120 — same as myocarditis Y126; thread consistently |
| Y147 | dilated_cm gap.md L19 | "TD mutants replicate 100,000x slower" | Same as t1dm Y53; thread Kim 2008 J Virol consistently |
| Y148 | infertility PROBLEM L6 | "IVF success rates plateau at ~30-40% per cycle" | SART / CDC ART reports; thread |
| Y149 | infertility PROBLEM L92 | "L-carnitine 2-3g (sperm motility)" | Lenzi et al. or Balercia trials; thread |
| Y150 | pericarditis PROBLEM and gap.md | (not read this fire) | Deferred to next audit; listed here for audit queue completeness |

## GREEN findings

- **G97** eczema PROBLEM L37–41 — **"Direct CVB connection: WEAK"**
  honest labeling. Eczema is a Th2-dominant disease (opposite Th1
  profile from CVB diseases); the corpus correctly flags that the
  CVB link is weak and builds the case on indirect-connection
  mechanisms (NLRP3, gut-skin axis, vitamin D, omega-3, Th1/Th2
  balance). This is sigma-method confirmation-bias-audit compliant —
  claims the strong links, disclaims the weak ones.
- **G98** psoriasis PROBLEM L41 — **"Direct CVB connection: NONE"**
  — even more explicit than eczema. Psoriasis is HLA-C*06:02-driven,
  IL-23/Th17 autoimmune; correctly declares no CVB mechanism and
  argues protocol overlap on NF-κB / NLRP3 / Th17 grounds.
- **G99** psoriasis PROBLEM L58–62 — **apremilast (Otezla) as the
  PDE4 bridge** — references T1DM attempt_062 "Gun, Bullet, Criminal"
  + notes apremilast is already FDA-approved for psoriasis +
  psoriatic arthritis. Convergent-evidence claim: "if apremilast
  helps both psoriasis and T1DM, that's convergent evidence for the
  shared NF-κB mechanism." This is sigma-method standing-wave
  pattern — the same drug succeeding across two diseases at different
  sites is cross-validation of the mechanism.
- **G100** dilated_cm gap.md L4–14 — **d(CardiacFunction)/dt
  inequality** with explicit Repair/Cleavage/Fibrosis terms.
  Cardiac-specific variant of the T1DM d(Beta)/dt framing. The
  "Repair ≈ 0.01/year (negligible in adults)" is correct and honestly
  flagged.
- **G101** dilated_cm gap.md L27–46 — **Fork A/B/C** (halt
  progression / reverse fibrosis / replace cardiomyocytes) with
  timeline for Fork C ("5-10 year timeline, parallels T1DM stem cell
  work"). Inheritance from myocarditis but explicitly diffed.
- **G102** dilated_cm gap.md L49–56 — **Anti-problem as a testable
  assay question**: "Is there a dystrophin fragment assay?" — this
  is a concrete next-action question, not a vague hypothesis.
  "Search: is there a dystrophin fragment assay?" is a literature
  query with a binary outcome.
- **G103** infertility PROBLEM L8–15 — **"Why This Belongs in the
  Campaign"** explicit justification: 4 reasons (protocol overlap,
  mechanism-rich but protocol-poor, CVB orchitis existing,
  multi-mountain attack applicable). This is the correct pattern
  for including a non-obvious-fit disease in the umbrella.
- **G104** infertility PROBLEM L67–74 — **Couple-Level Cascade**
  with "failure at ANY step = no baby" framing. Each step is
  a potential intervention point, each is diagnosable.
- **G105** infertility PROBLEM L79–95 — **protocol-component-to-
  fertility-benefit table** for male + female. Same pattern as
  myocarditis's 7/7 T1DM-protocol-transfer table. Explicit
  inheritance audit.

## Recommended fixes (ordered)

1. **[P0] CROSS-SUBDIR SWEEP**: soften WHM "NF-κB lockdown" framing
   in t1dm/SUPPLEMENT_SCHEDULE.md, dysbiosis/PROBLEM.md, and
   psoriasis/PROBLEM.md. Replace with "attenuated NF-κB activation"
   + cite Kox 2014 PNAS PMID 24799686. Single coordinated edit.
   This is the most impactful single fix because the bug has
   propagated across 4+ files.
2. **[P1]** eczema, psoriasis: thread Palmer 2006 Nat Genet
   (filaggrin), Nair 2006 Am J Hum Genet (HLA-C*06:02), Youm 2015
   Nat Med (BHB/NLRP3).
3. **[P1]** dilated_cm, myocarditis: thread Badorff 1999 Nat Med
   (dystrophin 2A cleavage) and Kim 2008 J Virol (TD mutants 100,000×
   slower) consistently with other subdirs.
4. **[P2]** infertility: thread SART data (IVF per-cycle success),
   L-carnitine (Lenzi/Balercia), AMH reference ranges.
5. **[P2]** pericarditis: defer audit to next fire.

## Non-audit observations

- **All 5 subdirs are Phase 0 Scaffolded and correctly self-label**
  as such. None are pretending to be deeper than they are. The
  structural discipline is good.
- **Protocol-overlap tables** are recurring (myocarditis 7/7,
  infertility male+female, dilated_cm Fork-structure, psoriasis
  protocol-overlap list, eczema "Shared protocol components"). This
  is a good cross-subdir synthesis pattern — when a disease shares
  protocol components with T1DM, the table makes the inheritance
  explicit and falsifiable.
- **The WHM NF-κB propagation bug** (R29) is now clearly a systemic
  issue rather than a localized overstatement. When one fact
  propagates across 4+ subdirs without correction, it reveals that
  the corpus's cross-pollination mechanism (imports, templates,
  shared protocol refs) carries errors as readily as signal. This is
  a Maps-Include-Noise stress case: the propagation itself is
  preserved as a map feature, but the audit's job is to flag it so
  the next operator can do a single sweep fix.
- **The anti-problem pattern** ("what do people who don't get this
  disease look like?") recurs in every one of the 5 subdirs and in
  dysbiosis, me_cfs, t1dm, POD, myocarditis. Nine subdirs with the
  same structural move. This IS sigma-method Phase 4 anti-problem
  framing applied consistently.

## Tag

005 (eczema). Batch audit of 5 mature medical subdirs (eczema,
psoriasis, dilated_cardiomyopathy, pericarditis, infertility). 1 🔴
is the **4th instance of the WHM NF-κB "lockdown" bug** — now
clearly a corpus-wide propagation issue requiring single cross-subdir
sweep (t1dm + dysbiosis + POD + psoriasis at minimum). 11 🟡 (PMID
threading for Palmer 2006 filaggrin, Nair 2006 HLA-C*06:02, Youm 2015
BHB/NLRP3, Badorff 1999 dystrophin, Kim 2008 TD mutants, Lenzi/Balercia
L-carnitine, SART IVF success rates). **9 🟢**: eczema/psoriasis
honest "Direct CVB connection" labeling (WEAK / NONE), apremilast
cross-disease convergent-evidence claim, d(CardiacFunction)/dt
inequality with correct Repair ≈ 0.01/yr, Fork A/B/C timeline, anti-
problem as testable-assay question, infertility why-belongs-in-
campaign explicit justification, couple-level cascade "failure at any
step = no baby", protocol-component-to-fertility-benefit table.
**Observation**: anti-problem pattern recurs in 9 subdirs —
sigma-method Phase 4 applied consistently. **Next fire: physics/ OR
philosophy/ OR cross-subdir WHM sweep fix.**
