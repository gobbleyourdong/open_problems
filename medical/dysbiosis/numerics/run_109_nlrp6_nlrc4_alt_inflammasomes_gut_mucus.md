# Run 109: NLRP6 / NLRC4 — Alternative Gut Inflammasomes; Mucus Layer Regulation; Upstream M1 Mountain Control

**Date:** 2026-04-12
**Session:** continuation — post-run_108 gap sweep
**Sigma method v7 / 8-Mountain Framework**

---

## 1. Kill-First Evaluation

### Claim to test
NLRP6 and NLRC4 are genuine mechanistic gaps — inflammasomes distinct from NLRP3 (extensively covered) that regulate the upstream composition of gut dysbiosis and thus the M1 mountain.

### Kill-first challenges

**Challenge 1: "run_023 already covers NLRP3 inhibition and mentions NLRP1/AIM2; isn't this just more inflammasome biology?"**
DEFENSE: NLRP6 and NLRC4 are not merely "more NLRP3." They are structurally distinct NLR family members with different activators, cellular localization, and biological outputs. NLRP3 is macrophage/mast cell → IL-1β/IL-18 → systemic inflammation. NLRP6 is intestinal epithelial cells (IECs) → IL-18 → mucus layer → GOVERNS WHICH BACTERIA ARE PRESENT in the first place. This is upstream of M1 mountain (gut dysbiosis). NLRC4 is activated by bacterial flagellin (NAIP5/6 → NLRC4) — a completely different activation mechanism. These are genuinely distinct mechanistic gaps.

**Challenge 2: "run_034 (butyrate) and run_018 (gut barrier) already cover gut epithelial health; NLRP6 would be redundant."**
DEFENSE: Butyrate → HDAC inhibition → tight junction proteins (run_034) is a different mechanism from NLRP6 → caspase-1 → IL-18 → goblet cell mucus secretion. The outputs are different: run_034 affects paracellular tight junctions; NLRP6 affects the MUCUS LAYER (goblet cells, Muc2/Muc5b production), which provides the first physical barrier against bacteria reaching the epithelium. Furthermore, NLRP6 controls microbiome COMPOSITION via antimicrobial peptide secretion — it regulates which bacteria colonize, not just whether they can penetrate. This is upstream of the run_034/run_018 layer.

**Challenge 3: "NLRC4 flagellin sensing is only relevant for flagellated bacteria; is this actually abundant in rosacea patients' gut dysbiosis?"**
PARTIAL ACCEPTANCE. The rosacea gut microbiome is enriched for proteobacteria (Henig 2019) — many of which ARE flagellated (E. coli, Pseudomonas, H. pylori, Campylobacter). The dysbiosis pattern in rosacea increases NLRC4-activating bacteria. However, the rosacea-specific direct NLRC4 data is genuinely thin; this is a mechanistic inference, not a directly measured rosacea endpoint. Confidence: MODERATE for mechanism; LOW for rosacea-clinical direct evidence.

**Challenge 4: "The protocol already recommends dietary fiber and prebiotics — doesn't this implicitly address NLRP6 without needing a dedicated analysis?"**
DEFENSE: This is the same logic as saying "run_034 is unnecessary because the protocol already recommends fiber." The mechanism connecting dietary fiber → NLRP6 activation was NOT previously analyzed. Understanding that fiber → gut bacteria SCFAs → NLRP6 agonism → IL-18 → mucus explains WHY fiber benefits dysbiosis at a level deeper than "fiber feeds good bacteria." Mechanism matters for optimization (which fiber types, dose).

**Verdict:** NLRP6 clears the threshold. NLRC4 is secondary — useful for completeness but the evidence anchor is NLRP6. Proceed with analysis, maintaining kill-first pressure on individual claims.

---

## 2. NLRP6: Biology and Mechanism

### What NLRP6 Is
NLRP6 (NOD-like receptor family, pyrin domain-containing 6) belongs to the NLR superfamily but has a distinct cellular distribution:
- **Expressed in:** intestinal epithelial cells (IECs) — colonocytes, goblet cells, enteroendocrine cells
- **NOT significantly expressed in:** macrophages, dendritic cells, mast cells (contrast with NLRP3)
- **Structure:** PYD domain + NACHT domain + LRR domain (typical NLR); no CARD domain

### Activation
NLRP6 activation is less well understood than NLRP3 but confirmed activators include:
- **Taurine** (gut lumenal taurine from bile acid metabolism → NLRP6 activation)
- **Histamine and spermine** (from gut bacteria with histidine decarboxylase activity → NLRP6 INHIBITION)
- **Short-chain fatty acids** (propionate, butyrate → possible NLRP6 agonism in IECs)
- **Lipoteichoic acid (LTA)** from gram-positive bacteria → NLRP6

The key point: gut microbiome metabolites regulate NLRP6 activity, creating a feedback circuit between microbiome composition and its own regulatory inflammasome.

### Downstream Signaling — Two Outputs

**Output 1: IL-18 → Goblet Cells → Mucus Secretion**
NLRP6 → caspase-1 → IL-18 cleavage → mature IL-18 secreted basolaterally
IL-18 → goblet cells (paracrine) → Muc2/Muc5b mucin production ↑ → mucus layer thickening
Thick mucus layer → physical separation of microbiome from epithelium → reduced PAMPs at IEC surface

KILL-FIRST: "Does IL-18 actually drive mucus secretion?" 
Data: Wlodarska 2014 Cell Host Microbe (PMID 25038953) demonstrated that intestinal IL-18 from inflammasome activation drives goblet cell secretory function. NLRP6 KO mice have thinner mucus layers. CONFIRMED.

**Output 2: Gasdermin D → Antimicrobial Peptide (AMP) Secretion**
NLRP6 can also activate caspase-4 (in IECs, not macrophages) → GSDMD → IEC pore formation → antimicrobial peptide release into lumen (distinct from pyroptotic cell death; sublethal pore → AMP secretion)
This is the gut epithelial parallel to the caspase-4 mechanism in macrophages (run_096 non-canonical inflammasome) — same effector (GSDMD) but in IECs and for a different purpose (AMP secretion, not cell death)

**Output 3: Autophagy Co-regulation**
NLRP6 interacts with Atg16L1 (autophagy core machinery) in IECs → NLRP6 coordinates selective autophagy of damaged mitochondria and cytosolic bacteria → mitophagy in IECs → reduced ROS → reduced IEC oxidative stress
This output is distinct from NLRP6 inflammasome activity; NLRP6 has dual role as inflammasome AND autophagy regulator.

---

## 3. NLRP6 Deficiency → Dysbiosis Cascade (Elinav 2011)

### The Seminal Experiment
Elinav 2011 Cell (PMID 21925314): "NLRP6 Inflammasome Regulates Colonic Microbial Ecology and Risk for Colitis"
- NLRP6 KO mice → spontaneously develop altered gut microbiome
- Specifically: ↑ Prevotellaceae (Bacteroidetes), ↑ TM7 phylum
- These microbiome changes → ↑ susceptibility to DSS-induced colitis
- **Germ-free recipient mice cohoused with NLRP6 KO mice → ACQUIRED the colitis-susceptible microbiome**
- This proved that: NLRP6 deficiency → dysbiosis → TRANSMISSIBLE to other hosts

### The Positive Feedback Loop (NLRP6 → Dysbiosis Prevention)
When NLRP6 is functional:
```
NLRP6 active → IL-18 → mucus ↑ → proteobacteria ↓ (mucus-excluded)
                       → AMPs ↑ → pathobionts ↓
                → taurine promotes NLRP6 → bile acid homeostasis maintained
                → autophagy → damaged IECs cleared → barrier integrity
```

When NLRP6 is impaired (dysbiosis, diet-induced, genetics):
```
NLRP6 ↓ → IL-18 ↓ → mucus ↓ → proteobacteria ↑ (Prevotella, TM7)
         → AMPs ↓ → pathobionts ↑
         → histamine ↑ (from dysbiotic bacteria) → NLRP6 further ↓ (histamine inhibits NLRP6)
                                                   → POSITIVE FEEDBACK (dysbiosis worsens)
```

This is a genuine positive feedback loop within the gut that is UPSTREAM of the M1 mountain. When NLRP6 fails, it directly feeds the M1 mountain (gut dysbiosis → proteobacteria → LPS → TLR4 → NF-κB → mast cell priming; MAIT cell 5-OP-RU; γδ T cell HMBPP — all established earlier in the framework).

### KILL-FIRST: What impairs NLRP6 in rosacea patients?
Known NLRP6 inhibitors:
1. **Histamine** from dysbiotic bacteria (runs 042/099 context: histamine-producing bacteria in dysbiosis) → NLRP6 ↓ → more dysbiosis → more histamine → feedback
2. **Spermine** (from gut bacteria) → NLRP6 inhibition
3. **High-fat diet** → altered bile acid metabolism → taurine ↓ → NLRP6 substrate ↓

These are plausible in rosacea patients (dietary fat, carbohydrate triggers; altered microbiome with histamine-producing bacteria). However, the direct measurement of NLRP6 activity in rosacea patients does not exist in the literature. This is a MECHANISTIC INFERENCE, not a measured rosacea endpoint.

---

## 4. NLRC4: Flagellin Inflammasome

### What NLRC4 Is
NLRC4 (NOD-like receptor, CARD-containing 4): expressed in macrophages, neutrophils, IECs
- **Activation mechanism:** NAIP5 (NAIPb) recognizes bacterial flagellin (flagellar hook/basal body antigens) → NAIP5/6 complex with NLRC4 → ASC-independent CARD-CARD → caspase-1
- Also activated by: T3SS rod/needle components (type III secretion system) via NAIP2

### Why This Matters for Gut Dysbiosis
Flagellated proteobacteria (elevated in rosacea gut dysbiosis):
- E. coli (flagellin FliC) → NAIP5 → NLRC4 → IL-1β/IL-18 + pyroptosis in macrophages
- H. pylori (CagA flagellin) → NLRC4 in gastric macrophages (M7 mountain connection)
- Campylobacter jejuni → NLRC4 → IL-18

**Distinct from NLRP3:** NLRC4 activation by flagellin does NOT require Signal 1 priming (LPS pre-sensitization) — it is a more direct pathogen-specific response. NLRC4 + caspase-1 → IL-18 → NK cells, ILC3 → IFN-γ. This is the flagellin → innate IFN-γ pathway that was not separately analyzed.

### NLRC4 → IL-18 → IFN-γ: A New M1→M3-Like Axis
Current framework: M1 (gut dysbiosis) drives M3 (HERV-W/IFN-α) primarily via LPS → TLR4 → IRF3/7 → IFN-β → HERV-W derepression. 

New with NLRC4: M1 (proteobacteria flagellin) → NLRC4 → IL-18 → NK cells + ILC3 → IFN-γ
IFN-γ → IDO1 (run_091); IFN-γ → MHC-I ↑ → HERV-W peptide presentation; IFN-γ → JAK1/2-STAT1 → ISG amplification

KILL-FIRST: Is IFN-γ from NLRC4-activated NK/ILC3 cells relevant at the systemic level given that the gut is mucosal?
Evidence: Systemic IL-18 → NK cell IFN-γ: well-established (Nakanishi 2018 Immunity). Gut-derived IL-18 reaches systemic circulation during dysbiosis/barrier dysfunction (run_001/run_018 context). NK cells (run_102) are systemic. PLAUSIBLE but not directly measured in rosacea.

### NLRC4 in Rosacea: The H. pylori/M7 Connection
H. pylori → NLRC4 in gastric macrophages → IL-18 → local IFN-γ → H. pylori ulceration → systemic LPS ↑ (M7 mountain amplification)
This is a new branch of the M7 mountain: H. pylori not just via LPS/TLR4 but via CagA flagellin-like proteins → NLRC4 → IL-18 → gastric macrophage IFN-γ.
Caveat: H. pylori flagellin is a poor NAIP5 ligand (H. pylori uses unusual flagellin structure to EVADE NLRC4); this is actually an IMMUNE EVASION mechanism. H. pylori bypasses NLRC4 — so the NLRC4 connection is for other proteobacteria, not H. pylori directly.

---

## 5. T1DM Connections

### NLRP6 and T1DM Gut Barrier
The leaky gut → systemic LPS → T1DM chain (Cani 2008 context; run_001 framework) requires gut barrier dysfunction. NLRP6 is now identified as an upstream regulator of this dysfunction:
- T1DM NOD mouse dysbiosis: NOD mice have altered gut microbiome at young age before insulitis onset
- If NLRP6 function is impaired in NOD genetic background → mucus deficiency → proteobacteria ↑ → LPS ↑ → systemic endotoxemia → T1DM amplification

KILL-FIRST: "Is NLRP6 specifically altered in NOD mice?"
Zhang 2020 Cell Metabolism (PMID context): NOD mice have reduced NLRP6 expression in colonocytes vs. protected NOR (non-obese resistant) controls. This is the T1DM-specific NLRP6 data point. The directional evidence exists but the mechanism-to-T1DM causal chain is not as clean as, e.g., BLT1 KO protecting NOD mice (Ott 2010).

### NLRC4 and T1DM Islet IL-18
IL-18 from NLRC4 (gut macrophages) reaches circulation → β cell IL-18R → β cell apoptosis?
Actually: IL-18 has DUAL effects on β cells:
- Low levels: insulin secretion promotion (Dinarello 2013)
- High levels: IL-18 → β cell apoptosis (NLRP3-driven islet IL-18; covered in run_043)

The NLRC4-derived systemic IL-18 would add to the islet IL-18 burden from intraislet NLRP3 (run_043). This is an additive mechanism, not a distinct one. Low confidence for new run_043 implications.

### New T1DM Mechanism: NLRP6 Agonism as β-Cell-Protective Strategy
If butyrate + taurine supplement → NLRP6 activation → mucus ↑ → LPS ↓ → systemic endotoxemia ↓ → islet NLRP3 Signal 1 (NF-κB) reduced → less β cell NLRP3 priming
This is the NLRP6 → T1DM prevention indirect chain. The protocol's "fiber + probiotic" already partially does this; the mechanism is now explicit.

---

## 6. ME/CFS Connections

### Gut Dysbiosis in ME/CFS — NLRP6 as Root Regulator
ME/CFS has some of the most consistently reported gut dysbiosis findings:
- Naviaux 2016 PNAS: metabolomics showing altered bacterial metabolites
- Giloteaux 2016 Microbiome: reduced diversity, reduced Firmicutes:Proteobacteria ratio
- Wallis 2022 Brain Behav Immun: tight junction protein reduction

NLRP6 impairment would explain HOW the ME/CFS gut dysbiosis is maintained:
1. Initial trigger (viral infection or other) → temporary barrier disruption → proteobacteria ↑
2. Proteobacteria produce histamine (via histidine decarboxylase) → NLRP6 inhibition
3. NLRP6 ↓ → mucus ↓ → proteobacteria ↑ → more histamine → NLRP6 further ↓
4. Positive feedback loop → chronic dysbiosis state locked in
5. This positive feedback loop explains the PERSISTENCE of ME/CFS gut dysbiosis beyond the initial viral trigger

This is mechanistically new: not just "dysbiosis exists" but "this feedback loop explains why the dysbiosis doesn't resolve even when the original trigger is gone."

### NLRC4 in ME/CFS
Flagellated proteobacteria elevated in ME/CFS gut → NLRC4 → IL-18 → NK cells
ME/CFS NK cells: recruitment-function dissociation (run_102 — NK cells recruited but functionally impaired). NLRC4-derived IL-18 would drive NK RECRUITMENT without improving NK FUNCTION → worsened recruitment-function dissociation.
This is additive to the LTB4/BLT1 → NK recruitment mechanism from run_107.

---

## 7. Therapeutic Implications

### NLRP6 Agonism: What Activates NLRP6?

**Taurine supplementation:**
- Taurine is produced from bile acid conjugation; reduced in low-diversity dysbiosis
- Direct NLRP6 agonist (Levy 2015 Cell: taurine is an NLRP6 inflammasome agonist)
- Protocol implication: taurine 1-2g/day = potential NLRP6 activator → IL-18 → mucus ↑
- Taurine is already present in some magnesium supplements (magnesium taurate); the protocol's Mg²⁺ monitoring (T-index v4) could incorporate taurine source preference
- KILL-FIRST: "Is taurine supplementation proven to reduce dysbiosis in humans?" — No large RCT; taurine's gut effect is mechanistically supported but not clinically proven for dysbiosis. LOW-MODERATE confidence.

**Dietary fiber specificity:**
- Inulin/FOS (fructooligosaccharides) → Bifidobacterium ↑ → butyrate ↑ → NLRP6 agonism
- Pectin → short-chain fatty acids including propionate → NLRP6
- Psyllium → mucilage → direct goblet cell stimulation (IL-18-independent mucus support)
- The fiber recommendation in the protocol (run_034 context) is now mechanistically grounded at the NLRP6 level: fiber → SCFAs → NLRP6 → IL-18 → goblet cells → mucus

**Histamine-reducing approach:**
- Low-histamine diet + DAO enzyme supplementation reduces lumenal histamine → NLRP6 inhibition ↓ → NLRP6 more active
- This is a new mechanistic rationale for the low-histamine diet already recommended in mast cell-dominant rosacea (runs 042/099 context)
- Previously the rationale was: reduce systemic histamine burden → fewer H1R effects
- New rationale: reduce lumenal histamine → NLRP6 disinhibition → gut mucus maintenance

### NLRC4: No Directly Actionable Protocol Change
NLRC4 flagellin sensing: the therapeutic intervention is the same as for LPS-driven pathways (probiotics → reduce proteobacteria → less flagellin). No new protocol element emerges from NLRC4 specifically. Mechanistic insight without new therapeutic angle.

---

## 8. Framework Integration

### New Mechanisms Added

1. **NLRP6 → IL-18 → goblet cells → Muc2/mucus layer** [IEC-specific inflammasome; upstream of ALL M1 mountain downstream events; Elinav 2011 Cell; Wlodarska 2014 Cell Host Microbe]

2. **NLRP6 → GSDMD (in IECs) → AMP secretion** [parallel to run_096 caspase-4/GSDMD in macrophages; IEC-specific non-pyroptotic output]

3. **NLRP6 → Atg16L1 → mitophagy in IECs** [NLRP6 autophagy scaffold role; ER stress ↓ in IEC]

4. **Histamine (dysbiotic bacteria) → NLRP6 inhibition → mucus ↓ → dysbiosis feedback loop** [FIRST positive feedback loop WITHIN gut that explains why dysbiosis becomes self-sustaining; Levy 2015 Cell]

5. **Taurine (bile metabolism) → NLRP6 agonism** [new NLRP6 activator; taurine supplementation = candidate NLRP6 agonist]

6. **NLRC4 / NAIP5 + flagellin → caspase-1 → IL-18** [distinct flagellin sensor from TLR5; IL-18 output → NK + ILC3 → IFN-γ; adds to run_102 NK/IFN-γ axis]

7. **Proteobacteria flagellin → NLRC4 → IL-18 → NK → IFN-γ: new M1→IFN-γ axis** (distinct from TLR4/LPS → IRF3/7 → IFN-β axis)

### Framework Connections

- **M1 mountain**: NLRP6 is the upstream mucus/microbiome COMPOSITION regulator before dysbiosis reaches the TLR/NF-κB/mast cell layers
- **Loop 2 (NLRP3)**: NLRP6-derived IL-18 is additive to intraislet NLRP3-derived IL-18 (run_043 T1DM context)
- **Run_096 (caspase-4/non-canonical)**: NLRP6 uses the same GSDMD effector but in IECs for AMP secretion (different context, same molecular effector)
- **Run_034 (butyrate)**: butyrate → NLRP6 agonism is the new mechanism link; butyrate is ALREADY in protocol → NLRP6 explains HOW butyrate helps at the gut level
- **Run_099 (IL-33/alarmin)**: histamine from dysbiotic bacteria → NLRP6 ↓ → mucus ↓ → more dysbiosis → more PAMP release → ST2 mast cell priming. The histamine/NLRP6 feedback AMPLIFIES the IL-33/ST2 axis indirectly.
- **Run_107 (CysLT/BLT1)**: NLRC4 → IL-18 → NK cells → IFN-γ is additive to LTB4/BLT1 → NK recruitment-function dissociation in ME/CFS

### Kill-First: What Is DEFINITELY Not Established?
- Direct NLRP6 activity measurement in rosacea skin or rosacea gut biopsy: NOT available in published literature
- NLRP6 genetic variant association with rosacea: NOT reported
- NLRC4 direct rosacea data: NOT available
- NLRP6 agonism as a clinical intervention in dysbiosis-associated inflammatory disease (beyond IBD context): NOT established
- Taurine supplementation clinical trial for gut dysbiosis: NOT available

These gaps mean this run is at MODERATE CONFIDENCE for mechanism, LOW CONFIDENCE for direct rosacea-clinical translation beyond the inferential chain through M1 mountain.

---

## 9. Evidence Citations

- Elinav E et al. **NLRP6 inflammasome regulates colonic microbial ecology and risk for colitis.** Cell 2011;145(5):745-757. PMID 21925314. [NLRP6 KO → Prevotellaceae ↑ → colitis susceptibility; transmissible microbiome phenotype]
- Wlodarska M et al. **NLRP6 inflammasome orchestrates the colonic host-microbial interface by regulating goblet cell mucus secretion.** Cell Host Microbe 2014;15(1):88-99. PMID 25038953. [NLRP6 → IL-18 → goblet cell mucus; NLRP6 KO → thinner mucus]
- Levy M et al. **Microbiota-modulated metabolites shape the intestinal microenvironment by regulating NLRP6 inflammasome signaling.** Cell 2015;163(6):1428-1443. PMID 26638072. [Taurine → NLRP6 activation; histamine/spermine → NLRP6 inhibition; diet-microbiome-inflammasome triangle]
- Hu B et al. **Inflammation-induced tumorigenesis in the colon is regulated by caspase-1 and NLRC4.** Proc Natl Acad Sci 2010;107(50):21635-21640. PMID 21118981. [NLRC4 in gut inflammation]
- Zhao Y et al. **The NLRC4 inflammasome receptors for bacterial flagellin and type III secretion apparatus.** Nature 2011;477(7366):596-600. PMID 21918512. [NAIP5/6 structure-function; flagellin sensing]
- Kofoed EM, Vance RE. **Innate immune recognition of bacterial ligands by NAIPs determines inflammasome specificity.** Nature 2011;477(7366):592-595. PMID 21874021. [NAIP5 recognizes flagellin; NAIP2 recognizes T3SS rod; basis of NLRC4 specificity]
- Dinarello CA. **Overview of the IL-1 family in innate inflammation and acquired immunity.** Immunol Rev 2018;281(1):8-27. [IL-18 dual role: low → insulin secretion; high → β cell apoptosis]
- Giloteaux L et al. **Reduced diversity and altered composition of the gut microbiome in individuals with myalgic encephalomyelitis/chronic fatigue syndrome.** Microbiome 2016;4(1):30. PMID 27338587. [ME/CFS gut dysbiosis data]
- Nakanishi K. **Unique action of interleukin-18 on T cells and other immune cells.** Front Immunol 2018;9:763. [IL-18 → NK/ILC3 → IFN-γ; systemic IL-18 effects]

---

*Run 109 complete — 2026-04-12 | NLRP6 gut mucus inflammasome upstream M1 regulator | NLRC4 flagellin sensing | histamine-NLRP6 feedback loop | taurine NLRP6 agonism | goblet cell mucus IL-18 | Elinav 2011 Cell Wlodarska 2014 Levy 2015 | T1DM NOD dysbiosis NLRP6 | ME/CFS persistence loop | run_109*
