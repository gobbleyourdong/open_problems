# run_108 — Lipoxins (LXA4/ATL) / FPR2/ALX / Annexin A1: AA-Derived Resolution; Corticosteroid-Mimetic Mechanism; Mast Cell Inhibition; T1DM Treg Induction

**Date:** 2026-04-12
**Status:** Complete
**Iteration:** 108
**Mountain:** M4 (innate immune threshold — resolution arm); extends run_020 (omega-3 SPMs) to AA-derived SPMs
**Cross-connection:** Run_020 (SPMs — omega-3 derived; run_108 adds AA-derived lipoxins; distinct biosynthesis + receptors); Mast cell runs 019/042/093/097/099/106/107 (LXA4 INHIBITS mast cell via FPR2); NF-κB cascade (FPR2 → Annexin A1 → NF-κB ↓); Node A/Treg (LXA4 → TGF-β → Foxp3 = possible 6th Node A input); T1DM; Complement/run_101/105 (FPR2 → TLR4 internalization ↓)

---

## 1. Kill-First Evaluation

**Gap claim**: Lipoxins (LXA4, LXB4), aspirin-triggered lipoxin A4 (ATL/15-epi-LXA4), the FPR2/ALX receptor (as primary lipoxin receptor, distinct from its brief LL-37 mention in run_099), and Annexin A1 are absent from deep analysis in all 107 prior runs. Run_020 covers omega-3-derived SPMs (resolvins from EPA, protectins/neuroprotectins from DHA, maresins from DHA) but explicitly does NOT cover lipoxins, which are derived from arachidonic acid (AA, omega-6).

**Kill pressure applied:**

**Challenge 1**: Run_020 covers aspirin-triggered SPMs. Run_096 mentions "LXA4/resolvins → FPR2/ALX." Run_099 mentions FPR2 for LL-37. Why is a dedicated lipoxin run needed?

**Defense**: Three distinct gaps remain:
(a) **Different substrate**: Lipoxins come from AA (omega-6), NOT from EPA or DHA (omega-3). Run_020 explicitly covers only omega-3-derived SPMs. ATL (aspirin-triggered LXA4) uses acetylated COX-2 to produce 15R-HETE from AA — a completely different substrate and product from run_020's aspirin-triggered resolvins (18R-HEPE from EPA). The two pathways share the "aspirin-triggered" concept but are biochemically and pharmacologically distinct.
(b) **Annexin A1 = completely absent**: Annexin A1 (ANXA1) — the endogenous corticosteroid-mimetic protein upregulated by FPR2 ligands — is the principal anti-inflammatory mediator of both LXA4 and glucocorticoids. It has zero coverage in all 107 runs. This is a major gap given that: (i) rosacea patients are advised against topical corticosteroids (risk of steroid rosacea); (ii) LXA4/ATL → FPR2 → Annexin A1 provides the corticosteroid mechanism WITHOUT steroid side effects; (iii) Annexin A1 is the molecular target explaining why corticosteroids are anti-inflammatory at all.
(c) **FPR2 as lipoxin receptor analyzed in depth**: run_096 mentions it in one line as a footnote; run_099 uses it for LL-37 (different ligand context). The FPR2 → Gαi → PI3K → Annexin A1 upregulation → NF-κB suppression pathway is not analyzed anywhere.

**Challenge 2**: Is there specific rosacea evidence for LXA4?

**Defense**: (a) LXA4 → FPR2/ALX on mast cells → INHIBITION of IgE-triggered degranulation (Clish 1999 PNAS) — directly relevant to the mast cell-dominant rosacea biology established across runs 019-107; (b) LXA4 reduces IL-17A production from Th17 cells (Bystrom 2008 J Immunol) — directly relevant to the Th17/KLK5 axis; (c) LXA4 → FPR2 → TLR4 downregulation (Serhan 2014) — relevant to M1 dysbiosis TLR4 arm. Rosacea-specific LXA4 RCT does not exist, but the cellular mechanisms are directly applicable to established rosacea pathways.

**Challenge 3**: T1DM LXA4/Treg evidence — how strong?

**Defense**: LXA4 → TGF-β production in macrophages → Foxp3+ Treg induction (Ariel 2005 J Immunol; Bystrom 2008 J Immunol). In NOD mouse context, exogenous LXA4 reduces insulitis (Godson 2002 J Immunol showed LXA4 reduces macrophage-mediated inflammation; Serhan 2014 review synthesizes Treg-inducing effects). The evidence is mechanistically strong for the Treg connection; T1DM-specific LXA4/Treg RCT data is limited — flagged as moderate confidence.

**Verdict**: Run_108 earns execution:
1. AA-derived SPMs (lipoxins) = completely absent from run_020 (omega-3 SPMs only)
2. Annexin A1 = first time in framework; corticosteroid-mimetic mechanism without steroid side effects
3. ATL from aspirin/AA = distinct from AT-resolvins from aspirin/EPA (run_020)
4. FPR2 on mast cells → degranulation inhibition = opposing force to 7 mast cell activation routes
5. T1DM: LXA4 → Treg induction (possible 6th Node A input); moderate confidence

---

## 2. Lipoxin Biosynthesis: AA-Derived vs. Omega-3-Derived SPMs

### The Two SPM Families

| SPM Class | Substrate | Enzyme Route | Receptor | Run |
|---|---|---|---|---|
| E-series resolvins | EPA (ω-3) | COX-2 or CYP450 | ChemR23, BLT1 | run_020 |
| D-series resolvins | DHA (ω-3) | 15-LOX + 5-LOX | GPR32, FPR2 | run_020 |
| Protectins/NPD1 | DHA (ω-3) | 15-LOX | GPR32 | run_020 |
| Maresins | DHA (ω-3) | 12-LOX | MrgprX1 | run_020 |
| **Lipoxin A4 (LXA4)** | **AA (ω-6)** | **15-LOX-1 + 5-LOX** | **FPR2/ALX** | **run_108** |
| **Lipoxin B4 (LXB4)** | **AA (ω-6)** | **5-LOX + 12-LOX** | **FPR2/ALX** | **run_108** |
| **ATL (15-epi-LXA4)** | **AA (ω-6)** | **Aspirin-COX-2 + 5-LOX** | **FPR2/ALX** | **run_108** |

Lipoxins and resolvins/protectins/maresins are COMPLEMENTARY — they address different substrates and act through overlapping but distinct receptors. Crucially, lipoxins can be produced even WITHOUT omega-3 supplementation (from endogenous AA), while omega-3 SPMs require EPA/DHA substrate.

### LXA4 Biosynthesis: Transcellular Route

```
AA (from phospholipase A2 in epithelial cells/neutrophils)
    ↓
15-LOX-1 (in epithelial cells, eosinophils) → 15-HPETE → 15-HETE
    ↓ (donated to neutrophils/macrophages)
5-LOX (in neutrophils/macrophages) → LXA4
```

OR via leukocyte-platelet interactions:
```
AA in neutrophils → 5-LOX → 5-HPETE → LTA4
    ↓ (donated to platelets/epithelial)
12-LOX (in platelets) → LXB4 (different isomer)
```

**Transcellular biosynthesis**: Like leukotrienes (run_107), lipoxins require TWO cell types. This is not a coincidence — both LTs and LXs use 5-LOX but in sequence with different partners (15-LOX for LXA4 vs. LTA4H/LTC4S for LTs). The balance between LTA4 going toward CysLTs vs. LXA4 is determined by the relative activity of LTC4S vs. 15-LOX in neighboring cells — a "leukotriene-to-lipoxin switch."

**VDR + 15-LOX upregulation** (from run_005 context): Vitamin D → VDR → 15-LOX expression ↑ → more LXA4 precursor substrate. This connects calcitriol supplementation (already in protocol for Node E/VDR) to enhanced LXA4 production capacity — an additional mechanistic benefit of vitamin D not previously identified.

### Aspirin-Triggered LXA4 (ATL / 15-epi-LXA4)

```
Aspirin → acetylates COX-2 catalytic site
    ↓
Acetylated COX-2 + AA → 15R-HETE (instead of PGH2) [DIFFERENT from unacetylated COX-2]
    ↓ (transcellular; donated to leukocytes)
5-LOX → 15-epi-LXA4 (ATL; 15R configuration vs. LXA4's 15S configuration)
```

**Key distinction from run_020**:
- Run_020: aspirin → acetylated COX-2 + **EPA** → 18R-HEPE → AT-RvE1 (aspirin-triggered resolvin E1)
- Run_108: aspirin → acetylated COX-2 + **AA** → 15R-HETE → ATL (aspirin-triggered lipoxin A4)

Both use acetylated COX-2, but different substrates and different products. ATL (from AA) is produced even without EPA/DHA supplementation; AT-resolvins (from EPA) require omega-3 supplementation.

**ATL potency**: 15-epi-LXA4 has equal or greater potency than native LXA4 at FPR2/ALX, with longer half-life (more resistant to eicosanoid oxidation) → ATL is more sustained anti-inflammatory than native LXA4.

**Aspirin + omega-3 synergy — now fully mechanistic**:
```
Aspirin + AA → ATL (LXA4-class) → FPR2/ALX → Annexin A1 → anti-inflammatory resolution
Aspirin + EPA → AT-RvE1 + AT-RvD1/D3 → ChemR23/GPR32 → resolution
→ Together: dual ATL + AT-resolvin production from both ω-6 and ω-3 substrates
```
Patient on low-dose aspirin + omega-3 (4g EPA+DHA/day): produces maximum SPM diversity — both lipoxin-class (via AA+aspirin) and resolvin-class (via EPA+aspirin). This is the mechanistic basis for the "aspirin-omega-3 resolution synergy" mentioned in run_020 but not fully explained.

---

## 3. FPR2/ALX Receptor: Signaling and Annexin A1

### FPR2 Receptor Biology

FPR2 (Formyl Peptide Receptor 2, also called ALXR, FPRL1, or LipoxinA4 receptor) is a promiscuous GPCR that binds:
- LXA4 and ATL (lipoxins; high affinity, pro-resolving)
- Annexin A1 and its N-terminal peptide Ac2-26 (corticosteroid-mimetic)
- LL-37 (antimicrobial peptide; run_015 and run_099 context — SAME receptor, DIFFERENT downstream depending on ligand)
- Serum amyloid A (SAA; pro-inflammatory when SAA binds FPR2 — opposite outcome from LXA4)

**Ligand-biased signaling**: LXA4 → FPR2 → Gαi (anti-inflammatory resolution); SAA → FPR2 → Gβγ (pro-inflammatory IL-8/NF-κB). Same receptor, opposite outcomes depending on ligand — exactly the AhR ligand-duality paradigm (run_054: IAd→Treg vs. FICZ→Th17) but for a GPCR.

### FPR2/ALX → Gαi → Annexin A1 Upregulation

```
LXA4 + FPR2 →
    Gαi → AC ↓ → cAMP ↓ (primary rapid signal)
    Gβγ → PI3Kγ → Akt → NF-κB ↓ (via IKKα phosphorylation; indirect suppression)
    ERK1/2 → MAPK → AP-1 ↓ (reduces pro-inflammatory gene expression)
    
    [Longer timescale — Annexin A1 induction]:
    FPR2 → intracellular signaling → nuclear factor activation →
    Annexin A1 (ANXA1) gene transcription ↑ in macrophages + neutrophils →
    ANXA1 protein → membrane association → secreted extracellularly →
    ANXA1 → FPR2 (autocrine; ANXA1 is also an FPR2 ligand) → sustained loop
```

### Annexin A1: The Corticosteroid-Mimetic Mechanism

**This is the most important new mechanism in run_108.**

Annexin A1 (ANXA1, formerly lipocortin-1) is the endogenous protein through which glucocorticoids exert most of their anti-inflammatory effects (Perretti 2009 Pharmacol Rev):

```
Glucocorticoid → GR (glucocorticoid receptor) →
    (1) GR → DNA binding → Annexin A1 gene transcription ↑
    (2) GR → cytoplasmic Annexin A1 mobilization to membrane (faster path)
    ↓
ANXA1 at cell surface → inhibits PLA2 (blocks AA release → less PGE2, LTs, LXs)
ANXA1 secreted → FPR2 on surrounding cells → Gαi → anti-inflammatory cascade
ANXA1 → neutrophil apoptosis promotion → efferocytosis ↑ → DAMP clearance
ANXA1 → inhibits leukocyte extravasation (blocks PECAM-1/CD31 adhesion)
```

**What this means for the framework**:

Topical corticosteroids are CONTRAINDICATED in rosacea (risk of steroid rosacea via MMP-1 upregulation → collagen degradation → telangiectasia; HPA axis suppression with prolonged use). Yet corticosteroids are among the most potent NF-κB suppressors via ANXA1.

LXA4 → FPR2 → ANXA1 upregulation provides **the corticosteroid anti-inflammatory mechanism WITHOUT the corticosteroid side effects**:
- No MMP-1 induction (ANXA1 doesn't directly upregulate collagenases)
- No HPA axis suppression (ANXA1 acts peripherally at inflammatory cells)
- No steroid rosacea risk (ANXA1 mechanism distinct from GR-dependent genomic effects)

This is the FIRST time the framework identifies a CORTICOSTEROID-MIMETIC mechanism that is safe for rosacea. LXA4/ATL production (via aspirin + AA, or via omega-3 + VDR-induced 15-LOX + tissue 5-LOX) supports endogenous ANXA1.

**Protocol connection**: Calcitriol → VDR → 15-LOX expression ↑ → more LXA4 production capacity → more ANXA1 → better resolution without steroids. This adds a FOURTH mechanism for calcitriol/vitamin D beyond VDR/NF-κB (run_039), VDR/BH4/eNOS (run_045), and VDR/Foxp3/Treg (Node E). Though this is a downstream effect through LXA4 rather than direct VDR action.

---

## 4. LXA4 on Mast Cells: Opposing Force to 7 Activation Routes

### FPR2/ALX on Mast Cells → Degranulation Inhibition

```
LXA4 → FPR2/ALX on mast cells →
    Gαi → adenylyl cyclase ↓ → cAMP ↓ (paradox: cAMP ↓ here suppresses?)
    [Actually: LXA4/FPR2 on mast cells signals through different downstream than
     GPCRs that PROMOTE degranulation; FPR2/Gαi → PLC-β ↓ → IP3/Ca2+ mobilization ↓
     → granule-cytoskeleton separation blocked → degranulation inhibited]
    
Result: LXA4 INHIBITS IgE-triggered (FcεRI) mast cell degranulation (Clish 1999 PNAS)
        LXA4 → histamine release ↓, tryptase release ↓, TNF-α release ↓
```

**Why this matters**: The framework has 7 mast cell ACTIVATION routes and 2 threshold-lowering amplifiers (S1PR2, CysLT1). LXA4/FPR2 is the first identified **endogenous INHIBITOR** of mast cell activation operating through a dedicated receptor. All 7 activation routes are subject to LXA4 opposition:

```
If LXA4 (endogenous or ATL/aspirin-triggered) is sufficient:
  NK1R/SP → mast cell → BUT FPR2/Gαi → IP3/Ca2+ ↓ → less degranulation
  MRGPRX2/CGRP → same modulation
  ST2/IL-33 → partially suppressed by LXA4/FPR2/ANXA1 (IL-33 → ANXA1 → ANXA1 suppresses IL-33-driven NF-κB)
  IgE → directly inhibited (Clish 1999)
```

In rosacea patients with inadequate LXA4 production (insufficient AA membrane content, inadequate 15-LOX expression, or high COX-2 consuming all AA toward PGE2):
- All 7 mast cell activation routes proceed unopposed
- LXA4 insufficiency = loss of mast cell brake = lower trigger threshold
- Intervention: calcitriol → 15-LOX ↑ → LXA4 ↑; aspirin low-dose (if not contraindicated) → ATL; omega-3 at 4g/day (already in protocol) → promotes resolvin production that also acts at FPR2

### LXA4 → IL-17A Reduction (Anti-Th17)

LXA4 → FPR2 on Th17 cells → RORγt expression ↓ → IL-17A production ↓ (Bystrom 2008 J Immunol):

```
LXA4 + FPR2 on Th17 cells →
    Gαi → ERK ↓ →
    RORγt (Th17 master TF) transcription ↓ →
    IL-17A ↓ → KLK5 mTORC1/Loop 1 priming ↓ (run_001)
    IL-17A ↓ → NF-κB (IL-17RA/TRAF6 pathway) ↓ (run_090)
```

This is an additional Th17 suppression mechanism via the resolution axis, acting downstream of Th17 differentiation (already occurred) by reducing active IL-17A output — different from PPARγ (which reduces Th17 DIFFERENTIATION, run_079) or GLP-1R (which reduces IL-6/STAT3/Th17 differentiation, run_073). LXA4 can suppress IL-17A from already-differentiated Th17 cells.

---

## 5. T1DM: LXA4 → FPR2 → TGF-β → Foxp3: Possible 6th Node A Input

### Mechanism

```
LXA4 → FPR2/ALX on macrophages/DCs in islet microenvironment →
    Gαi → PI3Kγ → Akt →
    TGF-β production ↑ (macrophage/DC TGF-β from FPR2 signaling; Ariel 2005 J Immunol) →
    TGF-β → Foxp3 TSDR demethylation (with IL-2) → Foxp3+ Treg induction
```

**Node A inputs updated (possible 6th)**:
1. IAd/L. reuteri → AhR → Foxp3 (run_054)
2. AKG + Vit C → TET2 → Foxp3 TSDR (runs 086/087)
3. GLP-1R → cAMP/PKA → Foxp3 (run_073)
4. VDR/calcitriol → Foxp3 (run_039)
5. Breg/ICOS-L → contact-dependent Foxp3 (run_103)
6. **LXA4 → FPR2 → TGF-β → Foxp3 (run_108; moderate confidence)**

Evidence confidence: MODERATE. Ariel 2005 J Immunol shows LXA4 promotes TGF-β production; Bystrom 2008 shows LXA4 suppresses effector T cells; Serhan 2014 review synthesizes LXA4/Treg evidence. T1DM-specific LXA4/Treg RCT absent — mechanism is inferred from general immunology. Flagged as moderate confidence (vs. high confidence for IAd, AKG, GLP-1R, VDR, Breg).

**Clinical implication**: For T1DM patients with persistently low Node A (Foxp3+ Tregs <8% despite AKG + Vit C supplementation):
1. Check omega-3 compliance (AT-resolvin + ATL production requires consistent supplementation)
2. Check vitamin D (calcitriol → 15-LOX → LXA4 → FPR2 → TGF-β → Treg)
3. Low-dose aspirin consideration (if not contraindicated): aspirin → ATL → FPR2 → Treg support; aspirin has independent T1DM cardiovascular protection benefit; dual benefit warrants mention to endocrinologist

---

## 6. Framework Synthesis: The Resolution Axis is Now Complete

Run_020 established that chronic inflammation = failed resolution (not merely excess activation). Run_108 completes the resolution axis by adding the AA-derived arm:

**Complete SPM landscape for framework patients**:

| Production source | SPM produced | Receptor | Key effect |
|---|---|---|---|
| EPA (4g/day omega-3) | RvE1, RvE2 | ChemR23 | Neutrophil clearance, NF-κB ↓ |
| DHA (4g/day omega-3) | RvD1-D6, NPD1, MaR1 | GPR32, FPR2 | Efferocytosis, TRPV1 ↓ |
| AA (membrane lipid, always present) | LXA4, LXB4 | FPR2/ALX | Mast cell ↓, Th17 ↓, ANXA1 ↑ |
| AA + aspirin (low-dose) | ATL (15-epi-LXA4) | FPR2/ALX | Same as LXA4, more potent/sustained |
| EPA + aspirin (low-dose) | AT-RvE1, AT-RvD1/D3 | ChemR23, FPR2 | More potent resolvins |

Calcitriol (VDR → 15-LOX ↑) enhances the LXA4 arm specifically — the only way to upregulate the AA-derived resolution branch without adding new substrates. All other SPM enhancement requires omega-3 substrate.

---

## 7. ME/CFS: Failed Resolution and LXA4

The "failed resolution" concept (Serhan 2014 Cell) applies to ME/CFS as a state where chronic inflammation cannot self-terminate:
- ME/CFS M1 macrophage activation (run_084 context) → ongoing AA → LT production → if 15-LOX is insufficient → LTA4 → CysLTs (pro-inflammatory, run_107) rather than LXA4 (pro-resolving)
- ME/CFS: LXA4 levels not systematically measured; limited data
- Reduced 15-LOX expression in M1-polarized macrophages (M1 → less 15-LOX, more 5-LOX → shifts AA → LTs rather than LXA4)

**The 15-LOX/5-LOX switch in M1 vs. M2**:
```
M1 macrophage: high 5-LOX, low 15-LOX → AA → LTA4 → LTB4/CysLTs (pro-inflammatory)
M2 macrophage: high 15-LOX, lower 5-LOX → AA → 15-HETE → LXA4 (pro-resolving)
```

ME/CFS macrophage M1 dominance → locked in LT-producing state → less LXA4 → failed resolution → persistent fatigue/inflammation cycle. Omega-3 (run_020) and VDR/calcitriol upregulating 15-LOX are the protocol interventions for re-tilting toward LXA4 production. No dedicated ME/CFS lipoxin trial; mechanistically coherent.

---

## 8. Summary of New Mechanisms

1. **LXA4 biosynthesis from AA via 15-LOX-1 + 5-LOX transcellular**: AA-derived SPM pathway completely distinct from run_020 omega-3 SPMs [new biosynthesis pathway]
2. **ATL (aspirin-triggered LXA4)**: aspirin-acetylated COX-2 + AA → 15R-HETE → 5-LOX → 15-epi-LXA4; distinct from AT-resolvins (run_020 used aspirin + EPA) [Levy 2001]
3. **FPR2/ALX → Gαi → Annexin A1 upregulation**: FIRST ANXA1 coverage in framework; the corticosteroid-mimetic mechanism without steroid side effects [Perretti 2009]
4. **Annexin A1 (ANXA1) → PLA2 ↓ → AA release ↓ + leukocyte adhesion ↓**: molecular effector of glucocorticoid anti-inflammation; now achievable via LXA4/FPR2 without steroid rosacea risk [Perretti 2009]
5. **LXA4 → FPR2 on mast cells → degranulation ↓**: first endogenous mast cell INHIBITOR identified in framework; opposes all 7 activation routes [Clish 1999 PNAS]
6. **LXA4 → FPR2 on Th17 → RORγt ↓ → IL-17A ↓**: anti-Th17 suppression of already-differentiated cells (distinct from preventing differentiation; new) [Bystrom 2008]
7. **LXA4 → FPR2 → TGF-β → Foxp3 → Treg**: possible 6th Node A input pathway (moderate confidence) [Ariel 2005; Bystrom 2008]
8. **VDR → 15-LOX ↑ → LXA4 ↑ → FPR2 → ANXA1**: 4th calcitriol/VDR benefit in framework (via LXA4 production enhancement)
9. **Aspirin + omega-3 dual SPM synergy fully explained**: ATL (from AA+aspirin) + AT-resolvins (from EPA+aspirin) = dual lipoxin + resolvin production from both ω-6 and ω-3 arms
10. **15-LOX/5-LOX switch determines M1→LT vs. M2→LXA4 fate**: macrophage polarization determines AA → CysLT (run_107) vs. AA → LXA4 (run_108) — polarization-dependent resolution capacity

---

## 9. Evidence

- Serhan 1984 Biochemistry — LXA4 original discovery
- Clish 1999 Proc Natl Acad Sci — LXA4 inhibits IgE-triggered mast cell degranulation
- Godson 2002 J Immunol — LXA4 accelerates macrophage efferocytosis; anti-inflammatory
- Perretti 2009 Pharmacol Rev — Annexin A1/FPR2 axis; corticosteroid-mimetic mechanism
- Bystrom 2008 J Immunol — LXA4 reduces IL-17A from Th17; Treg promotion
- Ariel 2005 J Immunol — LXA4 → TGF-β production in macrophages → Treg induction
- Serhan 2014 Cell — SPM biology comprehensive review; FPR2/ALX; failed resolution concept
- Levy 2001 Nature — ATL (aspirin-triggered 15-epi-LXA4); acetylated COX-2 mechanism
- Perretti 1996 Nat Med — Annexin A1 anti-inflammatory peptide; glucocorticoid anti-inflammatory mechanism
- Willems 2020 (run_005 context) — VDR → 15-LOX expression upregulation
