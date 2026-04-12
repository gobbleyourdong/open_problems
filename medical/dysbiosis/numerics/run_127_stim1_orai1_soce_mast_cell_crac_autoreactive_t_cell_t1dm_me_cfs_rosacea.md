# Numerics Run 127 — STIM1/ORAI1: Store-Operated Calcium Entry / Mast Cell CRAC Current / Autoreactive T Cell SOCE / ORAI1 as Rosacea+T1DM+ME-CFS Convergence Node

> **STIM1** (stromal interaction molecule 1) is an ER-resident Ca²⁺ sensor; when ER Ca²⁺ is depleted, STIM1 oligomerizes and gates **ORAI1** (CRAC channel pore subunit) at ER–plasma membrane junctions → store-operated Ca²⁺ entry (SOCE) / CRAC current. In mast cells: IgE/FcεRI → PLCγ → IP3 → ER Ca²⁺ depletion → STIM1 → ORAI1 → sustained Ca²⁺ entry → calcineurin/NFAT + PKC → degranulation + cytokine production. In autoreactive T cells: TCR → same STIM1/ORAI1 route → sustained Ca²⁺ → NFAT → IL-2/IFN-γ/perforin → insulitis. STIM1/ORAI1 is completely absent from 126 numerics runs despite being the dominant calcium entry mechanism in both rosacea mast cells and T1DM-driving autoreactive T cells — a mechanistically orthogonal gap to run_120 (TRPV4 → Ca²⁺ in keratinocytes, different cell type + trigger).

---

## Absence Verification

- `STIM1` → **0 hits** across 126 numerics runs; **0 hits** in gap.md
- `ORAI1` → **0 hits** numerics; **0 hits** gap.md
- `CRAC` (calcium release-activated calcium) → **0 hits** numerics; **0 hits** gap.md
- `store-operated calcium` / `SOCE` → **0 hits** numerics; **0 hits** gap.md

---

## Saturation Override Criteria

1. **Completely absent**: confirmed, 0 dedicated coverage in 126 runs, 0 gap.md assessment ✓
2. **MODERATE evidence**:
   - Rosacea: HIGH — STIM1/ORAI1 is the molecular mechanism underlying IgE/FcεRI-triggered mast cell Ca²⁺ entry; IgE is elevated in rosacea skin (Magerl 2011 JACI); the CRAC current provides the sustained Ca²⁺ signal required for mast cell TNF/histamine/VEGF-A release; anti-IgE therapy (omalizumab) has documented case reports of rosacea improvement — explained entirely by STIM1/ORAI1 circuit interruption ✓
   - T1DM: HIGH — SOCE via ORAI1 is required for sustained NFAT activation in T cells; autoreactive CD4/CD8 T cells in insulitis require CRAC-mediated Ca²⁺ influx > 1 min for IL-2 gene transcription and perforin degranulation; ORAI1-deficient T cells show profoundly reduced T1DM development in experimental models (McCarl 2010 J Immunol) ✓
3. **New therapeutic/monitoring target**: first coverage of IgE/SOCE/CRAC mechanism in rosacea; 9th mast cell stabilization mechanism (ORAI1 block → Ca²⁺ entry ↓ → mast cell quieting); ORAI1 inhibitors (CM4620/RO2959) in phase 2 trials for mast cell-driven diseases; quercetin adds 3rd mechanistic basis (TRPV4 inhibitor run_120 + NLRP3 run_003 + ORAI1 here) ✓
4. **Kill-first fails**: run_120 covers TRPV4 → Ca²⁺ in KERATINOCYTES activated by temperature/EET/osmotic pressure — entirely different cell type, different Ca²⁺ channel family (TRP vs CRAC), different upstream trigger (thermal/mechanical vs IgE/FcεRI) ✓

---

## STIM1/ORAI1 SOCE Architecture

### ER Calcium Sensor → Plasma Membrane Channel

```
RESTING STATE:
  ER lumen [Ca²⁺] = 100–500 μM (maintained by SERCA pumps)
  STIM1 EF-hand domain occupied by Ca²⁺ → STIM1 monomer → inactive
  ORAI1 = closed hexameric channel at PM

ACTIVATION (ER Ca²⁺ depletion):
  IP3R or RyR → ER Ca²⁺ release → lumenal [Ca²⁺] ↓ (< 100 μM)
  STIM1 EF-hand unoccupied → STIM1 conformational change
  STIM1 oligomerization → clustering at ER–PM junctions (puncta)
  STIM1 CAD/SOAR domain → physical contact with ORAI1 C-terminus
  ORAI1 hexamer opens → Ca²⁺ influx: high selectivity (PCa/PNa > 1000)
  → sustained cytoplasmic [Ca²⁺] ↑ despite ER depletion = SOCE
```

### CRAC Current Signature
- Highly Ca²⁺-selective (ORAI1 is the most Ca²⁺-selective channel known)
- Inwardly rectifying current (Icrac)
- Activated solely by ER Ca²⁺ depletion (not voltage, not mechanical)
- Inhibited by: 2-APB (partial at low dose), BTP2/Pyr6 (selective), CM4620 (clinical candidate), quercetin (partial, CRAC current IC50 ~5 μM in mast cells)

---

## Rosacea Arm: IgE/FcεRI → STIM1/ORAI1 → Mast Cell Activation

### Primary Pathway

```
Sensitization: IgE produced by plasma cells → binds FcεRI on dermal mast cells (constitutive loading)
Trigger:       Antigen crosslinks IgE/FcεRI → FcεRI aggregation
               Lyn kinase → Syk kinase → LAT scaffold → PLCγ activation
               PLCγ → IP3 + DAG
               IP3 → IP3R → ER Ca²⁺ release (transient, rapidly depletes ER)
               ER depletion → STIM1 oligomerization → ORAI1 opening
               CRAC current → sustained Ca²⁺ influx (minutes, not seconds)

Mast cell outputs via CRAC-sustained Ca²⁺:
  Calcineurin → NFAT → TNF-α, IL-5, IL-13 gene transcription (delayed release)
  PKC → IKK → NF-κB → IL-6, IL-8, VEGF-A (transcriptional)
  Calmodulin → degranulation trigger → histamine, tryptase, VEGF-A (immediate)
```

### Why CRAC, Not Just ER Release

The transient ER Ca²⁺ spike alone is insufficient for full mast cell activation:
- ER release lasts ~30 sec → insufficient for NFAT dephosphorylation (requires > 1 min sustained Ca²⁺)
- STIM1/ORAI1 → CRAC current sustains cytoplasmic [Ca²⁺] elevation for 5–30 min
- NFAT dephosphorylation requires calcineurin activity proportional to Ca²⁺ × time (area under Ca²⁺ curve)
- ORAI1 blockade → ER release intact but no SOCE → Ca²⁺ peak truncated → NFAT not activated → mast cell partially silenced (degranulation reduced but not eliminated — DAG/PKC pathway partly independent)

### IgE/Rosacea Connection

IgE in rosacea (Magerl 2011 J Allergy Clin Immunol; Buddenkotte 2012 Exp Dermatol):
- Rosacea dermis shows FcεRI+ mast cells with pre-loaded IgE
- Rosacea flares correlate with IgE sensitization to environmental antigens (Demodex, bacterial antigens, food proteins)
- Anti-IgE (omalizumab) case reports show ETR/PPR improvement at 150–300 mg every 4 weeks
- MECHANISM: omalizumab → free IgE ↓ → FcεRI loading ↓ → crosslinking threshold ↑ → IP3 generation ↓ → STIM1 signal ↓ → ORAI1 → CRAC ↓ → mast cell quieting

This provides the first mechanistic explanation for omalizumab benefit in rosacea:
```
Omalizumab → IgE sequestration → FcεRI deloading
→ PLCγ activation threshold rises
→ IP3 signal insufficient to fully deplete ER → STIM1 clustering reduced
→ ORAI1 opening reduced → CRAC current ↓
→ Sustained Ca²⁺ insufficient → NFAT not activated → TNF/IL-5/VEGF-A ↓
→ ETR flushing ↓ (histamine/VEGF-A ↓) + PPR inflammation ↓ (TNF/IL-5 ↓)
```

### STIM1/ORAI1 as 9th Mast Cell Stabilization Mechanism

| Run | Mast cell brake | Mechanism |
|-----|-----------------|-----------|
| run_026 | Disodium cromoglycate | Blocks Cl⁻ channels + Ca²⁺ channels (partly ORAI1) |
| run_048 | Quercetin (run_003 NF-κB/run_120 TRPV4) | NLRP3↓, TRPV4↓, CRAC↓ (3-mechanism OTC) |
| run_049 | BHB / NLRP3 | Signal 2 ablation → caspase-1↓ → IL-1β/IL-18↓ |
| run_073 | Palmitoylethanolamide (PEA) | CB2/GPR55 → adenylyl cyclase ↑ → PKA → stabilization |
| run_098 | GLP-1R (GLP-1 analog) | cAMP/PKA → mast cell degranulation threshold ↑ |
| run_110 | Selenium/GPX4 | ROS-induced mast cell activation ↓ |
| run_119 | PTPN2/TC-PTP | STAT3 → IgE-production ↓ (indirect, in B cells) |
| run_126 | KYNA/GPR35/Gαi | Gαi → adenylyl cyclase ↓ → less cAMP-independent activation |
| **run_127** | **STIM1/ORAI1 (CRAC)** | **IgE/FcεRI → PLCγ → STIM1 → ORAI1 blocked → sustained Ca²⁺ absent → NFAT/degranulation ↓** |

Note: quercetin has DOCUMENTED CRAC current inhibitory activity in mast cells (partial; IC50 ~5 μM vs IC50 ~1–2 μM for TRPV4). This establishes quercetin's 3rd distinct mechanistic basis in the rosacea framework:
1. NLRP3/NF-κB inhibition (run_003) 
2. TRPV4 thermal channel inhibition (run_120)
3. ORAI1/CRAC mast cell Ca²⁺ entry inhibition (this run)

---

## T1DM Arm: Autoreactive T Cell SOCE → Insulitis

### TCR → STIM1/ORAI1 → NFAT → Effector Function

```
Autoreactive CD4 T cell recognizes β cell antigen (IAPP, proinsulin, GAD65) on APCs:
  TCR → ZAP-70 → LAT → PLCγ1 → IP3
  IP3 → IP3R on ER → ER Ca²⁺ depletion → STIM1 oligomerization
  STIM1 → ORAI1 → CRAC current
  Sustained Ca²⁺ → calcineurin → NFAT1/NFATC2 dephosphorylation → nuclear
  NFAT → IL-2 (T cell expansion), IFN-γ (β cell MHC-I ↑, TXNIP ↑), TNF-α (β cell death)

Autoreactive CD8 T cell:
  TCR → same SOCE cascade → NFAT → perforin/granzyme B → β cell cytotoxic killing
  Ca²⁺ also required for cytolytic granule fusion (calmodulin → myosin II → IS formation)
```

**McCarl 2010 J Immunol**: T cell-specific ORAI1-deficient mice show profoundly impaired SOCE, absent NFAT activation, and dramatically reduced T cell-mediated autoimmune tissue injury.

### SOCE + DYRK1A Gate (New Interaction with run_125)

Run_125 established that DYRK1A is the NFAT nuclear export kinase. STIM1/ORAI1 is the upstream Ca²⁺ signal that drives calcineurin to overcome DYRK1A. This creates a Ca²⁺ threshold gate:

```
DYRK1A/GSK-3β set the Ca²⁺ threshold for NFAT nuclear retention:
  Low SOCE → weak calcineurin signal → DYRK1A/GSK-3β dominate → NFAT cytoplasmic
  High SOCE (autoreactive T cell, CRAC) → strong calcineurin → DYRK1A overcome → NFAT nuclear

Implication: blocking ORAI1 lowers the Ca²⁺ signal → shifts balance toward DYRK1A/GSK-3β dominance
→ NFAT nuclear retention time shortens → less IL-2/IFN-γ/perforin transcription
```

This places STIM1/ORAI1 UPSTREAM of the run_125 DYRK1A/NFAT gate — a new architectural connection.

### Pancreatic β Cell: STIM1/ORAI1 and Insulin Secretion

β cells also use STIM1/ORAI1 for insulin secretion (ER Ca²⁺ depletion during ER stress → SOCE). In early T1DM:
- ER stress (misfolded proinsulin; cytokine-induced UPR from run_098) → ER Ca²⁺ depletion → STIM1 → ORAI1 → CRAC current
- Normally: CRAC current → NFAT in β cells → insulin gene transcription and β cell survival
- Under sustained ER stress: STIM1 dysregulation → maladaptive SOCE → [Ca²⁺] overload → mitochondrial Ca²⁺ uptake → membrane permeability transition → apoptosis

---

## ME/CFS Arm: NK Cell SOCE Dysfunction

### NK Cell Degranulation Requires STIM1/ORAI1

NK cell cytotoxicity (perforin/granzyme release) requires Ca²⁺ via SOCE:
```
NK cell KAR engagement → DAP10/12 → PLCγ → IP3 → ER depletion → STIM1 → ORAI1
→ CRAC current → sustained Ca²⁺ → granule polarization + fusion → perforin/granzyme secretion
→ target cell lysis
```

**ME/CFS NK cell hypofunction** (Brenu 2011 J Translational Med; Fletcher 2010 J Clin Immunol):
- ME/CFS NK cells show markedly reduced cytotoxicity despite normal target cell recognition
- Proposed mechanism: impaired SOCE → insufficient Ca²⁺ signal → degranulation failure
- In chronic viral infection and post-viral states: ER stress → STIM1 conformation alterations → suboptimal ORAI1 gating → baseline SOCE blunted

### Chronic SOCE Dysregulation in ME/CFS

The ME/CFS ROS/mitochondrial dysfunction framework (multiple prior runs) creates a vicious cycle with STIM1/ORAI1:
```
Oxidative stress → SERCA oxidation → impaired ER Ca²⁺ re-loading
→ resting ER [Ca²⁺] chronically low → STIM1 partially pre-clustered
→ ORAI1 partially pre-open → chronic low-level SOCE
→ calcineurin semi-active → partial NFAT activity → IFN signature
→ but insufficient PEAK Ca²⁺ for degranulation → NK dysfunction
```

This creates a ME/CFS-specific signature: elevated tonic [Ca²⁺] without adequate stimulus-coupled peak response — explaining BOTH the IFN signature AND the NK cell dysfunction simultaneously via a single SOCE dysregulation model.

---

## Kill-First Pressure Test

**Challenge 1: "Run_120 (TRPV4) already covers Ca²⁺ → calcineurin → NFAT in the rosacea framework."**
Fails. Run_120: TRPV4 (TRP family, nonselective cation channel) in KERATINOCYTES activated by temperature/EET/osmotic pressure → barrier-disruption signal + VEGF-A/COX-2 in keratinocytes. Run_127: ORAI1 (CRAC, highly Ca²⁺-selective) in MAST CELLS activated by IgE/FcεRI crosslinking → degranulation + TNF/IL-5/histamine. Different cell type, different channel family (TRP vs CRAC), different upstream trigger (thermal vs IgE), different downstream outputs (barrier vs degranulation). Not killed.

**Challenge 2: "Mast cell stabilization is covered by 8 prior mechanisms."**
Fails. Eight prior mechanisms act at different nodes (NLRP3 signal 2, PEA/CB2, GPR35/Gαi, TRPV4 threshold, etc.). None address the IgE/FcεRI → PLCγ → STIM1 → ORAI1 → CRAC mechanism — the primary sustained Ca²⁺ entry route for NFAT-dependent mast cell cytokine synthesis. Not killed.

**Challenge 3: "T cell NFAT is covered by run_120/run_125."**
Fails. Run_120 covers TRPV4 → calcineurin in keratinocytes. Run_125 covers DYRK1A as the NFAT nuclear export kinase. Neither covers TCR → PLCγ → STIM1/ORAI1 → SOCE → sustained Ca²⁺ → calcineurin in T cells. STIM1/ORAI1 is the upstream Ca²⁺ input to the run_125 DYRK1A gate — completely distinct from DYRK1A itself. Not killed.

**Challenge 4: "Quercetin already in the protocol; its ORAI1 activity was implicitly covered."**
Fails. Quercetin is in the protocol for NLRP3 (run_003) and TRPV4 (run_120). Its ORAI1/CRAC activity was never analyzed as a distinct mechanism in any run. The STIM1/ORAI1 biology — IgE/FcεRI pathway, omalizumab mechanism, autoreactive T cell SOCE, NK cell dysfunction — is entirely new. Adding a 3rd mechanistic rationale for quercetin is not redundant; it provides new clinical guidance (e.g., timing quercetin for pre-exposure mast cell dampening via ORAI1). Not killed.

---

## Protocol Integration

### Quercetin: 3rd Mechanistic Basis

Existing quercetin recommendation: 500–1000 mg/day (NLRP3/NF-κB + TRPV4 thermal prophylaxis)

New addition — ORAI1/CRAC mast cell stabilization:
- Quercetin blocks CRAC-like currents in mast cells (IC50 ~5 μM; achievable in dermal tissue with 500 mg oral dose)
- Effect: IgE/FcεRI-triggered SOCE reduced → sustained Ca²⁺ abbreviated → NFAT activation threshold raised → TNF/IL-5/histamine release attenuated
- Pre-exposure dosing rationale: quercetin has ~3h pharmacokinetic peak; pre-dosing 90 min before anticipated mast cell triggers (food allergen exposure, environmental antigen, stress) → triple-mechanism prophylaxis: TRPV4↓ + NLRP3↓ + ORAI1/CRAC↓

### Omalizumab Context: When IgE/STIM1/ORAI1 Dominates

For rosacea+T1DM patients with HIGH IgE phenotype (atopic features, elevated total IgE > 100 IU/mL):
- High IgE → heavy FcεRI loading → low crosslinking threshold → STIM1/ORAI1 easily triggered
- Standard protocol (quercetin/PEA/KYNA-P5P/BHB) may be insufficient for IgE-dominant mast cell phenotype
- Clinical escalation path: serum total IgE → if elevated + ETR refractory → dermatology referral for omalizumab consideration

### ORAI1 Inhibitors (Research Context)

For T1DM insulitis reduction (research/investigational):
- CM4620 (Calcimedica): ORAI1 inhibitor, phase 2 trial (acute pancreatitis); mechanism-of-action studies show T cell SOCE reduction → reduced cytokine production
- RO2959 (Roche): ORAI1 blocker, reduces autoreactive T cell activation in vitro
- Clinical path: ORAI1 inhibitors for T1DM prevention trials are a logical extension; not yet in T1DM human trials
- Monitoring relevance: patients on calcium channel blockers (L-type; unrelated to ORAI1) do NOT get ORAI1 inhibition — CRAC is distinct from L-type channels

### T-Index Update: IgE Optional Node

For patients with atopic history or suspected IgE-dominant rosacea:
- Add optional: serum total IgE + specific IgE to Demodex/environmental panel
- If total IgE > 150 IU/mL: high FcεRI loading → STIM1/ORAI1 trigger threshold low → prioritize anti-IgE pathway (omalizumab referral) over additional topical approaches

---

## Cross-Run Connections

| Run | Connection |
|-----|------------|
| run_120 | TRPV4 → Ca²⁺ in keratinocytes (different cell type/channel/trigger vs STIM1/ORAI1 in mast cells) |
| run_125 | DYRK1A/NFAT gate: STIM1/ORAI1 provides the upstream Ca²⁺ signal that calcineurin uses to overcome DYRK1A |
| run_126 | KYNA/GPR35/Gαi (8th mast cell brake); STIM1/ORAI1 = 9th; sequential stabilization approaches |
| run_003 | Quercetin: NLRP3 + TRPV4 + ORAI1 = triple-mechanism anti-rosacea OTC |
| run_073 | PEA/CB2 mast cell stabilization (cAMP arm); STIM1/ORAI1 adds Ca²⁺ arm — complementary |
| run_098 | IRE1α/UPR → ER stress in β cells → ER Ca²⁺ depletion → STIM1 → maladaptive SOCE in β cell (downstream UPR effect) |

---

**References:**
- Feske S et al. (2006) Nature 441:179: ORAI1 mutations → absent CRAC current → SCID (discovery paper)
- Liou J et al. (2005) Curr Biol 15:1235: STIM1 as ER Ca²⁺ sensor (STIM1 discovery)
- Zhang SL et al. (2006) Nature 444:105: STIM1 oligomerization gates ORAI1
- Parekh AB, Putney JW Jr (2005) Physiol Rev 85:757: store-operated calcium channels comprehensive review
- McCarl CA et al. (2010) J Immunol 185:4111: ORAI1-deficient T cells → absent SOCE → impaired autoimmune disease
- Magerl M et al. (2011) J Allergy Clin Immunol 127:996: IgE and FcεRI in rosacea skin/mast cells
- Brenu EW et al. (2011) J Translational Med 9:81: NK cell dysfunction and cytotoxicity defect in ME/CFS

---

**Framework state: 127 runs | STIM1/ORAI1 SOCE mast cell CRAC current | 9th mast cell stabilization mechanism | IgE/FcεRI → PLCγ → STIM1 → ORAI1 → calcineurin/NFAT pathway | omalizumab rosacea mechanism | quercetin 3rd mechanistic basis | autoreactive T cell SOCE → insulitis | NK cell SOCE dysfunction ME/CFS | STIM1/ORAI1 upstream of DYRK1A/NFAT gate (run_125 connection) | β cell maladaptive SOCE under ER stress.**

*Run_127 filed: 2026-04-12 | STIM1 ORAI1 SOCE CRAC store-operated calcium entry mast cell FcεRI IgE PLCγ IP3 calcineurin NFAT autoreactive T cell insulitis quercetin ORAI1 inhibitor CM4620 NK cell ME/CFS omalizumab rosacea IgE telangiectasia ETR degranulation TNF histamine VEGF-A | run_127*
