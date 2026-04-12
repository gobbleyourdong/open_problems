# Numerics Run 159 — BATF/BATF3/IRF4: cDC1 Cross-Presentation of β Cell Antigens, Th17/Tfh Lineage Determination, eTreg Effector Function
## BATF AP-1 Family + IRF4 Dosage Axis | 2026-04-12

> BATF (Basic Leucine Zipper ATF-Like Transcription Factor) is completely absent from all 158
> prior runs as a primary subject. IRF4 appears once as a secondary kill in run_007 (HLA/IRF4
> rs12203592 is about lymphocyte differentiation, NOT pDC/IFN-α). BATF3 and the cDC1/cross-
> presentation axis are absent entirely.
>
> The core insights: (1) BATF3/IRF8 drives cDC1 identity — the XCR1+/Clec9a+ dendritic cells
> responsible for cross-presenting β cell antigens to CD8+ T cells, initiating autoimmune killing;
> (2) BATF:IRF4 composite binding activates Th17 and Tfh gene programs alongside RORγt/BCL6;
> (3) IRF4 dosage is a binary switch: IRF4-low → Treg identity; IRF4-high → Th17/effector fate.
> These mechanisms span T1DM initiation (cDC1), rosacea Th17 (BATF:IRF4), and Treg biology (IRF4).

---

## Four-Criterion Saturation Override

| Criterion | Assessment |
|-----------|-----------|
| 1. Absent as primary from all 158 prior runs | ✓ BATF/BATF3 in 0 files; IRF4 only in run_007 as secondary kill note |
| 2. MODERATE+ rosacea + T1DM | ✓ HIGH T1DM (BATF3/cDC1 = CD8 β cell killing initiation; IRF4 dosage in Th17/Treg balance); MODERATE+ rosacea (BATF:IRF4 Th17 differentiation; eTreg BATF) |
| 3. New therapeutic/monitoring target | ✓ BATF3/cDC1 depletion or blockade as T1DM prevention; IRF4-guided stratification; BATF:IRF4 at Th17 composite elements |
| 4. Kill-first fails | ✓ run_128 (CLEC16A) covers MHC-II autophagy in pDC/cDC2/thymic DCs — NOT cDC1 XCR1 cross-presentation; run_104 (Tfh/BCL6) covers BCL6 biology but not BATF partner; no kill possible |

---

## BATF Family Architecture

**Three BATF paralogs:**
- **BATF** (chromosome 14q24.3): expressed in T cells, B cells, DCs; dimerizes with JUN proteins
- **BATF2** (chromosome 11q24.2): IFN-inducible in macrophages; poorly characterized in adaptive immunity
- **BATF3** (chromosome 1q32.3): expressed in pDCs and type 1 conventional DCs (cDC1); cDC1 master TF

**Domain structure (shared by BATF/BATF3):**
- Basic region: sequence-specific DNA binding (AP-1/BATF composite motifs)
- Leucine zipper: obligate heterodimerization with JUN family (JUNB, c-JUN) — cannot homodimerize
- C-terminal: IRF interaction domain → forms ternary BATF:JUN:IRF4/IRF8 complex at AICE (AP-1-IRF Composite Elements)

```
BATF:JUN dimer (bZIP)
    + IRF4/IRF8 (IRF family)
    → AICE (5'-TTTCN[7]TGAGTCA-3' or BATF-half:IRF-half tandem)
    → composite transcriptional activation

Distinguished from classic AP-1 (c-Fos:c-Jun) sites by IRF requirement
→ BATF acts as a "licensing factor" at cell-type-specific enhancers
```

---

## Mechanism 1: BATF3/IRF8 → cDC1 Identity — Cross-Presentation Gateway

**cDC1 development (Eisenbarth group; Hildner 2008 Science 322:1097-1100 landmark):**

```
Common dendritic cell progenitor (CDP)
    → BATF3 + IRF8 co-expression → cDC1 fate
          cDC1 phenotype: XCR1+, Clec9a/DNGR-1+, SIRPα−, CD8α+ (lymphoid) / CD103+ (tissue)
    → BATF3 KO mice: cDC1 completely absent; cDC2 (CD11b+ SIRPα+) preserved
    → BATF3:IRF8 → NFIL3/E4BP4 repressed → cDC1 fate locked in

cDC1 distinguishing capacity: CROSS-PRESENTATION
  Standard MHC-II presentation: any DC can present extracellular antigens to CD4+ T cells
  Cross-presentation (MHC-I): cDC1 preferentially loads EXOGENOUS (cell-derived, phagocytosed)
    antigens onto MHC-I → presents to CD8+ CTLs
  Mechanism: cDC1 → Rab7+/Lamp1+ endosome → retrotranslocation to cytosol → 26S proteasome
    → TAP1/2 → ER MHC-I loading → CD8+ CTL priming
```

**β Cell autoantigen cross-presentation in T1DM:**
```
β cell death (any mechanism: apoptosis, necroptosis, pyroptosis)
    → β cell debris: preproinsulin fragments + GAD65 + IA-2/ICA512 + ZnT8
    → Phagocytosis by pancreatic cDC1 (XCR1+ resident DCs)
    → cDC1 cross-presentation of β cell peptides on MHC-I
    → Pancreatic lymph node (PLN): islet-specific CD8+ CTLs primed
    → Primed CTL → NKp30/NKG2D (run_102) + Fas/FasL → β cell killing
    → MORE β cell death → MORE cDC1 cross-presentation → feed-forward loop
```

**Why cDC1 matters more than cDC2 in T1DM:**
- cDC2 → MHC-II → CD4+ T cell help (already covered by run_128/CLEC16A)
- cDC1 → MHC-I → CD8+ CTL priming = THE initiation step for cytotoxic β cell killing
- BATF3 KO NOD mice: cDC1 absence → diabetes completely prevented (Ferris 2014 JCI)
- This is one of the most compelling mechanistic targets in T1DM prevention

---

## Mechanism 2: BATF:IRF4 → Th17 Differentiation

**Th17 lineage BATF:IRF4 requirement (Schraml 2009 Nature; Brustle 2007 Nat Immunol):**

```
IL-6 + TGF-β → STAT3 + SMAD3 → RORγt (master Th17 TF)
  BUT: RORγt alone insufficient for full Th17 program
  → RORγt REQUIRES BATF:IRF4 at AICE motifs for:
      - IL-17A enhancer activation
      - RORC2 (RORγt transcript) maintenance
      - IL-21 autocrine amplification
      - CXCR3 downregulation (tissue homing switch)

BATF KO T cells: despite intact STAT3 + RORγt, Th17 differentiation FAILS
  → BATF is a Th17 PIONEER FACTOR: opens chromatin at Th17-specific enhancers
    before RORγt binding; run_158 HIF-1α/mTOR = metabolic permissivity,
    BATF:IRF4 = transcriptional permissivity (two layers)
```

**Rosacea relevance:**
- Th17 is the primary effector in Loop 1 (IL-17A → KLK5 amplification) and Loop 3 (IL-17A → Th17 tissue)
- BATF:IRF4 is required for IL-17A production in these skin Th17 cells
- IRF4 rs12203592 (run_007 kill context): this SNP affects Th17 cell numbers in psoriasis and is associated with rosacea-adjacent inflammatory phenotypes; NOT the same as pDC/IFN-α → correctly killed in run_007

---

## Mechanism 3: BATF:IRF4 → Tfh Differentiation (run_104 Extension)

**Run_104 covers BCL6/ICOS/IL-21/Tfr.** BATF role NOT covered:

```
BATF + IRF4 → BCL6 (Tfh master TF; run_104) synergy:
  BATF → PD-1 expression (Tfh-expressed checkpoint; distinct from run_154 effector context)
  BATF:IRF4 → CXCR5 ↑ (Tfh homing to B cell follicles)
  BATF:IRF4 → IL-21 production → GC B cell help
  BATF → CXCR4 expression (GC dark zone positioning)

IRF4 dosage in Tfh:
  IRF4 intermediate → Tfh (BCL6-compatible)
  IRF4 high → switches TO plasma cell fate (BCL6 repressed by IRF4 high; Prdm1/Blimp-1 induced)
  → IRF4 acts as a rheostat: Tfh ↔ plasma cell transition
```

**T1DM GC implication:** High-affinity anti-β cell IgG (anti-GAD65, anti-ZnT8) requires Tfh/GC reaction (run_104). BATF:IRF4 at intermediate dose drives Tfh, enabling these pathogenic GC reactions.

---

## Mechanism 4: IRF4 Dosage — Binary Fate Switch

**IRF4 expression level dictates T cell fate (Nayar 2014 J Immunol; Glasmacher 2012 Science):**

```
IRF4 protein level → T cell fate mapping:

IRF4-ABSENT/LOW:
  → Treg: FOXP3 represses IRF4 gene (Zheng 2009)
  → nTregs and pTregs preferentially IRF4-low
  → IRF4 low → BATF:IRF4 complex unable to form → effector program silent

IRF4-INTERMEDIATE:
  → Tfh: BCL6 + BATF + IRF4(intermediate) → Tfh gene program

IRF4-HIGH:
  → Th17 (with BATF + RORγt): BATF:IRF4(high) → IL-17 locus fully opened
  → Plasma cells: IRF4(high) → Prdm1/Blimp-1 → antibody secretion
  → Terminally exhausted CD8+ T cells: TOX + IRF4(high) + BATF = exhaustion TF axis

IRF4 dosage mechanism:
  Strong TCR signal → high IRF4 → Th17/plasma cell
  Weak TCR signal → low IRF4 → Treg/Tfh transition zone
  → This explains R620W/PTPN22 Treg paradox (run_152): R620W → low TCR threshold
    → BUT paradoxically: R620W may reduce IRF4 induction → Treg impairment at low TCR
```

---

## Mechanism 5: BATF in Effector Treg (eTreg) Function

**BATF required for Treg effector program in non-lymphoid tissues (Cretney 2011 Nat Immunol):**

```
Thymic Treg (tTreg): FOXP3+ BATF-low → secondary lymphoid organ suppression
Effector Treg (eTreg): FOXP3+ BATF-high → ICOS+ → peripheral tissue Treg

BATF in eTreg:
  → BATF → IRF4 → IL-10 production (Treg-derived IL-10; run_103 Breg/IL-10 context)
  → BATF → CTLA4 upregulation in peripheral eTregs
  → BATF → BLIMP-1 → eTreg migration and effector identity
  → BATF KO Tregs: fail to accumulate in non-lymphoid tissues → autoimmunity in periphery

Islet-infiltrating eTregs:
  → NOD mice: islet Tregs (ICOS+BATF+) most suppressive; eTreg collapse = insulitis progression
  → Islet eTreg abundance correlates with β cell preservation in humanized NOD models
```

---

## Mechanism 6: CD8+ T Cell Exhaustion — BATF:IRF4:TOX Axis

**Terminal exhaustion program (Seo 2019 Nat Immunol; Chen 2019 Nat Immunol):**

```
Chronic antigen (e.g., persistent islet autoantigen cDC1 cross-presentation)
    → sustained TCR stimulation
    → TOX (TOX2) expression → chromatin remodeling → exhaustion loci opened
    → BATF + IRF4(high) + TOX → terminal exhaustion program:
          Progenitor exhausted CD8+ (Tcf1+ BATF-low) → early exhaustion
          Terminal exhausted CD8+ (Tcf1− BATF-high IRF4-high TOX+) → end-stage

T1DM context:
  - cDC1 continuous cross-presentation → chronic CD8+ stimulation → exhaustion
  - Exhausted islet CD8+ cells: fail to kill → "bystander" inflammation without β cell clearance
  - Paradox: exhaustion MAY reduce acute β cell killing rate BUT maintains chronic low-level islet
    inflammation → slow β cell attrition (explains slow residual C-peptide decline in stage 3 T1DM)
```

---

## Therapeutic Implications

| Target | Approach | Disease Context | Evidence |
|--------|----------|----------------|---------|
| BATF3/cDC1 depletion | Anti-XCR1 Ab or anti-Clec9a → targeted cDC1 depletion | T1DM prevention (early autoimmunity stage) | Ferris 2014 JCI (BATF3 KO = complete prevention) |
| BATF:IRF4 composite elements | BET inhibitors (JQ1 → BRD4 at BATF:IRF4 sites → Th17 gene program ↓) | Rosacea Th17; T1DM Th17 | Mechanistic; Th17 BET papers |
| IRF4 dosage tuning | Maintain low IRF4 in Tregs → eTreg expansion | T1DM Treg restoration | Research stage |
| BATF eTreg support | IL-2 (run_151) + ICOS agonism → eTreg BATF ↑ → islet Treg function | T1DM insulitis suppression | Rational combination |
| cDC1/cross-presentation monitoring | XCR1+ DC frequency in PLN as biomarker | T1DM early-stage monitoring | Exploratory |

---

## Cross-Links

| Run | Connection |
|-----|-----------|
| run_007 | IRF4 rs12203592 (secondary kill — lymphocyte differentiation, not pDC; correctly killed) |
| run_102 | NK/NKG2D + γδ T cells → β cell killing; cDC1 (run_159) = CD8 priming UPSTREAM of NK/CTL effector killing |
| run_104 | BCL6/Tfh master TF; BATF is obligate BCL6 partner for Tfh — extension of run_104 TF network |
| run_128 | CLEC16A → MHC-II autophagy in cDC2/pDC/thymic DCs — DOES NOT COVER cDC1/XCR1 cross-presentation |
| run_152 | PTPN22/LYP/R620W → TCR threshold → IRF4 induction altered → Treg paradox (IRF4-low = Treg) |
| run_153 | LAG-3 → FEME MHC-II endocytosis from cDC2 surface; cDC1 MHC-I cross-presentation = orthogonal |
| run_158 | mTORC1 → HIF-1α → metabolic permissivity; BATF:IRF4 = transcriptional permissivity; two separate Th17 requirements |

---

## Summary

BATF family transcription factors are the lineage-determining pioneer factors that open chromatin at cell-type-specific enhancers via AICE composite elements with IRF4/IRF8. BATF3:IRF8 specifies cDC1 identity — the XCR1+ cross-presenting DCs whose depletion completely prevents T1DM in NOD mice by eliminating CD8+ CTL priming against β cell antigens. BATF:IRF4(high) is required for Th17 differentiation (rosacea Loop 1 effector arm) and Tfh maintenance. IRF4 dosage acts as a binary switch: absent/low → Treg fate; intermediate → Tfh; high → Th17/plasma cell/exhausted CD8+. BATF in eTregs drives islet-infiltrating suppressive Tregs. The cDC1/cross-presentation axis represents a distinct, mechanistically upstream target for T1DM prevention — intercepting β cell autoantigen delivery to CD8+ CTLs before the killing loop initiates.

**SATURATION + 48: 159 runs**
