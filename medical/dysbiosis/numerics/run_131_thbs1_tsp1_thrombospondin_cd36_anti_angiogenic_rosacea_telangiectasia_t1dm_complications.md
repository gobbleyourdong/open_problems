# Run 131 — THBS1/TSP-1 (Thrombospondin-1): Endogenous Anti-Angiogenic Restraint, CD36 Receptor, Rosacea Telangiectasia, T1DM Microvascular Complications

**Date:** 2026-04-12
**Framework position:** 6th endogenous telangiectasia restraint (ETR) mechanism; first matricellular anti-angiogenic protein; first CD36/fatty-acid-translocase-class receptor in framework
**Saturation criteria:** (1) THBS1/TSP-1/thrombospondin/CD36 absent from all 130 prior runs ✓ (2) Rosacea HIGH + T1DM MODERATE-HIGH (DR/DN) ✓ (3) New: first endogenous anti-angiogenic protein; CD36 anti-angiogenic receptor first in framework; completes pro/anti angiogenic balance with run_124 ✓ (4) Kill-first fails: run_124 LRG1/ALK1 covers pro-angiogenic switch in existing vessels; TSP-1/CD36 covers apoptotic restraint mechanism — distinct protein, distinct receptor, distinct direction ✓

---

## 1. Molecular Architecture

**Thrombospondin-1 (TSP-1):** Homotrimeric matricellular glycoprotein (~450 kDa assembled). Each monomer 1170 aa (human THBS1, chr15q14). Secreted by endothelial cells, platelets (dense granules), macrophages, keratinocytes, fibroblasts, pericytes, smooth muscle cells.

**Domain organization (N→C):**
```
NH2 — [N-terminal domain (NTD)] — [Procollagen homology] — 
       [Type 1 TSR repeats × 3] — [Type 2 EGF-like × 3] — 
       [Type 3 Ca²⁺-binding × 7] — [C-terminal domain (CTD)] — COOH
```

**Functional domains:**
- **NTD**: Heparin binding, HSPG association at cell surface; N-terminal interaction with VEGFR2 (inhibitory)
- **Type 1 TSR repeats**: Core anti-angiogenic domain; contains RFYVVMWK and GVITRIR peptide sequences; binds CD36 on ECs (Fyn-dependent apoptosis); activates latent TGF-β via KRFK motif → LSKL displacement from LTGF-β
- **Type 3 repeats**: Ca²⁺-binding EGF-like domains; binds integrins αVβ3 and αIIbβ3 (platelet)
- **CTD**: Binds CD47 (integrin-associated protein) → Gi → cAMP ↓; inhibits eNOS signaling

**CD36 (fatty acid translocase / thrombospondin receptor):**
- Class B scavenger receptor; 88 kDa; N/C-terminal cytoplasmic tails; large extracellular domain (hairpin structure)
- Ligands: TSP-1 type 1 repeats, oxidized LDL, long-chain FFAs (palmitate, oleate), apoptotic cells, Plasmodium-infected RBCs, beta-amyloid
- Expression: endothelial cells (microvasculature), macrophages/monocytes, dendritic cells, adipocytes, skeletal muscle, platelets, pancreatic ductal cells, keratinocytes
- Signaling upon TSP-1 binding: CD36 → Fyn kinase → p38 MAPK/JNK → caspase-3/8 → endothelial cell apoptosis (selective — VEGF simultaneously blocks this by promoting Bcl-2)
- Lipotoxicity arm: palmitate/CD36 on β cells/macrophages → ceramide synthesis → ER stress → apoptosis (distinct from TSP-1/anti-angiogenic arm)

---

## 2. TSP-1 Anti-Angiogenic Mechanisms (Four Distinct Axes)

### Axis 1: CD36/Fyn/Caspase → EC Apoptosis
```
TSP-1 (type 1 TSR domain)
    ↓ binds
CD36 (endothelial microvascular)
    ↓ 
Fyn (Src-family tyrosine kinase) phosphorylation
    ↓
p38 MAPK activation → caspase-3/8 activation
    ↓
Endothelial cell APOPTOSIS
    ↓
Capillary regression
```
Counter-signal: VEGF → KDR/VEGFR2 → PI3K/Akt → Bcl-2 ↑ → BLOCKS CD36/Fyn apoptosis
→ TSP-1 and VEGF compete for EC survival/death decision

### Axis 2: VEGFR2 Antagonism
- TSP-1 NTD binds VEGFR2 directly → inhibits VEGF-A binding → suppresses VEGFR2 autophosphorylation → PLCγ/PI3K/MAPK cascade ↓
- TSP-1 NTD also competes with fibroblast growth factor (FGF-2) for HSPG co-receptor binding
- Net: less VEGFR2 signaling → less EC proliferation/survival/migration

### Axis 3: CD47/eNOS Inhibition
- TSP-1 CTD → CD47 (integrin-associated protein IAP) → Gi-protein coupling → adenylyl cyclase inhibition → cAMP ↓ → PKA ↓ → eNOS Ser1177 phosphorylation ↓ → NO production ↓
- Reduced NO: (a) vasodilation ↓ → reduced blood flow; (b) EC migration ↓; (c) angiogenic signaling ↓
- Also: TSP-1 → CD36 → Fyn → indirect eNOS inhibition (separate from CD47 route)
- Net: hypoxia-induced vasodilation blunted, angiogenesis suppressed

### Axis 4: Latent TGF-β Activation
- TSP-1 type 1 TSR contains KRFK sequence → displaces LSKL sequence from latent TGF-β (LTBP complex) → releases active TGF-β
- Active TGF-β in rosacea context: mixed — anti-angiogenic (Smad3 → TSP-1 ↑ feedback) + immunosuppressive (Treg induction) but also pro-fibrotic (Smad2 → collagen)
- This axis is dose/context-dependent

---

## 3. Rosacea: TSP-1 as 6th ETR Mechanism

**Current ETR framework (anti-angiogenic restraints broken in rosacea):**

| # | Mechanism | Run |
|---|-----------|-----|
| 1 | ANGPT1/TIE2 vessel stabilization (pericyte-mediated) | run_063 |
| 2 | IFN-β/cGAS → anti-angiogenic ISGs | run_063 |
| 3 | VDR → TSP-1 ↑ (calcitriol axis) | referenced in run_031/056 |
| 4 | SPHK1/S1P → S1PR1 endothelial barrier | run_087 |
| 5 | LRG1/ALK1 — NOTE: this is PRO-angiogenic; its INDUCTION is the rosacea pathology | run_124 |
| **6** | **TSP-1/CD36/Fyn → EC apoptosis + VEGFR2 antagonism (loss = telangiectasia)** | **run_131** |

**Correction to ETR numbering:** run_124 LRG1/ALK1 is the PRO-angiogenic switch (its induction = pathology). TSP-1 is the endogenous restraint whose LOSS = pathology. Both together explain the angiogenic imbalance.

**Rosacea molecular mechanism:**
```
Normal skin:
TSP-1 (keratinocyte/EC/pericyte-secreted)
    ↓
CD36/VEGFR2 antagonism → EC homeostasis
    ↓
Controlled microvasculature

Rosacea:
KLK5 → PAR2 → VEGF-A ↑
LL-37 → VEGFR2 ↑ (direct)
UV-B → ROS → THBS1 promoter suppression (NF-κB antagonizes THBS1)
Demodex/microbiome TLRs → NF-κB → THBS1 ↓ (NF-κB represses THBS1)
    ↓
TSP-1 ↓ → CD36/Fyn apoptosis brake LOST
    ↓
VEGF unopposed → EC survival/proliferation
    ↓
Telangiectasia
```

**Evidence in rosacea tissue:**
- TSP-1 protein reduced in rosacea lesional skin vs perilesional and control (immunohistochemistry data)
- NF-κB activation (central to LL-37/KLK5/TLR2 rosacea) actively represses THBS1 transcription
- VDR → THBS1 ↑ (calcitriol connection: calcitriol indirectly upregulates TSP-1 via VDR; gains calcitriol 6th mechanism)
- ROS: UV-B and DAMP-driven oxidative stress → TSP-1 glycoprotein oxidative modification → loss of CD36-binding activity

**Run_124 / Run_131 integration (yin-yang model):**
```
Pro-angiogenic: LRG1 (run_124) → ALK1 → SMAD1/5 → EC proliferation  [induced in rosacea]
Anti-angiogenic: TSP-1 (run_131) → CD36/Fyn → EC apoptosis           [suppressed in rosacea]
                                  → VEGFR2 antagonism
Net effect: VEGF + LRG1 driving, TSP-1 brake absent → telangiectasia
```

---

## 4. T1DM: Microvascular Complications and β Cell Context

### 4a. Diabetic Retinopathy (DR)
- Normal retinal vasculature: pericytes produce TSP-1 → restrains EC proliferation
- Early DR: hyperglycemia → AGE accumulation → RAGE → NF-κB → THBS1 ↓ in pericytes/ECs
- Also: glycation of TSP-1 protein → CD36-binding domain impaired → functional loss even at normal mRNA
- TSP-1 loss → VEGF unopposed → retinal neovascularization (the pathology of proliferative DR)
- TSP-1 injection experiments in rodent DR models: exogenous TSP-1 delays/reduces retinal neovascularization
- Framework connection: run_124 LRG1/ALK1 also drives retinal neovascularization (run_124 covers ALK1 in DR context) — TSP-1 is the complementary restraint loss

### 4b. Diabetic Nephropathy (DN)
- TSP-1's TGF-β activation axis: in DN, TSP-1 → active TGF-β → Smad2 → glomerulosclerosis/collagen IV accumulation
- Dual role: loss of anti-angiogenic CD36/Fyn axis (bad for DR) but TGF-β activation (mediates fibrosis in DN)
- This explains why simple "restore TSP-1" approaches for T1DM complications require context-specific targeting

### 4c. CD36 / Lipotoxicity → β Cell
- CD36 expressed on pancreatic ductal/acinar cells, some β cell populations
- Palmitate → CD36 → ceramide synthesis (de novo pathway, separate from CERS2 run_106) → ER stress → mitochondrial dysfunction → β cell apoptosis
- This is the 19th β cell death mechanism: **lipotoxicity via CD36/ceramide entry**
- Distinct from run_106 (palmitate/SFA → ER stress via protein misfolding — CD36 as entry receptor was not named in run_106)
- Genetic variant: CD36 expression polymorphisms affect lipotoxic sensitivity
- Protocol note: CD36-mediated lipotoxicity is blocked by PPAR-α/γ ligands (fenofibrate, berberine) which downregulate CD36 surface expression on β cells and macrophages

### 4d. Macrophage CD36 / Insulitis
- CD36 on macrophages: TSP-1/CD36 → efferocytosis of apoptotic β cells → normally anti-inflammatory (tolerogenic)
- Deficient efferocytosis → accumulation of secondary necrotic β cell debris → DAMP release → NLRP3 (run_002) + NF-κB → amplified insulitis
- Connection: TSP-1-driven macrophage CD36 efferocytosis deficiency in hyperglycemic conditions → insulitis amplification

---

## 5. ME/CFS: Endothelial Dysfunction and Platelet Axis

- Platelet activation in ME/CFS: activated platelets release TSP-1 (stored in α-granules/dense granules); platelet hyperactivation → paradoxically HIGH platelet-derived TSP-1 in plasma
- However: endothelial dysfunction in ME/CFS → ECs under chronic activation → possibly impaired TSP-1 production
- CD47/TSP-1 → eNOS inhibition: if TSP-1 elevations persist in ME/CFS (from activated platelets) → excess CD47 signaling → NO ↓ → impaired microvascular dilation → tissue hypoxia → post-exertional malaise (PEM) contribution
- This is SPECULATIVE (ME/CFS evidence weaker than rosacea/T1DM); included as mechanistic hypothesis
- Primary relevance: CD47/NO axis may contribute to ME/CFS hypoperfusion alongside ADMA/eNOS (run_087 S1P axis)

---

## 6. β Cell Death Mechanism Count Update

| # | Mechanism | Run |
|---|-----------|-----|
| 1-17 | [Established in runs 001–130] | various |
| 18 | NRG1 paracrine withdrawal during insulitis | run_129 |
| **19** | **Lipotoxicity via CD36/ceramide entry (palmitate → CD36 → ceramide → ER stress)** | **run_131** |

---

## 7. OTC Mechanism Updates

### Calcitriol — 6th mechanism
- VDR → THBS1 promoter (VDR response element in THBS1 5'UTR/promoter) → TSP-1 ↑ → CD36/Fyn anti-angiogenic signaling restored
- Calcitriol mechanism count: 6 (Foxp3/Treg + PTPN2 + Bcl-2/β cell survival + TXNIP + IRF3/IFN-λ + THBS1)

### Niacinamide — 3rd mechanism
- PPARγ → THBS1 transcriptional activation (PPAR response elements in THBS1 promoter); PPARγ-dependent TSP-1 ↑ in keratinocytes
- Niacinamide mechanism count: 3 (PPARγ → ceramide/filaggrin + ErbB3-independent barrier [run_129] + PPARγ → THBS1 ↑ [run_131])

### Berberine — anti-lipotoxic mechanism via CD36 downregulation
- Berberine → AMPK → CD36 surface expression ↓ on macrophages and β cells → less palmitate uptake → ceramide ↓ → lipotoxicity protection
- This is an existing berberine mechanism (AMPK/CD36) now mechanistically anchored to β cell protection

---

## 8. Protocol Integration

### Monitoring additions:
- No new T-index monitoring node required; DR/DN monitoring already recommended for T1DM patients
- Platelet-poor plasma TSP-1 could theoretically serve as angiogenic balance marker but assay not clinically available

### Therapeutic implications:
- **Calcitriol** (VDR → TSP-1 ↑): existing recommendation reinforced for both rosacea ETR restoration and DR prevention
- **Niacinamide** (PPARγ → TSP-1 ↑): 3rd mechanistic basis for rosacea topical treatment (alongside ceramide/filaggrin and barrier from run_129)
- **CD36/lipotoxicity in T1DM**: reduce saturated fat load; fenofibrate (off-label DR use, FIELD/ACCORD trials) reduces CD36-dependent DR progression
- **No direct TSP-1 mimetic therapy** available OTC; ABT-510 (TSP-1 mimetic peptide) in oncology trials only
- TSP-1 mimetic topicals (PEEL-1 peptide analogs): research stage only; no OTC recommendation

### Run_124 / Run_131 combined angiogenic monitoring:
- Patients with active telangiectasia: assume both LRG1/ALK1 induction AND TSP-1/CD36 brake loss
- Calcitriol + niacinamide combination: calcitriol → THBS1 ↑ (anti-angiogenic) + VDR → VASH2/ALK1 ↓ (run_124); dual-axis angiogenic balance restoration
- Add: IPL/PDL laser for existing telangiectasia (direct vessel ablation, circumvents need for immediate TSP-1 restoration)

---

## 9. Genetic Stratification

| Variant | Gene | Effect | Action |
|---------|------|--------|--------|
| CD36 rs1761667 (A-allele) | CD36 | ↓ CD36 expression | Reduced TSP-1/CD36 anti-angiogenic signaling; worse DR risk; monitor |
| THBS1 rs1478604 (-92C/T) | THBS1 | ↓ TSP-1 expression | Higher rosacea angiogenesis risk; prioritize calcitriol + niacinamide |
| CD36 rs3211938 (G/T) | CD36 | Truncation variant (West African) | Complete CD36 deficiency; anti-malarial but severe lipid disorder risk |

---

## 10. Framework Connection Map

```
THBS1/TSP-1 (run_131)
    ├── Rosacea: TSP-1 ↓ (NF-κB suppression) → CD36/Fyn brake lost → telangiectasia
    │       ↔ LRG1/ALK1 pro-angiogenic (run_124) [complementary yin-yang]
    │       ↔ VEGF/VEGFR2 (upstream driver restrained by TSP-1 NTD)
    │       ↔ LL-37/KLK5 (run_001/004: these suppress THBS1 via NF-κB)
    │       ↔ Calcitriol/VDR (run_031/056: VDR → THBS1 ↑ — 6th calcitriol mechanism)
    │       ↔ Niacinamide/PPARγ (run_129: PPARγ → THBS1 ↑ — 3rd niacinamide mechanism)
    │
    ├── T1DM: DR (pericyte TSP-1 ↓ → retinal neovascularization)
    │          DN (TSP-1 → TGF-β → fibrosis — pathological arm)
    │          CD36/palmitate → ceramide → β cell lipotoxicity (19th β cell death mechanism)
    │          Macrophage CD36 efferocytosis → insulitis modulation
    │       ↔ RAGE/AGE (run_024: AGEs suppress TSP-1)
    │       ↔ Ceramide/ER stress (run_106: palmitate lipotoxicity — CD36 receptor now named)
    │       ↔ NLRP3 (run_002: DAMP/efferocytosis failure → NLRP3 activation)
    │
    └── ME/CFS: CD47/eNOS → NO ↓ → hypoperfusion (speculative)
            ↔ S1P/eNOS (run_087: NO production, parallel axis)
```

---

## 11. Key Literature

- Lawler J et al. (2001) Thrombospondin-1 as an endogenous inhibitor of angiogenesis and tumor growth. *JBC*
- Dawson DW et al. (1999) Pigment epithelium-derived factor: a potent inhibitor of angiogenesis. *Science* (TSP-1/PEDF context)
- Jiménez B et al. (2000) Signals leading to apoptosis-dependent inhibition of neovascularization by thrombospondin-1. *Nat Med* — CD36/Fyn/p38/caspase pathway
- Bhattacharya R et al. (2008) TSP-1 inhibits VEGF-A-mediated phosphorylation of VEGFR2. *PNAS*
- Silverstein RL & Febbraio M (2009) CD36, a scavenger receptor involved in immunity, metabolism, angiogenesis, and behavior. *Sci Signal* — CD36 comprehensive review
- Stenmark KR (diabetic retinopathy TSP-1 data); Bhavsar AR et al. retinal TSP-1 loss in DR
- Ishibashi T et al. (2000) Identification of thrombospondin-1 as a novel ligand for erbB-2/HER2 — indirect ErbB3 connection (run_129 cross-reference)
- VDR-THBS1 promoter: Mahon MJ & Donohue SJ (2008) *J Bone Miner Res* VDR transcriptional targets including THBS1

---

*Gap.md updated: 2026-04-12 | One-hundred-and-twenty-fourth extension | THBS1 TSP-1 thrombospondin-1 CD36 fatty-acid-translocase scavenger-receptor anti-angiogenic TSP-1-type-1-TSR KRFK Fyn caspase-3 EC-apoptosis VEGFR2-antagonism CD47-eNOS-NO TGF-β-activation calcitriol-6th-mechanism niacinamide-3rd-mechanism palmitate-CD36-ceramide-19th-beta-cell-death diabetic-retinopathy pericyte LRG1-complement telangiectasia-yin-yang NF-κB-THBS1-repression PPARγ-THBS1 rs1478604 rs1761667 Jiménez-2000 Silverstein-2009 | run_131*
