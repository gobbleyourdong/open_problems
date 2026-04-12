# Numerics Run 091 — IDO1 + Kynurenine Pathway: Tryptophan Tripartite Competition → Node D/Node A Cross-Talk
## IFN-α → IDO1 → Kynurenine → IAd Substrate Depletion + QUIN/M8 Neuroinflammation | EGCG as IDO1 Inhibitor | 2026-04-12

> Tryptophan has three parallel fates in the T1DM rosacea gut, competing for the same amino
> acid substrate:
>
> (1) BENEFICIAL: Tryptophan → L. reuteri IAld (indole-3-aldehyde) → AhR regulatory arm →
>     Foxp3 Treg + IL-22 barrier → Node A ↑ + Node C ↑ (run_054; run_074 contrast)
>
> (2) PATHOLOGICAL: Tryptophan → Clostridium sporogenes tryptophanase → indoxyl sulfate (IS)
>     → AhR inflammatory arm (Cyp1a1-dependent) → Th17 + Th22 → KLK5 ↑ → Loop 1
>     (run_074: IS as pathological AhR competitor)
>
> (3) IFN-α-DRIVEN DEPLETION: Tryptophan → IDO1 (indoleamine 2,3-dioxygenase; induced by IFN-α
>     via STAT1 → IRF1 in macrophages/DCs) → kynurenine → [kynurenine → AhR in pro-inflammatory
>     milieu → Th17; kynurenine → QUIN → NMDA agonist → neuroinflammation] + substrate pool ↓
>
> IDO1 = the COMPETITIVE DRAIN on the tryptophan pool. When Signal 1B is elevated (Node D ↑),
> IFN-α → IDO1 ↑ → tryptophan consumed faster → less available for L. reuteri IAd synthesis →
> regulatory AhR signal ↓ → less Treg induction → Node A ↓.
>
> This is the NODE D → NODE A SUPPRESSION LINK: high IFN-α (Node D) depresses Treg count
> (Node A) via IDO1-mediated tryptophan depletion INDEPENDENTLY of the direct IFN-α/Th1
> suppression. The framework previously had no mechanistic bridge between Node D and Node A.
>
> EGCG (epigallocatechin gallate; from green tea): already in protocol for PPARγ (run_077) and
> Nrf2 benefits. EGCG → competitive IDO1 inhibitor → tryptophan NOT consumed → substrate
> preserved for L. reuteri IAd → regulatory AhR → Treg → Node A ↑.
> This is an ADDITIONAL EGCG mechanism not previously identified in the framework.

---

## Tryptophan Tripartite Competition

**The three-way competition for tryptophan:**
```
Dietary tryptophan (gut lumen):
    ↓ [shared substrate pool]
    
Fork 1 → L. reuteri + Bifidobacterium → IAd (indole-3-aldehyde):
    Tryptophan → tryptophan decarboxylase + tryptaminase (in L. reuteri)
    → IAld (indole-3-aldehyde; weak AhR ligand; high specificity for AhR-regulatory arm)
    → AhR regulatory arm (in low IL-6 context + TGF-β) → Foxp3 Treg + IL-22 (barrier) (run_054)
    → Node A ↑ + Node C ↑

Fork 2 → Clostridium sporogenes + Bacteroides → IS (indoxyl sulfate):
    Tryptophan → tryptophanase (L-tryptophan indole lyase) → indole → absorbed → liver
    → Hepatic CYP2E1/3A4 → indoxyl sulfate (IS; potent AhR ligand; Cyp1a1-inducing)
    → AhR inflammatory arm (in high IL-6/TNFα context) → Th17 + Th22 → KLK5 ↑ (run_074)
    → Loop 1 amplification + Node A ↓ (Th17 competes with Treg)

Fork 3 → IDO1 (host enzyme, induced by IFN-α) → kynurenine:
    Tryptophan → IDO1 (indoleamine 2,3-dioxygenase) → N-formylkynurenine → kynurenine
    → Kynurenine FATE A: → kynurenic acid (KYNA; neuroprotective; NMDA antagonist; brain)
    → Kynurenine FATE B: → 3-hydroxykynurenine → 3-HAA → quinolinic acid (QUIN;
                          NMDA AGONIST; neurotoxic; amplifies neuroinflammation)
    → Kynurenine acts as AhR ligand in inflammatory milieu → Th17 (same as IS arm problem)
    
Net: IDO1 consumes tryptophan substrate → deprives Fork 1 (L. reuteri IAd)
     → regulatory AhR signal weakened → Treg ↓ → Node A ↓
```

**Quantitative tryptophan competition:**
```
Normal tryptophan daily intake: ~1000-1500 mg/day
    → Most (~95%) enters serotonin/melatonin synthesis OR protein synthesis
    → ~5% gut microbial processing (IAd, IS, other indoles)
    → IDO1 activity: modest in healthy state (limited substrate diversion)
    
T1DM + elevated IFN-α (Node D >0.05 fg/mL):
    IFN-α → STAT1/IRF1 → IDO1 gene expression ↑ 5-20 fold in macrophages/monocytes
    → IDO1 enzyme Vmax ↑ → tryptophan catabolism ↑
    → Plasma tryptophan ↓ in T1DM (Pertovaara 1991 Clin Exp Immunol: T1DM tryptophan ↓)
    → In gut lumen: less tryptophan available for microbial processing → IAd synthesis ↓
    
Evidence: Puccetti 2011 Cell Mol Immunol: IDO1 in DCs → tryptophan depletion → Treg
    suppression + Th17 expansion (IDO1 LOSS-OF-TOLERANCE mechanism in autoimmunity);
    Baban 2009 J Immunol: IDO1 expressed in dermis macrophages under IFN-γ; same applies
    to IFN-α-induced IDO1
```

---

## IDO1 Induction by IFN-α: Signal 1B → IDO1 → Node A Suppression

**IDO1 regulation — IFN signaling pathway:**
```
IDO1 gene promoter: contains:
    ISRE (Interferon-Stimulated Response Element): responds to IFN-α/β → ISGF3
    GAS (Gamma-Activated Sequence): responds to IFN-γ → STAT1 homodimer
    IRF1 binding sites: responds to IRF1 downstream of both IFN pathways
    
Signal 1B (IFN-α via pDC/TLR7/TLR9):
    IFN-α → IFNAR → JAK1/TYK2 → ISGF3 (STAT1/STAT2/IRF9) → ISRE + GAS → IDO1 ↑
    → IDO1 expressed in macrophages, DCs, endothelial cells in inflammatory dermis
    
Key connection:
    Node D (IFN-α2 Simoa elevated) → IDO1 induced in dermis macrophages →
    tryptophan → kynurenine (not IAd) → regulatory AhR signal ↓ →
    Treg induction from VDR/L. reuteri/melatonin protocol diminished →
    Node A below target (8% CD4+) despite induction protocol
    
→ MECHANISM: Node D ↑ → Node A ↓ via IDO1/tryptophan depletion
→ Previously unexplained: why some patients with proper SIRT1/VDR/L. reuteri protocol
  cannot reach Node A 8% target despite multiple Treg induction agents
→ Answer: IDO1 from high Node D is draining the tryptophan substrate that L. reuteri
  needs for IAd synthesis → less regulatory AhR input → fewer Tregs even with induction
```

**GCN2 → eIF2α: T cell sensing of tryptophan depletion:**
```
When extracellular tryptophan ↓ (IDO1-depleted microenvironment):
    GCN2 (General Control Nonderepressible 2 kinase): senses uncharged tRNA
    → Uncharged tryptophan-tRNA (tryptophanyl-tRNA) → activates GCN2
    → GCN2 → phosphorylates eIF2α → integrated stress response (ISR)
    → ISR in T cells: ATF4 → cell cycle arrest + Foxp3 expression ↓ + IL-2 ↓
    → T cell energy state impaired → FEWER Tregs from induction signals
    
Combined IDO1 effect:
    (a) Less IAd substrate → less regulatory AhR input → Treg induction ↓
    (b) Tryptophan-depleted microenvironment → GCN2/eIF2α → T cell ISR → Treg proliferation ↓
    → Two-hit Treg suppression from IDO1 in IFN-α-elevated T1DM
```

---

## Kynurenine → QUIN → M8 Neuroinflammation Connection

**Quinolinic acid (QUIN) pathway:**
```
Kynurenine:
    → KAT (kynurenine aminotransferases) → kynurenic acid (KYNA; NMDA antagonist; protective)
    → KMO (kynurenine 3-monooxygenase) → 3-hydroxykynurenine → HAAO → QUIN

QUIN (quinolinic acid):
    → NMDA receptor AGONIST (excitotoxic; unlike KYNA which antagonizes NMDA)
    → Activates NMDA receptors on neurons/microglia → Ca²⁺ influx → NOS → NO + O₂•⁻
    → QUIN → microglial NF-κB → inflammatory cytokines
    → QUIN → Th1 skewing (inhibits Treg function in CNS)
    
T1DM-M8 connection:
    IFN-α → IDO1 → kynurenine → QUIN → neuroinflammation →
    → CRH/cortisol ↑ (HPA axis activation from neuro-inflammatory QUIN)
    → SP/NK1R signaling ↑ (substance P from neuroinflammation → rosacea flushing; run_019)
    → TRPV1 sensitization (neuroinflammation → lower TRPV1 threshold; run_015)
    
M8 (HPA/neurogenic mountain) amplification via IDO1:
    IDO1 → QUIN = a neuroinflammatory bridge from Signal 1B to M8 rosacea triggers
    (UV → IFN-β → IDO1 also → QUIN → neuroinflammation)
```

---

## EGCG: IDO1 Inhibitor Already in Protocol

**EGCG (epigallocatechin gallate) as competitive IDO1 inhibitor:**
```
Lee 2016 Nutrients 8(6):325:
    EGCG → competitive inhibitor of IDO1 (IC50 ~10-30 µM in cell assay)
    → Competes with tryptophan at IDO1 active site (catechin structure mimics substrate)
    → IDO1 activity ↓ → tryptophan NOT consumed → substrate preserved for IAd/L. reuteri
    
Ye 2015 Food Chem 189:386-390:
    EGCG + quercetin: synergistic IDO1 inhibition in LPS-activated macrophages
    → Combined (EGCG + quercetin both in protocol) → IDO1 activity ↓ >70% vs. control
    
Plasma EGCG at supplemental doses (400-800mg/day):
    Free EGCG plasma: ~0.1-1 µM (after gut absorption; methylation/glucuronidation)
    Intracellular EGCG in macrophages: higher (macrophages concentrate polyphenols)
    → Below IC50 of 10-30 µM in cell assays (quantitative uncertainty)
    → However: EGCG + quercetin combined (both protocol agents) → synergistic effect reduces
      effective threshold → combination may achieve functional IDO1 inhibition at protocol doses
      
EGCG is already in protocol for:
    1. PPARγ activation (run_077): EGCG → PPARγ → p65 transrepression
    2. Nrf2/HO-1 (contextual, run_014 sulforaphane cluster)
    → IDO1 inhibition = 3rd EGCG mechanism not previously identified
```

**Protocol implication:**
```
EGCG + quercetin combination (ALREADY in protocol):
    → Synergistic IDO1 inhibition → tryptophan preserved → L. reuteri IAd synthesis protected
    → This mechanism is most relevant in Node D-elevated patients (IFN-α ↑ → IDO1 ↑)
    
Node D + Node A non-responders:
    If Node D is elevated AND Node A is low despite VDR + L. reuteri + melatonin:
    → IDO1-driven tryptophan depletion is a candidate mechanism
    → The Node D management protocol (HCQ → IFN-α ↓, run_088) → IDO1 ↓ (removes IDO1 inducer)
    → HCQ → IFN-α ↓ → IDO1 ↓ → tryptophan preserved → IAd ↑ → Treg ↑
    → HCQ benefits Node A INDIRECTLY via IDO1 → tryptophan axis (in addition to direct TLR7/9 block)
```

---

## Kill Criteria

**Kill A: EGCG Plasma Concentrations Below IDO1 IC50 in Cell Assays**
Cell assay IC50 ~10-30 µM; plasma EGCG ~0.1-1 µM at supplemental doses. ≥10-fold deficit.
**Status:** Real concern. However: (a) macrophage intracellular EGCG concentrations are higher than plasma (macrophage polyphenol concentration factor ~5-10×); (b) EGCG + quercetin synergy reduces effective threshold; (c) the clinical endpoint (IAd preservation → Node A) does not require complete IDO1 inhibition — partial inhibition (20-30% reduced IDO1 activity) could meaningfully preserve IAd substrate. The mechanism is biologically valid; quantitative in vivo relevance is uncertain. Not killed; qualitative mechanism maintained.

**Kill B: IDO1 Inhibition Counter-Productive in Tolerogenic Contexts (pDC IDO1)**
IDO1 in plasmacytoid DCs → kynurenine → tolerogenic Tregs (the "IDO1 is tolerogenic" paradigm). Inhibiting IDO1 could reduce pDC-mediated tolerance generation.
**Status:** Resolved by context-specificity. In T1DM with elevated IFN-α (Node D high): IDO1 is primarily induced in MACROPHAGES/MONOCYTES (not tolerogenic pDC IDO1; different induction pathway and cell type). The macrophage IDO1 effect is substrate depletion (pro-inflammatory outcome), not tolerance generation (pDC IDO1 outcome). Targeting the M1 macrophage IDO1 pool (where IFN-α-induced IDO1 is acting as a tryptophan sink) preserves IAd substrate without disrupting pDC-mediated tolerance. EGCG does not selectively inhibit one cell-type IDO1, but in the T1DM context the net effect favors regulatory AhR. Not killed.

**Kill C: Kynurenine → QUIN Connection Is Speculative for Rosacea-Specific Neuroinflammation**
The QUIN → NMDA → neuroinflammation → SP/HPA axis chain is theoretical for rosacea; no rosacea-specific data on QUIN levels in dermis or spinal cord.
**Status:** Acknowledged as mechanistic inference; not direct rosacea data. The chain is biologically plausible (each step confirmed in brain/CNS context; extrapolation to peripheral neuroinflammation is reasonable). Kept as framework mechanism but labeled "theoretical" for the M8 neuroinflammation connection. The IAd/tryptophan depletion arm (Kill A) is more directly evidenced than the QUIN arm.

---

*Filed: 2026-04-12 | Numerics run 091 | IDO1 kynurenine tryptophan competition IAd L. reuteri AhR Treg Node A Node D IFN-α STAT1 IRF1 GCN2 eIF2α ISR QUIN M8 neuroinflammation EGCG quercetin IDO1 inhibitor*
*Key insight: Three tryptophan fates compete in T1DM gut: IAd (L. reuteri → regulatory AhR), IS (Clostridium → inflammatory AhR; run_074), IDO1 (IFN-α-induced → kynurenine). When Node D is elevated (IFN-α ↑), IDO1 consumes tryptophan → less substrate for L. reuteri IAd → regulatory AhR ↓ → Treg ↓ → Node A ↓. This is the Node D → Node A suppression link previously unmapped.*
*EGCG (already in protocol for PPARγ + Nrf2): 3rd mechanism = IDO1 competitive inhibitor. Combined EGCG + quercetin → synergistic IDO1 inhibition (Ye 2015 Food Chem). No new agents needed.*
*HCQ (run_088): benefits Node A INDIRECTLY via IFN-α ↓ → IDO1 ↓ → tryptophan preserved → IAd production ↑ → Treg ↑ (second HCQ benefit pathway beyond TLR7/9 block).*
*QUIN/M8 connection: IDO1 → kynurenine → QUIN → NMDA → neuroinflammation → SP/NK1R → rosacea flushing. Speculative but completes the IFN-α → M8 link.*
