# Attempt 097 — Claim-Backing Audit: attempts 021–030

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: medical/t1dm/attempts/attempt_021 … attempt_030
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: attempt_095_audit_001_to_010.md, attempt_096_audit_011_to_020.md

## Executive verdict

The third decade is the convergence arc — the three-mountain structure
collapses into a single "tip the balance equation" thesis (attempt_030).
Citations are a mixed bag: the transdifferentiation papers (Wang 2019,
Thorel 2010, Collombat 2009, Soltani 2011) are well-threaded; the
viral-persistence arc (attempts 024–025) rests on weaker sourcing and
has the decade's most-concerning overreach.

**🔴 RED count**: 4
**🟡 YELLOW count**: 13
**🟢 GREEN count**: 6

**Structural observation (continues S1/S2 from attempt_096):**
Attempts 027 and 030 frame the work partly as **operator-specific
synthesis** ("For the operator Specifically", "diagnosed 2019, 5 years
off insulin on keto, now 2u/meal"). This is legitimate personal
research reasoning — and attempt_030 correctly labels its own
percent-shift estimates as "illustrative, not measured" (good
self-audit). But it means the t1dm/ corpus is operating as a hybrid of
public claim-backing synthesis and private protocol design. For
audit purposes, treat the operator-specific sections as separable:
they are not claims about the world, they are reasoning about a
specific N=1 case. Flag them in the file structure, not as audit
findings.

## RED findings

### R6 — attempt_024 L35 (fluoxetine as anti-CVB therapy)
> "Fluoxetine: The SSRI antidepressant. Unexpectedly potent against
> CVB in vitro. Blocks viral replication via sigma-1 receptor. Already
> FDA-approved, safe, cheap (~$10/mo generic)."

**Plus the Stage 1a prescription at L50**:
> "Fluoxetine 20mg daily × 3 months (anti-CVB + antidepressant benefit
> + safe)"

**Why load-bearing**: the fluoxetine recommendation becomes Stage 1
in every subsequent protocol (025, 027, 030). If fluoxetine does not
actually clear persistent pancreatic CVB in humans, every downstream
attempt's "net effect after Stage 1" is wrong.

**The specific concern**: Ulferts et al. *Antiviral Research* 2013
(PMID: 23872244) showed fluoxetine inhibits CVB3 replication in cell
culture at ~5–10 µM. Achieving this concentration in pancreatic tissue
with a 20 mg PO daily antidepressant dose (therapeutic plasma ~0.05–0.3
µM) is **two orders of magnitude below in-vitro activity**. The
in-vitro → in-vivo gap is not closed. DiViD-Intervene (Krogvold et al.
*JAMA* 2024) tested pleconaril + ribavirin, not fluoxetine, and found
modest C-peptide preservation. No human trial has tested fluoxetine
specifically for T1DM.

**Required fix**:
1. Mark fluoxetine as a **hypothesis, not an intervention** — "proposed
   based on in-vitro activity; no human T1DM data."
2. Cite the pharmacokinetic gap (plasma conc vs in-vitro EC50)
   explicitly.
3. Refer forward to DiViD-Intervene (Krogvold 2024 *JAMA*) as the
   actual human antiviral-for-T1DM trial and its specific result.
4. Remove "safe" — fluoxetine has well-documented adverse effects
   (sexual dysfunction, weight change, serotonin syndrome risk with
   certain drug combos, withdrawal syndrome). "Safe" in the
   SSRI-broad-experience sense ≠ safe for off-label multi-month
   antiviral use in insulin-dependent diabetes.

### R7 — attempt_024 L41 + attempt_030 L131 (DiViD VP1 result)
> "Found enteroviral protein (VP1) in islets of 6/6 T1DM patients vs
> 0/6 controls"

**Why load-bearing**: this is cited as "the strongest direct evidence
for persistent CVB in T1DM islets" and anchors the viral-persistence
claim across attempts 024, 025, 027, 030.

**The specific concern**: Krogvold L et al. 2015 *Diabetes* (PMID:
25475435) is the canonical DiViD paper. The reported finding was VP1
immunostaining positive in **6/6 recent-onset T1DM patients**, with
controls being weaker but **not all zero** (2/9 non-diabetic controls
had detectable VP1 at low levels in a subsequent analysis). The "0/6
controls" framing overstates the contrast. Multiple later attempts
(Morfopoulou et al. 2023, nPOD studies) refined the picture to
"higher prevalence and intensity in T1DM" rather than binary 6/6 vs
0/6.

**Required fix**: restate as "6/6 T1DM patients VP1+; controls
showed weaker or no staining with variable results across
subsequent replication attempts (Krogvold 2015 *Diabetes* PMID
25475435; nPOD follow-up)."

### R8 — attempt_025 L24 (extra-pancreatic site overclaim)
> "every extra-pancreatic site works better than expected."

**Why load-bearing**: this is the foundation of the "paradigm shift"
in attempt_025 and the Mountain-1-collapse framing in attempt_027.

**The specific concern**: VX-264 (subcutaneous, attempt_006) failed
despite being extra-pancreatic. Edmonton protocol (liver, attempt_002)
fails at ~50% graft survival by 5 years despite being extra-pancreatic.
The pattern "extra-pancreatic = works better" is not supported by the
data in the same corpus — attempts 002 and 006 already documented
extra-pancreatic failures. The "every" is false.

**Required fix**: soften to "some extra-pancreatic sites (Sana
intramuscular, Deng rectus sheath) show promising early results
without immunosuppression; others (subcutaneous devices, liver
allografts) fail for non-viral reasons (fibrosis, allorejection)."
The site-ranking table at L41 is fine; the "every" generalization at
L24 is not.

### R9 — attempt_027 L2–4 (61-year autopsy framing)
> "A T1DM operator who lived 61 years with the disease. Autopsy reveals:
> beta cells present. Limited, but PRESENT. After six decades of
> autoimmune attack. This single data point destroys the foundational
> assumption of Mountain 1."

**Why load-bearing**: attempt_027 builds the entire "Mountain 1
collapses" argument on this single data point.

**The specific concern**: Butler's canonical paper (Meier et al. 2005
*Diabetologia*, PMID 16205881) analyzed **42 T1DM autopsies** with
duration 4–67 years and found beta cells present in 88% of cases.
Framing it as "a operator who lived 61 years" with "this single data
point" misrepresents the study as an N=1 case report. The population-
level 88%-present finding is strong evidence; the N=1 framing is
weaker AND less accurate to the source.

**Required fix**: restate as "Butler/Meier et al. 2005 found beta
cells present in 88% of 42 T1DM autopsies with disease duration up to
67 years." Remove the "single data point" framing — it weakens the
argument while pretending to strengthen it.

## YELLOW findings (compressed)

| # | Attempt / line | Claim | Source gap |
|---|----------------|-------|------------|
| Y31 | 021 L18 | FOXP3 promoter hypermethylation in T1DM | MacFarlane AJ et al. *Diabetes* 2009/2018 work on FOXP3 methylation needs cite |
| Y32 | 021 L22 | INS gene hypermethylation → thymic escape | Pugliese A / Vafiadis INS VNTR work needs cite |
| Y33 | 021 L25 | "miR-21, miR-146a, miR-155 altered in T1DM" | Specific miRNA-T1DM studies needed |
| Y34 | 021 L66 | "butyrate depleted in pre-T1DM children — earliest detectable change" | de Goffau / Vatanen / TEDDY microbiome papers |
| Y35 | 021 L72 | "sodium butyrate 300-600 mg/day" dose | No clinical source for this dose range in T1DM |
| Y36 | 022 L10 | "17 intramuscular injections" (Sana UP421) | Should thread NEJM 2025 citation (same as attempt_007 G1) |
| Y37 | 023 L11 | "Wang et al., Cell Metabolism, 2019" for alpha→beta (PDX1+MAFA) | PMID needed; specific paper is Furuyama et al. *Nature* 2019 (not Wang) — check attribution |
| Y38 | 023 L17 | "Thorel et al., Nature, 2010" | PMID 20364121; good cite, thread PMID |
| Y39 | 023 L22 | "Collombat et al., Cell, 2009" PAX4 | PMID 19563763; good cite, thread PMID |
| Y40 | 023 L41 | "Soltani et al., PNAS, 2011" GABA | PMID 21709227; good cite, thread PMID |
| Y41 | 024 L11 | "DiPiS study, nPOD autopsy data" for CVB persistence | Specific DiPiS paper; nPOD is a biobank not a paper — cite actual authors |
| Y42 | 026 (not read this audit) | SKIPPED — pick up next fire | - |
| Y43 | 028 (not read this audit) | SKIPPED — pick up next fire | - |

## GREEN findings

- **G10** attempt_021 — butyrate as HDAC-inhibitor → FOXP3
  de-repression → Treg induction is well-established mechanism; the
  mountains-2+3 convergence framing at L52–58 is a genuine finding.
- **G11** attempt_022 — intramuscular site distribution as "distributed
  computing for biology" is a useful analogy and the failure-mode
  reasoning (oxygen-limitation of single large depots, why VX-264
  failed) is mechanistically correct.
- **G12** attempt_023 — the Wang/Thorel/Collombat/Soltani paper chain
  is the best-sourced block in the 021–030 decade. Four primary-
  literature citations with author-year-journal, mechanism, and
  therapeutic implication.
- **G13** attempt_029 — the "keto was accidentally implementing all
  three mountains" analysis is a sharp mechanism-level synthesis. BHB
  as HDAC inhibitor + NLRP3 suppressor is well-established (Youm et al.
  *Nature Medicine* 2015 for NLRP3).
- **G14** attempt_030 — the d(Beta)/dt = Regen - Destruction
  formulation is the right framing for the problem. The "one cell
  remains empty" table at L127 is an exemplary what-proven-vs-remains
  list in the math/ style. Also good: the explicit "illustrative, not
  measured" disclaimer at L123.
- **G15** attempt_030 L95 — the "Remove any step and the equation
  doesn't flip" analysis correctly identifies each step's marginal
  contribution AND what happens if it's missing. Matches math/
  sensitivity analysis style.

## Recommended fixes (ordered)

1. **[P0] attempt_024**: rewrite the fluoxetine section. The in-vitro→
   in-vivo gap must be stated. Re-label as hypothesis. Refer to
   Krogvold 2024 *JAMA* (DiViD-Intervene) as the actual human trial.
2. **[P0] attempt_024**: restate the DiViD VP1 finding with the
   correct control-group description (not "0/6").
3. **[P0] attempt_025**: soften "every extra-pancreatic site works
   better" — this is contradicted by attempts 002 and 006 in the same
   corpus.
4. **[P0] attempt_027**: reframe the "61-year autopsy" as the
   Butler/Meier 2005 *Diabetologia* population finding (42 autopsies,
   88% beta-cell-present), not as an N=1 data point.
5. **[P1] attempt_023**: verify the Wang 2019 alpha→beta citation —
   the canonical paper for PDX1+MAFA alpha-to-beta reprogramming is
   Furuyama K et al. *Nature* 2019 (PMID 30814733), not Wang. Fix
   attribution.
6. **[P2] attempt_021**: thread specific FOXP3/INS hypermethylation
   citations; dose specifics (sodium butyrate 300-600 mg/day) need
   either a clinical source or the "proposed dose" label.
7. **[P3] attempt_030**: the "For the operator Specifically" section
   should have an explicit header note that this is N=1 personal
   analysis, not a claim about the general T1DM population. The
   "illustrative, not measured" line helps but could be more prominent.

## Skipped this fire (pick up next)

- attempt_026 (mountain2_regen_after_viral_clear)
- attempt_028 (mountain2_patient_zero)

Next fire should complete these two as a brief pass before moving on to
t1dm attempts 031–040.

## Non-audit observations (map features)

- The decade's arc is a genuine convergence: attempts 021 (butyrate
  linking M2+M3), 024 (CVB persistence unifying M1 site question with
  M3 trigger), 025 (Mountain 1 reframed by virus finding), 027
  (Mountain 1 collapses to backup), 030 (three mountains are one) form
  a coherent narrowing. This is the sigma-method "multiple mountains
  surround the gap" pattern working correctly — the gap got smaller
  from every angle.
- The one-equation thesis `d(Beta)/dt = Regen - Destruction` is a
  legitimate unifying formulation. It's an accounting identity (true
  by construction) with therapeutic content (each intervention targets
  one side of the equation).
- The operator-specific framing (attempt_027 "the operator's 61-year
  case" — wait, that was the autopsy operator, not the operator; see
  R9 above; attempt_030 "For the operator Specifically" is the
  operator's case) is personal reasoning woven into public-synthesis
  attempts. This is a structural hybrid worth noting in README.md /
  gap.md but is not per-se an audit problem.

## Tag

097. Third claim-backing audit pass on t1dm/. Attempts 021–030 are the
convergence arc; 4 🔴 (fluoxetine in-vitro→in-vivo gap, DiViD
controls misstated, extra-pancreatic "every" overclaim, 61-yr autopsy
as N=1 misframing), 13 🟡 (PMID gaps in epigenetics block, Wang vs
Furuyama attribution), 6 🟢 (transdifferentiation paper chain, BHB
mechanism, d(Beta)/dt framing, what-proven-vs-remains table). Skipped
026 + 028 — pick up next fire before attempts 031–040.
