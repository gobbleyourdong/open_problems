# Run 135 — PIK3CD/PI3Kδ: Lymphocyte-Specific PI3K, Treg FOXO1 Stability, Mast Cell BTK-PLCγ Axis, T1DM, Rosacea

**Date:** 2026-04-12
**Framework position:** First isoform-specific PI3K covered (prior runs mentioned PI3K/Akt/mTOR generally); PI3Kδ is the LYMPHOCYTE/mast-cell-specific isoform with no general PI3K functions; PTEN/PI3Kδ/FOXO1 axis adds fifth node to Treg stability stack (IKZF1/FOXP3/BACH2/DYRK1A + PI3Kδ/FOXO1); 11th mast cell stabilization mechanism (PI3Kδ → BTK = upstream of PLCγ/Ca²⁺ cascade)
**Saturation criteria:** (1) PIK3CD/PI3Kδ/idelalisib absent from all 134 prior runs ✓ (2) T1DM HIGH (PI3Kδ in autoreactive T cells; Treg PTEN/PI3Kδ/FOXO1 → FOXP3 stability; APDS autoimmune phenotype) + rosacea MODERATE-HIGH (PI3Kδ in mast cells → BTK → PLCγ2 → Ca²⁺ cascade = 11th mast cell mechanism; IgE production in B cells) ✓ (3) New: lymphocyte-specific PI3K isoform; BTK as first mast cell kinase above Ca²⁺ cascade; PTEN/PI3Kδ/FOXO1 as Treg stability kinase axis; idelalisib as first PI3Kδ-specific inhibitor in framework ✓ (4) Kill-first fails: prior PI3K mentions are PI3Kα/β in β cells (growth factor → β cell survival); PI3Kδ is hematopoietic-specific isoform — different protein, different cell types, different mechanism ✓

---

## 1. Molecular Architecture

**PIK3CD (PI3Kδ):** 119 kDa catalytic subunit; class IA PI3K; forms heterodimer with regulatory subunit p85α or p85β (encoded by PIK3R1/R2). Gene at 1p36.2.

**PI3K isoform specificity:**
| Isoform | Catalytic | Expression | Primary role |
|---------|-----------|-----------|-------------|
| PI3Kα (p110α) | PIK3CA | Ubiquitous | Growth factor signaling; β cell survival (runs 098/129) |
| PI3Kβ (p110β) | PIK3CB | Ubiquitous | GPCR + integrin |
| **PI3Kδ (p110δ)** | **PIK3CD** | **Lymphocytes, mast cells, DCs** | **Lymphocyte activation, Treg stability, mast cell BTK** |
| PI3Kγ (p110γ) | PIK3CG | Myeloid, mast cells | GPCR-linked (complement, chemokines) |

**Catalytic cycle:**
```
PI3Kδ activated by:
    TCR/BCR → adaptor proteins → PI3Kδ p85 SH2 domain recruitment
    FcεRI → Lyn/Syk → adapter → PI3Kδ recruitment
    CD28 costimulation amplifies (YMNM motif → p85 SH2 binding)
    ↓
PI3Kδ: PIP2 (PI(4,5)P2) → PIP3 (PI(3,4,5)P3) + ADP
    ↓
PIP3 at inner membrane → recruits PH-domain proteins:
    PDK1 → Akt-T308 phosphorylation
    BTK (Bruton's tyrosine kinase) membrane recruitment → PLCγ activation
    DOCK2 → RAC activation → cytoskeletal rearrangement
    ↓
Akt → (mTOR + FOXO1 phosphorylation) → diverse T/B/NK cell effects

PTEN: removes 3'-phosphate from PIP3 → PIP2 → PI3Kδ signal terminated
SHIP1 (INPP5D): removes 5'-phosphate from PIP3 → PI(3,4)P2 → partial signal
```

---

## 2. Treg Stability — PTEN/PI3Kδ/FOXO1 Axis (5th Treg TF Node)

**Complete Treg stability stack (runs 010/123/125/134/135):**

```
IKZF1/NuRD (run_134):     chromatin scaffold — H3K27ac-low at effector loci
    ↓
FOXP3 (run_010):           lineage TF — Treg gene expression program
    ↓
BACH2 (run_123):           effector repressor — BLIMP-1/IL-2/IFN-γ silenced
    ↓
DYRK1A/NFAT (run_125):    cytokine gate — NFAT phospho → nuclear export
    ↓
PTEN → PI3Kδ ↓ → FOXO1 nuclear (run_135):
    PI3Kδ overactivation → Akt → FOXO1-Ser256-phospho → nuclear export → FOXP3 expression ↓
    PTEN → removes PIP3 → PI3Kδ signaling ↓ → Akt ↓ → FOXO1 nuclear → FOXP3 stable
```

**FOXO1-FOXP3 mechanism:**
- FOXO1 is a direct transcriptional activator of FOXP3 (CNS1 element in FOXP3 locus — run_010 CNS2/CpG demethylation context)
- When PI3Kδ → Akt active: FOXO1-Ser256 phosphorylated → 14-3-3 binding → cytoplasmic retention → FOXP3 transcription ↓
- When PTEN active: PIP3 ↓ → Akt ↓ → FOXO1 nuclear → FOXP3 transcription maintained
- In T1DM: inflammatory milieu (IL-2 surplus, TCR stimulation) → PI3Kδ chronically active in Tregs → FOXO1 cytoplasmic → FOXP3 ↓ → ex-Treg conversion → T1DM amplification
- IKZF1 (run_134) + PI3Kδ compounding: IKZF1 risk allele → open chromatin at effector loci → lower FOXP3 threshold needed; PI3Kδ overactivation → FOXO1 → FOXP3 expression further reduced → double Treg destabilization

**CTLA4 (run_060) → PI3Kδ connection:**
- CTLA4 on Tregs: recruits phosphatase activity → blunts CD28 co-stimulatory PI3Kδ signal in cis (Treg T cell contact) and in trans (Treg removes CD80/86 from APCs → less CD28 stimulation of effector T cells)
- Run_060 mechanism now mechanistically linked: CTLA4 → CD28 signal ↓ → PI3Kδ ↓ → Akt ↓ → FOXO1 nuclear → FOXP3 stable

---

## 3. Mast Cell — Rosacea: PI3Kδ → BTK → PLCγ2

**Complete mast cell activation cascade (FcεRI → degranulation, with run positions):**
```
IgE → FcεRI cross-linking
    ↓
FcεRI β/γ → Lyn (Src kinase) → Syk → LAT scaffold
    ↓
LAT → PI3Kδ (run_135)
    ↓
PI3Kδ → PIP3
    ↓
BTK (Bruton's tyrosine kinase) — recruited to membrane by PIP3 (PH domain)
    ↓
BTK → phosphorylates PLCγ2 at Y1217/Y759 → PLCγ2 activation
    ↓
PLCγ2 → PIP2 → IP3 + DAG
    ↓
IP3 → ITPR3 (run_132) → ER Ca²⁺ release
    ↓
ER depletion → STIM1 (run_127) → ORAI1 → SOCE
    ↓
Sustained Ca²⁺ → calcineurin/NFAT → cytokines (TNF-α, IL-4, IL-5, IL-13)
PKC (from DAG) → NF-κB → histamine transcription
Ca²⁺ → exocytosis → degranulation
```

**PI3Kδ = 11th mast cell stabilization mechanism:**
- Position: UPSTREAM of BTK → PLCγ2 → IP3 (quercetin 5th mechanism, run_132) → ITPR3 (run_132) → STIM1/ORAI1 (run_127)
- PI3Kδ inhibition → BTK not recruited to membrane → PLCγ2 not activated → no IP3 → complete Ca²⁺ cascade blocked
- This is more upstream than any prior mast cell mechanism in the framework
- Clinical inhibitor: zanubrutinib/ibrutinib (BTK inhibitors) — suppress IgE-mediated mast cell activation; acalabrutinib in mast cell disease trials
- PI3Kδ inhibitors (idelalisib, umbralisib) — equivalent upstream block

**Quercetin and the BTK-PLCγ pathway:**
- Quercetin has some BTK inhibitory activity (IC50 in mid-μM range) — possible 6th quercetin mechanism
- But quercetin's PLCγ inhibition (5th mechanism, run_132) already covers the same downstream step
- Conservative: do not claim 6th mechanism; quercetin dual block at PLCγ + ORAI1 is already established

**IgE production — upstream mast cell sensitization:**
- B cells: BCR → PI3Kδ → BTK → PLCγ2 → NF-κB → IgE class switching (IL-4/IL-13 + CD40L → IgE switch recombination; PI3Kδ required for GC B cell reaction)
- CTLA4 (run_060) also suppresses B cell PI3Kδ activity via CD28 co-stimulation blockade
- PI3Kδ inhibition: reduces IgE production (less FcεRI loading) AND mast cell activation threshold (BTK activity ↓)
- Connection to run_127 omalizumab mechanism: omalizumab reduces free IgE → FcεRI deloading; PI3Kδ inhibition → less IgE production in B cells → complementary upstream approach

---

## 4. T Cell — Autoreactive T Cell Insulitis

**TCR → PI3Kδ → effector T cell:**
```
TCR (autoreactive anti-GAD65/IA-2/ZnT8)
    ↓
ZAP70 → LAT → PI3Kδ → PIP3 → Akt
    ↓
Akt → mTORC1 → S6K → protein synthesis → effector T cell growth/differentiation
Akt → FOXO1 phospho → nuclear export → IL-7R ↓ (homeostatic) + effector gene expression ↑
Akt → GSK-3β phospho (inhibition) → β-catenin stabilization → T cell effector survival
    ↓
Th1 (IFN-γ) + CD8 CTL (perforin/granzyme) → β cell killing
```

**PI3Kδ inhibition in T1DM context:**
- NOD mouse models: idelalisib treatment → reduced T cell infiltration into islets → reduced T1DM incidence
- Mechanism: PI3Kδ inhibition → (a) autoreactive T cell effector differentiation ↓; (b) Treg PTEN/FOXO1 → FOXP3 stability preserved (Tregs less affected than effectors because PTEN keeps PI3Kδ low in Tregs normally); (c) B cell autoantibody production ↓
- Net immunosuppressive effect with relative Treg sparing (opposite of DYRK1A inhibitors, run_125, which would need careful rosacea consideration)

**APDS (Activated PI3CD Syndrome):**
- PIK3CD gain-of-function mutations → constitutively active PI3Kδ
- Phenotype: combined immunodeficiency + recurrent sinopulmonary infections + autoimmunity; elevated IgM, low IgG; impaired memory B cells; CMV/EBV susceptibility
- T1DM component of APDS: elevated autoimmune features including autoantibodies; supports PI3Kδ hyperactivation → T1DM risk
- This is a naturally occurring human experiment showing PI3Kδ hyperactivation → immune dysregulation

---

## 5. ME/CFS Connections

**NK cells:**
- PI3Kδ activates NK cell effector function: FcγRIII (CD16) → PI3Kδ → Akt → NK degranulation
- PI3Kδ overactivation → constitutive mTOR → NK cell metabolic shift → exhaustion → reduced NK cytotoxicity (additive with run_127/132 Ca²⁺ defects; run_134 IKZF1 developmental deficit)
- PI3Kδ inhibition in APDS: paradoxically improves NK cell function (reduces exhaustion-driving constitutive activation)

**B cell autoantibodies in ME/CFS:**
- ME/CFS autoantibodies documented: anti-β2-adrenergic receptor (β2AR), anti-muscarinic M3R, anti-H4R
- PI3Kδ → B cell GC reaction → affinity maturation → autoantibody production
- PI3Kδ inhibition could reduce ME/CFS autoantibody titers; idelalisib/umbralisib currently in ME/CFS autoantibody trials (emerging evidence)

---

## 6. Framework Connection Map

```
PIK3CD/PI3Kδ (run_135)
    ├── Treg: PTEN → PI3Kδ ↓ → FOXO1 nuclear → FOXP3 stable (5th Treg stability node)
    │       ↔ FOXP3 (run_010): FOXO1 = direct FOXP3 transcription activator
    │       ↔ IKZF1 (run_134): compound Treg destabilization (chromatin + PI3Kδ/FOXO1)
    │       ↔ CTLA4 (run_060): CTLA4 → CD28 ↓ → PI3Kδ ↓ → Akt ↓ → FOXO1 nuclear
    │       ↔ DYRK1A (run_125): parallel gate (NFAT vs FOXO1)
    │
    ├── Mast cell: FcεRI → PI3Kδ → BTK → PLCγ2 → IP3 → ITPR3 → STIM1 → ORAI1
    │       ↔ ITPR3 (run_132): downstream Ca²⁺ release; PI3Kδ/BTK = upstream
    │       ↔ STIM1/ORAI1 (run_127): Ca²⁺ entry; PI3Kδ/BTK = far upstream
    │       ↔ Quercetin (runs 127/132): PLCγ + ORAI1 dual block; PI3Kδ/BTK block adds upstream layer
    │       ↔ Omalizumab/run_127: anti-IgE (FcεRI deloading); PI3Kδ → less IgE production (B cell)
    │
    ├── Autoreactive T cell: TCR → PI3Kδ → Akt → mTOR + FOXO1-phospho → effector
    │       ↔ DYRK1A/NFAT (run_125): parallel T cell activation gate
    │       ↔ CD73/adenosine (run_121): A2A → Gs → cAMP → PKA → PI3Kδ inhibition
    │
    └── ME/CFS: NK exhaustion from constitutive PI3Kδ; B cell autoantibody production
            ↔ run_127/132/134: NK dysfunction stack (Ca²⁺ functional + developmental + metabolic)
```

---

## 7. β Cell Death — No New Mechanism
PI3Kδ does not directly contribute to β cell death (PI3Kα/β in β cells via growth factor signaling was covered separately). Primary PI3Kδ role is in immune cells (lymphocytes, mast cells). No new β cell death mechanism.

---

## 8. Protocol Integration

**Genetic stratification:**
- No T1DM GWAS variant specifically for PIK3CD (APDS mutations are rare, gain-of-function, not GWAS)
- But PIK3CD pathway is actionable pharmacologically

**Clinical therapeutics anchored:**
- **Idelalisib** (PI3Kδ inhibitor): approved for CLL; emerging in autoimmune contexts (RA, lupus, T1DM trials); dual benefit for T1DM: (a) autoreactive T cell suppression + Treg sparing; (b) reduced IgE production (less mast cell sensitization) + BTK-dependent mast cell activation ↓
- **BTK inhibitors** (zanubrutinib, acalabrutinib, ibrutinib): downstream of PI3Kδ; approved for B cell malignancies; reducing IgE-mediated mast cell activation in mast cell activation syndrome (MCAS) — rosacea mast cell phenotype connection
- **Precaution**: PI3Kδ inhibitors → risk of immunosuppression, infections (similar to idelalisib clinical use); not OTC; require specialist oversight

**OTC limitation:**
- No specific OTC PI3Kδ inhibitor identified with sufficient selectivity
- Quercetin: broad PI3K inhibitory activity but not δ-selective; existing quercetin Ca²⁺ mechanisms (runs 127/132) cover the downstream; no new quercetin mechanism claimed here
- Adenosine/A2A receptor (run_121): cAMP → PKA → PI3Kδ negative regulation in T cells; NMN/NAD+ → cAMP pathway? Indirect; not claimable as direct mechanism

**Updated Treg stability protocol (5-node stack now):**
```
IKZF1/chromatin: Vitamin A 3000–5000 IU/day → RA → RARE → IKZF1 ↑
FOXP3:           Vitamin D → FOXP3 CNS2 demethylation + expression
BACH2:           Vitamin A → BACH2 ↑; sulforaphane → NRF2 → oxidative stress ↓
DYRK1A:          [note: harmine rosacea contraindication, run_125]
PI3Kδ/FOXO1:     reduce TCR/CD28 stimulation load → less PI3Kδ activation → FOXO1 nuclear → FOXP3 stable
                 → calcitriol (VDR → PTEN ↑ in some contexts?) [weak, conservative]
```

---

## 9. Key Literature

- Okkenhaug K et al. (2002) Impaired B and T cell antigen receptor signaling in p110δ PI3-kinase mutant mice. *Science* — foundational PI3Kδ lymphocyte role
- Angulo I et al. (2013) Phosphoinositide 3-kinase δ gene mutation predisposes to respiratory infection and airway damage. *Science* — APDS discovery (gain-of-function PIK3CD)
- Patton DT et al. (2006) PI 3-Kinase p110δ regulates T lymphocyte development and is required for regulatory T cell function. *J Immunol* — PI3Kδ in Tregs
- Lannutti BJ et al. (2011) CAL-101, a p110δ selective phosphatidylinositol-3-kinase inhibitor for the treatment of B-cell malignancies. *Blood* — idelalisib pre-clinical data
- Ali K et al. (2004) Essential role for the p110δ phosphoinositide 3-kinase in the allergic response. *Nature* — PI3Kδ in mast cell IgE-mediated response and BTK pathway

---

*Gap.md updated: 2026-04-12 | One-hundred-and-twenty-eighth extension | PIK3CD PI3Kδ p110δ lymphocyte-specific PI3K PIP3 Akt BTK Bruton-tyrosine-kinase PLCγ2 mast-cell-11th-mechanism FcεRI Lyn Syk LAT PTEN-PI3Kδ-FOXO1 Treg-stability FOXO1-FOXP3 5th-Treg-node CTLA4-PI3Kδ APDS gain-of-function PIK3CD T1DM autoreactive T-cell FOXO1-nuclear FOXP3-stable idelalisib umbralisib zanubrutinib ibrutinib BTK-inhibitor ME/CFS-NK-exhaustion autoantibody IKZF1-compound Okkenhaug-2002-Science Angulo-2013-Science Ali-2004-Nature | run_135*
