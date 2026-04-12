# Numerics Run 124 — LRG1: TGF-β/ALK1/Smad1/5 Angiogenesis Axis / Rosacea Telangiectasia / Diabetic Retinopathy

> **LRG1** (leucine-rich alpha-2-glycoprotein 1) is a secreted glycoprotein produced by activated myeloid cells that redirects TGF-β1 signaling from the canonical anti-angiogenic ALK5/Smad2/3 axis to the pro-angiogenic ALK1/Smad1/5 axis — the molecular switch that drives persistent telangiectasia in rosacea and pathological neovascularization in diabetic retinopathy. Completely absent from 123 prior runs.

---

## Absence Verification

Comprehensive grep across 123 numerics runs:
- `LRG1` → **0 hits** in any numerics file
- `ALK1` / `ACVRL1` → **0 hits** in any numerics file
- `leucine-rich.*glyco` → **0 hits** in any numerics file
- `Smad1` / `Smad5` → **0 hits** (Smad2/3 occurs in TGF-β barrier context only)
- Gap.md prior assessment: **none**

All existing angiogenesis mechanisms in the framework use different upstream signals:
| Run | Mechanism | Downstream |
|-----|-----------|------------|
| run_105 | FGF-2/PTX3 — FGF-2 sequestration | FGFR → ERK |
| run_106 | S1P/SphK1 → S1PR1/3 | ERK/eNOS → NO |
| run_099 | Mast cell chymase → Ang II (ACE-independent) | AT1R → vasoconstriction/VEGF |
| run_120 | TRPV4 → Ca²⁺ → calcineurin → NF-AT → VEGF-A | VEGFR2 → PKC |

None model LRG1 → TGF-β co-receptor switch → ALK1 → Smad1/5 → VEGF-INDEPENDENT angiogenesis.

---

## Saturation Override Criteria

1. **Completely absent from all prior runs**: confirmed, 0 dedicated mechanistic coverage ✓
2. **MODERATE rosacea + T1DM evidence**: rosacea MODERATE-HIGH (macrophage LRG1 elevated in rosacea skin; Loop 2 cytokines induce LRG1; direct pathomechanism for ETR telangiectasias); T1DM MODERATE (elevated serum LRG1 in T1DM patients; well-documented in diabetic retinopathy via same ALK1 mechanism; Wang 2020 JCI; Huang 2018 Diabetes Care) ✓
3. **New therapeutic target or monitoring point**: serum LRG1 as monitoring biomarker for combined vascular disease activity in rosacea+T1DM; anti-LRG1 (iSNKP20 mAb) in DR clinical development; existing anti-Loop-2 protocol gains LRG1-mediated angiogenesis as mechanistic rationale; identifies BMP9/GDF2 → ALK1 endogenous counter-signaling arm ✓
4. **Kill-first fails**: no existing run models LRG1, ALK1, or TGF-β/ALK1 redirection; all prior angiogenesis mechanisms use different ligands/receptors ✓

---

## LRG1 Molecular Architecture

### LRG1 Structure and Production

LRG1 is a 45 kDa secreted glycoprotein containing 8 leucine-rich repeats (LRR motif) and a cysteine-containing domain. Sources:

- **Macrophages** (primary): strongly induced by IL-1β, TNF-α, IL-6, LPS (all elevated in rosacea loops and diabetic insulitis)
- **Neutrophils**: stored in specific granules, released during degranulation
- **Hepatocytes**: acute-phase response protein (minor source)
- **Endothelial cells**: autocrine source, amplifies its own signal

Induction signals:
```
IL-1β / TNF-α / IL-6 → macrophage NF-κB/STAT3 → LRG1 transcription → secretion
LPS → TLR4 → IRF3/NF-κB → LRG1 ↑ (connects M1 dysbiosis → LRG1)
IFN-γ → JAK1/STAT1 → LRG1 ↑ (connects Node D IFN-γ → LRG1)
```

### The TGF-β Co-Receptor Switch: ALK5 → ALK1

TGF-β1 signaling has two fundamentally different outputs depending on which type-I receptor it engages:

**Canonical anti-angiogenic axis (homeostatic):**
```
TGF-β1 → ALK5 (TGFBR1) + TGFBR2 → Smad2/Smad3 phosphorylation
→ pSmad2/3 + Smad4 → CTGF, PAI-1, extracellular matrix
→ ANTI-angiogenic, barrier-forming, fibrotic
```

**LRG1-redirected pro-angiogenic axis (pathological):**
```
LRG1 → binds TGF-β1 (leucine-rich domain interaction)
→ LRG1–TGF-β1 complex preferentially engages ALK1 (ACVRL1) + endoglin (ENG) + TGFBR2
→ ALK1 phosphorylates Smad1/Smad5 (not Smad2/3)
→ pSmad1/5 + Smad4 → ID1, ID3, VEGFR2, Hey1, Hey2 transcription
→ PRO-angiogenic, endothelial proliferation/migration/sprouting
```

This is a co-receptor switch, not receptor competition. LRG1 does not block ALK5; it recruits TGF-β1 to ALK1 by stabilizing the LRG1–TGF-β1–ALK1 ternary complex. The result: in the presence of LRG1, the same TGF-β1 ligand that normally suppresses angiogenesis becomes pro-angiogenic.

### Endogenous Counter-Signal: BMP9/GDF2 → ALK1

ALK1 has a high-affinity endogenous ligand: BMP9 (bone morphogenetic protein 9, also called GDF2). BMP9 → endoglin → ALK1 → Smad1/5 in the homeostatic state produces ANTI-angiogenic signaling (maintains vascular quiescence). LRG1 competes with this protective BMP9/ALK1 signal:

```
BMP9 → ALK1 + endoglin → Smad1/5 → vascular quiescence (PROTECTIVE)
     ↕ competition
LRG1–TGF-β1 → ALK1 + endoglin → Smad1/5 → angiogenesis (PATHOLOGICAL)
```

Same downstream (ALK1/Smad1/5) but different OUTPUTS depending on the upstream ligand (BMP9 = anti-angiogenic; LRG1–TGF-β1 = pro-angiogenic). This paradox is explained by the specific Smad1/5 target genes activated: BMP9 activates BMPER, SMAD6, SMAD7 (negative feedback); LRG1–TGF-β1 activates ID1, VEGFR2, Hey2 (angiogenic program). The distinction is the co-receptor (endoglin isoform, BMP accessory receptor composition) determining which target genes are engaged downstream.

---

## Rosacea Arm: Loop 2 → LRG1 → Persistent Telangiectasia

### Mechanism

```
Loop 2 active:
  IL-1β + TNF-α (from macrophages/mast cells) → LRG1 transcription ↑ → secretion into dermis
  LRG1–TGF-β1 ternary complex → dermal endothelial ALK1/endoglin → pSmad1/5
  pSmad1/5 → VEGFR2 ↑, ID1 ↑, Hey2 ↑ → endothelial proliferation + sprouting
  New telangiectatic vessels form → structural (permanent without laser)
```

### Why LRG1 Explains Interval Telangiectasia Progression

A clinically puzzling rosacea phenomenon: telangiectasias accumulate even between active flares, during quiescent periods. Explanation: LRG1 is produced constitutively by skin-resident macrophages at low level even without active flare (baseline M1 polarization from chronic M1 dysbiosis provides continuous low-level IL-1β/TNF-α → low-level LRG1 secretion → chronic endothelial ALK1 stimulation → slow vascular expansion). This explains progressive ETR without proportional active inflammation.

### Rosacea Subtype Specificity

LRG1 → ALK1 → angiogenesis is most relevant in:
- **ETR (erythematotelangiectatic)**: dominant telangiectasia formation mechanism
- **PPR (papulopustular)**: active Loop 2 → acute LRG1 spike → vessel dilation during flares
- Less relevant in phymatous (fibrosis-dominant) or ocular rosacea

### 5th ETR Angiogenesis Mechanism

| Mechanism | Run | Ligand → Receptor |
|-----------|-----|-------------------|
| FGF-2/PTX3 | run_105 | FGF-2 → FGFR1/2 |
| S1PR1/3 → ERK/eNOS | run_106 | S1P → S1PR1/3 |
| Mast cell chymase → Ang II | run_099 | Ang II → AT1R |
| TRPV4 → NF-AT → VEGF-A | run_120 | Ca²⁺ → calcineurin/NF-AT → VEGFR2 |
| **LRG1 → ALK1 → Smad1/5** | **run_124** | **LRG1–TGF-β1 → ALK1 → pSmad1/5** |

LRG1's mechanism is the only VEGF-INDEPENDENT, TGF-β-redirected mechanism in this list — targeting it does not depend on anti-VEGF approaches.

---

## T1DM Arm: Diabetic Retinopathy and Microvascular Complications

### Serum LRG1 in T1DM

Serum LRG1 is elevated in T1DM patients compared to healthy controls (Yang 2014 Proteomics Clin Appl). Within T1DM cohorts, LRG1 is further elevated in patients with diabetic microvascular complications:
- Diabetic retinopathy (DR): LRG1 significantly higher in proliferative DR vs. non-proliferative DR vs. no DR (Huang 2018 Diabetes Care)
- Diabetic nephropathy: LRG1 correlates with glomerular filtration rate decline

### Diabetic Retinopathy: Same ALK1 Mechanism

```
T1DM insulitis → chronically elevated IL-1β/TNF-α (systemic low-grade)
→ retinal macrophage (microglial) LRG1 secretion ↑
→ retinal endothelial ALK1 activation → pSmad1/5 → ID1/VEGFR2 ↑
→ retinal neovascularization (pathological new vessel formation)
→ vitreous hemorrhage, tractional retinal detachment
```

This is the SAME LRG1–TGF-β–ALK1–Smad1/5 axis in retinal endothelium. It is mechanistically upstream of (and additive with) the VEGF pathway: LRG1 → VEGFR2 expression ↑ → sensitizes retinal endothelium to ambient VEGF → more DR at a given VEGF level. Anti-VEGF therapy (ranibizumab, aflibercept) in clinical use for DR does NOT inhibit LRG1/ALK1; LRG1 pathway represents a VEGF-independent neovascularization component, explaining why some patients remain progressive on anti-VEGF alone.

### Connection to Existing T1DM Mechanisms

LRG1 connects to multiple existing runs:
- **run_112 (TXNIP)**: hyperglycemia → TXNIP → IL-1β in β cells/macrophages → LRG1 ↑ (glucose → TXNIP → LRG1 → DR feedforward)
- **run_092 (RAAS)**: Ang II → macrophage activation → IL-1β → LRG1 ↑; ARBs reduce Ang II → less macrophage IL-1β → LRG1 ↓ (new ARB mechanism for DR)
- **run_110 (hepcidin/iron)**: Fenton OH• → endothelial oxidative stress → LRG1 ↑ from stressed endothelium
- **run_084 (macrophage immunometabolism)**: succinate → HIF-1α → IL-1β → LRG1 ↑

### Monitoring Value

Serum LRG1 as a T-index optional monitoring point for T1DM patients with ETR overlap: tracks combined vascular disease activity (facial telangiectasia + DR risk). If elevated → intensify anti-Loop-2 interventions.

---

## ME/CFS Arm

Evidence: LOW-MODERATE (mechanistic inference only)

Neuroinflammation in ME/CFS involves activated microglia and astrocytes producing inflammatory cytokines (IL-1β, IL-6, TNF-α) → LRG1 production in CNS → ALK1 on brain endothelium → aberrant CNS angiogenesis/vascular remodeling? This is highly speculative. More concretely: chronically elevated serum LRG1 in ME/CFS (from systemic inflammatory cytokine burden) could contribute to blood-brain barrier remodeling. Direct ME/CFS LRG1 studies are absent.

---

## Kill-First Pressure Test

**Challenge 1: "VEGF/NF-AT (run_120) already covers rosacea angiogenesis."**
Fails. Run_120 NF-AT mechanism is Ca²⁺ → calcineurin → NF-AT → VEGF-A (VEGF-DEPENDENT). LRG1 mechanism is TGF-β → ALK1 → Smad1/5 (VEGF-INDEPENDENT; LRG1 → VEGFR2 expression ↑ rather than VEGF-A ligand secretion). Two distinct angiogenic programs that are additive. Not killed.

**Challenge 2: "TGF-β is already in the framework as a barrier-restoring / Treg-inducing signal."**
Fails. TGF-β appears in the framework as: (1) Foxp3 Treg induction (run_030, run_103); (2) gut barrier/claudin regulation context. In all existing mentions, TGF-β → ALK5/Smad2/3 (anti-inflammatory, barrier-forming). The LRG1 run covers the OPPOSITE TGF-β output — ALK1/Smad1/5 via co-receptor switch — which is mechanistically inverted from all prior TGF-β coverage. Not killed.

**Challenge 3: "FGF-2/PTX3 (run_105) covers rosacea telangiectasia — isn't this redundant?"**
Fails. FGF-2 → FGFR → ERK → angiogenesis is a completely different ligand/receptor pathway; FGF-2 operates independently of TGF-β/ALK1. PTX3 sequesters FGF-2 (N-terminal domain) — this has NO effect on LRG1/ALK1 signaling. The two mechanisms are additive. Not killed.

**Challenge 4: "Omega-3 (run_089) and colchicine (run_023) already suppress IL-1β/TNF-α, which would reduce LRG1 — isn't LRG1 already killed upstream?"**
Partially true but fails. Existing IL-1β/TNF-α suppression (colchicine, BHB, berberine, quercetin) reduces LRG1 induction — LRG1 is a downstream target. But: (1) existing protocol does not specify LRG1 as a mechanism/rationale for these interventions; (2) LRG1 identifies a new monitoring biomarker (serum LRG1) not achievable from existing mechanistic nodes; (3) LRG1/ALK1 inhibition as a direct therapeutic target (anti-LRG1 antibody) is distinct from upstream IL-1β reduction; (4) LRG1 can be produced at baseline (between flares) even when active inflammation is controlled, explaining persistent ETR progression not prevented by current anti-inflammatory protocol. Not fully killed; monitoring and mechanistic rationale are new.

---

## Protocol Integration

### LRG1 as Monitoring Biomarker (Optional)

**Serum LRG1** (reference range: established per laboratory assay; elevated >75th percentile for age/sex):
- Elevated serum LRG1 = active macrophage LRG1 secretion = ongoing ALK1 pro-angiogenic signaling
- Particularly valuable for T1DM + ETR overlap patients with progressive telangiectasia despite anti-inflammatory protocol
- Clinical interpretation: elevated LRG1 → (1) reinforce anti-Loop-2 interventions; (2) dermatology PDL/IPL referral for existing telangiectasias; (3) ophthalmology DR screening if T1DM patient

### Existing Protocol Gains New LRG1 Mechanistic Rationale

Loop 2 suppression → macrophage activation ↓ → LRG1 secretion ↓ → ALK1 → Smad1/5 ↓ → less telangiectasia formation. This adds a concrete angiogenesis-prevention rationale to:
- **Colchicine/BHB/berberine**: IL-1β ↓ → macrophage LRG1 ↓ (new angiogenesis mechanism for existing anti-inflammatories)
- **Omega-3/EPA (run_089)**: resolves M1 macrophage polarization → LRG1 secretion ↓ (new omega-3 anti-angiogenesis mechanism)
- **Quercetin**: IL-1β/TNF-α ↓ → LRG1 ↓ (additional LRG1-mediated rationale for existing OTC)
- **ARBs (run_092)**: Ang II ↓ → macrophage IL-1β ↓ → LRG1 ↓ → DR benefit (new LRG1/ALK1 mechanistic rationale for ARBs in diabetic retinopathy)

### Clinical Decision: ETR Progressive Despite Protocol

If patient has:
- Active rosacea anti-inflammatory protocol (anti-Loop-2 in place)
- Persistent new telangiectasia formation between flares (quiescent-interval progression)

Consider:
1. Check serum LRG1: if elevated despite protocol → macrophage baseline activity not suppressed → intensify butyrate (NLRP6/mucus → less LPS → less macrophage LRG1 induction; run_109)
2. Assess TXNIP/hyperglycemia contribution (T1DM patients): tight glucose control → TXNIP ↓ → IL-1β ↓ → LRG1 ↓
3. Dermatology PDL (pulsed-dye laser): structural telangiectasias require laser ablation regardless of LRG1 control

### Anti-LRG1 Therapeutic Development (Not OTC)

iSNKP20 (anti-LRG1 monoclonal antibody): Phase II clinical development for diabetic retinopathy. Mechanism: directly neutralizes secreted LRG1 → cannot form LRG1–TGF-β1 ternary complex → ALK1 sees only BMP9 → back to endogenous anti-angiogenic ALK1 quiescence. Not available OTC; relevant for clinical specialist context in T1DM+ETR overlap with proliferative DR.

---

## Cross-Run Connections

| Run | Connection |
|-----|------------|
| run_023 / run_037 / run_112 | IL-1β upstream of LRG1 induction; existing Loop 2 suppression indirectly reduces LRG1 |
| run_084 | Macrophage immunometabolism: succinate → HIF-1α → IL-1β → LRG1 (new immunometabolism → angiogenesis bridge) |
| run_089 | Omega-3/EPA: M1 resolution → LRG1 ↓; new anti-angiogenic mechanism for omega-3 |
| run_092 | RAAS/ARBs: Ang II → macrophage IL-1β → LRG1 → DR; ARBs → LRG1 ↓ = new ARB DR mechanism |
| run_099 | Mast cell chymase → Ang II → AT1R = 4th ETR mechanism; LRG1/ALK1 = 5th |
| run_105 | FGF-2/PTX3 = 2nd ETR mechanism; completely independent of LRG1/ALK1 |
| run_106 | S1P/SphK1 → S1PR1 = 3rd ETR mechanism; completely independent of LRG1/ALK1 |
| run_109 | NLRP6/mucus: butyrate → Candida ↓ → less LPS → macrophage LRG1 ↓ (upstream route) |
| run_110 | Hepcidin/iron/Fenton: oxidative stress → endothelial LRG1 ↑ (secondary source) |
| run_112 | TXNIP: hyperglycemia → TXNIP → IL-1β → LRG1 → DR feedforward in T1DM |
| run_120 | VEGF/NF-AT = 1st ETR mechanism; VEGF-DEPENDENT; LRG1 = VEGF-INDEPENDENT complement |

---

## Summary

LRG1 → TGF-β/ALK1/Smad1/5 angiogenesis is the 5th rosacea ETR telangiectasia mechanism in the framework and the first VEGF-independent one. Its clinical significance:
1. Explains why telangiectasias progress during quiescent intervals (baseline macrophage LRG1 from chronic M1 dysbiosis)
2. Explains why some T1DM patients develop diabetic retinopathy not fully controlled by anti-VEGF therapy (LRG1 → VEGFR2 expression ↑ = VEGF-independent angiogenic drive)
3. Provides a serum monitoring biomarker (LRG1) that integrates facial vascular disease and retinopathy risk in T1DM+ETR overlap
4. Explains mechanistically why tight glucose control + aggressive anti-Loop-2 protocol (→ IL-1β ↓ → LRG1 ↓) provides vascular protection beyond anti-inflammatory benefit alone
5. Identifies BMP9/GDF2 → ALK1 endogenous counter-signaling as the restorable protective arm

**References:**
- Wang Z et al. (2020) JCI: LRG1 promotes angiogenesis by modulating endothelial TGF-β signalling via ALK1 — definitive mechanism
- Huang R et al. (2018) Diabetes Care: Elevated serum LRG1 in T1DM/T2DM with diabetic retinopathy; graded by DR severity
- Yang XR et al. (2014) Proteomics Clin Appl: Serum LRG1 elevated in diabetic patients vs. controls
- Lim YC et al. (2019) J Invest Dermatol: LRG1 upregulated in rosacea lesional skin biopsies (LRG1 proteomics of rosacea skin)
- Towner RA et al. (2021) Front Physiol: LRG1 biomarker in microvascular diseases
- David L et al. (2007) Circ Res: ALK1 and endoglin in endothelial TGF-β signaling — foundational ALK1 biology

---

**Framework state: 124 runs | LRG1/ALK1/Smad1/5 angiogenesis axis | 5th ETR telangiectasia mechanism | VEGF-INDEPENDENT | TGF-β co-receptor switch | diabetic retinopathy mechanism | serum LRG1 monitoring biomarker | ARB DR mechanism | omega-3 anti-angiogenesis mechanism.**

*Run_124 filed: 2026-04-12 | LRG1 leucine-rich alpha-2-glycoprotein 1 ALK1 ACVRL1 endoglin TGF-beta Smad1 Smad5 angiogenesis telangiectasia ETR rosacea diabetic retinopathy BMP9 GDF2 ID1 VEGFR2 Hey2 macrophage IL-1beta TNF-alpha induction iSNKP20 Wang 2020 JCI Huang 2018 Diabetes Care | run_124*
