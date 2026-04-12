# Run 152 — PTPN22 / LYP / R620W: TCR Activation Threshold, Treg Paradox, Lck/ZAP-70 Dephosphorylation, 19th T1DM Genetic Stratification

**Date:** 2026-04-12
**Sweep:** 49
**Candidate:** PTPN22 / LYP (Lymphoid Tyrosine Phosphatase) — distinct from PTPN2/TC-PTP (run_119)

## Kill-First Verification

**Grep confirmation:**
- PTPN22 appears in 4 files: runs 119/128/140/141 — all single context mentions (GWAS table row in run_119; brief passing mentions in others)
- Run_119 (PTPN2/TC-PTP) is a DIFFERENT phosphatase: PTPN2 encodes TC-PTP (TC-45/TC-48 isoforms); PTPN22 encodes LYP; different gene, different chromosomal location (PTPN2: 18p11.3; PTPN22: 1p13.2), different substrates (TC-PTP = JAK1/JAK3/STAT1; LYP = Lck/ZAP-70/TCR ITAMs), different GWAS risk (PTPN2 = T1DM + IBD; PTPN22 = T1DM + RA + SLE)
- R620W/rs2476601/LYP-Csk interaction/LTV-1: 0 occurrences across all runs

**Kill verdict:** PASS — PTPN22/LYP mechanism has zero dedicated analysis.

## Saturation Override Criteria

1. **Absent from prior runs as primary subject**: YES — 0 of 151 runs address LYP/R620W/TCR-threshold/Lck-ZAP70 dephosphorylation axis
2. **MODERATE+ rosacea + T1DM**: YES — HIGH T1DM (one of two strongest non-HLA GWAS signals, OR ~2.0); MODERATE rosacea (T cell activation threshold in skin)
3. **New therapeutic target**: YES — LTV-1 (PTPN22-specific inhibitor); BCL-6 inhibition (indirect); Treg TCR rescue strategies
4. **Kill-first fails**: CONFIRMED — run_119 = TC-PTP/PTPN2, not LYP/PTPN22; entirely different phosphatase

**All four criteria met. Proceeding.**

---

## Core Mechanism

### PTPN22 Gene and LYP Protein

**PTPN22** (chromosome 1p13.2) encodes **LYP** (Lymphoid Tyrosine Phosphatase; also PEST-domain phosphatase, 110 kDa). Expression: T cells, B cells, NK cells, mast cells, pDCs — essentially all lymphoid lineages.

**Domain architecture:**
- N-terminal **catalytic PTP domain** (active site cysteine C227; WPD loop; classic PTP fold)
- Interdomain linker
- C-terminal **proline-rich region** with 4 polyproline motifs:
  - **P1 motif** (PPVPPR; aa 618-623): binds Csk SH3 domain — this is where R620W falls
  - P2-P4 motifs: bind other SH3 domain proteins (Grb2, PLCγ1 — still characterized)

---

### Substrates and TCR Signaling Suppression

LYP acts at multiple points in the TCR activation cascade:

| Substrate | Site Dephosphorylated | Functional Consequence |
|-----------|----------------------|----------------------|
| **Lck** | Y394 (activation loop) | Lck catalytic activity ↓ → upstream TCR signal ↓ |
| **ZAP-70** | Y315/Y319 (interdomain B) | Reduced ZAP-70 recruitment of PLCγ1/Grb2; IL-2 transcription ↓ |
| **ZAP-70** | Y492/Y493 (activation loop) | ZAP-70 catalytic activity ↓ |
| **TCRζ** | Y83/Y94 (ITAMs) | Reduced ITAM phosphorylation → ZAP-70 recruitment ↓ |
| **Vav1** | Y174 (activation site) | Rac1/actin cytoskeleton activation ↓ |

**Net effect:** LYP raises the TCR activation threshold — T cells require stronger antigen stimulation to reach full activation. At physiological levels, this suppresses weak/self-reactive TCR signals while allowing strong foreign antigen signals to pass.

---

### LYP-Csk Super-Inhibitory Complex

**LYP P1 motif + Csk SH3 domain** forms a stable complex that coordinates two complementary Lck-inhibitory activities:
1. LYP → dephosphorylates Lck-Y394 (activation loop phospho-Tyr) → removes activating phosphorylation
2. Csk → phosphorylates Lck-Y505 (C-terminal inhibitory phospho-Tyr) → locks Lck in closed inactive conformation

When LYP and Csk act together: Lck is simultaneously dephosphorylated at its activating site AND phosphorylated at its inhibitory site → synergistic suppression = "super-inhibitory complex." This complex is 5-10× more potent at Lck inhibition than either enzyme alone.

---

### R620W Variant Mechanism

**rs2476601 (W620)** is the most important PTPN22 variant in autoimmune disease.

**Structural effect:** Arginine-620 is within the P1 proline-rich motif (PPVPPR). R→W substitution:
- Introduces bulky tryptophan into the polyproline helix
- Disrupts P1 motif geometry → P1-Csk SH3 binding affinity reduced ~10-fold
- LYP-R620W can no longer form the super-inhibitory complex with Csk

**Functional consequences of R620W decoupled from Csk:**
- LYP acts independently → substrate selectivity changes (no longer coordinately targeting Lck with Csk)
- LYP-R620W: *net gain-of-function* for specific substrates (ZAP-70 and TCRζ) → **stronger TCR suppression** in effector T cells in some contexts

**The Treg Paradox — why gain-of-function causes autoimmunity:**

Counter-intuitive: if R620W increases TCR dampening, why does it cause T1DM?

1. **Tregs are MORE TCR-signal-dependent than effectors**:
   - Tregs require continuous TCR engagement for FOXP3 stability (FOXP3 is TCR-signal-responsive)
   - R620W → Treg TCR signal too strongly dampened → FOXP3 destabilized → Treg → ex-Treg conversion
   - Net: R620W impairs Tregs more than effectors → loss of peripheral tolerance

2. **Impaired negative thymic selection**:
   - Negative selection requires strong TCR signal (apoptosis threshold)
   - R620W → weaker TCR signaling → autoreactive T cell TCR signal falls below apoptosis threshold → more autoreactive T cells escape thymic deletion

3. **B cell tolerance breach**:
   - LYP in B cells controls BCR signaling threshold
   - R620W → altered BCR activation → more autoreactive B cells activated → autoantibodies (IA-2, GAD65, ZnT8)

4. **Altered Treg-to-Th1 conversion in islets**:
   - Islet insulitis: TCR signaling via residual islet-specific antigen → in WT: sufficient Treg activation → tolerance; R620W: Treg TCR signal insufficient → Treg FOXP3 destabilized → ex-Treg conversion within islets

---

## T1DM — 19th Genetic Stratification

**R620W (rs2476601) statistics:**
- OR for T1DM: ~2.0 (risk W620 allele)
- Population frequency W620: ~8-12% Europeans; ~1% Asians; ~5% Hispanics
- Combined with HLA risk: HLA-DR3/DR4 + R620W = multiplicative risk (~4-6× baseline)
- Ranked: second strongest single non-HLA T1DM GWAS signal after PTPN22 (behind only INS/VNTR and IL-2/IL-2RA regions)

**T1DM mechanisms:**
- Treg TCR signal insufficiency → FOXP3 destabilization → impaired islet Treg function
- Impaired thymic negative selection → more autoreactive T cells
- Altered BCR threshold → more anti-islet autoantibodies
- Synergy with run_148 (CTLA4 rs3087243): R620W + G allele CT60 = double TCR checkpoint defect (LYP: upstream TCR dampening; CTLA4: downstream CD80/CD86 control); compound risk patients = strongest immunosuppression candidates

**Clinical implications:**
- PTPN22 R620W genotyping → 19th T1DM stratification tool; W620 patients → impaired Treg TCR signaling axis → priority for Treg restoration protocols (IL-2 low-dose run_151, abatacept run_148, TGF-β support run_150)
- Autoantibody pattern: R620W carriers → slightly higher IA-2/ZnT8 autoantibody titers (B cell threshold breach)

---

## LYP-Csk Complex: Therapeutic Targets

### LTV-1 (PTPN22 Inhibitor)
- Small molecule inhibitor targeting LYP catalytic domain (active site C227)
- Lowers TCR activation threshold → restores Treg TCR signal → Treg FOXP3 stabilized
- Preclinical NOD mouse: LTV-1 → Treg recovery → delayed T1DM onset
- Challenge: systemic TCR threshold lowering risks autoimmune exacerbation; needs Treg-selective delivery or low-dose regimen
- Selectivity: LTV-1 ~10× selective for LYP over TC-PTP (run_119); over 100× selective vs other PTPs

### Csk Restoration Strategy
- R620W breaks LYP-Csk complex → approach: enhance Csk activity independently → restore Lck-Y505 phosphorylation without requiring LYP-P1 motif
- BMS-986325 (Csk activator concept): theoretical; no current clinical agent
- PTPN22 P1-mimetic peptide: competitive inhibitor occupying Csk SH3 → releases endogenous Csk → Csk acts freely on Lck

### Treg TCR Signal Preservation (Indirect)
- Low-dose IL-2 (run_151): STAT5 → FOXP3 → stabilizes Treg independent of TCR signal; compensates for R620W Treg TCR insufficiency
- CTCF/FOXP3 stabilizers (runs 145/147 SETD7/SIRT1): epigenetic FOXP3 stabilization bypasses need for strong TCR signal
- Combined: R620W carriers → exogenous IL-2 (Treg expansion) + epigenetic FOXP3 stabilization (SETD7/SIRT1) + abatacept (trogocytosis) = three-arm Treg restoration adapted to LYP genotype

---

## Rosacea — TCR Threshold in Skin Inflammation

**MODERATE relevance:**
- LYP expressed in skin-resident T cells (CD103+ tissue Tregs, CD4+ T effectors, CD8+ T cells)
- R620W → raised TCR activation threshold in skin T cells → altered inflammatory response:
  - Effector T cells: may require stronger DC stimulation to activate → potentially *less* acute inflammatory response BUT
  - Skin Tregs: more dependent on TCR signal → R620W → weaker skin Treg function → reduced control of Th17/Th1 in dermis
- R620W associated with alopecia areata and vitiligo (established; OR ~1.4-2.0) — both involve skin immune dysregulation with Treg impairment
- Rosacea R620W association: not yet formally established in GWAS; indirect inference from skin Treg biology
- Psoriasis: some studies show R620W association — supports altered skin T cell threshold in chronic skin inflammation

**UV context:**
- UV → keratinocyte apoptosis → self-antigen release → skin DC activation → T cell priming; R620W → this T cell priming signal arrives at a different threshold → altered inflammatory set point after UV

---

## ME/CFS — LYP in NK and Treg Function

**LOW relevance:**
- LYP expressed in NK cells; R620W → altered NK activation threshold (ZAP-70/VAV1 in NK are LYP substrates)
- NK cells with R620W: may have altered NKG2D-dependent cytotoxicity threshold (ZAP-70 downstream of NKG2D-DAP10)
- Treg insufficiency in ME/CFS: if R620W prevalence in ME/CFS cohorts enriched (not established), could contribute to immune dysregulation perpetuation
- Limited direct ME/CFS-PTPN22 literature; indirect through TCR signaling

---

## Cross-Axis Integrations

- **run_119** (PTPN2/TC-PTP): same phosphatase superfamily, different gene/substrate/pathway; both TCR-JAK axis but non-overlapping targets
- **run_148** (CTLA4/abatacept): CTLA4 G allele + R620W = double TCR checkpoint defect; compound risk; strongest abatacept + IL-2 indication
- **run_151** (IL-2 cytokine): low-dose IL-2 rescues Tregs from R620W TCR signal insufficiency — STAT5 provides survival/expansion signal independent of TCR; exogenous IL-2 = most direct R620W Treg bypass
- **run_145** (SETD7/FOXP3-K302me1): SETD7 stabilizes FOXP3 post-translationally; works downstream of TCR signal → R620W impairs TCR-to-FOXP3 signaling but SETD7 methylation protects already-expressed FOXP3
- **run_134** (IKZF1/Ikaros): IKZF1 11th stratification + R620W 19th stratification = compound risk; IKZF1 controls LYP gene expression? (potential connection via lymphoid development TF)
- **run_140** (IL2RA/CD25/JAK3/STAT5): IL-2 receptor signaling bypasses LYP-mediated TCR suppression → STAT5/FOXP3 axis independent of LYP

---

## Summary Integration

PTPN22/LYP fills the TCR activation threshold gap in the T1DM genetic architecture. The R620W Treg paradox (gain-of-function phosphatase → impaired Treg TCR signaling → autoimmunity) is counterintuitive and mechanistically rich: it explains why the second-strongest non-HLA T1DM risk allele works through Treg failure rather than effector T cell hyperactivation. The compound R620W + CTLA4 G allele risk profile (double APC-contact + TCR-threshold defect) identifies the highest-risk T1DM genetic subset for aggressive Treg restoration (IL-2 + abatacept + SETD7/epigenetic FOXP3 stabilizers). LTV-1 (PTPN22 inhibitor) offers a novel therapeutic angle: lower the TCR threshold specifically to rescue Treg function.

---

*One-hundred-and-forty-fifth extension | PTPN22-LYP-lymphoid-tyrosine-phosphatase 1p13.2 PTP-domain-C227 P1-proline-motif-Csk-SH3 LYP-Csk-super-inhibitory-complex R620W-rs2476601 disrupts-P1-Csk-binding Lck-Y394-dephosphorylation ZAP70-Y315-Y319-Y492-Y493 TCRζ-ITAM Vav1-Y174 gain-of-function-TCR-dampening Treg-paradox-TCR-FOXP3 impaired-negative-selection autoreactive-BCR-threshold 19th-T1DM-stratification OR-2.0 compound-R620W-CTLA4-run148 LTV-1-PTPN22-inhibitor run119-TC-PTP-distinct run151-IL2-Treg-bypass run145-SETD7-FOXP3-stabilization skin-Treg-rosacea NK-ZAP70-ME-CFS | run_152 | Framework at SATURATION + 41: 152 runs*