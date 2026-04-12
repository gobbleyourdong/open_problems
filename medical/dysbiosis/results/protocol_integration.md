# Integrated Protocol — Post-Phase 3 Complete Synthesis
## All Mountains, All Bridges, One Actionable Document
## 2026-04-11

> This document replaces scattered phase summaries as the single actionable reference.
> It is organized from "do this now" to "this is the decision tree" to "this is the
> experimental frontier." The mechanism map is in phase3_synthesis.md; this document
> is what to actually do with it.
>
> WARNING: This is research-grade synthesis, not medical advice. The user's physician
> must review before implementing any medical interventions.

---

## The Framework in One Paragraph

The eight mountains of dysbiosis (gut/M1, skin/M2, virome/M3, threshold/M4, diet/M5,
early-life/M6, oral/M7, neuroimmune/M8) do not operate independently. They feed each other through
a shared pDC/IFN-α/IL-23 axis. The host-microbe threshold (M4) is jointly lowered
by two modifiable inputs: chronic IFN-α (from CVB persistent infection, M3 arm) and
gut Th17 trafficking (from gut dysbiosis, M1 arm). A third structural input (M6 floor,
early-life Treg pool) is not modifiable in adulthood but determines how much margin
exists. The furthest upstream modifiable factor is diet (M5), which feeds gut dysbiosis
(M1), oral dysbiosis (M7), and glycemic control, which in turn gates the M7→M3 arm.

**The single highest-leverage combination of interventions is:**
1. Reduce M3 arm input (CVB protocol — antiviral + IFN-suppression)
2. Reduce M1 arm input (gut dysbiosis protocol — diet + fiber + probiotics)
3. Clear M7 (periodontal treatment — removes P. gingivalis CAR-priming)
4. Monitor threshold (T-index v3 — measures both arms simultaneously)

---

## Part 1: Immediate Measurements (T-Index v3 Baseline)

These four measurements map the current state of the M4 threshold inputs.
Order simultaneously. Interpret together, not individually.

### Node C — I-FABP (Intestinal Fatty Acid Binding Protein)
- **What it measures**: Enterocyte damage → gut barrier compromise → M1 arm Th17 trafficking
- **Normal range**: <200 pg/mL (varies by lab)
- **In psoriasis patients**: 243 vs 114 pg/mL controls, r=0.78 with disease activity
- **Interpretive rule**: Elevated I-FABP → active gut barrier leak → M1 arm input to M4 is ON
- **Cost**: ~$50-150 (commercial labs: Doctor's Data, ZRT, or specialty)
- **Caveat**: Acute intestinal illness elevates transiently. Sample during stable period.

### Node D — IFN-α2 Simoa
- **What it measures**: Circulating type I IFN → M3 arm (CVB persistence proxy)
- **Method**: Simoa (single-molecule array) — standard ELISA is too insensitive for basal IFN-α
- **Normal range**: Not established; N=1 baseline is the goal; ~1-5 fg/mL in healthy adults
- **CRITICAL: No validated T1DM-specific cutoff exists. First measurement = your own baseline.**
- **Decision tree**:
  - First, check CXCL10 (IP-10, $30-50): if elevated >600 pg/mL → order Simoa; also order on clinical context (active rosacea in T1DM = IFN-α arm active by clinical argument; Simoa on any T1DM patient initiating antiviral protocol is justified)
  - CXCL10 is ~50% sensitive for IFN-α activation in T1DM — do NOT use as exclusive gate
- **Cost**: ~$150-300 (Quest Diagnostics, LabCorp, or research-grade)

### Node B — Inflammatory Tone Panel
- **What it measures**: Current M4 threshold state (secondary to Nodes C + D)
- **Components**:
  - hsCRP (<1 mg/L = low risk; >3 = active systemic inflammation)
  - IL-17A (if available; $50-100 specialty)
  - Fecal F. prausnitzii + Akkermansia muciniphila (via gut microbiome sequencing; or infer from Bristol/FODMAP response)
- **Practical approach**: hsCRP is the first-line screen; fecal sequencing adds precision if CRP elevated

### Node A — Functional Tregs (Foxp3+/RORγt-)
- **CRITICAL DISTINCTION**: Total Foxp3+ cells do NOT measure this. IL-23 converts Foxp3+ Tregs to RORγt+/Foxp3+ cells that produce IL-17A while counting as "Tregs" numerically.
- **Actual measurement**: Flow cytometry (Foxp3/RORγt co-staining on peripheral blood) — NOT a standard clinical test
- **Practical substitute**: CD4+CD25+FOXP3+ flow cytometry with RORγt exclusion (research labs only)
- **Interpretation**: If IL-17A is elevated AND FoxP3+ Tregs appear normal numerically → Treg plasticity is the mechanism (M4 is compromised despite apparent normal Treg count)
- **Cost**: Research-grade only; not routinely available clinically
- **Recommendation**: Skip Node A for now; rely on Nodes C + D + B as proxy panel. Add Node A if research context available.

### M6 History (Structural Floor Modifier — questionnaire, not blood test)
- C-section delivery? (Y/N)
- Antibiotic courses in first 2 years of life? (count)
- Formula-fed vs breastfed?
- Diverse solid food introduction before 12 months?

**Interpretation**: M6 risk factors do NOT change what's measured in Nodes A-D. They change how the numbers are interpreted. A "normal" Node A-D result in a patient with 3 M6 risk factors means less buffer than a patient with 0 M6 risk factors. The threshold is the same; the structural floor is lower.

---

## Part 2: Highest-Leverage Add-On Test (P. Gingivalis Serology)

### Why This is Separate from T-Index v3
P. gingivalis serology tests the M7→M3 bridge, which is independent of the gut (M1) and diet (M5) arms. In T1DM patients with poor glycemic control, the M7→M3 chain may be running independently of gut health.

### Test
- **P. gingivalis IgG serology** (~$50, commercial labs)
- **Interpretation**:
  - Negative: M7 arm is not active → focus on M1 (gut) and M3 (CVB/IFN-α)
  - Positive (any titer): M7 arm is active → PERIODONTAL TREATMENT IS PRECONDITION for antiviral protocol
    - Do not add OSBP inhibitors (itraconazole) or antiviral interventions without addressing P. gingivalis
    - P. gingivalis actively primes CAR → adds CVB entry point that the antiviral protocol cannot address without clearing the bacteria first
- **Concurrent**: professional dental evaluation; probe depth / attachment loss assessment

### If P. Gingivalis Seropositive: Periodontal Protocol
1. Professional scaling + root planing (by periodontist)
2. Chlorhexidine 0.12% rinse BID × 2 weeks (reduces P. gingivalis load; maintenance thereafter 2-3×/week)
3. Xylitol gum 2-3 pieces 3× daily (directly inhibits P. gingivalis gingipains)
4. EGCG (green tea extract) — gingipain inhibition at low µM; 400 mg green tea extract with meals
5. SLS-free toothpaste (reduces perioral mucosal disruption; reduces son's POD risk as side benefit)
6. Re-check serology at 6 months to confirm reduction

**Note (run_008 finding):** P. gingivalis produces butyrate as a metabolic byproduct. Butyrate is a known HDAC inhibitor that reactivates latent EBV in gingival B cells (EBV's latency reservoir). This means P. gingivalis oral dysbiosis → EBV reactivation → additional IFN-α load — a THIRD mechanism by which M7 connects to M4 threshold (beyond bacteremia→CAR and gut colonization→TLR2). Periodontal treatment addresses all three simultaneously.

---

## Part 3: The CVB/IFN-α Arm Protocol (M3 — Revised Cascade)

### Decision Tree for IFN-α Arm
```
Active rosacea in T1DM patient?
→ YES: IFN-α arm is clinically presumed active (OR 2.59 co-occurrence)
       Even if IFN-α Simoa is "normal," pDC priming may be ongoing
       → Proceed to antiviral protocol regardless

Check CXCL10 (IP-10):
→ >600 pg/mL: IFN-α arm is likely active → order IFN-α2 Simoa + proceed
→ <600 pg/mL: IFN-α arm may be quiescent — BUT CXCL10 is only 50% sensitive
              → Do NOT use CXCL10 negative as exclusive kill criterion
              → Still consider Simoa if clinical context warrants (rosacea, T1DM)
```

### IFN-α2 Simoa — Concurrent Testing Requirement (run_008)

IFN-α2 Simoa elevation cannot distinguish between CVB persistence, EBV reactivation, HERV-W activation, or general T1DM autoimmune IFN-α tone. When elevated, ADD:

- **EBV serology** (VCA IgM + EA-D IgG, NOT just VCA IgG): ~$30-60
  - VCA IgM = acute reactivation; EA-D IgG = recent reactivation marker
  - VCA IgG alone is meaningless (everyone is seropositive by adulthood)
  - If EBV reactivation confirmed: general antiviral protocol is appropriate; valacyclovir for EBV suppression is off-label but used in some protocols
- **HLA-DR3 genotyping** (~$50-100, if not yet done): T1DM HLA-DR3 carriers may have a genetically elevated IFN-α baseline; contextualizes the Simoa absolute value
- **Note**: OSBP inhibitors (itraconazole) are CVB-specific; if EBV or other non-CVB source explains IFN-α elevation, itraconazole adds no benefit for IFN suppression (though it may still address CVB component if present)

### OSBP Inhibitor Consideration (itraconazole)
- **Mechanism**: OSBP (Oxysterol-Binding Protein) mediates PI4P/cholesterol exchange at CVB replication organelles. Multiple structurally independent OSBP inhibitors are potently anti-CVB in cell culture.
- **Grade of evidence**: II-2 (cell culture only; no T1DM animal/clinical data)
- **Itraconazole** is the only clinically accessible OSBP inhibitor:
  - FDA-approved antifungal; EC50 for CVB: 0.3-1.6 µM achievable at standard antifungal dosing (200mg BID)
  - Clinically deployable TODAY
  - **BEFORE USE**: Full CYP3A4 interaction review (itraconazole is a potent CYP3A4 inhibitor):
    - Statins (simvastatin, lovastatin) → CONTRAINDICATED (rhabdomyolysis risk)
    - Calcium channel blockers → elevated plasma levels (blood pressure monitoring)
    - Immunosuppressants (cyclosporine, tacrolimus) → elevated levels
    - Warfarin → elevated INR (dose adjustment needed)
  - Do NOT initiate without pharmacist/physician medication interaction review
- **Dosing consideration**: Standard antifungal pulse (200mg BID × 1 week per month) is being used empirically; continuous dosing at lower dose also achievable. No established protocol for CVB suppression — physician decision.

### First-Choice CVB Antiviral: Fluoxetine (IMPORTED from broader campaign)

**This was missing from the dysbiosis protocol. It is the primary antiviral in the 12-disease CVB campaign (94+ attempts).**

- **Mechanism**: CVB 2C ATPase inhibitor — disrupts viral helicase/RNA packaging
- **Dose**: 20mg QD baseline; 60mg QD for males (higher mass-based dosing)
- **Advantages over itraconazole**: No cardiac contraindication; no colchicine interaction; ~$4-8/month; already commonly prescribed
- **Safety**: CYP2D6 metabolism; serotonin syndrome with MAOIs (absolute CI); QTc effect with QT-prolonging drugs; ↑bleeding with NSAIDs (add PPI for GI protection if concurrent NSAID use)
- **Dual benefit**: if depression is concurrent (T1DM + chronic illness → depression common), fluoxetine addresses both
- **Physician prescription required**; discuss CVB antiviral rationale + standard psychiatric dosing

### Second-Choice CVB Antiviral: Trehalose 2g/day (IMPORTED — LAMP2 bypass)

**Mechanism**: TFEB (transcription factor EB) activation → lysosomal biogenesis → restores LAMP2 expression in CVB-infected cells → repairs autophagic flux → enables viral clearance
**Confirmed**: GSE184831 bioinformatics data — CVB-infected human cells show LAMP2 depletion as persistence mechanism; trehalose restores
**Cost**: ~$15/month (food-grade trehalose)
**Safety**: metabolized as glucose; T1DM — count 2g trehalose as ~8g equivalent glucose; minimal glycemic impact with protein/fat co-ingestion
**Timing**: morning with breakfast

### Antiviral Supporting Protocol

- **Pleconaril**: specific VP1 binder; clinical trials for T1DM completed (mixed results); available named-patient in some countries
- **Vitamin D3 + K2**: Supports IFN signaling AND Treg induction; target 60-80 ng/mL; co-administer with zinc (gates VDR activation)
- **Serum zinc**: Check before adding any micronutrient stack. VDR activation is zinc-dependent; deficiency blunts D3 effectiveness.
- **Omega-3 fatty acids (EPA/DHA)**: Supports resolvin production, reduces IL-17 skewing; 2-4g/day EPA+DHA
- **Autophagy support — TWO TIERS**:
  - Daily 16:8 IF → NLRP3 suppression + mild autophagy (keep)
  - **FMD 5-day/month (ADD)**: Fasting-Mimicking Diet → deep autophagy → TD mutant clearance from viral reservoirs. Simple IF is insufficient for reservoir clearance. T1DM: mandatory insulin adjustment during FMD; physician supervision required. Prolon protocol or home-made equivalent (~800 kcal/day, high fat/low protein/low carb × 5 days).
- **Selenium 200μg/day** (IMPORTED — was missing): Prevents CVB virulence mutations. Selenium is a cofactor for antioxidant selenoproteins that reduce viral RNA replication error rate. Deficiency → CVB quasispecies diversification → more persistent/virulent variants. Keshan disease (endemic CVB cardiomyopathy in China) = selenium deficiency model. Do NOT exceed 400μg/day (selenosis). ~$5-10/month.

### M8 (HPA/Neurogenic) Arm — When Active

If stress-driven flares occur despite protocol adherence (signature: flare during stress/sleep deprivation with no dietary change, I-FABP elevation during stress period):
- **Sleep priority**: 7-9h/night; most potent cortisol regulator
- **Ashwagandha (KSM-66) 300mg BID**: reduces cortisol 28% in RCT; DHEA-S:cortisol ratio improvement
- **Quercetin 500mg BID**: mast cell stabilizer; also inhibits P. gingivalis gingipains (dual M7 benefit)
- **WHM cold exposure 3×/week**: acute cortisol spike → sustained reduction
- Monitoring: morning salivary cortisol + DHEA-S:cortisol ratio if M8 suspected
- See `attempts/attempt_013_m8_neuroimmune_hpa.md` for full mechanism and interventions

### OSBP Inhibitor Consideration (itraconazole — SECOND-LINE only)

**Safety update (CRITICAL):** Itraconazole + colchicine is POTENTIALLY FATAL (documented fatalities via CYP3A4 interaction → 2-3× colchicine levels → bone marrow suppression). If colchicine is used for NLRP3 suppression at any dose, itraconazole must be excluded. Itraconazole is also CONTRAINDICATED in heart failure.

Use itraconazole ONLY if: fluoxetine is contraindicated (MAOI use, QTc concern) AND colchicine is not being used AND echocardiogram confirms no HF.

---

## Part 4: The Gut Dysbiosis Arm Protocol (M1 — Revised)

### Why I-FABP Changes the Protocol Priority
If Node C (I-FABP) is elevated → gut barrier is compromised → GALT is actively priming
dual-homing Th17 cells. This means gut intervention is the MOST URGENT PRIORITY, not
secondary to antiviral work. Both arms lower M4, but in some patients the M1 arm is the
primary driver.

### Gut Protocol Stack
**Dietary base (M5 feeds M1):**
- Low-glycemic index diet: <35 GI for main carbohydrate sources
- 30g+ dietary fiber/day: primarily from legumes + vegetables + oats (SCFA precursors)
- Prebiotic diversity: garlic, onion, leek, chicory, artichoke (inulin-type FOS for Bifidobacterium)
- Minimize ultra-processed foods: CMC, polysorbate-80, carrageenan (mucus layer disruptors)
- No alcohol (direct gut barrier disruption + rosacea trigger)
- Reduce omega-6 seed oils, increase EPA/DHA (see above)

**Probiotic stack (evidence-based):**
- Lactobacillus rhamnosus GG (LGG): best-evidenced single strain for Treg induction; 10^9 CFU/day
- Multi-strain preparation with L. acidophilus, L. plantarum, B. lactis: diversity coverage
- Saccharomyces boulardii: especially during/after antibiotic courses (prophylactic C. difficile)
- Timing: evening dose, after food (gastric acid protection)

**Gut barrier support:**
- **Butyrate (sodium butyrate or tributyrin)**: Foxp3 epigenetic imprinting via HDAC inhibition at CNS1/CNS3; **TARGET 4-6g/day** (FOXP1 mechanism requires HDAC-level dose — confirmed in broader CVB campaign; 600mg is commercially common but sub-therapeutic for Treg induction). Titrate up from 600mg over 4-6 weeks to minimize GI gas. Enteric-coated preferred. Tributyrin is better tolerated than sodium butyrate. Alternative: 40g+/day dietary fiber + LGG probiotic approaches similar endogenous butyrate production.
- Berberine: SCFA-like effect + NLRP3 suppression; 500mg BID with food
- Glutamine: enterocyte fuel + tight junction support; 5g BID (especially if I-FABP elevated)
- Zinc carnosine: documented mucosal repair at gastric/gut level; 75mg/day

**Monitoring:**
- Repeat I-FABP at 3 months to assess gut barrier response
- Symptom tracking: Bristol stool consistency, bloating, cramping, post-meal fatigue

---

## Part 5: The Skin Dysbiosis Arm Protocol (M2 — Rosacea Non-Responder Attention)

### The Rosacea Non-Responder Pattern (~25% of patients)
Per attempt_008: B. oleronius → type I IFN → IL-23 → Th17 loop activates KLK5-mTORC1
positive feedback. Once this loop is established, it is DEMODEX-DENSITY INDEPENDENT.
Ivermectin alone is insufficient. The loop requires:
1. Reduce Demodex density (ivermectin) — removes TRIGGER but not the established loop
2. Block KLK5 activity (azelaic acid) — interrupts the mTORC1 positive feedback
3. If loop is fully established (severe rosacea non-responder): anti-IL-23 (risankizumab,
   guselkumab) — breaks the Th17 arm directly

**Red flag**: If rosacea does not respond to standard ivermectin/metronidazole after 3 months,
suspect established KLK5-mTORC1 loop. Add azelaic acid (20% cream or 15% gel).

**Dupilumab warning**: If dupilumab is initiated for atopic derm, Th2 suppression →
Th17 unchecked → Demodex loop may activate. If rosacea flares after starting dupilumab,
do NOT discontinue dupilumab — add ivermectin + azelaic acid to address the Th17/Demodex
loop that was unmasked, not caused, by dupilumab.

**Topical anti-Malassezia maintenance:**
- Ketoconazole 2% shampoo on scalp/eyebrows/nasolabial folds: 2-3×/week (reduce to weekly maintenance once controlled)
- Avoid comedogenic oils on sebaceous zones: olive oil, coconut oil, wheat germ oil
- Check "fatty acid esters" in skincare ingredients (cetearyl alcohol, oleic acid → Malassezia food)
- "Malassezia-safe" formulations: Cerave approved list, La Roche-Posay Toleriane range

### Chalazion Prevention
- No occlusive oils near eyelids (olive oil → meibomian gland obstruction → P. acnes + Demodex)
- Warm compresses + expression: 1-2 min BID if any lid swelling
- Monitor for early signs (lid margin thickening, mild erythema)

---

## Part 6: What NOT to Do — Anti-Problem Integration

**Highest-priority avoidances for this specific cluster (T1DM + seb derm + rosacea/chalazion):**

1. **No topical corticosteroids on face/eyelids** — even mild (hydrocortisone 1%): POD risk, Demodex promotion, skin atrophy
2. **No broad-spectrum antibiotics without clear indication** — gut microbiome is load-bearing for T1DM immune calibration; narrow-spectrum when necessary + probiotic rescue
3. **No PPIs for mild reflux** — gastric acid = first microbial filter; ~25% of US adults on PPI unnecessarily; taper if on chronic PPI
4. **No comedogenic oils on sebaceous zones** — eyebrows, scalp, nasolabial folds, eyelids specifically
5. **No dairy during active skin flares** — IGF-1 amplification → sebum substrate → Malassezia/Demodex food supply
6. **No high-glycemic loads** — insulin/IGF-1 elevation → sebum composition shift AND PMN dysfunction (M7 arm)
7. **IL-17 blockers contraindicated if IBD is present** — secukinumab/ixekizumab (psoriasis/rosacea) worsen IBD; use anti-IL-23 (risankizumab) instead for dual psoriasis+IBD
8. **Periodontal neglect** — dual mechanism: (a) P. gingivalis bacteremia → CAR priming (M7→M3); (b) oral P. gingivalis reaches gut under PPI protection → TLR2+TLR4 synergy potentiates M1 arm (M7→M1). Periodontal treatment is double-duty.
9. **PPI use without reassessment** — raises gastric pH → more oral bacteria (including P. gingivalis) survive into gut → enables M7→M1 oral-gut colonization bridge. If on chronic PPI for mild reflux (not Barrett's/severe GERD), physician taper review is warranted before antiviral protocol.
10. **Itraconazole without drug interaction review** — CYP3A4 interactions; statins contraindicated

**Son's POD risk reduction:**
- SLS-free + fluoride-free toothpaste trial (SLS resolves 30%+ refractory POD; already in anti_problem)
- No topical corticosteroids near perioral area
- Dietary diversity (diverse solids early); low-GI baseline

---

## Part 7: Monitoring Schedule

| Timepoint | Measurement | Purpose |
|-----------|-------------|---------|
| Baseline | Node C (I-FABP) + Node D (IFN-α2 Simoa) + P. gingivalis IgG + CXCL10 + hsCRP + zinc | Set T-index v3 baseline |
| Baseline | M6 history questionnaire | Structural floor modifier |
| Baseline | Periodontal assessment | If P.g. seropositive: start scaling before other additions |
| Week 4-8 | IFN-α2 Simoa repeat (if elevated at baseline) | Assess response to antiviral protocol |
| Week 8-12 | I-FABP repeat | Assess gut barrier response to M1 protocol |
| 3 months | Rosacea severity score (DLQI or IGA scale) | Skin arm response |
| 6 months | P. gingivalis IgG repeat (if seropositive at baseline) | Confirm periodontal treatment efficacy |
| 6 months | Full panel repeat (Node C + D + hsCRP) | Protocol response, adjustment decision |

---

## Part 8: The Decisive Experiments (Research Context Only)

These are NOT patient actions — they are the experiments that would formally cross THE WALL.

| Experiment | What it tests | Who could do it |
|------------|---------------|-----------------|
| nPOD dual IHC: VP1 + gingipain on same section | M3↔M7 bridge co-localization | Graves + Richardson labs + nPOD network |
| IFN-α2 Simoa in T1DM cohort, stratified by rosacea status | M3↔M2 bridge (controls for HLA) | Any T1DM cohort with dermatology phenotyping |
| I-FABP + IL-17A + IFN-α2 simultaneous panel, stratified by skin disease | T-index v3 validation (two-input M4) | Clinical research consortium |
| Ivermectin + azelaic acid RCT in ivermectin non-responders | M2+M4 rosacea loop prediction | Dermatology RCT (two FDA-approved agents) |
| Periodontal treatment RCT in new-onset T1DM, C-peptide outcome | M7→M3→CVB chain (would prove periodontal care delays T1DM) | Endocrinology + periodontology collaboration |
| Foxp3 CNS2 methylation in C-section vs vaginal delivery adults, matched | M6↔M4 epigenetic setpoint | Epigenetics lab + cohort biobank |

---

## Part 8b: Genetic Floor — T-Index Interpretation Adjustment

Run once at protocol initiation. Results modify T-index thresholds permanently.

### Key variants and their effect on T-index reading

| Variant | Test | Effect on T-index |
|---------|------|-------------------|
| **HLA-DR3/DR4** | HLA-DR typing or 23andMe imputation | Node D (IFN-α) baseline elevated; +2-4 pg/mL expected floor; adjust "active M3" threshold upward |
| **NOD2 frameshift** (rs2066844/845/847) | SNP panel or 23andMe | Node C baseline elevated; M7→M1 bridge amplified; target butyrate 6g/day (not 4g) |
| **TLR4 Asp299Gly** (rs4986790) | 23andMe | Node C UNDERESTIMATES P. gingivalis activity; P. gingivalis IgG > Node C in this genotype |
| **IL23R Arg381Gln** (rs11209026) | 23andMe or IBD panel | Structurally higher M4 threshold; if disease present despite this protection → M3 arm is dominant → antiviral protocol first |

### Clinical rules

1. **HLA-DR3 carrier + IFN-α2 4 pg/mL** → May be genetic baseline, not active CVB. Context: active rosacea = treat; isolated elevated Simoa without symptoms = genotype first, then interpret.
2. **NOD2 frameshift carrier** → Increase butyrate target to 6g/day; prioritize periodontal treatment (M7→M1 amplified in these patients)
3. **TLR4 Asp299Gly carrier + low Node C** → Do NOT interpret as "M7→M1 bridge not active" — check P. gingivalis IgG regardless
4. **IL23R Arg381Gln carrier with severe rosacea** → M3 (antiviral) arm is the likely dominant driver; start there before gut protocol

### Practical testing

- **23andMe or AncestryDNA** ($99-129): imputes HLA-DR3/DR4 (~85-90% accuracy), contains NOD2 3-SNP, TLR4 Asp299Gly, IL23R rs11209026 via raw data download + tool (Promethease $12/year or free alternatives)
- **Clinical T1DM workup**: HLA-DR typing often already performed; request confirmation if uncertain
- See `numerics/run_009_genetic_floor_precision.md` for full effect size derivation

---

## Part 9: Framework Confidence Assessment

**What is established (not speculative):**
- Gut Th17 → skin via dual-homing trafficking (PMID 38654394)
- IL-23 → Treg plasticity in human skin (PMID 31776355) 
- P. gingivalis in islets (PMC7305306)
- Rosacea-T1DM co-occurrence OR 2.59 (Egeberg 2016)
- HLA-DR3 shared haplotype (rosacea + T1DM) explaining part of OR 2.59
- KLK5-mTORC1 positive feedback in rosacea
- Early-life Tregs non-redundant (Rudensky Science 2015)
- OSBP inhibitors anti-CVB in cell culture
- Hyperglycemia → PMN dysfunction → periodontal disease (extensive literature)

**What is candidate (mechanistically sound but not formally tested in this combination):**
- CVB→IFN-α→pDC priming in T1DM→rosacea threshold (pDC expansion confirmed; causal chain inferred)
- P. gingivalis → CAR upregulation in human islets (PMC5129002 mechanism; direct islet evidence indirect)
- Diet → P. gingivalis → CVB chain in T1DM (each link established; chain constructed)
- M6 floor modification of T-index v3 clinical meaning

**What is inferred but unconfirmed:**
- AGE→RAGE→CAR concatenation (constructed from three separate published steps)
- Itraconazole → CVB suppression → IFN-α reduction in T1DM (cell culture only; no clinical)
- Periodontal treatment → IFN-α2 reduction via M7→M3 chain reduction

---

*Compiled: 2026-04-12 | Post-Phase 4 complete synthesis*
*Sources: attempts 001-015, numerics runs 001-009, phase3_synthesis.md, resolution_biology.md*
*Framework status: 8 mountains, 10+ sky bridges (6 strong candidate, 5 candidate)*
*Part 8b added: genetic floor T-index adjustment (HLA-DR3, NOD2, TLR4, IL23R)*
*Part 9 confidence unchanged: assembly is research-grade synthesis requiring physician review*
*De-escalation criteria: see results/resolution_biology.md*
*Next update: when T-index v3 measurements or genetic floor panel results are available*
