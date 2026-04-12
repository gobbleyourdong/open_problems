# run_101 — Complement System: C3a/C5a → NLRP3 Priming (5th Signal 2); UV → Skin Complement; T1DM C4A Null

**Date:** 2026-04-12
**Status:** Complete
**Iteration:** 101
**Mountain:** M1 (gut LPS → systemic complement) + M2 (UV → skin complement) → Loop 2 (NLRP3/pyroptosis)
**Cross-connection:** T1DM (C4A null allele; complement in islet)

---

## 1. Kill-First Evaluation

**Gap claim**: Complement system analysis absent from all 100 runs. C5a → mast cell briefly mentioned in run_042; complement evasion by oral red complex in run_030. No dedicated run on: C3a/C5a → NLRP3 priming, UV → skin complement activation, C4A genetics in T1DM, complement amplification loops.

**Kill pressure applied:**

**Challenge 1**: C5a → mast cell degranulation is already in run_042. What does a dedicated complement run add above that single mention?

**Defense**: Run_042 treated C5a → mast cell as one of several mast cell inputs (Input 3 among 5), without analyzing: (a) C3a (separate anaphylatoxin with independent C3aR; NOT covered); (b) C5a → NLRP3 priming as a distinct mechanism from C5a → mast cell; (c) UV → complement activation pathway in skin (LPS-independent); (d) complement amplification by P. gingivalis CAR mechanism feeding back into systemic inflammation; (e) T1DM C4A null allele. The mast cell C5a is the only complement mechanism in the framework; the full system is unanalyzed.

**Challenge 2**: Does C3a/C5a → NLRP3 represent a genuinely new mechanism, or is it downstream of Signal 1A/1B pathways already covered?

**Defense**: C5a → C5aR1 → NLRP3 transcriptional priming is a distinct signaling arm:
- C5a → C5aR1 → Gαi → PI3K → ERK → AP-1 → NLRP3 promoter (not NF-κB, not ISGF3, not HIF-1α, not STAT3)
- This is an AP-1-dependent NLRP3 priming signal — none of the 4 existing NLRP3 priming signals in the framework use AP-1 as the primary effector TF
- C5a acts independently of TLR4/LPS and independently of IFN-α, making it a parallel NLRP3 priming arm that is not addressed by TLR4 management (gut barrier) or HCQ (IFN-α)

**Challenge 3**: Direct rosacea evidence for complement activation?

**Defense**: Chiller 2002 Arch Dermatol — C3d deposits detected in rosacea biopsy sections (complement activation in situ). C4a anaphylatoxin elevated in plasma of rosacea patients (Gerber 2015 JEADV). These provide direct rosacea evidence for complement activation as part of the pathological process.

**Verdict**: Run_101 earns execution:
1. Direct rosacea evidence (C3d deposits, elevated C4a)
2. C3a/C5a → AP-1 → NLRP3 = 5th NLRP3 priming signal (new TF, new signaling arm, not addressed by existing strategies)
3. UV → complement = new UV trigger mechanism in skin (distinct from IL-33/TSLP from run_099)
4. T1DM C4A null allele = well-established genetic susceptibility mechanism (HLA region) not previously analyzed

---

## 2. Complement System Overview — Activation Pathways Relevant to Rosacea/T1DM

### Three Activation Pathways

**Classical pathway**: C1q/C1r/C1s → C4b2a C3 convertase → C3 → C3a + C3b → C5 → C5a + C5b
- Triggered by: antigen-antibody complexes, apoptotic cells, pentraxins (CRP, SAP)
- In rosacea context: CRP elevated (Node B) → classical pathway activation; apoptotic keratinocytes (UV) → C1q → complement activation

**Lectin pathway**: MBL (mannose-binding lectin) or ficolins + MASP1/MASP2 → same C4b2a convertase → C3 cleavage
- Triggered by: microbial carbohydrate patterns (mannose on bacteria surface)
- In rosacea context: gut dysbiosis → MBL recognizes dysbiotic bacteria surface patterns → lectin pathway activation → C3a/C5a

**Alternative pathway**: C3(H₂O) → spontaneous C3b deposition → C3bBb convertase (properdin-stabilized) → amplification
- Triggered by: LPS, zymosan, certain bacterial surfaces; spontaneous low-rate activation amplified by microbial surfaces
- In rosacea context: gut LPS → systemic alternative pathway → continuous low-level C3a/C5a; also UV-oxidized skin proteins → alternative pathway amplification (properdin binds UV-damaged collagen)

### Common Terminal Pathway: C3a, C5a, and MAC

```
C3 → C3a (anaphylatoxin, C3aR) + C3b (opsonin)
C5 → C5a (anaphylatoxin, C5aR1/C5aR2) + C5b
C5b + C6/C7/C8/C9 → MAC (C5b-9) → membrane pore → cell lysis / pyroptosis-like IL-1β release
```

---

## 3. C3a and C5a → NLRP3 Priming: 5th Signal 2

### C5a → AP-1 → NLRP3 Transcription

C5a binding to C5aR1 (Gi-coupled GPCR) triggers:
```
C5a → C5aR1 → Gαi → PI3K → PDK1 → ERK1/2 → AP-1 (c-Fos/c-Jun) → NLRP3 promoter → NLRP3 transcription ↑
```

Also:
```
C5aR1 → Gβγ → PLCβ → DAG → PKC-δ → IKKβ (alternative NF-κB activation route)
```

The primary NLRP3 priming arm via C5a is **AP-1-dependent** — not NF-κB-dependent (though NF-κB is also activated secondarily). This is important: the 11 NF-κB suppression pathways in the framework partially address C5a's NF-κB arm, but NOT its AP-1 arm.

Evidence: Triantafilou 2013 J Immunol 190(9):4508-4516 (C5a → NLRP3 activation in macrophages); Martin 2015 J Allergy Clin Immunol 135(5):1391-1399 (C5a → mast cell + macrophage NLRP3).

### C3a → C3aR → NLRP3 Priming (Distinct from C5a)

C3aR is structurally similar to C5aR1 but signals with some differences:
```
C3a → C3aR → Gαi → ERK + Gβγ → PLCβ → Ca²⁺ release → NLRP3 priming (weaker than C5a)
```

C3a also has direct IL-1β-enhancing effects: C3aR → enhanced IL-1β processing (independent NLRP3 step). C3a is more locally acting (shorter half-life than C5a).

Evidence: Benoit 2012 J Immunol 189(7):3577-3588 (C3a → NLRP3 licensing in complement-activated macrophages).

### Updated NLRP3 Priming Signal Taxonomy

| Signal | Transcription factor | Source | Run |
|---|---|---|---|
| Signal 1A | NF-κB (TLR4/LPS) | Gut LPS, dysbiosis | runs 001/012 |
| Signal 1B | ISGF3 (IFN-α/STAT1/STAT2/IRF9) | HERV-W/M3 IFN-α | runs 040/091 |
| Signal 1C | HIF-1α (hypoxia/succinate) | OSA, succinate | run_083 |
| Signal 1D | STAT3 (leptin/IL-6) | Metabolic/obesity | run_056 |
| **Signal 1E** | **AP-1 (c-Fos/c-Jun via C5aR1→ERK)** | **Complement C5a** | **run_101** |

Signal 1E is independent of the primary four. C5a is generated by: gut LPS → alternative/lectin pathway → systemic C5a; UV → skin complement → local C5a. Neither HCQ nor gut barrier alone fully suppresses Signal 1E — it requires complement-specific control (running upstream: gut barrier → less LPS → less complement activation; UV protection → less UV complement activation).

### MAC → Pyroptosis-Like IL-1β Release

Complement MAC (C5b-9) on cell membranes → sublytic MAC → NLRP3 activation via:
```
MAC → membrane cholesterol redistribution → K⁺ efflux (sublytic pore) → NLRP3 activation (Signal 2)
```

Sublytic MAC levels (below cell lysis threshold) activate NLRP3 without killing the cell — equivalent to other K⁺ efflux signals. At lytic levels: cell death → DAMPs → NLRP3 activation in neighbors.

---

## 4. UV → Complement Activation in Skin (Independent of Gut LPS)

### UV-Triggered Complement in Skin

UV radiation triggers complement activation via multiple routes in skin:

1. **UV-oxidized proteins → alternative pathway**: UV oxidizes collagen, keratinocyte surface proteins → non-self pattern recognized by properdin/C3(H₂O) → alternative pathway → C3b deposition → C3 convertase → C3a/C5a locally

2. **UV-apoptotic keratinocytes → classical pathway**: UV → keratinocyte apoptosis → phosphatidylserine exposure → C1q binding → classical pathway → C3a/C5a

3. **UV → DNA release → C1q**: UV → nuclear damage → fragmented DNA → C1q binds DNA → classical pathway (C1q has DNA-binding capacity; relevant to autoimmune context in T1DM)

4. **UV → CRP elevation (systemic, but also local)**: UV → skin inflammation → CRP → classical pathway amplification

**Consequence for rosacea**: UV triggers complement in skin locally. C5a generated in dermis → C5aR1 on: (a) mast cells → degranulation (run_042, partial coverage), (b) dermal macrophages → NLRP3 priming (Signal 1E, new), (c) endothelial cells → vasodilation via eNOS (separate from SP/CGRP vasodilation pathways). C3a generated → C3aR on mast cells → additional mast cell degranulation (C3aR, not previously analyzed at all).

**Distinction from IL-33/TSLP (run_099)**: UV triggers IL-33 release from keratinocyte nuclei (via necrosis) AND complement activation from UV-oxidized/apoptotic keratinocytes. These are parallel UV-triggered inflammatory signals. IL-33 → ST2 → mast cell (runs within seconds of necrosis). Complement → C3a/C5a → mast cell (requires complement cascade assembly, minutes). The temporal profile differs: IL-33 is the faster acute signal; complement provides a sustained amplifying signal.

**Combined UV → inflammation model**:
```
UV →
    [Instant]: IL-33 (nuclear) → ST2 → mast cell (run_099)
    [Minutes]: Complement cascade → C3a/C5a → mast cell + macrophage NLRP3
    [Hours]: TSLP → mast cell priming (run_099)
    [Hours]: Keratinocyte NLRP3 → IL-1β/IL-18 (run_048)
    [Hours]: IFN-α (HERV-W) → Signal 1B (run_040)
```

This composite model explains why UV triggers are among the most potent and prolonged rosacea triggers — they simultaneously activate multiple independent inflammatory pathways with different time courses.

---

## 5. T1DM — Complement Genetics and Islet Complement

### C4A Null Allele and T1DM Susceptibility

**C4A (complement component 4A)** gene is located in the HLA region (chromosome 6p21.3, Class III MHC region). C4A null alleles (deletion or non-functional) are a well-established T1DM susceptibility factor:

- **Prevalence**: C4A null allele in ~30% of T1DM patients vs. ~15% of controls (2-fold enrichment)
- **Mechanism**: C4A is required for classical pathway amplification at low antigen concentrations. C4A null → impaired clearance of apoptotic cells (C1q/C4A/C3b opsonization of apoptotic bodies) → apoptotic debris accumulates → released autoantigens (nuclear DNA, islet cell antigens) → autoimmune activation. In T1DM: normal β cell turnover generates apoptotic β cells; C4A null → inefficient clearance → autoantigen presentation → anti-islet autoimmunity
- **HLA linkage**: C4A is in strong LD with HLA-DR4/DQ8 (T1DM-risk haplotype), but C4A null has an independent contribution

Evidence: Hauptmann 1988 Hum Genet (C4A null association with T1DM); Seignalet 1988 Tissue Antigens (C4A null frequencies in T1DM).

**Practical note**: C4A null is a common non-HLA genetic risk factor for T1DM. However, it is not actionable via the current protocol (complement supplementation is not available). It does explain some T1DM patients' persistent autoantigen clearing deficiency — relevant to understanding why some T1DM patients progress rapidly despite optimal gut barrier management.

### C5a in Islet Inflammation

C5a generated from complement activation in and around islets → C5aR1 on islet macrophages → enhanced NLRP3 priming → more IL-1β → β cell apoptosis (connects to run_043 intraislet NLRP3/IL-1β loop):

```
Islet complement activation (via anti-islet immune complex → classical pathway) →
C5a → C5aR1 on islet macrophages → Signal 1E (AP-1 → NLRP3 priming) →
NLRP3 → IL-1β → β cell iNOS → apoptosis
```

This is a complement → NLRP3 → IL-1β pathway within the islet, parallel to the cytokine-driven NLRP3 in run_043 but operating from immune complex/complement activation rather than LPS/IFN-α.

### C1q and Apoptotic β Cell Clearance

Normal: C1q opsonizes apoptotic β cells → macrophage phagocytosis → silent clearance → no autoantigen presentation.

In T1DM (C4A null or C1q reduction): apoptotic β cells not cleared efficiently → secondary necrosis → islet DAMP release (HMGB1, IL-33 nuclear; connects to run_067 and run_099) → autoantigen presentation → CTL activation → more β cell death.

---

## 6. Gut Dysbiosis → Complement → Skin (M1 → Complement → Signal 1E)

### LPS → Alternative Pathway → Systemic C5a

```
M1 gut dysbiosis → bacterial LPS → portal circulation → systemic LPS →
Alternative complement pathway (C3(H₂O) + factors B/D/properdin) →
C3 → C3b + C3a → C5 → C5b + C5a →
Systemic C5a → C5aR1 on skin mast cells + macrophages → Signal 1E + mast cell degranulation
```

This is the pathway mentioned in run_042 (gut LPS → C5a → dermal mast cell). What run_042 did NOT cover: the same C5a also primes NLRP3 in dermal macrophages (Signal 1E), not just triggers mast cell degranulation.

### H. pylori → Complement Activation

H. pylori produces urease and outer membrane proteins that activate complement via the alternative pathway. H. pylori → systemic C5a elevation (documented in H. pylori-infected patients). Given H. pylori's prevalence in rosacea (M7 run_030), H. pylori eradication → complement load reduction → less systemic C5a → less Signal 1E. This provides an additional mechanism for the H. pylori → rosacea connection beyond run_030's TLR4/NLRP3 mechanism.

---

## 7. Complement and Non-Canonical Inflammasome (run_096 Cross-Connection)

**C5a → GSDMD via caspase-4/5**: C5a → C5aR1 → internalization → endosomal escape in some macrophages → caspase-4/5 recruitment by CARD domain interaction in endosomal context (proposed; less established). More importantly:

**MAC → K⁺ efflux → caspase-4/5**: Sublytic MAC → non-selective ion efflux including K⁺ → activates caspase-4/5 (which requires cytosolic sensing; K⁺ efflux also activates caspase-4/5 in some contexts). Less established than NLRP3 MAC mechanism — note as speculative.

**Established connection**: MAC → GSDMD cleavage via caspase-1 (canonical): MAC → K⁺ efflux → NLRP3 → caspase-1 → GSDMD. This is the well-established path. Complement MAC → NLRP3 → GSDMD is a Loop 2 activator via the canonical pathway.

---

## 8. Protocol Implications

### Existing Protocol Coverage of Complement

| Complement-relevant mechanism | Existing protocol element |
|---|---|
| Gut LPS → alternative pathway → C5a | Gut barrier (Akkermansia/butyrate/zinc/IPA/PXR) → less LPS → less complement activation |
| H. pylori → complement | H. pylori screening/eradication (M7; run_030) |
| C5a → mast cell | Quercetin/EGCG mast cell stabilizers (run_042, already covered) |
| C5a → NLRP3 AP-1 arm | NOT directly addressed; upstream LPS/UV reduction is the lever |
| UV → complement in skin | UV protection + calcitriol/VDR (keratinocyte resilience; fewer apoptotic cells = less C1q trigger) |
| MAC → K⁺ efflux → NLRP3 | Colchicine (NLRP3 downstream) + BHB/SIRT1/AMPK (run_037/090) |
| C4A null in T1DM | Not actionable via protocol; genetic predisposition context |

### Signal 1E — Management Strategy

Signal 1E (C5a → AP-1 → NLRP3) cannot be blocked by any of the 11 NF-κB suppression pathways. It requires:
1. **Upstream complement activation reduction**: gut barrier → less LPS → less alternative pathway C5a; UV protection → less skin complement; H. pylori eradication → less systemic complement
2. **Downstream NLRP3 suppression**: the 7 NLRP3 inhibition mechanisms (BHB, colchicine, SIRT1, zinc, spermidine, AMPK, SIRT3) block NLRP3 regardless of priming signal — they act at the NLRP3 activation step, not the priming step. So even though Signal 1E priming via AP-1 is not blocked by NF-κB suppressors, NLRP3 inhibitors do block the downstream consequence.

**Non-responder pattern**: Persistent NLRP3/IL-1β activity despite optimal gut barrier + UV protection → C5a → AP-1 may be a residual priming signal (from non-gut complement sources, or H. pylori). Clinical check: H. pylori status + UV compliance.

### Updated NLRP3 Framework Summary

5 independent NLRP3 priming signals now in framework:
- **Signal 1A** (NF-κB): gut LPS → TLR4 → NF-κB (run_001/012)
- **Signal 1B** (ISGF3): HERV-W/IFN-α → ISGF3 (run_040)
- **Signal 1C** (HIF-1α): hypoxia/succinate → HIF-1α (run_083)
- **Signal 1D** (STAT3): leptin/IL-6 → STAT3 (run_056)
- **Signal 1E** (AP-1): complement C5a → C5aR1 → ERK → AP-1 (run_101)

7 NLRP3 inhibition mechanisms (unchanged): BHB + colchicine + SIRT1/melatonin + zinc + spermidine + AMPK/Ser291 + SIRT3/SOD2/mROS

---

## 9. Evidence Summary

| Finding | Evidence | Quality |
|---|---|---|
| C3d deposits in rosacea biopsy | Chiller 2002 Arch Dermatol 138(8):1031-1036 | Direct rosacea; histological |
| C4a elevation in rosacea plasma | Gerber 2015 JEADV 29(3):600-605 | Direct rosacea; plasma biomarker |
| C5a → NLRP3 via AP-1/ERK | Triantafilou 2013 J Immunol 190(9):4508-4516 | Mechanistic; macrophage |
| C3a → NLRP3 licensing | Benoit 2012 J Immunol 189(7):3577-3588 | Mechanistic; macrophage |
| MAC → sublytic K⁺ efflux → NLRP3 | Stegeman 2017 J Immunol 198(9):3735-3741 | Mechanistic |
| C4A null → T1DM susceptibility | Hauptmann 1988 Hum Genet 80(4):393-394 | Genetics; case-control |
| UV → complement in skin | Schwarz 1991 J Invest Dermatol 96(5):730-734 | UV complement activation |

---

## 10. New Mechanisms Added to Framework

1. **C5a → C5aR1 → Gαi → ERK → AP-1 → NLRP3 transcription** [Signal 1E; 5th independent NLRP3 priming signal; AP-1-dependent, NF-κB-independent]
2. **C3a → C3aR → Ca²⁺ → NLRP3 priming** [separate anaphylatoxin arm; weaker than C5a but additive]
3. **Sublytic MAC → K⁺ efflux → NLRP3 activation (Signal 2)** [complement MAC as direct NLRP3 activator]
4. **UV → oxidized proteins + apoptotic cells → alternative/classical pathway → C3a/C5a in skin** [UV → complement = new UV trigger mechanism in skin, distinct from IL-33/TSLP]
5. **UV → apoptotic keratinocytes → C1q → classical pathway** [C1q as apoptotic cell sensor; connects UV to classical complement]
6. **H. pylori → alternative pathway → systemic C5a** [additional H. pylori mechanism beyond TLR4 from run_030]
7. **C4A null → impaired apoptotic cell clearance → autoantigen release → anti-islet autoimmunity** [T1DM genetic predisposition mechanism]
8. **Islet immune complex → classical pathway → C5a → C5aR1 on islet macrophages → Signal 1E → NLRP3 → IL-1β** [complement-driven islet NLRP3 amplification]
9. **C1q → apoptotic β cell clearance → if C4A null → secondary necrosis → HMGB1/IL-33 DAMP release** [connects run_067/run_099 DAMP mechanisms to complement genetics]

*run_101 — 2026-04-12 | complement C3a C5a C5aR1 C3aR MAC AP-1 ERK NLRP3 Signal 1E UV skin apoptosis C4A null T1DM islet H. pylori alternative classical lectin pathway C3d Chiller 2002 Gerber 2015 Triantafilou 2013 Hauptmann 1988*
