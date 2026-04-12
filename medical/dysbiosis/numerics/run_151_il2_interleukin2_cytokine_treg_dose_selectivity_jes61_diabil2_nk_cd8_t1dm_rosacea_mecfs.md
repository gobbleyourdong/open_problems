# Run 151 — IL-2 / Interleukin-2 Cytokine: Dose-Selective Treg Expansion, Receptor Affinity Hierarchy, JES6-1 Complexes, DIABIL-2 Trial, NK Dysfunction

**Date:** 2026-04-12
**Sweep:** 49
**Candidate:** IL-2 (interleukin-2) cytokine — protein itself, production control, dose-selectivity pharmacology

## Kill-First Verification

**Grep confirmation:**
- run_140 (IL2RA/CD25/JAK3/STAT5): receptor-side analysis only; IL-2 cytokine biology (production, dose-selectivity, complex engineering) = 0 coverage
- IL-2 appears in 40+ files as passing context (Treg homeostasis, low-dose IL-2, DIABIL-2 mentions) — no file with IL-2 *cytokine* as primary subject
- Distinct from run_140 (receptor signaling): run_140 = what happens after IL-2 binds CD25; this run = the cytokine itself — its production, affinity hierarchy, pharmacological engineering

**Kill verdict:** PASS — IL-2 cytokine biology has zero dedicated analysis.

## Saturation Override Criteria

1. **Absent from prior runs as primary subject**: YES — 0 of 150 runs address IL-2 cytokine production/dose-selectivity/complex engineering
2. **MODERATE+ rosacea + T1DM**: YES — HIGH T1DM (direct therapeutic); MODERATE rosacea (Treg/Th17 balance)
3. **New therapeutic target**: YES — aldesleukin (recombinant IL-2), IL-2/JES6-1 complexes, ultra-low-dose regimens
4. **Kill-first fails**: CONFIRMED — run_140 covers receptor side; cytokine side is genuinely absent

**All four criteria met. Proceeding.**

---

## Core Mechanism

### IL-2 Gene Production and Control

IL-2 is a 15.5 kDa four-helix bundle cytokine produced almost exclusively by **activated CD4⁺ T cells** (naive → Th0 activation) and to lesser extent by CD8⁺ T cells, NK cells, and dendritic cells under antigen stimulation.

**Transcriptional control (IL2 gene, chromosome 4q26-27):**
- TCR ligation → ZAP-70 → PLCγ1 → DAG → PKCθ → AP-1 (c-Fos/c-Jun) + Ca²⁺/calcineurin → NFAT1/NFAT2 nuclear translocation
- AP-1 + NFAT cooperate at the IL-2 promoter ARRE1/ARRE2 elements → IL-2 transcription burst within 30 min of TCR activation
- CD28 co-stimulation: CD28 → PI3K/Akt → PKCθ activation → NF-κB + AP-1 → IL-2 amplification ~10-100×; CD28 signal is the principal IL-2 amplifier
- **CTLA4 competition (run_148)**: CTLA4 outcompetes CD28 for CD80/CD86 (10× higher affinity) → CD28 signal lost → IL-2 transcription collapses; Tregs use CTLA4 trogocytosis to indirectly suppress IL-2 production in effector T cells
- mRNA instability: IL-2 mRNA half-life ~30 min (AU-rich element in 3'UTR → TTP-mediated degradation); IL-2 is a burst cytokine, not constitutive

**Post-transcriptional control:**
- 3'UTR AU-rich elements → tristetraprolin (TTP/ZFP36) → rapid mRNA decay → IL-2 signal is inherently transient
- Cyclosporin A / tacrolimus: calcineurin inhibitors → NFAT nuclear entry blocked → IL-2 production dramatically suppressed

---

## Receptor Affinity Hierarchy and Dose-Selectivity

This is the pharmacological core of low-dose IL-2 immunotherapy.

### Three Receptor Complexes (Kd hierarchy)

| Receptor | Chains | Kd | Cell Types | Signal |
|----------|--------|----|-----------|--------|
| **Trimeric IL-2Rαβγ** (high-affinity) | CD25 (IL-2Rα) + CD122 (IL-2Rβ) + CD132 (γc) | ~10 pM | Tregs (constitutive CD25), activated T cells | JAK1/JAK3 → STAT5 (run_140) |
| **Dimeric IL-2Rβγ** (intermediate) | CD122 + CD132 (no CD25) | ~1 nM | NK cells, CD8⁺ T cells, memory T cells | JAK1/JAK3 → STAT5 |
| **Monomeric IL-2Rα** (no signal) | CD25 only | ~10 nM | Trans-presentation | Binding/presentation only |

**Dose-selectivity principle:**
- At ultra-low IL-2 concentrations (<10 pM in vivo): only trimeric IL-2Rαβγ (10 pM Kd) is occupied → **Treg-selective expansion**
- At higher concentrations (>1 nM): dimeric IL-2Rβγ (NK/CD8) also engaged → effector activation, capillary leak, VLS (vascular leak syndrome)
- Clinical window for Treg-selective expansion: 0.33-1 × 10⁶ IU/m² (vs 5-20 × 10⁶ IU/m² anti-tumor dosing, which triggers VLS)
- Tregs constitutively express CD25 → always at high-affinity state; naive T cells require activation to upregulate CD25

**STAT5 pulsing kinetics:**
- Trimeric signaling: prolonged STAT5 phosphorylation (30-120 min) → FOXP3 transcription sustained → Treg survival/expansion
- Dimeric signaling: more transient STAT5 pulsing → NK cytotoxicity activation

---

## IL-2/Antibody Complexes (JES6-1 and Analogs)

### The Problem with Naked IL-2
IL-2 half-life in vivo: ~8-10 minutes (rapid renal clearance + receptor internalization). Ultra-low-dose dosing is technically difficult; toxicity window is narrow.

### IL-2/JES6-1 Complex Engineering

**JES6-1** is a murine anti-IL-2 monoclonal antibody (human analog: F5111.2 / NKTR-358 concept) that binds IL-2 at a site overlapping with **IL-2Rβ binding epitope** but NOT the IL-2Rα (CD25) binding site:

- JES6-1 blocks IL-2 binding to IL-2Rβγ (dimeric, intermediate-affinity receptor on NK/CD8)
- Leaves IL-2Rα (CD25) binding epitope fully exposed → complex can still engage trimeric IL-2Rαβγ on Tregs
- Net effect: **CD25-directed delivery** → Treg-selective; NK and CD8 cells cannot respond
- IL-2/JES6-1 complexes: 10× longer half-life than naked IL-2 + complete Treg selectivity
- Preclinical NOD mice: IL-2/JES6-1 complexes → ~3-5× Treg expansion → 30-50% insulitis reduction

**Human analogs under development:**
- **NKTR-358** (Nektar): IL-2 conjugated with 6-arm PEG at IL-2Rβ-blocking position → CD25-biased IL-2; Phase 2 for systemic lupus (SOL-UTION trial)
- **RG7461** (Roche/Genentech): IL-2/JES6-1 human antibody approach
- **LY3471851** (Eli Lilly): IL-2Rβ-blocking antibody-IL-2 fusion

---

## T1DM — DIABIL-2 Trial and Clinical Data

### DIABIL-2 (Hartemann et al., 2013, Lancet Diabetes & Endocrinology)

**Design:** Phase 1/2 dose-escalation; established T1DM (<5 years); ultra-low-dose aldesleukin (recombinant human IL-2)
**Dosing:** 1 × 10⁶ IU/m²/day × 5 days → maintenance × 5 months
**Primary finding:**
- Selective CD25hi Treg expansion (Foxp3⁺) — no NK/CD8 activation at this dose
- CD4⁺CD25hiCD127low Tregs: +40-50% expansion sustained during maintenance
- β cell function (C-peptide): stable/preserved in treated patients vs decline in controls
- No vascular leak syndrome, no autoimmune exacerbation at ultra-low dose

**TrialNet context (run_140 receptor side + this run cytokine side):**
- Combined: run_140 covers why IL-2 signal works (JAK3/STAT5/FOXP3 upregulation); this run covers the pharmacological engineering to achieve Treg-selectivity
- Abatacept (run_148) + low-dose IL-2: orthogonal synergy — IL-2 = more Tregs (numerical expansion via trimeric receptor); abatacept = more effective per Treg (trogocytosis preserved)

### IL-2 as Treg Autocrine Survival Factor

Tregs are **IL-2 consumers**, not producers — they express CD25 constitutively but do not produce IL-2 themselves (FOXP3 binds and represses the IL-2 promoter directly). Tregs depend entirely on **paracrine IL-2** from CD4⁺ effector T cells nearby:
- Inflammatory microenvironment: effector T cells produce IL-2 → fuels local Treg survival/expansion
- Islet insulitis: as autoimmune destruction proceeds, effector T cells become exhausted → IL-2 production collapses → Tregs starve → Treg pool shrinks exactly when needed most
- IL-2 supplementation rationale: rescue Treg pool from starvation at the moment of collapse

**FOXP3 repression of IL-2 promoter:**
- FOXP3 → binds NFAT → sequesters NFAT from IL-2 promoter → Tregs cannot produce IL-2; self-limiting: Tregs competitively consume IL-2 without producing it → "sink" model

---

## Rosacea — Treg Expansion and Th17 Suppression

**MODERATE relevance:**
- Skin Treg:Th17 ratio determines rosacea inflammatory set point; low-dose IL-2 → skin Treg expansion → Th17 suppression → LL-37/IL-17/TNF-α reduction
- Rosacea skin: IL-2Rα (CD25) expression on skin-resident Tregs; low-dose IL-2 can expand skin Tregs specifically
- TGF-β (run_150) + low-dose IL-2: TGF-β/SMAD3 → CNS1 FOXP3 induction; IL-2 → CD25/JAK3/STAT5 (run_140) → Treg survival; combination = induction + survival
- **IL-2/CTLA4-Ig synergy (runs 148+140+151 triad)**: abatacept preserves CD80/CD86 trogocytosis capacity; low-dose IL-2 numerically expands Treg pool; TGF-β induces new iTregs from naive T cells — three orthogonal Treg-restoration strategies

**Rosacea NK axis:**
- NK cells in rosacea: IL-2 at higher doses activates NK via dimeric IL-2Rβγ; ultra-low-dose Treg protocol keeps NK quiescent while expanding Tregs
- TGF-β (run_150) already suppresses NK NKG2D — low-dose IL-2 adds Treg expansion without NK reactivation at therapeutic doses

---

## ME/CFS — IL-2 Deficiency and NK Dysfunction

**MODERATE relevance:**
- NK cells express dimeric IL-2Rβγ; normal physiological IL-2 → NK priming; in ME/CFS, reduced IL-2 availability (exhausted CD4⁺ T cells) → NK cytotoxicity further impaired
- ME/CFS paradox: IL-2 increases NK number (via IL-2Rβγ dimeric) but also expands Tregs (trimeric); therapeutic goal = NK restoration without excess Treg induction → dosing nuance
- Low-dose IL-2 (Treg-selective): ME/CFS with autoimmune features → appropriate; ME/CFS without autoimmunity → NK deficiency is primary → intermediate dosing may be needed
- IL-2 + NK axis: run_102 (NKG2D/NKG2DL) + run_150 (TGF-β suppression) + run_151 (IL-2 deficiency) = three converging NK suppression mechanisms in ME/CFS

---

## Protocol Additions

### T1DM Treg Restoration (High Priority)

**Ultra-low-dose aldesleukin (recombinant IL-2):**
- Dose: 0.33-1 × 10⁶ IU/m²/day × 5 days induction, then maintenance
- Target: CD4⁺CD25hiCD127low Treg expansion (flow cytometry monitoring)
- Contraindication: avoid if active infection, VLS history, cardiac disease
- Monitor: CBC differential (Treg/Tregs count), creatinine, BP for VLS signs

**IL-2/anti-IL-2 complex formulations (investigational):**
- NKTR-358 / LY3471851 / RG7461 in trials; mechanistically superior to naked IL-2 (Treg-selectivity, longer half-life)
- Consider trial enrollment for T1DM patients not achieving immune control with standard agents

**Combination protocol (three-arm Treg restoration):**

| Mechanism | Drug | Run | Target |
|-----------|------|-----|--------|
| iTreg induction | TGF-β pathway support (losartan reduces TGF-β overshoot; SOCE/Mg) | run_150 | CNS1 SMAD3 |
| Treg survival/expansion | Ultra-low-dose IL-2 / aldesleukin | run_151 | CD25/STAT5 |
| Treg effector function | Abatacept (CTLA4-Ig) | run_148 | Trogocytosis |

**Monitoring:**
- Treg expansion confirmation: CD4⁺CD25hiCD127low (flow cytometry) at 4 weeks
- C-peptide AUC: track β cell preservation response
- IL-2 serum levels: not routinely available; dosing guided by Treg % and clinical tolerance

---

## Cross-Axis Integrations

- **run_140** (IL2RA/CD25/JAK3/STAT5): receptor-side partner; run_151 = cytokine, run_140 = signal transduction; together = complete IL-2/IL-2R axis
- **run_148** (CTLA4/abatacept): CTLA4 trogocytosis depletes CD80/CD86 → reduces IL-2 production in effector cells; abatacept + low-dose IL-2 = synergistic Treg restoration
- **run_150** (TGF-β/SMAD3): TGF-β induces new iTregs (CNS1); IL-2 maintains/expands existing Tregs; three-arm restoration
- **run_127** (SOCE/STIM1/ORAI1): NFAT1 downstream of SOCE → cooperates with SMAD3 at CNS1 → also activates IL-2 promoter in effector T cells; Ca²⁺ signal drives both IL-2 production (effectors) and iTreg induction (TGF-β/NFAT1/SMAD3)
- **run_102** (NKG2D): IL-2 deficiency → NK dysfunction; NK NKG2D expression partially dependent on IL-2 priming via dimeric IL-2Rβγ
- **run_085** (AMPK): AMPK → mTORC1 ↓ → Treg metabolic fitness; IL-2/STAT5 signaling → mTORC1 activation needed for Treg proliferation; AMPK/mTOR balance determines net Treg expansion efficiency

---

## Summary Integration

IL-2 cytokine fills the final gap in the complete IL-2/IL-2R axis (run_140 = receptor; run_151 = cytokine + pharmacology). The dose-selectivity pharmacology (trimeric 10 pM Kd for Tregs vs dimeric 1 nM Kd for NK/CD8) is the mechanistic foundation for DIABIL-2 and the entire low-dose IL-2 immunotherapy rationale. JES6-1/CD25-biased IL-2 engineering removes the last pharmacological obstacle (selectivity without NK activation). The three-arm Treg restoration protocol (TGF-β/CNS1 induction + IL-2/CD25 expansion + abatacept/trogocytosis) represents the most complete Treg-restoration strategy in the framework.

---

*One-hundred-and-forty-fourth extension | IL-2-cytokine-4-helix-bundle IL-2-gene-AP1-NFAT-promoter CD28-amplification CTLA4-run148-IL2-suppression mRNA-instability-TTP-AU-rich trimeric-IL-2Rαβγ-Tregs-10pM dimeric-IL-2Rβγ-NK-CD8-1nM dose-selectivity-hierarchy JES6-1-anti-IL2-complex CD25-biased-delivery NKTR358-RG7461-LY3471851 DIABIL-2-Hartemann2013-LancetDE aldesleukin-Treg-expansion C-peptide-preservation Treg-autocrine-starvation FOXP3-IL2-promoter-repression IL-2-deficiency-NK-ME-CFS run140-receptor-partner run148-CTLA4-synergy run150-TGF-β-CNS1-partner run127-SOCE-NFAT1 run102-NKG2D rosacea-Treg:Th17-ratio three-arm-Treg-protocol | run_151 | Framework at SATURATION + 40: 151 runs*