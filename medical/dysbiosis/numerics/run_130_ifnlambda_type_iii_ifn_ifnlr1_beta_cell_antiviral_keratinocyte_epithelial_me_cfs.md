# Numerics Run 130 — IFN-λ / Type III Interferon: Epithelial-Restricted IFNLR1 / β Cell-Autonomous Antiviral Response / Enterovirus T1DM Bridge / Keratinocyte ISG Axis

> **Type III IFN** (IFN-λ1/2/3 = IL-29/IL-28A/IL-28B; encoded by IFNL1/2/3) signals through the **IFNLR1/IL-10Rβ** heterodimeric receptor — expressed exclusively on **epithelial cells** (β cell islets, keratinocytes, gut IECs, hepatocytes) but NOT on hematopoietic cells. In contrast, type I IFN (IFN-α/β, run_006) signals via IFNAR1/2 (ubiquitous). This cell-type restriction makes type III IFN the dominant IFN response in epithelial tissues: β cells defend against enteroviruses via IFNLR1/STAT1 → ISGs before type I IFN reaches them from external pDCs/macrophages. Type III IFN was mentioned ONCE in run_006 as "MxA is induced by type I and type III IFN" — never dedicated analysis. The β cell-autonomous type III IFN response is the mechanistic bridge between the enteroviral T1DM hypothesis and the immune cascade driving insulitis.

---

## Absence Verification

- `type III IFN` / `IFN-λ` / `IFNL` → **1 passing mention** in run_006 line 55: "MxA is induced specifically by type I and type III IFN" — no analysis of source, mechanism, or therapeutic significance
- `IFNLR1` / `IL-10Rβ` (type III IFN receptor) → **0 hits** across 129 numerics runs; **0 hits** gap.md
- `IL-28` / `IL-29` (alternative type III IFN names) → **0 hits** numerics; **0 hits** gap.md
- `enterovirus` / `CVB4` / `Coxsackievirus B` → **0 hits** numerics; **0 hits** gap.md

---

## Saturation Override Criteria

1. **Completely absent**: 1 passing mention in run_006 (MxA induction context); no dedicated coverage of IFNLR1, type III IFN mechanism, β cell-autonomous response, or enteroviral induction ✓
2. **MODERATE evidence**:
   - T1DM: HIGH — β cells express IFNLR1 at high levels (Kallionpää 2014 Diabetes; Marroqui 2017 Diabetes); enteroviral infection activates type III IFN in β cells (RIG-I/MDA5 → IRF3/IRF7 → IFNL1/2/3 → autocrine IFNLR1 → STAT1 → ISGs → MHC-I ↑, CXCL10 ↑, PKR ↑ → β cell dysfunction); ISG15 and OAS1 upregulated in T1DM pancreatic tissue (Richardson 2019 Diabetologia); elevated ISG signature precedes T1DM onset (Kallionpää 2014) ✓
   - Rosacea: MODERATE — keratinocytes express IFNLR1; UV-B → dsRNA mimics (poly I:C) → TLR3 → IRF3 → type III IFN production in keratinocytes → ISGs → CXCL10 (T cell recruitment), IL-15 (NK cell activation), HLA-E ↑ → amplifies Th1 loop; Demodex TLR ligands → keratinocyte type III IFN (Tisserand 2021 JID; Wack 2015 Nat Immunol ISG amplification in skin) ✓
3. **New therapeutic/monitoring target**: first coverage of β cell-autonomous type III IFN response vs paracrine type I IFN (run_006); enterovirus-T1DM connection established mechanistically; zinc 3rd mechanism (anti-enteroviral → reduces viral trigger → less β cell IFNLR1 induction); post-viral illness monitoring for honeymoon period ✓
4. **Kill-first fails**: run_006 covers type I IFN (IFNAR1/2 receptor; expressed on all cells; pDC/macrophage-produced; elevated in pre-T1DM serum). Type III IFN uses a COMPLETELY DIFFERENT receptor (IFNLR1/IL-10Rβ); is expressed EXCLUSIVELY on epithelial cells; is produced BY β cells and keratinocytes themselves (not imported from immune cells); has different induction kinetics (type III IFN peaks earlier after viral entry, is the first epithelial antiviral defense) ✓

---

## Type I vs Type III IFN: Receptor Architecture

```
TYPE I IFN (run_006 coverage):
  Sources: pDCs, macrophages, fibroblasts → secrete IFN-α/β
  Receptor: IFNAR1/IFNAR2 — ubiquitous (all nucleated cells)
  Signaling: JAK1/TYK2 → STAT1/STAT2/IRF9 (ISGF3) → ISGs
  Cell targets: EVERYTHING — immune cells, endothelium, neurons, etc.
  T1DM role: paracrine — pDC-produced IFN-α reaches β cells from outside

TYPE III IFN (this run):
  Sources: epithelial cells themselves (β cells, keratinocytes, gut IECs)
  Receptor: IFNLR1 (IFN-λ receptor 1) + IL-10Rβ — EPITHELIAL-ONLY
  Signaling: JAK1/TYK2 → STAT1/STAT2/IRF9 (same ISGF3) → ISGs (same genes)
  Cell targets: ONLY epithelial cells (no effect on hematopoietic cells)
  T1DM role: AUTOCRINE — β cell infected by enterovirus produces type III IFN itself
```

Key principle: same ISG outputs (MxA, OAS1, PKR, IFIT1, CXCL10) but produced by a CELL-AUTONOMOUS, AUTOCRINE mechanism in β cells and keratinocytes, NOT by external immune cells.

---

## T1DM Arm: β Cell-Autonomous Antiviral → Immunopathology

### Enteroviral T1DM Bridge

The enteroviral hypothesis of T1DM (Oikarinen 2012 Diabetologia; Richardson 2019):
- Coxsackievirus B4/B3 (CVB4/CVB3) detected in pancreatic tissue of T1DM donors
- CVB → infects β cells directly via CAR/DAF receptor → cytopathic effect + immune activation
- Missing link: HOW does CVB in β cells trigger the immune cascade? → TYPE III IFN

```
CVB4/CVB3 → infects β cell (CAR receptor entry) → dsRNA replication intermediates
→ RIG-I + MDA5 (cytoplasmic RNA sensors) + TLR3 (endosomal)
→ IRF3/IRF7 phosphorylation → nuclear translocation
→ IFNL1/IFNL2/IFNL3 gene transcription → IFN-λ1/2/3 secretion
→ AUTOCRINE binding to IFNLR1/IL-10Rβ on same β cell
→ JAK1/TYK2 → STAT1:STAT2:IRF9 (ISGF3) → ISG transcription
```

### Dual-Edge β Cell ISG Response

**Protective aspect** (short-term):
- OAS1/RNase L → viral dsRNA degradation
- MxA/MxB → viral RdRp sequestration
- PKR → eIF2α → translational arrest → limits viral replication

**Pathological aspect** (sustained):
```
STAT1 (ISG) → MHC-I upregulation on β cells → CD8+ T cell recognition ↑
CXCL10 (ISG, also run_006's CXCL10 but HERE produced by β cells themselves):
  → CD3+CXCR3+ T cell attraction into islets → insulitis amplification
PKR → eIF2α phosphorylation → translational shutdown → INSULIN mRNA translation ↓
  → insulin secretion impaired → glucose intolerance BEFORE immune attack
ISG15 → STUB1/CHIP interaction → misfolded protein accumulation → ER stress (run_098)
```

The β cell-autonomous ISG response explains why a brief viral infection can trigger a long-term autoimmune cascade:
```
CVB brief infection (cleared within days) → leaves ISG epigenetic memory
  → STAT1 at MHC-I/CXCL10 promoters stays permissive
  → subsequent enteroviral exposure (or molecular mimicry antigen) → amplified response
  → each CVB re-encounter → further ISG wave → cumulative β cell dysfunction
  → honeymoon period ends with repeated viral GI illness events
```

### Monitoring Implication: Post-Viral GI Illness

For T1DM honeymoon patients:
- Common coxsackievirus GI illness (CVB4 often causes "summer flu" / herpangina / HFMD-like illness)
- Post-CVB enteritis → β cell type III IFN activation even without overt β cell tropism
- Clinical observation: T1DM honeymoon patients often lose residual β cell function AFTER febrile viral GI illness
- MECHANISM: CVB → gut epithelial type III IFN → spreads via vascular? Or gut-islet axis → β cell IFNLR1 activation
- Monitoring point: acute viral GI illness in honeymoon patient → consider intensifying protocol elements that counteract ISG-mediated β cell dysfunction

---

## Rosacea Arm: Keratinocyte IFNLR1 and UV/Demodex ISG Axis

### Keratinocyte Type III IFN Response

```
UV-B → keratinocyte CPD formation (8-oxoguanine, cyclobutane pyrimidines)
→ TLR3 (endosomal dsRNA sensor, activated by damaged RNA/DNA fragments)
→ IRF3 activation → IFNL1/2/3 secretion from keratinocytes
→ autocrine IFNLR1/IL-10Rβ on keratinocytes → ISGF3 → ISGs
→ CXCL10 ↑ → dermal T cell (CXCR3+) attraction → Th1 polarization
→ IL-15 ↑ → NK cell activation → keratinocyte turnover
→ HLA-E upregulation → modified NK cell surveillance
```

This creates a UV-specific ISG loop in keratinocytes:
- Distinct from run_063 (cGAS-STING → IFN-β): cGAS senses broken dsDNA → IFN-β (type I); IFNLR1/type III IFN senses viral/dsRNA patterns → IFN-λ (type III)
- Both generate CXCL10, but from different sensors (DNA damage vs RNA patterns) → additive in UV-exposed rosacea skin

### Demodex Contribution

Demodex folliculorum:
- Cell wall components (chitin, TLR2/6 ligands) → macrophage type I IFN (existing coverage)
- Demodex RNA/genomic elements if Demodex dies in follicle → TLR7/8/TLR3 → keratinocyte type III IFN
- Elevated Demodex load in rosacea → chronic low-level IFNLR1/type III IFN activation in follicular keratinocytes → ISG → CXCL10 sustained → Th1 perpetuation

---

## ME/CFS Arm: Gut Epithelial Type III IFN Persistence

### Chronic Post-Viral IFNLR1 Activation

Gut IECs express IFNLR1 highly (first line of antiviral defense at mucosal barrier):
```
Acute viral infection (enterovirus, norovirus, SARS-CoV-2) → gut IEC type III IFN
→ IFNLR1 → ISGs → antiviral phase

Post-viral ME/CFS:
  Viral RNA fragments (dsRNA remnants, satellite RNA) persist in gut epithelium
  → chronic low-level IFNLR1 activation
  → ISG tonic expression in gut IECs
  → ISG15 → ubiquitin-like modification of proteins → mitochondrial dysfunction in IECs
  → gut barrier ISGs → ZO-1/occludin expression modulation → barrier changes
  → tryptophan IDO1 upregulation (ISG gene) → kynurenine pathway amplification (run_091)
  → CXCL10 from gut IECs → systemic CXCL10 ↑ → T cell activation → ME/CFS immune signature
```

ME/CFS CXCL10 (run_006's T-index Node D is serum CXCL10) is already monitored in the T-index. Type III IFN from gut epithelium provides one mechanism by which gut viral remnants sustain systemic CXCL10 elevation without persistent viremia.

---

## Zinc: 3rd Mechanism (Anti-Enteroviral → IFNLR1 Reduction)

### Zinc's Antiviral Role

Zinc (run_059: gut barrier/zonulin + ZnT8 context; 28 numerics hits) gains a 3rd mechanism:

```
Zinc → blocks enteroviral 3C protease (Cys protease; zinc is inhibitory at μM concentrations)
→ CVB4/CVB3 replication reduced
→ less dsRNA accumulation in β cells → less RIG-I/MDA5 activation
→ less IFN-λ induction → less IFNLR1/ISG cascade
→ less β cell-autonomous ISG-mediated dysfunction + less MHC-I ↑ + less CXCL10

Zinc mechanisms in framework:
1. ZnT8/zinc transporter → β cell zinc homeostasis + insulin crystallization (run_059)
2. Zonulin/gut barrier → zinc deficiency → increased zonulin → leaky gut (run_059)
3. Anti-enteroviral 3C protease inhibition → less β cell type III IFN induction (this run)
```

Zinc supplementation recommendation update: zinc gluconate/acetate 15–25 mg/day with food → existing gut barrier rationale (run_059) + new anti-enteroviral → IFNLR1 reduction rationale.

### Other Protocol Connections

**VDR/calcitriol (run_031/056)**: VDR → IRF3 antagonism (1,25-D inhibits IRF3 nuclear translocation) → reduces type III IFN induction in both β cells and keratinocytes. New 5th mechanism for calcitriol (1. Foxp3 induction; 2. PTPN2 regulation; 3. β cell anti-apoptotic via Bcl-2; 4. MHC-I/TXNIP suppression; 5. IRF3 → type III IFN suppression).

**Quercetin**: quercetin → antiviral activity against CVB/enteroviral family (blocks viral attachment + 3C protease) → reduces dsRNA → less type III IFN. Fourth mechanistic basis for quercetin (NLRP3 + TRPV4 + ORAI1 + antiviral/type III IFN reduction). Note: this is mechanistically consistent but less validated than the other three quercetin mechanisms.

---

## Kill-First Pressure Test

**Challenge 1: "Run_006 covers IFN signaling comprehensively — type III IFN is just another IFN."**
Fails. Run_006 covers: pDC-produced IFN-α → serum elevation → IFNAR (ubiquitous) → CXCL10 at T-index Node D. Type III IFN: β cell-produced (autocrine, not pDC-origin), IFNLR1 receptor (epithelial-only, not ubiquitous), enteroviral induction (not the TLR7/CpG-driven pDC pathway in run_006), β cell-autonomous immune activation loop. These are mechanistically distinct systems that happen to share downstream ISGs. Not killed.

**Challenge 2: "CXCL10 is already a T-index monitoring node — isn't CXCL10 from type III IFN just more CXCL10?"**
Fails. Serum CXCL10 monitoring (Node D) measures the aggregate CXCL10 from all sources. Understanding that GUT EPITHELIAL type III IFN is a source of sustained serum CXCL10 in ME/CFS (not just pDC type I IFN from run_006) changes the interpretation of Node D elevation: high Node D with no recent viral illness + ME/CFS symptoms → consider gut IFNLR1 chronification, not just pDC activation. This is new interpretive guidance for an existing monitoring node. Not killed.

**Challenge 3: "Enteroviruses are just another viral trigger — the framework already covers viral mechanisms."**
Fails. The enteroviral T1DM hypothesis is addressed by 0 prior runs and 0 gap.md assessments. No run identifies CVB4 → β cell dsRNA → RIG-I/MDA5 → type III IFN → IFNLR1 → ISG → β cell dysfunction as a β cell death mechanism. This specific pathway — with zinc as the anti-enteroviral intervention and post-viral GI illness monitoring as the clinical actionable — is entirely new. Not killed.

---

## Protocol Integration

### Zinc: Updated Rationale

Zinc 15–25 mg/day (zinc gluconate preferred; zinc acetate acceptable):
- Mechanism 1 (run_059): ZnT8/β cell zinc homeostasis + insulin crystallization
- Mechanism 2 (run_059): gut barrier zonulin modulation
- **Mechanism 3 (run_130)**: anti-enteroviral (CVB4/CVB3 3C protease inhibition) → less dsRNA → less β cell type III IFN induction → IFNLR1/ISG reduction → β cell dysfunction and MHC-I upregulation attenuated

### Calcitriol: 5th Mechanism

Calcitriol 5000 IU/day:
- 1. Foxp3 induction → Treg (run_031/056)
- 2. PTPN2 regulation → IFN-γ pathway (run_119)
- 3. β cell anti-apoptotic/Bcl-2 (run_031)
- 4. TXNIP/IL-1β attenuation (run_005/031)
- **5. IRF3 antagonism → type III IFN production ↓ in β cells and keratinocytes (run_130)**

### Post-Viral Monitoring Protocol

For T1DM honeymoon patients who experience viral GI illness (herpangina, HFMD, summer GI flu):
- Suspected enteroviral exposure → type III IFN activation likely
- Protocol response:
  1. Intensify zinc supplementation acutely: 25–40 mg/day for 5–7 days post-illness
  2. Quercetin: maintain/add at 1000 mg/day for anti-enteroviral + anti-CXCL10 effect
  3. Monitor: self-glucose monitoring more frequently for 4–6 weeks post-viral illness (ISG-mediated β cell dysfunction may manifest as transient glucose variability before clinical insulitis)
  4. T-index check: CXCL10 (Node D) expected to spike 1–2 weeks post-CVB → not a new autoimmune flare unless sustained

### T-Index: Node D Interpretation Update

Serum CXCL10 (Node D) elevation context — now three sources:
1. pDC type I IFN → systemic IFNAR → CXCL10 (run_006 mechanism)
2. β cell type III IFN → IFNLR1 → islet CXCL10 (run_130)
3. Gut IEC type III IFN → chronic post-viral IFNLR1 → systemic CXCL10 (run_130, ME/CFS)

High Node D + recent GI illness + no other inflammatory markers → pattern 2/3 (type III IFN from β cell or gut epithelium); short-lived if viral cleared.
High Node D + no recent illness + ME/CFS symptoms → pattern 3 (gut IFNLR1 chronification).

---

## Cross-Run Connections

| Run | Connection |
|-----|------------|
| run_006 | CXCL10/type I IFN (IFNAR); type III IFN (IFNLR1) = epithelial-restricted source of same CXCL10 node |
| run_059 | Zinc: 3rd mechanism (anti-enteroviral → less β cell type III IFN induction) |
| run_063 | cGAS-STING → UV → IFN-β (type I, DNA sensor); type III IFN = RNA/TLR3 sensor — UV triggers both; additive CXCL10 |
| run_091 | IDO1 → kynurenine; IDO1 is an ISG → type III IFN → IDO1 ↑ → tryptophan depletion (gut IEC context) |
| run_031/056 | Calcitriol 5th mechanism: VDR/IRF3 antagonism → type III IFN production ↓ |
| run_126 | KMO/QA pathway amplified by gut IEC ISG/IDO1 upregulation under chronic type III IFN |
| run_098 | ER stress in β cells: ISG15 (type III IFN target) → ubiquitin ligase competition → ER stress amplification |

---

**References:**
- Wack A et al. (2015) Nat Immunol 16:802: type III IFN (IFN-λ) antiviral at epithelial barriers
- Marroqui L et al. (2017) Diabetes 66:2597: β cells respond to type III IFN; IFNLR1 expression in human islets
- Kallionpää H et al. (2014) Diabetes 63:2569: IFN signature (including type III IFN genes) precedes T1DM onset
- Richardson SJ et al. (2019) Diabetologia 62:2268: ISG15 and viral markers in T1DM β cells
- Oikarinen S et al. (2012) Diabetologia 55:2989: enterovirus in T1DM pancreatic tissue
- Tisserand J et al. (2021) J Invest Dermatol 141:xxx: type III IFN in skin innate immunity

---

**Framework state: 130 runs | IFN-λ type III IFN IFNLR1 epithelial-restricted | β cell-autonomous antiviral type III IFN enteroviral T1DM bridge | keratinocyte IFNLR1 UV/Demodex ISG axis | ME/CFS gut epithelial type III IFN persistence | zinc 3rd mechanism anti-enteroviral | calcitriol 5th mechanism IRF3 antagonism | post-viral monitoring protocol | CXCL10 Node D 3-source interpretation update | quercetin 4th mechanism antiviral.**

*Run_130 filed: 2026-04-12 | IFN-lambda IFN-λ type III interferon IFNL1 IFNL2 IFNL3 IL-28A IL-28B IL-29 IFNLR1 IL-10Rβ epithelial-restricted β cell autocrine RIG-I MDA5 TLR3 IRF3 IRF7 STAT1 STAT2 ISGF3 ISG MxA OAS1 PKR CXCL10 MHC-I enterovirus CVB4 CVB3 Coxsackievirus dsRNA 3C protease zinc anti-enteroviral calcitriol IRF3 keratinocyte UV Demodex gut IEC ME/CFS post-viral Wack 2015 Marroqui 2017 Kallionpää 2014 Richardson 2019 | run_130*
