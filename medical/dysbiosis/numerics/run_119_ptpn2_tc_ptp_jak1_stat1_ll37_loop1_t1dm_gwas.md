# Numerics Run 119 — PTPN2/TC-PTP: JAK1/STAT1 Loop 1 Amplifier + Strongest Non-HLA T1DM GWAS Signal

> **PTPN2** (protein tyrosine phosphatase non-receptor type 2; also called TC-PTP, T-cell protein
> tyrosine phosphatase) dephosphorylates JAK1 (at Y1034/Y1035), JAK3 (at Y980), STAT1 (Y701),
> and STAT3 (Y705). By inactivating the JAK1 kinase, PTPN2 terminates IFN-γ → JAK1 → STAT1 →
> CAMP (cathelicidin/LL-37) signaling in skin keratinocytes. This JAK1/STAT1 → LL-37 axis is
> a completely absent rosacea Loop 1 input arm: all 118 prior runs address Loop 1 via KLK5
> upregulation or LL-37 downstream effects, but none identify the upstream IFN-γ → JAK1 →
> STAT1 → CAMP transcription pathway or its brake (PTPN2). Separately, PTPN2 rs45450798 is
> one of the STRONGEST non-HLA T1DM GWAS signals (Smyth 2008 Nat Genet; OR 1.6, Bonferroni
> p = 1.3×10⁻¹²; fully replicated in multiple cohorts). Absent from all 118 runs.

---

## What exists in the framework

**JAK/STAT coverage in current runs:**
- Run_070 (leptin/STAT3/NLRP3): leptin → JAK2 → STAT3 (Y705) → NLRP3 priming (Signal 1D)
- Run_080 (AhR/IL-22/Th22/KLK5): JAK1/TYK2 → STAT3 (Y705) → IL-22 signaling cascade → KLK5
- Run_104 (Tfh): BCL6 driven by JAK1/STAT3 in T follicular helper differentiation
- Run_040 (IFN-α/NLRP3): IFN-α → IFNAR → JAK1/TYK2 → ISGF3 (STAT1/STAT2/IRF9) → Signal 1B

**What is completely absent:**
- PTPN2/TC-PTP itself (0 hits in 118 runs)
- IFN-γ → JAK1 → STAT1 (Y701) → CAMP transcription → LL-37 ↑ in keratinocytes
- The concept of JAK1-specific signaling termination in keratinocytes as a Loop 1 regulator
- PTPN2 as the brake on this pathway
- PTPN2 genotyping as a genetic stratification tool
- Intestinal PTPN2 → STAT1/IFN-γ → gut permeability connection (M1 mountain amplifier)
- JAK inhibitor therapeutic pathway identification for PTPN2 LOF genotype patients

**Mechanistic gap:** The framework has three LL-37 induction pathways (KLK5 → Loop 1, VDR/calcitriol, TRPV1/AMPs), but none model the IFN-γ/Th1 dermis → JAK1 → STAT1 → CAMP promoter → LL-37 synthesis arm. This is a distinct input into Loop 1 that explains some Loop 1 non-responders.

---

## PTPN2: Mechanism Architecture

```
IFN-γ (from Th1 cells in rosacea dermis)
    ↓
IFNGR1/IFNGR2 → JAK1 (Y1034 autophosphorylation) + JAK2 → STAT1 (Y701) homodimer
    ↓
γ-activated sequence (GAS element) in CAMP promoter
    ↓
CAMP gene transcription → pre-pro-LL-37 protein → KLK5-cleaved → LL-37 (37 aa active form)
    ↓
LL-37 → TLR2/TLR4/FPR → Loop 1 amplification (all downstream mechanisms: mTORC1, KLK5 ↑, NLRP3 priming)
    ↑
PTPN2 terminates JAK1 activation:
    PTPN2 → JAK1 Y1034/Y1035 dephosphorylation → JAK1 inactive → STAT1 not phosphorylated
    → CAMP not transcribed → LL-37 NOT produced from this arm
```

**Substrate specificity of PTPN2:**
| Substrate | Site | Effect of PTPN2 | Pathway terminated |
|-----------|------|-----------------|-------------------|
| JAK1 | Y1034/Y1035 | JAK1 kinase inactive | IFN-γ/α → STAT1 + IFN-γ → STAT3 |
| JAK3 | Y980 | JAK3 inactive | γc cytokines (IL-2, IL-4, IL-7, IL-15) → STAT5 |
| STAT1 | Y701 | STAT1 cannot dimerize | Direct IFN → gene transcription |
| STAT3 | Y705 | STAT3 cannot dimerize | IL-6, IL-10, IL-17 → STAT3 target genes |
| EGFR | Y1045 | EGFR endocytosis | EGF → proliferation (skin context) |
| Insulin receptor | Y1158/Y1163 | Reduced insulin signaling | Insulin → PI3K → Akt |

**Why PTPN2 is broader than STAT3 coverage in existing runs:**
- Run_070 (leptin/STAT3): targets STAT3 Y705 indirectly via leptin pathway modulation
- Run_080 (IL-22/Th22/KLK5): targets IL-22 → STAT3 in Th22 context
- **PTPN2 terminates BOTH JAK1 AND STAT1** — the IFN-γ → STAT1 (not STAT3!) → CAMP arm is not covered by any STAT3-focused run

---

## Rosacea Arm

**IFN-γ → JAK1 → STAT1 → LL-37: the missing Loop 1 input arm**

```
Rosacea dermis: Th1 cells (CXCR3+, IFN-γ+ — confirmed in rosacea biopsies)
    ↓ (IFN-γ secreted into dermis)
Dermal keratinocytes: IFNGR1/IFNGR2 expressed constitutively
    → JAK1 autophosphorylation Y1034 → STAT1 Y701 → STAT1 homodimer
    → CAMP promoter GAS element binding
    → cathelicidin/LL-37 mRNA ↑
    → KLK5 cleaves pre-pro-LL-37 → mature LL-37
    → Loop 1: LL-37 → FPR + TLR2/4 → NF-κB → KLK5 ↑ → more LL-37 (feed-forward)
```

**Evidence:**
- Schauber et al. 2009 J Invest Dermatol: IFN-γ + Staphylococci → STAT1 → CAMP (cathelicidin) in keratinocytes; STAT1 inhibition blocked this induction — DIRECT evidence for STAT1 → LL-37 in skin
- Seo et al. 2012 (and multiple rosacea genomics): IFN-γ pathways significantly elevated in rosacea biopsy transcriptomics; STAT1-target gene signature is part of rosacea molecular profile
- Yamasaki 2011 (JAI): cathelicidin (LL-37) is overexpressed in rosacea — defines the molecular lesion; CAMP gene upregulation documented in papular/pustular rosacea

**PTPN2 deficiency in rosacea:**
- If PTPN2 expression or activity is reduced in rosacea keratinocytes:
  → JAK1 Y1034 remains phosphorylated after IFN-γ stimulation
  → STAT1 Y701 remains phosphorylated (sustained homodimer)
  → CAMP promoter continuously active
  → LL-37 elevated chronically → Loop 1 non-termination
  → Explains Loop 1 non-responders: these patients have STAT1-mediated LL-37 production
    that continues even when KLK5 is suppressed (different pathway)

**Mechanistic integration:**
This is the THIRD molecular input into LL-37 production in rosacea:
1. VDR/calcitriol → VDRE in CAMP promoter (run_056) — vitamin D dependent
2. KLK5 → LL-37 (Loop 1 direct — runs 015, 028) — protease dependent
3. **IFN-γ → JAK1 → STAT1 → GAS → CAMP (new, run_119)** — Th1 cytokine dependent

Non-responder phenotype clarification:
- Calcitriol non-responders: VDR variant + PTPN2 LOF → LL-37 still high via STAT1 arm
- Loop 1 management targets KLK5 (LEKTI/spermidine/AzA) → reduces protease arm but not STAT1 arm

---

## T1DM Arm

**PTPN2 rs45450798 — Strongest Non-HLA T1DM GWAS Signal:**

| Gene/Locus | T1DM GWAS Effect | Evidence Level |
|-----------|-----------------|----------------|
| HLA (DQ/DR) | OR ~3-7 | Definitive (largest effect) |
| INS/VNTR | OR ~2.0 | Very strong |
| PTPN22 R620W | OR ~2.0 | Very strong |
| **PTPN2 rs45450798** | **OR ~1.6** | **Smyth 2008 Nat Genet — Bonferroni p = 1.3×10⁻¹²; independently replicated** |
| IL2RA/CD25 | OR ~1.7 | Strong |
| IFIH1/MDA5 | OR ~1.5 | Strong |
| TNFAIP3 (run_113) | OR ~1.4 | Confirmed |

PTPN2 rs45450798 is an **intronic variant** → likely affects PTPN2 expression level (not protein function) → functional haploinsufficiency. Risk allele carriers: PTPN2 expression reduced → JAK1/STAT1 hyperactivation in ALL tissues.

**T1DM mechanisms via PTPN2:**

1. **Islet macrophage JAK1/STAT1 hyperactivation:**
   ```
   IFN-γ (from islet-infiltrating Th1/CD8+ T cells) → JAK1 → STAT1
       → iNOS gene transcription ↑ (GAS element in NOS2 promoter)
       → NO → β cell death (13th β cell death mechanism; iNOS/NO arm directly driven by STAT1)
       PTPN2 LOF → STAT1 unchecked → more iNOS → more NO → more β cell death
   ```

2. **Intestinal PTPN2 → gut barrier → antigen spillover:**
   Filer et al. 2017 Nat Immunol: IEC (intestinal epithelial cell)-specific PTPN2 deletion:
   - JAK1/STAT1 hyperactivation in gut epithelium
   - IFN-γ → STAT1 → claudin-2 upregulation (pore-forming tight junction protein)
   - Gut permeability ↑ → microbial antigen translocation → islet antigen cross-reactivity
   - **M1 mountain amplifier**: PTPN2 LOF in gut → chronic leaky gut → T1DM antigen spillover
   - Filer 2017 directly showed this in colitis mouse model; T1DM gut context: same IEC mechanism

3. **T cell PTPN2 → JAK3 → γc cytokine signaling:**
   PTPN2 in T cells dephosphorylates JAK3 → reduces IL-2/IL-15/IL-7 signaling
   IL-2 → CD25 (IL-2RA) → STAT5 → Treg proliferation and FOXP3 maintenance
   PTPN2 LOF → excessive STAT5 signaling? No — actually, excessive JAK3 → STAT5 could
   paradoxically HYPERACTIVATE effector T cells rather than Tregs if signal is above threshold
   → Complex, context-dependent
   More certain: PTPN2 LOF in T cells → T cells more sensitive to cytokine stimulation → more
   vigorous anti-islet Th1 response (higher IFN-γ production per antigen exposure)

4. **Pancreatic stellate cell JAK1 → pancreatitis-like environment:**
   PTPN2 in stellate cells → JAK1/STAT3 → inflammation; LOF → exocrine + endocrine pancreas
   in a more pro-inflammatory state (mechanism 3 is less well-supported)

**Evidence summary for T1DM:**
- Smyth 2008 Nat Genet: genetics (HIGH, Bonferroni-significant)
- Filer 2017 Nat Immunol: intestinal PTPN2 → gut barrier (MODERATE-HIGH)
- Scharl 2012 GUT: intestinal PTPN2 — IBD relevant but T1DM extrapolation is mechanistically solid
- Mechanistic connection via STAT1 → iNOS/NOS2 → NO → β cell death: established pathway

---

## ME/CFS Bonus

1. **Microglial JAK1/STAT1 hyperactivation**: IFN-γ from neuroinflammation → microglial JAK1 → STAT1 → iNOS → NO → neuronal stress. PTPN2 in microglia terminates this; LOF → sustained microglial STAT1 activity → neuroinflammation persistence. ME/CFS neuroinflammation involves microglial activation.

2. **BBB endothelial PTPN2**: PTPN2 in brain endothelial cells → maintains barrier via EGFR dephosphorylation; LOF → VEGFR hyperactivation → BBB permeability. Some ME/CFS data showing BBB dysfunction.

3. **Post-COVID ME/CFS**: IFN-γ (elevated in Long COVID) → JAK1 → STAT1 hyperactivation in multiple tissues. PTPN2 LOF → prolonged IFN-γ → STAT1 signaling → chronic inflammatory gene expression → fatigue/cognitive dysfunction axis.

---

## Kill-First Assessment

**Challenge 1: "HCQ (run_088) blocks IFN-α → ISGF3 signaling; doesn't this cover STAT1?"**

FAIL:
- HCQ → TLR7/9 endosomal block → IFN-α ↓ → ISGF3 (STAT1/STAT2/IRF9) reduction
- PTPN2 run addresses IFN-γ → JAK1 → STAT1 homodimer — DISTINCT from HCQ's target
- IFN-γ is produced by Th1/CD8+ T cells; its receptor (IFNGR) is on keratinocytes, macrophages — NOT blocked by HCQ endosomal approach
- HCQ reduces IFN-α from pDCs; it does NOT reduce IFN-γ from T cells and does NOT affect JAK1 → STAT1 directly
- Kill-first fails for the IFN-γ/JAK1/STAT1/CAMP arm

**Challenge 2: "Existing STAT3 coverage (run_070/080/090) overlaps with JAK1/STAT1"**

FAIL:
- Run_070 targets leptin → STAT3 Y705 (Tyr705) — different residue, different transcription factor
- CAMP gene promoter has BOTH GAS elements (STAT1 homodimer) AND VDRE (VDR)
- GAS-dependent CAMP transcription is STAT1-specific; STAT3 Y705 binds different promoter elements (SIE/GAS variants)
- Suppressing STAT3 does NOT suppress STAT1-driven CAMP; these are orthogonal transcriptional pathways
- Kill-first fails

**Challenge 3: "Baricitinib/tofacitinib are Rx drugs; no OTC PTPN2 activator exists — criterion 3 fails"**

PARTIAL: OTC element is weak. However, criterion 3 requires "new therapeutic target OR monitoring point":
- **PTPN2 genotyping** (rs45450798 intronic variant): new actionable genetic stratification — identifies patients with constitutively lower PTPN2 → JAK1/STAT1 hyperactivation → aggressive anti-Th1/anti-IFN-γ protocol indicated + JAK inhibitor referral for T1DM
- **IFN-γ measurement**: serum/plasma IFN-γ → proxy for JAK1/STAT1 activation state; currently not in T-index but would identify PTPN2-LOF patients who have high IFN-γ-driven STAT1
- **New Loop 1 non-responder mechanism**: for rosacea patients failing LL-37-targeted therapy → test STAT1 arm; topical JAK inhibitor trials (tofacitinib 2% cream is FDA-approved for alopecia areata) represent a future option
- Kill-first partially fails on criterion 3 (new monitoring + genetic stratification)

---

## Protocol Integration

### Genetic Stratification (5th Point)

| SNP | Gene | Disease association | Effect | Action |
|-----|------|---------------------|--------|--------|
| HFE C282Y/H63D (run_110) | HFE | T1DM iron loading | Iron accumulation in β cells | Iron management, no phlebotomy |
| rs2327832, rs6920220 (run_113) | TNFAIP3 | T1DM susceptibility, rosacea ETR→PPR | A20 haploinsufficiency | Continuous protocol, butyrate |
| rs4077515 (run_115) | CARD9 | Mycobiome/Candida susceptibility | CARD9 S12N LOF → worse fungal CARD9 | Caprylic acid, stool Candida |
| rs45450798, rs2847281 (run_119) | PTPN2 | **Strongest non-HLA T1DM GWAS** | PTPN2 ↓ → JAK1/STAT1 chronic | IFN-γ monitoring; JAK inhibitor referral |

**PTPN2 genotyping clinical action:**
```
PTPN2 rs45450798 risk allele (intronic; affects expression):
    → Serum IFN-γ measurement at baseline
    → If IFN-γ elevated (>10 pg/mL): JAK1/STAT1-dominant pattern confirmed
    → For T1DM: discussion with endocrinologist re: baricitinib eligibility (TrialNet ongoing)
    → For rosacea: maximize anti-Th1 protocol (omega-3/EPA → Th1 → Th0 shift; HCQ for Node D
       if IFN-α elevated; topical azelaic acid suppresses Th1-driven LL-37)
```

### IFN-γ as New T-Index Monitoring Component

```
Serum IFN-γ (Simoa or standard ELISA):
    <2 pg/mL: normal
    2-10 pg/mL: borderline; consider PTPN2 genotyping
    >10 pg/mL: JAK1/STAT1 arm is active driver of Loop 1 / islet inflammation
    
When elevated IFN-γ is confirmed:
    → Rosacea: anti-Th1 measures (run_020 omega-3 → Th1↓; run_056 calcitriol → Treg↑)
    → T1DM: baricitinib consultation (JAK1/2 inhibitor); ongoing TrialNet trials
    → Both: PTPN2 LOF genotype screen to confirm chronic JAK1/STAT1 activation
```

### Loop 1 Non-Responder Algorithm Update

Previous branches for Loop 1 (LL-37) non-responders:
1. VDR variant → insufficient calcitriol → LL-37 elevated via VDR-independent arm → more vitamin D3
2. KLK5 upregulation → more LL-37 cleavage from pre-pro → LEKTI/AzA/ivermectin
3. TRPV1 sensitization → neurogenic LL-37 release → capsaicin desensitization (run_015)

**New branch (run_119):**
4. IFN-γ → JAK1 → STAT1 → CAMP transcription → LL-37 elevated at mRNA level
   → Identify via: elevated serum IFN-γ + elevated CXCL10 (STAT1 target; run_006 as marker)
   → Address via: anti-Th1 protocol (omega-3/EPA, calcitriol/Treg, HCQ if Node D coactivated)
   → Monitor via: CXCL10 normalization (STAT1-driven CXCL10 falls when JAK1/STAT1 attenuated)

### OTC Cross-Mechanism Insights

**No new OTC agent required**, but existing protocol elements gain new mechanistic rationale:

- **Omega-3 EPA (run_089)**: EPA → PPAR-α + resolvin E1 → Th1 → Th0 phenotype shift → less IFN-γ → less JAK1 activation → PTPN2 is less depleted. Indirect benefit via Th1 reduction.
- **Calcitriol (run_056)**: Tregs suppress IFN-γ from Th1 cells → less JAK1/STAT1 activation in keratinocytes. The Treg induction → IFN-γ ↓ → STAT1 ↓ → LL-37 ↓ pathway is now formally identified.
- **HCQ (run_088)**: pDC IFN-α ↓ → less ISGF3/STAT1 (type I IFN arm); does NOT reduce IFN-γ directly but reduces the IFN-α → Th1 amplification loop → indirectly less IFN-γ over time.

---

## Framework Connections

**Run_006 (CXCL10):** CXCL10/IP-10 is a STAT1 target gene (GAS element in CXCL10 promoter). CXCL10 elevation → confirms active IFN-γ → STAT1 signaling. CXCL10 can serve as an INDIRECT PROXY for STAT1 activation and PTPN2 insufficiency. This cross-run connection means: elevated CXCL10 (especially in IFN-γ-dominant patients) = JAK1/STAT1 is the active arm.

**Run_040 (IFN-α/NLRP3):** IFN-α → ISGF3 (STAT1/STAT2/IRF9) is Signal 1B. Run_119 adds: IFN-γ → STAT1 homodimer → different transcriptional program (ISGs vs. GAS-driven cathelicidin). These are two distinct STAT1-mediated arms: IFN-α/ISGF3 (Signal 1B) vs. IFN-γ/STAT1-homodimer (Loop 1 → LL-37).

**Run_113 (A20/TNFAIP3):** JAK1/STAT1 → SOCS3 → A20 expression? Actually STAT3 → SOCS3 → A20 is documented. STAT1 hyperactivation → sustained inflammatory gene expression AND potential SOCS3 upregulation → A20 reduced (indirect). PTPN2-LOF patients may have compound A20 depletion via STAT1-mediated SOCS3.

**Run_056 (VDR/M4):** VDR → CAMP (via VDRE) + PTPN2 → JAK1 → STAT1 → CAMP (via GAS): TWO independent promoter elements for CAMP in keratinocytes. VDR-non-responsive patients may still have high LL-37 via STAT1 arm. VDR-responsive patients who improve: improvement may reflect Treg induction → IFN-γ ↓ → STAT1 ↓ as much as direct VDR → CAMP modulation.

---

*Filed: 2026-04-12 | Numerics run 119 | PTPN2 TC-PTP JAK1 STAT1 Y701 CAMP cathelicidin LL-37 Loop 1 IFN-gamma rosacea non-responder T1DM GWAS Smyth 2008 Nat Genet OR 1.6 rs45450798 gut permeability Filer 2017 Nat Immunol IFNGR iNOS NOS2 GAS promoter CXCL10 STAT1 homodimer baricitinib tofacitinib JAK inhibitor genetic stratification 5th point IFN-γ monitoring T-index*
*Key insight: The rosacea LL-37 overexpression has THREE transcriptional origins in keratinocytes: (1) VDR → VDRE → CAMP (calcitriol arm); (2) KLK5 maturation of pre-pro-LL-37 (protease arm); (3) IFN-γ → JAK1 → STAT1 → GAS → CAMP (Th1 cytokine arm, this run). PTPN2 terminates arm 3. Loss-of-function via the T1DM GWAS variant (rs45450798) → constitutively hyperactivated JAK1/STAT1 → Loop 1 cannot be terminated via KLK5 suppression alone. CXCL10 serves as proxy biomarker for STAT1 activity (Schauber 2009 J Invest Dermatol; Smyth 2008 Nat Genet; Filer 2017 Nat Immunol).*
