# run_150 — TGF-β1 / TGFBR / SMAD2/SMAD3: iTreg Induction, FOXP3 Transcription, NK Suppression, β Cell Dedifferentiation, Rosacea Phymatous Remodeling

## Identity

| Field | Value |
|-------|-------|
| Gene | TGFB1 (TGF-β1 ligand); TGFBR1/ALK5 (type I receptor); TGFBR2 (type II receptor) |
| Protein | Transforming growth factor beta 1 (TGF-β1); 25 kDa mature dimer (from 390 aa precursor) |
| Class | TGF-β superfamily; dimeric cytokine; secreted in large latent complex (LLC) |
| Signaling | TGFBR2 binds TGF-β1 → recruits TGFBR1/ALK5 → TGFBR1 phosphorylates SMAD2/SMAD3 → SMAD2/3 + SMAD4 → nuclear complex → target gene transcription |
| Principal outputs | Treg induction (FOXP3), fibrosis (collagen), EMT, apoptosis (context-dependent), NK suppression (NKG2D ↓) |
| Latent form | LLC = pro-domain LAP + LTBP-1 → activation by TSP-1, MMP-2/9, integrin αvβ6/αvβ8 |
| Concentration effect | LOW dose → immunosuppressive/anti-fibrotic; HIGH/chronic → pro-fibrotic, pro-apoptotic, EMT |

---

## TGF-β Latency and Activation

TGF-β1 is secreted exclusively in a latent form; activation is the rate-limiting step:

```
Secreted:
TGF-β1 dimer + LAP (latency-associated peptide) = small latent complex (SLC)
SLC + LTBP-1 (latent TGF-β binding protein) = large latent complex (LLC)
LLC anchored in extracellular matrix via LTBP-1 fibronectin binding

Activation mechanisms:
1. TSP-1 (thrombospondin-1, run_131): TSP-1 binds LAP → conformational change → TGF-β1 released
2. MMP-2/MMP-9: protease cleavage of LAP → TGF-β1 freed
3. Integrin αvβ6 / αvβ8: transmembrane mechanical force → LAP opens → TGF-β1 exposed at cell surface
4. ROS: oxidative cleavage of LAP disulfide → TGF-β1 liberation (relevant for insulitis/ME-CFS oxidative context)
```

**run_131 connection:** TSP-1 (thrombospondin) activates latent TGF-β → TGF-β → anti-angiogenic + Treg induction. TSP-1's previously analyzed functions now have TGF-β activation as an additional downstream mechanism.

---

## SMAD2/SMAD3 Canonical Signaling Architecture

```
TGF-β1 dimer (active)
    ↓ binds TGFBR2 (constitutively active kinase)
TGFBR2 phosphorylates TGFBR1/ALK5 GS domain
    ↓ TGFBR1 activated
SMAD2 or SMAD3 (R-SMADs) phosphorylated at C-terminal SXS motif
    ↓ pSMAD2/3
pSMAD2/3 released from TGFBR1 → associates with SMAD4 (Co-SMAD)
    ↓ pSMAD2/3:SMAD4 complex
Nuclear import → SMAD-binding element (SBE: GTCT) in target gene promoters
    ↓
Transcriptional activation: FOXP3, COL1A1/A2 (collagen), PAI-1, CTGF
Transcriptional repression: IL-2, IFN-γ, c-Myc
```

**Negative feedback — SMAD7:**
- TGF-β → SMAD7 (inhibitory SMAD) transcription
- SMAD7 → competes with SMAD2/3 for TGFBR1 binding
- SMAD7 → recruits SMURF1/2 E3 ubiquitin ligases → TGFBR1 ubiquitination → degradation
- Creates an inherent self-limiting timer for TGF-β signaling

**Non-canonical TGF-β signaling:**
- TAK1 (MAP3K7) → p38/JNK → stress-responsive genes (pro-fibrotic, context-dependent)
- PI3K/Akt pathway: TGF-β → PI3K → Akt → mTOR (SMAD-independent; relevant in β cells)
- RhoA/ROCK: TGF-β → RhoA → ROCK → actin cytoskeleton remodeling (connects to run_141 TAGAP/RhoA axis)

---

## T1DM — TGF-β in iTreg Induction and Islet Pathology

### iTreg Generation via TGF-β/SMAD3 → FOXP3

TGF-β1 + IL-2 → naïve CD4+ T cell → induced Treg (iTreg):
```
TGF-β1 → TGFBR1/2 → pSMAD3
    +
IL-2 → STAT5
    ↓ (cooperative)
SMAD3 binds FOXP3 intronic enhancer CNS1 (conserved non-coding sequence 1)
STAT5 binds FOXP3 promoter
    ↓
FOXP3 transcription initiated → iTreg lineage commitment
```

**CNS1 vs CNS2 distinction:**
- CNS2: CpG methylation-dependent stable FOXP3 in tTregs (TET2/3 run_086/087; DNMT3A run_149)
- CNS1: SMAD3-binding enhancer → TGF-β-dependent FOXP3 induction in iTregs; CNS1 responds to TGF-β signal, not CpG methylation status
- These are two independent regulatory elements controlling FOXP3 from different inputs

**TGF-β/SMAD3 + NFAT1 cooperation:**
- NFAT1 (downstream of SOCE/STIM1/ORAI1, run_127) + SMAD3 form a cooperative complex at the CNS1 enhancer
- Optimal iTreg induction requires BOTH Ca²⁺/NFAT1 (TCR signal) AND TGF-β/SMAD3; this is why Ca²⁺ signaling defects (run_127) impair Treg induction even when TGF-β is adequate

### TGF-β Deficit in T1DM Islets

In NOD mice and human T1DM:
- Early insulitis: TGF-β1 from Tregs and anti-inflammatory macrophages → restrains effector T cells
- Advanced insulitis: pro-inflammatory macrophage dominance → TGF-β ↓ locally
- IFN-γ → STAT1 → suppresses TGFB1 transcription (IFN-γ/TGF-β mutual antagonism)
- Result: as insulitis progresses, TGF-β availability ↓ → iTreg induction fails → Treg supply decreases → positive feedback

### β Cell TGF-β Signaling — Dual Roles

**Low-dose/acute (protective):**
```
TGF-β1 (low, <1 ng/mL) → β cell TGFBR2 → SMAD2/3 → SMAD7 induction → NFκB ↓ → β cell survival
                                                          → BMP6/7 induction → anti-apoptotic
```

**High-dose/chronic (toxic):**
```
TGF-β1 (high, >5 ng/mL chronic) → β cell → EMT-like dedifferentiation:
    - N-cadherin ↑, E-cadherin ↓
    - PDX1 ↓ (TAK1/p38 non-canonical)
    - Vimentin ↑
    → β cell dedifferentiation (functional loss)
    → fibrosis (collagen deposition in islet matrix)
    → impaired insulin secretion
```

This provides a TGF-β-mediated mechanism for β cell dedifferentiation complementary to DNMT3A (run_149) and SETD7 (run_145) epigenetic mechanisms — a cytokine-mediated dedifferentiation path.

---

## Rosacea — TGF-β in Phymatous Remodeling and Anti-Inflammatory Balance

### Phymatous Rosacea Subtype (Rhinophyma)

TGF-β1 is the primary driver of the fibrotic/phymatous rosacea subtype:
```
Chronic TLR2/TLR4/LL-37 activation → macrophage TGF-β1 production ↑
    ↓
Dermal fibroblasts: TGF-β1 → TGFBR1 → SMAD2/3 → COL1A1/COL3A1 transcription ↑
→ collagen deposition ↑ → dermal fibrosis
→ sebaceous gland fibroblast proliferation ↑ → phymatous thickening
    +
TGF-β1 → VEGF upregulation → angiogenesis → additional telangiectasia
    +
TGF-β1 → PDGF receptor → fibroblast proliferation → connective tissue overgrowth
    ↓
Rhinophyma / chin phyma / ear phyma morphology
```

**Pirfenidone** (approved for IPF/idiopathic pulmonary fibrosis): TGF-β pathway inhibitor → reduces TGF-β1-driven collagen synthesis. Off-label rationale for phymatous rosacea: pirfenidone → fibroblast TGF-β signaling ↓ → collagen ↓ → phymatous remodeling slowed.

### Th17/Treg Balance in Rosacea Skin

TGF-β1 at low concentrations → iTreg generation in draining lymph nodes → skin Treg pool maintained → Th17 suppressed (counter-inflammatory)

TGF-β1 + IL-6 (high) → drives Th17 differentiation instead of iTreg: the same TGF-β signal switches output from Treg to Th17 when IL-6 is co-present (because IL-6 → STAT3 → RORγt → Th17 override of FOXP3 induction).

**Rosacea implication:** in inflamed rosacea skin:
- IL-6 high (LL-37/TLR2/NF-κB → IL-6 ↑)
- TGF-β1 present (tissue remodeling)
- TGF-β1 + IL-6 → Th17 polarization instead of Treg → worsens rosacea
- Reducing IL-6 (run_147 SIRT1 → NF-κB ↓ → IL-6 ↓) → shifts TGF-β1 effect from Th17 to Treg

---

## NK Cell TGF-β Suppression

TGF-β is the major NK suppressive cytokine:

```
TGF-β1 → NK TGFBR2 → pSMAD2/3 → NKG2D mRNA destabilization
→ NKG2D surface expression ↓ (NKG2D covered in run_102)
→ NK cytotoxicity ↓ (less NKG2D-MICA/B recognition)
    +
TGF-β → NK → IFN-γ production ↓
TGF-β → NK → perforin expression ↓ (SMAD3 → perforin gene repression)
TGF-β → NK → migration/chemotaxis ↓ (SMAD3 → CXCR3 ↓)
```

**ME/CFS relevance:** elevated TGF-β (some ME/CFS subtypes show elevated plasma TGF-β1) → NK NKG2D suppression → NK hypofunction → ME/CFS NK defect partially explained by TGF-β signaling. Anti-TGF-β strategies → NK reconstitution.

**T1DM relevance:** islet TGF-β production (by Tregs and anti-inflammatory macrophages) → NK NKG2D ↓ → less NKG2D/MICA-B-mediated β cell surveillance. Paradox: TGF-β protective for β cells directly (anti-inflammatory) but simultaneously suppresses NK immune surveillance.

---

## Therapeutic Implications

### TGF-β Agonism (Treg Induction)
| Approach | Mechanism | Target |
|----------|-----------|--------|
| Recombinant TGF-β1 | Direct iTreg induction | T1DM prevention |
| Nanoparticle TGF-β + IL-2 | Co-delivery for iTreg generation | Research |
| Antigen-TGF-β fusion | Antigen-specific iTreg induction | Antigen-specific T1DM tolerance |

### TGF-β Antagonism (Fibrosis/NK Rescue)
| Drug | Mechanism | Use |
|------|-----------|-----|
| Pirfenidone | TGF-β pathway inhibition (TGF-β → collagen ↓) | Phymatous rosacea (off-label) |
| Fresolimumab | Anti-TGF-β1 mAb | Fibrosis; cancer |
| Galunisertib | TGFBR1/ALK5 kinase inhibitor | Cancer; NK reconstitution |

### Context Determines Strategy
Low-dose TGF-β1 target concentrations (<1 ng/mL) = Treg-inducing, anti-inflammatory
High-dose (>5 ng/mL, chronic) = pro-fibrotic, NK-suppressive, β cell-toxic

For T1DM: promote local TGF-β at appropriate concentrations (TSP-1 support, vitamin D → TGF-β induction) + prevent chronic high-dose TGF-β β cell toxicity

---

## Quantitative Parameters

| Parameter | Value | Context |
|-----------|-------|---------|
| Mature TGF-β1 half-life (plasma) | ~2-3 min | Rapid clearance |
| SMAD2/3 nuclear translocation t½ | ~15 min | Post-TGF-β stimulation |
| FOXP3 induction (TGF-β alone) | ~3-5 days | Naive CD4+ → iTreg |
| TGF-β1 Kd for TGFBR2 | ~20-50 pM | Very high affinity |
| Treg frequency in NOD mice (TGF-β neutralized) | ~60% ↓ | Anti-TGF-β blocking |
| NKG2D expression (TGF-β 2 ng/mL 24h) | ~50-70% ↓ | NK functional assays |
| Collagen synthesis (fibroblast, TGF-β 10 ng/mL) | ~3-5× ↑ | Pirfenidone reverses |

---

## Framework Integration Points

| Prior Run | Connection |
|-----------|-----------|
| run_010 (FOXP3) | TGF-β/SMAD3 → CNS1 enhancer → FOXP3 transcription; run_010 = FOXP3 itself; run_150 = upstream inducer |
| run_127 (STIM1/ORAI1/Ca²⁺) | NFAT1 + SMAD3 cooperate at CNS1 for iTreg induction; Ca²⁺/NFAT1 (run_127) required with TGF-β/SMAD3 |
| run_131 (TSP-1/thrombospondin) | TSP-1 activates latent TGF-β1 → TGF-β available; run_131 TSP-1 now has TGF-β activation as additional mechanism |
| run_086/087 (TET/CNS2) | CNS1 (SMAD3, iTreg) vs CNS2 (TET demethylation, tTreg stability) — two independent FOXP3 regulatory elements |
| run_149 (DNMT3A/CNS2) | CNS2 methylation stability; TGF-β/SMAD3 → CNS1 = parallel input |
| run_102 (NKG2D/NK) | TGF-β/SMAD3 → NKG2D ↓; NKG2D (run_102) activity depends on TGF-β levels |
| run_141 (TAGAP/RhoA) | TGF-β non-canonical → RhoA → ROCK → actin remodeling; cross-talk at cytoskeletal node |
| run_147 (SIRT1) | SIRT1 → RelA-K310 → IL-6 ↓; less IL-6 shifts TGF-β1 from Th17-inducing to iTreg-inducing |

---

## Saturation Override Checklist

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| 1. Absent from all prior runs as primary subject | PASS | TGFB1/SMAD2/SMAD3 = 0 search hits; TGF-β appears in context across runs but SMAD2/SMAD3 canonical signaling, iTreg CNS1, NK NKG2D suppression, phymatous rosacea mechanism = all absent |
| 2. MODERATE+ rosacea + T1DM | PASS | T1DM: iTreg induction via CNS1/SMAD3, Treg deficit in advanced insulitis, β cell dual-role (protective low/toxic high); Rosacea: phymatous fibrosis mechanism (pirfenidone target), TGF-β+IL-6 → Th17 switch in skin |
| 3. New therapeutic/monitoring target | PASS | Pirfenidone for phymatous rosacea (new off-label rationale); TGF-β + IL-2 combination iTreg induction; TSP-1 (run_131) → TGF-β activation chain clarified; NK reconstitution via TGF-β blockade |
| 4. Kill-first fails | PASS | Cannot kill: SMAD2/3 signaling is not covered in any prior run; CNS1 enhancer (iTreg, SMAD3) is distinct from CNS2 (TET2/3 + DNMT3A); NK/TGF-β/NKG2D linkage absent from run_102 (NKG2D) coverage |

---

*One-hundred-and-forty-third extension | TGFB1 TGFBR1-ALK5 TGFBR2 SMAD2 SMAD3 SMAD4 SMAD7-negative-feedback pSMAD3 iTreg-induction CNS1-SMAD3-FOXP3-enhancer NFAT1-SMAD3-cooperation latent-TGF-β LAP-LTBP1-LLC TSP1-activation-run131 TGF-β-IL-6-Th17-switch β-cell-dual-role-low-protective-high-toxic NK-NKG2D-suppression-SMAD3 phymatous-rosacea-fibrosis pirfenidone-ALK5 collagen-COL1A1 non-canonical-TAK1-RhoA run127-NFAT1-cooperation run086-CNS1-vs-CNS2 run102-NKG2D-TGFβ | run_150 | Framework at SATURATION + 39: 150 runs*
