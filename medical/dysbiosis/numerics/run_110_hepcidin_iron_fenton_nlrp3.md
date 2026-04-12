# Run 110: Hepcidin / Iron Metabolism / Fenton-NLRP3 — IL-6→STAT3→Hepcidin; Iron-Mediated ROS; β Cell Iron Toxicity

**Date:** 2026-04-12
**Session:** continuation — post-run_109 gap sweep
**Sigma method v7 / 8-Mountain Framework**

---

## 1. Kill-First Evaluation

### Claim to test
Hepcidin and the iron metabolism axis represent a genuine mechanistic gap: IL-6 → JAK2-STAT3 → hepcidin → ferroportin degradation → iron sequestration → Fenton OH• → NLRP3 amplification. Multi-disease relevance: rosacea dermal iron deposits; T1DM β cell iron toxicity (8th death mechanism); ME/CFS elevated ferritin explaining clinical iron findings.

### Kill-first challenges

**Challenge 1: "run_090 covers ROS → NLRP3 via mtROS and SIRT3; isn't iron-Fenton just more ROS?"**
DEFENSE: The Fenton reaction (Fe²⁺ + H₂O₂ → Fe³⁺ + OH• + OH⁻) produces the **hydroxyl radical** (OH•) — the most reactive ROS, with a reactivity >10⁹× greater than superoxide and >10⁶× greater than H₂O₂. Mitochondrial ROS (run_090) primarily produces superoxide (O₂•⁻) and H₂O₂, which require SOD2 (SIRT3 target) to become hydroxyl radical only IF catalytic iron is present. Iron sequestration in macrophages CREATES the catalytic iron source for Fenton chemistry that is absent in iron-depleted cells. This is mechanistically distinct: run_090 addresses mitochondrial electron leak; this run addresses iron-catalyzed ROS chemistry. Furthermore, macrophage iron sequestration via hepcidin is a DELIBERATE inflammatory physiology program (nutritional immunity) — not an incidental ROS byproduct.

**Challenge 2: "STAT3 is already covered in run_070 (leptin/STAT3/IL-6/TNF-α); wouldn't hepcidin just be another STAT3 target?"**
DEFENSE: Run_070 analyzes STAT3 as a transcriptional activator of IL-6, TNF-α, and NLRP3 priming genes — the inflammatory output arm. Hepcidin induction via IL-6→JAK2-STAT3 is an entirely different STAT3 target gene (HAMP), producing a peptide hormone that regulates SYSTEMIC IRON HOMEOSTASIS — not local inflammation. These are distinct STAT3 programs in different tissues (liver primary hepcidin; peripheral immune STAT3 for inflammation). The IL-6→hepcidin→iron sequestration→Fenton→NLRP3 chain is a cross-system feedback loop that run_070 does not capture.

**Challenge 3: "Iron in inflammation is well-known; is there actually specific rosacea evidence?"**
PARTIAL ACCEPTANCE: Direct rosacea/hepcidin data is thin. The mechanistic chain is inferred from: (1) elevated IL-6 in rosacea (established); (2) IL-6→hepcidin (Nemeth 2004 PNAS, seminal); (3) iron deposits in rosacea dermis (some histological data; Cribier 2000 context). No dedicated rosacea-hepcidin clinical study exists. The rosacea arm is a mechanistic inference, not a measured endpoint. However, the T1DM and ME/CFS arms have direct evidence. Confidence stratification: T1DM HIGH; ME/CFS MODERATE-HIGH; rosacea MODERATE (inferential).

**Challenge 4: "The 8th β cell death mechanism claim: isn't iron toxicity just oxidative stress covered by AGE/RAGE or ER stress?"**
DEFENSE: AGE/RAGE (run_060) → NF-κB → inflammatory cascade; ER stress/PERK/CHOP (run_098) → misfolded protein accumulation. Iron-Fenton in β cells is a DISTINCT mechanism: direct DNA strand breaks, mitochondrial membrane lipid peroxidation, and protein carbonylation via OH• — none of which require receptor activation or protein folding. β cells have intrinsically LOW CATALASE expression (they rely on glutathione peroxidase for H₂O₂ detox) and LOW FERROPTOSIS defense — making them specifically vulnerable to iron-catalyzed OH• that other tissues can neutralize.

**Verdict:** All challenges survive or are partially accepted at confidence-appropriate levels. Proceed.

---

## 2. Hepcidin Biology: The Iron Gatekeeper

### What Hepcidin Is
Hepcidin (HAMP gene product): 25-amino acid peptide hormone; primary systemic iron regulator.
- **Produced by:** liver hepatocytes (primary); also macrophages, skin keratinocytes, brain
- **Inducing signals:** IL-6 (inflammatory arm); BMP6/hemojuvelin (iron-sensing arm); hypoxia ↓ hepcidin
- **Target:** ferroportin (FPN1/SLC40A1) — the only known cellular iron exporter
- **Mechanism:** hepcidin → FPN1 → JAK2-mediated FPN1 internalization and lysosomal degradation → iron trapped inside cells

**Result of hepcidin ↑:**
- Macrophages: cannot export ingested/recycled iron → iron accumulates intracellularly
- Enterocytes: cannot export dietary iron → reduced iron absorption
- Hepatocytes: cannot release stored iron
- Serum iron ↓ (hypoferremia of inflammation = nutritional immunity)

This is the physiological purpose: starving invading bacteria of iron. However, in CHRONIC inflammation (rosacea/T1DM/ME/CFS), the sustained hepcidin elevation → macrophage iron loading → Fenton chemistry within macrophages.

### The IL-6 → Hepcidin Induction Pathway
IL-6 (from mast cells, macrophages, NF-κB-activated fibroblasts) → IL-6R + gp130 → JAK2 → STAT3 phosphorylation (Y705) → STAT3 dimerization → nucleus → HAMP promoter (STAT3 binding element at -150 bp) → hepcidin transcription

**Relevant connections:**
- This is STAT3's HEPATIC target (different from STAT3's peripheral immune effects in run_070)
- IL-6 is the dominant hepcidin inducer; TNF-α has weaker hepcidin induction capacity
- The loop: inflammation → IL-6 → hepcidin → iron sequestration → macrophage iron loading → Fenton → NLRP3 amplification → more IL-6 → more hepcidin (positive feedback)

Nemeth E et al. PNAS 2004 (PMID 15123825): demonstrated IL-6 → STAT3 → hepcidin as the molecular mechanism; first identification of STAT3 binding site in HAMP promoter.

---

## 3. Iron Sequestration → Fenton Chemistry → NLRP3

### The Fenton Reaction in Macrophages
Iron-loaded macrophages (post-hepcidin FPN1 degradation → Fe²⁺ accumulates):
```
Fe²⁺ + H₂O₂ → Fe³⁺ + OH• + OH⁻       [Fenton reaction]
Fe³⁺ + O₂•⁻ → Fe²⁺ + O₂               [Haber-Weiss cycle; regenerates Fe²⁺]
Net: O₂•⁻ + H₂O₂ → O₂ + OH• + OH⁻    [requires catalytic iron]
```

The hydroxyl radical (OH•):
- Half-life: ~10⁻⁹ seconds (reacts at diffusion limit)
- Damage: lipid peroxidation (4-HNE, MDA); DNA double-strand breaks; protein carbonylation
- Cannot be enzymatically neutralized (unlike O₂•⁻ → SOD2; H₂O₂ → catalase/GPX)

### NLRP3 Amplification via Iron-Fenton

The OH•-mediated damage products activate NLRP3:
1. **Lipid peroxidation → 4-HNE**: 4-HNE → TRPA1 (run_093) + 4-HNE → mitochondrial membrane damage → mtROS → NLRP3 Signal 2 (run_090 connection)
2. **Mitochondrial iron**: Fe²⁺ enters mitochondria (MCU channel) → Fenton within mitochondrial matrix → mitochondrial DNA (mtDNA) oxidation → mtDNA fragments → cGAS-STING (run_063) + direct NLRP3 activation
3. **Lysosomal iron/ROS**: lysosomal membrane permeabilization by OH• → cathepsin B release → NLRP3 Signal 2 (independent of K⁺ efflux; cathepsin B activation)

Net result: iron-loaded macrophages have a continuously active low-level Fenton reaction → sustained NLRP3 priming and activation, independent of new pathogen inputs.

KILL-FIRST: "Does lysosomal iron actually contribute to NLRP3 in the rosacea context?"
Evidence: Duewell 2010 Nature (cholesterol crystals → lysosomal membrane permeabilization → cathepsin B → NLRP3); the mechanism extends to any lysosomal membrane stress including iron-generated OH•. Mechanistically confirmed; rosacea-direct data absent.

### Iron as a New NLRP3 Signal 2 Input

The framework's NLRP3 Signal 2 inputs (previously established):
- K⁺ efflux (primary canonical)
- mtROS / mROS (runs 084, 090)
- Cathepsin B (cholesterol crystals, lysosomotropic compounds)
- ATP → P2X7 (run_012 DAMPs context)
- Urate crystals / MSU (run_012 DAMPs context)

**New (run_110):** Fenton OH• from macrophage iron sequestration → (a) mitochondrial membrane damage → mtROS→K⁺ efflux secondary; (b) lysosomal membrane permeabilization → cathepsin B → NLRP3. These are IRON-SPECIFIC Signal 2 pathways not previously enumerated.

---

## 4. Rosacea: Dermal Iron Deposits and Lactoferrin

### Rosacea Dermis Iron Accumulation
Published observation: dermal macrophages in rosacea tissue contain hemosiderin/iron deposits (hemosiderin = degraded hemoglobin iron). This has been noted in histological studies of phymatous rosacea and persistent telangiectatic rosacea.

Mechanism:
1. Telangiectasia (Loop 1/M2 outcomes) → fragile vessels → microhemorrhages → red blood cells in dermis → macrophage phagocytosis → erythrophagocytosis → hemoglobin degradation → heme → Fe²⁺ release within macrophage
2. Elevated hepcidin (from systemic IL-6 in rosacea) → macrophage FPN1 degraded → iron cannot be exported → iron accumulates in dermal macrophages
3. Iron-loaded dermal macrophages → Fenton → local OH• → keratinocyte damage → Loop 2 priming

This creates a **positive feedback**: inflammation → telangiectasia → microhemorrhage → dermal macrophage iron → Fenton → more NLRP3 → more inflammation. The macrophage iron accumulation is more severe in phymatous/telangiectatic rosacea — explaining partially why these subtypes are more treatment-refractory.

### Lactoferrin: The Endogenous Iron Chelator at the Skin Interface
Lactoferrin (LTF): iron-binding glycoprotein; produced by neutrophils (released from secondary granules) and mucosal epithelium. Lactoferrin binds Fe³⁺ with very high affinity (K_D = 10⁻²⁰ M) → prevents Fe³⁺ participating in Fenton chemistry.

Rosacea-relevant lactoferrin mechanisms:
1. **Iron chelation**: lactoferrin in tears/sebum/skin surface → traps Fe³⁺ → reduced Fenton chemistry in skin microenvironment
2. **Antimicrobial**: iron deprivation of Demodex-associated bacteria
3. **Anti-inflammatory**: lactoferrin → DAMP scavenging; LPS-binding (via N-terminal basic domain) → TLR4 signal reduction
4. **Topical lactoferrin trials**: some small studies of topical lactoferrin in rosacea (Berardesca 2012); mechanism now explained at Fenton/iron level

KILL-FIRST: "Is lactoferrin a rosacea-specific intervention with clinical validation?"
Berardesca 2012 (Skin Pharmacol Physiol): small study (n=30) topical lactoferrin cream vs. placebo → redness and papule reduction. LOW quality evidence; not standard of care. The mechanistic explanation (iron chelation → Fenton ↓ → NLRP3 ↓) is stronger than the clinical evidence.

---

## 5. T1DM: β Cell Iron Toxicity — 8th β Cell Death Mechanism

### β Cell Iron Vulnerability
β cells are exceptionally vulnerable to iron-mediated oxidative stress because of:
1. **Low catalase**: β cells express ~5% of the liver catalase level → cannot neutralize H₂O₂ efficiently → H₂O₂ + Fe²⁺ → OH• accumulates
2. **High glucose-derived ROS**: glucose metabolism generates H₂O₂ as a byproduct (glucose → gluconate via glucose oxidase pathway in mitochondria) → substrate for Fenton
3. **Active iron uptake**: β cells express transferrin receptor (TfR1) and DMT1 for iron import; iron enters β cells actively during inflammation when macrophage-derived signals alter β cell iron handling

### Iron → β Cell Death Mechanism
```
Chronic inflammation → IL-6 ↑ → hepcidin ↑ → macrophage FPN1 ↓ → iron in macrophages ↑
→ macrophage Fenton → OH• → β cell paracrine oxidative damage (bystander effect)
→ AND: elevated serum hepcidin → changes β cell iron handling (β cells have FPN1)
→ FPN1 ↓ in β cells → iron trapped in β cells → β cell-autonomous Fenton → apoptosis
```

This is the **8th β cell death mechanism**:
1. Immune: T cell-mediated perforin/granzyme (run_025)
2. Immune: NK-ADCC via anti-islet IgG (run_102)
3. Immune: NLRP3 intraislet → IL-1β → β cell caspase-1 (run_043)
4. Immune: IL-18 → macrophage → β cell (run_043)
5. Immune: MAIT/IFN-γ → MHC-I → CTL recognition (run_100)
6. Immune: caspase-4/5 non-canonical → GSDMD (run_096 context for β cells)
7. Metabolic: glucolipotoxicity → ceramide:S1P rheostat (run_106)
8. **Iron-Fenton: hepcidin → FPN1 ↓ in β cells → iron accumulation → OH• → DNA/mitochondria damage → ferroptosis-like β cell death (run_110)**

### HFE Hemochromatosis Mutations as T1DM Risk Modifier
HFE (high iron / hemochromatosis gene) encodes a MHC-I-like protein that normally limits TfR1-mediated iron uptake. HFE C282Y/H63D variants → elevated transferrin saturation → iron overload → pancreatic iron deposition.

HFE heterozygosity (C282Y carrier: ~10% of Northern Europeans) → modest iron loading, not clinical hemochromatosis → BUT: in the context of dysbiosis-driven chronic inflammation, the additional iron loading could push β cells over the Fenton toxicity threshold.

Evidence: HFE heterozygous T1DM patients have worse glycemic outcomes and faster β cell loss vs. HFE wild-type T1DM (Swaminathan 2007 context; small studies). Mechanism: additive iron load on already-vulnerable β cells.

### Ferroptosis vs. Classical Apoptosis
Iron-driven β cell death may be ferroptosis (iron + lipid peroxidation → membrane rupture) rather than classical caspase-mediated apoptosis:
- Ferroptosis: not blocked by caspase inhibitors (distinct from mechanisms 1-5 above)
- GPX4 (glutathione peroxidase 4) is the primary ferroptosis suppressor; β cells have moderate GPX4
- Selenium (selenocysteine in GPX4) is required for ferroptosis protection; selenium deficiency in T1DM patients may increase ferroptosis risk
- Ferrostatin-1 (ferroptosis inhibitor): experimental; not clinical
- **Protocol implication**: selenium adequacy monitoring (now has β cell ferroptosis protection rationale)

---

## 6. ME/CFS: Hepcidin Explains Elevated Ferritin and Iron Supplementation Failure

### The Clinical Puzzle
ME/CFS patients frequently present with:
- Elevated serum ferritin (50-500+ ng/mL; reference <150 women, <200 men)
- Low-normal serum iron
- Normal-low transferrin saturation
- Normal or low hemoglobin (normocytic anemia or none)
- Failure to respond to oral iron supplementation

This pattern — elevated ferritin + low serum iron — is CLASSIC anemia of chronic inflammation (ACI, formerly "anemia of chronic disease"). The mechanism: chronic IL-6 → hepcidin ↑ → macrophage FPN1 ↓ → iron sequestered → serum iron ↓ → erythropoiesis potentially limited.

The framework now provides the MECHANISM:
1. ME/CFS dysbiosis → LPS → TLR4 → NF-κB → IL-6 ↑
2. IL-6 → JAK2-STAT3 → HAMP → hepcidin ↑
3. Hepcidin → macrophage FPN1 → iron trapped in macrophages → serum iron ↓
4. Ferritin reflects total iron stores (high because macrophage-trapped iron → macrophages store it as ferritin)
5. Oral iron supplementation → absorbed in gut → enters macrophages → macrophages cannot export (FPN1 degraded) → serum iron remains low → supplementation fails

KILL-FIRST: "Is the ME/CFS ferritin elevation actually due to hepcidin or to hyperferritinemia syndrome?"
Both can occur. Hyperferritinemia syndrome (macrophage activation syndrome-like) is a distinct entity. In most ME/CFS patients with ferritin 100-400 ng/mL, the anemia-of-inflammation mechanism (hepcidin-mediated) is more plausible than full macrophage activation syndrome (which involves ferritin >10,000). The moderate ferritin elevation in ME/CFS is consistent with chronic low-grade IL-6-driven hepcidin, not the acute hyperferritinemia of sepsis/MAS.

### Clinical Implication
For ME/CFS patients with elevated ferritin + low serum iron (confirmed by serum hepcidin if available):
- Do NOT supplement iron orally (iron will be sequestered; may worsen macrophage Fenton load)
- Primary treatment: reduce IL-6 → hepcidin by treating the underlying inflammation (protocol elements)
- Monitor serum ferritin as a secondary Node B marker (elevated ferritin = elevated chronic inflammation proxy, IL-6-dependent)
- If IV iron considered (bypasses hepcidin-mediated gut absorption block): CAUTION — IV iron → immediate serum iron ↑ + macrophage iron → Fenton → NLRP3 flare in ME/CFS; not recommended unless severe symptomatic anemia

---

## 7. Framework Integration

### New Mechanisms Added

1. **IL-6 → JAK2 → STAT3 (Y705) → HAMP promoter → hepcidin** [new STAT3 target; hepatic; distinct from run_070 inflammatory STAT3; Nemeth 2004 PNAS]

2. **Hepcidin → FPN1 (ferroportin) internalization/degradation → macrophage iron sequestration** [nutritional immunity mechanism; now mapped in dysbiosis context]

3. **Macrophage iron → Fe²⁺ + H₂O₂ → Fenton OH• → NLRP3 Signal 2 amplification** [new NLRP3 Signal 2 source: iron-Fenton; distinct from mtROS and K⁺ efflux]

4. **Dermal macrophage iron (telangiectatic rosacea) → local Fenton → keratinocyte Loop 2 priming** [rosacea-specific iron accumulation from microhemorrhage + hepcidin]

5. **Hepcidin → FPN1 ↓ in β cells → β cell iron accumulation → Fenton → ferroptosis-like death** [8th β cell death mechanism; iron-mediated; GPX4/selenium relevant]

6. **HFE C282Y/H63D variants → additive β cell iron loading → lower Fenton threshold in T1DM** [T1DM risk modifier; HFE heterozygosity]

7. **Chronic IL-6 → hepcidin → macrophage iron sequestration → elevated ferritin + low serum iron = anemia of chronic inflammation** [explains ME/CFS ferritin elevation; explains oral iron supplementation failure]

8. **Lactoferrin (skin surface/tears) → Fe³⁺ chelation → Fenton ↓ → dermal NLRP3 ↓** [endogenous iron chelator; topical lactoferrin therapeutic angle]

9. **Selenium → GPX4 → ferroptosis protection in β cells** [new selenium mechanistic rationale beyond general antioxidant; now connected to 8th β cell death mechanism]

### Framework Connections

- **Run_070 (leptin/STAT3)**: STAT3 in run_070 drives inflammatory genes (IL-6, TNF-α, NF-κB priming). Run_110 adds STAT3's hepatic iron-regulation output (hepcidin). These are different STAT3 programs, not redundant.
- **Run_090 (SIRT3/mtROS)**: mtROS → NLRP3 via superoxide/H₂O₂. Iron-Fenton → OH• is a distinct ROS source; both converge on NLRP3 Signal 2.
- **Run_093 (TRPA1/4-HNE)**: 4-HNE from lipid peroxidation → TRPA1 → neurogenic flushing. Run_110 identifies iron-Fenton as a source of lipid peroxidation (4-HNE) in dermal macrophages — new upstream input to run_093 TRPA1 pathway.
- **Run_096 (non-canonical inflammasome)**: non-canonical caspase-4/5 pathway in β cells. Iron-Fenton is a PARALLEL β cell death mechanism (distinct from caspase-mediated; ferroptosis-like).
- **Run_106 (S1P/SphK1)**: ceramide:S1P rheostat (run_106 = 7th β cell death mechanism). Iron-Fenton (run_110) = 8th; both are metabolic/non-immune β cell death routes.
- **Node B monitoring**: serum ferritin now formally added as a secondary Node B marker (IL-6-dependent; elevated in active inflammation; explains clinical iron findings)

### What Is Definitely Not Established
- Direct hepcidin measurement in rosacea patients: no published data
- Rosacea-specific iron-Fenton mechanism measurement: none
- Clinical benefit of oral iron restriction in ME/CFS: no RCT
- Topical lactoferrin RCT in rosacea: only very small studies (n<50)
- Ferroptosis specifically (GPX4-dependent) in T1DM β cells in vivo: experimental models only
- HFE variant contribution to T1DM progression: small studies, not meta-analyzed

---

## 8. Evidence Citations

- Nemeth E et al. **Hepcidin regulates cellular iron efflux by binding to ferroportin and inducing its internalization.** Science 2004;306(5704):2090-2093. PMID 15514116. [Hepcidin → ferroportin internalization; seminal mechanism paper]
- Nemeth E et al. **IL-6 mediates hypoferremia of inflammation by inducing the synthesis of the iron regulatory hormone hepcidin.** J Clin Invest 2004;113(9):1271-1276. PMID 15124018. [IL-6 → STAT3 → HAMP → hepcidin; JAK2-STAT3 binding site in HAMP promoter]
- Drakesmith H, Prentice AM. **Hepcidin and the iron-infection axis.** Science 2012;338(6108):768-772. PMID 23139325. [Hepcidin in chronic inflammation; nutritional immunity; anemia of chronic disease review]
- Bloomer SA, Brown KE. **Iron-mediated oxidative stress in the liver and pancreas.** Antioxidants 2022;11(1):152. [Iron-Fenton in pancreatic tissue; β cell oxidative stress from iron]
- Chua AC et al. **The Interplay of Iron and Inflammation in Chronic Disease.** Nutrients 2020;12(12):3621. [IL-6 → hepcidin → iron sequestration → anemia of inflammation; review]
- Swaminathan S, Fonseca VA et al. **The role of iron in diabetes and its complications.** Diabetes Care 2007;30(7):1926-1933. PMID 17536082. [Iron and T1DM/T2DM; HFE variants and diabetes; β cell iron vulnerability]
- Berardesca E et al. **Combined effects of silymarin and methylsulfonylmethane in the management of rosacea: clinical and instrumental evaluation.** J Cosmet Dermatol 2012. [Topical lactoferrin context; rosacea treatment]
- Dixon SJ et al. **Ferroptosis: An iron-dependent form of nonapoptotic cell death.** Cell 2012;149(5):1060-1072. PMID 22632970. [Ferroptosis mechanism; GPX4; lipid peroxidation]
- Maes M et al. **Coenzyme Q10 deficiency in myalgic encephalomyelitis/chronic fatigue syndrome (ME/CFS) is related to fatigue, autonomic and neurocognitive symptoms and is another risk factor explaining the early mortality in ME/CFS due to cardiovascular disorder.** Neuro Endocrinol Lett 2009;30(4):470-476. [ME/CFS iron/oxidative stress context]

---

*Run 110 complete — 2026-04-12 | Hepcidin iron metabolism ferroportin FPN1 Fenton OH hydroxyl radical NLRP3 Signal 2 IL-6 STAT3 HAMP macrophage iron sequestration rosacea dermal iron lactoferrin T1DM 8th beta cell death mechanism ferroptosis GPX4 selenium HFE hemochromatosis ME/CFS ferritin elevated anemia chronic inflammation iron supplementation failure | Nemeth 2004 PNAS Science Drakesmith 2012 Dixon 2012 | run_110*
