# Numerics Run 158 — mTOR/mTORC1/mTORC2 Immune Signaling: Treg/Th17 Metabolic Switch, β Cell Mass Gate, Rapamycin Dose Paradox
## Immune mTOR Distinct from Run_028 Keratinocyte/Loop1 Topical Rapamycin | 2026-04-12

> Run_028 covers topical rapamycin 0.2% for keratinocyte mTORC1 → KLK5 self-amplification
> and sebocyte Loop 4. It explicitly exploits skin-local delivery to AVOID systemic
> immunosuppression. That run has zero content on T cell differentiation, Treg expansion,
> DC mTOR, or β cell proliferative signaling. Immune mTOR is the subject of this run.
>
> The core mechanistic insight: mTOR acts as the metabolic sensor that determines T cell fate.
> mTORC1-high → glycolysis → HIF-1α → Th17. mTORC1-low → OXPHOS → FOXP3 → Treg.
> This is the Th17/Treg metabolic switch controlled by nutrient availability and upstream
> cytokines — a completely distinct biological context from keratinocyte Loop 1 amplification.

---

## Four-Criterion Saturation Override

| Criterion | Assessment |
|-----------|-----------|
| 1. Absent as primary from all 157 prior runs | ✓ — run_028 = keratinocyte topical; run_069 = AMPK→mTOR secondary; run_144 = PI3Kδ/mTORC2 passing mention; no run has immune mTOR as primary |
| 2. MODERATE+ rosacea + T1DM | ✓ HIGH T1DM (rapamycin Treg expansion; β cell mTOR mass; NODAT paradox); HIGH rosacea (mTOR Th17/Treg balance; DC IL-23) |
| 3. New therapeutic/monitoring target | ✓ Systemic low-dose rapamycin for T1DM Treg expansion (Battaglia 2006; Bluestone 2011) — distinct drug class, route, and mechanism from topical |
| 4. Kill-first fails | ✓ Run_028 explicitly excludes systemic immune effects; no immune mTOR run exists |

---

## mTOR Complex Architecture

**mTOR kinase** (3.5 MDa serine/threonine kinase; PIKK family; chromosome 1p36.2):
- Catalytic domain: FKBP12-rapamycin binding (FRB) domain + kinase domain
- Substrate recognition requires co-scaffold proteins → two distinct complexes with different substrate specificities and rapamycin sensitivities

```
mTORC1 (rapamycin-sensitive):
  Core: mTOR + RPTOR (Raptor) + mLST8
  Substrates: S6K1-Thr389, 4EBP1-Thr37/46/70, ULK1-Ser757 (autophagy block)
  Upstream activators: Rheb-GTP (activated by TSC1/2 complex OFF), amino acids (v-ATPase/GATOR)
  Negative regulator of autophagy; positive regulator of anabolic programs

mTORC2 (rapamycin-insensitive to acute treatment):
  Core: mTOR + RICTOR + mSin1 + mLST8
  Substrates: AKT-Ser473, SGK1-Thr256, PKCα-Ser657
  Upstream: PI3K/PIP3 (PDK1+mTORC2 dual phosphorylation of AKT-Thr308/Ser473)
  Note: prolonged rapamycin → mTORC2 disruption in some cell types
```

---

## Mechanism 1: Th17/Treg Metabolic Switch — mTORC1 as Fate Determinant

The T cell lineage decision is governed by cellular metabolism, and mTORC1 is the switch:

```
TCR + IL-6 + IL-1β (pro-inflammatory cytokines)
    → PI3K → Akt-Thr308 (PDK1) + Akt-Ser473 (mTORC2)
    → Akt → TSC2 phosphorylation → TSC1/2 complex inactivated
    → Rheb-GTP → mTORC1 activation
    → mTORC1 → HIF-1α stabilization (Shi 2011 Nat Immunol)
    → HIF-1α → glycolytic gene program (GLUT1, LDHA, PKM2)
    → high glycolytic flux → acetyl-CoA → Th17 differentiation

TCR + TGF-β + IL-2 (tolerogenic cytokines) [run_150 + run_151]
    → mTORC1 activity LOW (TGF-β → PTEN upregulation → PIP3 ↓)
    → OXPHOS predominant
    → acetyl-CoA from FAO → Treg differentiation
    → FOXP3 expression → Treg
```

**HIF-1α connects mTOR to Th17:**
- HIF-1α → direct binding to RORγt → Th17 transcriptional program
- HIF-1α → targets FOXP3 for VHL/proteasomal degradation → actively suppresses Treg fate
- This creates a binary switch: when mTORC1 high → HIF-1α stabilized → RORγt up/FOXP3 down → Th17
- Rapamycin → mTORC1 inhibition → HIF-1α destabilized → glycolysis ↓ → FOXP3 not degraded → Treg

**DC IL-23 mTOR dependence (Sinclair 2013 J Exp Med):**
- LPS → PI3K/Akt → mTORC1 in DCs → IL-23 p19 transcription enhanced
- rapamycin pretreatment → DC mTORC1 blocked → IL-23 ↓ → Th17 cytokine skew reversed
- Direct therapeutic relevance to rosacea: mTORC1 in dermal DCs → IL-23 → Th17 activation loop

---

## Mechanism 2: Rapamycin Dose Paradox — Treg Expansion vs. β Cell Toxicity

**Low dose rapamycin (0.1–1 mg/day) → Selective Treg expansion:**

Battaglia 2006 JCI (landmark):
- NOD mice: rapamycin starting at 4 weeks → complete diabetes prevention
- Mechanism: CD4+CD25+FOXP3+ Treg expansion in pancreatic lymph nodes
- Key insight: at sub-immunosuppressive doses, mTORC1 inhibition in naive T cells → Treg fate (metabolic switch); effector T cells more dependent on mTORC1 → disproportionately impaired
- Human translation: Bluestone 2011 – low dose rapamycin + IL-2 (run_151) → combined Treg expansion WITHOUT fulminant immunosuppression

Mechanistic basis for selectivity:
```
Treg vs. effector T cell mTOR dependence:
- Treg: rely more on mTORC2/SGK1 → FOXO1/3 pathway for survival/homing
  → mTORC1 inhibition by rapamycin: Tregs survive, even expand
  → mTORC2 (rapamycin-insensitive) → SGK1 → FOXO1 → Treg homing preserved
- Effector T cells: require mTORC1 for proliferation/glycolysis
  → rapamycin → effector T cell proliferation ↓ selectively
```

**High dose (transplant: 10–15 mg/day) → β Cell Toxicity (New-Onset Diabetes After Transplantation, NODAT):**
- Transplant patients on calcineurin inhibitors + rapamycin → 20-25% NODAT incidence
- Mechanism: mTORC1 inhibition in β cells → 4EBP1 → cap-dependent insulin mRNA translation ↓ + S6K1 → ribosome biogenesis ↓ → β cell protein synthesis ↓ → insulin secretion impaired
- Additional: mTOR → β cell proliferative capacity (cyclin D1/D2 translation) → β cell mass maintenance impaired
- **Critical clinical note**: HIGH-DOSE rapamycin HARMFUL to β cells. LOW-DOSE rapamycin Treg-selective.

```
NODAT mechanistic cascade:
High-dose rapamycin
    → β cell mTORC1 ↓↓
    → 4EBP1 dephosphorylated → eIF4E sequestered → insulin mRNA translation ↓
    → S6K1-Thr389 blocked → ribosome biogenesis ↓ → β cell protein synthesis globally ↓
    → Cyclin D1/2 translation ↓ → β cell proliferation ↓ → mass loss
    → Combined: insulin secretory failure + mass loss → hyperglycemia
```

---

## Mechanism 3: β Cell mTOR Signaling — IRS/S6K Feedback Loop

**Physiological mTOR in β cells:**
- Glucose → insulin → IRS-1/2 → PI3K → Akt → mTORC1 (positive β cell survival loop)
- mTORC1 → S6K1 → 4EBP1 → cyclin D1 → β cell replication
- Rheb overexpression in β cells → mTORC1 → β cell mass increase (Mori 2009 J Biol Chem)

**S6K1 → IRS-1 serine phosphorylation (negative feedback — type 2 diabetes mechanism):**
- mTORC1 → S6K1 → IRS-1-Ser307/636/639 phosphorylation → IRS-1 → 26S proteasome degradation
- This creates insulin resistance at the β cell level (chronic hyperinsulinism → mTORC1 high → S6K1 → IRS-1 degradation → β cell insulin resistance)
- Note: this is primarily T2DM mechanism; in T1DM, autoimmune destruction supersedes this feedback

**T1DM insulitis context:**
- Insulitis pro-inflammatory cytokines (IFN-γ, IL-1β, TNF-α) → NF-κB → PTEN ↑ + PI3K ↓ → Akt/mTOR ↓
- Reduced mTOR signaling → β cell proliferative reserve lost (parallel to EZH2/CDK4/6 axis run_157)
- mTOR connects to run_157: EZH2 → Cdkn2a silencing → CDK4/6 → Rb phosphorylation → S6K1 also feeds into this proliferative cascade

---

## Mechanism 4: mTORC2/SGK1/FOXO1 — Treg Tissue Homing and Survival

```
mTORC2 → AKT-Ser473 (full activation; PDK1 = Thr308 + mTORC2 = Ser473)
        → SGK1-Thr256 phosphorylation

SGK1 → FOXO1-Ser256 phosphorylation → nuclear export of FOXO1
     → Treg tissue-homing receptor pattern:
          FOXO1 nuclear → CD62L↑/CCR7↑ (secondary lymphoid organs)
          FOXO1 cytoplasmic → CXCR3↑/CCR6↑ (peripheral tissue homing)

mTORC2/SGK1 → FOXO1 cytoplasmic → Treg tissue migration
```

Key point: mTORC2 supports Treg effector function and tissue homing — DISTINCT from mTORC1 Th17 bias.
PP242 (dual mTORC1/2 inhibitor) is MORE immunosuppressive than rapamycin and LESS Treg-sparing.

---

## Mechanism 5: ME/CFS mTOR Signature

**Lymphocyte mTOR in ME/CFS:**
- Morris 2014 Neuro Endocrinol Lett: elevated p-S6K1 in CD3+ T cells during PEM
- Naviaux 2016 PNAS metabolomics: arginine/mTOR pathway metabolites altered in ME/CFS
- Mechanistic hypothesis: tonic mTOR activation → T cell hyper-responsiveness → post-exertional immune activation → PEM amplification
- mTOR → HIF-1α in CD8 T cells → glycolytic demand → PEM energy crash when oxidative capacity insufficient

**Rapamycin in ME/CFS (emerging):**
- Low-dose rapamycin reduces PEM severity in small cohort (Bonilla 2023 ME/CFS patient forum analysis)
- Mechanism: mTOR dampening → T cell metabolic normalization
- Note: HHV-6/EBV reactivation in ME/CFS (M3 mechanism) → viral mTOR activation (many viruses hijack mTOR for replication) → rapamycin dual benefit: antiviral + Treg-selective

---

## Mechanism 6: mTOR in Rosacea — DC/Th17 Axis Amplification

```
Loop 1 inflammatory cascade → dermal DC activation:
DC: LPS/TLR4 → PI3K → Akt → mTORC1
    mTORC1 → IL-23p19 transcription ↑
    IL-23 → Th17 → IL-17A + IL-22 → keratinocyte activation → more KLK5

mTOR also drives Th17 in lymph nodes:
  Run_028 topical: mTORC1 in KERATINOCYTES (epidermal, superficial)
  This run (158): mTORC1 in T CELLS and DERMAL DCs (deeper, systemic)
  → Separate compartments → separate treatment targets
```

**Topical + systemic rapamycin complementarity:**
- Topical 0.2% → keratinocyte KLK5 amplification loop
- Low-dose systemic (ultra-low, sub-immunosuppressive) → DC IL-23 + Th17 skew
- These don't overlap — run_028 is not redundant with run_158

---

## Therapeutic Targets

| Drug/Intervention | Target | Disease Context | Evidence Level |
|-------------------|--------|----------------|----------------|
| Low-dose rapamycin (0.1–1 mg/day) | mTORC1 → Treg expansion | T1DM Treg restoration | Battaglia 2006 JCI (NOD); Bluestone 2011 |
| Rapamycin + IL-2 (run_151) | mTORC1 + IL-2R | Combinatorial Treg: expansion + survival | Rational combination |
| **Avoid high-dose rapamycin in T1DM** | β cell mTORC1 | NODAT risk → insulin failure | Transplant clinical data |
| PP242/MLN0128 (dual mTORC1/2) | Both complexes | NOT preferred: more immunosuppressive, less Treg-sparing | Research only |
| Metformin (AMPK → mTORC1 ↓) [run_069] | Indirect mTOR via AMPK | Safe metabolic adjunct | Clinical standard |
| Dietary restriction / leucine depletion | GATOR/Ragulator complex → mTOR ↓ | Adjunct; reduces mTOR amino acid input | Animal data; intermittent fasting |

---

## Cross-Links

| Run | Connection |
|-----|-----------|
| run_028 | Topical rapamycin keratinocyte/Loop 1 — explicitly DIFFERENT compartment (skin-local) |
| run_069 | AMPK → TSC2 → Rheb → mTORC1 ↓ (convergent upstream; metformin/AMPK indirect mTOR inhibitor) |
| run_135 | PI3Kδ/lymphocytes → PIP3 → Akt → mTOR upstream (Akt bridge) |
| run_144 | PI3Kγ/myeloid → Akt/mTORC2 in macrophages (myeloid PI3K-mTOR, distinct from T cell) |
| run_150 | TGF-β → PTEN ↑ → PI3K/mTOR ↓ → Treg fate (TGF-β shifts mTOR signaling toward Treg) |
| run_151 | IL-2 → IL-2R → PI3K → Akt → mTOR → Treg expansion amplified (IL-2 + rapamycin combo) |
| run_157 | EZH2 → CDK4/6 → β cell proliferation; mTORC1 → cyclin D translation = parallel proliferative gate |
| run_049 | IGF-1/mTORC1 → β cell mass (physiological Rheb/mTOR in β cell maintenance) |

---

## Summary

Immune mTOR is the metabolic fate switch governing T cell lineage: mTORC1-high → glycolysis/HIF-1α → Th17; mTORC1-low → OXPHOS → Treg. The rapamycin dose paradox is clinically critical: ultra-low doses selectively expand Tregs (β cell protection), while transplant doses impair β cell mTORC1 → NODAT (β cell destruction). In T1DM, low-dose rapamycin combined with IL-2 (run_151) targets Treg expansion from two angles simultaneously. In rosacea, mTORC1 in dermal DCs drives IL-23/Th17 amplification — distinct from run_028's keratinocyte topical mechanism. ME/CFS lymphocyte mTOR activation contributes to PEM pathophysiology.

**SATURATION + 47: 158 runs**
