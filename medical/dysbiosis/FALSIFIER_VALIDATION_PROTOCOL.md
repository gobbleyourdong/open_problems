# Falsifier Validation Protocol — Dysbiosis Framework v9.1

> **Purpose**: operationalize the v9.1 framework falsifier (gap.md
> 2026-04-18 LAMP2 prediction + 2026-04-20 TFEB/GDF15 sharpening)
> into a concrete clinical sampling + analysis protocol that future
> instances and clinical collaborators can execute without rebuilding
> the prediction chain from scratch.
>
> **Status**: Tier 1 framework doc per sigma v9.1 Method Mechanism
> Map (4-Tier Quality Hierarchy). Companion to `CITATION_DISCIPLINE.md`
> (Fire 88) — that doc enforces citation accuracy; this doc enforces
> falsifier-validation accuracy.
>
> **Maps to**: sigma v9.1 C5 (every principle needs a falsifier),
> v5 Convention Beats Instruction (this protocol is structural
> enforcement of the falsifier validation method), v8 Priors Don't
> Beat Source (PBMC measurement choices are source-anchored to the
> Settembre/Roczniak-Ferguson/Nakayasu primary literature).

---

## The framework prediction in falsifiable form

**Central claim** (per gap.md 2026-04-18 + 2026-04-20):

> Full-protocol engagement (CVB clearance + NLRP3 block + FMD
> autophagy + immune modulation, per `protocol_integration.md`)
> reduces systemic inflammatory load, which reduces chronic mTORC1
> hyperactivation, which de-represses TFEB, which activates the
> CLEAR network including LAMP2, with disease-direction-specific
> shifts in GDF15.

**Mechanistic chain**:

```
Protocol intervention (FMD + BHB + NMN + sulforaphane + fluoxetine
        antiviral + spermidine + multiple)
    ↓
Systemic inflammatory cytokine load ↓ (IL-6, TNF-α, IL-1β)
    ↓
Chronic mTORC1 hyperactivation ↓
    ↓
TFEB-Ser211 phosphorylation ↓ → 14-3-3 dissociation → TFEB
    nuclear translocation ↑
    ↓
CLEAR network transcription ↑ (LAMP2, LAMP1, MCOLN1, CTSD, ATG7,
    BECN1, BCL2)
    ↓
Lysosomal biogenesis ↑ + autophagy/mitophagy capacity ↑ →
    damaged mitochondria cleared → mtISR signal reduces
    ↓
GDF15 (mtISR-driven, secreted): T1DM ↑ (translation block lifts);
    ME/CFS ↓ (chronic CDR engagement reduces); skin/rosacea
    direction-uncertain
```

**Each step is independently testable** — a failure at any specific
step disambiguates which part of the framework needs revision.

---

## Biomarker panel + sampling schedule

| # | Biomarker | Sample type | Method | Predicted direction | Earliest detection | Falsifier threshold |
|---|-----------|-------------|--------|--------------------|--------------------|--------------------|
| 1 | Nuclear TFEB protein | PBMC | IHC OR nuc/cyt fractionation Western | ↑ vs baseline | Week 2-4 | < 1.3× baseline ratio at week 4 → fail |
| 2 | Cytoplasmic 14-3-3-bound TFEB | PBMC | Co-IP or PLA | ↓ vs baseline | Week 2-4 | < 0.8× baseline at week 4 → fail |
| 3 | CLEAR network panel mRNA | PBMC | qPCR or RNA-seq | All 7 ↑ co-elevated | Week 4-12 | LAMP2 ↑ alone without ≥ 4 of 6 siblings → fail (rules out alternative inducers) |
| 4 | LAMP2 protein | PBMC | Western OR flow cytometry | ↑ ≥ 1.5× baseline | Month 3-6 | < 1.5× at 6 months → fails original 2026-04-18 falsifier |
| 5 | Serum GDF15 | Plasma/serum | ELISA (Roche or R&D) | T1DM: ↑ as inflammation ↓; ME/CFS: ↓ as CDR ↓; Skin: → / ↑ disease-context | Month 3-6 | Disease-direction failure → revise mtISR-axis subpredictions |
| 6 | Serum IL-6, TNF-α, IL-1β | Plasma | Multiplex panel | ↓ (the upstream driver) | Month 1-3 | No reduction → upstream chain breaks before mTORC1 |
| 7 | C-peptide (T1DM only) | Serum | Standard | preservation > 25% above placebo at 12 months | Month 6-12 | Failure → run_171 GDF15 protein-supplementation indication moot |
| 8 | Bell scale + DSQ-PEM (ME/CFS only) | Patient-reported | Validated questionnaires | improvement | Month 3-6 | No improvement → biomarker-clinical disconnect, framework needs subsetting |

**Sampling schedule**:

- **Pre-protocol baseline**: all 8 biomarkers, plus full inflammatory
  cytokine panel (CRP, ESR, ferritin) for context
- **Week 2**: biomarkers 1, 2 (early TFEB signal)
- **Week 4**: biomarkers 1, 2, 3, 6 (TFEB + CLEAR network onset +
  upstream cytokines)
- **Month 3**: biomarkers 1-7 (full panel except disease-specific
  clinical endpoints)
- **Month 6**: full panel including C-peptide (T1DM) or PEM (ME/CFS)
- **Month 12**: full panel + clinical endpoints

**Sample volume**: standard PBMC isolation requires ~16-20mL whole
blood (CPT tube or Ficoll). Serum requires 2-3mL. Total per visit:
~20-25mL. Compatible with standard outpatient clinical lab capacity.

---

## Statistical thresholds + interpretation

**Primary endpoint**: PBMC LAMP2 protein ↑ ≥ 1.5× baseline at
month 6 (matches original 2026-04-18 falsifier).

**Mechanism-validation co-primary**:
- Nuclear TFEB protein ↑ ≥ 1.3× baseline at week 4
- ≥ 4 of 6 CLEAR-network siblings co-elevated with LAMP2 at month 3

**Disease-direction sub-endpoints**:
- T1DM: serum GDF15 trajectory (rise predicts inflammatory translation
  block lifting); C-peptide preservation
- ME/CFS: serum GDF15 reduction (CDR engagement reducing); Bell scale
  improvement; PEM resolution kinetics correlation

**Failure-mode disambiguation matrix**:

| What fails | Which framework component is revised |
|------------|---------------------------------------|
| Upstream cytokines don't drop | Protocol's anti-inflammatory arms not engaging in this patient — revise protocol selection, not framework |
| Cytokines drop but nuclear TFEB doesn't rise | mTORC1-TFEB-Ser211 axis broken in this patient (FLCN-Ragulator dysfunction, calcineurin block) — alternative TFEB-suppression mechanism present |
| TFEB rises but CLEAR network doesn't | Co-factor deficit (TFEB-co-activators, chromatin accessibility), epigenetic block — revise CLEAR-network framing |
| CLEAR network rises but LAMP2 protein doesn't | Translation block at LAMP2 specifically (analog of GDF15 translation block in T1DM islets) — mechanism-level finding, framework partially intact |
| Everything rises but clinical endpoints don't move | Biomarker-clinical disconnect — framework biomarkers track substrate state, not clinical phenotype — major revision needed |
| Disease-direction GDF15 wrong | Disease-specific subprediction (run_171) wrong, but T1DM-vs-ME/CFS direction-opposite framing valuable to revise |

---

## Safety nuances (per CITATION_DISCIPLINE Pasquier 2023 finding)

**Critical caveat for protocol design**: per Pasquier & Pastore et al.
2023 *EMBO J* PMID 37712288, **chronic TFEB activation suppresses
insulin gene expression** in β cells under nutrient deprivation as a
starvation-adaptive program. This means:

1. **Cyclic > continuous**: intermittent TFEB activators (FMD pulses,
   time-restricted feeding cycles) likely safer than continuous
   TFEB-driver exposure (chronic rapamycin, sustained spermidine
   high-dose). Validation protocol should distinguish patients on
   cyclic vs continuous protocols.
2. **β-cell-specific monitoring**: T1DM patients with significant
   residual β-cell function should be monitored for insulin output
   reduction during sustained TFEB-activator exposure. C-peptide
   should be measured monthly during initial 6-month protocol period.
3. **Withdrawal vs continuation**: if TFEB-axis biomarkers rise but
   C-peptide DROPS, the protocol may be over-driving TFEB. Switch
   to cyclic-pulse design rather than abandoning intervention.
4. **ME/CFS may tolerate more sustained activation**: since β-cell
   insulin-suppression is the primary safety concern and ME/CFS
   patients without T1DM don't have this constraint, ME/CFS may be
   the cleanest population for testing more sustained TFEB-activation
   protocols.

---

## Cross-disease cohort design

**Three-disease minimum** (per gap.md 2026-04-18 falsifier specification):
T1DM + ME/CFS + dilated cardiomyopathy (or another CVB-family disease).

**Sample size calculation** (back-of-envelope):
- Effect size assumption: 1.5× LAMP2 elevation, σ ≈ 0.4× baseline
- α = 0.05, β = 0.20 (80% power)
- Per-disease arm: ~16-20 patients
- Three-disease design: ~50-60 patients total
- Add control arm (un-engaged patients on standard care): +20-30
- **Estimated total**: ~75-90 patients across 4 arms

**Stratification variables**:
- Genotype: HLA, PTPN22, IFIH1 (T1DM) — affects baseline inflammation
- Disease duration (recent vs chronic)
- Concurrent medications (especially mTOR-affecting: metformin,
  rapamycin, steroid use)
- Cyclic vs continuous protocol exposure (per Pasquier 2023 nuance)

---

## How this protocol differs from standard clinical-trial designs

Standard biomarker validation trials measure **one biomarker against
one clinical endpoint**. This protocol measures **a mechanistic chain
of biomarkers (1→2→3→4) against multiple disease-specific clinical
endpoints**.

The mechanistic-chain design is intentional per sigma v9.1: a
phenomenological prediction ("LAMP2 rises") can fail without
disambiguating which mechanism is wrong. A mechanism-grounded
prediction with a chain ("TFEB → CLEAR network → LAMP2 → mitophagy
→ disease state") fails AT a specific step that points to which
framework component needs revision.

This is the same logic as the v9.1 Lean backbone discipline applied
to clinical biomarker validation: each link in the chain is
independently falsifiable, so failure is informative, not catastrophic.

---

## Validation status (as of 2026-04-20)

**Pre-validation**: zero patients enrolled. The protocol is currently
in the framework-prediction phase. The biomarker panel and analysis
plan are pre-registered here as a **frozen specification** so that
any future clinical validation can be compared to what the framework
predicted before the data was collected (per sigma v9.1 D1 replication
tier — single-operator framework prediction is currently Tier 2 with
"same-operator" flag).

**For Tier 3 promotion**: independent operator (clinical research
group) running this protocol on a cohort and reporting results
without prior framework involvement.

**Patient n=1 status** (per `medical/dysbiosis/results/
patient_zero_actionability_2026-04-14.md` referenced in memory):
the patient-zero cohort frozen since 2026-04-09 should have this
biomarker panel added to its lab order sheet. If patient-zero does
the protocol with this panel measured, that's a single-patient
informal preliminary validation (not a clinical trial, but anchors
the framework prediction in actual data).

---

## Cross-references

- `gap.md` 2026-04-18 + 2026-04-20 — falsifier prose specification
- `CITATION_DISCIPLINE.md` (Fire 88) — companion structural-enforcement
  doc for citation accuracy
- `VERIFIED_REFS.md` (Fires 78-90) — PMID-anchored top-20 references
  including Naviaux 2016 PMID 27573827 (CDR foundation)
- `numerics/run_171_gdf15_*.md` — GDF15 mechanism + disease-direction
  predictions
- `numerics/run_172_tfeb_*.md` — TFEB CLEAR network + Pasquier 2023
  nuance
- `medical/t1dm/THEWALL.md` (Fire 13 cross-refs) — T1DM-specific
  GDF15/TFEB integration
- `medical/me_cfs/THEWALL.md` (Fire 14 cross-refs) — ME/CFS-specific
  GDF15/TFEB integration with opposite-direction predictions
- `protocol_integration.md` — clinical protocol; this falsifier
  panel should be added to its monitoring section
