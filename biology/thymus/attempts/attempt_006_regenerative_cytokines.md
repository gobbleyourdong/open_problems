# attempt_006 — Regenerative Cytokines: IL-7, IL-22, and KGF

> Sixth attempt. attempt_005 covered the sex-hormone pathway to
> thymic regeneration. This attempt covers the cytokine
> pathways: IL-7, IL-22, and KGF (FGF7) all have documented
> regenerative effects on the thymus, all are clinically tested,
> and they target different cellular components (IL-7 on
> thymocytes; IL-22 and KGF on TECs). Combinations are likely the
> future. Key clinical translations: CYT107 (recombinant IL-7) in
> sepsis and HSCT; palifermin (recombinant KGF) for chemo-induced
> mucositis with thymic regeneration as off-label benefit; IL-22
> trials for graft-versus-host disease.

---

## Three pathways, three targets

The three "regenerative cytokines" with the most clinical evidence:

| Cytokine | Target cell | Mechanism | Clinical formulation |
|---|---|---|---|
| **IL-7** | Thymocytes (DN, DP) | Survival/proliferation via JAK-STAT | CYT107 (recombinant human IL-7) |
| **IL-22** | TECs (cTECs, mTECs) | Trophic; FOXN1 upregulation; STAT3 activation | F-652 (rIL-22-IgG2 fusion); recombinant IL-22 |
| **KGF (FGF7)** | TECs primarily, also other epithelial | TEC proliferation, differentiation | Palifermin (rhKGF) — Kepivance, FDA-approved |

These work synergistically: IL-22 and KGF rebuild the TEC niche;
IL-7 supports the thymocytes growing within it. Ideal regeneration
combines them.

---

## IL-7 — survival/proliferation factor for thymocytes

### The basic biology

- Source in thymus: cTECs primarily, also some mTECs and stromal
  fibroblasts (per attempt_003 chemistry section).
- Receptor: IL-7Rα (CD127) + common γ chain (CD132).
- Signaling: JAK1/JAK3 → STAT5 → induces Bcl-2 (anti-apoptotic) and
  drives cell cycle entry.
- Function: SURVIVAL signal for DN3 → DP → SP thymocytes throughout
  development.

IL-7 deficiency causes severe T cell lymphopenia. IL-7Rα null
humans have SCID. IL-7 is non-redundant for T cell development.

### CYT107: recombinant human IL-7

CYT107 is a glycosylated recombinant human IL-7 manufactured by
Revimmune (formerly Cytheris). It has been administered to >390
patients across multiple trials for various indications.

### IL-7 in sepsis: the IRIS-7 trial

**Francois B et al. (2018).** "Interleukin-7 restores lymphocytes in
septic shock: the IRIS-7 randomized clinical trial." *JCI Insight*
3(5):e98960. PMID 29515037.

Design: prospective, randomized, double-blind, placebo-controlled
trial in patients with septic shock and severe lymphopenia.
27 patients at academic sites in France + US. CYT107 vs placebo
for 4 weeks.

Findings:
- CYT107 well tolerated; no cytokine storm, no organ dysfunction
  worsening
- **3- to 4-fold increase** in circulating CD4 and CD8 T cells
- Induced T cell proliferation and activation markers
- No significant change in mortality (small N for that endpoint)

This established CYT107's safety and on-target T cell expansion
effect in critically ill patients.

### IL-7 in HIV

CYT107 in HIV patients with persistent lymphopenia despite optimal
antiretroviral therapy:
- 2- to 4-fold dose-dependent increase in CD4 and CD8 T cells
- TREC content increased (suggesting some thymic component)
- Effect persists for months after dosing

Reference: **Sereti I et al. (2009).** "IL-7 administration drives
T cell-cycle entry and expansion in HIV-1 infection." *Blood*
113:6304-6314.

### IL-7 in HSCT (post-transplant T cell recovery)

**Perales MA et al. (2012).** "Recombinant human interleukin-7
(CYT107) promotes T-cell recovery after allogeneic stem cell
transplantation." *Blood* 120:4882-4891.

Patients post-allogeneic HSCT given CYT107:
- Faster recovery of CD4 and CD8 T cell numbers
- Some TREC recovery (thymic-output recovery indicator)
- No increase in graft-versus-host disease
- Reduced infections in some cohorts

This is one of the closest "thymic regeneration" indications: T cell
reconstitution after transplant is a major clinical problem, and
CYT107 demonstrably accelerates it.

### IL-7's mechanism on the thymus specifically

A subtlety: IL-7 acts on EXISTING thymocytes (and peripheral T cells).
It does NOT directly regenerate the TEC niche. So IL-7 expands what
the thymus can produce IF the niche is intact, but does not fix the
underlying TEC loss in age-related involution.

This is why IL-7 alone is not the full answer for elderly thymic
regeneration. It needs to be combined with TEC-trophic factors
(IL-22, KGF) — which is the rationale for combination protocols.

---

## IL-22 — TEC trophic factor (Dudakov / van den Brink work)

### Discovery

A breakthrough paper:

**Dudakov JA, Hanash AM, Jenq RR, Young LF, Ghosh A, Singer NV,
West ML, Smith OM, Holland AM, Tsai JJ, Boyd RL, van den Brink MR
(2012).** "Interleukin-22 drives endogenous thymic regeneration in
mice." *Science* 336:91-95. PMID 22383805.

What they found:
- After thymic damage (irradiation, chemo, GVHD), endogenous IL-22
  drives TEC recovery
- Source of intrathymic IL-22: group 3 innate lymphoid cells (ILC3s)
- IL-22 acts directly on TEC stroma via IL-22R + IL-10R2
- Augments FOXN1 expression
- Activates JAK/STAT/Mcl-1 pathway → TEC survival and expansion

### Mechanism

```
Thymic damage (radiation, chemo, GVHD)
        ↓
Death of DP thymocytes
        ↓
ILC3 sense damage signals → produce IL-22
        ↓
IL-22 binds IL-22R + IL-10R2 on TECs
        ↓
JAK1/STAT3 activation
        ↓
FOXN1 upregulation, Mcl-1 induction
        ↓
TEC survival + proliferation
        ↓
Recovered niche → DP thymocyte regeneration
```

### IL-22 in GVHD

Graft-versus-host disease (GVHD) destroys ILC3s in addition to its
other damage:

**Dudakov JA et al. (2017).** "Loss of thymic innate lymphoid cells
leads to impaired thymopoiesis in experimental graft-versus-host
disease." *Blood* 130:933-942. PMID 28607133.

Findings:
- Alloreactive T cells eliminate thymic ILC3s in GVHD
- Loss of ILC3s = loss of intrathymic IL-22
- Loss of IL-22 = loss of TEC protection
- Recombinant IL-22 administration POST-BMT reverses thymic damage

This is the rationale for IL-22-based therapies in HSCT recipients.

### Clinical formulations and trials

- **F-652**: an IL-22-Fc fusion protein (longer half-life than
  recombinant IL-22). Tested in alcoholic hepatitis and GVHD trials.
- **Recombinant IL-22**: tested in early-phase trials for various
  inflammatory and tissue-damage conditions.

Status: still investigational. No FDA-approved IL-22 product yet.
Most relevant to thymic biology: Phase 1/2 trials in HSCT recipients
for T cell reconstitution.

### IL-22 vs IL-7: complementary

Note the complementarity:
- IL-22 fixes the TEC niche
- IL-7 fixes thymocyte support

Combined IL-22 + IL-7 should work better than either alone. Some
preclinical studies confirm; clinical combinations are emerging.

---

## KGF (FGF7) — TEC trophic factor with FDA-approved formulation

### The basic biology

- Source in thymus: stromal mesenchymal cells.
- Target: thymic epithelial cells (cTECs and mTECs).
- Receptor: FGFR2-IIIb.
- Function: TEC proliferation and survival.

KGF was characterized for thymic effects in:

**Min D et al. (2002).** "Sustained thymopoiesis and improvement in
functional immunity induced by exogenous KGF administration in
murine models of aging." *Blood* 99:4592-4600. PMID 12036893.

Findings:
- Aged mice given recombinant KGF showed sustained thymopoiesis
- Increased peripheral T cell numbers and TREC content
- Effect persisted weeks after dosing

### Palifermin: clinical KGF

**Palifermin (Kepivance)** is recombinant human KGF, FDA-approved
for chemotherapy-induced oral mucositis (since 2004).

- Dose: 60 µg/kg IV daily for 3 days before chemo + 3 days after
- Indication: hematopoietic SCT recipients receiving high-dose
  conditioning
- On-label benefit: reduced oral mucositis severity and duration
- Off-label / observed: improved thymic recovery in some studies

### KGF for thymic regeneration in HSCT

**Coles AJ et al. (2012).** "Keratinocyte growth factor impairs
human thymic recovery from lymphopenia." Hmm — the picture is
mixed in human trials. Some trials show KGF benefits T cell
recovery; others show null or even negative results, possibly due
to dose, timing, or population differences.

The MOUSE evidence for KGF as a thymic regenerator is strong; the
human evidence is less definitive than for IL-7. KGF's main
clinical use remains mucositis prevention.

### Why mouse-to-human translation is incomplete

Several possible reasons:
- KGF dose/timing in HSCT trials may not be optimal for thymic
  endpoint
- Thymic damage in HSCT is more severe than mouse aging models;
  more than KGF alone is needed
- Human TEC FGFR2-IIIb expression and downstream signaling may
  differ from mouse

Combination KGF + IL-7 or KGF + sex hormone blockade might bridge
this. Active investigation.

---

## BMP4 — early-life thymic factor (less relevant clinically)

BMP4 (mentioned in attempt_003 chemistry) is critical for thymic
organogenesis and TEC FOXN1 induction during embryogenesis. In
adults, BMP4-based interventions are largely experimental
(organoid construction, attempt_010). Not yet a clinical
regeneration tool.

---

## Combination protocols

The clear next step in clinical thymic regeneration: combinations
that target multiple pathways simultaneously:

1. **LHRH analog + IL-7 + KGF**: sex hormone removal + thymocyte
   support + TEC support. Theoretically should outperform any
   single intervention.
2. **CYT107 + palifermin**: tested in HSCT in some trials with
   modest additive benefit.
3. **IL-22 + IL-7**: emerging interest for HSCT and post-cytotoxic
   regeneration.
4. **TRIIM (attempt_010) growth hormone + DHEA + metformin**:
   different mechanism cluster (metabolic + hormonal); not directly
   IL-7/22/KGF but achieved measurable thymic regeneration in
   clinical trial.

The optimal combination, dose, and timing remain open clinical
questions. The TRIIM-X Phase 2 trial is ongoing at this writing
and may inform.

---

## What we can say about adult thymic regeneration via cytokines

Honest summary:

- **IL-7 (CYT107) clinical efficacy**: documented in sepsis, HIV,
  HSCT — modest but real. Increases peripheral T cells; partial
  effect on TRECs.
- **IL-22 clinical efficacy**: emerging from GVHD trials; promising
  in preclinical; clinical-grade IL-22 still not FDA-approved.
- **KGF (palifermin) clinical efficacy**: FDA-approved for
  mucositis. Thymic regeneration effect observed in mice; human
  data mixed.
- **None alone is a complete adult thymic regeneration strategy**.
  Combinations look more promising than any single agent.

---

## Open at this stage

- **Optimal IL-7 dose / schedule** for thymic-specific (vs
  peripheral T-cell) effect
- **IL-22 effects in elderly humans** (not just HSCT recipients):
  most data are from severely lymphodepleted populations
- **KGF combinations**: KGF + LHRH + IL-7 should be tested
  systematically
- **Long-term immune effects** of any cytokine-based regeneration:
  do regenerated cells have proper central tolerance? (Cross-
  reference attempt_002's caveat about regeneration without
  AIRE/mTEC restoration risk.)

## Status

Cytokine pathways covered. attempt_007 dives deep into FOXN1 as
master regulator (Bredenkamp/Blackburn forced-expression work).

## Key sources

Primary:
- **Min D et al. 2002 *Blood* 99:4592** (KGF for aged mouse
  thymopoiesis). PMID 12036893.
- **Sereti I et al. 2009 *Blood* 113:6304** (IL-7 in HIV).
- **Dudakov JA et al. 2012 *Science* 336:91** (IL-22 drives
  endogenous thymic regeneration). PMID 22383805. **Landmark.**
- **Perales MA et al. 2012 *Blood* 120:4882** (CYT107 promotes
  T-cell recovery post-HSCT).
- **Dudakov JA et al. 2017 *Blood* 130:933** (loss of thymic ILC3s
  → impaired thymopoiesis in GVHD). PMID 28607133.
- **Francois B et al. 2018 *JCI Insight* 3:e98960** (IRIS-7 sepsis
  trial). PMID 29515037.

Reviews:
- Velardi E, Tsai JJ, van den Brink MRM 2021 *Nat Rev Immunol*
  21:277 (T cell regeneration after immunological injury).

---

## Gap opened

- Combination cytokine + sex hormone blockade trials in elderly
  (not just transplant) populations
- IL-22 long-term safety and durability profile in human aging
  context
- Tissue-specific / TEC-specific delivery of these cytokines to
  reduce off-target effects

## Status

Complete. attempt_007 (FOXN1 master regulator + Blackburn forced
expression) is next.

---

*Filed: 2026-04-15 | biology/thymus/attempts/attempt_006*
*Follows: attempts 001-005.*
