# Attempt 122 — Claim-Backing Audit: biology/evolution/results/therapeutic_convergence.md

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue, Fire 50)
**Scope**: biology/evolution/results/therapeutic_convergence.md (358L,
full read). Third synthesis-note audit.
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: Fires 48 (taxonomy 411L) + 49 (host_coevolution 378L) —
both showed parallel structural discipline. Expecting similar here.

## Executive verdict

**Therapeutic-convergence synthesis is the framework's clinically
sharpest output.** 7 drug/class sections (doxycycline 40mg, ivermectin,
metronidazole, NLRP3 suppressors, anti-cytokine biologics, anti-CD20,
omega-3) each with mechanism + cross-disease-application table. The
core claim — "treat the substrate, not each organism" — converts the
7-class taxonomy into a clinical-decision framework.

**This file's status-list is LESS STALE** than taxonomy.md / host_
coevolution.md. L340-352 marks items 1, 2, 3 as ✅ DONE (taxonomy,
host-coevolution, this note) while items 4, 5, 6 are ⏳ pending.
In fact all 6 items now done (modernity_trajectory.md 347L +
class_boundary_cases.md 360L + attempt_001 addendum all exist).
So **still partially stale**, but chronologically written later than
the other two synthesis notes — visible evolution of status-list
accuracy as the series progressed.

**Strongest single finding**: the doxycycline 40mg case (L43-87)
is the **cleanest cross-class therapeutic-convergence pattern** in
the entire non-math corpus — same drug, same mechanism (MMP-9
inhibition), 4 disease contexts across classes 6 (P. gingivalis
periodontitis) + 7 (Demodex rosacea/blepharitis, Malassezia/C. acnes
ecosystem MGD). Each FDA approval date + specific dose traced: Oracea
2006 40mg/day + Periostat 1998 20mg BID.

**🔴 RED count**: 0
**🟡 YELLOW count**: 6
**🟢 GREEN count**: 13

## YELLOW findings

| # | Location | Claim | Source gap |
|---|----------|-------|------------|
| Y285 | L115-118 "Ivermectin also shows... Coxsackievirus (Benkahla 2018 CV-B4 in vitro and mouse model; fluoxetine is a stronger-effect analog)" | Citation ambiguity | **Benkahla 2018 is about fluoxetine against CVB, not ivermectin.** The parenthetical "fluoxetine is a stronger-effect analog" likely means the author is conceding ivermectin is weak; but the Benkahla 2018 citation is mis-attached to ivermectin. Clarify: ivermectin antiviral activity is documented (Yang 2020 PMID 32251768 for SARS-CoV-2) but not for CVB via Benkahla. |
| Y286 | L340-352 "Status" section marks items 4-6 still ⏳ pending | Stale list | All 4 remaining (modernity_trajectory.md + class_boundary_cases.md + attempt_001 addendum) now DONE; only less stale than taxonomy/host_coevolution because L340-342 did mark items 1-3 ✅ DONE. Bulk-update. |
| Y287 | L169 "COLCOT trial showed post-MI CVD benefit" | PMID | Tardif et al. 2019 NEJM PMID 31733140 (colchicine post-MI CVD reduction). Thread. |
| Y288 | L180-182 "CANTOS trial showed major CVD benefit from IL-1β blockade" | PMID | Ridker et al. 2017 NEJM PMID 28845751 (canakinumab vs placebo post-MI CVD). Thread. |
| Y289 | L184-186 "MCC950 (investigational)... Preclinical promise; trials in multiple indications" | Current status | **MCC950 (CP-456773) clinical development was halted in 2016 for liver toxicity** — currently only preclinical use + structurally related compounds (e.g., NP3-146, ZYIL1) in development. Update "trials in multiple indications" to reflect halted status. |
| Y290 | L237-240 "Anti-CD20 for MS = targeted persistent-organism-reservoir therapy" | Mechanism claim | Reframing ocrelizumab MS efficacy as "targeting EBV reservoir" is a reasonable hypothesis (memory B cells carry EBV episomes), but clinical efficacy predates EBV causation proof (2017 approval vs 2022 Bjornevik) — suggests reframing is post-hoc rationalization not causal-mechanism evidence. Acknowledge the reframing is a hypothesis, not established mechanism. |

## GREEN findings

- **G392** **7 drug/class sections with per-drug structure**:
  doxycycline 40mg → ivermectin → metronidazole → NLRP3 suppressors
  → anti-cytokine biologics → anti-CD20 → omega-3. Each with
  mechanism + cross-disease table + framework interpretation.
- **G393** **Doxycycline 40mg cross-class table** (L62-68): 5
  diseases × class × dose × role × source. Each row has specific
  dose (40 mg/day typically, 20-40 mg/day for Periostat) + FDA
  approval date (Oracea 2006, Periostat 1998) + cross-reference
  to per-organism attempt file. **Math-standard specificity**.
- **G394** **"Same drug, same mechanism, 4 disease contexts"
  (L70-77)** — cross-class unification claim explicitly names
  what is shared (MMP-9 inhibition, neutrophil ROS, tissue
  destruction) vs what differs (organism biology upstream).
  Mechanism-level precision.
- **G395** **Patient-clinical-synthesis observation** L84-87:
  "patients with periodontitis + rosacea + blepharitis (a common
  clinical trio... see `medical/blepharitis/results/cross_directory_
  drift.md`) can be treated with a single sub-antimicrobial
  doxycycline regimen that addresses all three simultaneously."
  Operationally useful clinical finding traceable to specific
  repo cross-ref.
- **G396** **Ivermectin triple-mechanism labeling** (L93-103):
  GABA-Cl channel agonist (arthropods) + importin α/β-1 nuclear
  transport inhibitor (NF-κB suppression) + additional unknown
  mechanisms. Multi-MOA honest framing.
- **G397** **Metronidazole bridge-function** L149-154: "clearest
  bridge between class-7 disease (Demodex rosacea) and class-6
  disease (periodontitis, H. pylori)... at antibacterial doses,
  so resistance + microbiome side effects apply (unlike sub-
  antimicrobial doxy)." Comparative precision between two bridge
  drugs.
- **G398** **NLRP3 4-drug catalog** (L164-186): colchicine (micro-
  tubule → IKK → NF-κB), BHB (direct NLRP3 + HDAC), IL-1β biologics
  (canakinumab, anakinra), MCC950 (direct NLRP3). Per-drug
  mechanism-level treatment.
- **G399** **Anti-cytokine biologic table** (L204-210) — 5 drug
  classes × targets × specific drug-name brands × per-class
  disease indications spanning persistent-organism framework.
  Real-world "which biologic works for which set of diseases"
  decision support.
- **G400** **Anti-CD20 + EBV-reservoir reframing** (L237-246) —
  speculative but clearly labeled as "reframing via EBV causation";
  uses the Bjornevik 2022 causation proof to offer mechanistic
  hypothesis for existing anti-CD20 efficacy data across MS,
  Sjögren's, lupus. Not presented as established — "may be partly
  targeting EBV reservoirs".
- **G401** **Core framework prediction** L279-282: "Persistent-
  organism diseases share a downstream inflammatory substrate.
  Treatment targeting the substrate works across diseases. Treatment
  targeting a specific organism works only for that disease."
  **Two-sentence therapeutic-convergence thesis** — framework
  compressible to a single pair of sentences.
- **G402** **Drug-discovery-priority implication** L302-306:
  "developing better MMP-9 / NLRP3 / IL-6 targeting agents has
  disproportionately high cross-class return. A new NLRP3
  inhibitor that beats MCC950 could benefit rosacea + periodontitis
  + T1DM + atherosclerosis + CAPS + gout simultaneously." **Kill-
  ROI at pharmacology level** — names specific research targets.
- **G403** **Framework-linked predictions** (L293-306): biomarker-
  driven therapy, combination-therapy logic two-phase architecture,
  drug-discovery priority. Each ties back to a framework element
  (host_coevolution common hubs → substrate-targeting; two-phase
  architecture → per-organism-clearance + substrate-targeting).
- **G404** **Open question #4** L324-328: "Is there a theoretical
  upper bound to cross-class therapeutic convergence? Maybe — the
  more specific a therapeutic target (organism-specific clearance),
  the less cross-class utility. At the substrate level (MMP-9,
  NLRP3), maximum cross-class." **Framework-self-limiting
  observation**: the convergence isn't universal; it's graded by
  drug-target specificity.

## Recommended fixes (ordered)

1. **[P1]** Y285 — clarify ivermectin-CVB citation. Benkahla 2018
   is about fluoxetine not ivermectin. Replace with Yang 2020 PMID
   32251768 if citing ivermectin SARS-CoV-2 antiviral, or remove
   the CVB-specific claim for ivermectin.
2. **[P2]** Y289 — update MCC950 status. Clinical development was
   halted 2016 for hepatotoxicity; structural analogs still in
   development. "Trials in multiple indications" is stale.
3. **[P2]** Thread PMIDs for COLCOT (Y287, Tardif 2019 NEJM PMID
   31733140) + CANTOS (Y288, Ridker 2017 NEJM PMID 28845751).
4. **[P2]** Y286 — bulk-update all 3 synthesis-note status lists
   together (taxonomy L381-402, host_coevolution L357-372,
   therapeutic_convergence L340-352). All mark varying numbers of
   items remaining; all items now done.
5. **[P3]** Y290 — acknowledge anti-CD20/EBV-reservoir as hypothesis
   not mechanism.

## Non-audit observations

- **Doxycycline 40mg case (L43-87) is arguably the single most
  operationally useful synthesis in the non-math corpus.** It
  identifies a specific drug, specific dose, specific mechanism,
  specific 4-disease indication list, specific patient population
  (periodontitis + rosacea + blepharitis clinical trio), with
  FDA approval dates. A rheumatologist, dermatologist, or dentist
  could read this section and immediately apply it.
- **Three sequential synthesis files** (taxonomy → host_coevolution →
  therapeutic_convergence) **form a coherent trilogy**: taxonomy
  = organism-side structure; host_coevolution = host-side substrate;
  therapeutic_convergence = clinical application. Each ~358-411
  lines; each with parallel structure (VERIFICATION STATUS → main
  content → predictions → open questions → status). Framework
  engineering at the synthesis-note level.
- **The status-list staleness pattern across all 3 synthesis notes**
  is a bulk-update candidate. All 3 lists mark themselves as DONE
  but mark other synthesis files as pending. Each was written in
  isolation; none was updated when others completed. Batch fix:
  mark all 5 synthesis files + attempt_001 addendum as ✅ in all
  3 status lists simultaneously.
- **The 7 drug/class sections are unevenly backed**: doxycycline
  40mg has specific dose + FDA dates + cross-ref; ivermectin has
  specific formulations (Soolantra 2014, Stromectol oral) + doses;
  metronidazole has clinical-use table; NLRP3 section has 4
  drugs with mechanism. Lower-depth: anti-CD20 section has
  4 drugs but no doses/brands beyond names; omega-3 has use-table
  but no dose/EPA+DHA ratio recommendations. A future pass could
  standardize drug-depth.
- **Anti-CD20/EBV hypothesis (G400)** is the most speculative claim
  in the file but honestly labeled. Prior anti-CD20 efficacy data
  (2017 approval) exists; EBV causation (Bjornevik 2022) exists
  independently; the combination as mechanism is **untested**. The
  "may be partly" language matches confirmation-bias-audit
  compliance — hypothesis presented as hypothesis.

## Tag

122 (biology/evolution/results/therapeutic_convergence.md). 358L
full read. **0 🔴**. 6 🟡: ivermectin-CVB Benkahla-2018 citation
ambiguity (Benkahla 2018 is about fluoxetine not ivermectin —
cleanest substantive fix); status-list partial staleness (items
1-3 marked ✅ but items 4-6 pending when all done); COLCOT/CANTOS
PMIDs (Tardif 2019 PMID 31733140, Ridker 2017 PMID 28845751);
MCC950 clinical-development-halted-2016 status update needed;
anti-CD20/EBV-reservoir reframing as hypothesis. **13 🟢**:
**doxycycline 40mg cross-class table with Oracea 2006 + Periostat
1998 FDA dates + specific doses + 4 disease contexts** = single
most operationally useful synthesis in non-math corpus; ivermectin
triple-MOA honest labeling; metronidazole bridge-function between
classes 6+7 with comparative antibacterial-dose vs sub-antimicrobial-
doxy discussion; NLRP3 4-drug catalog (colchicine, BHB, IL-1β
biologics, MCC950); anti-cytokine biologic 5-drug-class table with
per-class disease indications; anti-CD20/EBV reframing honestly
labeled as hypothesis; **two-sentence therapeutic-convergence
thesis** ("treat the substrate, not each organism"); drug-discovery-
priority kill-ROI (MMP-9/NLRP3/IL-6 cross-class return); framework-
linked predictions; **framework-self-limiting observation** (convergence
is graded by drug-target specificity); cross-reference to `medical/
blepharitis/results/cross_directory_drift.md` for periodontitis+
rosacea+blepharitis patient trio; combination-therapy-logic two-
phase-architecture consistency with medical/persistent_organisms/
PROBLEM.md; operationally-useful clinical synthesis. **Observation**:
Fires 48+49+50 complete the **synthesis trilogy** (taxonomy +
host_coevolution + therapeutic_convergence = organism-side + host-
side + clinical-application, 411+378+358=1147L). All 3 have parallel
status-list staleness — bulk-update recommended. Doxycycline 40mg
case is the framework's clinical-deliverable. Next fire: `modernity
_trajectory.md` (347L) + `class_boundary_cases.md` (360L) =
remaining 2 synthesis notes, OR 5 `audit_100series_round{1..5}.md`
files (1097L prior audit methodology), dysbiosis numerics, WHM sweep
(pending op), or loop termination.
