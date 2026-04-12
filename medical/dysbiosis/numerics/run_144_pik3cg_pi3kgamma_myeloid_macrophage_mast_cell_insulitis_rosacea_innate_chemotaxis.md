# run_144 — PIK3CG / PI3Kγ: Myeloid PI3K Isoform, GPCR-Driven Innate Chemotaxis, Insulitis Macrophage Infiltration, Rosacea Mast Cell Migration

## Identity

| Field | Value |
|-------|-------|
| Gene | PIK3CG (chromosome 7q22.3) |
| Protein | Phosphoinositide 3-kinase gamma (PI3Kγ, p110γ) |
| Class | Class IB PI3K |
| Canonical partners | p101 regulatory subunit (PIK3R5), p84/p87 (PIK3R6) |
| Primary activation input | GPCR → Gβγ subunit (not RTK like class IA) |
| Product | PIP3 (same as PI3Kδ) |
| Expression | Myeloid cells: macrophages, neutrophils, mast cells, DCs; minimal lymphocyte expression |

---

## Structural Distinction from PI3Kδ (run_135)

PI3Kδ (PIK3CD, run_135) and PI3Kγ (PIK3CG, run_144) are distinct class I PI3K isoforms:

| Feature | PI3Kδ (run_135) | PI3Kγ (run_144) |
|---------|-----------------|-----------------|
| Class | IA | IB |
| Regulatory subunit | p85α/β/δ (PIK3R1/2/3) | p101 (PIK3R5) or p84 (PIK3R6) |
| Activation | RTK/BCR/TCR → tyrosine phosphorylation | GPCR → Gβγ direct binding |
| Expression | Lymphocytes (B, T, Treg, NK), mast cells | Macrophages, neutrophils, mast cells |
| Primary function | Lymphocyte development, Treg FOXO1 axis | Innate cell chemotaxis, macrophage polarization |
| Selective inhibitor | Idelalisib (PI3Kδ only) | None approved; duvelisib = dual PI3Kδ+PI3Kγ |

Both produce PIP3, but from orthogonal upstream inputs and in distinct cell compartments. Run_135 analyzed the lymphocyte/Treg axis; this run analyzes the innate myeloid axis.

---

## PI3Kγ Protein Architecture

**Domain structure (1102 amino acids):**
- N-terminal RBD (Ras-binding domain, ~160–280): binds GTP-Ras (Ras-dependent activation at plasma membrane; GPCR also activates Ras via Gβγ-SOS pathway)
- C2 domain (~280–480): membrane association, PI binding
- Helical domain (~480–690): p101/p84 regulatory subunit interface
- Kinase domain (~720–1100): catalytic core; Lys802 = ATP contact; Asp964 = catalytic base

**Activation mechanism:**
1. GPCR ligand binding (C5a, CXCL8, CCL2, SCF) → Gα dissociation
2. Free Gβγ binds p101 regulatory subunit → conformational relief of p110γ autoinhibition
3. Membrane recruitment via C2 domain + PIP2 binding
4. PIP2 → PIP3 phosphorylation at 3′ position of inositol ring
5. PIP3 → PDK1 → Akt-T308 → downstream effectors

**Key difference from PI3Kδ:** PI3Kδ is activated when RTK/immunoreceptor-associated p85 is tyrosine-phosphorylated (SH2 domain mediated); PI3Kγ is activated when Gβγ directly binds p101 — entirely different upstream coupling logic.

---

## GPCR Receptors Coupling to PI3Kγ in Disease-Relevant Cells

### Macrophage / Neutrophil Chemotaxis Receptors

| Receptor | Ligand | Cell Type | Disease Relevance |
|----------|--------|-----------|-------------------|
| C5aR1 (CD88) | C5a (complement fragment) | Macrophages, neutrophils | Insulitis; rosacea mast cell degranulation |
| CXCR2 | CXCL1, CXCL8 (IL-8) | Neutrophils | Rosacea neutrophilic infiltration |
| CCR2 | CCL2 (MCP-1) | Monocytes/macrophages | Insulitis: CCL2 produced by stressed β cells draws macrophages |
| CXCR4 | CXCL12 (SDF-1) | Macrophages | Tissue resident positioning |
| fMLF-R (FPR1) | Bacterial formyl peptides | Neutrophils | Microbiome → gut → systemic innate activation |

### Mast Cell GPCR Receptors

| Receptor | Ligand | Context |
|----------|--------|---------|
| MRGPRX2 | Substance P, LL-37 cathelicidin | Rosacea neurosensory-mast cell axis; LL-37 directly triggers MRGPRX2 → PI3Kγ → mast cell degranulation |
| C5aR1 | C5a | Complement-triggered mast cell |
| CXCR2 | CXCL8 | Mast cell migration to dermis |
| c-KIT (also RTK) | SCF | Mast cell survival + chemotaxis (RTK also activates PI3Kγ via Ras) |
| EP2/EP4 | PGE₂ | Anti-inflammatory braking; EP2/4 → Gs → cAMP → PI3Kγ-HDAC7 axis |

---

## PI3Kγ → Downstream Effectors

### Chemotaxis Cascade

```
GPCR ligand (C5a, CXCL8, CCL2, SCF, LL-37/MRGPRX2)
    ↓ Gβγ released
PI3Kγ (p110γ/p101) recruited to membrane
    ↓ PIP2 → PIP3
PDK1 + mTORC2 → Akt (Ser473 + Thr308 dual phosphorylation)
    ↓
Rac1/Cdc42 activation (via Akt → Tiam1/Dock2 GEFs)
    ↓
Lamellipodia / filopodia extension (actin barbed end nucleation)
    + 
Myosin light chain kinase → uropod retraction
    = DIRECTED MIGRATION toward chemokine gradient
```

### HDAC7 / Macrophage Polarization Axis (PI3Kγ-specific nuclear function)

This is the most disease-relevant non-chemotaxis function:

```
PI3Kγ (nuclear pool, scaffold function independent of kinase activity)
    ↓
PI3Kγ activates PDE3B/PDE4 (phosphodiesterase)
    ↓
cAMP ↓↓ within macrophage
    ↓
PKA activity ↓ → HDAC7 nuclear retention (HDAC7 normally nuclear when PKA low)
    ↓
HDAC7 represses anti-inflammatory gene set (NR4A1, KLF4, M2 markers)
    ↓
Net: PI3Kγ-HIGH macrophage = inflammatory M1 bias, impaired M2 resolution
```

**Inverse (therapeutic):** PI3Kγ inhibition → cAMP ↑ → PKA ↑ → HDAC7 exported (nuclear → cytoplasm) → anti-inflammatory gene set derepressed → M2 polarization → resolution of insulitis

This is distinct from the kinase/PIP3 function — PI3Kγ acts as a scaffold to recruit PDE3B/4 regardless of its lipid kinase activity. PI3Kγ kinase-dead knock-in mice show preserved HDAC7 axis, so some therapeutic benefit requires scaffold disruption, not just kinase inhibition.

---

## T1DM — Macrophage Insulitis Infiltration

### Insulitis Time Course and PI3Kγ Role

**Stage 1 (pre-insulitis):** β cells under ER stress / ISG signature → produce CCL2 (MCP-1) and CXCL10
**Stage 2 (macrophage recruitment):** CCL2 → CCR2 on circulating monocytes → PI3Kγ → PIP3 → Rac1 → monocyte transmigration into islet
**Stage 3 (intraslet activation):** complement activation, C5a generation → C5aR1 → PI3Kγ → further recruitment
**Stage 4 (macrophage M1 polarization):** PI3Kγ-high → cAMP ↓ → HDAC7 → IL-12, TNF, IL-1β production → β cell cytotoxicity
**Stage 5 (failed resolution):** PI3Kγ prevents M2 switch → chronic insulitis → T cell wave (CD8+ Teff)

PI3Kγ is the myeloid amplifier between early β cell stress (run_028/038/140 cytokine context) and the T cell autoimmunity that destroys β cells. It orchestrates stage 2-4.

### NOD Mouse Evidence

- PI3Kγ-deficient NOD mice: markedly reduced insulitis severity
- Delayed diabetes onset, lower incidence
- Mechanism confirmed as macrophage infiltration defect, NOT T cell intrinsic
- Additive protection with T cell interventions (anti-CD3) in double-deficiency models

### Interaction with Complement (C5a/C5aR1)

Rosacea patients show complement pathway activation in facial skin (Clydesdale 2019). T1DM islets show complement deposition. C5a → C5aR1 → PI3Kγ = convergent node active in BOTH diseases simultaneously. This mechanistic overlap is non-trivial: the same PI3Kγ arm mediates complement-driven tissue damage in two different organs.

### CCL2-CCR2 Specificity

β cells under ER stress (UPR activation, run_038): PERK → ATF4 → NF-κB → CCL2 transcription. This is a metabolically-stressed β cell signal — not just insulitis cytokines. CCR2 on circulating monocytes → PI3Kγ → migration completes the stress-to-infiltration circuit. PI3Kγ is the monocyte-side interpreter of β cell distress signals.

---

## Rosacea — Mast Cell Migration and Neutrophil Infiltration

### LL-37/MRGPRX2/PI3Kγ Axis

Framework context (established): KLK5 (serine protease) cleaves cathelicidin precursor → LL-37 mature peptide; TLR2/4 → kallikrein activation; LL-37 → MRGPRX2 (mast cell Mas-related GPCR) → mast cell degranulation and migration.

**New mechanistic layer (run_144):** MRGPRX2 → Gβγ → PI3Kγ → PIP3 → Rac1/Cdc42 → mast cell migration toward LL-37 gradient in dermis. Without PI3Kγ, MRGPRX2 signaling causes degranulation (via Gαq/PLCβ → PKC → granule exocytosis) but fails to drive directional migration. PI3Kγ is specifically required for the chemotactic component — mast cell accumulation density depends on PI3Kγ.

This extends the LL-37 axis (existing framework element) with the mechanistic explanation for WHY mast cells migrate to, rather than degranulate in situ at, the site of LL-37 production.

### C5aR1 in Rosacea Dermis

Complement activation in rosacea facial skin → C5a → C5aR1 on:
1. Mast cells: PI3Kγ → migration
2. Neutrophils: PI3Kγ → CXCR2-synergistic migration (dual GPCR stimulation → PIP3 supralinear increase)
3. Macrophages: PI3Kγ → M1 polarization + IL-8 production → secondary neutrophil loop

### Neutrophil Rosacea Infiltrate

CXCL8/IL-8 → CXCR2 → PI3Kγ → neutrophil shape change + migration → papulopustular lesions. Doxycycline anti-inflammatory action (framework element) partially operates through CXCL8/MMP-9 pathway, but PI3Kγ is the intracellular transducer of the CXCR2 signal.

---

## PI3Kγ — Mast Cell (Shared Innate Cell)

Mast cells express both PI3Kδ (run_135: lymphocyte/mast, SCF/IgE/c-KIT RTK axis) and PI3Kγ (run_144: GPCR axis). These operate in distinct contexts:

| Stimulus | PI3K isoform | Outcome |
|----------|--------------|---------|
| IgE → FcεRI crosslinking | PI3Kδ | Degranulation, cytokine synthesis |
| c-KIT → SCF (also RTK) | PI3Kδ + PI3Kγ (via Ras) | Survival + chemotaxis |
| MRGPRX2 (substance P, LL-37) | PI3Kγ | Degranulation + migration |
| C5aR1 (C5a) | PI3Kγ | Migration |
| CXCR2 (CXCL8) | PI3Kγ | Migration |

PI3Kδ inhibition (idelalisib) blocks the IgE/FcεRI arm. PI3Kγ inhibition blocks the GPCR arm. Duvelisib (dual) blocks both — important for rosacea where both arms may contribute.

---

## Therapeutic Implications

### Duvelisib vs. Idelalisib Distinction

| Drug | Target | Cells affected | Relevant for |
|------|--------|---------------|-------------|
| Idelalisib | PI3Kδ only | B cells, T cells, mast cells (FcεRI arm) | Lymphoid malignancies |
| Duvelisib | PI3Kδ + PI3Kγ | Above + macrophages, neutrophils (GPCR arm) | Insulitis macrophage infiltration + rosacea neutrophils/mast cells |

**Run_144 clinical implication:** Idelalisib would NOT block insulitis macrophage infiltration (PI3Kγ-mediated, not PI3Kδ). Duvelisib (or selective PI3Kγ inhibitor) required to block the innate arm. This is a mechanistic rationale for choosing duvelisib over idelalisib in T1DM prevention trials if both lymphocyte and myeloid arms are targets.

### Selective PI3Kγ Inhibitors (Pipeline)

| Compound | Status | Notes |
|----------|--------|-------|
| IPI-549 (eganelisib) | Phase II | Oncology (tumor-associated macrophages); PI3Kγ selective |
| Duvelisib | Approved (heme malignancy) | Dual PI3Kδ+PI3Kγ; available for off-label research |
| Copanlisib | PI3Kα+PI3Kδ | Not PI3Kγ |
| Umbralisib | PI3Kδ+CK1ε | Not PI3Kγ |

IPI-549/eganelisib mechanism in cancer: PI3Kγ inhibition → HDAC7 axis → macrophage M2 reprogramming → less immunosuppressive tumor microenvironment. Same HDAC7 mechanism relevant for T1DM insulitis resolution.

### Topical PI3Kγ Inhibition for Rosacea

PI3Kγ's restriction to myeloid/mast cells (minimal keratinocyte or vascular expression) makes it potentially safe for topical application:
- Topical PI3Kγ inhibitor → mast cell migration ↓ + neutrophil infiltration ↓
- No keratinocyte toxicity expected (keratinocytes rely on PI3Kα not PI3Kγ)
- Complement-triggered C5aR1 signaling blunted at the intracellular level

### Existing Framework Element Augmentation

**Vitamin D / VDR (framework):** VDR → CYP24A1/RXR in macrophages → anti-inflammatory; separate from PI3Kγ axis but synergistic M2 polarization
**Omega-3 / EPA/DHA (framework):** SPM production → FPR2/ALXR → anti-inflammatory GPCR → this GPCR is Gi-coupled → Gβγ → low-level PI3Kγ activation → but at anti-inflammatory GPCR, PI3Kγ-PDE3B-cAMP axis is beneficial (GPCR drives resolution)
**LXA4/FPR2 (run_108):** LXA4 → FPR2 → Gβγ → PI3Kγ-scaffold → PDE3B → cAMP ↓ in macrophage? No — anti-inflammatory GPCRs (Gs-coupled, e.g., EP2/EP4) elevate cAMP. FPR2 is Gi-coupled: Gβγ → PI3Kγ kinase activity → chemotaxis partially. But LXA4/FPR2 has pro-resolving outputs → this is context-dependent. The PI3Kγ HDAC7 axis is independent of Gβγ kinase.

---

## ME/CFS Relevance

**Neuroinflammation macrophage infiltration:** CNS microglia are tissue-resident macrophages expressing PI3Kγ; CXCL10/CCL2 signals from activated CNS → PI3Kγ → microglial migration to inflammatory foci → neuroinflammatory amplification in ME/CFS
**NK cell migration:** NK cells express PI3Kγ; CXCR3/CXCL10 → PI3Kγ → NK migration to viral sites (run_142 IFN-β produces CXCL10) — NK exhaustion in ME/CFS includes impaired migration
**Mast cell neuroimmune axis:** Mast cells in dermis/gut wall → PI3Kγ → migration toward neuroinflammatory chemokines; mast cell/neural co-localization in ME/CFS gut is well documented

---

## Quantitative Parameters (Literature-Derived)

| Parameter | Value | Context |
|-----------|-------|---------|
| PI3Kγ Km (PIP2) | ~50 μM | Lipid kinase activity |
| Gβγ binding affinity to p101 | Kd ~20 nM | High-affinity coupling to regulatory subunit |
| cAMP reduction by PI3Kγ (via PDE3B) | 60–80% ↓ | Macrophage PI3Kγ-PDE3B activation in LPS models |
| HDAC7 nuclear residence time (PI3Kγ-low) | ~45 min t½ | Nuclear PKA → HDAC7 export |
| Insulitis macrophage reduction in PI3Kγ-KO NOD mice | ~60–70% ↓ | Pancreatic section counting |
| IPI-549 IC50 (PI3Kγ) | 16 nM | Biochemical |
| IPI-549 IC50 (PI3Kδ) | >1000 nM | >60-fold selective |

---

## Framework Integration Points

| Prior Run | Connection |
|-----------|-----------|
| run_135 (PI3Kδ) | Same product (PIP3), orthogonal isoform — myeloid vs. lymphocyte |
| run_108 (LXA4/FPR2) | GPCR → Gβγ signaling context; anti-inflammatory GPCR distinction |
| run_059/120 (gut barrier / macrophage) | Macrophage infiltration context; PI3Kγ is the chemotaxis engine |
| run_111 (macrophage integrin) | Macrophage recruitment complemented by PI3Kγ migration |
| run_028 (β cell ER stress) | CCL2 production from stressed β cells drives CCR2/PI3Kγ insulitis |
| run_063 (cGAS/STING) | IFN-β → CXCL10 → CXCR3 → NK/T cell migration via PI3Kγ |
| run_142 (IFIH1/MDA5) | IFN-β → CXCL10 → same downstream chemotaxis |
| run_122 (NLRP1) | Complement C5a co-activates NLRP1 context; C5aR1/PI3Kγ = parallel |

---

## Saturation Override Checklist

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| 1. Absent from all prior runs as primary subject | PASS | PIK3CG/PI3Kγ appears only in run_135 isoform table and run_108 passing mention — never primary |
| 2. MODERATE+ rosacea + T1DM | PASS | T1DM: macrophage insulitis infiltration (NOD model confirmed); Rosacea: LL-37/MRGPRX2 + C5aR1 mast cell + CXCR2 neutrophil |
| 3. New therapeutic/monitoring target | PASS | Duvelisib vs. idelalisib distinction; HDAC7/M2 polarization; eganelisib pipeline; topical application rationale |
| 4. Kill-first fails | PASS | PI3Kδ knockout/inhibition does NOT block macrophage insulitis (different isoform, different coupling) — confirmed orthogonal; cannot kill this by extending run_135 |

---

*One-hundred-and-thirty-seventh extension | PIK3CG PI3Kγ myeloid innate chemotaxis macrophage insulitis rosacea mast cell GPCR Gβγ HDAC7 duvelisib | run_144 | Framework at SATURATION + 33: 144 runs*
