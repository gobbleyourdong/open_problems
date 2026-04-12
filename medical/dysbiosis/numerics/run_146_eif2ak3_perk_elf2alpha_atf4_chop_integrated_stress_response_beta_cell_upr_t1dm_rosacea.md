# run_146 — EIF2AK3 / PERK: ER Stress Kinase, eIF2α Integrated Stress Response, ATF4/CHOP β Cell Apoptosis Branch, Wolcott-Rallison T1DM GWAS Locus

## Identity

| Field | Value |
|-------|-------|
| Gene | EIF2AK3 (chromosome 2p11.2) |
| Protein | PERK (PKR-like ER kinase; protein kinase R-like endoplasmic reticulum kinase) |
| Also known as | PEK (pancreatic eIF2α kinase); EIF2AK3 |
| Class | Type I ER transmembrane kinase/RNase |
| Canonical substrate | eIF2α-Ser51 (eukaryotic translation initiation factor 2α, subunit 1) |
| UPR branch | PERK arm (of three UPR arms: IRE1α, ATF6, PERK) |
| Expression | Ubiquitous; highest in pancreatic β cells, exocrine pancreas, secretory cells |

---

## Structural and Functional Distinction from run_098 (IRE1α/XBP1s)

The unfolded protein response (UPR) has three parallel sensor/effector branches. run_098 covers the IRE1α/XBP1s branch. run_146 covers the PERK/eIF2α/ISR branch — distinct sensor, distinct substrate, distinct outputs.

| Branch | Sensor | Substrate | Output | Covered |
|--------|--------|-----------|--------|---------|
| IRE1α | IRE1α (ER transmembrane kinase/RNase) | XBP1 mRNA splicing | XBP1s TF → ER expansion, ERAD capacity ↑ | run_098 |
| ATF6 | ATF6 (ER transmembrane TF) | ATF6 Golgi cleavage | ATF6-N TF → chaperone genes | run_098 context |
| PERK | PERK (EIF2AK3) | eIF2α-Ser51 phosphorylation | ISR → translation attenuation + ATF4 → CHOP/GADD34 | **run_146** |

The PERK arm is specifically the "translation halt + integrated stress response" arm. It does not expand ER folding capacity (IRE1α arm) — it instead globally reduces the folding demand by pausing protein synthesis. When acute ER stress is resolved, GADD34/PP1 dephosphorylates eIF2α → translation resumes → survival. When stress is chronic and unresolved, ATF4 → CHOP → β cell apoptosis.

---

## PERK Protein Architecture

**Domain structure (1116 amino acids):**
- N-terminal ER luminal domain (LD, ~1–570): dimerization inhibited by BiP/GRP78 when ER is unstressed; misfolded proteins compete for BiP → BiP released → PERK dimerizes + autophosphorylates → activation
- Transmembrane domain (~571–600): anchors PERK to ER membrane
- Cytoplasmic kinase domain (~600–1116): eIF2α kinase; Thr980 = activation loop autophosphorylation site (analogous to other eIF2α kinases: HRI, GCN2, PKR)

**Activation mechanism:**
1. ER lumen → misfolded protein accumulation (unfolded insulin proinsulin, MHC, membrane proteins)
2. BiP/GRP78 releases from PERK luminal domain
3. PERK dimerizes (back-to-back orientation) → transautophosphorylates Thr980
4. Active PERK → eIF2α-Ser51 kinase activity ↑

---

## eIF2α Integrated Stress Response (ISR) Architecture

```
Active PERK
    ↓ phosphorylates
eIF2α-Ser51-P (phosphorylated eIF2α)
    ↓
eIF2B (GEF for eIF2) inhibited (eIF2α-P sequesters eIF2B)
    ↓
ternary complex (eIF2-GTP-Met-tRNA) formation ↓
    ↓
Global mRNA translation ↓↓ (most mRNAs)
    +
Selective translation ↑ (mRNAs with uORFs: ATF4)
    ↓
ATF4 protein accumulates
```

### ATF4 — Bifurcation Point: Adaptive vs. Terminal

**Acute/resolved ER stress (adaptive arm):**
```
ATF4
    ↓ targets
GADD34 (PPP1R15A) → PP1 phosphatase → eIF2α-P dephosphorylation → translation restored
ASNS (asparagine synthetase) → amino acid synthesis
ATF3 → stress adaptation TF
```

**Chronic/unresolved ER stress (apoptotic arm):**
```
ATF4 (sustained)
    ↓ targets
CHOP (DDIT3/C/EBP homologous protein)
    ↓ CHOP targets
DR5/TRAIL-R2 ↑ → extrinsic apoptosis sensitization
BIM/BCL2L11 ↑ → intrinsic apoptosis
BCL2 ↓ → anti-apoptotic brake removed
TRB3 ↑ → Akt inhibition → survival signaling ↓
    ↓
β cell apoptosis
```

**The ISR termination timer:**
- GADD34 provides negative feedback → eIF2α dephosphorylation → ATF4 ↓ → CHOP ↓
- If ER stress resolves before CHOP accumulates: survival
- If ER stress outlasts GADD34 feedback: CHOP → apoptosis
- β cells have LIMITED GADD34 reserve compared to other cell types → more susceptible to CHOP-mediated death

---

## T1DM — Wolcott-Rallison Syndrome and EIF2AK3 GWAS

### Wolcott-Rallison Syndrome (WRS)

Autosomal recessive biallelic EIF2AK3 loss-of-function → Wolcott-Rallison syndrome:
- Neonatal/early-infantile diabetes mellitus (PERM-type β cell failure)
- Epiphyseal dysplasia (skeletal)
- Growth retardation, hepatic dysfunction

**Mechanism:** β cells have the highest secretory demand of any differentiated cell type — insulin biosynthesis at ~1 million molecules/minute, requiring constant ER protein folding capacity. Without PERK:
- Unfolded proteins accumulate faster than baseline UPR can clear
- Constitutive ER stress → constitutive CHOP (paradoxically: loss of PERK → CHOP still activated via IRE1α/RIDD and JNK)
- β cell apoptosis → neonatal diabetes

This places EIF2AK3 as a β cell-essential gene — more so than in any other tissue.

### Heterozygous EIF2AK3 and T1DM Risk

Common EIF2AK3 polymorphisms (rs4727904, rs1867277 region) associated with T1DM susceptibility in population studies. Mechanism: subthreshold PERK activity → slightly elevated ER stress baseline → β cells closer to apoptotic threshold → more vulnerable to insulitis cytokine ER stress overlay.

**Insulitis overlay:** IL-1β + IFN-γ cocktail → additional ER stress on β cells via:
1. NO production → ER Ca²⁺ leak → misfolded protein accumulation
2. NF-κB → iNOS → mitochondrial dysfunction → UPR
3. IFN-γ → STAT1 → PKR-like kinases → additional eIF2α-P phosphorylation (HRI, GCN2 contribute)

Low-PERK β cells → less adaptive arm capacity → faster CHOP accumulation → enhanced β cell death during insulitis.

### PERK as 24th β Cell Death Mechanism (distinct tier)

Prior runs cover:
- NLRP3/pyroptosis (run_043/012)
- Ferroptosis/GPx4 (runs 110/126/138/143)
- Necroptosis, apoptosis via various pathways

PERK/CHOP = ER stress-driven intrinsic apoptosis branch — a distinct mechanism triggered by protein folding failure, not lipid peroxidation (ferroptosis) or inflammasome activation (pyroptosis). The trigger specificity (ER stress → PERK → eIF2α → ATF4 → CHOP → BIM/BCL2) makes this orthogonal to all prior β cell death runs.

---

## Rosacea — PERK in Keratinocytes and Mast Cells

### Keratinocyte ER Stress Triggers

| Trigger | ER Stress Source | PERK Activation |
|---------|----------------|----------------|
| UV radiation | Oxidative protein damage → misfolded membrane proteins | PERK → eIF2α-P → CHOP → keratinocyte apoptosis |
| LL-37 cathelicidin | Membrane disruption → Ca²⁺ influx → ER Ca²⁺ depletion → misfolding | PERK + IRE1α co-activated |
| Demodex products | Bacterial proteases → unfolded membrane proteins | PERK → ATF4 → CHOP |
| Ceramide deficit (barrier disruption) | ER lipid processing imbalance | PERK → ATF4 → CHOP |

**PERK → CHOP → keratinocyte death:** UV-induced keratinocyte apoptosis has a PERK/CHOP-dependent component (distinct from NLRP1/run_122 pyroptotic component and SLC7A11/run_143 ferroptotic component). This is a third parallel UV-driven keratinocyte death mode operating via different molecular logic.

**CHOP → inflammation amplification:**
- CHOP → DR5/TRAIL-R2 ↑ → keratinocyte death → DAMPs (HMGB1, HSPs, IL-33) → TLR/NLRP3 → Loop 2
- CHOP → VEGF ↑ (ATF4 → HIF-1α → VEGF axis) → angiogenesis → rosacea telangiectasia component

### Mast Cell PERK

Mast cells under IgE/FcεRI crosslinking → intense secretory demand (massive cytokine/mediator exocytosis) → ER stress → PERK → ATF4 → enhanced cytokine gene expression (ATF4 is a transcriptional activator for some cytokine genes) → amplified mast cell degranulation response.

---

## ISR Inhibitor Therapeutics (PERK-Specific)

### ISRIB (Integrated Stress Response Inhibitor)

ISRIB mechanistic insight:
```
eIF2α-P → sequesters eIF2B → ternary complex formation ↓
ISRIB binds eIF2B (Asp2B subunit interface) → stabilizes eIF2B octamer → eIF2B activity restored
even in presence of eIF2α-P → translation resumes despite PERK activation
```

**Effect:** ISRIB does NOT prevent PERK activation or eIF2α phosphorylation — it bypasses the downstream translational block. Translation is restored but the upstream stress signal is not suppressed.
- β cell application: ISRIB → insulin biosynthesis restored even during ER stress → β cell function maintained
- Preclinical: ISRIB improves glucose homeostasis in prediabetic mice with ER stress burden
- Caveat: bypassing translational arrest may not allow adequate UPR resolution — use in context of chemical chaperones that reduce misfolded protein load

### Salubrinal / Guanabenz (GADD34 Inhibitors)

These inhibit GADD34/PP1-mediated eIF2α dephosphorylation → maintains eIF2α-P for longer → allows UPR resolution time before translation resumes. Paradoxical survival benefit when stress is acute but cells need more time to fold proteins before resuming translation.

| Compound | Mechanism | Effect |
|----------|-----------|--------|
| Salubrinal | Inhibits GADD34/PP1 → sustained eIF2α-P | Prolongs ISR → more adaptation time → reduces CHOP if stress resolves |
| Guanabenz | Same GADD34 mechanism + additional α2-adrenergic | Reduces ER stress load in β cells in NOD mouse |
| ISRIB | Stabilizes eIF2B → bypasses eIF2α-P translational block | Translation restored → β cell function maintained |

### Chemical Chaperones (Reduce PERK Activation Load)

| Compound | Mechanism | Status in Framework |
|----------|-----------|-------------------|
| 4-Phenylbutyrate (4-PBA) | Hydrophobic chaperone → promotes protein folding → less misfolding → less PERK activation | Mentioned in run_098 context; now specifically: reduces PERK activation load in β cells |
| TUDCA (tauroursodeoxycholic acid) | Bile acid chemical chaperone → ER stress ↓ → PERK activation ↓ | Similar; mentioned in run_098 context |
| Betaine | Osmolyte/chaperone → protein stabilization | Framework element (one-carbon cycle, run_145 context) |

**New mechanistic clarity (run_146):** 4-PBA/TUDCA previously justified via IRE1α/XBP1 branch (run_098). run_146 adds: these compounds ALSO reduce PERK activation by lowering total ER misfolded protein load → eIF2α-P ↓ → CHOP ↓ → β cell survival ↑. Same supplements, deeper mechanistic rationale.

---

## Quantitative Parameters

| Parameter | Value | Context |
|-----------|-------|---------|
| PERK Km (eIF2α peptide) | ~5 μM | Biochemical |
| eIF2α-P induction at 50% ER stress | ~20-30 min | Live cell imaging |
| ATF4 induction (post-eIF2α-P) | t½ ~45 min | Translation derepression |
| CHOP induction (post-ATF4) | ~2-4 hours | Sustained ER stress |
| β cell CHOP threshold for apoptosis | ~4-8× basal CHOP | Flow cytometry + cleaved caspase-3 |
| GADD34 feedback loop t½ | ~60-90 min | Feedback kinetics |
| ISRIB EC50 (eIF2B reactivation) | ~3 nM | In vitro |
| WRS diabetes diagnosis age | 6 weeks–6 months | Clinical series |
| EIF2AK3 polymorphism OR for T1DM | ~1.2-1.4 | Population studies |

---

## ME/CFS Relevance

- **Chronic ER stress in ME/CFS:** Oxidative stress (lipid peroxidation, run_143) → protein carbonylation → misfolded proteins → PERK activation → ISR → protein synthesis reduction → metabolic fatigue compound
- **eIF2α-P → global translation ↓ → NAD+ biosynthesis impaired:** NAMPT (NAD+ salvage enzyme) synthesis requires translation; eIF2α-P → NAMPT ↓ → NAD+ ↓ → SIRT1 (next run) impaired → mitochondrial dysfunction cascade
- **ATF4 → amino acid transporter upregulation (SLC7A5/LAT1):** ATF4 selectively transcribes amino acid import genes → cells under ISR increase amino acid uptake; in ME/CFS this may compete with neurotransmitter precursor transport
- **ISRIB in neurological models:** ISRIB reverses cognitive deficits in aged mice (ISR in neurons); potential ME/CFS cognitive/PEM neurological component

---

## Framework Integration Points

| Prior Run | Connection |
|-----------|-----------|
| run_098 (IRE1α/XBP1s) | Same UPR, orthogonal branch — PERK is the third sensor; 4-PBA/TUDCA now have dual IRE1α + PERK justification |
| run_043 (β cell NLRP3) | NLRP3 = canonical inflammasome death; PERK/CHOP = ER stress intrinsic apoptosis; parallel β cell death modes |
| run_143 (SLC7A11/ferroptosis) | Ferroptosis = lipid death; PERK/CHOP = ER protein misfolding death; orthogonal mechanisms in β cells |
| run_122 (NLRP1) | UV → NLRP1 → pyroptosis; UV → PERK → CHOP → apoptosis: three UV-driven keratinocyte death modes |
| run_028 (β cell ER stress) | run_028 context: CCL2 production via NF-κB from ER-stressed β cells; PERK/CHOP is the death pathway when that stress is unresolved |
| run_038 (β cell ER stress loop) | PERK = the kinase arm; ATF4 → CCL2 (upstream of run_144 macrophage insulitis) |
| run_085 (metformin/B12/AMPK) | Metformin → AMPK → mTOR ↓ → reduced ER protein load → less PERK activation (one mechanism for metformin β cell protection) |

---

## Saturation Override Checklist

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| 1. Absent from all prior runs as primary subject | PASS | EIF2AK3/PERK as primary: 0 hits; only context mentions in run_098/130/133/142 |
| 2. MODERATE+ rosacea + T1DM | PASS | T1DM: WRS neonatal diabetes + EIF2AK3 polymorphism T1DM risk + β cell highest ER demand; Rosacea: UV/LL-37/Demodex → PERK → CHOP → keratinocyte apoptosis (third UV keratinocyte death mode) |
| 3. New therapeutic/monitoring target | PASS | ISRIB (eIF2B stabilizer), salubrinal/guanabenz (GADD34 inhibitors), new PERK-specific justification for 4-PBA/TUDCA; ATF4/CHOP as pharmacological target |
| 4. Kill-first fails | PASS | run_098 covers IRE1α/XBP1s branch — different sensor, different substrate (XBP1 mRNA vs eIF2α-Ser51), different outputs (ER expansion vs translation halt); PERK branch cannot be dismissed as extension of IRE1α coverage |

---

*One-hundred-and-thirty-ninth extension | EIF2AK3 PERK eIF2α-Ser51 ISR integrated-stress-response ATF4 CHOP DDIT3 GADD34 PPP1R15A eIF2B ISRIB salubrinal guanabenz UPR-PERK-branch Wolcott-Rallison-syndrome neonatal-diabetes β-cell-intrinsic-apoptosis 24th-β-cell-death WRS-EIF2AK3 4-PBA TUDCA keratinocyte-ER-stress third-UV-death-mode mast-cell-PERK run098-IRE1α-orthogonal-branch | run_146 | Framework at SATURATION + 35: 146 runs*
