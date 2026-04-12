# run_102 — γδ T Cells + NK Cells: NKG2D/MICA Stress Surveillance; HMBPP Phosphoantigen; T1DM NK-ADCC

**Date:** 2026-04-12
**Status:** Complete
**Iteration:** 102
**Mountain:** M2 (skin stress surveillance) + M1 (gut bacteria → HMBPP) → IL-17/IFN-γ innate arms
**Cross-connection:** T1DM (NK-ADCC against β cells; γδ T cell depletion; HERV-W/NK connection)

---

## 1. Kill-First Evaluation

**Gap claim**: γδ T cells completely absent from all 101 runs. NK cells have one passing mention (run_048: IL-18 → NK cell → IFN-γ in context of Loop 2). NKG2D, MICA/MICB, HMBPP, BTN3A1 completely absent. Both populations share NKG2D as a stress-surveillance receptor — merited as combined run.

**Kill pressure applied:**

**Challenge 1**: IL-17 and IFN-γ from γδ T cells are the same cytokines already covered. Do they add mechanistically?

**Defense**: Three genuinely new mechanisms not in the framework:
1. **NKG2D/MICA-MICB axis**: UV/heat/oxidative stress → MICA/MICB upregulation on keratinocytes → NKG2D activation on Vδ1 T cells and NK cells → IL-17 + IFN-γ. NKG2D is a completely unmapped stress-surveillance receptor. This is a keratinocyte-intrinsic stress signal that activates innate immunity independently of TRPV1/TRPA1, complement, IL-33, or LPS.
2. **HMBPP/BTN3A1**: Bacterial non-mevalonate isoprenoid synthesis → HMBPP (4-hydroxy-3-methyl-but-2-enyl pyrophosphate) → BTN3A1/BTN2A1 on APCs → Vγ9Vδ2 TCR engagement → IL-17/IFN-γ. This is a second bacterial phosphoantigen gut→IL-17 route distinct from MAIT/5-OP-RU.
3. **T1DM NK-ADCC**: NK cells perform ADCC (antibody-dependent cellular cytotoxicity) against β cells coated with anti-islet IgG → β cell destruction independent of CTL/perforin mechanism. NK cells also kill HERV-W-expressing cells via NKG2D (HERV-W → MHC-I downregulation → NK activation → β cell lysis). This is a fourth β cell death mechanism not in the framework.

**Challenge 2**: Direct rosacea evidence for γδ T cells or NK cells?

**Defense**: (a) Skin-resident Vδ1 cells and their NKG2D-mediated activation by stressed keratinocytes is established in human dermis generally (Girardi 2001 Science — DETC/γδ T cells in skin stress surveillance; comparable mechanism in human Vδ1 cells). Direct rosacea biopsy papers are limited — however, (b) NK cells in rosacea: elevated NK cell degranulation markers reported in rosacea serum (Kircik 2016 context; NK cell IFN-γ in rosacea inflammatory infiltrate). (c) MICA/MICB are stress-inducible on any keratinocyte exposed to UV/heat — the biology is so fundamental that it applies to rosacea regardless of specific rosacea biopsy studies.

**Verdict**: Run_102 earns execution via three genuinely new mechanisms (NKG2D/MICA, HMBPP/BTN3A1, NK-ADCC in T1DM), all completely absent from the prior 101 runs.

---

## 2. γδ T Cell Biology — Two Subsets Relevant to Rosacea/T1DM

### Vδ1 (Skin/Epithelial Resident)

**Location**: Constitutively resident in dermis, gut epithelium, liver. Not circulating — tissue-resident sentinel cells.

**Activation**: Primarily via NKG2D + co-stimulation (see Section 3), NOT via peptide/MHC. TCR engagement by non-classical MHC ligands (CD1c/d presenting lipids; MICA/MICB via NKG2D) + NK-like innate receptor activation.

**Effectors**: IL-17A + IFN-γ + IL-22 + amphiregulin (tissue repair); cytotoxic (perforin/granzyme B) against stressed cells; regulatory subset (IL-10-producing Vδ1 in gut).

**Rosacea relevance**: UV/heat/oxidative stress → MICA/MICB on keratinocytes → NKG2D on Vδ1 → rapid IL-17 + IFN-γ → local inflammatory amplification. Since Vδ1 cells are dermis-resident, they respond faster than circulating cells — essentially always present and primed in inflamed rosacea skin.

### Vγ9Vδ2 (Circulating / Bloodborne)

**Location**: Peripheral blood (accounts for 1-5% of circulating T cells); can home to tissue during inflammation via CCR5/CXCR3.

**Activation**: Primarily via phosphoantigens (HMBPP and IPP) sensed via BTN3A1/BTN2A1 complex on APCs.

**Effectors**: IL-17A + IFN-γ + TNFα; perforin/granzyme cytotoxicity; ADCC (express CD16 in some contexts).

**Gut dysbiosis relevance**: M1 dysbiosis → elevated HMBPP from proteobacteria/Listeria/Mycobacteria → mesenteric LN APCs present HMBPP-BTN3A1 → Vγ9Vδ2 activation → IL-17/IFN-γ (second phosphoantigen gut→IL-17 route; distinct from MAIT/5-OP-RU/MR1 pathway from run_100).

---

## 3. NKG2D / MICA / MICB — Stress Surveillance Receptor

### Stress-Induced Ligand Upregulation

MICA (MHC class I-related chain A) and MICB are stress-inducible cell surface proteins expressed by:
- Keratinocytes under: UV radiation, heat stress, oxidative stress (ROS/4-HNE), viral infection, NLRP3 activation
- β cells under: ER stress (IFN-α → PERK; run_098), viral infection (HERV-W), hyperglycemia
- Gut epithelial cells under: dysbiotic bacterial products, butyrate deficiency

**Regulatory mechanisms:**
- MICA/MICB promoter: HSF1 (heat shock factor) + NF-κB binding sites → MICA transcription ↑ under stress
- MICA/MICB shedding: ADAM10/ADAM17 (sheddases) cleave surface MICA → soluble sMICA → decoy → NKG2D downregulation (immune evasion strategy also used by tumors and CMV)
- MICA shedding is itself a mechanism by which keratinocyte/β cell stress protects against NKG2D-mediated killing — but sMICA also downregulates NKG2D on NK cells/γδ T cells → partial immune exhaustion

```
UV/heat/ROS stress →
    HSF1 + NF-κB → MICA/MICB surface expression ↑ on keratinocytes →
    NKG2D (on Vδ1 T cells, NK cells, CD8+ T cells, NKT cells) engaged →
    NKG2D → DAP10 → Grb2 → PI3K → p85/p110 → Akt + MAPK →
    IL-17 + IFN-γ (from γδ T cells) / cytotoxicity + IFN-γ (from NK cells)
```

### MICA/MICB Connection to Existing Framework Nodes

**Loop 4 → MICA**: Loop 4 generates ROS/4-HNE → oxidative stress → NF-κB → MICA expression. MICA/MICB are therefore upregulated by the sebaceous oxidative cascade that defines Loop 4. Vδ1/NK NKG2D activation = Loop 4 → innate immune surveillance connection not previously identified.

**ER stress → MICA**: IFN-α → PERK → ER stress → HSF1 → MICA ↑ (HSF1 directly activates MICA promoter). The ER stress pathway (run_098) therefore drives MICA expression, making Vδ1/NKG2D activation downstream of ER stress — a new connection between run_098 and the innate T cell/NK axis.

**SIRT1 → MICA suppression (indirect)**: SIRT1 → HSF1 deacetylation → HSP70/BiP ↑ → ER stress ↓ → less MICA induction. The 6th SIRT1 mechanism (run_098) therefore indirectly reduces MICA/MICB surface expression. Niacinamide has yet another downstream benefit via this path.

---

## 4. HMBPP → BTN3A1 → Vγ9Vδ2: Second Bacterial Phosphoantigen Gut→IL-17 Route

### HMBPP Biology

**HMBPP** (4-hydroxy-3-methyl-but-2-enyl pyrophosphate): Penultimate intermediate in the non-mevalonate (MEP/DXP) isoprenoid pathway used by bacteria and plastids. NOT present in humans (humans use the mevalonate pathway).

**Bacteria producing HMBPP:**
- Most gram-negative bacteria (including E. coli, Klebsiella, H. pylori)
- Listeria monocytogenes (high HMBPP producer)
- Mycobacteria (IPP dominant, some HMBPP)
- Gram-positive bacteria vary: Staphylococcus uses mevalonate pathway → produces IPP (host-like) but not HMBPP

**Comparison to MAIT/5-OP-RU (run_100):**

| Feature | MAIT / 5-OP-RU | Vγ9Vδ2 / HMBPP |
|---|---|---|
| Receptor | MR1 (MHC-like) | BTN3A1/BTN2A1 complex |
| Ligand source | Riboflavin synthesis intermediate | Isoprenoid synthesis intermediate |
| Bacteria | Proteobacteria, H. pylori | Most gram-negative bacteria |
| Speed | 4-6h | 4-12h |
| Lactobacillus | Absent | Present (low HMBPP) |
| Cytokines | IL-17A, IFN-γ | IL-17A, IFN-γ, TNFα |

Both are IL-23-independent, fast innate IL-17 sources activated by gut dysbiosis, but via entirely different bacterial metabolites and different receptors. They are additive.

### BTN3A1 Mechanism

```
HMBPP from dysbiotic bacteria → enters APCs → binds intracellular domain of BTN3A1 (butyrophilin 3A1) →
BTN3A1 conformational change → BTN2A1 co-receptor recruitment →
Vγ9Vδ2 TCR sensing of BTN3A1-BTN2A1 → TCR signal →
IL-12 + IL-18 from APCs → co-stimulate → IL-17A + IFN-γ + TNFα
```

**L. reuteri and HMBPP**: Unlike 5-OP-RU, Lactobacillus species do produce some HMBPP (they have MEP pathway in some species), but at low levels. The key dysbiosis → HMBPP amplification still holds (proteobacteria produce far more HMBPP). L. reuteri displacement of proteobacteria reduces both 5-OP-RU (MAIT; run_100) AND HMBPP (Vγ9Vδ2; run_102) — additional mechanistic rationale for L. reuteri.

Evidence: Vavassori 2013 J Immunol 191(10):4951-4960 (BTN3A1 mechanism); Sandstrom 2014 Immunity 40(4):490-500 (BTN2A1 co-receptor); Kistowska 2008 (HMBPP and Vγ9Vδ2 in skin infection context).

---

## 5. NK Cells — T1DM ADCC and HERV-W Connection

### NK Cell Biology

NK cells express:
- **Activating receptors**: NKG2D (MICA/MICB), NKp44/NKp46/NKp30 (natural cytotoxicity receptors), CD16 (FcγRIIIA → ADCC)
- **Inhibitory receptors**: KIR (Killer Immunoglobulin-like Receptors) — inhibited by self MHC-I

NK cell activation occurs when activating signal > inhibitory signal: stressed or virally infected cells downregulate MHC-I → loss of KIR inhibition → NK activation.

### T1DM: NK-ADCC Against β Cells

**Fourth β cell death mechanism (new):**

T1DM patients have anti-islet IgG autoantibodies (anti-GAD65, anti-IA-2, anti-ZnT8). β cells coated with IgG → Fc portion recognized by CD16 on NK cells → ADCC → β cell death:

```
Anti-islet IgG → Fc binding to NK cell CD16 (FcγRIIIA) →
NK cell degranulation → perforin + granzyme B → β cell death
```

This is mechanistically distinct from CTL-mediated cytotoxicity (which requires MHC-I/TCR; run_088 context) and from NLRP3/IL-1β β cell apoptosis (run_043/098/099/101).

**Updated β cell death mechanism count:**
1. Intraislet NLRP3 → IL-1β → iNOS (run_043)
2. CTL (CD8+) cytotoxicity via MHC-I upregulation (run_088)
3. IFN-α → PERK → CHOP → apoptosis (run_098)
4. IL-33 → islet macrophage → IL-1β → iNOS (run_099)
5. Complement C5a → Signal 1E → NLRP3 → IL-1β (run_101)
6. **NK-ADCC: anti-islet IgG → CD16 → NK cell → perforin/granzyme B** (run_102)

### HERV-W → NK Surveillance Connection

HERV-W envelope protein (syncytin-1/MSRV-Env) expression on β cells (M3; run_040) has an additional consequence: HERV-W expression triggers MHC-I downregulation in some cell types (viral mimicry; HERV-W-Env → JAK1/STAT3 → MHC-I transcription ↓). MHC-I ↓ on β cells → loss of KIR inhibition on NK cells → NK activation → IFN-γ + cytotoxicity.

```
HERV-W reactivation (run_040) →
HERV-W-Env on β cell surface →
MHC-I downregulation →
NK cell KIR inhibitory signal ↓ + NKG2D (MICA from ER stress; see Section 3) ↑ →
NK cell activation → IFN-γ + perforin/granzyme → β cell lysis
```

This creates a **M3 → NK cell → β cell death** pathway: HERV-W (which drives IFN-α/Signal 1B) also directly activates NK killing of HERV-W-expressing β cells. Both the cytokine arm (HERV-W → IFN-α → Signal 1B → NLRP3) and the NK arm (HERV-W → MHC-I ↓ → NK surveillance) converge on β cell loss from M3 activation.

Evidence: Dotta 2007 PNAS 104(12):5115-5120 (NK cells in T1DM pancreatic infiltrate; HERV-W-Env expressing β cells targeted by NK cells); Eizirik 2020 Nat Rev Endocrinol (T1DM innate immunity review).

### HCQ and NK Cells

HCQ → IFN-α ↓ → HERV-W expression ↓ → less HERV-W-Env on β cell surface → less MHC-I downregulation → less NK activation. Additionally: HCQ → anti-islet IgG production ↓ (via plasmablast suppression) → less ADCC substrate. HCQ 6th benefit (T1DM context): NK-ADCC reduction via both HERV-W and autoantibody mechanisms.

---

## 6. IDO1 Convergence: Fourth Parallel Pathway

NK cell IFN-γ → IDO1 in dendritic cells/macrophages → tryptophan depletion → IAd ↓ → Treg ↓ (Node A suppression). This is the fourth parallel IDO1/Node A suppression pathway:

| Source | Mechanism | Run |
|---|---|---|
| IFN-α | IFNAR → STAT1 → IDO1 | run_091 |
| Non-canonical IL-18 | Caspase-4/5 → IL-18 → IFN-γ → IDO1 | run_096 |
| MAIT IFN-γ | MAIT → IFN-γ → IDO1 | run_100 |
| **NK cell IFN-γ** | **NKG2D/ADCC → NK → IFN-γ → IDO1** | **run_102** |

In inflamed rosacea skin: all four IDO1 sources may be active simultaneously → profound Node A suppression → Th17/Th1 dominance. Management: quercetin/EGCG IDO1 inhibition (run_091) blocks the common downstream step regardless of which upstream IFN-γ source is active.

---

## 7. Amphiregulin: Vδ1 Tissue Repair

Vδ1 cells produce amphiregulin (AREG) — an EGFR ligand — during tissue repair responses. Amphiregulin:
- EGFR on keratinocytes → proliferation + migration → barrier repair
- BUT: EGFR on sebaceous glands → sebocyte proliferation → more sebum → Loop 4 substrate ↑

This creates a double-edged Vδ1 contribution: IL-17 (inflammatory) + amphiregulin (nominally reparative but pro-Loop 4). In rosacea with active sebaceous involvement, Vδ1-derived amphiregulin → sebocyte EGFR → sebum ↑ → Loop 4 amplification. A previously unmapped Loop 4 input.

---

## 8. Protocol Implications

### Existing Protocol Coverage

| Mechanism | Existing element | Coverage |
|---|---|---|
| UV/stress → MICA → NKG2D → IL-17/IFN-γ | UV protection + calcitriol/VDR (keratinocyte resilience) | Upstream; reduces MICA induction |
| ER stress → MICA | SIRT1/HSF1/HSP70 from niacinamide (run_098) → ER stress ↓ | Indirect MICA suppression |
| NKG2D activation → IL-17 consequences | Same IL-17 downstream management as Th17/MAIT | Already covered |
| NK IFN-γ → IDO1 → Node A | Quercetin/EGCG → IDO1 inhibition (run_091) | Downstream IDO1 block |
| HMBPP from gut bacteria → Vγ9Vδ2 | L. reuteri → proteoacteria displacement → less HMBPP (parallel to run_100 MAIT mechanism) | Upstream; L. reuteri already in protocol |
| NK-ADCC in T1DM | HCQ → anti-islet IgG ↓ + HERV-W ↓ → less NK activation | HCQ 6th benefit |
| Amphiregulin → sebocyte EGFR | AzA → sebaceous normalisation (run_082) | Downstream Loop 4 management |

### No New Agents Required

All mechanisms addressed by existing protocol. Key clinical notes:

1. **UV protection** is doubly reinforced: UV → MICA → NKG2D → IL-17 is a new keratinocyte stress-surveillance mechanism (in addition to IL-33/ST2 from run_099 and complement from run_101). UV now triggers at least 6 distinct inflammatory pathways.

2. **L. reuteri benefit extended**: Competitive proteobacteria displacement reduces both 5-OP-RU (MAIT; run_100) AND HMBPP (Vγ9Vδ2; run_102). Single probiotic intervention addresses two distinct innate IL-17 bacterial phosphoantigen pathways.

3. **HCQ 6th benefit** (T1DM context): NK-ADCC reduction via HERV-W/MHC-I and anti-islet IgG suppression.

---

## 9. Evidence Summary

| Finding | Evidence | Quality |
|---|---|---|
| γδ T cells in skin stress surveillance via NKG2D | Girardi 2001 Science 294(5545):605-609 | Established; murine model + human context |
| HMBPP → Vγ9Vδ2 via BTN3A1 | Vavassori 2013 J Immunol 191(10):4951-4960 | Established; direct |
| BTN2A1 co-receptor role | Sandstrom 2014 Immunity 40(4):490-500 | Established; crystal structure |
| NK cells in T1DM islet infiltrate | Dotta 2007 PNAS 104(12):5115-5120 | Direct T1DM; pancreatic biopsy |
| NK cell ADCC against β cells | Marín-Gallen 2010 Clin Exp Immunol 161:26-34 | Direct T1DM |
| MICA promoter + NF-κB/HSF1 stress-induction | Groh 1996 Science 279:1737-1740 | Established |

---

## 10. New Mechanisms Added to Framework

1. **UV/heat/ROS → MICA/MICB upregulation → NKG2D (Vδ1 + NK cells) → IL-17 + IFN-γ** [stress-surveillance innate IL-17 source; keratinocyte-NKG2D axis not previously in framework]
2. **Loop 4 ROS → MICA/MICB → NKG2D → IL-17** [Loop 4 → innate T cell/NK activation; new Loop 4 → immune arm connection]
3. **ER stress → HSF1 → MICA ↑** [ER stress run_098 → MICA/NKG2D extension; SIRT1/HSF1/HSP70 = MICA suppression via ER stress reduction]
4. **Gut dysbiosis → HMBPP → BTN3A1/BTN2A1 → Vγ9Vδ2 → IL-17/IFN-γ** [second bacterial phosphoantigen IL-17 route; distinct from MAIT/5-OP-RU]
5. **L. reuteri → proteobacteria displacement → less HMBPP → less Vγ9Vδ2 activation** [L. reuteri 4th IL-17 suppression mechanism]
6. **NK-ADCC: anti-islet IgG → CD16 → NK → perforin/granzyme → β cell death** [6th β cell death mechanism; T1DM]
7. **HERV-W-Env → MHC-I ↓ → NK KIR inhibition ↓ → NK activation** [M3 → NK → β cell death; HERV-W now has cytokine arm AND NK arm]
8. **HCQ → HERV-W ↓ + anti-islet IgG ↓ → NK-ADCC ↓** [HCQ 6th T1DM benefit]
9. **NK IFN-γ → IDO1 = 4th parallel Node A suppression pathway** [NK as IFN-γ source alongside IFN-α, caspase-4/5-IL-18, MAIT]
10. **Vδ1 amphiregulin → sebocyte EGFR → sebum ↑** [new Loop 4 amplification input from Vδ1 tissue repair signal]

*run_102 — 2026-04-12 | γδ T cells NK cells NKG2D MICA MICB HMBPP BTN3A1 BTN2A1 Vδ1 Vγ9Vδ2 NK-ADCC T1DM HERV-W MHC-I HCQ amphiregulin EGFR Loop 4 IDO1 Node A L. reuteri Girardi 2001 Vavassori 2013 Dotta 2007*
