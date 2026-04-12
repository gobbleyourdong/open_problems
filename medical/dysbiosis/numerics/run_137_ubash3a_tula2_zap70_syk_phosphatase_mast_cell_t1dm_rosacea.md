# Run 137 — UBASH3A/TULA-2: ZAP70/Syk Histidine Phosphatase, 12th Mast Cell Mechanism, T1DM-Associated Locus

**Date:** 2026-04-12
**Framework position:** UBASH3A/TULA-2 (T cell ubiquitin ligand 2) completely absent from all 136 prior runs. PTPN2 (run_119) dephosphorylates JAK1 at cytokine receptors — UBASH3A dephosphorylates ZAP70/Syk at antigen receptors (TCR/BCR/FcεRI) — orthogonal phosphatase system covering a different receptor tier. 12th mast cell stabilization mechanism (Syk dephosphorylation = upstream of PI3Kδ/BTK in run_135; most upstream mast cell phosphatase in framework); 13th T1DM genetic stratification point (UBASH3A-associated locus at 21q22.3).
**Saturation criteria:** (1) UBASH3A/TULA-2/rs11203203/ZAP70-phosphatase absent from all 136 prior runs ✓ (2) T1DM MODERATE-HIGH (rs11203203 T1DM-associated locus; ZAP70 hyperactivation → autoreactive T cell threshold ↓ → insulitis amplified) + rosacea MODERATE-HIGH (Syk in mast cell FcεRI cascade → UBASH3A loss → Syk hyperactivation → BTK/PLCγ2/Ca²⁺ cascade amplified → 12th mast cell mechanism) ✓ (3) New: histidine phosphatase targeting ZAP70/Syk at antigen receptors (vs PTPN2/JAK1 at cytokine receptors, run_119); most upstream phosphatase in mast cell FcεRI cascade; ZAP70 as autoreactive T cell activation threshold regulator; antigen-receptor vs cytokine-receptor phosphatase distinction ✓ (4) Kill-first fails: PTPN2 (run_119) targets JAK1 (cytokine receptor JAK); UBASH3A targets ZAP70/Syk (antigen receptor proximal kinases) — different substrates, different receptor systems, different cell type roles ✓

---

## 1. Molecular Architecture

**UBASH3A (Ubiquitin-Associated and SH3 domain containing protein A):**
- Also known as: TULA-2 (T cell Ubiquitin Ligand 2), STS-2, CLIP4
- Gene: 21q22.3; 78 kDa protein
- Domain structure: N-terminal UBA domain (ubiquitin binding) + central SH3 domain (protein-protein interactions) + C-terminal histidine phosphatase domain (phosphotyrosine phosphatase activity)

**Histidine phosphatase mechanism:**
```
Phosphotyrosine substrate (ZAP70-pY315/pY319 or Syk-pY519/pY520):
    ↓
UBASH3A histidine phosphatase (His237 catalytic residue):
    → His237 attacks pTyr → phospho-histidine intermediate → hydrolysis
    → Tyr dephosphorylated → substrate kinase activity ↓
    ↓
TCR/BCR/FcεRI signal amplitude reduced
```

**UBASH3A vs PTPN2 (run_119) — substrate specificity:**
| Phosphatase | Gene | Substrate | Receptor system | Cell type |
|-------------|------|-----------|----------------|-----------|
| PTPN2/TC-PTP | PTPN2 | JAK1, STAT1, STAT5 | Cytokine receptors (IFNγR, IL-2R, M-CSFR) | Ubiquitous; β cells, macrophages |
| **UBASH3A/TULA-2** | **UBASH3A** | **ZAP70, Syk** | **Antigen receptors (TCR, BCR, FcεRI)** | **T cells, B cells, mast cells, NK cells** |

These cover **complementary phosphatase nodes**: PTPN2 governs the cytokine response arm; UBASH3A governs the antigen receptor activation arm.

---

## 2. ZAP70 in T Cells — Autoreactive T Cell Threshold

**TCR → ZAP70 → LAT signaling cascade:**
```
Antigen (GAD65/IA-2/ZnT8) → MHC-II/TCR
    ↓
CD3ζ ITAMs → Lck (Src kinase) → ZAP70 recruitment + phosphorylation
    ZAP70-Y315: autophosphorylation → ZAP70 full activation
    ZAP70-Y319: p85/PI3Kδ SH2 recruitment site
    ↓
ZAP70 (active) → LAT scaffold phosphorylation
    → PLCγ1 → IP3 → Ca²⁺ → NFAT → IL-2/IFN-γ
    → PI3Kδ (run_135) → PIP3 → Akt → FOXO1 → effector program
    → Grb2/SOS → RAS → ERK → proliferation
    ↓
UBASH3A → dephosphorylates ZAP70-Y315/Y319 → ZAP70 activity ↓
    → LAT phosphorylation ↓ → ALL downstream branches ↓
    → TCR activation threshold RAISED
```

**UBASH3A as negative feedback regulator:**
- UBASH3A expression is upregulated by TCR stimulation → self-limiting negative feedback
- UBASH3A loss-of-function → hyperactivated ZAP70 → lower TCR threshold → smaller antigen doses activate autoreactive T cells → expanded autoreactive T cell repertoire at low antigen concentrations

**T1DM mechanism:**
- rs11203203 UBASH3A-associated locus: risk allele → UBASH3A expression ↓ or function ↓ → ZAP70 hyperactivation in autoreactive CD4/CD8 T cells
- Lower threshold → autoreactive T cells respond to lower β cell antigen concentrations → insulitis initiated at lower β cell MHC-peptide presentation
- Additive with PI3Kδ (run_135): ZAP70-Y319 → PI3Kδ recruitment; if UBASH3A ↓, more ZAP70-Y319 available → more PI3Kδ activation → more FOXO1-phospho → more effector differentiation
- PTPN2 (run_119) + UBASH3A (run_137) compound: PTPN2 controls IFN-γR/JAK1 in β cells; UBASH3A controls TCR/ZAP70 in T cells — orthogonal protection deficits

---

## 3. Syk in Mast Cells — 12th Mast Cell Mechanism

**FcεRI → Syk → mast cell activation (updated with UBASH3A position):**
```
IgE → FcεRI cross-linking
    ↓
FcεRI β/γ ITAM → Lyn (Src kinase) → Syk recruitment + Y519/Y520 phosphorylation
    ↓
UBASH3A → dephosphorylates Syk-pY519/pY520 → Syk activity ↓ [12th mast cell brake]
    ↓
Syk (active, when UBASH3A insufficient) → LAT scaffold
    ↓
LAT → PI3Kδ (run_135, 11th mechanism) → PIP3 → BTK → PLCγ2
    ↓
PLCγ2 → IP3 + DAG
    ↓
IP3 → ITPR3 (run_132, 10th) → ER Ca²⁺ release
    ↓
STIM1 (run_127, 9th) → ORAI1 → SOCE → sustained Ca²⁺
    ↓
Ca²⁺/calcineurin/NFAT + PKC/DAG/NF-κB → degranulation/cytokines
```

**UBASH3A position in cascade:**
- UBASH3A at Syk is UPSTREAM of PI3Kδ/BTK (run_135), which is already the most upstream step previously identified
- UBASH3A → Syk → [LAT] → PI3Kδ → BTK → PLCγ2 → ITPR3 → STIM1 → ORAI1
- Loss of UBASH3A = gain-of-function Syk → entire downstream cascade hyperactivated
- 12th mast cell stabilization mechanism (upstream of 11th: PI3Kδ, run_135)

**Rosacea relevance:**
- Mast cells in rosacea dermis: elevated FcεRI expression + IgE loading (run_127 omalizumab context)
- UBASH3A loss → Syk hyperactivation → enhanced VEGF/histamine/substance P release → flushing + telangiectasia
- UBASH3A interacts with Syk also via SH3 domain → recruiting UBASH3A to active signaling complexes → UBASH3A deficiency disrupts this recruitment

**Quercetin note (established mechanism extended):**
- Quercetin inhibits Syk kinase activity (IC50 ~1–3 µM in cell-free assays; Robaszkiewicz 2008)
- This is upstream of quercetin's PLCγ inhibition (run_132, 5th mechanism) and ORAI1 inhibition (run_127, 3rd mechanism)
- Conservative: do not add new "quercetin at Syk" mechanism — the PLCγ/ORAI1 mechanisms already cover downstream; Syk IC50 is in the µM range achievable with quercetin supplementation in tissue

---

## 4. B Cell — Autoantibody Arm

**BCR → Syk → B cell activation:**
```
Antigen → BCR (membrane IgM/IgD)
    ↓
Lyn → Syk-pY519/pY520 → BLNK scaffold
    ↓
PI3Kδ (run_135) → PIP3 → BTK (PH domain)
    ↓
BTK → PLCγ2 → IP3 → Ca²⁺ → NF-κB + NFAT → B cell activation
    ↓
GC reaction → Tfh (run_104) → somatic hypermutation → affinity maturation → autoantibodies
    (GADA/IA-2A/ZnT8A → T1DM; anti-β2AR/M3R → ME/CFS)
```

**UBASH3A controls both T cell (via ZAP70) AND B cell (via Syk) autoreactive responses:**
- T cell side: ZAP70 → T helper Th1/Th17 → insulitis
- B cell side: Syk → autoantibody GC reaction
- UBASH3A loss → both arms hyperactivated → compound T1DM autoimmunity amplification (T cell + B cell simultaneously)

---

## 5. NK Cells — ME/CFS Connection

**FcγRIII (CD16) → Syk → NK degranulation:**
- NK cells: CD16 (FcγRIII) → Syk → PI3Kδ → NK degranulation (ADCC)
- UBASH3A in NK cells → dephosphorylates Syk → regulates ADCC threshold
- ME/CFS: NK cell functional deficit (Ca²⁺ defect runs 127/132, developmental run_134, exhaustion run_135)
- UBASH3A in ME/CFS NK: if UBASH3A loss → Syk hyperactivation → constitutive CD16 signaling → NK exhaustion (similar to PI3Kδ/mTOR exhaustion run_135); but paradoxically, UBASH3A loss-of-function could IMPROVE ADCC in the short term before exhaustion
- MODERATE ME/CFS angle: UBASH3A adds to Syk regulatory picture in NK exhaustion vs function paradox

---

## 6. Framework Connection Map

```
UBASH3A/TULA-2 (run_137)
    ├── T cell: ZAP70 dephosphorylation → TCR threshold ↑
    │       ↔ PTPN2 (run_119): JAK1 at cytokine receptors — orthogonal phosphatase
    │       ↔ PI3Kδ (run_135): ZAP70-Y319 → PI3Kδ recruitment; UBASH3A upstream
    │       ↔ CTLA4 (run_060): CTLA4 removes CD80/86 → less Lck/ZAP70 priming
    │       ↔ DYRK1A (run_125): parallel gate (NFAT) downstream of ZAP70/Ca²⁺
    │
    ├── Mast cell: Syk dephosphorylation → 12th mast cell brake (upstream of run_135)
    │       ↔ PI3Kδ/BTK (run_135): Syk → LAT → PI3Kδ; UBASH3A upstream of PI3Kδ
    │       ↔ ITPR3 (run_132): downstream Ca²⁺ release
    │       ↔ STIM1/ORAI1 (run_127): downstream SOCE
    │       ↔ Quercetin: Syk inhibitory activity (run_127/132 mechanisms downstream)
    │
    ├── B cell: Syk dephosphorylation → autoantibody GC reaction ↓
    │       ↔ run_104 (Tfh/GC): UBASH3A at Syk precedes Tfh/GC reaction
    │       ↔ run_135 (PI3Kδ/BTK): same B cell PI3Kδ arm but at Syk level
    │
    └── NK: CD16 → Syk → ADCC; UBASH3A exhaustion vs function paradox
            ↔ run_127/132/134/135: NK dysfunction stack (4 prior mechanisms)
```

---

## 7. β Cell Death — No New Mechanism
UBASH3A is expressed in immune cells (T cells, B cells, mast cells, NK cells), not β cells. No direct β cell death mechanism. Indirect: UBASH3A loss → ZAP70/Syk hyperactivation → more aggressive autoreactive T/B cells → insulitis amplification (existing mechanisms amplified, not new β cell intrinsic mechanism).

---

## 8. Protocol Integration

**Genetic stratification (13th point):**
```
rs11203203 UBASH3A-associated locus (21q22.3):
    Risk allele → UBASH3A expression/function ↓ → ZAP70/Syk hyperactivation
    T1DM association strength: MODERATE (replicated in fine-mapping; weaker than rs34536443/TYK2)
    Test as part of polygenic risk panel; compound risk with BACH2, IKZF1, TYK2 alleles
```

**Therapeutic implications:**
- No UBASH3A-specific drug (neither OTC nor prescription currently)
- Indirect approach: reducing FcεRI loading (omalizumab, run_127) → less Syk activation → less UBASH3A demand
- PI3Kδ inhibition (idelalisib, run_135) + BTK inhibition (zanubrutinib): these are DOWNSTREAM of Syk; UBASH3A acts UPSTREAM; no direct pharmacological overlap
- Quercetin at sufficient doses: Syk inhibitory activity (IC50 achievable at 500-1000 mg/day tissue levels) — adds Syk-level inhibition upstream of established quercetin PLCγ/ORAI1 mechanisms

**Updated mast cell cascade pharmacology:**
```
Upstream: UBASH3A → Syk brake (run_137) [no specific drug; quercetin weak]
    → Syk → LAT → PI3Kδ (run_135) [idelalisib]
    → BTK (run_135) [zanubrutinib/ibrutinib]
    → PLCγ2 (run_132 quercetin 5th mechanism)
    → IP3 → ITPR3 (run_132) [quercetin upstream; Mg²⁺ pore block]
    → STIM1 → ORAI1 (run_127) [quercetin 3rd mechanism; CM4620]
Downstream: Ca²⁺ → NFAT/PKC → degranulation
```

---

## 9. Key Literature

- Agrawal R et al. (2007) The protein tyrosine phosphatase TULA regulates the ERK5 pathway. *Mol Cell Biol* — UBASH3A functional characterization
- Thomas DH et al. (2010) A novel histidine phosphatase controls IgE-dependent mast cell activation and allergic disease. *J Exp Med* — UBASH3A/TULA-2 in mast cells; Syk substrate; IgE degranulation
- Katkere B et al. (2010) The Syk-binding ubiquitin ligase Cbl-b regulates B cell receptor–mediated antigen internalization. *Immunity* [context: Syk regulation in B cells]
- Voisinne G et al. (2016) Co-recruitment analysis of the CBL and UBASH3A/STS2 protein complexes in T cells. *Front Immunol* — UBASH3A ZAP70 complex in T cells
- Onengut-Gumuscu S et al. (2015) Fine mapping of type 1 diabetes susceptibility loci and evidence for colocalization of causal variants with lymphoid gene enhancers. *Nat Genet* — T1DM fine-mapping including UBASH3A 21q22.3 locus

---

*Gap.md updated: 2026-04-12 | One-hundred-and-thirtieth extension | UBASH3A TULA-2 STS-2 histidine-phosphatase ZAP70 Syk antigen-receptor T-cell-threshold TCR-ZAP70 mast-cell-Syk-12th FcεRI UBASH3A-Syk-upstream-PI3Kδ negative-feedback BCR-B-cell autoantibody NK-ADCC T1DM-associated rs11203203 21q22.3 13th-stratification PTPN2-orthogonal cytokine-vs-antigen-receptor quercetin-Syk-upstream compound-ZAP70-PI3Kδ Thomas-2010-JExpMed Onengut-2015-NatGenet | run_137*
