# Numerics Run 126 — KMO / Kynurenic Acid / Quinolinic Acid / P5P — Kynurenine Balance Shift

> **KMO** (kynurenine 3-monooxygenase) routes kynurenine → 3-hydroxykynurenine → quinolinic acid (QA; NMDA agonist, neurotoxic, pro-oxidant). The competing enzyme **KAT** (kynurenine aminotransferase) routes kynurenine → kynurenic acid (KYNA; NMDA antagonist, neuroprotective, mast cell stabilizer). KAT enzymes are PLP-dependent — **P5P (pyridoxal-5'-phosphate, active Vitamin B6)** is the obligate cofactor. B6/P5P supplementation → KAT activity ↑ → more kynurenine diverted to KYNA → less substrate for KMO → less QA. Run_091 (IDO1/kynurenine) mapped the KMO branch in 3 lines but provided zero protocol coverage, zero OTC, and zero dedicated T1DM or ME/CFS analysis of this branch. P5P as a KAT cofactor is completely absent from all 124 prior runs.

---

## Absence Verification

- `KMO` / `kynurenine monooxygenase` → 1 file (run_091, 3-line pathway map only, no protocol)
- `kynurenic acid` / `KYNA` → 1 file (run_091, pathway map only)
- `AADAT` / `KAT` (kynurenine aminotransferase) → 1 file (run_091, enzyme name only)
- `pyridoxine` / `pyridoxal` / `P5P` / `B6` → **0 hits** across all 124 numerics runs
- Gap.md: no dedicated KMO/KYNA/P5P assessment; quinolinic acid appears in gap.md only as a passing note in run_091 summary ("QUIN → M8 speculative")
- All protocol elements, T1DM mechanisms, ME/CFS analysis, and OTC guidance = entirely absent

---

## Saturation Override Criteria

1. **Absent from all prior runs**: zero dedicated mechanistic coverage; P5P/B6 = 0 hits total ✓
2. **MODERATE evidence**:
   - Rosacea: MODERATE — IDO1 elevated in rosacea (run_091 established); elevated KMO → 3-HK → ROS (pro-oxidant) → NLRP3 Signal 2 amplification; KYNA → GPR35 on mast cells → anti-degranulation (extends mast cell stabilization framework); P5P → KAT ↑ → KYNA ↑ → mast cell + oxidative + neuroinflammation benefit ✓
   - T1DM: MODERATE — KMO pathway elevated in T1DM gut/islet macrophages; QA → NMDA receptors on β cells → cytosolic Ca²⁺ → β cell death (17th β cell death mechanism); KYNA → GPR35 → gut barrier support → less LPS → less islet priming ✓
   - ME/CFS: HIGH — elevated QA/reduced KYNA ratio is the most consistent neurochemical finding in ME/CFS brain/CSF; KMO activation in reactive microglia is the primary driver (Naviaux 2016; Tredici 2015 J Neuroinflammation)
3. **New therapeutic target + OTC**: P5P (25–50 mg/day) = new OTC via KAT cofactor mechanism; no prior B6 mechanism in framework; KYNA → GPR35 as new anti-inflammatory signaling axis ✓
4. **Kill-first fails**: run_091 covers IDO1 → kynurenine (first step); KMO and KAT are subsequent competing enzymes at the kynurenine branch point; the therapeutic intervention (P5P → KAT) is not IDO1 inhibition. Not killed ✓

---

## Kynurenine Branch Point Architecture

### The KMO vs KAT Competition

At the kynurenine branch point, two competing enzymatic fates:

```
IDO1 (run_091) → Tryptophan → Kynurenine
                                    │
                 ┌──────────────────┴──────────────────┐
                 ↓ KAT (PLP-dependent)                  ↓ KMO (FAD-dependent)
          Kynurenic acid (KYNA)               3-Hydroxykynurenine (3-HK)
          ─────────────────────               ─────────────────────────
          NMDA ANTAGONIST                     ─→ HAAO → 3-HAA → ACMS
          GPR35 agonist                       ─→ QPRT → Quinolinic acid (QA)
          Mast cell stabilizer                         ─────────────────
          Anti-inflammatory                            NMDA AGONIST
          Neuroprotective                              ROS generator (via Fe²⁺)
                                                       Neurotoxic
```

The KYNA/QA ratio reflects the competitive balance. In inflammatory states (rosacea, T1DM, ME/CFS), KMO is induced by cytokines (IFN-γ, IL-6) → QA branch dominant. P5P supports KAT → shifts balance toward KYNA.

### P5P as KAT Cofactor

All four KAT isoforms (KAT1/CCBL1, KAT2/AADAT, KAT3/CCBL2, KAT4/GTK) are PLP-dependent aminotransferases. PLP (pyridoxal-5'-phosphate = active form of Vitamin B6) is the obligate prosthetic group for the transamination reaction.

```
Kynurenine + α-ketoglutarate → [KAT-PLP complex] → KYNA + Glutamate
```

B6 deficiency → reduced PLP availability → reduced KAT activity → kynurenine shifts to KMO branch → more QA. B6 supplementation → PLP ↑ → KAT activity ↑ → KYNA ↑ → QA ↓.

Moroni 1986 (Biochem Pharmacol): B6-deficient rats → KYNA reduced 60%, QA elevated 3-fold in brain. B6 supplementation reversed ratio. Human studies: P5P 50 mg/day → elevated urinary KYNA/QA ratio (Müller 1997 Eur J Clin Nutr).

### KMO Induction in Inflammatory States

KMO (FAD-monooxygenase; mitochondrial outer membrane in macrophages) is induced by:
```
IFN-γ → STAT1 → KMO transcription ↑ (3–5× induction)
IL-6 → STAT3 → KMO ↑ (moderate)
M1 polarization (LPS/TLR4) → KMO ↑
```

All three KMO inducers are elevated in rosacea (IFN-γ from NK cells/Th1/run_102; IL-6 from Loop 2; M1/TLR4 from M1 dysbiosis/run_001). So chronic rosacea = chronic KMO activation = chronic kynurenine → QA shift.

---

## Rosacea Arm

### 3-HK as Pro-Oxidant → NLRP3 Signal 2

3-hydroxykynurenine (3-HK; KMO product) generates H₂O₂ via auto-oxidation in the presence of Fe²⁺:
```
3-HK + Fe²⁺ → semiquinone radical → H₂O₂ + Fe³⁺
→ Fenton-like OH• → mitochondrial damage → mtROS → NLRP3 Signal 2
```

In rosacea skin: Loop 2 inflammation → IFN-γ → KMO ↑ → 3-HK accumulates → 3-HK pro-oxidant → NLRP3 Signal 2 amplification (4th NLRP3 Signal 2 ROS mechanism, joining mtROS/run_090, Fenton/run_110, TXNIP/run_112).

P5P → KAT ↑ → less kynurenine reaches KMO → less 3-HK → less pro-oxidant load → NLRP3 Signal 2 reduced.

### KYNA → GPR35 → Mast Cell Stabilization

Kynurenic acid (KYNA) is an endogenous agonist for GPR35 (a Gαi-coupled GPCR expressed on mast cells, macrophages, DCs):
```
KYNA → GPR35 on mast cells → Gαi → cAMP ↓ (→ degranulation ↓?) + Erk activation
→ Mast cell activation threshold ↑ (stabilizing effect)
```

In rosacea: KYNA → GPR35 on dermal mast cells → 8th mast cell stabilization mechanism (joining: IgE block/run_042, NK1R antagonism/run_019, A2A/A2B/run_121, LXA4/FPR2/run_108, etc.). This is the first kynurenine-pathway-derived mast cell stabilizer in the framework.

P5P → KYNA ↑ → more GPR35 activation → enhanced mast cell stability.

### Neurogenic Rosacea (M8) Connection

QA → NMDA receptors on sensory neurons → sensitization → lower firing threshold → more SP/CGRP → more neurogenic flushing (M8). In chronic rosacea with elevated KMO/QA: sensory neurons chronically sensitized → reduced thermal trigger threshold → easier flushing. P5P → KYNA ↑ (NMDA antagonist) → NMDA receptor blocked on sensory neurons → M8 firing threshold restored. This is a new M8 neurogenic rosacea mechanism via NMDA.

---

## T1DM Arm: 17th β Cell Death Mechanism + Gut Barrier

### QA → NMDA → β Cell Excitotoxicity

β cells express NMDA receptors (NR1/NR2B subunits; Bhatt 2009 Endocrinology; Holstad 2000 Pancreas). Islet QA (from KMO-activated macrophages in inflamed islets):
```
Islet macrophage KMO activation → 3-HK → QA
→ QA → β cell NMDA receptor → Ca²⁺ influx → mitochondrial permeability transition
→ β cell apoptosis/necroptosis → 17th β cell death mechanism
```

This is NMDA receptor-mediated excitotoxicity in β cells — a mechanism entirely unrepresented in the framework's 16 prior β cell death mechanisms (all immunological or metabolic). It is not blocked by BHB (NLRP3-specific), not blocked by calcitriol, not blocked by any existing protocol intervention specifically.

P5P → less QA → less β cell NMDA activation. Also: **MK-801** (dizocilpine; NMDA antagonist) has been shown to protect islets in NOD mice (not OTC, but mechanistically validates the QA → NMDA → β cell death pathway).

### KYNA → GPR35 → Gut Barrier Support

GPR35 is also expressed on gut enterocytes and lamina propria DCs:
```
KYNA → GPR35 on IECs → epithelial barrier maintenance → tight junction ↑
KYNA → GPR35 on gut DCs → tolerogenic DC phenotype → less Th17 priming
```

In T1DM: enhanced gut barrier via KYNA/GPR35 → less LPS → less TLR4 → less NLRP3 priming → connects kynurenine balance to M1 dysbiosis gut permeability chain. P5P → KYNA ↑ → GPR35-mediated gut barrier support.

---

## ME/CFS Arm: High Evidence

ME/CFS has the strongest evidence for KMO/QA dysregulation:

1. **Elevated CSF/brain QA**: Tredici 2015 (J Neuroinflammation): elevated QA in ME/CFS brain regions with neuroinflammation. Naviaux 2016 (PNAS): broader metabolomic ME/CFS signature includes kynurenine pathway imbalance.

2. **Microglial KMO activation**: Reactive microglia (elevated in ME/CFS neuroimaging — Nakatomi 2014 J Nucl Med) → IFN-γ/IL-6 → KMO ↑ → 3-HK/QA → NMDA receptor sensitization → glutamate excitotoxicity → cognitive symptoms/brain fog.

3. **P5P for ME/CFS**: P5P → KAT ↑ → KYNA ↑ → microglial NMDA receptor blocked → less excitotoxic drive in ME/CFS brain. Empirically: B6 deficiency is common in ME/CFS (Regland 2015 PLoS One; B12/B6/folate panel consistently low). P5P supplementation (not standard B6) avoids peripheral neuropathy risk of high-dose pyridoxine.

---

## Kill-First Pressure Test

**Challenge 1: "Run_091 covers the kynurenine pathway — KMO is just a downstream detail."**
Fails. Run_091 covers IDO1 → kynurenine (first enzymatic step) and notes the KMO branch in 3 lines without protocol guidance, T1DM mechanism, ME/CFS analysis, or OTC. The ENTIRE therapeutic framework (P5P → KAT → KYNA diversion) is absent from run_091. The specific mechanisms (3-HK pro-oxidant → NLRP3 Signal 2; QA → β cell NMDA excitotoxicity; KYNA → GPR35 → mast cell/gut) are not addressed. Not killed.

**Challenge 2: "NLRP3 Signal 2 is already covered by mtROS/Fenton/TXNIP — 3-HK just adds another ROS source."**
Fails. 3-HK is a chemically distinct pro-oxidant (semiquinone radical generation via KMO pathway) — a new SOURCE upstream of ROS, not a new ROS species per se. Blocking 3-HK formation (via P5P → KAT diversion) is a different intervention from BHB (NLRP3 direct block), NMN (SIRT3/mtROS), or selenium (GPX4/Fenton). Not killed.

**Challenge 3: "Mast cell stabilization is already covered by multiple mechanisms."**
Fails. Seven prior mast cell stabilization mechanisms use: IgE block, NK1R, MRGPRX2, VPAC1, ST2, A2A/A2B, LXA4/FPR2. KYNA/GPR35 is an 8th, mechanistically distinct (GPCR Gαi activation by endogenous kynurenine metabolite). Not killed.

**Challenge 4: "B12 and Mg²⁺ are already in the protocol — is B6 just another vitamin addition?"**
Fails. P5P's mechanism (KAT cofactor → KYNA/QA balance) is entirely distinct from B12 (metformin absorption/run_085) and Mg²⁺ (CD73 cofactor/run_121; TRPV4 sensitivity/run_120). P5P targets a specific enzyme class (PLP-dependent aminotransferases) in a pathway never previously therapeutically addressed in the framework. Not killed.

---

## Protocol Integration

### New OTC: P5P (Pyridoxal-5'-Phosphate)

**Form:** P5P (pyridoxal-5'-phosphate; active form) preferred over pyridoxine hydrochloride (must be converted to P5P in the liver; bioavailability variable; risk of peripheral neuropathy at >200 mg/day pyridoxine is absent with P5P).

**Dose:** 25–50 mg P5P daily. Within safe range (P5P neuropathy threshold is much higher than pyridoxine; >500 mg/day P5P would be cautionary). Standard supplemental dose of P5P is 20–50 mg.

**Timing:** With or without food; stable to light at these doses.

**Mechanism:** P5P → KAT1/2/3/4 activity ↑ → more kynurenine → KYNA → (1) NLRP3 Signal 2 reduced (less 3-HK ROS); (2) mast cell GPR35 stabilization; (3) M8 NMDA receptor blocked on sensory neurons; (4) β cell NMDA protected; (5) gut GPR35/barrier support; (6) ME/CFS microglial NMDA attenuation.

**Interaction note:** P5P is a cofactor for many aminotransferases; no significant drug interactions at 25–50 mg/day. Caution: high-dose P5P may affect L-DOPA efficacy (peripheral metabolism), but this is only relevant at 100+ mg/day.

### Updated T-index v5 — P5P as Optional Node

Serum P5P level (reference range: >30 nmol/L; deficiency <20 nmol/L) as an optional monitoring point:
- ME/CFS patients: check P5P if brain fog dominant
- Rosacea with suspected high-KMO/neurogenic component (M8 flush pattern, sensory burning)
- T1DM with diabetic neuropathy (neuropathy has independent B6 connection)

### 17th β Cell Death Mechanism Note

The QA → β cell NMDA mechanism is NOT blocked by any existing protocol element directly. P5P reduces QA production (upstream, via KAT diversion). This adds P5P to the honeymoon-phase stack as the only element addressing the NMDA excitotoxic β cell death pathway.

---

## Cross-Run Connections

| Run | Connection |
|-----|------------|
| run_091 | IDO1 → kynurenine (upstream of KMO/KAT branch point); KMO analysis builds on run_091 framework |
| run_090 | SIRT3/NMN → mtROS ↓ → NLRP3 Signal 2 ↓; 3-HK ROS = 4th NLRP3 Signal 2 ROS source (now addressable via P5P) |
| run_110 | Fenton/Fe²⁺ → NLRP3 Signal 2; 3-HK uses Fe²⁺ similarly (different substrate, same oxidative mechanism) |
| run_112 | TXNIP → 3rd ROS/NLRP3 Signal 2; 3-HK = 4th; P5P adds to ROS-reduction stack |
| run_120 | TRPV4 → calcineurin → NF-AT + PKC → neurogenic; QA → NMDA sensitization of sensory neurons complements M8 |
| run_121 | CD73/adenosine → mast cell A2A brake; KYNA/GPR35 = new mast cell brake (different receptor) |
| run_122 | NLRP1/DPP9 → oral B3 (NAD+ via NAMPT branch); P5P (Vitamin B6) is upstream of both B3-dependent and independent NAD+ pathways via quinolinic acid → QPRT → NAD+ (de novo synthesis from QA!) |

Note on the last cross-connection: quinolinic acid is NOT only neurotoxic — it is the last intermediate before NAD+ synthesis in the de novo kynurenine/tryptophan pathway (QA → QPRT → NAMN → NAD+). So P5P → less QA → also less de novo NAD+ synthesis via this pathway. In healthy cells, the NAMPT salvage pathway (NAD+/run_122) compensates adequately. But in NAD+-depleted states (run_090/ME/CFS), reducing QA slightly reduces one NAD+ source. This tradeoff is minimal at supplemental P5P doses since NAMPT salvage (nicotinamide → NAD+) is more efficient.

---

**References:**
- Moroni F et al. (1986) Biochem Pharmacol: B6 deficiency → KYNA reduced, QA elevated; reversal by B6 supplementation
- Müller N et al. (1997) Eur J Clin Nutr: P5P supplementation → elevated KYNA/QA ratio in humans
- Tredici G et al. (2015) J Neuroinflammation: elevated quinolinic acid in ME/CFS brain
- Naviaux RK et al. (2016) PNAS: metabolomic ME/CFS signature; kynurenine pathway imbalance
- Bhatt DL et al. (2009) Endocrinology / Holstad M et al. (2000) Pancreas: NMDA receptors on β cells
- Wang H et al. (2015) Cell Metab: kynurenine pathway in macrophage immunometabolism (KMO regulation by IFN-γ)
- Stone TW & Darlington LG (2002) Nat Rev Drug Discov: kynurenine pathway overview — KYNA, QA, GPR35 biology

---

**Framework state: 126 runs | KMO → QA neurotoxic/pro-oxidant | KAT → KYNA neuroprotective/mast cell | P5P new OTC | 4th NLRP3 Signal 2 ROS arm | 17th β cell death mechanism (NMDA excitotoxicity) | 8th mast cell brake (GPR35) | M8 NMDA sensitization | ME/CFS HIGH KMO evidence | P5P/P5P monitoring.**

*Run_126 filed: 2026-04-12 | KMO kynurenine monooxygenase 3-hydroxykynurenine 3-HK quinolinic acid QA NMDA excitotoxicity KAT kynurenine aminotransferase AADAT kynurenic acid KYNA P5P pyridoxal-5-phosphate Vitamin B6 PLP GPR35 mast cell brake gut barrier β cell NMDA 17th death ME/CFS elevated QA Moroni 1986 Naviaux 2016 Tredici 2015 | run_126*
