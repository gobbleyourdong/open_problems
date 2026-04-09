# Model: CVB Cardiac Cascade — From Entry to DCM

## The Mechanistic Pathway (Formalized)

```
ENTRY
│
CVB virion + CAR receptor (intercalated disc) → endocytosis
│
├── CAR is concentrated at INTERCALATED DISCS (cell-cell junctions)
│   → virus enters at the mechanical weak point of the heart
│   → explains why cardiac muscle is uniquely vulnerable
│
ACUTE PHASE (days 1-7)
│
├── CVB genome release → polyprotein translation → 2A + 3C proteases
│
├── 2A protease cleaves:
│   ├── eIF4G → host translation shutdown (all picornavirus)
│   ├── DYSTROPHIN at hinge 3 region (AA 2025-2032)
│   │   └── DGC complex disassembles
│   │       ├── β-dystroglycan dissociates from sarcolemma
│   │       ├── Sarcoglycans lost from membrane
│   │       └── Sarcolemma loses cytoskeletal anchor
│   │           └── EACH CONTRACTION tears membrane at unanchored sites
│   │               └── Ca²⁺ influx → necrosis OR repair if minor
│   └── SERF2 (small EDRK-rich factor 2) → unclear functional consequence
│
├── 3C protease cleaves:
│   ├── SNAP29 → blocks autophagosome-lysosome fusion → autophagy hijacked
│   ├── TFIIIC → disrupts Pol III transcription
│   └── Multiple host factors → protein synthesis disruption
│
├── Viral replication → 10⁸ copies per gram of tissue at peak
│
├── IMMUNE RESPONSE (beneficial)
│   ├── Type I IFN (IFN-α/β) → antiviral state in neighboring cells
│   ├── NK cells → kill infected cardiomyocytes (missing-self recognition)
│   ├── CD8+ CTLs → kill infected cells (MHC-I restricted)
│   └── Macrophages → phagocytosis + cytokine production
│
├── IMMUNE RESPONSE (pathological)
│   ├── Molecular mimicry: cardiac myosin heavy chain shares epitopes with CVB VP1
│   │   └── Anti-cardiac myosin antibodies → attack UNINFECTED cardiomyocytes
│   ├── Bystander activation: IFN-γ activates autoreactive T cells
│   └── Epitope spreading: initial viral response → release of cardiac antigens → new autoimmune targets
│
DECISION POINT (weeks 2-4)
│
├── PATH A: CLEARANCE (60-70% of cases)
│   ├── Strong IFN response + NK + CTL → virus eliminated
│   ├── No TD mutant establishment
│   ├── Autoimmune response subsides (Tregs restore tolerance)
│   ├── Minor fibrosis at sites of cardiomyocyte loss
│   └── RECOVERY → normal cardiac function
│
├── PATH B: PERSISTENCE → CHRONIC MYOCARDITIS → DCM (30-40%)
│   ├── CVB 5' terminal deletion → TD mutant formation
│   ├── TD mutants replicate 100,000x slower
│   ├── Below immune detection threshold
│   ├── BUT still produce 2A protease (at low levels)
│   └── CHRONIC PHASE begins
│
CHRONIC PHASE (months to years)
│
├── TD mutant 2A production → continuous dystrophin cleavage
│   ├── Rate: slow but nonzero
│   ├── Each cleavage event weakens one DGC complex
│   ├── Over time: cumulative sarcolemma instability
│   └── Rate equation:
│       d(dystrophin_intact)/dt = -k_cleave × [2A] × [dystrophin] + k_synth
│       where k_cleave × [2A] > k_synth → net dystrophin loss
│
├── Autoimmune component persists
│   ├── Anti-cardiac myosin antibodies (if generated) persist for years
│   ├── Complement fixation on cardiomyocyte surface → membrane damage
│   └── Adds to mechanical damage from dystrophin loss
│
├── Cardiomyocyte death
│   ├── Source 1: sarcolemma tears during contraction (mechanical)
│   ├── Source 2: autoimmune attack (immunological)
│   ├── Source 3: mitochondrial dysfunction from chronic stress
│   └── Replacement: fibrosis (collagen deposition by cardiac fibroblasts)
│       NOT new cardiomyocytes (adult heart regeneration ≈ 1%/year)
│
├── Fibrosis accumulates
│   ├── TGF-β → fibroblast → myofibroblast → collagen I/III
│   ├── Fibrosis is STIFF → reduces compliance
│   ├── Fibrosis is ELECTRICALLY INERT → conduction abnormalities
│   └── Fibrosis is IRREVERSIBLE (without anti-fibrotic intervention)
│
ENDSTAGE: DILATED CARDIOMYOPATHY
│
├── Chamber dilation (volume overload due to reduced contractility)
├── Reduced LVEF (<40%)
├── Heart failure symptoms (dyspnea, edema, fatigue)
├── Arrhythmia risk (fibrosis creates re-entrant circuits)
└── Transplant or death
```

## Intervention Points (Mapped to T1DM Arsenal)

| Stage | Intervention | Mechanism | From T1DM attempt |
|-------|-------------|-----------|-------------------|
| Entry | sCAR decoy | Block CAR receptor binding | Novel (not in T1DM) |
| Acute replication | Fluoxetine | 2C ATPase block | 062 (bullet factory) |
| Acute replication | Itraconazole | OSBP/PI4KB → RO collapse | 062 (bullet factory) |
| 2A protease activity | No direct inhibitor exists | **GAP** — 2A protease inhibitor would stop dystrophin cleavage directly | **OPEN TARGET** |
| TD mutant persistence | FMD/autophagy | Clear infected cells | 062 (bullet factory) |
| Autoimmune component | Vitamin D + butyrate | Treg induction | 062 (arm enforcers) |
| Autoimmune component | WHM → IL-10 | Macrophage deactivation | 062 (disarm criminals) |
| Inflammation | BHB | NLRP3 suppression | 062 (unload gun) |
| Inflammation | Colchicine | NLRP3 microtubule block | 062 (jam trigger) |
| Fibrosis | Pirfenidone/Nintedanib | TGF-β pathway | Novel (not in T1DM) |
| Cardiac function | SGLT2i (empagliflozin) | HF therapy + autophagy | Novel combination |

## The Open Target: 2A Protease Inhibitor

In T1DM, stopping 2A protease is achieved indirectly (kill the virus → no more 2A).
In myocarditis/DCM, a DIRECT 2A protease inhibitor would:
- Immediately stop dystrophin cleavage
- Allow dystrophin resynthesis and DGC reassembly
- Protect cardiomyocytes while antiviral therapy clears the virus

**This is a drug development target.** 2A is a cysteine protease. Structure is known (PDB: multiple entries). Virtual screening for 2A inhibitors is feasible.

## Key Measurements

| Biomarker | What it measures | Stage detected |
|-----------|-----------------|---------------|
| Troponin-I | Acute cardiomyocyte necrosis | Acute phase |
| BNP/NT-proBNP | Ventricular wall stress | Chronic/DCM |
| Cardiac MRI (LGE) | Fibrosis location and extent | Chronic |
| Cardiac MRI (T2 mapping) | Active inflammation/edema | Acute/subacute |
| LVEF (echo) | Systolic function | Any stage |
| Enteroviral RNA (biopsy) | Viral persistence | Any stage (invasive) |
| Anti-cardiac myosin Ab | Autoimmune component | Subacute/chronic |
| Dystrophin fragments (?) | 2A protease activity | **Not yet available** |
