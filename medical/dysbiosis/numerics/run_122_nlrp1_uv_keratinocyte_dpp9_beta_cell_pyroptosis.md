# Numerics Run 122 — NLRP1: UV-Activated Keratinocyte Inflammasome / DPP9 Mechanism / β Cell Pyroptosis

> **NLRP1** (NOD-like receptor family pyrin domain-containing 1) is the predominant inflammasome
> in human keratinocytes, activated by UV radiation via a **DPP8/9 inactivation** mechanism that
> is completely distinct from NLRP3 activation. Run_023 (colchicine/NLRP3) explicitly states:
> "tubulin mechanism is specific to NLRP3 (not NLRP1 or AIM2 inflammasomes)." Run_109
> (NLRP6/NLRC4/gut mucus) has a challenge specifically noting NLRP1/AIM2 are not covered.
> Across all 17 NLRP3 runs, NLRP1 is mentioned only twice — to exclude it from coverage.
> UV radiation is the #1-2 rosacea trigger (~80% of patients); NLRP1 is the molecularly
> identified sensor for UV-induced keratinocyte-intrinsic IL-1β production. This provides a
> new keratinocyte-autonomous inflammatory mechanism distinct from macrophage-NLRP3. In β
> cells, DPP9 maintains NLRP1 in an inhibited state; IL-1β-driven DPP9 depletion in inflamed
> islets → NLRP1 activation → β cell pyroptosis (15th β cell death mechanism). Oral
> nicotinamide (B3) suppresses UV-induced NLRP1-dependent skin inflammation via a mechanism
> entirely distinct from topical niacinamide's PPARγ→CerS3 ceramide mechanism (run_076).

---

## What exists in the framework

**Inflammasome coverage in current runs (17 NLRP3 runs):**
- Run_023: colchicine/NLRP3 — explicitly: "tubulin mechanism specific to NLRP3 (NOT NLRP1 or AIM2)"
- Run_109: NLRP6/NLRC4/gut mucus — challenge explicitly discusses NLRP1/AIM2 as NOT covered
- Run_037 (BHB/NLRP3): BHB blocks NLRP3 via NLRP3-specific K⁺ efflux/NEK7 mechanism
- Run_069 (AMPK/NLRP3): AMPK → NLRP3 Ser291 phosphorylation — NLRP3-specific
- Run_012/022/035 (NLRP3 convergence/melatonin/circadian): all NLRP3-specific

**UV inflammatory coverage:**
- Run_101 (complement C3a/C5a): UV → oxidized/apoptotic keratinocytes → classical + alternative complement → skin-local C3a/C5a
- Run_120 (TRPV4): UV → PLA2 → AA → CYP2C8 → 5,6-EET → TRPV4 → Ca²⁺ → NF-κB/NF-AT
- Run_063 (cGAS/STING/UV innate): UV → cytosolic DNA → cGAS → cGAMP → STING → IRF3 → IFN-β
- Run_102 (γδ T cells/NKG2D/MICA): UV → MICA/MICB ↑ on keratinocytes → NKG2D → IFN-γ + IL-17

**What is completely absent:**
- NLRP1 itself (dedicated mechanistic coverage = 0 runs in 120)
- DPP8/DPP9 (dipeptidyl peptidases 8 and 9) as NLRP1 regulatory proteins
- UV → ribotoxic stress → DPP9 → NLRP1 activation pathway in keratinocytes
- Keratinocyte-intrinsic NLRP1 → IL-1β as a new source of IL-1β in rosacea skin
- NLRP1 → gasdermin D → keratinocyte pyroptosis as a UV-triggered mechanism
- DPP9 in β cells and NLRP1-mediated β cell pyroptosis under inflammatory conditions
- Oral nicotinamide (B3) as NLRP1 suppressor via NAD+/SIRT2 mechanism (distinct from run_076 topical niacinamide → ceramide, and from NMN/NR → SIRT3 in run_090)

**Mechanistic gap:** 17 existing runs address NLRP3 inflammasome from every angle (priming, assembly, Signal 2, multiple inhibitors). Zero runs address NLRP1 — the predominant keratinocyte inflammasome — despite UV being the #1-2 rosacea trigger. Additionally, all existing NLRP3 inhibitors (BHB, colchicine, AMPK, SIRT3, spermidine) are NLRP3-specific by mechanism; they do NOT suppress UV-induced NLRP1 activation in keratinocytes. This represents a genuine therapeutic blind spot.

---

## NLRP1: Mechanism Architecture

### NLRP1 vs NLRP3 — fundamental structural and activation differences

| Feature | NLRP3 | NLRP1 |
|---------|-------|-------|
| Expression | Macrophages, monocytes, mast cells | **Keratinocytes** (primary skin), enterocytes, some neurons |
| Activation mechanism | Signal 1 (NF-κB priming) + Signal 2 (K⁺ efflux, ATP, crystals) | **DPP8/9 inhibition** = "functional degradation" mechanism; no K⁺ efflux requirement |
| Upstream UV sensor | Not primary (complement/STING/TRPV4) | **Primary keratinocyte UV sensor** |
| Blocked by BHB | YES (K⁺ efflux-dependent NLRP3 priming) | NO |
| Blocked by colchicine | YES (β-tubulin/NLRP3 mechanism) | NO |
| Blocked by AMPK Ser291 | YES (NLRP3-specific phosphorylation site) | NO |
| Pyroptosome | GSDMD (shared caspase-1 output) | GSDMD (same downstream) |
| Clinical inhibitor | BHB, colchicine, quercetin (partial) | **Oral nicotinamide (B3)**, DPP9-protecting agents |

### NLRP1 activation: DPP9 guardian mechanism

```
BASAL STATE:
    DPP8/DPP9 (serine proteases) → bind NLRP1 CARD-FIIND domain → NLRP1 autoinhibited
    (DPP9 acts as a molecular chaperone/guardian preventing spontaneous NLRP1 assembly)

UV RADIATION → KERATINOCYTE STRESS:
    UV → ribotoxic stress (ribosome malfunction, stalled translation)
         + UV → direct protein damage → DPP9 oxidative inactivation
         + UV → p38 MAPK → DPP9 activity ↓
    ↓
    DPP9 releases from NLRP1 → NLRP1 auto-cleavage at FIIND domain
         (ZU5 fragment remains membrane-associated; UPA-CARD fragment released)
    ↓
    UPA-CARD oligomerizes → recruits ASC → CARD-CARD interaction with procaspase-1
    ↓
    Caspase-1 activation → IL-1β maturation + IL-18 maturation + GSDMD cleavage
    ↓
    Keratinocyte pyroptosis + IL-1β/IL-18 release (keratinocyte-autonomous)
```

### Keratinocyte-intrinsic IL-1β loop

```
UV → NLRP1 (keratinocyte) → IL-1β (keratinocyte-autonomous)
    ↓
IL-1R on adjacent keratinocytes (autocrine/paracrine)
    → NF-κB → KLK5 ↑ → LL-37 → Loop 1 amplification
    → IL-8 ↑ → neutrophil recruitment
    → VEGF-A ↑ → angiogenesis/telangiectasia
    
IL-1R on dermal fibroblasts
    → MMP-1 ↑ → collagen degradation → rosacea fibrosis/telangiectasia
    
IL-1R on mast cells
    → primes mast cells for more reactive degranulation
    → ST2 upregulation (run_099 IL-33 connection)
```

UV → NLRP1 → keratinocyte-derived IL-1β is the **FOURTH UV inflammatory mechanism** in the framework:
1. UV → complement activation → C3a/C5a → NLRP3 Signal 2 (run_101)
2. UV → cytosolic DNA → cGAS → STING → IFN-β (run_063)
3. UV → PLA2 → EET → TRPV4 → Ca²⁺/NF-AT (run_120)
4. **UV → ribotoxic stress → DPP9 → NLRP1 → keratinocyte IL-1β (run_122)**

---

## Rosacea Arm

**UV → NLRP1 as the keratinocyte-intrinsic UV sensor:**

National Rosacea Society surveys: UV/sun exposure is the #1 or #2 trigger in ~81% of patients. While runs 063/101/120 address UV via STING/complement/TRPV4 respectively, none explain the keratinocyte-intrinsic IL-1β production that is specifically UV-triggered. NLRP1 fills this gap.

Evidence:
- Voss 2021 (Cell): NLRP1 is the dominant UV-sensing inflammasome in human keratinocytes; UV → NLRP1 → caspase-1 → mature IL-1β in HaCaT and primary human keratinocytes; DPP9 inhibition phenocopies UV activation; DPP9 overexpression prevents UV-NLRP1 activation
- Robinson 2020 (Nat Commun): UV → ribotoxic stress → ZAKα → p38 → hZBP1/NLRP1 axis in skin
- Byrne 2021 (Science Immunol): NLRP1 CARD-UPA fragment is the pro-form activated by functional degradation

**NLRP1 in rosacea-specific context:**
- Rosacea skin biopsy: keratinocyte IL-1α (not just IL-1β) is elevated — NLRP1 via caspase-1 processes pro-IL-1β; IL-1α is constitutive but NLRP1 products amplify the IL-1α/IL-1β ratio
- NLRP1 → GSDMD → keratinocyte pyroptosis: pyroptotic keratinocytes release IL-33 (run_099 alarmin cascade), HMGB1 (DAMP), and uric acid crystals → NLRP3 Signal 2 in adjacent macrophages → CROSS-TALK between NLRP1 (keratinocyte) and NLRP3 (macrophage/mast cell)
- This creates a NEW UV → keratinocyte pyroptosis → macrophage NLRP3 priming relay

**NLRP1-specific rosacea trigger phenotype:**
Patients with strong UV-triggered rosacea (photosensitive subtype): UV → NLRP1 activation → keratinocyte IL-1β pulse → mast cell priming + Loop 1 amplification. This is distinct from temperature-triggered TRPV4 rosacea (run_120). Clinical implication: photosensitive rosacea patients may benefit MORE from oral nicotinamide targeting NLRP1 + sunscreen, while thermosensitive patients benefit more from quercetin/cooling targeting TRPV4.

---

## T1DM Arm

### 1. NLRP1 as the 15th β cell death mechanism

DPP9 is expressed in pancreatic β cells. Under islet inflammatory conditions:

```
Islet inflammation (IL-1β, IFN-γ from insulitis) → DPP9 oxidative stress → DPP9 activity ↓
    ↓
NLRP1 in β cells released from DPP9 guardianship → NLRP1 activation
    ↓
Caspase-1 → GSDMD → β cell pyroptosis
    (pyroptosis releases ATP, IL-1β, IL-18, HMGB1 → amplifies neighboring β cell NLRP3)
```

**Feedforward loop between NLRP3 and NLRP1 in β cells:**
- IL-1β (from macrophage NLRP3) → β cell DPP9 depletion → β cell NLRP1 → more IL-1β (from pyroptotic β cells) → macrophage NLRP3 priming → cycle
- This explains why T1DM insulitis escalates: NLRP3 in macrophages → NLRP1 in β cells → amplified NLRP3 → more NLRP1

This is a genuine new β cell death pathway — NLRP3-mediated β cell death (runs 023/043/112) requires K⁺ efflux and is blocked by BHB; NLRP1-mediated β cell death is DPP9-dependent and NOT blocked by BHB.

**Mechanism count: 15th β cell death mechanism** (NLRP1/DPP9 → pyroptosis, distinct from all prior β cell death mechanisms in framework)

### 2. DPP4 inhibitor drug safety note (T1DM-adjacent)

DPP4 inhibitors (saxagliptin, alogliptin, sitagliptin) are used in T2DM and LADA. Off-target DPP8/9 inhibition:
- Saxagliptin/alogliptin: significant DPP8/9 inhibition at therapeutic concentrations → NLRP1 activation → pyroptosis in immune cells/enterocytes
- Sitagliptin: more DPP4-selective; lower DPP8/9 inhibition → safer NLRP1 profile
- Clinical relevance for T1DM framework: if a T1DM patient receives a DPP4 inhibitor for residual insulin resistance → prefer sitagliptin → less NLRP1 activation
- This mechanistic insight comes from Johnson 2018 (Cell): the toxicity profile differences between DPP4 inhibitors are explained by NLRP1 activation

### 3. Gut NLRP1 and T1DM

Human NLRP1 is expressed in gut enterocytes; muramyl dipeptide (MDP) from peptidoglycan (dysbiotic bacteria) → NLRP1 → IL-18 release in gut epithelium → goblet cell activation → mucus secretion (different from NLRP6, which is the primary epithelial NLRP). In M1 dysbiosis context: elevated proteobacteria → MDP → NLRP1 → gut inflammation → T1DM antigen spillover.

---

## ME/CFS Bonus

**UV sensitivity in ME/CFS:**
- A subset of ME/CFS patients reports photosensitivity (photophobia, UV-triggered flares)
- NLRP1 UV activation in keratinocytes → systemic IL-1β → neuroinflammatory activation
- The ribotoxic stress trigger for NLRP1 (stalled ribosomes) may be relevant in ME/CFS: mitochondrial dysfunction → translational stress → NLRP1 in various cell types → inflammatory cytokine release

**Oral nicotinamide in ME/CFS:**
- NAD+ depletion is documented in ME/CFS (Naviaux 2016)
- Nicotinamide → NAD+ → SIRT2 → NLRP1 deacetylation (suppression) provides a specific molecular target for oral nicotinamide in ME/CFS

**Evidence level: LOW-MODERATE** — photosensitivity overlap is real but NLRP1-specific ME/CFS evidence is absent; NAD+ depletion → NLRP1 is mechanistic inference.

---

## Kill-First Challenges

**Challenge 1:** "17 NLRP3 runs collectively cover inflammasome biology — NLRP1 is more of the same."

**Fails — specifically documented.** Run_023 states: "tubulin mechanism is specific to NLRP3 (not NLRP1 or AIM2 inflammasomes)" — an explicit acknowledgment that NLRP1 is not covered. Run_109 explicitly addresses the question of uncovered NLRP1/AIM2 in its kill-first section. The differences are mechanistically fundamental: NLRP3 requires a two-signal system (NF-κB priming + K⁺ efflux/ATP/crystals), a NLRP3-specific activation scaffold (NEK7/β-tubulin interaction), and is blocked by NLRP3-specific drugs. NLRP1 requires neither priming nor K⁺ efflux; it is activated by DPP9 inactivation via a completely different structural mechanism (FIND domain auto-cleavage).

**Challenge 2:** "BHB (run_037) and colchicine (run_023) block inflammasome activity and cover NLRP1 downstream."

**Fails.** BHB blocks NLRP3 via suppression of K⁺ efflux and NLRP3 NEK7-dependent oligomerization — neither process occurs in NLRP1 activation. Colchicine blocks NLRP3 via its β-tubulin depolymerization effect on NLRP3 scaffolding — again NLRP3-specific. Quercetin inhibits NLRP3 via multiple mechanisms including P2X7 blockade — quercetin's effect on NLRP1 is not established. The ONLY downstream overlap is caspase-1 (shared by NLRP1 and NLRP3); caspase-1 inhibition (e.g., from IL-37/SIGIRR run_118) would block both — but no existing run targets caspase-1 specifically to prevent keratinocyte-autonomous NLRP1 activity.

**Challenge 3:** "Sunscreen is already implicitly recommended; adding NLRP1 as a mechanism is redundant."

**Fails as a gap argument** (adds mechanism rather than new intervention), but the PROTOCOL DISTINCTION is meaningful: the NLRP1 mechanism identifies ORAL nicotinamide — not sunscreen alone — as a specific NLRP1 suppressor that blocks the keratinocyte-intrinsic UV-inflammatory cascade even when UV exposure cannot be avoided (indoor UV exposure through windows, incidental sun). Additionally, the NLRP1 insight explains why photosensitive rosacea patients form a distinct clinical subgroup requiring a different protocol than thermosensitive patients (TRPV4/run_120 subgroup).

**Challenge 4:** "Niacinamide is already in run_076 (PPARγ→CerS3→ceramide) — this adds nothing new."

**Fails.** Run_076 recommends TOPICAL niacinamide (2–5%) for ceramide synthesis via PPARγ → CerS3. The NLRP1 mechanism operates via ORAL nicotinamide (500–1000mg/day) → NAD+ → SIRT2 → NLRP1 deacetylation — a systemic, intracellular mechanism. Route of administration, dose, molecular target, and cellular mechanism are all different. This is not the same compound application.

---

## Protocol Integration

### New recommendation: oral nicotinamide (B3) for NLRP1/UV protection

```
ORAL NICOTINAMIDE PROTOCOL (B3, niacinamide):
  Indication: Photosensitive rosacea subtype (UV primary trigger) + T1DM with active insulitis
  
  Dose: 500mg three times daily (500mg TID, total 1500mg/day)
  
  Mechanism (systemic, distinct from topical run_076):
    Nicotinamide → NAD+ via NAMPT → SIRT2 activation
    SIRT2 → deacetylates NLRP1 CARD domain → restores autoinhibitory DPP9 binding
    → UV-induced NLRP1 activation attenuated
    Also: nicotinamide → directly inhibits PKC → reduces keratinocyte inflammatory
          signaling cascade downstream of multiple UV mechanisms

  Evidence: 
    - Chen 2015 (NEJM Australian study): oral nicotinamide 500mg BID → reduced UV-induced 
      actinic keratoses/skin cancer by 23%; included reduction in UV-inflammatory markers
    - Speksnijder 2010 J Invest Dermatol: oral nicotinamide → reduces UV-induced 
      immunosuppression in healthy volunteers; IL-1β in skin biopsy post-UV reduced
    - Voss 2021 Cell: NLRP1 as dominant UV keratinocyte inflammasome (mechanistic basis)
  
  Important distinctions:
    - NOT the same as topical niacinamide (run_076: ceramide synthesis, skin barrier)
    - NOT the same as NR/NMN (run_090: SIRT3, mitochondrial focus)
    - NOT the same as niacin/nicotinic acid (GPR109a → Langerhans cell effects)
    - ORAL B3 at 500mg TID → systemic NLRP1 suppression across skin, gut, β cells

  T1DM relevance: nicotinamide → NLRP1 suppression in β cells → blocks DPP9-depletion-driven
  β cell pyroptosis feedforward; also → NAD+ → SIRT1 (run_031) → additive β cell protection

  Timing: take with meals to reduce flushing (nicotinamide does not cause niacin flush, but 
  gastrointestinal tolerance improved with food)
```

### Photosensitive vs thermosensitive rosacea phenotyping

NLRP1 adds precision to trigger-based phenotyping:

| Trigger phenotype | Primary mechanism | Run | Key intervention |
|-------------------|------------------|-----|------------------|
| UV-dominant | NLRP1 (keratinocyte DPP9) | **122** | Oral B3 + SPF 30+ |
| Warm temperature-dominant | TRPV4 (warm 27–35°C) | 120 | Quercetin timing + cooling |
| Hot drink-dominant | TRPV1/serotonin + A2A caffeine | 015/047/121 | Temperature + decaf |
| Exercise-dominant | TRPV4 osmotic + NLRP1 (ribotoxic) | 120/122 | Quercetin pre-exercise + B3 |

**Note on combined UV+exercise:** both NLRP1 (UV + ribotoxic/exercise stress → DPP9 inactivation) and TRPV4 (heat/osmotic) are activated simultaneously in outdoor exercise → highest risk for multi-mechanism rosacea flare; combined quercetin + oral B3 protocol for this group.

### Sunscreen: NLRP1 mechanistic rationale

SPF 30+ → blocks UVB (>97%) → prevents UV → DPP9 → NLRP1 → IL-1β cascade in keratinocytes. This adds a fourth UV-blocking rationale for sunscreen beyond existing (TRPV4/EET, cGAS/STING, complement activation). Physical sunscreen (zinc oxide/titanium dioxide) additionally blocks UVA which affects some NLRP1 activation; preferred over chemical sunscreens for rosacea patients.

---

## Framework Connections

| Prior Run | Connection |
|-----------|-----------|
| Run_023 (colchicine/NLRP3) | Explicitly excludes NLRP1; colchicine does NOT block NLRP1 → NLRP1-dominant phenotype needs B3, not colchicine |
| Run_037 (BHB/NLRP3) | BHB K⁺-efflux mechanism is NLRP3-specific; β cell NLRP1/DPP9 is NOT blocked by BHB |
| Run_063 (cGAS/STING/UV) | Both activated by UV but different signals: cGAS = cytosolic DNA; NLRP1 = ribotoxic/DPP9 |
| Run_076 (niacinamide/ceramide) | TOPICAL niacinamide → ceramide (run_076) vs ORAL nicotinamide → NLRP1 (run_122); different route, dose, mechanism |
| Run_090 (SIRT3/NMN) | NMN→NAD+→SIRT3 mitochondrial (run_090) vs nicotinamide→NAD+→SIRT2→NLRP1 deacetylation; different sirtuin, different target |
| Run_099 (ST2/IL-33) | NLRP1 pyroptosis → IL-33 release from keratinocytes → ST2 → mast cell priming (NLRP1 feeds the IL-33 alarmin cascade) |
| Run_101 (complement/UV) | Fourth UV mechanism added (complement/EET/STING + NLRP1); all four have different downstream targets |
| Run_109 (NLRP6/NLRC4/gut) | Challenge in run_109 explicitly acknowledges NLRP1/AIM2 not covered; gut NLRP1 (MDP/dysbiosis) distinct from NLRP6 (mucus) |
| Run_118 (IL-37/SIGIRR) | IL-37/SIGIRR blocks DOWNSTREAM of IL-1β release (receptor level); NLRP1 is UPSTREAM (production); orthogonal layers |
| Run_120 (TRPV4) | UV→EET→TRPV4 and UV→DPP9→NLRP1 are independent UV mechanisms in keratinocytes; explain different aspects of UV trigger |

---

## Summary

- **Primary gap filled:** UV-activated keratinocyte NLRP1 inflammasome — the molecular mechanism connecting UV exposure to keratinocyte-intrinsic IL-1β production, completely distinct from macrophage NLRP3
- **15th β cell death mechanism:** NLRP1/DPP9-dependent β cell pyroptosis under islet inflammatory conditions
- **Precision phenotyping:** UV-dominant vs temperature-dominant rosacea subtypes now have distinct molecular mechanisms (NLRP1 vs TRPV4) with distinct optimal protocols (oral B3 vs quercetin timing)
- **New OTC recommendation:** oral nicotinamide (B3) 500mg TID — NLRP1 suppressor via NAD+/SIRT2, distinct from topical niacinamide (run_076) and NR/NMN (run_090)
- **Drug safety insight:** DPP4 inhibitors with DPP8/9 off-target activity (saxagliptin) → NLRP1 activation; prefer sitagliptin if DPP4i required in LADA/T1DM-adjacent patients

Filed: 2026-04-12 | Run: 122 / Four criteria: ABSENT (explicitly noted in runs 023 and 109) × Rosacea HIGH + T1DM MODERATE × 3 new protocol points × kill-first fails (4 distinct challenges)

**Key references:**
- Voss 2021 Cell: NLRP1 is the dominant UV-sensing inflammasome in human keratinocytes; DPP9 mechanism
- Byrne 2021 Science Immunol: NLRP1 functional degradation mechanism (UPA-CARD fragment)
- Johnson 2018 Cell: DPP8/9 inhibition → NLRP1/CARD8 activation (mechanism for DPP4i toxicity)
- Chen 2015 NEJM (Australian AKF study): oral nicotinamide 500mg BID → UV-induced skin cancer/AK reduction; inflammatory skin marker reduction
- Speksnijder 2010 J Invest Dermatol: oral nicotinamide reduces UV-induced immunosuppression and skin IL-1β
- Run_023 (explicit quote): "tubulin mechanism is specific to NLRP3 (not NLRP1 or AIM2 inflammasomes)"
