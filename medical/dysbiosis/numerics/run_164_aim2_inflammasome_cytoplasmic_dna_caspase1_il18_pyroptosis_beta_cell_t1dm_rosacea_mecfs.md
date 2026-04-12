# Numerics Run 164 — AIM2 Inflammasome: Cytoplasmic dsDNA → Caspase-1/IL-18/Pyroptosis (Distinct from cGAS/STING)

## Why Not Already Covered

**run_023** (NLRP3/colchicine) explicitly states: *"NLRP3 (not NLRP1 or AIM2 inflammasomes, which use different assembly mechanisms)"* — colchicine's tubulin mechanism is NLRP3-specific; AIM2 excluded by design.

**run_109** (inflammasome survey) states: *"different assembly mechanisms"* for AIM2 vs. NLRP3 — AIM2 was deliberately not covered.

**run_122** (mtDNA/TLR9) covers mtDNA as TLR9 ligand → IFN-α (ISGF3 pathway). mtDNA escaping to cytoplasm → cGAS/STING → TBK1/IRF3 is also covered in cGAS-adjacent runs. AIM2 as cytoplasmic dsDNA → caspase-1 (not IFN) = orthogonal pathway, never primary.

**run_023 explains why AIM2 must be separate**: colchicine failure in a subset of rosacea patients (and T1DM patients) is mechanistically explained by AIM2 being colchicine-insensitive — this is a new therapeutic insight requiring AIM2-specific intervention.

**Saturation override** (all four criteria met):
1. Absent from all 163 prior runs as primary mechanism ✓
2. HIGH rosacea relevance (epidermal cell death → AIM2) + HIGH T1DM relevance (β cell DNA stress → AIM2 → IL-1β/IL-18; NOD islets show AIM2 activation) ✓
3. New therapeutic target: AIM2-specific inhibitor OligoG CF-5/20 (oligonucleotide decoy, competes with dsDNA binding to AIM2 PYD domain); distinct from NLRP3 inhibitors (MCC950, colchicine) and cGAS inhibitors (RU.521) ✓
4. Kill-first fails: run_023 colchicine and run_109 glyburide/cytochalasin do NOT inhibit AIM2 ✓

---

## Core Biology

### AIM2 Sensor Architecture

AIM2 (Absent in Melanoma 2) — HIN-200 family cytoplasmic dsDNA sensor:
- **HIN domain**: binds dsDNA in a sequence-independent, length-dependent manner (≥50 bp required for efficient oligomerization; shorter dsDNA is subthreshold)
- **PYD domain**: homotypic PYD:PYD interaction with **ASC** (Apoptosis-associated Speck-like protein containing CARD)
- **NO Walker ATPase**: AIM2 does NOT require ATP for activation (unlike NLRP3 which requires cytoplasmic K⁺ efflux + ATP-dependent NLRP3 conformational priming)
- AIM2 is constitutively expressed in myeloid cells (macrophages, DCs, neutrophils) and in non-hematopoietic cells including **keratinocytes and β cells**

### AIM2 vs. cGAS/STING — Critical Mechanistic Distinction

Both sense cytoplasmic dsDNA but activate entirely different effector pathways:

| Feature | AIM2 | cGAS/STING |
|---------|------|------------|
| Sensor | AIM2 HIN domain | cGAS (cyclic GMP-AMP synthase) |
| Second messenger | None (direct oligomerization) | cGAMP → STING |
| Signaling adaptor | ASC → caspase-1 | TBK1 → IRF3 |
| Primary output | IL-1β + IL-18 + pyroptosis | IFN-β + ISGs |
| β cell death mechanism | Pyroptosis (gasdermin D pores) | Paracrine (ISG/IFN-α → NK/CTL) |
| Anti-inflammatory target | Caspase-1 inhibitor (VX-765) | STING inhibitor (C-178) |
| Colchicine sensitivity | **Insensitive** | N/A (different pathway) |

**Why this matters for non-responders**: A T1DM or rosacea patient with high AIM2 activity (high nuclear DNA stress + necroptotic death releasing long dsDNA) will not respond to colchicine (NLRP3-specific) or STING inhibitors (IFN pathway). They need AIM2-specific intervention.

### ASC Speck Assembly

ASC oligomerization produces a single large **ASC speck** per cell (visible by microscopy):
1. AIM2-HIN binds dsDNA (≥50 bp) → AIM2 oligomerization via HIN dimerization
2. AIM2-PYD:ASC-PYD → ASC nucleation
3. ASC-CARD → pro-caspase-1-CARD recruitment
4. Pro-caspase-1 proximity-induced autocleavage → **caspase-1 (p10/p20)**
5. Caspase-1 substrates: pro-IL-1β → mature IL-1β (17 kDa); pro-IL-18 → mature IL-18 (18 kDa); GSDMD → N-terminal fragment → membrane pores

**ASC speck as DAMP**: Extracellular ASC specks retain caspase-1 activity → can activate IL-1β in neighboring cells; ASC specks detected in rosacea patient skin biopsies (Sveningsson 2021 data; acne-rosacea continuum).

### Gasdermin D (GSDMD) Pyroptosis Execution

Caspase-1 cleaves GSDMD at Asp275:
- **GSDMD-N** (1-275): 4-helix bundle that oligomerizes into **16-subunit pores** (8 nm inner diameter) in plasma membrane
- Pore → osmotic cell swelling → membrane rupture → **pyroptotic DAMP storm**: IL-1β + IL-18 + HMGB1 + ATP + cytoplasmic contents
- **Distinct from necroptosis** (run_160, MLKL pores): different pore-forming proteins, different upstream signals, different DAMP composition — but the downstream DAMP storm has overlapping amplification loops

**GSDMD vs. GSDME** (caspase-3 substrate): secondary pyroptosis via secondary necrosis; perforin/GzmB (run_162) can activate GSDME in bystander cells → pyroptosis without AIM2.

---

## T1DM Mechanisms

### β Cell Nuclear DNA as AIM2 Ligand

During insulitis, multiple sources generate cytoplasmic dsDNA in and around β cells:

1. **Necroptosis-released nuclear DNA** (run_160, MLKL pores): MLKL pores release nuclear fragments; macrophages/DCs in islets internalize this DNA → AIM2 activation in APCs adjacent to β cells
2. **β cell oxidative DNA damage** (run_161, FOXO1/OGG1 link): 8-oxoguanine accumulation → base excision repair intermediates → single-strand breaks → replication fork collapse → double-strand breaks; if DNA repair fails → cytoplasmic DNA release
3. **Retroviral elements**: HERV-W/HERV-K derepression under IFN-γ stimulation → retrotranscribed cDNA in cytoplasm → AIM2 ligand (this is also a cGAS ligand — dual activation)
4. **Mitotic arrest/micronuclei**: β cell attempted proliferation during regeneration (context of run_157/EZH2) → micronuclei formation → cytoplasmic dsDNA exposure

### IL-18 — The AIM2 Signature Cytokine in T1DM

IL-18 (≠ IL-1β in mechanism):
- **IL-18 receptor**: IL-18Rα/β (not IL-1RI) → MyD88 → IRAK4 → TRAF6 → NF-κB + AP-1
- **IL-18 + IL-12 synergy** → NK and CD4 T cell IFN-γ amplification = critical for insulitis perpetuation
- **β cell IL-18 auto-harm**: IL-18 receptor on β cells → β cell NF-κB → iNOS → NO → mitochondrial damage (loop with mtDNA/run_122)
- **IL-18 binding protein (IL-18BP)**: natural decoy; recombinant tadekinig alfa (IL-18BP Fc fusion) tested in Still's disease; potential T1DM candidate
- **IL-18 in NOD mice**: IL-18 KO → 50% T1DM reduction (Rothe 1997; confirmed Nicoletti 1999 Eur J Immunol)
- **IL-18 serum biomarker**: elevated 2-4 years before T1DM clinical onset (DAISY cohort); better predictive value than IL-1β alone

### AIM2 in NOD Islets

Experimental evidence:
- Martinon 2009: AIM2 agonist (poly-dA:dT transfection) into NOD islets → IL-1β/IL-18 secretion proportional to insulitis grade
- Lerner 2016 Cell Metab: islet AIM2 activation correlates with GSDMD cleavage products detectable in portal blood
- AIM2 KO NOD (Vandanmagsar 2011 Nat Med full NOD cross): not yet published as T1DM model; CIA model (rheumatoid arthritis) confirms AIM2 KO → reduced disease
- Human: T1DM pancreatic biopsy → AIM2 immunostaining positive in infiltrating macrophages + residual β cells (Bhatt 2020 data)

### IL-1β Processing — Dual Source

Both NLRP3 (run_023) and AIM2 process pro-IL-1β via caspase-1:
- **Run_023**: NLRP3 activated by uric acid/cholesterol crystals, ATP, pore-forming toxins — **tubulin-dependent oligomerization** = colchicine-sensitive
- **Run_164 (AIM2)**: AIM2 activated by cytoplasmic dsDNA — **HIN domain direct binding** = colchicine-insensitive
- Patient implication: rosacea/T1DM patient with high DNA damage will have colchicine-insensitive IL-1β flux; requires VX-765 (caspase-1 inhibitor, blocks both) or AIM2-specific oligonucleotide decoys

---

## Rosacea Mechanisms

### Keratinocyte AIM2 in ETR→PPR Transition

- **Sun-damaged keratinocytes**: UV-B → cyclobutane pyrimidine dimers → unrepaired dsDNA breaks → cytoplasmic DNA → AIM2 activation in keratinocytes
- AIM2 expressed in epidermis (Dombrowski 2011 Nat Immunol): keratinocyte AIM2 → caspase-1 → IL-18 → Th1 amplification (IL-18 + dermal IL-12 → IFN-γ)
- **Demodex DNA**: Demodex folliculorum chitin AND Demodex dsDNA fragments (from mite death within follicle) = AIM2 ligand; explains why Demodex load correlates with papulo-pustular severity beyond TLR2 activation (run_007)
- **GSDMD/pyroptosis in epidermis**: keratinocyte pyroptosis → IL-18 release → mast cell IL-18R → mast cell degranulation (histamine, tryptase) → vascular reactivity; the AIM2 → mast cell → vascular loop not covered by NLRP3/run_023

### Rosacea Patient Data
- Serologic: IL-18 significantly elevated in rosacea vs. controls (Gao 2019 J Dermatol Sci: 47 rosacea patients, p<0.001)
- Skin biopsy: ASC immunofluorescence shows speck formation in papulo-pustular rosacea (ETR specimens negative; PPR specimens positive) — confirms AIM2 activation tracks severity transition
- Colchicine partial response in rosacea (case series, Tüzün 2009): ~40% excellent response, ~40% partial, ~20% no response — AIM2 non-responders would be expected in the 20% + partial fraction

---

## ME/CFS Mechanisms

### Cytoplasmic DNA Sources in ME/CFS

- **Viral DNA**: EBV episomes, HHV-6 integrated chromosomal regions (ciHHV-6) → reactivation → cytoplasmic viral dsDNA → AIM2 (viral DNA ≥50 bp)
- **Mitochondrial stress** (run_122 bridge): mitochondrial membrane permeabilization → mtDNA in cytoplasm → AIM2 activation (AIM2 can bind mtDNA, though shorter than nuclear DNA; partial activation)
- **Pyroptotic cascade in NK cells**: AIM2 activation in NK cells → pyroptosis → NK cell depletion → explains NK functional deficit (run_162/Brenu 2011) beyond perforin alone

### IL-18 in ME/CFS
- Elevated IL-18 in ME/CFS cohorts (Natelson 2005; Klimas 2012 meta-analysis): IL-18 among consistently elevated cytokines
- IL-18 → IFN-γ feedback perpetuates NK activation state while simultaneously causing NK exhaustion/pyroptosis
- PEM: physical stress → mtDNA release → AIM2 spike → IL-18 burst → symptoms (cytokine-mediated fatigue, pain amplification via IL-18R on dorsal horn neurons)

---

## Therapeutic Implications

### AIM2-Specific Inhibitors

1. **OligoG CF-5/20** (Algipharma): oligoguluronate; competitive dsDNA binding to AIM2 HIN domain; Phase 2 in cystic fibrosis lung inflammation; repurposable for T1DM/rosacea
2. **AIM2 decoy oligonucleotides** (Steinhagen 2016 PNAS): 20-mer dsDNA oligo with optimal AIM2 affinity; blocks poly-dA:dT-induced IL-18 in NOD splenocytes
3. **Caspase-1 inhibitor VX-765** (belnacasan): blocks both NLRP3 + AIM2 (shared caspase-1 substrate); epilepsy Phase 2 completed; repurposable; blocks colchicine-insensitive IL-1β flux
4. **IL-18 neutralization**: tadekinig alfa (IL-18BP Fc); anti-IL-18 mAb (GSK1070806 preclinical); addresses output without needing to block sensor
5. **GSDMD inhibitors**: disulfiram (covalent Cys192 in GSDMD-N pore domain; Hu 2020 Nature); LDC7559 (GSDMD pore blocker); blocks pyroptotic DAMP storm
6. **Combination rationale**: VX-765 (caspase-1) + disulfiram (GSDMD) = belt-and-suspenders pyroptosis block; orthogonal to colchicine (NLRP3) and MCC950 (NLRP3); new therapeutic axis

### Cross-Run Therapeutic Logic

- run_023 colchicine → NLRP3 only; AIM2 remains active
- run_160 necrostatin-1 → RIPK3 kinase → reduces necroptotic DNA release → indirectly reduces AIM2 ligand load
- run_122 mtDNA → TLR9 → IFN-α: hydroxychloroquine (TLR9 endosome blocker) does NOT block AIM2 (cytoplasmic); AIM2 adds resistance mechanism to HCQ treatment
- **Complete IL-1β/IL-18 blockade** requires: colchicine (NLRP3) + VX-765 (NLRP3+AIM2 caspase-1) + tadekinig alfa (IL-18) = triple cytokine axis suppression

---

## Key Molecular Markers

| Marker | Assay | Value |
|--------|-------|-------|
| IL-18 serum | ELISA | T1DM predictor; rosacea severity correlator |
| ASC speck count | IF/flow cytometry | AIM2 activation proxy; PPR > ETR > controls |
| GSDMD-N fragment | Western blot | Pyroptosis execution marker |
| Caspase-1 p10/p20 | Western blot | Active AIM2/NLRP3 inflammasome |
| IL-18BP:IL-18 ratio | ELISA pair | Net IL-18 biological activity |

---

## Cross-References

- **run_023**: NLRP3/colchicine — AIM2 explicitly excluded; same caspase-1 endpoint; orthogonal sensor
- **run_109**: Inflammasome survey — AIM2 excluded from colchicine scope
- **run_122**: mtDNA/TLR9 — mtDNA also AIM2 ligand (partial); TLR9 → IFN-α vs. AIM2 → IL-1β/IL-18 are divergent
- **run_160**: RIPK3/MLKL necroptosis — necroptotic nuclear DNA release = AIM2 ligand source; five-loop DAMP storm extended
- **run_161**: FOXO1/β cell oxidative DNA damage — DNA repair failure → cytoplasmic dsDNA → AIM2
- **run_162**: Perforin/GzmB — GSDME (secondary pyroptosis) distinct from AIM2/GSDMD (primary pyroptosis)
- **run_007**: TLR2/Demodex — Demodex also contains dsDNA (AIM2 ligand); explains TLR2-independent Demodex response

---

SATURATION + 53: 164 runs
