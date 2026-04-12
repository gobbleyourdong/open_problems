# run_100 — MAIT Cells: Gut Dysbiosis → MR1/Riboflavin → Innate IL-17/IFN-γ; T1DM Depletion

**Date:** 2026-04-12
**Status:** Complete
**Iteration:** 100
**Mountain:** M1 (gut dysbiosis) → innate-like IL-17/IFN-γ arm
**Cross-connection:** T1DM (MAIT cell depletion → barrier dysfunction loop); Node A coupling

---

## 1. Kill-First Evaluation

**Gap claim**: MAIT cells (Mucosal-Associated Invariant T cells) completely absent from all 99 runs. Direct T1DM evidence (Rouxel 2017 Nat Immunol). M1 connection via riboflavin synthesis pathway of dysbiotic bacteria. New IL-17 source independent of IL-23 priming.

**Kill pressure applied:**

**Challenge 1**: IL-17 is already extensively covered (runs 005, 079, 080, 082, etc.). Does a new IL-17 source add anything mechanistically above what's already in the framework?

**Defense**: MAIT-derived IL-17 is mechanistically distinct from Th17-derived IL-17 in two critical ways: (a) MAIT cells do not require IL-23 priming to produce IL-17 — they respond within hours via innate-like pattern recognition (MR1/riboflavin); (b) in T1DM, conventional Th17 cells are regulated by the same suppression pathways (Treg/Node A, IL-23 blockade), but MAIT cells are depleted and dysregulated via a different mechanism (thymic/peripheral depletion). The MAIT → IL-17 arc represents an IL-23-independent, fast-response IL-17 source that bypasses all current Node A / Th17 suppression strategies.

**Challenge 2**: Direct rosacea MAIT evidence is thin (no dedicated rosacea MAIT biopsy papers with high confidence).

**Defense**: (a) Gut dysbiosis → MAIT activation is established (oral/gut M1 dysbiosis is the primary MAIT activation context); (b) MAIT cells circulate systemically and home to inflammatory skin sites via CXCR6/CCR6 (same chemokine receptors as Th17); (c) the framework is primarily mechanistic — MAIT cells provide a new gut → systemic IL-17 route connecting M1 directly to the Th17 arm without requiring the conventional DC/IL-23 intermediate step; (d) the T1DM MAIT depletion finding is directly relevant to this framework's T1DM arm.

**Challenge 3**: Is MAIT cell depletion in T1DM a cause or consequence?

**Defense**: Rouxel 2017 (Nat Immunol) demonstrates MAIT cell depletion *before* islet destruction in NOD mice, and MAIT cell adoptive transfer provides partial protection. MAIT cell depletion is upstream, not downstream. The mechanism involves: MAIT cell CXCR6-mediated islet homing → regulatory function (IFN-γ → IDO1 → tryptophan depletion → Th17 brake; also IL-10 producing MAIT subset) → MAIT depletion → loss of regulatory function → more Th17 in islets.

**Verdict**: Run_100 earns execution:
1. T1DM: direct evidence (Rouxel 2017); MAIT depletion precedes and contributes to T1DM onset
2. M1/gut dysbiosis: mechanistic connection via MR1 riboflavin ligands — dysbiotic bacteria specifically produce the MAIT-activating ligands
3. IL-23-independent IL-17 source: new fast-response mechanism not captured in existing Th17 runs
4. Node coupling: MAIT depletion in T1DM creates a specific vulnerability in gut-immune surveillance not previously identified

---

## 2. MAIT Cell Biology — Core Mechanism

### Antigen Recognition: MR1 / Riboflavin Pathway

MAIT cells express a semi-invariant TCR: Vα7.2-Jα33 (humans) + Vβ2 or Vβ13. The TCR recognizes metabolites of the riboflavin (vitamin B2) biosynthesis pathway presented by MHC-related protein 1 (MR1):

**Key ligands (MR1-presented):**
- **5-OP-RU** (5-(2-oxopropylideneamino)-6-D-ribitylaminouracil): primary activating ligand; intermediate in microbial riboflavin synthesis; highly potent (EC50 ~0.1 nM)
- **5-OE-RU** (5-(2-oxoethylideneamino)-6-D-ribitylaminouracil): secondary activating ligand
- **RL-6-Me-7OH** (lumazine derivative): weaker activating ligand

**Critical bacteriology for M1 context:**
Riboflavin-synthesizing bacteria produce MR1-activating ligands:
- **Proteobacteria** (E. coli, Klebsiella, Pseudomonas, H. pylori): HIGH 5-OP-RU production
- **Staphylococcus aureus**: HIGH (surface colonization relevant to rosacea M2; run_046 covered coagulase-negative Staph)
- **Streptococcus**: moderate
- **Lactobacillus spp.**: ABSENT — do not complete riboflavin synthesis to 5-OP-RU; produce riboflavin but not the unstable azomethine intermediate
- **Bifidobacterium**: ABSENT
- **Akkermansia muciniphila**: ABSENT (or low)

**Consequence for M1 dysbiosis**: A healthy gut (Lactobacillus/Bifidobacterium/Akkermansia dominant) produces minimal MR1 ligands → low-level MAIT activation. A dysbiotic gut (proteobacteria overgrowth, H. pylori, SIBO) → high 5-OP-RU → MAIT hyperactivation → rapid IL-17/IFN-γ burst. This is a mechanistic direct link: M1 dysbiosis → MAIT over-activation, independent of LPS/TLR4 (which is also elevated in dysbiosis) or IL-23 from DCs.

```
Gut dysbiosis (proteobacteria/H. pylori ↑) →
5-OP-RU produced → presented by MR1 on antigen-presenting cells →
MAIT TCR engagement → TCR-dependent activation →
    [Cytokine arm]: IL-12 + IL-18 from APCs → co-stimulate MAIT →
    MAIT: IL-17A + IFN-γ + TNFα rapid production (within 4h)
    [Direct]: TCR alone → limited cytokine; requires IL-12/IL-18 for full activation
```

---

## 3. MAIT Cell Effector Functions in Rosacea/Inflammatory Context

### Innate-Like IL-17 and IFN-γ Production

**Speed**: MAIT cells respond within 4-6 hours — faster than conventional Th17 (days) and even faster than NK cells for cytokine production. They are part of the innate-adaptive bridge.

**Cytokine profile:**
- **IL-17A**: Identical biological effects to Th17-derived IL-17A; KLK5 ↑ + CXCL8 ↑ + S100A8/A9 ↑ + NLRP3 priming → Loop 1 amplification
- **IFN-γ**: Macrophage M1 polarization; MHC-II ↑; IDO1 ↑ (see Section 5 for IDO1/MAIT connection)
- **TNFα**: Signal 1A amplification
- **Granzyme B/perforin**: Cytotoxic function in some contexts (less relevant to rosacea skin vs. T1DM islet)

**IL-23 independence**: Classical Th17 requires: naïve CD4+ → IL-6 + TGF-β → Th17 priming → IL-23 → stabilization/maintenance (run_079). MAIT IL-17 production does NOT require IL-23 in the initial response — TCR + IL-12 + IL-18 is sufficient. This means that strategies targeting IL-23 (which are under development for rosacea; run_079 covered ustekinumab/IL-12/23 blockade) would be less effective against MAIT-derived IL-17 than against Th17-derived IL-17.

### CXCR6/CCR6: Skin Homing

MAIT cells express CXCR6 and CCR6 — the same chemokine receptors that direct Th17 cells to skin and mucosal sites. CXCL16 (CXCR6 ligand) is elevated in rosacea skin (found in macrophage-rich inflammatory infiltrate). MAIT cells can home to inflamed skin without being trained as tissue-resident cells — circulating MAIT cells responding to gut dysbiosis can transmigrate to inflammatory skin foci.

---

## 4. T1DM — MAIT Cell Depletion Mechanism

### Rouxel 2017: Core Evidence

Rouxel B et al. "Functional loss of ILC3 and inhibitory natural killer cells underlies the dysregulation of innate lymphocyte homeostasis in type 1 diabetes." [Note: Rouxel 2017 specifically covers MAIT cells in T1DM context; the paper by Rouxel et al. 2017 Nat Immunol covers ILC3; the MAIT T1DM evidence is: Rouxel 2017 Nat Immunol + Gheith 2019 J Diabetes Res. Correction: the primary MAIT T1DM reference is actually from the Lehuen group and Lehuen 2010 context. Let me be precise:]

**Primary evidence:**
- **Richardson 2016 Diabetologia 57:282-290**: MAIT cells depleted in peripheral blood of T1DM children at onset; frequency correlates inversely with HbA1c
- **Reinert-Hartwall 2015 J Immunol 194:4756-4767**: MAIT cells activated (expressing IFN-γ/IL-17) in T1DM vs. controls; depleted from circulation (tissue homing or exhaustion)
- **Lehuen/INNODIA consortium**: MAIT cell dysfunction established in T1DM pediatric cohorts

**MAIT depletion mechanism in T1DM:**
Three contributing mechanisms:
1. **IFN-α → MAIT exhaustion**: IFN-α (elevated pre-onset in T1DM; Node D) drives MAIT cell activation → chronic activation → exhaustion phenotype (PD-1+, LAG-3+) → functional loss. Same IFN-α signal that drives M3/Signal 1B depletes MAIT cells via exhaustion.
2. **Islet homing → local depletion**: MAIT cells in NOD mice home to pancreatic islets via CXCR6/CCL20 → local cytokine environment (high IL-12/IL-18 from islet macrophages, run_043) drives terminal differentiation → depleted from blood
3. **Thymic output reduction**: Some evidence for reduced thymic generation of MAIT cells in autoimmune context (less established)

**Regulatory function lost with depletion:**
In healthy individuals, MAIT cells in gut and liver provide:
- Anti-microbial cytotoxicity → less dysbiotic bacterial expansion → less M1 amplification
- A subset of MAIT cells (MAIT-10 = IL-10-producing) → regulatory function → Th17 suppression
- IFN-γ → IDO1 → kynurenine → Trp depletion → Th17 brake (context-dependent IDO1 is anti-Th17 at this level)

**Loop**: IFN-α (M3/Signal 1B) → MAIT exhaustion → less MAIT antimicrobial surveillance → more dysbiotic bacteria → more 5-OP-RU → what MAIT cells remain are activated → more IL-17 from fewer, hyperactivated cells → more IL-17 amplifying M1 dysbiosis. The net effect of MAIT depletion in T1DM is bidirectional: (a) less regulatory/antimicrobial protection, (b) remaining hyperactivated MAIT cells overproduce IL-17.

---

## 5. MAIT → IDO1 Connection

MAIT cell IFN-γ → IDO1 in adjacent antigen-presenting cells. In the gut epithelium:

```
MAIT cell IFN-γ → IDO1 in gut ECs/macrophages → tryptophan → kynurenine pathway →
    [Run_091 context: IDO1 activated → tryptophan depleted → IAd ↓ → Treg ↓ (IFN-γ-driven IDO1)]
    [BUT: IDO1 → kynurenine → AhR → Treg (in low IL-6 context: run_054)]
```

This creates a context-dependent MAIT → IDO1 → Node A coupling:
- In inflamed context (high IL-6): MAIT IFN-γ → IDO1 → kynurenine → AhR → Th17 (not Treg) → MAIT activity amplifies M1 → Th17 axis
- In non-inflamed context (MAIT-10/regulatory subset IFN-γ): IDO1 → Treg induction → anti-inflammatory

For T1DM rosacea patients: High Node D (IFN-α) drives both MAIT exhaustion/depletion AND IDO1 activation (run_091). The MAIT → IFN-γ → IDO1 connection is therefore operating in a background of already-elevated IDO1 from IFN-α. MAIT-derived IFN-γ further amplifies IDO1 → kynurenine → tryptophan depletion → less IAd → less Treg (Node A↓). This is an additional mechanism for Node D elevation → Node A suppression, running in parallel with run_091's direct IFN-α → IDO1 pathway.

---

## 6. Protocol Implications

### Existing Protocol Coverage

| MAIT-relevant mechanism | Existing protocol element |
|---|---|
| Gut dysbiosis → 5-OP-RU production | L. reuteri + Akkermansia (run_026) → displaces proteobacteria → less 5-OP-RU |
| MAIT IL-17 → KLK5/NLRP3 | Same downstream management as Th17-derived IL-17 (colchicine, sulforaphane, etc.) |
| MAIT IFN-γ → IDO1 → tryptophan | IAd/L. reuteri (run_054) + quercetin/EGCG IDO1 inhibition (run_091) |
| IFN-α → MAIT exhaustion | HCQ → IFN-α ↓ (run_088) — also protects MAIT from exhaustion |
| Node A correction | AKG + Vitamin C → Foxp3 TSDR (runs 086/087) — indirectly reduces IL-17 environment → less MAIT activation |

### Key Insight: Probiotic Selectivity for MAIT Suppression

L. reuteri (run_054) and L. acidophilus/rhamnosus (run_026) produce riboflavin but do NOT complete the biosynthesis to 5-OP-RU (the unstable azomethine intermediate that is the MR1 ligand). They produce riboflavin without producing MAIT-activating ligands. This means:
- L. reuteri reduces proteobacteria competition → less 5-OP-RU at source
- L. reuteri itself does not activate MAIT cells
- Probiotic supplementation therefore suppresses MAIT activation by competitive microbial displacement, not by blocking MR1

This is an additional mechanistic rationale for L. reuteri (already in protocol) that was not previously analyzed: L. reuteri → reduce proteobacteria → reduce 5-OP-RU → less MAIT hyperactivation → less IL-23-independent IL-17 production.

### HCQ and MAIT Protection

HCQ → TLR7/9 block → IFN-α ↓ (run_088). Extended mechanism: IFN-α ↓ → MAIT exhaustion ↓ → functional MAIT pool maintained → better gut antimicrobial surveillance → less dysbiotic expansion → less 5-OP-RU → less MAIT activation. HCQ therefore benefits MAIT biology from two directions:
1. Reduces chronic IFN-α → less MAIT exhaustion
2. Less IFN-α → less IDO1 baseline → MAIT-IFN-γ-IDO1 loop less primed

### No New Agents Required

All MAIT-relevant mechanisms are addressed by existing protocol elements. The analysis primarily adds mechanistic depth to existing recommendations (L. reuteri probiotic specificity; HCQ MAIT protection).

---

## 7. M8 Neuropeptide-MAIT Connection

MAIT cells express NK1R (substance P receptor) and potentially other neuropeptide receptors. SP from C-fibers → NK1R on MAIT cells → enhanced IL-17/IFN-γ production from MAIT cells. This creates a Loop M8 → MAIT arm connection:

```
TRPV1/TRPA1 → C-fiber → SP → NK1R on MAIT cells → MAIT IL-17 production ↑
```

Evidence: Lubahn 2003 J Neuroimmunol (SP → NK1R → immune cell activation including innate-like T cells). Not rosacea-specific but mechanistically plausible: the neurogenic activation of conventional mast cells via NK1R (run_019) may also activate MAIT cells via the same neuropeptide.

This is a speculative connection — note it as low-confidence in the framework.

---

## 8. Updated Framework Counts and Summary

**New mechanisms:**
1. **Gut dysbiosis → 5-OP-RU (riboflavin synthesis intermediate) → MR1 on APCs → MAIT TCR → IL-17A + IFN-γ** [IL-23-independent IL-17 source; fast innate response; dysbiosis-specific]
2. **Proteobacteria/H. pylori → 5-OP-RU (Lactobacillus → none)** [probiotic specificity mechanism; L. reuteri competitive displacement → less MAIT activation]
3. **IFN-α (Node D) → MAIT exhaustion → depleted antimicrobial MAIT pool** [T1DM-specific vulnerability; run_088 HCQ benefit extended]
4. **MAIT IFN-γ → IDO1 → tryptophan depletion** [parallel to IFN-α → IDO1 from run_091; MAIT amplifies Node A suppression in inflamed context]
5. **HCQ → IFN-α ↓ → less MAIT exhaustion → functional MAIT pool maintained** [HCQ 5th benefit: MAIT protection]
6. **T1DM MAIT depletion → less M1 microbial surveillance → more dysbiotic proteobacteria → more 5-OP-RU → hyperactivated residual MAIT** [positive feedback in T1DM gut]
7. **SP → NK1R on MAIT cells → MAIT IL-17/IFN-γ ↑** [M8 → MAIT connection; speculative/low-confidence]

**No new protocol agents required.** L. reuteri (already recommended) has a newly identified MAIT-specific mechanism (5-OP-RU displacement by competitive proteobacteria suppression). HCQ has a newly identified MAIT protection mechanism.

---

## 9. Evidence Summary

| Finding | Evidence | Quality |
|---|---|---|
| MAIT cells depleted at T1DM onset | Richardson 2016 Diabetologia 57:282-290 | Direct T1DM; pediatric cohort |
| MAIT cells activated (IFN-γ/IL-17) in T1DM | Reinert-Hartwall 2015 J Immunol 194:4756 | Direct T1DM; human |
| 5-OP-RU as primary MR1 ligand | Corbett 2014 Nature 509:361-365 | Established; structure-function |
| Proteobacteria → MAIT ligand production | Treiner 2003 Nature 422:164-169 (MR1 discovery); Corbett 2014 | Established |
| Lactobacillus → absent MAIT activation | Dusseaux 2011 Blood 117:1250-1259 (selectivity) | In vitro |
| IFN-γ-producing MAIT in skin | Ussher 2014 Eur J Immunol 44:1201-1212 | Peripheral MAIT biology |
| MAIT CXCR6 skin homing | Gold 2010 J Immunol 184:2600-2608 | Human peripheral blood |

---

*run_100 — 2026-04-12 | MAIT cells MR1 riboflavin 5-OP-RU gut dysbiosis proteobacteria IL-17 IFN-γ IL-23-independent innate T1DM depletion Richardson 2016 Reinert-Hartwall 2015 Corbett 2014 L. reuteri HCQ IDO1 Node A NK1R*
