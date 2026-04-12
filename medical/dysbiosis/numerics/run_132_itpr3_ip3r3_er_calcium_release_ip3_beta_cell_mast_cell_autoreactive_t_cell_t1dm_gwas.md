# Run 132 — ITPR3/IP3R3 (IP3 Receptor Type 3): ER Ca²⁺ Release, β Cell, Mast Cell, Autoreactive T Cell, T1DM GWAS

**Date:** 2026-04-12
**Framework position:** First ER Ca²⁺ RELEASE mechanism; upstream trigger for STIM1/ORAI1 cascade (run_127); completes two-step Ca²⁺ signaling architecture (IP3R → ER Ca²⁺ release → STIM1 sensing → ORAI1 SOCE); first IP3 receptor covered; Mg²⁺ inhibitory mechanism named
**Saturation criteria:** (1) ITPR3/IP3R3/IP3 receptor absent from all 131 prior runs ✓ (2) T1DM HIGH (GWAS rs3181505, independent of HLA; Lowe 2007 PNAS) + Rosacea HIGH (mast cell IgE/FcεRI upstream of STIM1/ORAI1 run_127; keratinocyte UV response) ✓ (3) New: first ER Ca²⁺ release mechanism; ITPR3 provides upstream trigger for STIM1 sensing — extends run_127 architecture by one node; Mg²⁺ mechanism anchored to IP3R3 blocking ✓ (4) Kill-first fails: run_127 (STIM1/ORAI1) covers Ca²⁺ ENTRY from plasma membrane via SOCE; ITPR3 covers Ca²⁺ RELEASE from ER — different protein, different compartment, different mechanism; ITPR3 is the TRIGGER for STIM1 activation ✓

---

## 1. Molecular Architecture

**IP3 Receptor Type 3 (IP3R3 / ITPR3):** Large (~2670 aa, 314 kDa monomer) homo- or heterotetramer in ER membrane. ITPR3 gene at 6p21.31 (adjacent to but independent of HLA region).

**Domain organization:**
```
NH2 — [IP3-binding domain (IBC)] — [Coupling/regulatory domain] — 
       [SERCA-binding/Ca²⁺-sensing] — [6× transmembrane helices (pore-forming)] — COOH

Tetramer: 4 subunits form the Ca²⁺ channel pore
```

**IP3R family:**
| Isoform | Primary expression | T1DM role |
|---------|-------------------|-----------|
| IP3R1 (ITPR1) | Neurons, cerebellum | — |
| IP3R2 (ITPR2) | Heart, hepatocytes | Minor β cell role |
| **IP3R3 (ITPR3)** | **β cells (dominant), mast cells, T cells, keratinocytes** | **GWAS rs3181505; dominant islet isoform** |

**IP3 production pathway:**
```
GPCR (GLP-1R cAMP amplifies) or RTK or IgE/FcεRI
    ↓
Gq → PLCβ    or    Receptor → PLCγ
    ↓
Phosphatidylinositol 4,5-bisphosphate (PIP2) hydrolysis
    ↓
IP3 (inositol 1,4,5-trisphosphate) + DAG
    ↓
IP3 → IP3R3 (ER membrane) → channel opening → ER Ca²⁺ release
DAG → PKC → NF-κB/AP-1 (parallel arm)
```

**Ca²⁺ regulation of IP3R3 (biphasic):**
- Low cytosolic Ca²⁺ (< ~300 nM): ACTIVATES IP3R3 (sensitization — Ca²⁺-induced Ca²⁺ release / CICR)
- High cytosolic Ca²⁺ (> ~1 μM): INHIBITS IP3R3 (inactivation — negative feedback brake)
- Mg²⁺: physiological Mg²⁺ (0.5–1 mM) BLOCKS IP3R3 pore → dampens amplitude; Mg²⁺ deficiency → ITPR3 hyperactivation

---

## 2. Two-Step Ca²⁺ Signaling Architecture

**Complete Ca²⁺ cascade (ITPR3 run_132 + STIM1/ORAI1 run_127):**

```
Step 1 — ER Ca²⁺ Release (ITPR3, run_132):
PLC → IP3 → IP3R3 (ER membrane)
    ↓
ER lumen Ca²⁺ → cytosol (rapid, transient)
    ↓
Cytosolic Ca²⁺ spike (amplitude ~400–800 nM, duration ~5–30 sec)
    ↓
ER Ca²⁺ stores DEPLETED

Step 2 — SOCE/Store-Operated Ca²⁺ Entry (STIM1/ORAI1, run_127):
ER Ca²⁺ ↓ → STIM1 ER Ca²⁺ sensor detects depletion
    ↓
STIM1 oligomerization → ER-PM junctions → gates ORAI1 (CRAC channel)
    ↓
Extracellular Ca²⁺ → cytosol (sustained, maintained until ER refilled)
    ↓
SERCA pumps Ca²⁺ back into ER → IP3R3 re-sensitizes

Integration:
- ITPR3 = trigger (fast peak); STIM1/ORAI1 = maintenance (plateau)
- Together produce Ca²⁺ oscillations → calcineurin/NFAT → effector gene expression
- mast cell: ITPR3 → fast degranulation peak; STIM1/ORAI1 → sustained cytokine synthesis
- β cell: ITPR3 → first-phase insulin secretion; STIM1/ORAI1 → second-phase amplification
- autoreactive T cell: ITPR3 → TCR-triggered ER release; STIM1/ORAI1 → sustained NFAT → IL-2/IFN-γ
```

---

## 3. β Cell Physiology and T1DM GWAS

### 3a. β Cell Ca²⁺ Signaling (ITPR3 central role)

**Insulin secretion Ca²⁺ hierarchy:**
```
Glucose → glucokinase → ATP ↑ → KATP channel closure → membrane depolarization
    ↓
Voltage-gated Ca²⁺ channel (Cav2.1/L-type) → Ca²⁺ influx → first-phase insulin
    +
Incretin (GLP-1R, run_098): GLP-1 → cAMP → PKA → PKA phosphorylates ITPR3
    → IP3R3 sensitized (lower IP3 threshold) → amplified ER Ca²⁺ release
    ↓
ITPR3 → ER Ca²⁺ → cytosol Ca²⁺ pool ↑ → potentiates exocytosis
    +
ER-mitochondria Ca²⁺ microdomains (VDAC/MCU):
ITPR3 at ER-mito contacts → Ca²⁺ → MCU → mitochondrial matrix Ca²⁺ ↑
→ PDH/IDH/α-KGDH (TCA cycle enzymes activated) → NADH/FADH2 ↑ → ATP ↑ (amplification)
→ More KATP closure → sustained depolarization → sustained insulin secretion
```

**ITPR3 in β cell Ca²⁺ oscillations:**
- β cells under constant glucose: Ca²⁺ oscillations (1–5 min period) coordinate pulsatile insulin secretion
- ITPR3 contributes to oscillation initiation and shaping: IP3R3-mediated ER release → Ca²⁺ trigger → CICR → spike; SERCA reuptake → oscillation reset
- T1DM pathology: inflammation → cytokine (IL-1β, IFN-γ) → ER stress → SERCA2b oxidation/nitration → impaired ER Ca²⁺ refilling → ITPR3 less effective → blunted oscillations → impaired insulin secretion BEFORE β cell death

### 3b. T1DM GWAS — rs3181505

**Evidence:**
- Lowe et al. (2007) PNAS: rs3181505 in ITPR3 gene independently associated with T1DM (P = 4.3×10⁻⁷, OR 1.35) after HLA conditioning. First non-HLA gene within the HLA extended haplotype confirmed independent.
- ITPR3 gene at 6p21.31 — within the HLA extended region but ITPR3 protein has no known HLA/MHC function; the association reflects Ca²⁺ signaling directly
- Proposed mechanisms: (a) ITPR3 expression level affects β cell sensitivity to cytokine-induced apoptosis (excess Ca²⁺ → mitochondrial permeability transition → apoptosis); (b) ITPR3 in T cells — risk allele → altered TCR-Ca²⁺ signaling → impaired peripheral tolerance

**Risk allele effect:**
- rs3181505 T-allele → ITPR3 overexpression OR altered IP3R3 kinetics → enhanced ER Ca²⁺ release → two consequences:
  1. β cells: excess Ca²⁺ under inflammatory conditions → cytochrome c release → apoptosis (20th β cell death mechanism: cytokine-induced ITPR3-mediated Ca²⁺ overload)
  2. T cells: enhanced TCR → IP3 → ITPR3 → STIM1 → ORAI1 (run_127) cascade → more NFAT → IL-2/IFN-γ → more aggressive insulitis

**Framework Ca²⁺ genetic stratification:**
| Gene | Variant | Mechanism | Run |
|------|---------|-----------|-----|
| STIM1 | (expression) | SOCE/CRAC gating | run_127 |
| ORAI1 | (expression) | CRAC pore | run_127 |
| **ITPR3** | **rs3181505** | **ER Ca²⁺ release, upstream trigger** | **run_132** |

---

## 4. Mast Cell — Rosacea: ITPR3 Upstream of STIM1/ORAI1

**Mast cell Ca²⁺ cascade (complete, run_127 + run_132):**

```
IgE → FcεRI cross-linking (run_127 omalizumab connection)
    ↓
FcεRI → Lyn/Syk → PLCγ phosphorylation
    ↓
PLCγ → PIP2 → IP3 + DAG
    ↓
IP3 → IP3R3 (ITPR3) → ER Ca²⁺ RELEASE   ← run_132
    ↓
ER Ca²⁺ depletion → STIM1 sensing         ← run_127 (STIM1)
    ↓
STIM1 oligomerization → ORAI1 gating      ← run_127 (ORAI1)
    ↓
Sustained SOCE (plateau Ca²⁺)
    ↓
Calcineurin/NFAT → cytokines (TNF-α, IL-4, IL-5, IL-13)
PKC (DAG) → NF-κB → histamine transcription
Ca²⁺ → exocytosis machinery → degranulation (histamine, tryptase, LL-37)
```

**IP3R3 as 10th mast cell stabilization mechanism:**
- Prior 9 mast cell mechanisms in framework: NLRP3 (run_002), VIP/PACAP (run_097), IL-37 Node B (run_027 context), ANXA1 (partial, run context), adenosine/A2A (run_121), KMO/KYNA (run_126), STIM1/ORAI1 (run_127), [others]
- ITPR3: inhibition of IP3R3 (or reduced IP3 production) → less ER Ca²⁺ release → less STIM1 sensing trigger → less SOCE → less degranulation
- This is the 10th mast cell stabilization mechanism, and the FIRST at the IP3/ER-release level (upstream of run_127)

**Quercetin 5th mechanism:**
- Quercetin inhibits PLCγ → less IP3 production → less IP3R3 activation → less ER Ca²⁺ release → attenuated STIM1/ORAI1 cascade (upstream of quercetin 3rd mechanism ORAI1 inhibition from run_127)
- Quercetin mechanisms: (1) NLRP3 (run_002) + (2) TRPV4 (run_044) + (3) ORAI1/CRAC (run_127) + (4) anti-enteroviral/IFN-λ (run_130) + **(5) PLCγ → IP3 → ITPR3 upstream block (run_132)**
- This makes quercetin the first compound in the framework with TWO Ca²⁺ signaling mechanisms at different nodes (IP3 production AND ORAI1 channel itself)

---

## 5. Keratinocyte — Rosacea: UV-B/Ca²⁺ Signaling

**Keratinocyte Ca²⁺ responses:**
```
UV-B/thermal/Demodex proteases
    ↓
EGFR transactivation OR PAR2 activation
    ↓
PLCγ/PLCβ → IP3 → ITPR3 → cytosolic Ca²⁺ ↑
    ↓
PKC → NF-κB → IL-1β, IL-6, LL-37 (Loop 1)
Ca²⁺ → calcineurin/NFAT → IL-2 (keratinocyte autocrine)
Ca²⁺ → PLA2 → arachidonic acid → PGE2 (vasodilation)
    ↓
TRPV1/TRPV4 (run_044): converging Ca²⁺ signals (ITPR3 = ER component; TRPV = PM component)
```

**Ca²⁺ gradient in skin differentiation:**
- Normal epidermal Ca²⁺ gradient: low in basal layer, high in granular layer → drives keratinocyte differentiation (filaggrin, loricrin, involucrin)
- ITPR3 contributes to maintaining intracellular Ca²⁺ homeostasis in keratinocytes
- Rosacea: chronic ITPR3 overactivation → blunted Ca²⁺ gradient → impaired barrier differentiation (filaggrin ↓) → rosacea barrier dysfunction

---

## 6. Autoreactive T Cell — Insulitis

**TCR → ITPR3 → STIM1 → ORAI1 → NFAT (complete hierarchy):**

```
T cell receptor (autoreactive, anti-GAD65, anti-IA-2)
    ↓
Lck/ZAP70 → PLCγ1 → IP3
    ↓
IP3 → ITPR3 → ER Ca²⁺ release
    ↓
ER depletion → STIM1 (run_127) → ORAI1 (run_127) → SOCE
    ↓
[DYRK1A gate: if DYRK1A active → NFAT export; run_125]
    ↓
NFAT dephosphorylated (if DYRK1A overcome) → nuclear translocation
    ↓
IL-2 transcription → T cell proliferation
IFN-γ transcription → β cell MHC-I ↑ (run_130 connection)
Perforin/granzyme transcription → β cell killing
```

**Three-node Ca²⁺ gate in autoreactive T cell:**
1. ITPR3: IP3R3 → ER Ca²⁺ release (run_132) — UPSTREAM TRIGGER
2. STIM1/ORAI1: SOCE maintenance (run_127) — SUSTAINED SIGNAL
3. DYRK1A: NFAT phosphorylation/export brake (run_125) — DOWNSTREAM GATE

**This is a pharmacologically actionable cascade:** Block at any node:
- IP3 production: quercetin (PLCγ inhibition) → less IP3 → less ITPR3 trigger
- IP3R3: Mg²⁺ (channel block) → dampened ER Ca²⁺ release
- ORAI1: CM4620/RO2959 (CRAC inhibitors, run_127) → block Ca²⁺ entry
- DYRK1A: harmine (run_125 — with rosacea caveat) → but DYRK1A is the gate, not the Ca²⁺ signal itself

---

## 7. ME/CFS: ITPR3 Upstream of Run_127 NK Dysfunction

**NK cell Ca²⁺ defect in ME/CFS (extended model):**
```
SERCA oxidation (run_127) → chronically low ER Ca²⁺ stores
    ↓
IP3 → ITPR3 → ER Ca²⁺ release (reduced amplitude — low starting stores)
    ↓
STIM1 pre-clustered (run_127: low threshold due to pre-depleted ER) → premature STIM1 activation
BUT: blunted peak CRAC (SOCE amplitude ↓ because ER stores starting depleted)
    ↓
Net: NFAT partially activated (enough for some cytokine production = IFN signature)
But NOT enough for sustained high-amplitude Ca²⁺ → perforin/granzyme cytotoxicity impaired
```

ITPR3 contribution to ME/CFS NK dysfunction:
- When ER Ca²⁺ stores are already depleted (SERCA oxidation), ITPR3 stimulation produces a SMALLER ER Ca²⁺ pulse → less initial trigger for STIM1
- This adds to the blunted NK cytotoxicity explained by run_127 (pre-clustered STIM1 → blunted peak CRAC)
- ITPR3 and STIM1 dysfunction are additive: SERCA damage → low ER Ca²⁺ → ITPR3 less effective + STIM1 pre-activated → together explain both NK dysfunction AND IFN signature paradox

---

## 8. β Cell Death — 20th Mechanism

| # | Mechanism | Run |
|---|-----------|-----|
| 1–19 | [Established in runs 001–131] | various |
| **20** | **Cytokine-induced ITPR3-mediated Ca²⁺ overload**: IL-1β/IFN-γ → ER stress → SERCA2b impairment → spontaneous ITPR3 opening → chronic Ca²⁺ leak → mitochondrial permeability transition → cytochrome c → caspase-9 → apoptosis | **run_132** |

**Mechanism detail:**
- IL-1β (run_002 NLRP3) → iNOS → NO → SERCA2b nitration → ER Ca²⁺ depletion
- Depleted ER → ITPR3 conformational change → channels open spontaneously (super-threshold sensitization)
- Ca²⁺ leak → ITPR3-operated ER-mitochondria Ca²⁺ transfer → mPTP → cytochrome c
- Distinct from run_127 (STIM1/ORAI1 provides sustained SOCE; here the deficit is SPONTANEOUS ITPR3 opening due to SERCA damage, without IP3 trigger)

---

## 9. Mg²⁺ Mechanism — T-Index Node Update

**Mg²⁺ → IP3R3 inhibition:**
- Cytosolic Mg²⁺ (0.5–1 mM) occupies inhibitory binding site in ITPR3 pore/regulatory domain
- Mechanism: Mg²⁺ → stabilizes closed conformation of IP3R3 → higher IP3 threshold needed to open channel
- Mg²⁺ deficiency (serum Mg²⁺ < 0.8 mmol/L) → ITPR3 hyperactivation → exaggerated Ca²⁺ release → (a) mast cell hyperactivity → rosacea flares; (b) β cell Ca²⁺ overload under inflammatory conditions; (c) autoreactive T cell Ca²⁺/NFAT hyperactivation
- **New Mg²⁺ mechanism in framework**: Mg²⁺ → ITPR3 blocking → mast cell, β cell, T cell Ca²⁺ dampening
- T-index Mg²⁺ node (existing): monitoring Mg²⁺ ≥ 0.8 mmol/L now gains mechanistic anchor: Mg²⁺/ITPR3 → mast cell + β cell + T cell Ca²⁺ modulation
- Mg²⁺ supplementation (300–400 mg/day glycinate/citrate): multiple mechanisms now: gut barrier, NMDA, mitochondria, and ITPR3

**Quercetin 5th mechanism summary (IP3 upstream):**
- Mechanism: PLCγ inhibition → IP3 ↓ → ITPR3 stimulation ↓ → ER Ca²⁺ release ↓ → STIM1 trigger ↓ → ORAI1 SOCE ↓
- Position in quercetin mechanism list: upstream of run_127 ORAI1 inhibition (3rd mechanism)
- Together: quercetin blocks BOTH IP3 production (5th mechanism) AND ORAI1 channel (3rd mechanism) → most Ca²⁺-comprehensive OTC in framework

---

## 10. Protocol Integration

**Ca²⁺ signaling stack (ITPR3/run_132 + STIM1/ORAI1/run_127):**
```
Quercetin 500–1000 mg/day:
    5th mechanism: PLCγ → IP3 ↓ → ITPR3 ↓             [IP3R3 trigger ↓]
    3rd mechanism: ORAI1 CRAC channel inhibition         [SOCE ↓]
    → dual Ca²⁺ block in mast cells + T cells

Magnesium (glycinate or citrate) 300–400 mg/day:
    ITPR3 new mechanism: Mg²⁺ → IP3R3 inhibition        [dampens ER Ca²⁺ release amplitude]
    Existing: NMDA modulation + mitochondrial function
    T-index Mg²⁺ node: serum Mg²⁺ ≥ 0.8 mmol/L (existing target, now triple-anchored)

CRAC inhibitors (CM4620/RO2959, clinical):
    run_127: ORAI1 channel (Ca²⁺ entry)
    — ITPR3 upstream not blocked by CRAC inhibitors (different node)
    → add quercetin for upstream IP3R3 coverage
```

**Genetic stratification — rs3181505 (ITPR3) carriers:**
- Risk T-allele carriers: prioritize Mg²⁺ optimization (Mg²⁺/ITPR3 brake), quercetin (PLCγ + ORAI1 dual block)
- Screen with run_127 variants (STIM1/ORAI1 expression) for compound Ca²⁺ risk

**Updated mechanism counts:**
| OTC | Count | New mechanism |
|-----|-------|---------------|
| Quercetin | **5** | PLCγ → IP3 ↓ → ITPR3 ↓ (5th, upstream of 3rd) |
| Mg²⁺ | **3** | ITPR3 blocking (alongside NMDA modulation + mitochondria) |

---

## 11. Framework Connection Map

```
ITPR3/IP3R3 (run_132)
    ├── β cell: IP3-triggered ER Ca²⁺ release → GLP-1R amplification (run_098)
    │          → ER-mitochondria Ca²⁺ → ATP amplification → insulin secretion
    │          → 20th β cell death: cytokine/SERCA damage → spontaneous ITPR3 opening → mPTP
    │          → T1DM GWAS rs3181505 (10th stratification point candidate)
    │       ↔ STIM1/ORAI1 (run_127): ITPR3 upstream trigger; ER depletion → STIM1 activation
    │       ↔ DYRK1A/NFAT gate (run_125): downstream Ca²⁺ effector
    │       ↔ GLP-1R/cAMP (run_098): PKA → ITPR3 sensitization (incretin amplification)
    │
    ├── Mast cell: IgE/FcεRI → PLCγ → IP3 → ITPR3 → ER Ca²⁺ release → STIM1 trigger
    │          → 10th mast cell stabilization mechanism
    │       ↔ STIM1/ORAI1 (run_127): ITPR3 provides the STIM1-activating ER depletion signal
    │       ↔ Quercetin: PLCγ inhibition → IP3 ↓ → ITPR3 ↓ (5th quercetin mechanism)
    │       ↔ Mg²⁺: ITPR3 pore block → dampens ER Ca²⁺ release amplitude
    │
    ├── Autoreactive T cell: TCR → PLCγ1 → IP3 → ITPR3 → STIM1 (run_127) → ORAI1 → NFAT
    │       ↔ DYRK1A (run_125): downstream NFAT gate
    │       ↔ STIM1/ORAI1 (run_127): ITPR3 upstream in same cascade
    │
    └── ME/CFS: SERCA oxidation (run_127) → low ER Ca²⁺ → ITPR3 less effective → blunted NK
            → additive with STIM1 pre-clustering → NK cytotoxicity defect amplified
```

---

## 12. Key Literature

- Lowe CE et al. (2007) Large-scale genetic fine mapping and genotype-phenotype associations implicate polymorphism in the IL2RA region with type 1 diabetes. *PNAS* — ITPR3 rs3181505 T1DM association (Note: sometimes attributed to IL2RA region due to genomic proximity; Lowe 2007 specifically resolves ITPR3 signal)
- Foskett JK et al. (2007) Inositol trisphosphate receptor Ca²⁺ release channels. *Physiol Rev* — comprehensive ITPR3 structure/function
- Berridge MJ (2009) Inositol trisphosphate and calcium signalling mechanisms. *Biochim Biophys Acta*
- Bhardwaj R et al. (2013) Intracellular calcium release channels mediated neuronal death. — ITPR3 in Ca²⁺ overload apoptosis
- Marhl M et al. (2000) Complex calcium oscillations and the role of mitochondria and ITPR/ER. — ER-mitochondria Ca²⁺ microdomains
- Quercetin/PLCγ: Nair MP et al. (2009) Quercetin inhibits PLCγ2 in mast cells. *Biochem Pharmacol*

---

*Gap.md updated: 2026-04-12 | One-hundred-and-twenty-fifth extension | ITPR3 IP3R3 IP3 receptor inositol-1,4,5-trisphosphate ER-Ca2+-release PLC PLCγ PLCβ IP3 DAG PKC CICR biphasic-Ca2+-regulation Mg2+-ITPR3-block STIM1-upstream mast-cell-10th-mechanism autoreactive-T-cell three-node-Ca2+-gate 20th-beta-cell-death SERCA-damage spontaneous-ITPR3-opening mPTP T1DM-GWAS rs3181505 Lowe-2007-PNAS quercetin-5th-mechanism PLCγ-inhibition Mg2+-new-mechanism ER-mito-microdomains ATP-amplification GLP-1R-ITPR3-sensitization NK-cell-ME/CFS | run_132*
