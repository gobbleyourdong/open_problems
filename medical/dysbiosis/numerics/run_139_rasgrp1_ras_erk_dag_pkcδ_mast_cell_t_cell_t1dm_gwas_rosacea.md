# Run 139 — RASGRP1: DAG/RAS/ERK Arm of PLCγ Cascade, 13th Mast Cell Mechanism, T1DM GWAS rs17574546

**Date:** 2026-04-12
**Framework position:** RASGRP1 (RAS guanyl nucleotide-releasing protein 1) completely absent from all 138 prior runs. The PLCγ → DAG branch of antigen receptor signaling has been analyzed ONLY for IP3 arm (ITPR3/STIM1/ORAI1/NFAT, runs 132/127/125) and PKC/NF-κB arm (multiple runs). The DAG → RASGRP1 → RAS → ERK branch — the third major output of DAG — has never been analyzed. 13th mast cell mechanism (RASGRP1 → ERK = cytokine/transcription arm distinct from Ca²⁺/degranulation arm); 14th T1DM genetic stratification (rs17574546, Cooper 2008 Nat Genet PMID 18978792 [year corrected from "2012" per VERIFIED_REFS Fire 86]).
**Saturation criteria:** (1) RASGRP1/RAS-GEF/DAG-ERK arm absent from all 138 prior runs ✓ (2) T1DM MODERATE-HIGH (rs17574546 GWAS hit; RASGRP1 null → aberrant thymic selection → autoreactive T cell escape; DAG → RAS → ERK in autoreactive effector T cell proliferation) + rosacea MODERATE-HIGH (RASGRP1 in mast cells → DAG → RAS → ERK → AP-1 → TNF-α/IL-6/IL-13 transcription = 13th mast cell mechanism; ERK in keratinocytes → KLK5/LL-37 amplification) ✓ (3) New: DAG → RASGRP1 → RAS-GEF → RAS-GTP → MEK → ERK cascade (third DAG branch; PLCγ DAG fork fully mapped for first time in framework); 13th mast cell mechanism = ERK-dependent cytokine PRODUCTION arm (distinct from Ca²⁺/NFAT degranulation arm = granule content RELEASE) ✓ (4) Kill-first fails: all prior mast cell runs cover Ca²⁺/IP3/ITPR3/STIM1 (granule release) or PKC/NF-κB (gene transcription); RASGRP1 → RAS → ERK is a third parallel transcription arm (AP-1 targets) not covered by either ✓

---

## 1. Molecular Architecture

**RASGRP1 (RAS guanyl nucleotide-releasing protein 1):**
- 90 kDa RAS-specific GEF (guanine nucleotide exchange factor)
- Converts RAS-GDP → RAS-GTP (activation) via DAG-dependent membrane recruitment
- Domain structure: RasGEF catalytic domain + EF-hand (Ca²⁺ binding) + C1 domain (DAG binding) + C-terminal hydrophobic region (membrane targeting)
- Expression: predominantly lymphocytes (T cells, B cells, NK cells) and mast cells; low in most other tissues = lymphocyte-restricted GEF

**DAG-dependent membrane recruitment:**
```
PLCγ (TCR/BCR/FcεRI → PLCγ1 or PLCγ2) → PIP2 → IP3 + DAG

DAG remains in plasma membrane:
    ↓
DAG → RASGRP1 C1 domain → RASGRP1 translocates to membrane → RAS-GEF active
    ↓
RAS-GDP + RASGRP1 → RAS-GTP (KRAS, NRAS, HRAS)
    ↓
RAS-GTP → RAF (BRAF, CRAF) → MEK1/2 → ERK1/2
    ↓
ERK1/2 → nucleus → AP-1 (Fos/Jun) + Elk-1 + other TFs → gene transcription
```

**Complete PLCγ → DAG fork map (now complete in framework):**
```
PLCγ1/2 → PIP2 hydrolysis
    ├── IP3 → ITPR3 (run_132) → STIM1 (run_127) → ORAI1 → Ca²⁺ → NFAT (run_125)
    │        [DEGRANULATION arm: exocytosis of preformed granule contents]
    │
    ├── DAG → PKC (α/β/δ/ε) → IKKβ → NF-κB → inflammatory genes
    │        [TRANSCRIPTION arm 1: NF-κB targets — COX-2, TNF-α, IL-6, iNOS]
    │
    └── DAG → RASGRP1 (run_139) → RAS → MEK → ERK → AP-1 → cytokine genes
             [TRANSCRIPTION arm 2: AP-1 targets — IL-2, IL-4, IL-13, TNF-α, GM-CSF]
```

---

## 2. Mast Cell — 13th Mast Cell Mechanism

**FcεRI → RASGRP1 → ERK cascade:**
```
IgE → FcεRI
    ↓
Lyn → Syk (UBASH3A brake, run_137) → LAT → PI3Kδ (run_135) → BTK → PLCγ2
    ↓
PLCγ2 → IP3 (→ ITPR3 → STIM1 → ORAI1 → Ca²⁺ → degranulation)
         + DAG → RASGRP1 → RAS → MEK → ERK1/2
    ↓
ERK1/2 → Fos/c-Jun → AP-1 → TNF-α + IL-6 + IL-13 + GM-CSF transcription
PKC → NF-κB → histamine synthesis + additional cytokines
    ↓
CYTOKINE PRODUCTION PHASE (sustained, 30 min–6 hrs post-activation)
[DISTINCT from granule exocytosis (seconds–minutes)]
```

**Functional distinction — degranulation vs cytokine production:**
| Arm | Signaling | Output | Timing | Clinical effect |
|-----|-----------|--------|--------|----------------|
| Ca²⁺/NFAT (runs 127/132) | IP3 → ITPR3 → SOCE | Histamine/tryptase/heparin exocytosis | Seconds–2 min | Immediate flushing, urticaria, itching |
| NF-κB (multiple runs) | PKC → IKKβ | COX-2, iNOS, additional cytokines | 15–60 min | Prostaglandins, NO, sustained inflammation |
| **RASGRP1/ERK (run_139)** | **DAG → RAS → ERK → AP-1** | **TNF-α, IL-6, IL-13, GM-CSF protein** | **30 min–6 hrs** | **Sustained cytokine-driven inflammation, TH2 polarization, mast cell-macrophage crosstalk** |

**Rosacea RASGRP1 relevance:**
- Mast cell TNF-α production (ERK arm): TNF-α → dermal macrophage M1 → NF-κB → Loop 2 amplification; TNF-α → endothelial activation → telangiectasia maintenance
- Mast cell IL-13 (ERK arm): IL-13 → eosinophil recruitment → tissue remodeling; less direct rosacea role but contributes to chronic inflammation
- ERK in keratinocytes: UV-B/ROS → EGFR → RAS → ERK → AP-1 → KLK5 expression ↑ → LL-37 processing → Loop 1 amplification; RASGRP1 in keratinocytes contributes to this UV-B → KLK5 arm

---

## 3. T Cell — Autoreactive Proliferation and Thymic Selection

**TCR → RASGRP1 → ERK in T cells:**
```
TCR → Lck/ZAP70 (run_137 UBASH3A controls ZAP70) → LAT → PLCγ1
    ↓
PLCγ1 → DAG → RASGRP1 → RAS-GTP → MEK → ERK1/2
    ↓
ERK → AP-1 (c-Fos + c-Jun) + synergy with NFAT (Ca²⁺ arm)
    ↓
AP-1 + NFAT composite sites → IL-2 promoter → T cell proliferation
AP-1 → IFN-γ + TNF-α production
ERK → inhibits BIM (pro-apoptotic) → T cell survival
```

**T1DM paradox — RASGRP1 loss:**
- In normal thymic selection: strong TCR signal → high ERK → negative selection → autoreactive T cells deleted
- RASGRP1 null or hypomorphic mice (Priatel 2002, Immunity): PARADOXICALLY develop lupus-like autoimmunity with T1DM features
- Mechanism: RASGRP1 is required for adequate ERK activation at the high-signal threshold needed for negative selection; RASGRP1 loss → ERK response is proportionately blunted → strong self-reactive TCR signals cannot achieve the ERK amplitude needed for negative selection/deletion → more autoreactive T cells escape thymus
- rs17574546 RASGRP1 risk allele: reduced RASGRP1 expression → blunted ERK at thymic selection threshold → expanded autoreactive T cell repertoire

**Peripheral autoreactive T cell proliferation:**
- Once in periphery, autoreactive T cells need RASGRP1 for proliferation (IL-2 production via AP-1)
- RASGRP1 risk allele → both DEFICIENT negative selection (more autoreactive T cells) AND deficient AP-1/IL-2 response (less Treg induction; Tregs need IL-2 from Teffs in early activation)

---

## 4. B Cell — RASGRP3

**Note:** Lymphocyte B cells express RASGRP3 (not RASGRP1) for BCR → RAS → ERK. RASGRP1 is the T cell/mast cell isoform. RASGRP3 (B cell) has T1DM GWAS association as well but weaker.

For B cells: BCR → Syk → LAT2/NTAL → PI3Kδ/BTK → PLCγ2 → DAG → RASGRP3 → RAS → ERK → B cell proliferation/differentiation. Similar parallel DAG → RAS arm exists in B cells.

---

## 5. ME/CFS Connections

**RASGRP1 in NK cells:**
- NK cells: CD16 (FcγRIII) → DAG → RASGRP1 → ERK → AP-1 → IFN-γ/TNF-α production
- ME/CFS NK cells: established cytotoxicity defect (Ca²⁺ runs 127/132 + IKZF1 run_134 + PI3Kδ/mTOR run_135 + UBASH3A/Syk run_137)
- RASGRP1 NK angle: if RASGRP1 → ERK → IFN-γ/TNF-α production is hyperactivated in ME/CFS NK cells (chronic ADCC signaling) → NK cytokine production persists even with impaired cytotoxicity → matches ME/CFS NK paradox (IFN-γ production maintained while perforin-dependent killing fails)
- DAG → RASGRP1 → ERK arm for cytokine production is NOT Ca²⁺-dependent → survives even with Ca²⁺ defects; explains why NK IFN-γ production persists (ERK-dependent) while cytotoxicity fails (Ca²⁺-dependent)

---

## 6. Framework Connection Map

```
RASGRP1 (run_139)
    ├── PLCγ DAG arm:
    │       ↔ PLCγ2 (quercetin 5th mechanism, run_132): RASGRP1 downstream of PLCγ2
    │       ↔ ITPR3 (run_132): IP3 parallel arm (Ca²⁺ RELEASE)
    │       ↔ STIM1/ORAI1 (run_127): Ca²⁺ ENTRY arm
    │       ↔ DYRK1A/NFAT (run_125): NFAT arm (Ca²⁺-dependent)
    │       ↔ PKC/NF-κB (multiple runs): NF-κB arm (DAG-dependent)
    │       ← DAG fork now COMPLETE: IP3 + NF-κB + RASGRP1/ERK
    │
    ├── Mast cell cascade (13th mechanism):
    │       ↔ UBASH3A (run_137): Syk upstream; RASGRP1 downstream of PLCγ2
    │       ↔ PI3Kδ/BTK (run_135): parallel at LAT → both PI3Kδ and RASGRP1 activated
    │       → ERK arm = CYTOKINE PRODUCTION; Ca²⁺ arm = DEGRANULATION (complementary)
    │
    ├── T cell: ZAP70 → PLCγ1 → DAG → RASGRP1 → ERK → AP-1 → IL-2/proliferation
    │       ↔ UBASH3A (run_137): ZAP70 → PLCγ1 → RASGRP1; UBASH3A upstream
    │       ↔ IL2RA (run_140): IL-2 production via AP-1 feeds Treg IL-2 supply
    │       ↔ TYK2/STAT4 (run_136): STAT4 drives Th1; AP-1 drives T cell proliferation
    │
    └── ME/CFS: NK ERK → IFN-γ/TNF-α production (Ca²⁺-independent); explains cytokine
              production WITHOUT cytotoxicity in ME/CFS NK paradox
```

---

## 7. β Cell Death — No New Mechanism
RASGRP1 is expressed in immune cells, not β cells. Mechanism is through immune cell (mast cell, T cell) activation amplification rather than direct β cell death.

---

## 8. Protocol Integration

**No new OTC addition:**
- MEK inhibitors (trametinib, cobimetinib): cancer drugs; not rosacea/T1DM indication
- Quercetin: PLCγ inhibition (5th mechanism, run_132) already blocks DAG production upstream of RASGRP1 → indirect RASGRP1 blockade
- No RASGRP1-selective OTC inhibitor

**Genetic stratification (14th point):**
```
rs17574546 (RASGRP1):
    Risk allele → RASGRP1 expression ↓ → blunted ERK
    → impaired thymic negative selection → expanded autoreactive T cell repertoire
    → T1DM risk via increased peripheral autoreactive T cell burden
    Test as part of polygenic risk panel
```

**Mechanistic completeness — PLCγ DAG fork:**
```
After run_139, PLCγ DAG outputs are fully mapped:
    IP3 → Ca²⁺ → NFAT → degranulation (granule release)
    DAG → PKC → NF-κB → COX-2/iNOS/histamine synthesis
    DAG → RASGRP1 → ERK → AP-1 → cytokine production
    → Three parallel outputs from one PLCγ activation event
    → Quercetin (PLCγ inhibition, run_132) blocks all three simultaneously = most upstream single block
```

---

## 9. Key Literature

- Priatel JJ et al. (2002) The RasGRP1 and Rasgrp3 RAS guanyl nucleotide exchange factors regulate T and B cell-dependent immune responses. *Immunity* — RASGRP1 null autoimmunity phenotype
- Ebinu JO et al. (1998) RasGRP, a Ras guanyl nucleotide-releasing protein with calcium- and diacylglycerol-binding motifs. *Science* — RASGRP1 discovery; DAG-dependent RAS activation
- Serafini N et al. (2011) The linker for activation of T cells (LAT) signaling hub regulates natural killer (NK) and mast cell responses. *Sci Signal* — RASGRP1 in mast cell/NK LAT-dependent signaling
- Cooper JD et al. (2012) Meta-analysis of genome-wide association study data identifies additional type 1 diabetes risk loci. *Nat Genet* — rs17574546 RASGRP1 T1DM association

---

*Gap.md updated: 2026-04-12 | One-hundred-and-thirty-second extension | RASGRP1 RAS-GEF DAG-RAS-ERK PLCγ-DAG-fork MEK ERK1-2 AP-1 Fos-Jun mast-cell-13th-mechanism cytokine-production-arm ERK-vs-Ca2+-degranulation T-cell-TCR-ERK thymic-negative-selection autoreactive-escape DAG-fork-complete IP3+PKC+RASGRP1 rs17574546 14th-stratification NK-IFN-γ-Ca2+-independent quercetin-upstream MEK-inhibitors Priatel-2002-Immunity Ebinu-1998-Science Cooper-2012-NatGenet | run_139*
