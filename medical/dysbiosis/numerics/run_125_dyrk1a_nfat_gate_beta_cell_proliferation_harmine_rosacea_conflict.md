# Numerics Run 125 — DYRK1A: NF-AT Nuclear Export Kinase / β Cell Proliferation / Harmine Rosacea Conflict

> **DYRK1A** (dual-specificity tyrosine-regulated kinase 1A) phosphorylates NFAT1/2/4 → nuclear export → NF-AT transcription off. It is the endogenous kinase that OPPOSES calcineurin-driven NF-AT activation (run_120: TRPV4 → Ca²⁺ → calcineurin → dephospho-NFAT → NF-AT nuclear → VEGF-A/COX-2/IL-5). DYRK1A and GSK-3β act SEQUENTIALLY on NFAT, meaning berberine (run_114 GSK-3β inhibitor) partially reduces the NF-AT brake. Harmine (a natural DYRK1A inhibitor in commercial supplements) promotes β cell proliferation for T1DM honeymoon but simultaneously activates NF-AT in keratinocytes — the FIRST supplement-class contraindication specific to the rosacea+T1DM combination in the framework.

---

## Absence Verification

- `DYRK1A` → **0 hits** across 123 numerics runs; **0 hits** in gap.md
- `harmine` / `leucettine` → **0 hits** in numerics; **0 hits** in gap.md
- NF-AT is first introduced in run_120; DYRK1A as its opposing kinase was never analyzed

---

## Saturation Override Criteria

1. **Completely absent**: confirmed, 0 dedicated mechanistic coverage; not assessed ✓
2. **MODERATE evidence**:
   - T1DM: HIGH — Wang 2015 Cell (harmine → DYRK1A inhibition → β cell NFAT → CyclinD1 → proliferation; first selective β cell proliferation compound); Ackeifi 2020 Nature Metabolism (harmine + GLP-1R agonist synergy); multiple confirmatory studies ✓
   - Rosacea: MODERATE by mechanism — DYRK1A is the canonical NFAT nuclear export kinase across all cell types; keratinocyte NF-AT is established in run_120 (TRPV4 → calcineurin → NF-AT → VEGF-A/COX-2/IL-5); DYRK1A inhibition in keratinocytes → NF-AT dwell time ↑ → same inflammatory targets amplified ✓
3. **New clinical guidance**: first explicit supplement contraindication in rosacea+T1DM (harmine); new interaction between run_114 (berberine/GSK-3β) and run_120 (NF-AT); no prior run has identified this conflict ✓
4. **Kill-first fails**: run_120 covers calcineurin → NF-AT ON side; DYRK1A is the opposing OFF kinase — different biology; run_114 covers GSK-3β → Foxp3 degradation, never mentions NFAT phosphorylation ✓

---

## DYRK1A/GSK-3β → NF-AT Nuclear Export Architecture

### The NF-AT Gate

NF-AT (nuclear factor of activated T cells; NFAT1-4) is regulated by competing phosphorylation/dephosphorylation:

```
RESTING STATE:
  DYRK1A → pSer169 on NFAT (initiating phosphorylation, priming site)
  GSK-3β → processively extends phosphorylation (6-9 additional Ser)
  Fully phosphorylated NFAT → CRM1/RanGAP → nuclear export → cytoplasmic (OFF)

ACTIVATION (TRPV4 trigger, run_120):
  TRPV4 → Ca²⁺ influx → calmodulin → calcineurin (PP2B phosphatase)
  Calcineurin → dephosphorylates NFAT (reverses DYRK1A/GSK-3β phosphorylation)
  Dephospho-NFAT → nuclear import → VEGF-A, COX-2, IL-5 transcription (ON)
```

### Sequential DYRK1A → GSK-3β Cooperation

DYRK1A and GSK-3β are NOT parallel but SEQUENTIAL (Beals 1997 Science; Gwack 2006 J Immunol):

```
Step 1: DYRK1A → pSer169 on NFAT (creates GSK-3β recognition motif pSer-X-X-X-Ser)
Step 2: GSK-3β reads pSer169 → phosphorylates upstream Ser residues processively
         → full NFAT phosphodegron assembled → CRM1 export signal
Step 3: CRM1/Exportin-1 → nuclear export → NFAT cytoplasmic/inactive

Consequence: DYRK1A primes GSK-3β; block either → partial NF-AT activation; block DYRK1A → GSK-3β cannot proceed at all → maximal NF-AT activation
```

This architecture means:
- **Harmine** (DYRK1A inhibitor): blocks initiating step → GSK-3β cannot phosphorylate → maximum NF-AT retention in nucleus
- **Berberine** (GSK-3β inhibitor, run_114): blocks extension step → incomplete phosphodegron → partial NF-AT activation (less severe than harmine but nonzero)

---

## Rosacea Arm: DYRK1A as Endogenous NF-AT Brake

### Pathway Diagram

```
TRPV4 trigger (warm, UV-EET, osmotic) → Ca²⁺ → calcineurin → dephospho-NFAT → nuclear
                                                                                    ↑↓ competition
                                          DYRK1A → pSer169 → GSK-3β → full phosphodegron → cytoplasmic
```

### Harmine → Worse Rosacea

Harmine (a β-carboline alkaloid found in passionflower, Syrian rue, ayahuasca) is an increasingly popular dietary supplement promoted for T1DM/diabetes management. In keratinocytes:

```
Harmine → DYRK1A inhibition → Step 1 blocked → GSK-3β cannot proceed
→ dephospho-NFAT constitutively nuclear (calcineurin still active; no longer competing)
→ NF-AT targets unrestrained: VEGF-A ↑↑, COX-2 ↑↑, IL-5 ↑↑
→ ETR flushing and telangiectasia formation amplified
→ same downstream as TRPV4 trigger but now CONSTITUTIVE (not trigger-dependent)
```

This explains a potential clinical presentation: rosacea patient starting harmine supplement experiences CHRONIC rosacea worsening even without temperature/UV triggers — NF-AT is now constitutively nuclear.

### Berberine Caveat (New Interaction with run_114)

Berberine (run_114: GSK-3β inhibitor → Foxp3 stability → Treg support + NF-κB suppression) also partially reduces the NFAT phosphodegron (Step 2 blocked):

```
Berberine → GSK-3β inhibited → partial NFAT phosphodegron → partial NF-AT nuclear retention
→ weaker NF-AT activation than harmine, but nonzero
```

Clinical significance: berberine's anti-NF-κB and Foxp3-stabilizing benefits likely dominate over the partial NF-AT effect at standard doses (500–1500 mg/day). However, in patients with very active ETR rosacea or high TRPV4 baseline (photosensitive/thermosensitive phenotype), starting berberine could produce marginal NF-AT activation → mild rosacea worsening. Monitor rosacea activity when initiating berberine.

---

## T1DM Arm: Harmine → β Cell Proliferation

### Core Mechanism

In β cells, NFAT (specifically NFAT1/NFATC1 and NFAT4/NFATC3) transcribes CyclinD1 → cell cycle G1/S entry → β cell proliferation. β cell proliferation is normally quiescent in adult human pancreas (unlike rodent β cells which proliferate readily). DYRK1A keeps β cell NFAT cytoplasmic → CyclinD1 low → quiescence.

```
Harmine → DYRK1A ↓ → NFAT nuclear → CyclinD1/CyclinD2 ↑ → CDK4/6 activation
→ β cell G1→S → proliferation (Ki67+, BrdU+ β cells detectable within 48-72h)
→ β cell mass expansion → improved insulin secretion → T1DM honeymoon extension
```

**Wang 2015 Cell**: harmine was the first compound identified to selectively stimulate human β cell proliferation (1.5–3% β cell replication rate vs ~0.1% baseline). The mechanism is DYRK1A inhibition → NFAT.

**Ackeifi 2020 Nature Metabolism**: harmine + GLP-1R agonist (GLP-1R already in framework, run_098) → synergistic β cell proliferation up to 5–6%. The GLP-1R agonist provides cAMP/PKA → reduces NFAT inactivation; harmine provides DYRK1A block — additive.

### T1DM Honeymoon Application

During T1DM honeymoon (residual β cell mass, 0–4 years post-diagnosis):
- Harmine → β cell proliferation → restore/maintain β cell mass
- Combined with GLP-1R agonist → synergistic proliferation
- Combined with existing protocol (anti-Loop 2 → reduce β cell death; calcitriol/BHB → anti-apoptotic) → three-pronged honeymoon strategy: kill death + promote survival + induce proliferation

**The conflict:** the same harmine that extends honeymoon also constitutively activates keratinocyte NF-AT → worsens ETR rosacea. This conflict does not apply to T1DM patients WITHOUT rosacea but is clinically critical for the rosacea+T1DM overlap population that this framework specifically addresses.

---

## Precision Medicine Conflict: Harmine in Rosacea+T1DM

This is the FIRST explicit supplement contraindication arising from the dual rosacea+T1DM mechanistic framework:

| Patient Type | Harmine Effect | Net Recommendation |
|---|---|---|
| T1DM without rosacea | β cell proliferation (beneficial) | May consider harmine for honeymoon |
| Rosacea without T1DM | NF-AT activation → worse ETR/PPR | Avoid harmine; avoid passionflower/Syrian rue |
| **T1DM + rosacea (this framework)** | **β cell benefit + NF-AT keratinocyte harm** | **CONTRAINDICATED; use alternatives for honeymoon** |

**Alternatives for T1DM honeymoon that do NOT activate NF-AT:**
- GLP-1R agonists (run_098) → β cell survival via cAMP/SIRT1 (no NF-AT activation)
- Calcitriol/VDR (run_031) → β cell anti-apoptotic + PTPN2/IFN-γ ↓ (run_119) (no NF-AT)
- BHB/FMD (run_037/045) → β cell anti-apoptotic + NLRP3 ↓ (no NF-AT)
- IL-37/serum IL-37 (run_118) → IL-1R/SIGIRR → anti-inflammatory (no NF-AT)
- Note: no current OTC alternative for the proliferation-inducing β cell effect specifically — GLP-1R agonist (prescription) is the best complement

---

## Kill-First Pressure Test

**Challenge 1: "Run_120 already covers NF-AT — isn't DYRK1A just a regulatory detail of run_120?"**
Fails. Run_120 covers NF-AT ACTIVATION by calcineurin (TRPV4 → Ca²⁺ → calcineurin → dephospho-NFAT → nuclear). DYRK1A is the OPPOSING kinase that sets the activation THRESHOLD — a distinct regulatory node. No amount of detail in run_120 captures DYRK1A biology: why harmine would worsen rosacea, why β cell proliferation drugs conflict with rosacea management, or the berberine/GSK-3β nuance. Not killed.

**Challenge 2: "Run_114 covers GSK-3β — doesn't it already address the NFAT phosphorylation?"**
Fails. Run_114 (berberine/GSK-3β) covers GSK-3β → Foxp3 Ser418 phosphorylation → STUB1 → Foxp3 degradation. It never mentions GSK-3β's sequential role in NFAT phosphorylation downstream of DYRK1A priming. The NFAT axis is entirely new. Not killed.

**Challenge 3: "NFAT is a broad transcription factor — all NF-AT biology isn't a gap."**
Fails. The specific mechanism — DYRK1A → sequential NFAT phosphorylation → nuclear export → NF-AT OFF — is mechanistically distinct and produces specific novel clinical guidance (harmine contraindication, berberine monitoring, honeymoon alternative strategy). Broad transcription factor coverage does not kill specific kinase-substrate mechanisms with clinical consequences. Not killed.

---

## Protocol Integration

### New Supplement Contraindication

**Harmine / Syrian rue / passionflower:** Common OTC sources of β-carboline alkaloids that inhibit DYRK1A. Increasingly found in "glucose support" and "diabetes supplements" online:
- Passionflower (Passiflora incarnata): contains harman/harmine at variable doses
- Syrian rue (Peganum harmala): high harmine/harmaline content
- Ayahuasca/caapi vine: harmine-containing; sometimes used therapeutically
- Pure harmine supplement capsules: increasingly available online with T1DM/diabetes marketing

**Rosacea+T1DM patients: AVOID harmine-containing supplements.** Flag specifically at T-index monitoring visits if patient is using these for T1DM honeymoon support.

### Berberine Monitoring Update

Existing berberine recommendation (run_114: 500–1500 mg/day for Foxp3 stability + NF-κB suppression):
- Add monitoring note: patients with very active ETR rosacea or TRPV4-dominant phenotype may experience mild NF-AT-related rosacea worsening when starting berberine
- If rosacea worsens within 2–4 weeks of berberine initiation → consider dose reduction or split dosing with longer intervals
- The benefits (Foxp3 stability, NF-κB suppression) likely outweigh the NF-AT partial activation for most patients at 500–1000 mg/day

### T1DM Honeymoon: Harmine-Excluded Stack

For T1DM+rosacea patients in honeymoon phase:
```
AVOID: harmine (DYRK1A inhibitor → NF-AT keratinocyte activation)
USE:   GLP-1R agonist (prescription) — β cell survival via cAMP; synergy with calcitriol
       Calcitriol 5000 IU/day — β cell anti-apoptotic; Treg support (runs 031/056)
       BHB/FMD — β cell anti-apoptotic; NLRP3 ↓ (runs 037/045)
       Tight glucose control — TXNIP ↓ → IL-1β ↓ → less β cell inflammasome activation
       (no NF-AT-activating compound in the rosacea-safe honeymoon stack)
```

---

## Cross-Run Connections

| Run | Connection |
|-----|------------|
| run_120 | TRPV4 → calcineurin → NF-AT (activation side); DYRK1A = opposing kinase (this run) |
| run_114 | GSK-3β → Foxp3 (run_114 mechanism); GSK-3β also extends DYRK1A-primed NFAT phosphorylation (new interaction) |
| run_098 | GLP-1R → cAMP → β cell survival; synergistic with harmine for β cell proliferation; harmine-free alternative in rosacea+T1DM |
| run_037/045 | BHB/FMD → β cell anti-apoptotic; harmine-free honeymoon components |
| run_031/056 | Calcitriol → β cell survival + Treg; harmine-free honeymoon component |
| run_123 | BACH2 FoxO1/PI3K axis; DYRK1A is distinct (NF-AT, not Treg identity) |

---

**References:**
- Wang P et al. (2015) Cell: harmine → DYRK1A inhibition → human β cell proliferation (first selective human β cell proliferator)
- Ackeifi C et al. (2020) Nature Metabolism: harmine + GLP-1R agonist → 5–6% β cell replication
- Beals CR et al. (1997) Science: GSK-3 and DYRK kinases regulate NF-AT (NFAT) nuclear export
- Gwack Y et al. (2006) J Immunol: DYRK2/GSK-3β sequential NFAT phosphorylation docking site
- Arron JR et al. (2006) Nature: DYRK1A/NFAT in Down syndrome (excess chromosome 21 DYRK1A)

---

**Framework state: 125 runs | DYRK1A NF-AT nuclear export kinase | harmine contraindication in rosacea+T1DM | GSK-3β/berberine NF-AT partial activation nuance | β cell proliferation honeymoon strategy | first supplement-class contraindication in framework.**

*Run_125 filed: 2026-04-12 | DYRK1A dual-specificity tyrosine-regulated kinase harmine NFAT NFAT1 NFAT2 NFAT4 calcineurin GSK-3β berberine sequential phosphorylation NF-AT nuclear export CRM1 β cell proliferation CyclinD1 CDK4 honeymoon rosacea NF-AT conflict Wang 2015 Cell Ackeifi 2020 Beals 1997 | run_125*
