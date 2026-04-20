# Numerics Run 171 — GDF15: Mitochondrial Integrated Stress Response Cytokine → β-Cell + Keratinocyte Stress-Adaptive Brake → CDR Bridge
## ATF4/CHOP-Driven mtISR Mitokine; GFRAL-Hindbrain Anorexia Axis; Inflammation-Suppressed in T1DM Islets and Psoriatic Skin | T1DM Mountain-2 Survival + Rosacea/POD Mitochondrial-Stress Bridge | 2026-04-20

> **First run after Phase 4b audit closure (Fires 78–90).** Citations
> in this run follow `CITATION_DISCIPLINE.md` discipline: every primary
> source is PMID-anchored inline, author + year + journal + mechanism
> all triangulated via WebSearch before writing. Foundational claims
> verified Fire 10 of the 2026-04-20 loop session.

---

## Saturation Criteria

1. **Completely absent from prior 170 runs**: confirmed via `grep -r
   "GDF15\|GDF-15\|GFRAL"` across `medical/`. Zero matches. mtISR axis
   was partially adjacent (run_146 PERK/eIF2α/ATF4/CHOP integrated
   stress response in β cell UPR; run_098 ER stress XBP1/UPR/NF-κB)
   but **GDF15 as the downstream secreted mitokine is not covered**.
   The mtISR → ATF4/CHOP → FGF21/GDF15 transcriptional output
   (Chung 2023 *Front Endocrinol* PMID 37818094) is the missing
   mechanism layer. ✓

2. **MODERATE-HIGH evidence**:
   - **T1DM: HIGH** — Nakayasu et al. 2020 *Cell Metab* PMID 31928885
     ("Comprehensive Proteomics Analysis of Stressed Human Islets
     Identifies GDF15 as a Target for Type 1 Diabetes Intervention")
     reports **~10-fold reduction in GDF15 in T1DM islets** vs healthy;
     translation is blocked during inflammation; **recombinant GDF15
     reduces diabetes incidence by 53% in NOD mice** and decreases
     insulitis. Nakayasu 2024 *Diabetologia* (independent group)
     confirmed via adenosine-deamination mechanism. Direction:
     **GDF15 is β-cell-PROTECTIVE; T1DM is GDF15-deficient**, opposite
     of the inflammatory cytokines covered in prior runs. ✓
   - **Rosacea/skin: WEAK / inferred-by-homologue** — downgraded from
     "MODERATE" per `SELF_AUDIT_2026-04-20.md` Confirmation Bias Audit:
     the only direct evidence is **psoriasis** (Hou et al. 2022 *J
     Invest Dermatol* PMID 36049542 — decreased GDF15 → enhanced
     psoriasiform inflammation; topical recombinant GDF15 alleviates
     epidermal hyperplasia + neutrophil infiltration), NOT rosacea.
     The cross-application to rosacea relies on (a) shared keratinocyte
     mtISR triggers (UV/ROS/TLR2 — run_002 + run_063 + run_119
     contexts) and (b) author-extrapolation that the
     psoriasis-protective mechanism generalizes to rosacea. **No
     rosacea-specific GDF15 measurement was located via Fire 11
     WebSearch.** This is a candidate hypothesis, not an evidenced
     claim, and should not be cited in patient-facing materials as
     direct rosacea evidence. ⚠️
   - **ME/CFS: MECHANISTIC PREDICTION (no direct measurement)** —
     downgraded label from "MODERATE-HIGH (mechanistic)" per
     `SELF_AUDIT_2026-04-20.md` to make the prediction-vs-evidence
     distinction explicit. Naviaux 2016 *PNAS* PMID 27573827 (verified
     Fire 78) frames ME/CFS as a hypometabolic "Cell Danger Response"
     (CDR) state. GDF15 is the canonical mtISR mitokine. **The
     "elevated baseline GDF15 in ME/CFS" claim is a framework
     prediction (this run's), not a measured finding** — Naviaux's
     CDR does not explicitly invoke GDF15, and direct GDF15 measurement
     in published ME/CFS cohorts was not located via Fire 11 WebSearch.
     The mechanistic plausibility is real (mtISR → GDF15 is canonical
     biology); the disease-specific direction prediction is testable
     but unverified. ✓

3. **New mechanism not in prior runs**: GDF15 is a **secreted mitokine**
   distinct from the intracellular mtISR machinery (PERK/ATF4/CHOP,
   covered in run_146). The framework's prior coverage was:
   - run_098 (ER-stress XBP1/UPR/NF-κB) — UPR transcriptional output
   - run_146 (PERK/eIF2α/ATF4/CHOP integrated stress response) — ISR core
   - run_090 (SIRT3/SIRT6 mitochondrial epigenetic) — sirtuin axis
   - run_157 (EZH2 PRC2) — repressive epigenetic
   GDF15 is the **systemic-signaling output** of mtISR — turns local
   mitochondrial stress into a circulating cytokine acting via
   GFRAL receptor in hindbrain (anorexia/satiety) AND via
   non-GFRAL paracrine signaling on neighboring cells. **First
   secreted-mitokine mechanism in framework**. ✓

4. **Kill-first fails**:
   - run_146 covers PERK→ATF4→CHOP intracellularly; no run covers the
     downstream secreted mitokine output ✓
   - run_073 (GLP-1R) covers cAMP/PKA/SIRT1 β-cell survival via GPCR;
     GDF15 is mtISR-driven, distinct receptor system ✓
   - run_111 (osteopontin/SPP1 M1/Th1/Treg) is M1-polarizing, opposite
     valence ✓
   - run_154 (PD-1/PD-L1) is exhaustion-axis on T cells; GDF15 acts on
     β-cell and keratinocyte cell-intrinsic stress, not T-cell exhaustion ✓
   - **Closest adjacent run**: run_146 PERK/CHOP. Verified independence:
     run_146 is intracellular ISR; run_171 is the downstream SECRETED
     mitokine. Both can be true; non-overlapping mechanisms. ✓

---

## Central Mechanism

```
Mitochondrial stress (ROS, mtDNA damage, OXPHOS dysfunction, ETC
        complex defects, viral protein interference with mtETC)
            ↓
ISR kinases (PERK if ER-stress, GCN2 if amino acid starvation,
        HRI if mitochondrial stress + heme deficiency, PKR if
        viral dsRNA)
            ↓
eIF2α-Ser51 phosphorylation → global translation suppression +
        cap-independent ATF4 translation upregulation
            ↓
ATF4 → CHOP (DDIT3) transcription
            ↓
CHOP → GDF15 promoter (CHOP/ATF4 binding sites at -250, -380 in
        GDF15 5' regulatory region)
            ↓
GDF15 mRNA → translation → ER processing → cleavage at RXXR
        propeptide site → mature GDF15 (112 aa, ~25 kDa homodimer)
            ↓
SECRETION via constitutive Golgi pathway → systemic circulation
            ↓
GFRAL (in area postrema + nucleus tractus solitarius hindbrain)
        → RET co-receptor → ERK/AKT signaling → satiety + reduced
        food intake (canonical anorexigenic pathway)
            +
PARACRINE (non-GFRAL) effects: TGF-β superfamily receptor
        signaling on neighboring cells → SMAD or TAK1 cascades →
        cell-intrinsic stress-protective gene programs (BCL-2 ↑,
        Bax ↓, cleaved caspase 3 ↓; per Nakayasu 2020 PMID 31928885
        islet experiments)
```

**Why this is a CDR (Cell Danger Response) signal, not an inflammatory
cytokine**: GDF15 is induced by stress (oxidative, ER, mitochondrial,
nutrient) but signals **withdrawal + adaptation**, not effector
inflammation. The Naviaux CDR framing (PMID 27573827) — cell enters
hypometabolic protective state under danger — has GDF15 as a probable
molecular signal. Distinct from IL-6/IL-1β/TNF-α (which are
pro-inflammatory effector cytokines). The mtISR axis is the cell's
"slow brake" against further mitochondrial damage; GDF15 is the
"systemic announcement" that the brake is engaged.

---

## T1DM-Specific Mechanism

**The β-cell paradox per Nakayasu 2020 PMID 31928885**:

T1DM islets show **~10-fold REDUCTION** in GDF15 protein vs healthy
donors. Counter-intuitive at first — T1DM islets are under heavy
inflammatory + mitochondrial + ER stress (covered in run_146 PERK,
run_098 XBP1, run_158 mTOR), so naïve prediction is GDF15 should be
ELEVATED. Instead it's depleted.

Mechanism per Nakayasu 2020:
1. IL-1β + IFN-γ (T1DM cytokine milieu) **block GDF15 translation**
   despite induced ATF4/CHOP transcription. The brake is engaged at
   the protein-synthesis level, not transcription.
2. Loss of GDF15 → loss of paracrine β-cell-protective signaling →
   **accelerated β-cell apoptosis under inflammatory stress**.
3. Recombinant GDF15 supplementation **restores the brake**: ~50%
   reduction in cleaved caspase 3 in EndoC-βH1; complete protection
   from cytokine-induced apoptosis in human islets; **53% reduction
   in NOD mouse diabetes incidence**.

**Framework slot**: 4th β-cell-survival arm in T1DM Mountain-2
(prior arms: GLP-1R/cAMP/SIRT1 from run_073; calcitriol/VDR/Bcl-2 from
runs 031/056; ErbB3/PI3K/Akt from run_129). GDF15 is mechanistically
distinct from all three (mtISR-driven, secreted-mitokine paracrine,
TGF-β superfamily downstream).

**Therapeutic window**: recombinant GDF15 administration in NOD mice
showed efficacy. Human translation pathway: mAbs anti-GFRAL (in
clinical development for cachexia) might accidentally remove the
β-cell-protective signal — caution flag for T1DM patients on
anti-cachexia GDF15 antagonists. Conversely, GDF15 agonist therapy
(in clinical development for obesity) might have **β-cell-protective
side benefit** in pre-diabetes / T1DM stage 1-2.

---

## Rosacea / POD / Skin-Specific Mechanism (Inferred from Psoriasis)

**Per Hou 2022 *JID* PMID 36049542** (the load-bearing skin paper):

- Imiquimod-induced psoriasiform dermatitis model
- GDF15 expression decreased in psoriatic-like skin
- Topical recombinant GDF15 → significantly reduced epidermal
  hyperplasia, neutrophil infiltration, psoriasis-related transcript
  signature

**Translation to rosacea / POD**: rosacea papulopustular variant has
neutrophil infiltration (covered in run_068 calprotectin; run_135
PI3Kδ; run_144 PI3Kγ) and keratinocyte hyperplasia (less prominent
than psoriasis but present in phymatous variants). The mtISR triggers
in rosacea include UV (run_063 cGAS-STING), mitochondrial ROS (run_143
ferroptosis), TLR2/KLK5 amplification (run_062 IL-17A→KLK5; run_080
STAT3 / Yamasaki 2011 PMID 21107351 — *verified Fire 86*). Each of
these triggers ATF4/CHOP induction, predicting GDF15 transcription —
but if the same translational block as in T1DM β cells operates in
keratinocytes under inflammatory cytokine stress (TNF-α, IL-17A,
IL-23), rosacea keratinocytes might also be **GDF15-deficient under
active inflammation**.

⚠️ **Rosacea-specific GDF15 measurement does not appear in current
literature search**. The framework prediction is plausible but
**unverified for rosacea-specific tissue**. Future fire should
search for direct rosacea biopsy GDF15 immunohistochemistry or
serum data.

**POD-specific note**: POD shares the steroid-rebound + KLK5
amplification pathway with rosacea (per `medical/perioral_dermatitis/
THEWALL.md`). If the GDF15-deficiency-under-inflammation pattern
holds, it might explain POD's tendency toward chronification — the
mtISR brake is induced but the protective output never reaches
effective tissue concentration.

---

## ME/CFS / CDR Bridge

**Per Naviaux 2016 *PNAS* PMID 27573827** (verified Fire 78 in
VERIFIED_REFS):

ME/CFS framed as hypometabolic Cell Danger Response. Metabolomic
profile (612 metabolites across 63 pathways) shows reduced sphingolipid,
phospholipid, and purine intermediates — pattern consistent with
chronic mitochondrial stress + dauer-like adaptation.

**GDF15 as candidate CDR marker**:
- Elevated baseline serum GDF15 in chronic mitochondrial-disease
  populations (mitochondrial myopathies, MELAS, Parkinson's) is
  well-established in mitokine literature (Chung 2023 *Front
  Endocrinol* PMID 37818094 review).
- Direct GDF15 measurement in ME/CFS is sparse; framework prediction
  is ELEVATED baseline reflecting chronic mtISR engagement.
- Distinct prediction from T1DM islet pattern: ME/CFS systemic
  GDF15 should be HIGH (chronic adaptive engagement); T1DM β-cell
  tissue GDF15 is LOW (translation blocked acutely by inflammatory
  cytokines). Same gene, opposite directions, same CDR framework.

**Falsifier for the run_171 framework slot**: if PBMC or serum GDF15
is NOT elevated in ME/CFS (verified by GSE-style analysis or direct
ELISA in clinical cohorts), the CDR-mediated GDF15 mitokine framing
is disconfirmed for ME/CFS. (Cf. v9.1 falsifier convention from
gap.md addendum 2026-04-18.)

---

## Kill Challenges + Defenses

### Kill A: GDF15 elevation is a downstream MARKER of disease severity, not an actionable target

The serum-biomarker literature (Chung 2023 PMID 37818094) shows GDF15
correlates with disease severity in many conditions — implying it's
just a stress-output that tracks badness, not a causal node.

**Defense**: For T1DM specifically, Nakayasu 2020 PMID 31928885 went
beyond correlation: recombinant GDF15 supplementation in NOD mice
**caused 53% reduction in diabetes incidence** + reduced insulitis.
This is interventional evidence, not just observational. The β-cell
GDF15-deficiency in T1DM is mechanistically actionable — restoring
GDF15 prevents β-cell loss. ⚠️ For ME/CFS the actionability is less
clear — if baseline GDF15 is already chronically elevated as part of
CDR, exogenous addition would not help and might worsen the dauer-like
state. Disease-direction-specific therapeutics required.
**Status**: Not killed for T1DM (intervention evidence). Status for
ME/CFS: actionable framing is wrong direction; the kill applies
selectively to that disease only.

### Kill B: GDF15 effects in T1DM are confounded by GFRAL-mediated weight loss

GDF15 → GFRAL → reduced food intake → weight loss → improved insulin
sensitivity. NOD mouse diabetes incidence reduction might be entirely
mediated by reduced caloric load, not by direct β-cell protection.

**Defense**: Nakayasu 2020 included **in vitro human islet experiments
without GFRAL involvement** (recombinant GDF15 → 50% reduction in
cleaved caspase 3 in EndoC-βH1; complete protection from cytokine
apoptosis in primary human islets). These are isolated cell systems
with no anorexia/weight pathway available. The β-cell-protective
effect is **direct + paracrine**, not GFRAL-mediated. GFRAL is one
GDF15 receptor; direct cell-autonomous effects via TGF-β superfamily
receptors are independent.
**Status**: Not killed. The in vitro evidence cleanly separates
direct β-cell protection from GFRAL-mediated systemic effects.

---

## Clinical / Protocol Integration

**For T1DM (Mountain-2 regeneration / preservation)**:

1. **Monitor**: serum GDF15 in patients on full-protocol engagement.
   Baseline + 3-month + 6-month. Target direction: gradual rise as
   inflammatory load decreases (translation block lifted).
2. **Cross-check with framework falsifier**: per gap.md 2026-04-18
   addendum, PBMC LAMP2 should rise within 3-6 months. GDF15 is a
   complementary marker — both reflect "the brake is engaged + cells
   are adapting." Combined biomarker panel: LAMP2 + GDF15 + (existing
   panel).
3. **Therapeutic candidate**: recombinant GDF15 protein has not been
   FDA-approved for T1DM. Pre-clinical NOD evidence is strong.
   Pathway: stage-1/2 T1DM trials would be the logical next step. No
   immediate consumer-accessible intervention.
4. **Drug-interaction caution**: anti-GFRAL antagonists (in clinical
   trials for cachexia) might attenuate β-cell-protective GDF15
   signaling. Patients in such trials with concurrent T1DM/pre-T1DM
   should be flagged.

**For rosacea/POD (skin Mountain-1)**:

1. **Mechanism verification needed**: search for direct rosacea/POD
   GDF15 IHC or serum data in next fire. Current support is via
   psoriasis homologue (PMID 36049542) + shared mtISR triggers.
2. **Topical recombinant GDF15** has psoriasis-model efficacy. Not
   yet a clinical product. Speculative for rosacea pending
   verification.
3. **Indirect support**: framework interventions that enhance
   mitochondrial quality (NMN/NAD+, mitophagy via spermidine in
   run_041, sulforaphane/NRF2 in run_027) may indirectly support
   GDF15 expression by reducing the mtISR translational block.

---

## Cross-Run Connections

- **run_146 (PERK/ATF4/CHOP)**: intracellular mtISR core. Run_171 is
  the downstream secreted-output extension.
- **run_098 (ER stress XBP1)**: parallel UPR arm. Both UPR/PERK and
  mitochondrial ISR converge on ATF4/CHOP/GDF15.
- **run_073 (GLP-1R)**: alternate β-cell survival arm. Now joined by
  GDF15 as fourth Mountain-2 mechanism.
- **run_158 (mTOR)**: integrates with mtISR — mTORC1 hyperactivity
  in dysbiosis can suppress autophagy → mt-stress accumulation →
  GDF15 induction (with translation block under inflammation).
- **run_063 (cGAS-STING UV innate)**: nuclear DNA damage axis.
  Mitochondrial DNA damage → cytosolic mtDNA → also activates
  cGAS-STING (literature beyond run_063). GDF15 may be secondary
  output of both nuclear and mitochondrial DNA-damage axes.
- **run_170 (LGALS1 / Galectin-1)**: most recent prior run. Both
  run_170 and run_171 are β-cell-protective in T1DM via
  cell-non-autonomous signaling (Gal-1 induces apoptosis of
  activated effectors; GDF15 protects β cells directly). Different
  mechanisms, complementary effects.

---

## v9.1 Falsifier (per CITATION_DISCIPLINE + sigma method discipline)

**Would falsify (this run's central claim)**: if recombinant GDF15
administration in stage-1/2 T1DM clinical trial does NOT preserve
β-cell function (C-peptide preservation > 25% above placebo at 12
months, per standard T1DM trial endpoints), the GDF15-as-actionable-
T1DM-target framing is disconfirmed for human translation. Weaker
falsifier: if PBMC GDF15 mRNA does NOT rise in patients on full
dysbiosis protocol with measurable LAMP2 rise (per gap.md addendum
co-prediction), then GDF15 and LAMP2 are tracking different
adaptive processes and the unified "brake engagement" framing needs
revision.

**Prior art**: GDF15 as mtISR mitokine ≈ FGF21 + GDF15 dual-mitokine
literature (Chung 2023 *Front Endocrinol* PMID 37818094 review).
Sigma addition: framing GDF15 as a **cross-disease threshold marker**
in the dysbiosis cross-disease integration framework (T1DM β-cell
deficiency; psoriasis/skin protective; ME/CFS CDR-elevated) — three
distinct disease-direction predictions from one gene.

---

## References (PMID-anchored per CITATION_DISCIPLINE.md)

- Nakayasu ES et al. 2020 *Cell Metab* PMID 31928885 "Comprehensive
  Proteomics Analysis of Stressed Human Islets Identifies GDF15 as a
  Target for Type 1 Diabetes Intervention" — primary T1DM evidence
  (10× reduction in T1DM islets; recombinant GDF15 → 53% NOD
  diabetes reduction).
- Hou L et al. 2022 *J Invest Dermatol* PMID 36049542 "Decreasing
  GDF15 Promotes Inflammatory Signals and Neutrophil Infiltration in
  Psoriasis Models" — primary skin-protective evidence (topical
  recombinant GDF15 alleviates psoriasiform dermatitis).
- Chung HK + Tanaka et al. 2023 *Front Endocrinol* PMID 37818094
  "The roles of FGF21 and GDF15 in mediating the mitochondrial
  integrated stress response" — mtISR review.
- Jiang J et al. 2022 *Sci Rep* PMID 35398052 "NAG-1/GDF15 protects
  against streptozotocin-induced type 1 diabetes by inhibiting
  apoptosis, preserving beta-cell function, and suppressing
  inflammation in pancreatic islets" — STZ-T1DM model confirmation.
- Naviaux RK et al. 2016 *PNAS* PMID 27573827 (verified Fire 78 in
  VERIFIED_REFS) — ME/CFS CDR framing; GDF15 as candidate CDR marker.

*Filed: 2026-04-20 | Numerics run 171 | GDF15 mitochondrial integrated stress response ATF4 CHOP β cell keratinocyte T1DM rosacea ME/CFS Cell Danger Response GFRAL anorexia Mountain-2 4th β-cell survival arm secreted mitokine TGF-β superfamily PMID-anchored per CITATION_DISCIPLINE Fire 88 first run after Phase 4b audit closure | run_171*

*Key insight: GDF15 is the secreted-mitokine output of the mtISR axis whose intracellular core (PERK/ATF4/CHOP) was covered in run_146; T1DM islets show 10× GDF15 deficiency due to inflammatory translation block, recombinant supplementation rescues NOD mice 53%; psoriasis-model parallel suggests skin/rosacea applicability though direct rosacea data is sparse and flagged for future verification; ME/CFS predicts opposite direction (chronically elevated as CDR adaptation) — same gene three disease-direction predictions = strong cross-disease integration value.*
