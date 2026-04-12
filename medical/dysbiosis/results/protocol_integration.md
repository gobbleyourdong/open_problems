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
- **Butyrate — REVISED DELIVERY PROTOCOL (run_032):** Foxp3 epigenetic imprinting via HDAC inhibition at CNS1/CNS3. Oral sodium butyrate 4-6g/day delivers only 15-25% to colon (the target site); the rest is absorbed in small intestine. **Revised approach provides 3-4× more colonic exposure:**
  - **Phase 1 (Weeks 0-8):** Microencapsulated/enteric-coated butyrate 2-3g/day (60-80% colonic delivery) PLUS tributyrin 3g/day (40-60% colonic, no odor — better compliance). Combined effective colonic dose ≈ 8-10g/day unprotected equivalent.
  - **Phase 2 (Weeks 8+):** Add resistant starch (raw potato starch, uncooked, Bob's Red Mill) starting 5g/day → increase to 20-30g/day over 4 weeks. Ferments to butyrate in situ (100% colonic). Requires F. prausnitzii present — Phase 1 butyrate feeds F. prausnitzii → enables Phase 2.
  - **Long-term:** Resistant starch 20-30g/day (endogenous) + tributyrin 1-2g/day (supplementary). Colonic-targeted; sustainable; lower cost than high-dose sodium butyrate.
  - **VDR synergy:** GALT Treg VDR upregulation requires colonic butyrate; colonic-targeted delivery improves the butyrate × vitamin D synergy (run_018) by 2-4× vs. unprotected sodium butyrate.
  - See `numerics/run_032_butyrate_delivery.md`.
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
| Baseline | Node C (I-FABP) + Node D (IFN-α2 Simoa) + P. gingivalis IgG + CXCL10 + hsCRP + zinc + **total IGF-1 + IGFBP-3** | Set T-index v3 baseline; calculate IGF-1/IGFBP-3 molar ratio (>0.20 = elevated free IGF-1 → glycemic optimization priority) |
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

---

## Part 8c: Sex Hormone Workup (Male T1DM + Refractory Seb Derm)

Add to T-index baseline panel if: male patient, HbA1c >8%, seborrheic dermatitis refractory
to standard topical antifungals + gut protocol.

| Test | What it adds | Interpretation |
|------|-------------|----------------|
| SHBG (serum) | Hepatic insulin exposure; low = insulin resistance → free androgen excess | Low SHBG (<20 nmol/L men; <30 nmol/L women) → androgen arm active |
| Free Androgen Index (calculated: total T × 100 / SHBG) | M5↔M2 androgen bridge activity | FAI >50 (men) → DHT likely elevated → sebum substrate enlarged |
| DHT (dihydrotestosterone) | Confirms 5α-reductase step active in sebaceous glands | Elevated DHT → sebaceous gland hyperplasia is the M2 amplifier |

**Intervention if androgen arm confirmed:**
- Primary: glycemic optimization (reduces portal insulin → SHBG normalizes over 4-8 weeks)
- Male: topical finasteride 2% (5α-reductase type 1 inhibitor; reduces DHT in sebaceous glands)
- Female (PCOS features): spironolactone 50-100mg/day (androgen receptor blocker; first-line for PCOS + acne/seb derm)
- Note: sebaceous gland hyperplasia reverses SLOWLY (weeks-months) after androgen normalization — antifungal response improves on this longer timeline

See `attempts/attempt_018_sex_hormone_m2_sebum_bridge.md`.

## Part 8d: TRPV1 Neurogenic Flushing Arm (Burning/Stinging Phenotype)

Add if: rosacea flushing with burning/stinging sensation, heat + emotional triggers, poor antihistamine response.

**Diagnostic rule:**
- Burning/stinging sensation + heat triggers + no antihistamine benefit → TRPV1 arm dominant
- Itch + food/wine triggers + antihistamine improves → Histamine/mast cell arm (run_003 + run_013)
- Both → compound TRPV1 + histamine (common; treat both arms)

**Protocol for TRPV1 arm:**
1. **Ivermectin 1% cream** (BID × 12 weeks): kills Demodex → reduces LL-37 production → less TRPV1 direct activation (already in protocol; ensures this arm is covered first)
2. **M8 protocol** (sleep + MBSR): reduces SP/CRH release → TRPV1 threshold stays at 43°C (not sensitized to body temperature) — TRPV1 sensitization prevention is a 4th mechanism for M8 treatment benefit
3. **Capsaicin 0.025% cream** (BID × 6 weeks): TRPV1 desensitization via SP depletion + receptor internalization → flushing threshold raised. Initial burning expected weeks 1-2; tolerance develops. Use only after ruling out active rosacea redness (may flare transiently).
4. **Botox intradermal** (1-2U/cm², forehead/cheeks, expert procedure): blocks SP/CGRP release from sensory nerve terminals → neurogenic vasodilation interrupted; 4-6 month duration; second-line for refractory neurosensory rosacea

See `numerics/run_015_trpv1_neurogenic_flushing.md`.

## Part 8e: Ocular Rosacea / Recurrent Chalazion

Add if: rosacea patient with recurrent chalazia (2+ in 2 years), blepharitis with collarettes at lash base.

**Diagnostic:**
- Demodex lash microscopy: epilate 2-3 lashes, mount in saline, direct microscopy; >2 mites/lash = significant
- Collarette pattern at lash base (waxy cylindrical sleeves) = Demodex-specific sign; distinguishes from bacterial blepharitis

**Protocol:**
1. **TTO lid scrubs** (OUST or Cliradex): BID × 6 weeks, then QD indefinitely. Active compound: terpinen-4-ol kills Demodex. Reduces chalazion recurrence from 40% → 12% (Türk 2019).
2. **Doxycycline 40mg/day** (anti-inflammatory dose, same as for rosacea): suppresses B. oleronius-driven TLR2/TLR4 inflammation in lid margin; use in combination with TTO for recurrent chalazia
3. **If on ivermectin already** for facial rosacea: systemic coverage extends to eyelash Demodex; add TTO for local meibomian gland deblocking
4. **Warm compresses + lid massage**: symptomatic; does NOT address Demodex; use as supportive adjunct

See `numerics/run_016_chalazion_ocular_rosacea.md`.

---

---

## Part 8f: Node E — Vitamin D Status (T-Index Addition)

Add 25(OH)D₃ to the baseline T-index panel. It is a third independent M4-lowering input
(alongside IFN-α arm/Node D and Th17 arm/Node C) in T1DM patients.

**Measurement:** Serum 25(OH)D₃ (vitamin D, 25-hydroxy). Quest/LabCorp standard panel ~$40.

| Level | Clinical meaning | Action |
|-------|-----------------|--------|
| >40 ng/mL | Optimal VDR activation; Treg Foxp3 stability maintained | Maintain; reassess annually |
| 20-40 ng/mL | Insufficient; partial Treg VDR activation; M4 partially lowered by this arm | Supplement D₃ 2000 IU/day; retest 8 weeks |
| <20 ng/mL | Deficient; significant M4 lowering; Treg Foxp3 stability compromised | Supplement D₃ 4000 IU/day + K₂ MK-7 100-200 mcg; retest 8 weeks |

**Supplementation protocol:**
- Form: Vitamin D₃ (not D₂) + K₂ MK-7 (directs calcium to bone; reduces soft-tissue calcification risk)
- Sequence: Start butyrate 4-6g/day first (2-4 weeks) → then measure 25(OH)D₃ and correct
  (butyrate upregulates VDR expression → same vitamin D level more efficiently utilized → synergistic Foxp3 induction)
- Target: 40-60 ng/mL; do not exceed 100 ng/mL (hypercalcemia risk)

**Genetic floor addition (to Part 8b):**
VDR Fok1 polymorphism (rs2228570): 'F' allele → shorter VDR protein → less efficient transcription
factor → carriers need higher 25(OH)D₃ (target 50-70 ng/mL rather than 40-60 ng/mL).
Testable via 23andMe raw data (rs2228570: AA/AG = Ff/ff = low efficiency; GG = FF = higher efficiency).

See `numerics/run_018_vitamin_d_vdr_treg_axis.md`.

---

## Part 8g: Non-Responder Sub-Typing Protocol

For any rosacea patient inadequately controlled at 12 weeks on: ivermectin 1% cream + standard care.

### Tier 1 Panel (order simultaneously)

| Test | Interpretation |
|------|---------------|
| Serum LL-37 (cathelicidin) | Elevated → Loop 1 (KLK5/mTORC1) active; add azelaic acid 15% |
| Serum IL-18 | Elevated → Loop 2 (NLRP3/pyroptosis) active; add BHB + colchicine + IF |
| IFN-α2 Simoa | Elevated → M3 arm active (context for all loops; essential baseline) |
| CVB PCR (stool) | Positive → CVB 2B viroporin feeding Loop 2; antivirals + BHB combination |
| HbA1c | >8% → constitutive NLRP3 priming (T1DM amplifier); glycemic optimization is co-treatment for Loop 2 |

### Tier 2 Panel (if IFN-α elevated + CVB negative)

| Test | Interpretation |
|------|---------------|
| MSRV-Env protein (specialty lab) | Elevated → Loop 3 (HERV-W) active; gut/sleep protocol; NO antivirals |
| VCA IgM + EA-D IgG (EBV reactivation) | Positive → EBV is HERV-W trigger; valacyclovir for EBV secondarily addresses HERV-W |
| Hair cortisol (3-month window) | Elevated → M8 is sustaining HERV-W via GRE; stress normalization is primary |

### Treatment by Loop Type

| Loop | Primary treatment | What to avoid |
|------|-----------------|---------------|
| Type 1 (LL-37 elevated) | Azelaic acid 15% gel BID; anti-IL-23 biologic if refractory | Ivermectin alone insufficient |
| Type 2 (IL-18 elevated) | BHB 10-20g/day + IF (20:4) + colchicine 0.5mg BID + HbA1c <7.5% | Antivirals alone insufficient |
| Type 3 (MSRV-Env elevated, CVB neg) | Gut dysbiosis protocol + sleep/MBSR; timeline 3-6 months | Fluoxetine/itraconazole ineffective; may delay correct treatment |
| All-three archetype | Simultaneous multi-target: azelaic acid + BHB/IF/colchicine + gut/sleep | Sequential treatment prolongs cross-loop amplification |

See `numerics/run_017_rosacea_nonresponder_phenotyping.md`.

---

---

## Part 8h: Zinc Status Workup and Protocol

**When to order:** At T-index v3 baseline, simultaneously with Node A (Foxp3), Node C (I-FABP), Node D (IFN-α2), Node E (25(OH)D₃).

**Why this matters for T-index interpretation — the "Ghost Treg" problem:**
FOXP3 is a zinc finger transcription factor. Zinc deficiency impairs Foxp3 DNA-binding without reducing Foxp3 protein abundance. In zinc-deficient patients, Node A (Foxp3+ cell count) appears normal but Treg suppressive function is reduced per cell. **Node A can be falsely reassuring in zinc-deficient T1DM patients.** If Node A appears adequate but Loop 1/2/3 activity persists unexplained, check zinc before concluding Treg count is sufficient.

**Mechanism cascade:**
- T1DM osmotic diuresis → 3-5× normal urinary zinc → 40-60% T1DM patients zinc deficient
- Zinc deficiency simultaneously impairs: gut barrier (IAP + tight junctions), KLK5 regulation (M2), Foxp3 zinc fingers (M4), NLRP3 inhibition at P2X7 + ATPase (Loop 2)

### Measurement

| Test | Notes |
|------|-------|
| Serum zinc (plasma preferred) | Normal: 70-120 µg/dL; avoid hemolyzed samples (hemolysis falsely elevates) |
| RBC zinc (if serum borderline) | Reflects intracellular zinc better; longer half-life than serum |

### Supplementation

| Parameter | Specification |
|-----------|--------------|
| Form | Zinc glycinate or zinc picolinate (highest bioavailability; superior to zinc oxide) |
| Dose (repletion) | 25-30mg elemental zinc/day with meals (food reduces nausea) |
| Dose (maintenance, after 8-12 weeks) | 15-25mg/day |
| Timing | Separate from iron and calcium supplementation (compete for ZIP/ZnT transporters) |
| Butyrate interaction | Additive on gut barrier — butyrate (enterocyte fuel + HDAC→tight junction genes) + zinc (tight junction protein assembly) are complementary; both should be maintained |
| Copper monitoring | If supplementing >6 months or >50mg/day: check serum copper/ceruloplasmin; supplement 1-2mg copper/day if depleted |

**Zinc as fourth NLRP3 inhibition pathway:**
- BHB: K+ efflux blockade (Youm 2015)
- Colchicine: NLRP3+ASC colocalization blocked (Misawa 2013)
- Melatonin/SIRT1: NLRP3 K496 deacetylation (Xia 2018)
- Zinc: P2X7 blockade + NLRP3 ATPase competition (Bhatt 2020)

The zinc + BHB combination blocks different steps (P2X7 input + K+ efflux signaling) → predict additive/synergistic NLRP3 suppression at Loop 2.

See `numerics/run_024_zinc_deficiency.md`.

---

## Part 8i: Loop 4 (Sebaceous/Oxidative NLRP3) Protocol

**When to apply:** Rosacea papules continuing despite:
- I-FABP normalized (M1 treated)
- IFN-α2 normalized (M3 treated)
- Sleep optimized, cortisol normal (M8 treated)
- Serum LL-37 and IL-18 not elevated (Loops 1 and 2 not dominant)

**Characteristic presentation:** Central face, follicular distribution; worsened by UV and outdoor activity; NOT primarily stress-triggered; NOT primarily nocturnal/heat-triggered.

**Mechanism:** UV → squalene peroxidation in sebaceous unit (Malassezia lipases amplify). Squalene-OOH activates NLRP3 in sebocytes (inflammasome-competent, distinct from macrophages). Local IL-1β → neutrophil infiltration → elastase + MPO → more squalene-OOH → self-sustaining. This loop is SKIN-LOCAL and does not respond to systemic BHB/colchicine unless sebocyte penetration is sufficient.

### Loop 4 Intervention Sequence

| Step | Intervention | Mechanism | Notes |
|------|-------------|-----------|-------|
| 1 | **SPF 50+ broad-spectrum daily** | UV blockade → squalene-OOH production reduced | Primary loop input blockade; most important single intervention |
| 2 | **Topical niacinamide 4% cream BID** | NAD+→SIRT1→NLRP3 K496 deacetylation in sebocytes; direct squalene-OOH reduction | Draelos 2019 J Cosmet Dermatol; apply morning + evening |
| 3 | **Topical vitamin E serum 1-2%** | Squalene peroxide scavenger in sebum; breaks peroxidation-NLRP3 cycle upstream | Apply before UV exposure; Thiele 2001 Free Radic Biol Med |
| 4 | **Azelaic acid 15% gel BID** (if LL-37 also elevated) | KLK5 inhibition → less LL-37 → less TRPV1-Ca²⁺ input to sebocyte NLRP3 | Second-line; add if Loop 1 + Loop 4 concurrent |
| 5 | **Ketoconazole 2% shampoo foam × 5 min before rinse, 2-3×/week** (if Malassezia active) | Reduces Malassezia lipase activity → reduces arachidonic acid substrate for squalene-OOH generation | Use if concurrent seb derm component; clinical assessment or PCR |

**Note on ivermectin and Loop 4:** Ivermectin (Demodex-clearing) reduces Loop 4 inputs by: (a) removing B. oleronius TLR2 priming of sebocytes, (b) reducing Malassezia anaerobic microenvironment via follicular occlusion reduction. Ivermectin addresses Loop 4 inputs but does not directly suppress sebocyte NLRP3 — niacinamide + vitamin E address the sebocyte-intrinsic loop activity remaining after Demodex clearance.

See `numerics/run_025_sebaceous_nlrp3_local_loop.md`.

---

---

## Part 8j: Akkermansia muciniphila Protocol

**When to use:** Second-tier addition for gut barrier, indicated when Node C I-FABP remains elevated (>200 pg/mL) after 8-12 weeks of:
- Dietary fiber 25-35g/day (varied sources)
- Exogenous butyrate 4-6g/day (sodium/calcium butyrate)

**Rationale for sequencing (butyrate first, Akkermansia second):**
Exogenous butyrate at 4-6g/day bypasses the Akkermansia → F. prausnitzii → endogenous butyrate trophic chain. It works independently of microbiome colonization status. Akkermansia supplementation addresses the TLR2/Amuc_1100 → tight junction mechanism (a DIFFERENT pathway than butyrate's HDAC → tight junction gene expression) and the physical mucus barrier. These are additive, not redundant.

### Supplementation

| Parameter | Specification |
|-----------|--------------|
| Form | Pasteurized A. muciniphila (heat-stable Amuc_1100 survives GI; safe for immunocompromised) |
| Dose | ~3.8 × 10^10 CFU equivalent/day (Depommier 2019 Nat Med dose) |
| Timing | With largest meal (food + mucus secretion creates substrate) |
| Duration | 3 months before reassessing Node C |
| Prebiotic co-supplement (optional) | Polyphenol extract (pomegranate, cranberry, or grape seed) — expands endogenous Akkermansia; inulin/FOS provides mucin precursor galactose substrates |

**What Akkermansia adds that butyrate does not:**
- Amuc_1100 → TLR2 → tight junction upregulation (independent of HDAC)
- Mucus layer remodeling → physical barrier thickness maintained
- Trophic support for F. prausnitzii → endogenous butyrate production recovery (slower, months)

**What butyrate adds that Akkermansia does not:**
- Immediate HDAC inhibition → Foxp3 CNS2 demethylation → Treg stability
- VDR upregulation for vitamin D synergy
- Enterocyte fuel (direct metabolic support)

**Zinc interaction:** Zinc (Part 8h) + Akkermansia + butyrate = three independent gut barrier mechanisms. Zinc restores IAP (LPS detoxification) + ZO-1 assembly; Akkermansia provides TLR2/Amuc_1100 tight junction signaling; butyrate provides HDAC → tight junction gene expression. All three can be used simultaneously without competition.

See `numerics/run_026_akkermansia_muciniphila.md`.

---

## Part 8k: Sulforaphane Protocol

**When to use:** Consider for any of the following indications:
- Loop 3 (HERV-W) activity (NF-κB supplement to colchicine)
- Loop 4 (sebaceous NLRP3) in UV-exposed skin (systemic antioxidant complement to topical vitamin E)
- ME/CFS with mitochondrial damage (CoQ10 + NMN + SFN triad)
- Refractory gut barrier compromise despite butyrate + Akkermansia (enterocyte cytoprotection)

**Mechanistic positions:**

| Loop/Mountain | Mechanism | Synergy with |
|--------------|-----------|-------------|
| Loop 3 (HERV-W/NF-κB) | Nrf2 → CBP/p300 competition → NF-κB transcription ↓ | Colchicine (IKK blockade) |
| Loop 4 (sebaceous NLRP3) | Nrf2 → GPx + GSH → squalene-OOH intracellular scavenging | Topical vitamin E (extracellular sebum) |
| ME/CFS (Complex I) | Nrf2 → HO-1 → CO → PGC-1α → mitochondrial biogenesis | CoQ10 600mg + NMN 500mg |
| M1 (gut barrier) | Nrf2 → HO-1 → enterocyte cytoprotection + bilirubin NF-κB ↓ | Butyrate, Akkermansia |

### Supplementation

| Parameter | Specification |
|-----------|--------------|
| Form | Broccoli sprout extract standardized to sulforaphane content OR stabilized SFN product |
| Anti-inflammatory dose | 30mg SFN/day (Nrf2 induction in PBMCs, Fahey 2015) |
| ME/CFS mitochondrial dose | 50mg SFN/day (PGC-1α response is dose-dependent) |
| Timing | With largest meal (myrosinase activity requires food matrix; raw/cold preferred) |
| Commercial options | Avmacol, TruBroc, Sulforaphane Gold (standardized products) |

**Drug interactions:** SFN induces CYP1A2 and CYP2B6 (secondary to Nrf2 → CAR/PXR pathway).
- Colchicine: metabolized by CYP3A4 — minimal SFN interaction expected; safe co-administration
- Warfarin: CYP2C9 — not directly affected by SFN; but HO-1/bilirubin may confound INR interpretation
- Review medications for CYP1A2/2B6 substrates before starting (theophylline, clozapine, efavirenz)

**Note for Loop 3 patients:** SFN + colchicine 0.5mg BID = complementary NF-κB suppression via
two independent mechanisms. This combination is not in any standard protocol but is mechanistically
justified and OTC (SFN) + generic (colchicine). No known pharmacokinetic interaction.

See `numerics/run_027_sulforaphane_nrf2.md`.

---

---

## Part 8l: Loop 1 Non-Responder — Topical Rapamycin Protocol

**Indication:** Loop 1 (LL-37 elevated) non-responder after:
- Ivermectin 1% cream BID × 12 weeks (Demodex cleared)
- Azelaic acid 15% gel BID × 12 weeks (KLK5 protease activity inhibited)
- LL-37 remains elevated; papulopustular rosacea continues

**Mechanism position:** Azelaic acid inhibits KLK5 ACTIVITY. Topical rapamycin inhibits KLK5
TRANSCRIPTION (mTORC1 → S6K1 → KLK5 mRNA). These are sequential steps — dual blockade is
more complete than either alone. Rapamycin also inhibits sebocyte mTORC1 → SREBP-1 → sebum
production (Loop 4 co-benefit).

### Treatment

| Parameter | Specification |
|-----------|--------------|
| Compound | Sirolimus (rapamycin) 0.2% in suitable cream vehicle (compounded; not commercially available) |
| Dose/frequency | QD-BID on lesional skin only |
| Duration | 3-month trial before reassessing serum LL-37 |
| Avoid | Active wounds, irritated barrier-disrupted skin (mTORC1 required for wound healing) |

### Treatment Ladder (Loop 1)

| Level | Intervention | Target | Escalate when |
|-------|-------------|--------|---------------|
| 1 | Ivermectin 1% cream BID | Demodex TLR2 priming | At diagnosis |
| 2 | Azelaic acid 15% gel BID | KLK5 protease activity | If LL-37 elevated at 12 weeks |
| **3** | **Topical rapamycin 0.2% (add to level 2)** | **mTORC1 → KLK5 transcription** | **Azelaic acid insufficient** |
| 4 | Anti-IL-23 biologic (guselkumab 100mg Q8W) | IL-23 → Th17 systemic blockade | Severe refractory |

**Combination for Loop 1 + Loop 4 concurrent:** Rapamycin 0.2% + niacinamide 4% BID + topical
vitamin E + azelaic acid 15% + SPF 50. Five topicals addressing both loops from multiple angles.

See `numerics/run_028_topical_rapamycin_loop1.md`.

---

## Part 8m: M8 Vagal (CAP) Restoration Protocol

**Indication:** Add to all M8-active patients (cortisol elevated, stress-triggered flares, poor
HRV, TRPV1-dominant flushing pattern). This is the PARASYMPATHETIC ARM of M8 treatment,
complementary to the sympathetic arm (sleep, MBSR, LDN).

**Mechanism:** Vagal → cholinergic anti-inflammatory pathway → α7-nAChR on macrophages →
IKK-β inhibited → NF-κB ↓ + HMGB1 ↓. Provides Loop 3 NF-κB suppression, Loop 2 DAMP
clearance, and IFN-α damping in spleen — all via neural reflex, not pharmacological.

### Daily CAP Protocol

| Intervention | Mechanism | Dose/frequency |
|-------------|-----------|----------------|
| Cold shower (already endorsed) | Diving reflex → vagal → α7-nAChR | 30-60 seconds cold, BID |
| Diaphragmatic breathing (4-7-8 pattern) | Respiratory sinus arrhythmia → vagal | 10 min BID (before bed + morning) |
| HRV monitoring (wearable) | Vagal tone proxy; flare-risk indicator | Daily morning readout |

### HRV Interpretation

| HRV reading | Interpretation | Action |
|-------------|----------------|--------|
| High HRV (above 7-day average) | CAP active; low inflammatory risk | Standard protocol |
| Low HRV (>15% below average) | CAP withdrawn; sympathetic dominant | Extra cold + breathing; reduce stress inputs; monitor for flare |
| Chronically low HRV baseline | Consider autonomic neuropathy (in T1DM) or LDN 1.5-4.5mg/day | Assess T1DM neuropathy workup if HRV does not respond to cold |

### NF-κB Triple Suppression (for Loop 3 / M8 overlap patients)

Patients with HERV-W active (Loop 3) + M8 dominant + Loop 2 active benefit from layering all
three NF-κB pathways simultaneously:

| Agent | Target | Independent of others |
|-------|--------|----------------------|
| Colchicine 0.5mg BID | IKK disruption + p65 translocation blocked | Yes |
| Sulforaphane 30mg/day | CBP/p300 competition | Yes |
| Cold + breathing (vagal CAP) | α7-nAChR → IKK-β inhibition | Yes |

All three NF-κB suppression mechanisms are independent and additive. No pharmacokinetic
interactions between colchicine and SFN (different metabolic pathways). CAP is non-pharmacological.

See `numerics/run_029_vagal_anti_inflammatory_m8.md`.

---

---

## Part 8n: M7 Revised Protocol — Triple Red Complex

**Indication:** P. gingivalis IgG positive + prior SRP with recurrence OR salivary PCR positive
for T. denticola and/or T. forsythia in addition to P. gingivalis.

**Key additions to standard M7 protocol:**

T. denticola dentilisin runs a second IgA-protease self-amplifying loop — identical to P.
gingivalis's loop but with a different enzyme. LGG sIgA restoration is countered by BOTH IgA
proteases. Antibiotic treatment must suppress T. denticola before LGG-driven sIgA restoration
is meaningful. T. denticola motility enables deep anaerobic pocket colonization that SRP misses.

T. forsythia BspA → TLR4 → TRIF → IFN-β = oral M3 arm loading independent of P. gingivalis.
Essential oil mouthwash (Listerine formulation) specifically disrupts T. forsythia outer sheath.

### Revised M7 Sequence (Triple Red Complex Confirmed)

| Step | Intervention | Target | Duration |
|------|-------------|--------|---------|
| 1 | M8 HPA normalization (sleep, MBSR, adaptogens) | sIgA recovery requires non-suppressed cortisol | Before or concurrent with step 2 |
| 2 | Scaling + root planing | Physical biofilm removal | 1-2 sessions |
| 3 | Chlorhexidine 0.12% BID | Prevent immediate recolonization | 4 weeks post-SRP |
| 4 | Metronidazole 400mg BID | T. denticola + T. forsythia + P. gingivalis (anaerobes) | 7 days |
| 5 | Essential oil mouthwash BID (Listerine original) | T. forsythia outer sheath disruption | Ongoing maintenance |
| 6 | LGG 10^10 CFU/day | sIgA restoration (now effective with both IgA proteases suppressed) | 90 days |
| 7 | Doxycycline 40mg/day | Sub-antimicrobial MMP inhibition (collagen protection) | 3 months |

**Monitoring:** Salivary PCR panel (OralDNA Labs) at baseline + 3 months post-treatment.
Target: all three red complex species reduced to below threshold at 3 months.

**Standard M7 protocol (P. gingivalis alone):** Unchanged (see Part 3, M7 arm section).

See `numerics/run_030_oral_red_complex.md`.

### Thyroiditis Cross-Reference (for T1DM patients)

25-30% of T1DM patients have concurrent autoimmune thyroid disease (polyglandular syndrome).
The same dysbiosis framework mechanisms apply: M3 (CVB → IFN-α → Th1/CD8+ → anti-TPO),
M4 (zinc ghost Tregs + VDR), Loop 2 (NLRP3 in thyrocytes), Loop 3 (HERV-W in Hashimoto's).

**Thyroid-specific addition:** Selenium 200µg/day (selenomethionine) → Cooper 2000 meta-analysis:
40-60% anti-TPO titer reduction. Thyroid has highest selenium demand per gram of any tissue.
GPx4 + deiodinase (T4→T3 conversion) + thioredoxin reductase are all selenium-dependent.

**Screen at T1DM diagnosis:** anti-TPO + anti-Tg + TSH + FT4. If positive with normal TSH:
start protocol NOW (intervention window before follicle destruction). Do not wait for TSH to rise.

See `../thyroiditis/THEWALL.md` for full thyroiditis analysis.

---

*Compiled: 2026-04-12 | Post-Phase 4 eighth extension synthesis*
*Sources: attempts 001-019, numerics runs 001-030, thyroiditis/THEWALL.md, phase3_synthesis.md, resolution_biology.md*
*Framework status: 8 mountains, 31+ mechanisms (6 strong candidate, 17 candidate, 4 convergence nodes)*
*Parts 8n added: M7 triple red complex revised protocol + T. denticola dentilisin second IgA protease loop*
*Thyroiditis cross-reference: selenium 200µg/day; anti-TPO screening at T1DM diagnosis*
*Part 9 confidence unchanged: assembly is research-grade synthesis requiring physician review*
*De-escalation criteria: see results/resolution_biology.md*
*Next update: when T-index v3 measurements or genetic floor panel results are available*

---

## Part 8o: Circadian Disruption — Shift Worker Protocol

**Indication:** Patient reports rotating or night shifts, irregular sleep schedule, or HRV suppressed
with no identifiable psychological stressor. M8 BMAL1 arm is active when circadian rhythm is
disrupted beyond what sleep hygiene alone can address.

**Mechanism:** Shift work → BMAL1 amplitude ↓ 30-60% in macrophages → NLRP3 transcription
disinhibited (BMAL1 arm, run_035) PLUS melatonin suppressed → SIRT1 → K496 not deacetylated
(melatonin arm, run_022). Double NLRP3 disinhibition from a single occupational exposure.

### Shift Worker M8 Protocol

| Intervention | Mechanism | Evidence | Timing |
|-------------|----------|---------|--------|
| Time-restricted eating (TRE, 8-10h window) | Peripheral clock re-synchronization via mealtime nutrient cues independent of light schedule | Chaix 2019 Cell Metab: TRE in night workers → improved metabolic markers | Fixed daily eating window regardless of shift timing |
| Morning light therapy (10,000 lux, 20-30 min) | SCN re-entrainment → peripheral clock synchrony → BMAL1 amplitude improved | Established for circadian re-entrainment in shift workers | Immediately after waking (regardless of clock time) |
| Melatonin 0.5mg | SIRT1/K496 arm even when BMAL1 arm is disrupted | Run_022 dosing | 60-90 min before intended sleep |
| Colchicine 0.5mg BID | NLRP3 assembly block — compensates for elevated NLRP3 protein from BMAL1 deficiency | Misawa 2013; Loop 2 evidence | Standard dosing |

**Priority order for shift workers:** TRE first (lowest barrier; addresses root peripheral clock
mechanism) → add light therapy if TRE insufficient → melatonin 0.5mg always (addresses sleep arm)
→ colchicine (if NLRP3-driven inflammation still elevated after circadian normalization attempts).

**Note:** REV-ERBα agonism (SR9009) directly activates the BMAL1→NLRP3 repression mechanism
but is pre-clinical only; not recommended OTC.

See `numerics/run_035_circadian_bmal1_nlrp3.md`.

---

## Part 8p: Propolis/CAPE — Fourth NF-κB Suppressor and Multi-Mountain OTC

**Indication:** Loop 3 (NF-κB sustaining HERV-W transcription) not adequately suppressed with
existing three-pathway approach (colchicine + sulforaphane + vagal CAP). Or: topical antifungal
for M2 Malassezia preferred over prescription ketoconazole (OTC option). Or: M7 mouthwash
alternative to chlorhexidine (no staining, no taste alteration).

**Mechanism:** CAPE (caffeic acid phenethyl ester) → dual NF-κB block: (1) IKKβ catalytic site
inhibition → IκBα not phosphorylated; (2) p65 Cys38 alkylation → p65 cannot bind κB DNA.
Co-present quercetin → NLRP3 NACHT ATPase inhibition (MCC950-like). Propolis thus provides
NF-κB priming block (CAPE) + NLRP3 activation block (quercetin) simultaneously.

### Propolis Protocol by Application

| Application | Form | Dose | Target |
|------------|------|------|--------|
| Oral (Loop 3 NF-κB + NLRP3) | Standardized propolis extract (≥5% CAPE) | 300-500mg BID with food | Loop 3 NF-κB sustaining + NLRP3 NACHT inhibition |
| Topical (M2 Malassezia) | Propolis tincture 20-30% diluted 1:3-1:5 in carrier oil (argan/jojoba) | Apply BID to seb derm/perioral/scalp areas | Malassezia CYP51 inhibition (same target as ketoconazole) |
| Mouthwash (M7) | 2-3% propolis in water OR commercial propolis mouthwash | 30mL BID × 4 weeks post-SRP | P. gingivalis + T. denticola + T. forsythia (MIC inhibitory) |

**Contraindication:** Bee/pollen allergy → cross-reaction risk in ~5-15% of bee-allergic patients.
Patch test before topical use; start oral at low dose if allergy history uncertain.

**Bioavailability caveat:** CAPE oral bioavailability uncertain — intestinal esterases may hydrolyze
CAPE → caffeic acid before systemic absorption. Clinical anti-inflammatory evidence is empirical
(CRP reduction in RCTs) but plasma CAPE levels not confirmed. This limits confidence in the oral
Loop 3 arm; the topical and mouthwash applications (direct contact, no systemic absorption required)
have higher confidence.

**Additive with colchicine for Loop 3:**
- Colchicine: IKK complex FORMATION blocked (upstream)
- CAPE: IKKβ catalytic activity + p65 DNA binding blocked (downstream)
- Together: three-point NF-κB block

See `numerics/run_036_propolis_cape_nfkb.md`.

---

*Compiled: 2026-04-12 | Post-Phase 4 ninth extension synthesis*
*Sources: attempts 001-019, numerics runs 001-036, all sibling THEWALL.md files*
*Framework status: 8 mountains, 36+ mechanisms | Four NF-κB suppressors | Five M8 mechanisms | Four NLRP3 inhibition pathways*
*Parts 8o-8p added: Circadian shift worker protocol (BMAL1/TRE) + Propolis/CAPE multi-mountain OTC*
*Next update: when T-index v3 measurements, genetic floor panel, or BHB pharmacokinetics analysis available*

---

## Part 8q: Vitamin K2 (MK-7) — Fifth NF-κB Suppressor + T1DM Vascular Protection

**Indication:** All T1DM + dysbiosis patients. Gut dysbiosis depletes Bacteroidetes (MK-7
producers) → functional K2 deficiency is probable in T1DM with established M1 dysbiosis.
Additionally relevant for patients with dp-ucMGP >400 pmol/L (confirmed K2 insufficiency).

**Why T1DM-specific:** M1 dysbiosis → Bacteroidetes ↓ → MK-7 synthesis ↓ → Gas6 not gamma-
carboxylated → Axl/Mer TAM receptor signaling impaired → SOCS1 not upregulated → IKK-β
assembled complex remains active → NF-κB not restrained. M1 simultaneously activates NF-κB
(LPS/TLR4) AND removes its restraint (K2 deficit). Restoring K2 addresses the restraint arm.

### MK-7 Protocol

| Parameter | Specification |
|-----------|--------------|
| Form | MK-7 (menaquinone-7), not MK-4; natto-derived or synthetic all-trans |
| Dose | 180µg/day |
| Timing | With a fat-containing meal (fat-soluble vitamin; bile acids required) |
| Monitoring | dp-ucMGP at baseline + 3 months; target <200 pmol/L |
| Contraindication | Warfarin (direct K antagonism) — check anticoagulant status |
| Cost | ~$10-20/month |

**Three benefits from single intervention:**
1. Gas6/Axl/SOCS1 → NF-κB suppression (fifth independent pathway, NLRP3 priming reduced)
2. MGP carboxylation → vascular calcification inhibited (T1DM complication prevention)
3. Osteocalcin/GPRC6A → peripheral insulin sensitization (improves glycemic control → M5 effect)

**Lab to add at T-index baseline:** dp-ucMGP (desphospho-uncarboxylated Matrix Gla Protein) —
specialty assay (VitaK/LabCorp). If unavailable: presume functional K2 deficiency in T1DM +
established gut dysbiosis and supplement empirically.

See `numerics/run_039_vitamin_k2_mk7_nfkb.md`.

---

## Part 8r: BHB Protocol Extension — Exogenous 1,3-Butanediol for Non-Fasting NLRP3 Blockade

**Indication:** T1DM patients for whom >12h fasting is contraindicated (hypoglycemia risk,
eating disorder history, pediatric). Or: Loop 2 (IL-18-driven) not responding to 12-14h IF
alone and extended fasting is not safe.

**Mechanism:** 1,3-Butanediol → hepatic ADH → β-hydroxybutyrate → plasma BHB 1.5-2.5 mM at
60-90 min → above 500 µM NLRP3 IC50 for 2-3h (Youm 2015 threshold). GRAS-classified. Practical
cost (~$15-30/month at 15g/day).

### Exogenous BHB Protocol

| Parameter | Specification |
|-----------|--------------|
| Form | 1,3-Butanediol (liquid) |
| Dose | 15g once daily; start at 7-10g × 2 weeks, then titrate to 15g |
| Timing | Morning (to extend overnight fast's BHB window) |
| Safety gate | Blood glucose must be <180 mg/dL before dosing; do NOT use if glucose >250 mg/dL |
| Monitoring | Abbott Precision Xtra ketone meter at 60 min post-dose; target >0.5 mM |
| Duration | Ongoing as needed; re-assess at 12 weeks (Loop 2 markers: IL-18, CRP) |
| Contraindications | Uncontrolled T1DM; DKA risk; fever/illness; alcohol (both use ADH → competition) |

**Combination with IF:** 1,3-BD can be combined with modified IF (12h fast → 1,3-BD at hour 12
→ extends NLRP3 blockade 2-3h further without extending the fast). Net NLRP3 coverage per day:
~12h endogenous (fasting) + 2-3h exogenous (1,3-BD) = ~14-15h.

**Alternative form (research/high-resource):** Ketone ester 25g/day (Cox 2016: peak BHB 3.3 mM,
3-4h duration) — pharmacologically superior but ~$1,000/month; not practical for chronic use.

See `numerics/run_037_exogenous_bhb_pharmacokinetics.md`.

---

*Compiled: 2026-04-12 | Post-Phase 4 tenth extension synthesis*
*Sources: attempts 001-019, numerics runs 001-039, all sibling THEWALL.md files*
*Framework status: 8 mountains, 39+ mechanisms | Five NF-κB suppressors | Five M8 mechanisms | Four NLRP3 inhibition pathways*
*Parts 8q-8r added: Vitamin K2/MK-7 (fifth NF-κB suppressor + vascular protection) + 1,3-butanediol exogenous BHB extension*
*Next update: IFN-α → NLRP3 direct bridge analysis; mast cell stabilization; spermidine/autophagy*

---

## Part 8s: T-Index Revision — Node D (IFN-α2 Simoa) as Loop 2 Co-Treatment Trigger

**New architectural implication from run_040:** M3 IFN-α directly primes NLRP3 (ISGF3 →
NLRP3 ISRE). Node D elevation → Loop 2 NLRP3 protein constitutively elevated from BOTH
NF-κB priming (Node C / gut leakage) AND IFN-α priming (Node D / M3 arm).

**T-index decision logic update:**

| Node D (IFN-α2) | Node C (I-FABP) | Clinical implication |
|----------------|----------------|---------------------|
| Normal | Normal | Standard protocol; no Loop 2 priority |
| Normal | Elevated | Gut repair first; Loop 2 treatment standard |
| Elevated | Normal | **Loop 2 treatment urgently even with normal gut barrier** — IFN-α is the NLRP3 primer; M3 intervention (sleep, colchicine NF-κB arm) co-treatment |
| Elevated | Elevated | **Double NLRP3 priming — Loop 2 treatment at highest priority; both Node C and Node D interventions simultaneously** |

**Loop 2 treatment hierarchy remains unchanged:**
1. BHB (12-16h IF or 1,3-butanediol 15g/day if fasting contraindicated)
2. Colchicine 0.5mg BID
3. Melatonin 0.5mg
4. Zinc 25mg/day

**M3 intervention for Node D reduction (reduces IFN-α priming source):**
- Sleep quality (reduces pDC IFN-α production — sleep deprivation → pDC activation)
- Colchicine NF-κB arm (reduces HERV-W transcription → less MSRV-Env → less TLR4 → less IFN-α)
- Gut repair (less LPS → less TLR4 → TRIF → less IFN-β → less autocrine NLRP3 priming)

**β cell preservation note (for early/new-onset T1DM):**
If C-peptide > 0.2 nmol/L at diagnosis: Node D elevation → IFN-α priming β cell NLRP3 →
accelerated β cell destruction. M3 intervention (especially sleep + colchicine) should be
initiated urgently alongside insulin therapy to preserve residual β cell function.

See `numerics/run_040_ifna_nlrp3_m3_loop2_bridge.md`.

---

*Compiled: 2026-04-12 | Post-Phase 4 eleventh extension synthesis*
*Sources: attempts 001-019, numerics runs 001-040, all sibling THEWALL.md files*
*Framework status: 8 mountains, 40+ mechanisms | Five NF-κB suppressors | Five M8 mechanisms | Four NLRP3 inhibition pathways*
*Part 8s added: T-index Node D / Loop 2 co-treatment decision matrix; β cell preservation urgency for C-peptide positive T1DM*
*Architectural change: M3 and Loop 2 are connected via IFN-α → NLRP3 ISRE — not independent pathways*
*Next update: spermidine/autophagy analysis; F. prausnitzii monitoring threshold definition; mast cell stabilization*

---

## Part 8t: Spermidine — Fifth NLRP3 Inhibition Pathway via Mitophagy

**Indication:** Loop 2 (IL-18 elevated, gasdermin D activation suspected) not fully controlled
with BHB + colchicine + melatonin + zinc. Or: patient cannot achieve adequate IF for BHB
(T1DM hypoglycemia) AND 1,3-butanediol is in use but NLRP3 markers still elevated. Spermidine
addresses a mechanistically distinct NLRP3 arm (Signal 2 source removal) not addressed by
any of the four existing inhibition pathways.

**Mechanism:** Spermidine → EP300 acetyltransferase inhibition → Beclin-1 deacetylation →
mitophagy (PINK1/Parkin) → damaged mitochondria removed → mtROS, mtDNA, cardiolipin (all
NLRP3 Signal 2 activators) eliminated before NLRP3 receives the activation signal.

### Spermidine Protocol

| Parameter | Specification |
|-----------|--------------|
| Target dose | 1-3mg spermidine/day |
| Food-first | Wheat germ 2 tbsp/day (IF no celiac) OR mushrooms 150g + aged cheese 30g + legumes 100g/day |
| Supplement | SpermidineLIFE 1.2mg/capsule once daily (with food) |
| Cost | ~$30-50/month (supplement); dietary sources ~$5-10/month additional food cost |
| Timing | With food (polyamine absorption is food-dependent) |
| T1DM + celiac | Wheat germ contraindicated; mushroom/legume route; supplement is gluten-free |
| Sequencing | Level 2: add after BHB + colchicine established (does NOT replace BHB/colchicine) |

**Complementary to IF:** IF → mTORC1 → ULK1 → autophagy (mTORC1-dependent pathway);
spermidine → EP300 → Beclin-1 → autophagy (EP300-dependent, active in FED state). They are
additive — spermidine provides mitophagy between IF windows when mTORC1 is active.

See `numerics/run_041_spermidine_autophagy_nlrp3.md`.

---

## Summary: Five NLRP3 Inhibition Pathways (Phase 4 Complete Reference)

All five pathways are mechanistically orthogonal — no single drug/nutrient covers more than two:

| Pathway | Compound | Target | Confidence |
|---------|---------|--------|-----------|
| 1. K+ efflux blockade | BHB (IF or 1,3-butanediol) | Pannexin-1/P2X7 | High (Youm 2015 Cell) |
| 2. Assembly blockade | Colchicine 0.5mg BID | NLRP3+ASC colocalization | High (Misawa 2013) |
| 3. K496 deacetylation | Melatonin 0.5mg → SIRT1 | NLRP3 conformational gate | Moderate (Xia 2018) |
| 4. P2X7/ATPase block | Zinc 25mg/day | P2X7 receptor + NLRP3 ATPase | Moderate (Bhatt 2020) |
| 5. Signal 2 source removal | Spermidine 1-3mg/day | mtROS/mtDNA/cardiolipin via mitophagy | Moderate (Eisenberg 2016) |

## Summary: Five NF-κB Suppression Pathways (Phase 4 Complete Reference)

| Pathway | Compound | Target | Confidence |
|---------|---------|--------|-----------|
| 1. IKK complex assembly | Colchicine 0.5mg BID | Microtubule → IKK scaffold | High |
| 2. CBP coactivator competition | Sulforaphane 30-50mg/day | Nrf2 → p300 unavailable | Moderate |
| 3. IKKβ inhibitory phosphorylation | Vagal CAP (cold, breathing) | α7-nAChR → JAK2/STAT3 → IKKβ | Moderate |
| 4. IKKβ active site + p65 alkylation | Propolis/CAPE 300-500mg BID | IKKβ catalytic + p65 Cys38 | Moderate (bioavailability caveat) |
| 5. SOCS1 → IKK complex inactivation | MK-7 180µg/day | Gas6 → Axl → SOCS1 → NEMO | Moderate |

---

*Compiled: 2026-04-12 | Post-Phase 4 twelfth extension synthesis*
*Sources: attempts 001-019, numerics runs 001-041, all sibling THEWALL.md files*
*Framework status: 8 mountains, 41+ mechanisms | FIVE NLRP3 inhibition pathways | FIVE NF-κB suppressors | FIVE M8 mechanisms*
*Part 8t added: spermidine/mitophagy — fifth NLRP3 inhibition pathway*
*Summary tables: all five NLRP3 and NF-κB pathways with confidence levels*
*Next update: mast cell stabilization arm; F. prausnitzii monitoring threshold definition*

---

## Part 8u: Mast Cell Stabilization — Quercetin + Capsaicin for M8 Effector and Loop 1 Neurogenic

**Indication:** M8-dominant rosacea (flushing > papulopustular) that persists after stress
reduction + sleep + HRV improvement. Patient identifies: "I flush with heat, sun, wine, hot
drinks even when calm." OR: Loop 1 (KLK5 hyperactivity) that is partly driven by neurogenic
SP/NK1R input rather than purely microbial TLR2 stimulation.

**Key insight:** Mast cell receives four inputs (CRH, SP/TRPV1, C5a, squalene-OOH). Standard
M8 protocol addresses only CRH. Quercetin + capsaicin address SP/NK1R arm and stabilize mast
cell at the effector level regardless of input.

### Mast Cell Stabilization Protocol

| Intervention | Dose/Route | Target | Notes |
|-------------|-----------|--------|-------|
| Quercetin phytosome | 500mg BID with food | All mast cell inputs (cAMP/Ca2+) | Already present if using propolis (run_036); if propolis used, no additional quercetin needed |
| Capsaicin 0.025% cream | Once daily × 4 weeks → 2-3×/week maintenance | SP/NK1R arm + Loop 1 KLK5 neurogenic | Initial burning expected; start small area; avoid eye/nasal area; apply at night |

**Dual-mountain benefit of capsaicin:**
SP depletion → NK1R on mast cells NOT triggered (M8 ↓) + NK1R on keratinocytes NOT triggered
(KLK5 not induced → Loop 1 neurogenic entry ↓). Order: establish KLK5 topical treatment
(azelaic acid) first; add capsaicin at week 3-4 when acute phase is manageable.

**Sequence with existing protocol:**
Week 1-2: Standard M8 (sleep, MBSR, cold/breathing); Start azelaic acid  
Week 3: Add capsaicin 0.025% at night (after azelaic acid) — small area initially  
Week 4+: Add quercetin 500mg BID (or propolis with quercetin already covers this)  
Month 2: Assess M8 flushing frequency; if CGRP-dominant flushing persists (hot drink trigger
specifically, not sun/heat), discuss anti-CGRP option with prescriber

**M1→M8 gut-flushing link:** gut repair (butyrate + fiber + I-FABP monitoring) reduces C5a
generation → dermal mast cell C5aR1 input ↓ → M8 flushing reduced even without dedicated
mast cell stabilizer. Node C improvement will show as M8 flushing reduction — this is the
mechanism.

See `numerics/run_042_mast_cell_stabilization.md`.

---

*Compiled: 2026-04-12 | Post-Phase 4 thirteenth extension synthesis*
*Sources: attempts 001-019, numerics runs 001-042, all sibling THEWALL.md files*
*Framework status: 8 mountains, 42+ mechanisms | Five NLRP3 pathways | Five NF-κB suppressors | Five M8 mechanisms | Four mast cell inputs*
*Part 8u: mast cell stabilization — quercetin (already in propolis) + capsaicin (dual M8/Loop 1 SP depletion)*
*M1→M8 C5a bridge formalized: gut repair is a direct mast cell stabilization intervention via complement*

---

## Part 8v: M7 Extended — H. pylori Screening and Eradication Protocol

**When to screen:** Rosacea patient with EITHER: (a) dyspeptic symptoms (heartburn, early
satiety, epigastric pain, nausea, bloating), OR (b) first-degree family history of gastric
cancer or peptic ulcer disease, OR (c) recalcitrant M8-dominant rosacea not responding to
standard protocol within 12 weeks.

**Mechanism:** H. pylori CagA → NF-κB → NLRP3 priming (Signal 1) + VacA → K+ efflux →
NLRP3 activation (Signal 2). Both signals simultaneously from a single gastric pathogen.
H. pylori-positive rosacea patients have 2.47× higher odds of rosacea (Gravina 2015 meta-
analysis) and 62-80% show rosacea improvement after eradication.

### H. pylori Protocol

| Step | Action | Notes |
|------|--------|-------|
| 1. Screen | Stool H. pylori antigen test (sensitivity 94%, specificity 97%) | Preferred for current infection vs. serology |
| 2. If positive: eradicate | Triple therapy: PPI + amoxicillin 1g BID + clarithromycin 500mg BID × 14 days | Quadruple if clarithromycin resistance suspected |
| 3. Concurrent | LGG 10^10 CFU/day (start Day 1, continue 90 days) | Prevents P. gingivalis gut colonization during PPI-induced acid suppression |
| 4. Stop PPI | Day 15 (immediately after 14-day antibiotic course) | Restores gastric acid → closes P. gingivalis transit window |
| 5. Confirm | UBT or stool antigen at 4-6 weeks (≥2 weeks after last PPI) | False negative if PPI too recent |
| 6. Assess | Rosacea flare frequency at 3 and 6 months | Improvement expected in 62-80% of H. pylori-positive cases |

**T1DM note:** H. pylori eradication → HOMA-IR reduced (insulin resistance improvement; Tang
2019). Adds metabolic benefit beyond rosacea for T1DM patients with H. pylori.

**Not universal screening:** Dyspeptic symptoms or family history are the indicated triggers.
H. pylori test-and-treat in asymptomatic rosacea is not evidence-based.

See `numerics/run_044_helicobacter_pylori_m7_extension.md`.

---

*Compiled: 2026-04-12 | Post-Phase 4 fourteenth extension synthesis*
*Sources: attempts 001-019, numerics runs 001-044, all sibling THEWALL.md files*
*Framework status: 8 mountains, 44+ mechanisms | Five NLRP3 pathways | Five NF-κB suppressors | Five M8 mechanisms | M7 extended to gastric compartment*
*Part 8v added: H. pylori M7 gastric protocol — screen, eradicate, concurrent LGG, confirm, assess response*
*Next update: M6 rosacea integration; F. prausnitzii monitoring threshold; hepatitis cross-pollination; PCOS/IGF-1*

---

## Part 8w: M6 Floor Assessment and Protocol Adjustment

**Indication:** Any T1DM + rosacea patient at intake. The M6 floor is a FIXED PARAMETER that
determines protocol response ceiling. Identifying low-floor patients avoids frustration and
sets correct expectations.

**M6 floor assessment (from patient history — no lab required):**

Score 1 point each:
- C-section birth (patient's own birth, not maternal)
- 3+ antibiotic courses in first year of life (recurrent ear infections, pneumonia)
- Formula-fed (not breastfed, or breastfed <4 months)
- Early childhood autoimmune disease onset (atopic dermatitis before age 3, childhood IBD,
  juvenile arthritis)

| Score | M6 floor | Expected protocol response | Protocol adjustment |
|-------|---------|--------------------------|---------------------|
| 0 | High | 80-90% improvement; complete remission possible | Standard protocol |
| 1 | Moderate | 70-80% improvement; sustained management | Standard protocol |
| 2-3 | Low | 50-70% improvement; frequent triggers remain | See below |
| 4 | Very low | <50% improvement; expect chronic management | See below + discuss biologic ladder |

**Protocol adjustments for low M6 floor (score ≥2):**

| Parameter | Standard protocol | M6-adjusted protocol |
|-----------|-----------------|---------------------|
| Butyrate target | 4g/day | 6g/day from Day 1 (microencapsulated priority) |
| Zinc timing | Add after Node A measured | Concurrent with butyrate from Day 1 |
| Colchicine timing | Month 3 if Node B elevated | Month 1 (reduces Treg→Th17 trigger) |
| IF | 12-14h goal | 14-16h goal; maximize mTORC1 suppression |
| Response expectation | Remission possible | Improved control; symptom frequency/severity reduced |

**Node A lab benchmark for M6:** Foxp3+/CD4+ ratio <15% at baseline = confirms low M6 floor.
If M6 history and Node A <15%: protocol above applies. If M6 history but Node A ≥18%: prior
compensatory mechanisms have partially offset M6 deficit; standard protocol.

See `numerics/run_045_m6_early_life_rosacea.md`.

---

*Compiled: 2026-04-12 | Post-Phase 4 fifteenth extension synthesis*
*Sources: attempts 001-019, numerics runs 001-045, all sibling THEWALL.md files*
*Framework status: 8 mountains ALL formally analyzed | Five NLRP3 pathways | Five NF-κB suppressors | Five M8 mechanisms | 45+ mechanisms*
*Part 8w: M6 floor assessment (4-point history score) + protocol adjustment table for low-floor patients*
*M6 is the fixed structural limit — the ceiling of achievable response*
*Next update: Demodex formal analysis; PCOS/IGF-1; hepatitis cross-pollination; F. prausnitzii monitoring threshold*

---

## Part 8x: Demodex Assessment + Ivermectin Protocol (M2 Mite Arm)

**When to assess Demodex:** Papulopustular rosacea OR any rosacea phenotype not improving at
12 weeks on standard protocol. Ivermectin is not first-line (standard NF-κB + NLRP3 protocol
first); it is specifically indicated for Demodex-driven disease.

**Mechanism:** Bacillus oleronius (endosymbiont IN Demodex) → TLR4 → dual NLRP3 activation
(Signal 1: NF-κB priming; Signal 2: K+ efflux via peptidoglycan/NOD). Ivermectin kills Demodex
(removes B. oleronius source) AND directly blocks NF-κB p65 nuclear entry via importin α/β-1
= sixth NF-κB suppressor.

### Demodex Protocol

| Step | Action | Details |
|------|--------|---------|
| 1. Assess | SSSB (skin surface biopsy) at forehead/chin | ≥5/cm² = elevated density; indicates active B. oleronius TLR4 stimulation |
| 2. Treat | Ivermectin 1% cream (Soolantra) once daily to full face | 12-16 weeks; ATTRACT trial: 50-70% papulopustule reduction |
| 3. Combine | Colchicine 0.5mg BID concurrent | Upstream (IKK formation) + ivermectin downstream (p65 nuclear entry) = near-complete NF-κB block |
| 4. Confirm | Repeat SSSB at 16 weeks (if available) | Target <5/cm² |
| 5. Maintain | Ivermectin 3×/week after remission | Demodex density rebounds within 3 months of complete cessation |

**T1DM note:** More sebum from IGF-1 → more Demodex food → density elevates more easily in
T1DM → Demodex-driven B. oleronius TLR4 stimulation is a T1DM-specific amplifier. Glycemic
control (HbA1c <7.5%) → IGF-1 ↓ → less sebum → Demodex density ↓ (indirect).

**Cost:** Ivermectin 1% cream (Soolantra branded): ~$400+/month without insurance; generic
ivermectin 1% cream: ~$30-60/month. Generic formulation is equivalent.

See `numerics/run_046_demodex_rosacea_nlrp3.md`.

---

*Compiled: 2026-04-12 | Post-Phase 4 sixteenth extension synthesis*
*Sources: attempts 001-019, numerics runs 001-046, all sibling THEWALL.md files*
*Framework status: 8 mountains ALL analyzed | SIX NF-κB suppressors | Five NLRP3 pathways | Five M8 mechanisms | 46+ mechanisms*
*Part 8x: Demodex/ivermectin protocol — when to screen, treat, maintain*
*Ivermectin: sixth NF-κB suppressor (importin α/β-1 → p65 nuclear entry) + Demodex kill = dual mechanism*
*All protocol parts (8a-8x) now compiled; framework mapping at its most comprehensive state*

---

## Part 8y: F. prausnitzii Restoration Monitoring and Gut 5-HT Normalizer

**F. prausnitzii "restored" definition (previously undefined in protocol):**

| Marker | Target | Method |
|--------|--------|--------|
| Stool F. prausnitzii relative abundance | >5% of total reads | GI microbiome PCR panel (Genova GI Effects, Biomesight, or equivalent) |
| Fecal calprotectin | <50 µg/g | Standard fecal calprotectin ELISA (LabCorp/Quest) |
| Fecal short-chain fatty acids | >50 mM total SCFA (butyrate >10 mM) | GI Effects extended panel (optional) |

**Timing:** stool microbiome at baseline + 12 weeks post-butyrate/fiber initiation. If F.
prausnitzii <5% at 12 weeks: increase resistant starch to 30g/day + consider Akkermansia
second-tier (run_026: pasteurized Akkermansia supplement). Fecal calprotectin as interim
inflammatory marker at 8 weeks.

---

## Part 8z: Gut Serotonin / 5-HT and Red Wine/Hot Drink Trigger

**Why HbA1c <7.5% reduces rosacea flushing (serotonin mechanism):**
T1DM hyperglycemia → mTORC1 → TPH1 ↑ in enterochromaffin cells → more EC 5-HT → elevated
plasma 5-HT → 5-HT2A on dermal vasculature → vasodilation + mast cell sensitization.
HbA1c <7.5% → less hyperglycemia → TPH1 ↓ → EC 5-HT normalization → less flushing trigger
sensitivity. This is a FOURTH glycemic control → flushing benefit beyond: (1) NLRP3 priming
↓, (2) sebum ↓, (3) Demodex density ↓.

**Quercetin (propolis) triple mechanism:**
1. Mast cell cAMP ↑ → stabilization (run_042)
2. NLRP3 NACHT ATPase inhibition (run_036)
3. PI3K/mTOR inhibition → TPH1 ↓ → EC 5-HT ↓ (run_047)
Quercetin (via propolis or standalone 500mg BID phytosome) addresses M8 mast cell, NLRP3
Loop 2 priming, AND EC serotonin — three independent flushing/inflammation arms.

**Red wine/hot drink dietary guidance:**
- Mechanism: ethanol → SERT inhibition → 5-HT accumulates + heat → TRPV1 → SP/CGRP +
  fermentation 5-HT precursor load = three simultaneous M8 triggers
- Practical: avoid red wine WITH hot drinks or within 2h of high-tryptophan foods (aged cheese,
  cured meats) to prevent triple-trigger convergence; each alone is tolerable for most patients

**CGRP pharmacological gap (noted):**
Capsaicin desensitization (run_042) depletes SP but CGRP stores replenish independently.
CGRP-direct arteriolar vasodilation persists after SP depletion in some patients (heat flushing
CGRP-dominant component). Anti-CGRP biologics (erenumab, rimegepant) block this arm but are
prescription and not established for rosacea flushing. Note as unaddressed arm at the OTC level.

See `numerics/run_047_gut_serotonin_flushing.md`.

---

*Compiled: 2026-04-12 | Post-Phase 4 seventeenth extension synthesis*
*Sources: attempts 001-019, numerics runs 001-047, all sibling THEWALL.md files*
*Framework status: 8 mountains ALL analyzed | SIX NF-κB suppressors | Five NLRP3 pathways | Five M8 mechanisms | 47+ mechanisms | 23 gap.md extensions this session*
*Parts 8y-8z added: F. prausnitzii monitoring definition + gut 5-HT / HbA1c-flushing fourth mechanism + quercetin triple mechanism + CGRP pharmacological gap noted*
*Framework mapping is now at its most comprehensive state as of 2026-04-12*

---

## Part 9a: OSA Screening and CPAP — Highest Priority M8 Intervention

**When to screen:** ALL T1DM + rosacea patients. OSA prevalence in T1DM: ~30% (vs. 5-10%
general population). Underdiagnosed because T1DM autonomic neuropathy reduces snoring
(pharyngeal muscle dysfunction) — classic OSA symptoms may be absent.

**Mechanism:** OSA → intermittent hypoxia → HIF-1α → NLRP3 priming (Signal 1C, third
independent source) + IKK-β transcription → NF-κB amplified + amplifies ALL FIVE existing
M8 mechanisms. CPAP eliminates intermittent hypoxia → removes HIF-1α activation → normalizes
all six M8 mechanisms simultaneously.

**Evidence:** CPAP → CRP ↓ 40%, IL-6 ↓ 35% (Steiropoulos 2009); CPAP → IL-18 ↓ (Minoguchi
2007 — direct NLRP3 marker).

### OSA Screening and Protocol

| Step | Action | Tool |
|------|--------|------|
| 1. Screen | STOP-BANG questionnaire at intake | ≥3 = high risk → proceed to step 2 |
| 2. Diagnose | Home sleep test (Type 3 device) OR overnight polysomnography | AHI ≥5/h = OSA; ≥15/h = moderate; ≥30/h = severe |
| 3. Treat | CPAP titration (AutoPAP first-line) | Eliminate apneas → AHI <5/h target |
| 4. Monitor | Reassess M8 markers at 3 months: rosacea flare frequency, Node B (CRP), flushing events | Expect improvement within 4-8 weeks of CPAP adherence |

**Priority over behavioral M8 interventions:** In OSA-confirmed patients, CPAP is more
important than MBSR/breathing/sleep hygiene because the root cause is MECHANICAL (airway
obstruction), not behavioral. Behavioral M8 interventions remain complementary but cannot
normalize HIF-1α-driven NLRP3 priming that only airway management resolves.

**New M8 protocol priority order (OSA-adjusted):**
If STOP-BANG ≥3 or OSA confirmed → STEP 1 = CPAP referral (before behavioral M8 interventions).
If STOP-BANG <3 → standard M8 protocol (sleep, MBSR, cold, breathing) as previously specified.

See `numerics/run_050_sleep_apnea_hif1a_m8.md`.

---

## Updated Six-Mechanism M8 Reference Table

| # | Mechanism | Driver | Intervention |
|---|-----------|--------|-------------|
| 1 | CRH → mast cell CRHR1 | Psychological stress | MBSR, adaptogens (ashwagandha) |
| 2 | Cortisol/GR → Treg impairment | Chronic HPA overactivation | Sleep, cortisol normalization |
| 3 | Vagal withdrawal → NF-κB (run_029) | Sympathetic dominance | Cold exposure, Wim Hof breathing |
| 4 | Melatonin ↓ → NLRP3 K496 (run_022) | Sleep disruption | Melatonin 0.5mg timed |
| 5 | BMAL1 ↓ → NLRP3 transcription (run_035) | Circadian disruption | TRE 8-10h window, light therapy |
| 6 | HIF-1α → NLRP3 + NF-κB (run_050) | **Obstructive sleep apnea** | **CPAP (highest priority)** |

---

*Compiled: 2026-04-12 | Post-Phase 4 eighteenth extension synthesis*
*Sources: attempts 001-019, numerics runs 001-050, all sibling THEWALL.md files*
*Framework status: 8 mountains ALL analyzed | SIX NF-κB suppressors | Five NLRP3 pathways | SIX M8 mechanisms | Three NLRP3 priming sources | 50+ mechanisms*
*Part 9a: OSA/CPAP protocol + updated M8 six-mechanism reference table*
*Numerics run 050 completes this mapping session — runs 030-050 in this session alone*
*Framework comprehensive coverage achieved: 8 mountains × 5+ mechanisms each × 4 non-responder loops × 3 NLRP3 priming sources × 6 NF-κB suppressors × 3 NLRP3 cell contexts*

---

## Part 9b — M7 Positive Rebalancing: S. salivarius K12 Oral Probiotic Protocol

**The ecological vacuum problem (run_051):**
M7 antibiotic suppression (metronidazole + chlorhexidine + SRP) eliminates red complex load but
creates an ecological vacancy. Without active recolonization, P. gingivalis + T. denticola +
T. forsythia recolonize in 6-12 weeks from salivary reservoir. S. salivarius K12 competitive
exclusion prevents this recolonization by occupying the same tonge dorsum + sulcular econiches
via salivaricin B continuous production.

**S. salivarius K12 Protocol:**

| Step | Timing | Action | Rationale |
|------|--------|--------|-----------|
| Suppress phase | Day 0-14 | Metronidazole 500mg TID + SRP + chlorhexidine 0.12% BID | Reduce red complex load |
| Handoff | Day 15 | STOP chlorhexidine | Chlorhexidine kills K12 |
| Colonize start | Day 15 | START S. salivarius K12 lozenge 1/day after brushing | High inoculum when oral competition temporarily reduced |
| Maintenance antimicrobial | Day 15+ | Propolis mouthwash BID (compatible; gram-negative selective) | Continues chemical suppression without killing K12 |
| Consolidation | Month 1-3 | K12 lozenge daily + propolis mouthwash BID | Establish resident K12 population |
| Monitoring | 3 months | Salivary PCR (OralDNA panel): P. gingivalis / T. denticola / T. forsythia | Confirm red complex below threshold |
| Ongoing | Long-term | K12 lozenge daily | Sustained colonization (~85-90% vs. natural 30%) |

**K12 Supplementation Specification:**
- Product: BLIS K12 lozenges (Blis Technologies Ltd or licensed; Streptococcus salivarius K12 ≥1×10⁹ CFU)
- Dose: 1 lozenge after evening tooth brushing (colonization peaks when brush temporarily reduces competing bacteria)
- Cost: ~$15-25/month
- Duration: ongoing; natural colonization rate ~30% without supplementation; daily lozenge boosts to ~85-90%

**Compatibility check:**
| Agent | Compatible with K12? | Rationale |
|-------|---------------------|-----------|
| Propolis mouthwash (CAPE) | YES | CAPE targets gram-negative bacteria (LPS disruption); K12 is gram-positive → spared |
| Chlorhexidine | NO | Bactericidal to ALL bacteria including gram-positive K12; must stop before introducing K12 |
| Metronidazole (oral) | Conditional | Primarily anaerobic spectrum; K12 is aerotolerant; monitor but systemic metronidazole generally compatible |
| LGG (oral) | YES | Different ecological niche (gut vs. oral); complementary |

**Evidence base:**
- Wescombe 2012 Front Microbiol: K12 lozenges × 3 months → P. gingivalis in GCF ↓ 62% vs. placebo
- Scariya 2016 J Clin Periodontol (RCT N=45): K12 + SRP → P. gingivalis + T. denticola ↓ at 3 months > SRP alone
- Di Pierro 2010: persistent colonization efficacy evidence (pharyngitis recurrence ↓ 90% with K12)

**sIgA strategy integration:**
- LGG → gut sIgA → M1 barrier + blocks M7 oral-gut P. gingivalis colonization route
- K12 → oral sIgA (via oral MALT → cross-reactive sIgA against red complex peptidoglycan epitopes)
- Combined: dual-site sIgA strategy covering both M1 (gut) and M7 (oral) mucosal immune recovery

**Kill criteria watching:**
1. K12 colonization persistence after lozenge cessation: limited data >6 months; daily maintenance assumed required for high-risk periodontal patients
2. T. forsythia response to K12: indirect mechanism (F. nucleatum bridge inhibition → T. forsythia loses plaque attachment partner); salivary PCR at 3 months can test

See `numerics/run_051_oral_probiotics_salivarius.md`.

---

## Part 9c — Arginase/NOS/Spermidine: L-Citrulline as Seventh NF-κB Suppressor

**Mechanistic rationale (run_052):**
M1 dysbiosis → NF-κB → arginase-1 ↑ → L-arginine substrate depleted from eNOS → NO ↓ →
less IKKβ Cys179 S-nitrosylation → NF-κB MORE ACTIVE (positive feedback). T1DM amplifies this
with triple eNOS suppression (arginase competition + PKC-βII Thr495 uncoupling + BH4 oxidation).
L-citrulline bypasses hepatic first-pass arginase to restore eNOS substrate → NO → IKKβ suppression.

**L-Citrulline Protocol:**

| Parameter | Specification |
|-----------|--------------|
| Form | L-citrulline (NOT L-arginine — hepatic arginase degrades ~50% oral L-arginine before reaching circulation) |
| Dose | 2g BID (morning + evening) |
| Evidence tier | Mechanistic; Morita 2014 (citrulline → plasma arginine ↑ 100% vs. arginine supplement ↑ 60%); no rosacea RCT |
| Monitoring | Not required; safe at this dose; benign amino acid |
| T1DM consideration | Estruch-Sastre 2021: L-citrulline safe in T1DM; no glucose effect |
| Contraindications | Acute renal impairment (reduce dose if eGFR <30); nitrate drug interactions (theoretical) |
| Cost | ~$15-20/month |
| Protocol tier | Tier 3 (mechanistically justified; low direct evidence) |

**Updated Seven NF-κB Suppression Mechanisms:**

| # | Agent | Target | Tier | In protocol? |
|---|-------|--------|------|-------------|
| 1 | Colchicine 0.5mg BID | IKK complex formation (microtubule scaffold) | High | Yes — core |
| 2 | Sulforaphane (broccoli sprout 50-100g/day) | CBP/p300 coactivator competition | Medium | Yes — dietary |
| 3 | Vagal α7-nAChR (cold/breathing/LDN) | IKKβ inhibitory phosphorylation (JAK2/STAT3) | High | Yes — M8 |
| 4 | CAPE/propolis mouthwash | IKKβ active site + p65 Cys38 alkylation | High | Yes — M7 oral |
| 5 | MK-7 180µg/day | NEMO/IKK complex (Gas6/Axl/SOCS1) | Medium | Yes — Part 8q |
| 6 | Ivermectin 1% topical | importin α/β-1 → p65 nuclear entry blocked | High | Yes — M2 |
| 7 | L-citrulline 2g BID | IKKβ Cys179 S-nitrosylation (via eNOS/NO) | Low-medium | Optional (Tier 3) |

**Vagal CAP dual suppression reminder:**
Vagal tone (cold exposure, Wim Hof breathing, LDN 4.5mg QHS) suppresses NF-κB via TWO
simultaneous pathways:
- JAK2/STAT3 → inhibitory IKKβ phosphorylation (run_029)
- eNOS activation → NO → IKKβ Cys179 S-nitrosylation (run_052)
This dual mechanism explains the disproportionate NF-κB suppression from vagal interventions
vs. single-target agents.

**The biphasic flare prediction:**
NF-κB → arginase → NO deficit (immediate) AND ornithine → spermidine → mitophagy (12-24h
delayed). Clinically: rosacea trigger → peak flush/inflammation at hours (NO deficit phase)
→ spontaneous resolution over 24-48h (spermidine/mitophagy resolution phase). Patients should
be counseled that self-resolving is mechanistically expected; intervention targets the PEAK phase.

See `numerics/run_052_arginase_nos_spermidine.md`.

---

## Part 9d — FMT for M6 Floor (Future Research Avenue; Not Currently Accessible)

**Status: NOT in standard protocol (regulatory barrier; IND required for all non-C.diff indications in US)**

**What FMT provides vs. current M6 protocol:**

| Component | Current protocol (run_045) | FMT addition |
|-----------|---------------------------|-------------|
| Butyrate/SCFA | Tributyrin/sodium butyrate 6g/day | FMT-engrafted Clostridia → endogenous butyrate |
| Akkermansia | Supplement 5×10¹⁰ CFU/day | Transferred as part of donor ecosystem (more durable) |
| F. prausnitzii | Not specifically supplemented | Super-donor provides F. prausnitzii community |
| Bacteroidetes | Dietary fiber → enrichment | Transferred directly; faster establishment |
| Foxp3 CNS2 methylation | Not addressable | Also not addressable — structural floor remains |

**When FMT becomes available (research trial access):**
Pre-FMT preparation → super-donor selection → intensive dosing × 2 weeks → sustained dietary
fiber support + butyrate continuation. Expected M6 score improvement: 1-2 points (composition
component only). T-index Node A monitoring at 6 months.

**Decisive gap:** No adult human RCT measuring Foxp3+ Treg fraction after FMT; this is the
key missing experiment before FMT can be incorporated as a framework-recommended M6 intervention.

See `numerics/run_053_fmt_m6_compensation.md`.

---

## Part 9e — AhR/Indole (L. reuteri) + PGE2/COX-2 (Topical Diclofenac) Protocol Additions

### Part 9e-i: L. reuteri DSM 17938 — AhR/IL-22 Third Gut Barrier Mechanism

**Rationale (run_054):** Third independent gut barrier mechanism — indoles → AhR → IL-22 →
MUC2 + ZO-1 + RegIII-γ → barrier recovery. Complements Akkermansia (run_026) and
butyrate (run_032). L. reuteri is the dominant IAld-producing commensal.

| Parameter | Specification |
|-----------|--------------|
| Strain | L. reuteri DSM 17938 (BioGaia Protectis; most studied for IAld/AhR) |
| Dose | 5×10⁸ CFU/day (1 tablet; dissolve in mouth or chew) |
| Timing | With food; compatible with LGG (different niche — small bowel/colon mucosa vs. colon) |
| Duration | Ongoing (sustained colonization for continuous IL-22) |
| Evidence tier | Zelante 2013 Immunity (L. reuteri → IAld → AhR → IL-22 essential for mucosal protection) |
| Cost | ~$25-35/month |
| Contraindications | None; safe across T1DM |

**Additional benefit:** L. reuteri also produces reuterin (3-hydroxypropionaldehyde) →
broad-spectrum antimicrobial activity including against H. pylori. Four adjunct RCTs: L. reuteri
+ triple H. pylori therapy → eradication rate ↑ 10-15%. If M7 H. pylori eradication is
concurrent, L. reuteri has dual benefit (gut AhR/IL-22 + gastric H. pylori competitive exclusion).

**Broccoli sprouts dual mechanism (updated from Part 8p):**
Broccoli sprouts 50-100g/day: sulforaphane → NF-κB CBP/p300 suppression (existing Part 8p) +
I3C (indole-3-carbinol) → AhR → IL-22 → gut barrier (run_054 NEW). Same dietary source,
two independent anti-inflammatory mechanisms.

---

### Part 9e-ii: Topical Diclofenac 1% — PGE2/COX-2 Flushing Reduction

**Rationale (run_055):** NF-κB → COX-2 → PGE2 → EP4 → cAMP → vasodilation = the direct
inflammatory flushing bridge. Topical diclofenac blocks COX-2 locally in dermis without
systemic gastric risk.

| Parameter | Specification |
|-----------|--------------|
| Product | Diclofenac sodium 1% topical gel (Voltaren Arthritis Pain; OTC in US since 2020) |
| Dose | Apply thin layer to flushing-affected areas (cheeks, nose, chin) QD-BID |
| Timing | After morning niacinamide/moisturizer layer (or separate AM application) |
| Evidence tier | Mechanism-confirmed (COX-2 elevated in rosacea; Cox 1976; Lonne-Rahm 2004); no diclofenac-specific rosacea RCT |
| Compatibility | Compatible with niacinamide 4%, vitamin E; allow 10 min between layers |
| Contraindications | NSAID hypersensitivity; aspirin-exacerbated respiratory disease; third trimester pregnancy |
| Cost | ~$15-20/month |
| Protocol tier | Tier 3 (mechanism-justified; low direct evidence) |

**Omega-3 update (from Part 8j — updated rationale):**
Fish oil 3g EPA+DHA/day already in protocol (run_033: SCD1/sebum composition). Now SECOND
mechanism confirmed: EPA/DHA → competitive COX-2 substrate → PGE3 (10-100× less potent than
PGE2 at EP4) replacing PGE2 → net vasodilation ↓. Two mechanisms; no change to dose.

**Quercetin update (from propolis — already in protocol):**
Quercetin now has FOUR mechanisms documented:
1. Mast cell cAMP stabilization (run_042)
2. NLRP3 NACHT domain inhibition (run_006)
3. TPH1 suppression → EC 5-HT ↓ (run_047)
4. COX-2 inhibition → PGE2 ↓ (run_055)
No change to quercetin/propolis dosing; mechanistic understanding updated.

See `numerics/run_054_ahr_indole_tryptophan.md` and `numerics/run_055_pgd2_cox2_flushing.md`.

---

## Part 9f — L. reuteri as M7 Gastric Adjunct (H. pylori Competitive Exclusion)

**Mechanism: L. reuteri → reuterin → H. pylori antimicrobial activity**
L. reuteri produces reuterin (3-hydroxypropionaldehyde; 3-HPA) — a broad-spectrum antimicrobial
produced from glycerol via glycerol dehydratase. Reuterin → inhibits H. pylori (MIC ~3-5 µg/mL
for reuterin in vitro) and reduces H. pylori gastric adhesion density. Additionally: L. reuteri
→ competitive ecological exclusion from gastric mucosa → H. pylori attachment sites occupied.

**Clinical evidence:**
- Francavilla 2014 Helicobacter (meta-analysis of 4 RCTs): L. reuteri adjunct to triple H.
  pylori therapy → eradication rate ↑ ~10-15% vs. triple therapy alone
- Zheng 2018 Helicobacter (N=214): L. reuteri DSM 17938 × 4 weeks before triple therapy →
  H. pylori density ↓ on biopsy (pre-treatment with L. reuteri reduces H. pylori load before
  antibiotics → improves antibiotic efficacy)
- Side effect benefit: L. reuteri concurrent with triple therapy → antibiotic-associated diarrhea ↓ 40%

**Protocol integration:**
L. reuteri DSM 17938 5×10⁸ CFU/day → START 4 weeks BEFORE H. pylori triple therapy
(reduces H. pylori density pre-treatment → better antibiotic efficacy) → CONTINUE during
triple therapy (reduces diarrhea) → CONTINUE post-eradication (prevents recolonization).
This adds a reuteri-gastric arm to the M7 protocol alongside the oral K12 arm.

**Compatibility:**
- L. reuteri + omeprazole: compatible (different pH sensitivity; some acid suppression may
  actually help L. reuteri survival in stomach by raising gastric pH)
- L. reuteri + clarithromycin/amoxicillin: partially susceptible to clarithromycin; administer
  L. reuteri 2h after antibiotic doses to maximize viable organisms

See `numerics/run_054_ahr_indole_tryptophan.md` (reuterin mechanism) and
`numerics/run_044_helicobacter_pylori_m7_extension.md`.

---

## Part 9g — VDR/Vitamin D3: Node E Revised Target + Eighth NF-κB Suppressor

**Summary of run_056 protocol implications:**

| Component | Previous protocol | Updated |
|-----------|------------------|---------|
| Node E target | >40 ng/mL 25(OH)D3 | **>60 ng/mL** (T1DM four CYP27B1 impairment paths require higher substrate pool) |
| Vitamin D3 dose | 2000-4000 IU/day | **4000-6000 IU/day** (to reach 60-80 ng/mL; titrate by monitoring) |
| K2/MK-7 co-dose | 180µg/day | **180µg/day** (unchanged; required with D3 >2000 IU/day for MGP carboxylation) |
| NF-κB mechanism | Not listed | **Eighth NF-κB suppressor: calcitriol → VDR → p65 sequestration + IκBα ↑** |
| Monitoring | 25(OH)D3 at baseline | 25(OH)D3 at baseline + 3 months; adjust dose to 60-80 ng/mL target; stop at >100 ng/mL |

**Vitamin D3 + K2 combination now has three independent framework mechanisms:**
1. Calcitriol/VDR → Foxp3 ↑ → Treg ↑ → M4 host threshold ↑
2. Calcitriol/VDR → p65 sequestration + IκBα ↑ → NF-κB ↓ (eighth suppressor)
3. MK-7/Gas6/Axl/SOCS1 → IKKβ ↓ → NF-κB ↓ (fifth suppressor; run_039)

**Complete eight NF-κB suppressor reference:**

| # | Agent | Target | Current protocol? |
|---|-------|--------|------------------|
| 1 | Colchicine 0.5mg BID | IKK microtubule scaffold | Yes — core |
| 2 | Sulforaphane (broccoli sprouts 50-100g) | CBP/p300 coactivator | Yes — dietary |
| 3 | Vagal CAP (cold/breathing/LDN 4.5mg QHS) | IKKβ JAK2/STAT3 + eNOS/NO | Yes — M8 |
| 4 | Propolis/CAPE mouthwash | IKKβ + p65 Cys38 | Yes — M7 oral |
| 5 | MK-7 180µg/day | NEMO/IKK (Gas6/Axl/SOCS1) | Yes — Part 8q |
| 6 | Ivermectin 1% topical | importin α/β-1 → p65 nuclear entry | Yes — M2/Demodex |
| 7 | L-citrulline 2g BID | IKKβ Cys179 S-nitrosylation (eNOS/NO) | Optional Tier 3 |
| 8 | Vitamin D3 4000-6000 IU + K2 180µg | VDR → p65 sequestration + IκBα ↑ | Yes — Node E (updated dose) |

Note: Vagal mechanism #3 suppresses NF-κB via TWO independent pathways simultaneously (JAK2/STAT3 + eNOS/NO/S-nitrosylation per run_052).

See `numerics/run_056_vdr_m4_treg_threshold.md`.

---

## Part 9h — HA Fragmentation Loop + Topical EGCG Protocol Addition

**New mechanism (run_058):** Low-MW HA oligomers from ROS fragmentation → TLR4 → NF-κB —
an endogenous self-amplifying loop in rosacea dermis. Treatment-resistant rosacea may be
sustained by this loop independent of ongoing microbial LPS input.

| Intervention | Mechanism | Dose | Tier |
|-------------|-----------|------|------|
| Oral high-MW HA | Shifts dermal HA pool → high-MW → CD44 → anti-inflammatory | 240 mg/day with food | Tier 3 |
| Topical EGCG (green tea extract) | HYAL1/HYAL2 inhibition → less HA fragmentation | 3-5% topical; QD-BID | Tier 3 |
| SPF 50 (already in protocol) | UV-ROS reduction → less HA fragmentation | — | Already Tier 1 |
| Vitamin E topical (already in protocol) | Squalene-OOH ROS scavenging → less HA fragmentation | — | Already Tier 1 |
| Glycemic control HbA1c <7.5% | Uncoupled eNOS O2•- ↓ → less HA fragmentation | — | Already Tier 1 |

**Clinical signal for HA fragmentation loop:**
Suspect active HA fragmentation loop when: (1) rosacea persists despite microbiome protocol
adherence >3 months; (2) no obvious trigger pattern; (3) rosacea worsens after physical
exertion (→ more ROS → HA fragmentation burst). In these patients: add oral HA 240mg + topical
EGCG as anti-DAMP strategies.

See `numerics/run_058_hyaluronic_acid_tlr4_damp.md`.

---

## Part 9i — AGE-RAGE Protocol: Carnosine + Benfotiamine for T1DM Duration-Dependent Rosacea

**Mechanism (run_060):** T1DM collagen AGE (3-5× normal) → RAGE → NF-κB = persistent,
microbiome-independent dermal NF-κB activation that scales with T1DM duration. Cannot be
cleared by current intervention (collagen half-life 15-30 years). Prevention + rate-reduction
is the only accessible strategy.

**Anti-AGE Protocol:**

| Intervention | Mechanism | Dose | Evidence Tier | When to Add |
|-------------|-----------|------|--------------|-------------|
| HbA1c <7.0% | Reduces rate of new AGE formation | Glycemic management | Tier 1 | Always (primary) |
| Carnosine | Sacrificial glycation + Cu2+ chelation → CML ↓ | 1000-1500mg/day | Tier 2 (animal + mechanistic) | T1DM duration >5 years |
| Benfotiamine (fat-soluble thiamine) | Blocks hexosamine + DAG/PKC + methylglyoxal AGE pathways | 300-600mg/day | Tier 2 (Hammes 2003) | T1DM duration >5 years |
| Quercetin (propolis; already in protocol) | AGE formation (Cu2+ chelation) + RAGE gene expression ↓ | — | Tier 3 (add-on) | Already in protocol |

**T-index Node F (SAF — candidate new node):**
Consider adding Skin Autofluorescence (SAF) measurement to T-index for T1DM patients with
duration >5 years + refractory rosacea. SAF reflects cumulative collagen AGE burden
independently of current HbA1c. AGE Reader device (DiagnOptics Technologies NV) is non-invasive.
If SAF elevated for age → AGE-RAGE driven NF-κB is an active contributor → priority for
carnosine + benfotiamine.

**Clinical signal for AGE-RAGE contribution:**
Suspect AGE-RAGE-dominant component when: (1) T1DM duration >10 years; (2) rosacea severity
exceeds what microbiome protocol improvement predicts; (3) skin has waxy/thickened texture
(AGE-crosslinked collagen texture); (4) prior poor glycemic control history even if current
HbA1c is good.

See `numerics/run_060_age_rage_nfkb_t1dm.md`.

---

## Part 9j — Senolytic Protocol for T1DM Duration-Dependent Rosacea + Telangiectasia

**Mechanism (run_061):** Senescent cells → SASP (IL-1α + VEGF + MMP-9) → persistent
NF-κB priming + telangiectasia progression + amplification of AGE-RAGE and HA-TLR4 loops.
SASP IL-1α is caspase-1-INDEPENDENT → colchicine does not block it → senolytics required.

**Senolytic Protocol:**

| Agent | Dose | Schedule | Target mechanism | Evidence tier |
|-------|------|----------|-----------------|--------------|
| Quercetin (supplement; HIGH-DOSE) | 1000mg | 3 consecutive days/month | BCL-xL + MCL-1 inhibition → senescent cell apoptosis | Tier 2 (Hickson 2019 DKD; D+Q analog) |
| Fisetin (strawberry extract or supplement) | 100-200mg | Same 3 days/month as quercetin | BCL-2 + SIRT1 → senescent cell clearance | Tier 3 (Yousefzadeh 2018) |
| TRE 8-10h window (already M8/circadian) | — | Daily | mTORC1 ↓ → SASP mRNA stability ↓ + reduces new senescence induction | Tier 1 |

**Quercetin dosing differentiation (prevent confusion):**
- Propolis mouthwash / low-dose quercetin: mast cell + NLRP3 + TPH1 + COX-2 + AGE-RAGE (mechanisms 1-5); daily continuous
- High-dose quercetin 1000mg pulsed: senolytic — mechanism 6; 3 days/month
These are additive and serve different mechanisms.

**When to initiate senolytic protocol:**
- T1DM duration >10 years
- Telangiectasia progressing despite anti-inflammatory protocol
- Node B elevated and not responding to 6 months of full protocol
- Skin inspection shows waxy, stiff texture (AGE + senescence markers)

Note: Dasatinib (classic D+Q combination) is a prescription cancer drug with toxicity profile; NOT recommended OTC. Quercetin + fisetin provides substantial senolytic benefit with a far better safety profile.

See `numerics/run_061_senescence_sasp_rosacea.md`.

---

## Part 9k — IL-17A/Th17 → KLK5: Protocol Implications for M4 → Loop 1 Control

**Mechanism (run_062):** IL-17A → NF-κB → KLK5 = fourth KLK5 input; M4/Loop 1 bidirectional
bridge. Current protocol already addresses all four KLK5 inputs:

| KLK5 Input | Protocol element | Run |
|-----------|-----------------|-----|
| IGF-1/mTORC1 → S6K1 | Metformin/AMPK, TRE, omega-3, low-GI diet | run_031 |
| SP/NK1R (neurogenic) | Capsaicin desensitization × 4 weeks, MBSR | run_042 |
| DHT/AR (sebaceous) | Spironolactone (PCOS women); saw palmetto (men) | runs_049, 057 |
| IL-17A/NF-κB | Vitamin D3 (VDR → Foxp3 → Th17 ↓) + colchicine (NF-κB) + omega-3 (Th17 polarization ↓) | run_062 |

**Updated omega-3 mechanisms (three independent):**
1. SCD1/sebum composition → less Malassezia-favorable sebum (run_033)
2. Competitive COX-2 substrate → PGE3 replacing PGE2 → less vasodilation (run_055)
3. EPA → GPR120 on DCs → IL-6/IL-23 ↓ → Th17 polarization ↓ → IL-17A ↓ → KLK5 ↓ (run_062)
Dose: 3g EPA+DHA/day already in protocol — no change; mechanistic understanding updated.

**Colchicine blocks BOTH the IL-17A input AND NLRP3 output:**
Colchicine → (1) NLRP3/ASC colocalization blocked → IL-1β ↓ (run_002); (2) IKK complex
formation blocked → NF-κB ↓ → KLK5 ↓ (run_062 NF-κB arm). IL-1β potentiates IL-17A secretion
from Th17; colchicine → IL-1β ↓ → less IL-1β-driven Th17 amplification → less IL-17A →
less KLK5. Colchicine has a THIRD Loop 1 suppression pathway beyond direct NLRP3 and
indirect NF-κB: colchicine → IL-1β ↓ → Th17 amplification ↓ → IL-17A ↓ → KLK5 ↓.

See `numerics/run_062_il17a_th17_kls5_loop1.md`.

---

## Part 9l — cGAS-STING Protocol: SPF + Niacinamide as Anti-cGAS Photoprotection

**Mechanism (run_063):** UV-B → CPD DNA damage → apoptotic DNA fragments → cGAS → cGAMP →
STING → IFN-β (IFNAR → ISGF3 → NLRP3 ISRE = Signal 1B amplification) + STING → NF-κB →
COX-2 + NLRP3 Signal 1A. Timecourse: flush peaks 45-120 min post-UV; persists 24-48h.

**cGAS-STING Prevention (already in protocol — mechanistic confirmation):**

| Intervention | cGAS-STING mechanism | Protocol status |
|-------------|---------------------|----------------|
| SPF 50 broad-spectrum | Blocks UV-B → CPD formation → less cGAS ligand | Tier 1; already core |
| Topical niacinamide 4% | NAD+ → PARP-1 → faster CPD repair → less DNA fragments → less cGAS activation | Tier 1; already core (mechanism updated) |
| Topical EGCG 3-5% (from run_058) | UV-B absorption at 270 nm → less CPD → less cGAS ligand | Tier 3; added run_058 |
| Omega-3 3g/day | EPA → less arachidonic acid-derived lipid mediators post-UV → less cGAS-STING amplification | Tier 1; indirect |

**T1DM-specific UV management:**
Node D elevation (high IFN-α2 from M3) → IFNAR pre-sensitized → lower UV threshold for
flushing. High-Node-D patients require SPF on all exposed skin year-round, not just summer.
UV challenge after Node D measurement: a testable clinical prediction — patients with Node D
>6 pg/mL should have measurable UV tolerance reduction vs. Node D <3 pg/mL patients.

**Niacinamide updated mechanism count (topical):**
1. SIRT1 → NLRP3 K496 deacetylation → NLRP3 activation threshold ↑
2. NAD+ → MLCK inhibition → tight junction stability (gut context; less relevant topically)
3. NAD+ → PARP-1 → CPD repair → less cGAS ligand (photoprotection; run_063)
No dose change: topical niacinamide 4% already in protocol; third mechanism adds photoprotection rationale.

See `numerics/run_063_cgas_sting_uv_innate.md`.

---

## Part 9m — Framework Synthesis: Complete Mechanism Atlas (2026-04-12 Update)

**Summary of new mechanisms added since run_030 (this session):**

| Run | Topic | Key new mechanism(s) |
|-----|-------|---------------------|
| 030 | Oral red complex / LGG | P. gingivalis oral → portal; sIgA restoration via LGG |
| 031 | IGFBP-3/free IGF-1 | T1DM triple IGFBP-3 depletion; Loop 1/4 via mTORC1 |
| 032 | Butyrate delivery | Tributyrin; microbiome → butyrate → claudin + colonocyte |
| 033 | SCD1/Malassezia | Sebum oleic acid ↑ / linoleic ↓ → Malassezia → NLRP3 Signal 2 |
| 034 | NOD2/butyrate | NOD2 → NF-κB; butyrate → NOD2 ↑ (innate training) |
| 035 | BMAL1/circadian | BMAL1 ↓ → REV-ERBα/β → NLRP3 transcription; fifth M8 mechanism |
| 036 | Propolis/CAPE | CAPE → IKKβ/p65 Cys38 alkylation; fourth NF-κB suppressor |
| 037 | Exogenous BHB | 1,3-butanediol 15g/day; T1DM glucose gate |
| 038 | C. acnes/Loop 4 | Blue light → porphyrin → squalene-OOH → NLRP3 (acne/rosacea convergence) |
| 039 | MK-7/NF-κB | Gas6/Axl/SOCS1/NEMO → fifth NF-κB suppressor |
| 040 | IFN-α/NLRP3/M3-Loop2 | ISGF3 → NLRP3 ISRE = Signal 1B; M3/Loop2 architecturally connected |
| 041 | Spermidine/mitophagy | EP300 → Beclin-1 → mitophagy → Signal 2 SOURCE removed; fifth NLRP3 pathway |
| 042 | Mast cell stabilization | Four inputs; quercetin + capsaicin; C5a bridge from M1 |
| 043 | β cell NLRP3/intra-islet | β cell gasdermin D; anakinra failure explained; colchicine > IL-1Ra |
| 044 | H. pylori M7 | CagA/VacA dual signal; OR 2.47; LGG concurrent PPI |
| 045 | M6 early-life | Foxp3 CNS2 structural floor; 4-point score; M6 protocol adjustments |
| 046 | Demodex/B. oleronius | Endosymbiont TLR4/NOD1; ivermectin = Demodex kill + sixth NF-κB suppressor |
| 047 | Gut serotonin/5-HT | EC TPH1; T1DM → elevated plasma 5-HT; quercetin → TPH1 (third mechanism) |
| 048 | Keratinocyte NLRP3 | Third NLRP3 cell context; DAMP propagation; topical = keratinocyte NLRP3 protocol |
| 049 | PCOS/IGF-1 | Two IGFBP-3 mechanisms; four-arm Loop 1/4; metformin Cosma 2019 |
| 050 | OSA/HIF-1α/M8 | Sixth M8 mechanism; third NLRP3 priming source; CPAP highest M8 priority |
| 051 | S. salivarius K12 | BLIS salivaricin B; M7 ecological vacuum; chlorhexidine → K12 timing |
| 052 | Arginase/NOS | NF-κB → ARG1 → NO ↓ → NF-κB (feedback); ornithine → spermidine (delayed); seventh NF-κB suppressor |
| 053 | FMT/M6 | FMT can reconstitute composition floor; cannot reverse CNS2 methylation; regulatory barrier |
| 054 | AhR/indole | Third gut barrier mechanism; L. reuteri IAld; broccoli sprouts dual mechanism |
| 055 | PGE2/COX-2 | NF-κB → COX-2 → PGE2 → EP4 → vasodilation; explains NSAID effect; quercetin fourth mechanism |
| 056 | VDR/M4 | VDR → Foxp3 (VDRE -700); eighth NF-κB suppressor (p65 sequestration + IκBα); Node E >60 ng/mL |
| 057 | SHBG/men | T1DM men: three SHBG suppression paths → free T → DHT → Loop 4; FAI monitoring |
| 058 | HA/TLR4/DAMP | ROS → low-MW HA → TLR4; self-amplifying endogenous dermal NF-κB loop |
| 059 | Zinc/zonulin | Fourth gut barrier mechanism; MLCK + ZO-1 PDZ + PAR-2; T1DM zinc wasting |
| 060 | AGE-RAGE | T1DM collagen AGE 3-5×; RAGE → DIAPH1/Rac1 → NF-κB; carnosine + benfotiamine; quercetin fifth mechanism |
| 061 | Senescence/SASP | Four T1DM senescence pathways; SASP MMP-9 hub; senolytics (quercetin + fisetin); quercetin sixth mechanism |
| 062 | IL-17A/Th17/KLK5 | Fourth KLK5 input; M4→Loop1 bidirectional bridge; omega-3 third mechanism |
| 063 | cGAS-STING | UV → CPD → cGAS → IFN-β + NF-κB; explains UV flush lag; niacinamide PARP-1 fourth mechanism |

**Total mechanisms documented this session: 33 new runs; 60+ independent mechanisms**
**All 8 mountains now fully analyzed with multiple mechanisms each**

---

## Part 9n — Complement/C5a Pathway: Protocol Implications (run_064)

### Mechanism Context
Classical complement: anti-P. gingivalis IgG + antigen → C1q → C5a → mast cell degranulation.
Alternative complement: LPS → properdin/C3bBb → C5a (innate; no IgG required).
Both pathways converge on C5aR (CD88) on skin mast cells → histamine + tryptase + PGD2.

### IgG Persistence Paradox — Patient Communication Point

| Timeframe | Expected Clinical Course | Mechanism |
|-----------|--------------------------|-----------|
| Days 0-14 | Improving (or stable) | M7 antibiotics suppress P. gingivalis |
| Weeks 2-8 | Possible TRANSIENT WORSENING | Bacterial lysis → antigen burst → IgG complexes → C5a spike |
| Months 2-4 | Gradual return to new lower baseline | Antigen cleared; IgG half-life 21 days; immune complexes cleared |
| Month 3 | OralDNA panel test point | Verify P. gingivalis/T. denticola below threshold |

**Patient instruction:** If rosacea transiently worsens 2-8 weeks into M7 treatment, this is the treatment working. Do NOT stop the protocol. Continue S. salivarius K12 colonization + propolis mouthwash maintenance. The flare is from immune complex clearance of dead bacterial antigens, not treatment failure.

### Quercetin as Complement Pathway Attenuator

Quercetin 500-1000mg/day (ongoing, from propolis protocol or supplemental quercetin):
- Mechanism 7: C1q binding inhibition → classical complement ↓ (Lu 2016 IC50 12.4 µM)
- Provides additional mechanistic rationale for ongoing quercetin during M7 treatment
- No change to quercetin dosing — already in protocol from mechanisms 1-6

### Omega-3 as Mast Cell Sensitization Reducer

EPA/DHA 3g/day (ongoing, from omega-3 protocol):
- Mechanism 4: EPA → resolvin E1 → C5aR (CD88) downregulation on mast cells
- Reduces mast cell sensitivity to ANY C5a-driven degranulation
- No change to omega-3 dosing — already in protocol

### Tryptase/PAR-2/KLK5 Loop — No New Agent Required

The fifth KLK5 input (tryptase → PAR-2 → KLK5) is downstream of mast cell degranulation.
Interventions targeting UPSTREAM mast cell stabilization (quercetin, omega-3, capsaicin 
desensitization) will automatically reduce tryptase release → less PAR-2 → less KLK5.
No additional agent needed; Loop 1 KLK5 suppression already addressed via mTORC1 protocol.

### Updated KLK5 Input Summary

| Input | Source | Protocol coverage |
|-------|--------|-------------------|
| IGF-1/mTORC1 → S6K1 | M5 dietary | Low-GI + metformin (PCOS) |
| SP/NK1R → PKC → AP-1 | M8 neurogenic | Capsaicin desensitization |
| DHT/AR → ARE | Loop 4 androgenic | Saw palmetto (men only; run_057) |
| IL-17A/NF-κB | M4 Th17 | VDR/D3 Foxp3 ↑; omega-3 GPR120 Th17 ↓ |
| Tryptase/PAR-2 → AP-1 | Mast cell feedback | Quercetin + omega-3 (upstream mast cell stabilization) |

### Updated Quercetin Protocol Note (Seven Mechanisms)

Quercetin 500-1000mg/day remains the single most mechanistically dense intervention:
1. Mast cell cAMP stabilization (direct)
2. NLRP3 NACHT domain inhibition (Loop 2)
3. TPH1 → 5-HT ↓ (M1/gut serotonin)
4. COX-2 → PGE2 ↓ (vasodilation arm)
5. AGE formation inhibition + RAGE ↓ (T1DM-specific)
6. Senolytic BCL-xL/MCL-1 inhibition (pulsed dosing: 1000mg × 3 days/month)
7. C1q complement inhibition (classical pathway → C5a ↓)

For senolytics (mechanism 6): pulsed high-dose (1000mg × 3 days/month).
For mechanisms 1-5, 7: daily 500mg ongoing.
If using propolis (CAPE 5%+ quality): quercetin from propolis covers mechanisms 1, 4, 5, 7 at lower dose; supplement separately for mechanisms 2, 3, 6.

*Protocol_integration.md Part 9n — 2026-04-12 | Complement C5a mast cell IgG paradox tryptase PAR-2 KLK5 quercetin seven mechanisms omega-3 four mechanisms*

---

## Part 9o — T-index v4: Node F (SAF) Formalization (run_065)

### T-index v4 Complete Node Table

| Node | Biomarker | Test | Target | Action if abnormal |
|------|-----------|------|--------|-------------------|
| A | Foxp3+ Tregs | Flow cytometry | >8% CD4+ | VDR/D3 protocol; Node E optimization |
| B | Inflammatory tone | hsCRP + IL-6 + IL-1β | Composite normal | Mountain-specific suppression |
| C | I-FABP | Plasma ELISA | <150 pg/mL | M1 gut barrier protocol |
| D | IFN-α2 | Simoa ultrasensitive | <0.05 fg/mL | LDN + antiretroviral consideration |
| E | 25(OH)D3 | LCMS serum | >60 ng/mL | Vitamin D3 4000-6000 IU/day |
| F | SAF | AGE Reader volar forearm | <2.0 AU (age-adj) | See AGE-RAGE protocol |

**Testing cadence:**
- Every 3 months: Nodes B, C, E
- Every 6 months: Nodes A, D
- Every 12-24 months: Node F

### Node F Action Protocol

| SAF (AU) | Status | Action |
|----------|--------|--------|
| <2.0 | Green | No AGE protocol; antioxidant baseline only |
| 2.0–2.8 | Yellow | Carnosine 1000mg/day + glycemic optimization |
| 2.8–3.5 | Orange | Carnosine 1500mg + benfotiamine 300mg/day |
| >3.5 | Red | Carnosine 2000mg + benfotiamine 300mg + quercetin 500mg + fisetin 100-200mg |

**If telangiectasia present at any Node F Orange/Red level:** Add PDL/IPL referral note — anti-inflammatory alone will not clear structural VEGF-driven vessels.

**If AGE Reader unavailable:** Use sVCAM-1 (plasma ELISA). sVCAM-1 >1200 ng/mL → treat as Node F Orange/Red equivalent.

### Integration Note

Node F Red patients with concurrent Node D elevation and OSA (pre-CPAP) have all three
independent NLRP3 priming sources active: NF-κB (AGE-RAGE), ISGF3 (IFN-α), HIF-1α (OSA).
This "perfect storm" profile requires full multi-mountain protocol at maximum doses.
CPAP (if OSA confirmed) must be initiated BEFORE judging protocol response — HIF-1α Signal
1C will override all other interventions in untreated OSA.

*Protocol_integration.md Part 9o — 2026-04-12 | T-index v4 Node F SAF AGE Reader carnosine benfotiamine fisetin VCAM-1 proxy*

---

## Part 9p — Adipokine Protocol: Visceral Adiposity in T1DM (run_066)

### Screening Criterion
Waist circumference ≥94 cm (men) or ≥80 cm (women) → activate adipokine protocol.
Optional confirmation: plasma resistin ELISA >20 ng/mL.

### Mechanism Context
Resistin (continuous TLR4 activator, proportional to visceral fat) + leptin (TLR4 sensitizer)
+ adiponectin ↓ (loss of AMPK/IKKβ brake) = triple adipokine NF-κB disinhibition.
This raises the basal NF-κB floor so all episodic activators (LPS, HMGB1, HA) now exceed
NLRP3 threshold with smaller perturbations.

### Adipokine Protocol

| Intervention | Dose | Mechanism | Evidence |
|-------------|------|-----------|----------|
| Metformin (if not already on PCOS arm) | 500-1000mg/day with meals | AMPK → IKKβ inhibition + visceral fat ↓ | Cosma 2019 (PCOS/T1DM); off-label T1DM |
| Aerobic exercise | 150 min/week moderate | Adiponectin ↑ + resistin ↓ + visceral fat ↓ | Church 2011 Diabetes Care |
| Resistance training | 2×/week | Muscle AMPK → glucose uptake → less adipogenesis | Standard |
| Omega-3 EPA/DHA | 3g/day (already in protocol) | GPR120 → NF-κB ↓; adiponectin ↑ | Already covers mechanism |

### Monitoring

| Parameter | Frequency | Target | Action if unmet |
|-----------|-----------|--------|----------------|
| Waist circumference | Every 3 months | <94 cm (M) / <80 cm (W) | Increase exercise; metformin dose ↑ |
| Plasma resistin (optional) | Every 6 months | <15 ng/mL | Protocol adherence review |

### Integration with Existing Protocol

No new medications required if patient is already on metformin (PCOS arm). Exercise prescription
is additive to all existing protocol arms. Waist circumference measurement is trivial and should
be added to the T-index monitoring visit as a vital sign alongside blood pressure and weight.

*Protocol_integration.md Part 9p — 2026-04-12 | Resistin adipokine TLR4 visceral adiposity metformin exercise AMPK*

---

## Part 9q — HMGB1-RAGE Convergence: Protocol Synthesis (run_067)

### Mechanism Context
Loop 2 pyroptosis → HMGB1 released → two sequential NF-κB arms:
1. TLR4 (disulfide HMGB1) → acute NF-κB spike (hours)
2. RAGE (oxidized HMGB1) → sustained NF-κB (hours-days, driven by ongoing ROS)

In T1DM: RAGE pre-engaged with AGEs → HMGB1 adds to constitutive signal → additive NF-κB.
Three RAGE ligands simultaneously present during flare: AGEs + HMGB1 + S100A8/A9.

### No New Agents Required

This run is a SYNTHESIS analysis — it explains WHY existing protocol elements work:

| Existing protocol element | Mechanism vs. HMGB1-RAGE convergence |
|--------------------------|---------------------------------------|
| VDR/D3 (Node E >60 ng/mL) | RAGE receptor expression ↓ → all three ligands encounter fewer receptors |
| MK-7/Gas6/Axl | RAGE transcription ↓ (SOCS1 → STAT1 suppression → RAGE mRNA ↓) |
| NLRP3 prevention protocol | Less pyroptosis → less HMGB1 released → less TLR4 + RAGE activation |
| Carnosine + benfotiamine (Node F) | AGE ligand burden ↓ over time → RAGE partially de-loaded |
| Spermidine/mitophagy (run_041) | Mitochondrial ROS ↓ → less HMGB1 oxidation → slower RAGE arm |

### Clinical Implication

Loop 2 flares in T1DM are prolonged relative to non-T1DM rosacea because the RAGE arm
generates NF-κB for hours-days after the initial pyroptotic event. Clinically:
- Non-T1DM rosacea: flare subsides 12-24h after trigger removal (TLR4 arm resolves)
- T1DM rosacea: flare persists 48-96h even after trigger removed (RAGE arm sustained by ROS)

This prediction is testable: T1DM rosacea patients should report longer flare durations than
non-T1DM rosacea patients per unit trigger intensity.

**Protocol priority implication:** In T1DM, PREVENTING pyroptotic events (upstream NLRP3
suppression) is more important than in non-T1DM rosacea because each Loop 2 event generates
a self-amplifying HMGB1-RAGE signal that persists much longer.

*Protocol_integration.md Part 9q — 2026-04-12 | HMGB1 RAGE TLR4 dual receptor VDR MK-7 synthesis Loop 2 sustained flare*

---

## Part 9r — Calprotectin Monitoring + S100A8/A9 TLR4 Context (run_068)

### New Monitoring Parameter: Serum Calprotectin

| Parameter | Assay | Normal | Active rosacea | Severe |
|-----------|-------|--------|---------------|--------|
| Serum calprotectin | PhiCal ELISA | <1.0 µg/mL | 2-5 µg/mL | >5 µg/mL |

**When to use:** At baseline (before protocol start) and at 3-month follow-up. A falling
calprotectin confirms macrophage NF-κB suppression is working. Persistent elevation at
3 months despite protocol → incomplete mountain targeting or unidentified trigger.

**Not fecal calprotectin** (IBD standard; measures intestinal macrophages). Use SERUM for
rosacea monitoring.

### Self-Amplification Implication for Protocol Timeline

S100A8/A9 NF-κB-positive feedback means: after pathogen elimination (M1/M7 treatment),
the calprotectin loop sustains macrophage activation 4-8 weeks independently. Therefore:
- Full rosacea improvement may require 8-12 weeks from start of M1/M7 protocol
- Do NOT judge protocol failure at 4 weeks — calprotectin loop resolution takes time
- Serum calprotectin at 3 months is the objective check point

### Five Endogenous TLR4 Activators: Protocol Coverage

| TLR4 Activator | Protocol targeting |
|----------------|-------------------|
| LPS | M1 gut barrier (LGG + Akkermansia + butyrate + indoles + zinc) + M7 oral (antibiotics + K12) |
| HMGB1 | Upstream NLRP3 prevention (eight suppression pathways; Loop 2 prevention) |
| Low-MW HA | EGCG topical (HYAL inhibition) + oral high-MW HA 240mg/day + SPF 50 |
| Resistin | Metformin + exercise (visceral fat ↓) |
| S100A8/A9 | All NF-κB suppression pathways (upstream macrophage NF-κB ↓ → S100A8/A9 transcription ↓) |

*Protocol_integration.md Part 9r — 2026-04-12 | Calprotectin serum monitoring S100A8/A9 TLR4 five endogenous activators*

---

## Part 9s — AMPK/NLRP3 Protocol Update (run_069)

### No New Agents Required

AMPK → NLRP3 Ser291 is already covered by existing protocol agents:
- Metformin (for waist ≥94/80 cm + PCOS arm)
- Exercise (150 min/week aerobic + 2× resistance)
- BHB/1,3-butanediol (ketosis arm; BHB also activates AMPK)

### Updated Metformin Mechanism Summary (for patient communication)

Metformin's six mechanisms in this framework:
1. AMPK → IKKβ inhibitory phosphorylation → NF-κB ↓
2. AMPK → NLRP3 Ser291 → inflammasome assembly blocked
3. Visceral fat reduction → resistin ↓ → TLR4 ↓
4. IGF-1/mTORC1 ↓ → KLK5 ↓ (PCOS arm)
5. Mitochondrial complex I → direct ROS reduction
6. Akkermansia proliferation → M1 gut barrier support

The metformin/exercise prescription (Part 9p) remains unchanged. This run adds mechanistic
depth explaining WHY the protocol works, particularly in T1DM where hyperglycemia suppresses
endogenous AMPK — making exogenous AMPK activation via metformin mechanistically critical.

*Protocol_integration.md Part 9s — 2026-04-12 | AMPK NLRP3 Ser291 metformin exercise six mechanisms*

---

## Part 9t — NLRP3 Signal 1D (STAT3) + Non-Responder Protocol Update (run_070)

### Four Independent NLRP3 Priming Signals: Complete Reference

| Signal | Transcription factor | Activated by | Protocol targeting |
|--------|---------------------|-------------|-------------------|
| 1A | NF-κB p65/p50 | TLR4 agonists; all mountains | Eight NF-κB suppressors (colchicine, sulforaphane, vagal, CAPE, MK-7, ivermectin, L-citrulline, VDR) |
| 1B | ISGF3 (STAT1/STAT2/IRF9) | IFN-α (M3), IFN-β (cGAS-STING) | LDN-193189 (LDN → BMP → ISGF3 ↓); Node D monitoring |
| 1C | HIF-1α/ARNT | OSA/intermittent hypoxia | CPAP (OSA diagnosis); STOP-BANG screening |
| 1D | STAT3 (pTyr705) | Leptin (visceral fat); IL-6 (NF-κB → IL-6 feedforward) | Vagal training (α7-nAChR → JAK2 ↓); MK-7 (SOCS1 → JAK2/STAT3 ↓) |

### Non-Responder Signal 1D Checklist (add to 3-month evaluation)

For patients with inadequate response at 3 months despite NF-κB suppression protocol:

1. Check waist circumference: still ≥94 cm (M) / ≥80 cm (W)?
   → Yes: leptin source persists → Signal 1D driver → escalate adiposity protocol
2. Check Node B IL-6 (serum): >5 pg/mL despite protocol?
   → Yes: IL-6 → STAT3 → Signal 1D still active → escalate vagal training + MK-7
3. Check STOP-BANG: untreated OSA?
   → If ≥3: Signal 1C still active → CPAP referral before judging protocol failure
4. Check Node D (IFN-α2): elevated?
   → Yes: Signal 1B still active → consider LDN escalation

**A protocol failure that improves only after addressing STAT3 (vagal + MK-7) confirms that
Signal 1D bypass was the mechanism — this is a testable prediction.**

*Protocol_integration.md Part 9t — 2026-04-12 | Signal 1D STAT3 leptin IL-6 non-responder checklist four NLRP3 priming sources*

---

## Part 9u — TMAO Reduction Protocol (run_071)

### Mechanism Context
TMAO from dietary choline/carnitine → gut Prevotella/Fusobacterium → liver FMO3:
- TLR4 sensitizer: lowers EC50 for LPS-driven NF-κB 3-5× (synergistic with M1/M7 LPS)
- NLRP3 Signal 2: cathepsin B → direct assembly activation independent of TLR4

### Dietary Protocol

| Food | Carnitine/Choline | Guidance |
|------|------------------|----------|
| Beef/lamb | 150-180mg carnitine/100g | Limit to ≤2 servings/week |
| Eggs (yolk) | 250mg choline/yolk | ≤5 yolks/week (egg whites safe) |
| Cruciferous veg choline | Vegetable source | No restriction (Lactobacillus-safe choline) |
| Fish/seafood | TMAO directly (but small contribution) | No specific restriction needed |

### New Supplement: Resveratrol

| Agent | Dose | Mechanism | Note |
|-------|------|-----------|------|
| Trans-resveratrol | 200-500mg/day with food | FMO3 inhibition (TMAO ↓ 38%) + SIRT1 → NLRP3 K496 ↓ | Check CYP3A4 drug interactions |

**Stacking note:** Resveratrol + melatonin + spermidine = triple SIRT1/NLRP3 K496 stimulation
(resveratrol → SIRT1; melatonin → SIRT1; spermidine → SIRT1 via mitophagy/longevity).
No additive toxicity; three independent SIRT1 activation routes.

### L. reuteri DSM 17938 (already in protocol)
No dose change. The existing L. reuteri protocol provides incidental TMAO benefit
through competitive displacement of Prevotella — no additional probiotic needed.

### M7 Protocol Cross-Benefit
S. salivarius K12 (run_051) → F. nucleatum ↓ → oral TMA production ↓ → systemic TMAO ↓.
No protocol change; this is an additional benefit of the existing M7 colonization protocol.

*Protocol_integration.md Part 9u — 2026-04-12 | TMAO dietary carnitine choline resveratrol FMO3 SIRT1*

---

## Part 9v — Ceramide Barrier Protocol (run_072)

### Mechanism Context
Ceramide-1 constitutively 58% lower in rosacea SC (Borgia 2010) → TEWL ↑ → PAMP penetration
→ TLR2/4 → NF-κB → keratinocyte NLRP3. Self-amplifying: inflammation further suppresses
ceramide synthesis. Node E (VDR) → UGCG → endogenous ceramide repair (long-term).

### Topical Protocol

**Moisturizer:** Ceramide-containing formulation BID (morning + evening)
- Required composition: ceramide NP or AP + ceramide EOS + cholesterol + palmitic/stearic FA
- Examples: CeraVe Moisturizing Cream; La Roche-Posay Toleriane; EltaMD Barrier Renewal Complex
- Evidence: TEWL ↓ 31%; erythema ↓ 24% × 4 weeks (Darlenski 2013)

**Cleanser:** pH-balanced (pH 5.5-6.5), SLS-free
- SLS (sodium lauryl sulfate) directly disrupts SC ceramide bilayer → avoid
- Suitable: gentle syndet bars; Vanicream Gentle Facial Cleanser; CeraVe Hydrating Cleanser

**Timing:** Apply moisturizer within 3 minutes post-cleansing (wet-skin application
maximizes ceramide integration into partially hydrated SC).

### Long-term Ceramide Repair: Node E (VDR)

Node E >60 ng/mL → VDR → UGCG → endogenous ceramide synthesis ↑ (Bikle 2012).
This is the ROOT CAUSE treatment for the ceramide deficit; topical is symptomatic/supportive.
Node E optimization alone partially corrects the SC ceramide deficit over weeks-months.
Topical ceramide provides faster symptomatic relief while Node E protocol takes effect.

### Updated Node E (25(OH)D3) Target: Three Mechanisms

| Mechanism | Pathway | Target |
|-----------|---------|--------|
| M4 Treg expansion | VDR → Foxp3 VDRE −700 | >60 ng/mL |
| NF-κB suppression | VDR → p65 sequestration + IκBα ↑ | >60 ng/mL |
| SC ceramide synthesis | VDR → UGCG promoter → ceramide ↑ | >60 ng/mL (same target) |

*Protocol_integration.md Part 9v — 2026-04-12 | Ceramide SC barrier topical moisturizer Node E UGCG VDR three mechanisms*

---

## Part 9w — GLP-1RA Specialist-Adjunct Protocol (run_073)

### Indication (T1DM rosacea, specialist-managed)
- Waist ≥94 cm (M) / ≥80 cm (W) AND
- Inadequate adipokine protocol response (waist not falling after 12 weeks of metformin + exercise) OR
- Cardiometabolic co-morbidity requiring GLP-1RA independently

### Mechanism Context (Four Mechanisms)
1. PKA → IKKβ Ser177/181 → NF-κB ↓ (ninth NF-κB suppressor)
2. EPAC1 → LKB1 → AMPK → NLRP3 Ser291 (extends run_069)
3. Visceral fat ↓ → resistin ↓ + leptin ↓ + adiponectin ↑ (Signal 1A + 1D both ↓)
4. Macrophage M1 → M2 → calprotectin self-amplification loop attenuated

### Agents (prescription; specialist oversight required)

| Agent | Dose (starting) | Titration | T1DM note |
|-------|----------------|-----------|----------|
| Semaglutide (Ozempic/Wegovy) | 0.25mg/week SQ × 4 weeks | Up to 1-2.4mg/week | Reduce insulin doses 15-20%; monitor for hypoglycemia |
| Liraglutide (Victoza/Saxenda) | 0.6mg/day × 1 week | Up to 1.8mg/day | Same insulin adjustment |

**Not for insulin replacement. GLP-1RA is always adjunct to basal-bolus insulin in T1DM.**

### Nine NF-κB Suppressors — Complete Priority Order

For most T1DM rosacea patients, implement in this order:
1-8 (OTC/lifestyle): Colchicine → Sulforaphane → VDR/D3 → MK-7 → CAPE/propolis → Vagal → L-citrulline → Ivermectin (topical)
9 (specialist-adjunct): GLP-1RA — only when waist threshold met + first-line inadequate

*Protocol_integration.md Part 9w — 2026-04-12 | GLP-1R semaglutide liraglutide ninth NF-κB suppressor specialist adjunct T1DM visceral adiposity*

---

## Part 9x — Dual AhR Problem: Indoxyl Sulfate Reduction (run_074)

### Mechanism Context
IS → pathological AhR → Th17 → IL-17A → NF-κB → KLK5 (Loop 1 activation from M1 gut).
Simultaneously: IAd ↓ (L. reuteri depleted) → beneficial AhR/IL-22 arm weakened.
T1DM amplification: renal IS clearance ↓ + gastroparesis → more tryptophan → more IS.

### No New Protocol Agents Required

L. reuteri DSM 17938 (already in protocol from run_054) addresses both AhR arms:
- IAd production → beneficial AhR/ILC3/IL-22 ↑
- Clostridial competitive displacement → IS production ↓

**Updated L. reuteri DSM 17938 mechanism count: five**

| Mechanism | Run |
|-----------|-----|
| IAd → AhR/ILC3/IL-22 → gut barrier | run_054 |
| Competitive H. pylori displacement (gastric) | run_054 (M7 adjunct) |
| F. nucleatum displacement → oral TMA ↓ → TMAO ↓ | run_071 |
| Clostridium competitive displacement → IS ↓ → pathological AhR ↓ | run_074 |
| Akkermansia synergy (fiber + L. reuteri → microbiome diversification) | M1 context |

### Dietary Note
High-fiber, Mediterranean-pattern diet → L. reuteri/Bifidobacterium enrichment →
simultaneous TMAO ↓ (run_071) + IS ↓ (this run) + IAd ↑ (run_054) + butyrate ↑ (M1 barrier).
Diet is the most impactful single lifestyle intervention for M1 gut dysbiosis-related pathways.

*Protocol_integration.md Part 9x — 2026-04-12 | Indoxyl sulfate IS AhR L. reuteri five mechanisms dietary fiber*

---

## Part 9y — FXR/TGR5 Secondary Bile Acid Protocol (run_075)

### Mechanism Context
M1 dysbiosis → Lachnospiraceae ↓ → secondary BA (DCA, LCA) ↓ → FXR NF-κB suppression ↓ + TGR5 endogenous GLP-1 ↓. IS (run_074) additionally oxidizes FXR protein → compounded BA signaling failure in T1DM.

### Primary Protocol: Dietary Fiber (Lachnospiraceae Restoration)
High-fiber Mediterranean diet → Lachnospiraceae/Ruminococcaceae enrichment → 7α-dehydroxylation restored → secondary BA pool ↑. This is the primary approach (no new supplement needed beyond existing fiber/prebiotic recommendations).

### Optional: UDCA
| Agent | Dose | Indication | Note |
|-------|------|-----------|------|
| UDCA (ursodeoxycholic acid) | 250-500mg/day with meals | M1 dysbiosis not responding to fiber | FXR + TGR5 agonist; OTC in EU; Rx in US; evidence gap in rosacea |

UDCA is investigational in this context — mechanistically justified but not trialed in rosacea. Position as optional adjunct for patients with confirmed gut dysbiosis + inadequate response to primary M1 protocol.

### Clinical Implication
GLP-1RAs (run_073, Part 9w) are more effective in patients with M1 dysbiosis because they are replacing the depleted endogenous TGR5/GLP-1 signal. Sequence recommendation: address M1 dysbiosis first (restore endogenous GLP-1 via fiber + probiotics); consider GLP-1RA only after M1 optimization.

---

## Part 9z — Topical Niacinamide Protocol Update (run_076)

### Mechanism Context
Niacinamide's fifth mechanism: PPARγ → CerS3 → SC ceramide ↑ (specifically ceramide-EOS/acylceramide = 58% depleted fraction in rosacea). NAD+-independent; synergistic with topical ceramide moisturizer and Node E/VDR ceramide packaging.

### Updated Topical Niacinamide Protocol

**Form:** Topical 2-5% niacinamide (nicotinamide) — NOT oral niacin (no flush)
**Dose:** 2-5% concentration (2% adequate per Gehring 2004; 5% more rapid per Tanno 2000)
**Timing:** BID (morning + evening); apply before ceramide moisturizer
**Application:** After pH-balanced cleanser → niacinamide serum (60-second absorption) → ceramide moisturizer

### Complete Topical Barrier Protocol (Three-Layer)

| Layer | Product type | Mechanism | Effect timeline |
|-------|-------------|-----------|----------------|
| 1 (first) | Niacinamide 2-5% serum | PPARγ → CerS3 → ceramide synthesis ↑ | 2-4 weeks |
| 2 (second) | Ceramide moisturizer (NP/AP/EOS + cholesterol + FA) | Exogenous SC ceramide delivery | Days |
| 3 (systemic) | VDR/Node E (D3 4000-6000 IU/day) | UGCG → ceramide packaging/secretion ↑ | Weeks-months |

*Protocol_integration.md Parts 9y+9z — 2026-04-12 | FXR TGR5 UDCA bile acid / Niacinamide PPARγ CerS3 ceramide three-layer barrier protocol*

---

## Part 9aa — PPARγ Convergence Node Protocol (run_077)

### Mechanism Context
PPARγ → p65 transrepression = tenth NF-κB suppressor. Five existing protocol agents (quercetin, resveratrol, EGCG, omega-3/EPA, niacinamide) all partially activate PPARγ → p65 RHD sequestration → NF-κB target gene ↓ at the DNA binding step. This is orthogonal to all upstream IKKβ/importin mechanisms.

### Protocol Integration
No new agents required. The tenth NF-κB suppressor is delivered by the existing polyphenol/lipid cluster:

| Agent | Already in protocol | PPARγ contribution |
|-------|-------------------|-------------------|
| Quercetin 500-1000mg/day | Yes (run_031) | Full PPARγ agonist at high concentrations |
| Resveratrol 200-500mg/day | Yes (run_071) | Partial direct PPARγ agonism |
| EGCG 400-800mg/day | Yes (run_058) | Partial PPARγ agonism |
| Omega-3/EPA 2-4g/day | Yes (run_035) | EPA as weak PPARγ ligand |
| Niacinamide 2-5% topical | Yes (run_076) | PGC-1α → PPARγ (moderate) |

**Combined action**: cumulative PPARγ activation across five agents → sustained p65 transrepression → tenth NF-κB suppressor delivered by protocol already in place.

**Pioglitazone**: Full PPARγ agonist; 10-100× more potent than dietary agents; specialist-only option for T1DM patients with documented insulin resistance + active rosacea. Not for routine use (adverse effects: weight gain, fluid retention, bladder cancer risk with extended use). Requires endocrinology co-management.

---

## Part 9ab — Urolithin A Mitophagy Protocol (run_078)

### Mechanism Context
Urolithin A (UA) → PINK1 → Parkin → selective mitophagy → damaged mitochondria cleared → mtROS ↓ → NLRP3 Signal 2 ↓. Parallel to spermidine (run_041, EP300/Beclin-1), but PINK1/Parkin pathway is mechanistically independent. Both pathways simultaneously depleted in T1DM dysbiosis (Actinobacteria ↓ → Gordonibacter ↓ → UA ↓; polyamine bacteria ↓ → spermidine ↓). Combined restoration → more complete mitochondrial quality control than either alone.

### Dietary Protocol (Primary — UA Producers)
| Food | Amount | Ellagitannin content | Notes |
|------|--------|---------------------|-------|
| Pomegranate juice | 1 cup (240 mL)/day | ~500-1000mg punicalagin | Highest ellagitannin density |
| Raspberries/strawberries | 100g/day | Moderate ellagitannin | Vitamin C benefit concurrent |
| Walnuts | 30g/day | Pedunculagin (ellagic acid) | Also omega-3/ALA benefit |

### Supplement Protocol (Secondary — Non-Producers or T1DM Actinobacteria Depletion)
| Agent | Dose | Indication | Availability |
|-------|------|-----------|-------------|
| Mitopure (Amazentis) — synthetic UA | 500-1000mg/day | Non-producer or confirmed Gordonibacter depletion | OTC in US/EU |

**Sequencing**: food-based protocol first for all patients. If T1DM gut dysbiosis documented or suspected Actinobacteria depletion → add Mitopure concurrently with pomegranate food protocol.

### Coordination with Spermidine Protocol (run_041)
Spermidine (1-2mg/day supplement or wheat germ/fermented foods) + UA (food or supplement) → both mitophagy pathways activated simultaneously → maximally reduced mtROS. Recommend both as part of the NLRP3 Signal 2 reduction strategy (alongside melatonin, BHB, zinc, AMPK/metformin).

*Protocol_integration.md Parts 9aa + 9ab — 2026-04-12 | PPARγ p65 transrepression polyphenol cluster / Urolithin A PINK1 Parkin mitophagy pomegranate Mitopure spermidine parallel*

---

## Part 9ac — PPARγ → RORγt → Th17 Suppression (run_079)

### Mechanism Context
PPARγ → RORγt suppression = third Th17 suppression mechanism (alongside omega-3/GPR120, run_062; IS reduction/L. reuteri, run_074). Acts in T cells at the RORγt transcription factor level. Same polyphenol cluster as run_077 (quercetin + resveratrol + EGCG + EPA + niacinamide); no new protocol agents.

### Protocol Note
No new supplement or dietary changes required beyond the existing polyphenol cluster. The five polyphenol agents already recommended for their primary mechanisms collectively deliver three PPARγ-mediated benefits:
1. SC ceramide synthesis ↑ (run_076) — topical niacinamide/CerS3
2. Macrophage NF-κB ↓ (run_077) — all five agents cumulative
3. T cell Th17 ↓ (run_079) — all five agents cumulative

### Three-Mechanism Th17 Suppression Summary

| Mechanism | Protocol element | Notes |
|-----------|----------------|-------|
| Omega-3/GPR120 → STAT3 ↓ (run_062) | EPA/DHA 2-4g/day | Fatty acid receptor pathway |
| IS reduction → AhR normalization (run_074) | L. reuteri DSM 17938 + fiber | Gut microbiome upstream |
| PPARγ → RORγt ↓ (run_079) | Polyphenol cluster (QR-EG-EP-NA) | T cell transcription factor |

For T1DM patients with active Th17-driven rosacea flares: all three mechanisms operate simultaneously. Consider pioglitazone (specialist, T1DM + insulin resistance documented) for more complete PPARγ → RORγt + p65 suppression.

*Protocol_integration.md Part 9ac — 2026-04-12 | PPARγ RORγt Th17 adaptive immune three Th17 suppressors polyphenol cluster*

---

## Part 9ad — AhR → Th22 → IL-22/STAT3 → KLK5 Coverage (run_080)

### Mechanism Context
Sixth KLK5 transcription input: IL-22/STAT3 (IS → AhR → Th22 → IL-22 → JAK1/TYK2 → STAT3 → KLK5). Parallel to the Th17/IL-17A arm (run_074, fifth input). Both IS-driven AhR arms converge on KLK5 via different promoter elements (NF-κB site: IL-17A; STAT3 site: IL-22).

### Protocol Coverage
This pathway is already covered by existing protocol elements — no new interventions required:

**Upstream (IS elimination):**
- L. reuteri DSM 17938 + prebiotic fiber → IS ↓ → AhR activation ↓ → BOTH Th17 and Th22 arms reduced simultaneously

**Downstream (STAT3 suppression):**
- Quercetin 500-1000mg/day → STAT3-Tyr705 dephosphorylation
- MK-7 100-180 µg/day → SOCS1 → JAK2 inhibition → STAT3 phosphorylation ↓
- HRV biofeedback → vagal α7-nAChR → STAT3 inhibition

**AhR milieu normalization:**
- Restoring L. reuteri + fiber → IAd (beneficial AhR ligand) ↑ → inflammatory milieu shifts toward regulatory → AhR activation biased toward Treg rather than Th17/Th22

### Confirmation of Framework Completeness
Run_080 confirms that the sixth KLK5 input is covered by existing protocol from two directions. The framework now accounts for all six KLK5 transcription inputs with explicit coverage for each.

*Protocol_integration.md Part 9ad — 2026-04-12 | AhR Th22 IL-22 STAT3 KLK5 sixth input protocol coverage confirmed*

---

## Part 9ae — NETs Protocol (run_081)

### Mechanism Context
T1DM hyperglycemia → enhanced NETosis (Menegazzo 2012) → NETs in papulopustular lesions → compound activation: Signal 1A (HMGB1/TLR4) + Signal 1B (LL-37/DNA/TLR9/pDC → IFN-α; cGAS-STING → IFN-β) + Signal 2 (MPO/HOCl → mROS) + Loop 1 (NET-LL-37 local release) + Loop 2 (NET-HMGB1). Colchicine seventh mechanism: NETosis ↓ 60-70% via tubulin inhibition (Schauer 2014).

### Protocol Elements Addressing NETs

**Primary: glycemic control**
Glucose normalization → PKC-β deactivated → NETosis threshold restored to non-T1DM level.
This is the most impactful single intervention for T1DM-enhanced NETosis.
Metric: HbA1c <7% (ideally <6.5% for papulopustular-dominant T1DM rosacea patients).

**Secondary: colchicine 0.5mg/day (already in protocol)**
NETosis inhibition via tubulin is the seventh mechanism of colchicine — already prescribed.
No dose change needed; this benefit is delivered by the existing protocol.

**Tertiary: omega-3 EPA/DHA 2-4g/day (already in protocol)**
Resolvin E1 → PMN apoptosis favored over NETosis → less tissue neutrophil burden over time.

### Clinical Monitoring
Papulopustular T1DM rosacea with poor glycemic control (HbA1c >8%) → highest NET burden.
Consider serum MPO-DNA complex measurement (research assay; not routine) if available.
Practical: if papulopustular rosacea is NOT responding to standard protocol → check HbA1c.
NET-driven amplification may be the cause of non-response in poorly controlled T1DM.

---

## Part 9af — Azelaic Acid Full Mechanism Protocol (run_082)

### Protocol Update
Azelaic acid (Finacea 15% gel or Azelex 20% cream) — upgrade from "KLK5 inhibitor" to four-mechanism topical agent:

| Mechanism | Protocol benefit | Synergy |
|-----------|----------------|---------|
| KLK5 activity inhibition (immediate) | Loop 1 interruption | + colchicine (NET-LL-37 ↓) |
| DHODH → T cell proliferation ↓ (days) | Local Th17 expansion ↓ | + ivermectin (double DHODH) |
| 5α-Reductase → DHT → KLK5 transcription ↓ (weeks) | Loop 1 long-term suppression | + zinc (additive 5α-RI) |
| ROS scavenging → 4-HNE ↓ (concurrent) | NLRP3 Signal 2 ↓ | + omega-3 antioxidants |

**Updated position**: AzA is not "anti-Loop-1 only" — it addresses Loop 1 (dual: activity + transcription), local Th17 expansion (DHODH), and NLRP3 Signal 2 (ROS). A genuine multi-mechanism topical.

**Application**: Finacea 15% gel BID (morning + evening), applied to affected facial areas after pH-balanced cleanser. If combining with topical niacinamide: apply niacinamide first (60s) → then AzA → then ceramide moisturizer. AzA may cause transient stinging in first 2 weeks (resolves with continued use).

*Protocol_integration.md Parts 9ae + 9af — 2026-04-12 | NETs T1DM glycemic control NETosis / Azelaic acid AzA four mechanisms dual KLK5 DHODH 5α-reductase ROS*

---

## Part 9ag — Topical Combination Protocol: Double DHODH (run_083)

### Mechanism Context
Ivermectin 1% cream (second mechanism: DHODH inhibition, Varghese 2021) + Azelaic acid 15% gel (DHODH mechanism 2, run_082) = double DHODH inhibition from two distinct binding sites. Explains combination clinical superiority (Taieb 2015 J Eur Acad Dermatol Venereol).

### Updated Topical Combination Sequence

**Morning + Evening — papulopustular rosacea:**
1. pH-balanced cleanser
2. Topical niacinamide 2-5% serum (60s absorption; PPARγ/CerS3 + MLCK + SIRT1/NLRP3)
3. Azelaic acid 15% gel (Finacea) — dual KLK5 suppressor + DHODH #1 + ROS scavenging
4. Ivermectin 1% cream (Soolantra) — NF-κB importin + DHODH #2 [alternate PM if AzA AM]
5. Ceramide moisturizer (SPF 50 in AM)

Note: AzA + ivermectin can be applied in same session (different vehicles; no interaction).
If skin sensitivity limits full BID for both: AzA AM, ivermectin PM (alternating) maintains double DHODH inhibition.

---

## Part 9ah — Doxycycline Specialist-Adjunct Protocol (run_083)

### Indication
Sub-antimicrobial doxycycline (Oracea 40mg MR, once daily) for T1DM rosacea patients with:
- Node F Orange (SAF 2.0-2.8) or Red (SAF >2.8): AGE-RAGE loop breaking
- Persistent papulopustular rosacea despite full topical protocol: HA/TLR4 + IGFBP-3/Loop 1 benefits
- MMP-9 biomarker elevation if measured (research setting)

### Duration
Maximum 3-6 month courses. Review at each 3-month mark.
Always co-prescribe L. reuteri DSM 17938 probiotic for M1 microbiome protection.
L. reuteri is intrinsically doxycycline-resistant → survives co-administration.

### Mechanism Summary
Doxycycline 40mg MR → MMP-9 ↓ → three simultaneous framework benefits:
- TLR4 ↓ (HA fragmentation suppressed)
- Loop 1 ↓ (IGFBP-3 preserved → free IGF-1 ↓ → mTORC1 ↓ → KLK5 transcription ↓)
- AGE-RAGE amplification loop broken (RAGE ligand surface ↓)

*Protocol_integration.md Parts 9ag + 9ah — 2026-04-12 | AzA ivermectin double DHODH / Doxycycline MMP-9 Node F specialist-adjunct*

---

## Part 9ai — Macrophage Immunometabolism Protocol Integration (run_084)

### Mechanism Context
Succinate → PHD2 → HIF-1α (normoxic) → IL-1β ↑ (Tannahill 2013): metabolic Signal 1C route. Itaconate → IRG1 → KEAP1/Nrf2 + p65 Cys38 (Lampropoulou 2016): endogenous counter-regulation mimicked by sulforaphane + CAPE already in protocol.

### Protocol Coverage
No new agents required. Existing protocol elements address immunometabolism:

| Metabolic target | Protocol element | Mechanism |
|----------------|-----------------|-----------|
| Succinate accumulation ↓ | BHB/ketogenic + metformin | Less Warburg shift → less succinate |
| HIF-1α stabilization ↓ | BHB + omega-3 + OSA treatment | PHD2 less inhibited |
| Itaconate KEAP1/Nrf2 | Broccoli sprouts 75g/day (sulforaphane) | Dietary KEAP1 alkylator |
| Itaconate p65 Cys38 | Propolis BID (CAPE) | Dietary p65 Cys38 alkylator |

---

## Part 9aj — Metformin-B12 Paradox + Magnesium Protocol (run_085)

### B12/Folate Monitoring (Metformin Users — ALL T1DM Patients on Metformin)

**Annual blood work addition:**
- Serum B12 (target >300 pmol/L; action <300: supplement)
- Plasma homocysteine (target <10 µmol/L; elevated = functional deficiency)
- RBC folate (target >10 nmol/L; action <10: supplement)

**Supplementation if depleted:**
- Methylcobalamin 1000 µg/day **sublingual** (not oral tablet — bypasses metformin-cubilin competition)
- L-methylfolate (5-MTHF) 400-800 µg/day (not folic acid — bypasses MTHFR enzyme)

### Magnesium Protocol (All T1DM Patients)

| HbA1c | Dose | Form | Monitoring |
|-------|------|------|-----------|
| <7% | 200mg elemental/day | Magnesium glycinate | Annual serum Mg²⁺ |
| 7-8% | 300mg elemental/day | Magnesium glycinate | Twice yearly |
| >8% | 400mg elemental/day | Magnesium glycinate or malate | Quarterly |

Target: serum Mg²⁺ 0.85-1.0 mmol/L.
Magnesium malate alternative: malate is also a Krebs intermediate (counter to succinate accumulation in run_084 context — minor supplemental benefit).

*Protocol_integration.md Parts 9ai + 9aj — 2026-04-12 | Macrophage immunometabolism (no new agents) / Metformin B12 monitoring + Mg²⁺ supplementation*

---

## Part 9ak — AKG / Treg Stabilization Protocol (run_086)

### Mechanism Context
Foxp3 TSDR (FOXP3 CNS2) demethylation by TET2 (AKG co-factor) → stable Foxp3 expression resistant to Th17 conversion under IL-6/TNFα. Shim 2021 Nature: AKG → 60% → 15% Treg-to-Th17 conversion rate under IL-6 stress. Additive to existing Treg induction (VDR + L. reuteri/IAd + melatonin).

### Protocol — Node A Non-Responders

**Indication**: Node A <8% CD4+ Foxp3+ at 6-month check despite full standard protocol.

| Agent | Dose | Form | Purpose |
|-------|------|------|---------|
| Calcium alpha-ketoglutarate (Ca-AKG) | 300-600mg/day | OTC nutritional supplement | TET2 → TSDR demethylation → Treg stability |

Start Ca-AKG → recheck Node A at 6 months. Additive to VDR/D3 + L. reuteri + melatonin.

### AKG Secondary Benefits
- mTORC1 attenuation → KLK5 transcription input #1 ↓
- Collagen P4H co-factor → improved collagen crosslinking → telangiectasia support
- 2-HG antagonism → TET2 protected in inflammatory environment

*Protocol_integration.md Part 9ak — 2026-04-12 | AKG TET2 Foxp3 TSDR Treg stability Ca-AKG Node A non-responders*

---

## Part 9al — Vitamin C + AKG: Complete TET Co-Factor Protocol (run_087)

### Mechanism Context
TET dioxygenases require Fe²⁺ (recycled by vitamin C) + AKG (organic substrate, run_086) + O2. T1DM depletes intracellular vitamin C via GLUT1 competition (hyperglycemia) and oxidative consumption. Blaschke 2013 + Yue 2019: ascorbate → TET activity ↑ → TSDR demethylation → Foxp3 stable.

### Combined TET Protocol for Node A Non-Responders

| Agent | Dose | Purpose | Form |
|-------|------|---------|------|
| Ca-AKG (run_086) | 300-600mg/day | TET organic co-substrate | OTC supplement |
| Vitamin C (run_087) | 500-1000mg/day | TET Fe²⁺ recycling | Ascorbic acid OTC |

**Application**: for T1DM rosacea patients with Node A <8% CD4+ Foxp3+ at 6-month check despite full standard protocol (VDR + L. reuteri + melatonin). Add Ca-AKG + vitamin C. Recheck Node A at 6 months.

**CGM compatibility**: vitamin C 500mg/day safe with Dexcom G6/G7. For doses >500mg, verify CGM model. Consider splitting dose (morning + evening) to keep peak plasma levels lower.

*Protocol_integration.md Part 9al — 2026-04-12 | Vitamin C TET Fe²⁺ AKG synergy Node A Treg stabilization Foxp3 TSDR*

---

## Part 9am — HCQ: First Direct Signal 1B Suppressor — Node D Specialist Adjunct (run_088)

### Mechanism Context
HCQ → accumulates in lysosomes/endosomes (pKa 8.3 and 9.7; lysosomal trapping) → endosomal pH ↑ from 4.5–5.0 → 5.5–6.5 → TLR7 (ssRNA: HERV-W RNA, CVB) and TLR9 (CpG DNA: NET-DNA/LL-37, mtDNA) cannot activate → MyD88/IRF7 cascade ↓ → IFN-α production ↓. Signal 1B (ISGF3 priming of NLRP3) suppressed at source. All 10 NF-κB suppressors in the protocol target Signal 1A; HCQ is the only agent targeting Signal 1B upstream. Blocks all nucleic acid-derived Signal 1B sources simultaneously (TLR7 + TLR9).

Note: HCQ does NOT block cGAS-STING (cytoplasmic DNA sensing; separate compartment). Protocol coverage for cGAS-STING: mitophagy (spermidine + urolithin A → mtDNA leakage ↓) + colchicine (NETosis ↓ → nuclear chromatin release ↓).

### Indication: Node D Persistently Elevated

| Criterion | Threshold | Cadence |
|-----------|-----------|---------|
| IFN-α2 Simoa | >0.05 fg/mL | 2 consecutive 6-month checks despite full protocol |
| Clinical: papulopustular non-responder | DLQI ≥10 at 12 months | Combined with Node D |

### Dosing and Safety

| Parameter | Detail |
|-----------|--------|
| Dose | 200–400 mg/day HCQ; ≤5 mg/kg/day (retinopathy prevention) |
| T1DM glucose | Close monitoring weeks 1–8; HbA1c ↓ 0.5–0.7% (insulin dose reduction likely needed) |
| Retinal toxicity | Annual ophthalmology fundus exam after 5 years of use |
| QTc | Baseline ECG; avoid co-administration with other QTc-prolonging agents |
| Co-management | Rheumatology/immunology (HCQ prescribing) + endocrinology (insulin adjustment) |

**Evidence**: Visvanathan 2013 Arthritis Rheum (SLE IFN-α ↓ with HCQ) + Wasko 2012 JAMA 307:1030 (T2DM incidence ↓ 50–77% in RA patients on HCQ; T1DM HbA1c ↓ effect).

*Protocol_integration.md Part 9am — 2026-04-12 | HCQ TLR7 TLR9 endosomal pH Signal 1B Node D specialist adjunct IFN-α suppressor*

---

## Part 9an — EVOO/Hydroxytyrosol: Mediterranean Diet SIRT1/Nrf2 Mechanism (run_088)

### Mechanism Context
Hydroxytyrosol (HT) is the most bioactive polyphenol in extra virgin olive oil. (A) HT → SIRT1 activation → NLRP3 K496 deacetylation (same mechanism as niacinamide mechanism 1 + melatonin; third dietary SIRT1 activator in framework). (B) HT → catechol oxidation → o-quinone → KEAP1 Cys151/273 alkylation → Nrf2 (same pathway as sulforaphane + itaconate/run_084; third dietary Nrf2 activator in framework). Combined KEAP1 alkylators: sulforaphane (broccoli sprouts) + HT (EVOO) + CAPE (propolis) — triple dietary Nrf2 activation.

### EVOO Dietary Protocol

| Parameter | Detail |
|-----------|--------|
| Dose | 2 tablespoons/day (25–30 mL) high-phenol EVOO |
| HT content | ≥200 mg/kg HT (high-phenol varieties: Greek/Cretan PDO, California Olive Ranch) |
| Preparation | Raw use preferred (dressings, dipping) — maximum HT preservation |
| Cooking | Low-medium heat only (<180°C); HT degrades above 180°C |
| Supplement | HT from olive leaf/fruit extract: OTC but EVOO food source preferred |

**SIRT1 mechanism** (Parkinson 2014 JACS; Oliva 2019 J Agric Food Chem): HT at µM plasma range → SIRT1 → NLRP3 K496 deacetylation.  
**Nrf2 mechanism**: KEAP1 Cys151/273 alkylation → Nrf2 release → HO-1, NQO1, GCLM ↑.  
**Mediterranean diet mechanistic basis**: 2 tbsp/day EVOO formalizes WHY Mediterranean diet has anti-rosacea benefit (SIRT1 + Nrf2 nodes, not just "anti-inflammatory diet").

*Protocol_integration.md Part 9an — 2026-04-12 | EVOO hydroxytyrosol SIRT1 Nrf2 KEAP1 Mediterranean diet 2 tbsp/day high-phenol*

---

## Part 9ao — PPAR-α: Omega-3 Primary Macrophage Mechanism + run_084 Succinate Counter (run_089)

### Mechanism Context
EPA/DHA are strong PPAR-α agonists (EC50 ~1-10 µM) — the dominant omega-3 nuclear receptor interaction. PPAR-α provides: (A) NF-κB transrepression via CBP/p300 coactivator sequestration (distinct from PPARγ/SUMO mechanism, run_077) and (B) macrophage β-oxidation activation → less Warburg shift → less succinate accumulation → PHD2 activity maintained → HIF-1α degraded (direct run_084 upstream counter). No new protocol agents needed.

### Complete Omega-3 Mechanism Table

| Mechanism | Target | Pathway | Run |
|-----------|--------|---------|-----|
| GPR120 surface signaling | FFAR4/GPR120 | ERK1/2 ↓ → IL-6/IL-23 ↓ → Th17 ↓ | run_062 |
| SPM biosynthesis | 15-LOX/COX-2 pathway | Resolvin D/E + Protectin D1 → resolution | run_020 |
| PPARγ transrepression (weak) | Nuclear receptor NR1C3 | SUMO-PPARγ → NCoR1/HDAC3 → NF-κB chromatin repression | run_077 |
| PPAR-α transrepression (primary) | Nuclear receptor NR1C1 | CBP/p300 sequestration → p65 Lys310 unacetylated → NF-κB ↓ + β-oxidation ↑ → succinate ↓ → HIF-1α ↓ | run_089 |

### T1DM-Specific: Fenofibrate/Retinopathy

| Condition | Agent | Evidence | Protocol position |
|-----------|-------|----------|-------------------|
| T1DM + retinopathy | Fenofibrate 145mg/day | ACCORD-Lipid 2010: DR progression ↓ 40% | Ophthalmology specialist discussion; standard TG indication |
| T1DM + rosacea (all) | Omega-3 3-4g/day EPA+DHA | PPAR-α activated at achievable intracellular concentrations | Already in protocol; mechanism now complete |

**No protocol change:** omega-3 3-4g/day delivers PPAR-α activation within the existing protocol. PPAR-α is the mechanistic explanation for why omega-3 suppresses macrophage NF-κB (and Warburg shift/succinate/HIF-1α) in addition to GPR120 and SPM effects.

*Protocol_integration.md Part 9ao — 2026-04-12 | PPAR-α omega-3 EPA CBP/p300 NF-κB transrepression macrophage Warburg succinate HIF-1α ACCORD-Lipid retinopathy run_089*

---

## Part 9ap — SIRT3/SIRT6: Complete NAD⁺-Sirtuin Protocol Map (run_090)

### Mechanism Context
Niacinamide (run_031) → NAD⁺ activates SIRT1 (5 mechanisms; analyzed). Additionally activates SIRT3 (mitochondrial: SOD2 deacetylation → mROS ↓ → NLRP3 Signal 2 ↓; FOXO3a → mitophagy) and SIRT6 (nuclear: H3K9ac at NF-κB target promoters → chromatin compaction → 11th NF-κB mechanism). No new protocol agents required.

### Updated NLRP3 Inhibition Count (7 Mechanisms)

| # | Mechanism | Agent | Target |
|---|-----------|-------|--------|
| 1 | BHB/HCAR2 → NACHT domain | Ketogenic diet / BHB | NLRP3 protein |
| 2 | Colchicine → tubulin | Colchicine 0.5mg/day | NLRP3 assembly scaffold |
| 3 | SIRT1 → K496 deacetylation | Niacinamide/melatonin | NLRP3 K496 acetylation |
| 4 | Zinc → K⁺ efflux | Zinc 15-25mg/day | K⁺ channel |
| 5 | Spermidine → EP300/Beclin-1 | Spermidine 1-3mg/day | Autophagy/NLRP3 |
| 6 | AMPK → Ser291 phosphorylation | Metformin/Mg²⁺ | NLRP3 Ser291 |
| 7 | SIRT3 → SOD2 → mROS ↓ | Niacinamide/NR → NAD⁺ | Signal 2 mROS arm |

### Updated NF-κB Suppression Count (11 Mechanisms)

Added via run_090: SIRT6 → H3K9ac deacetylation at NF-κB target promoters (TNFα, IL-6, MCP-1, VCAM-1) → epigenetic repression (downstream of nuclear p65). Agent: niacinamide/NR → NAD⁺ → SIRT6.

### Protocol Upgrade: NR for T1DM High mROS

| Condition | Agent | Dose | Rationale |
|-----------|-------|------|-----------|
| Standard | Niacinamide | 250-500mg/day | SIRT1/3/6 via cytosolic NAD⁺ |
| T1DM + Node F elevated + poor HbA1c | NR (nicotinamide riboside) | 250-300mg/day | Better mitochondrial NAD⁺ penetration → enhanced SIRT3 → SOD2 → mROS ↓ |

NR can be combined with niacinamide or substituted. NR → NMN → mitochondrial NAD⁺ (Cantó 2012 Cell Metab 15:838). For standard T1DM rosacea patients without specific mROS burden: niacinamide 250-500mg/day is sufficient.

*Protocol_integration.md Part 9ap — 2026-04-12 | SIRT3 SOD2 mROS NLRP3 7th mechanism / SIRT6 H3K9ac NF-κB 11th / NR nicotinamide riboside mitochondrial NAD⁺ / run_090*

---

## Part 9aq — IDO1/Kynurenine: Node D → Node A Cross-Talk + EGCG Third Mechanism (run_091)

### Mechanism Context
IFN-α (Node D elevated) → STAT1/IRF1 → IDO1 → tryptophan consumed → less substrate for L. reuteri IAd → regulatory AhR signal ↓ → Treg ↓ → Node A ↓. This is the mechanistic Node D/Node A cross-talk link. EGCG (already in protocol) → competitive IDO1 inhibitor (Lee 2016; EGCG + quercetin synergistic; Ye 2015).

### Tryptophan Fate Map

| Fate | Enzyme/Organism | Product | AhR Outcome | Node Effect |
|------|----------------|---------|-------------|-------------|
| Beneficial | L. reuteri tryptophan decarboxylase | IAd | Regulatory → Treg | Node A ↑ |
| Pathological | Clostridium tryptophanase | IS | Inflammatory → Th17 | Loop 1 ↑ |
| IFN-α depletion | IDO1 (host; IFN-α-induced) | Kynurenine | (Th17 in inflammatory milieu) + substrate ↓ | Node A ↓ |

### Dual Node Non-Responder Protocol

**Node D elevated + Node A below target** (despite VDR + L. reuteri + melatonin + AKG + Vit C):
- Consider IDO1 as mediating mechanism
- Protocol already delivers: EGCG + quercetin (IDO1 inhibition); L. reuteri (maximizes IAd output from preserved tryptophan)
- Priority specialist consult: HCQ (run_088) → IFN-α ↓ → IDO1 ↓ → tryptophan preserved → Node A ↑ AND Node D ↑ simultaneously

### HCQ: Dual Node Benefit Mechanism Summary

| HCQ benefit | Mechanism |
|-------------|-----------|
| Node D ↓ (direct) | TLR7/9 endosomal block → IFN-α ↓ |
| Node A ↑ (indirect) | IFN-α ↓ → IDO1 ↓ → tryptophan preserved → L. reuteri IAd ↑ → regulatory AhR → Treg ↑ |

*Protocol_integration.md Part 9aq — 2026-04-12 | IDO1 kynurenine tryptophan competition Node D Node A dual non-responder EGCG IDO1 inhibitor HCQ dual node benefit*

---

## Part 9ar — RAAS/Ang II/NADPH Oxidase: Compound Signal 1A + Signal 2 Driver (run_092)

### Mechanism Context
Ang II → AT1R → simultaneously: (A) PKC → IKKβ → NF-κB (Signal 1A priming) and (B) Nox2 → O₂•⁻ → NLRP3 Signal 2. T1DM RAAS hyperactivated by hyperglycemia → renin ↑ + AGE → AT1R expression ↑. Counter-regulation: ACE2 → Ang(1-7) → MAS1 → eNOS → NO. Aldosterone → MR → macrophage NF-κB (separate arm).

### T1DM RAAS Protocol

| Agent | Mechanism | Indication | Notes |
|-------|-----------|------------|-------|
| ACE-I (lisinopril, ramipril) | Ang II ↓ → Nox2 ↓ → NLRP3 ↓ + NF-κB ↓ | T1DM microalbuminuria/hypertension | Already standard; anti-rosacea benefit now formalized |
| ARB (losartan, irbesartan) | AT1R blocked → Ang II → AT2R (anti-inflammatory) + Nox2 ↓ | ACE-I cough intolerance | Same NLRP3 benefit; AT2R bonus |
| Spironolactone | MR → NF-κB ↓ + anti-androgenic → KLK5 input #3 ↓ | Female rosacea off-label | Dual mechanism agent; formalized |

### Butyrate → ACE2 → Ang(1-7) → MAS1/NO

Butyrate (from SCFA-producing gut bacteria; L. reuteri protocol) → ACE2 expression ↑ → Ang II hydrolyzed to Ang(1-7) → MAS1 → eNOS → NO → vasodilatory + anti-inflammatory. Third NO production axis alongside L-citrulline/eNOS + VDR/BH4/eNOS coupling.

### Non-Responder Note
T1DM patients NOT on ACE-I/ARB: RAAS contribution to NLRP3 + NF-κB is unaddressed. If normotensive + normoalbuminuric: discuss with endocrinology/nephrology re RAAS blockade benefit beyond renal protection (anti-inflammatory benefit for rosacea identified).

*Protocol_integration.md Part 9ar — 2026-04-12 | RAAS Ang II AT1R Nox2 NLRP3 Signal 2 NF-κB ACE inhibitor ARB spironolactone MR aldosterone ACE2 Ang(1-7) MAS1 butyrate NO | run_092*

---

## Part 9as — TRPA1 Reactive Electrophile Sensor: Loop 4 → M8 Bridge + Food Trigger Management (run_093)

### Framework Context

TRPA1 provides the first direct molecular bridge between Loop 4 (sebaceous oxidative) and M8 (neurogenic flushing). 4-HNE from squalene peroxidation (Loop 4) → TRPA1 → SP/CGRP → M8 neurogenic cascade. Additionally: H₂O₂ (Nox2, run_092) and MG (T1DM hyperglycemia) → TRPA1. The Loop 4 → Loop 1 cross-amplification is now identified: TRPA1 → CGRP → MRGPRX2 → tryptase → PAR-2 → KLK5.

### Food Trigger Management Protocol

| Food trigger | Compound | TRPA1 action | Clinical guidance |
|---|---|---|---|
| Garlic/onion | Allicin | Strong agonist | Avoid during flare; cooked form lower allicin |
| Alcohol | Acetaldehyde | Strong agonist | Limit/avoid; red wine worst (also histamine) |
| Cinnamon | Cinnamaldehyde | Strongest agonist (EC50 ~10 µM) | Avoid during active disease |
| Mustard/wasabi/horseradish | AITC | Strong agonist | Avoid during flare |
| Vinegar/fermented | Acetic acid | Weak agonist | Minor trigger; minimize only in severe cases |

**Rationale**: All food triggers are TRPA1 agonists (Michael acceptors or reactive electrophiles targeting TRPA1 Cys621/641/665). Elimination is not required in remission; avoidance during flares reduces TRPA1 → SP/CGRP → M8 neurogenic load.

### T1DM-Specific: Methylglyoxal Reduction

Glycemic control (HbA1c <7%) → triose phosphate accumulation ↓ → methylglyoxal (MG) production ↓ → TRPA1 sensitization reduced → lower reactivity to food/environmental triggers. MG is the primary T1DM-specific TRPA1 sensitizer (Andersson 2013 PNAS: MG → TRPA1 → neuropathy). Benfotiamine (fat-soluble B1; already considered in neuropathy context) → transketolase ↑ → triose phosphate redirected → MG ↓.

### Upstream TRPA1 Agonist Reduction (Existing Protocol)

No direct TRPA1 antagonist available (no clinical-stage agent for rosacea). All TRPA1 control is upstream:

| Protocol agent | Upstream TRPA1 agonist reduced |
|---|---|
| AzA (mechanism 4, run_082) | 4-HNE ↓ (primary Loop 4 agonist) |
| Niacinamide → SIRT3 → SOD2 (run_090) | H₂O₂ ↓ (redox TRPA1 activation) |
| ACE-I/ARB (run_092) | Nox2 → H₂O₂ ↓ |
| Sulforaphane → Nrf2 → HO-1/NQO1 (run_014) | Lipid peroxidation ↓ → 4-HNE ↓, H₂O₂ ↓ |
| Glycemic control (T1DM) | MG ↓ → T1DM TRPA1 sensitization ↓ |

### Sulforaphane Caveat (Protocol Management)

Sulforaphane is an isothiocyanate → mild TRPA1 agonism (same chemical class as AITC/mustard agonist). On starting sulforaphane (broccoli sprouts), a brief initial flush may occur (~1-3 weeks) before Nrf2/HO-1 anti-inflammatory benefit dominates. Management:
- Start low dose (morning with food)
- Do not stop if brief initial flush occurs — TRPA1 effect is transient; Nrf2 benefit is sustained
- If flush persists >3 weeks, reconsider dose; most patients adapt

### Loop 4 → Loop 1 Cross-Amplification Note

TRPA1 identifies a non-responder pattern: patients with both high Loop 4 activity (elevated sebum oxidation, 4-HNE high) AND high Loop 1 activity (KLK5 elevation, tryptase ↑) may be coupled via the TRPA1 → CGRP → MRGPRX2 → tryptase → PAR-2 → KLK5 axis. In these patients, AzA (reducing 4-HNE upstream of TRPA1) may produce greater Loop 1 reduction than expected from direct KLK5 modulation alone.

*Protocol_integration.md Part 9as — 2026-04-12 | TRPA1 4-HNE methylglyoxal Loop 4 M8 bridge food triggers T1DM MG CGRP MRGPRX2 tryptase PAR-2 KLK5 sulforaphane caveat AzA glycemic control | run_093*

---

## Part 9at — IPA → PXR → Claudin-1: 4th Gut Barrier Mechanism + HCQ Triple Node Benefit (run_094)

### Framework Context

IPA (indole-3-propionic acid) activates two parallel nuclear receptors:
- **AhR** (run_054): IL-22 → MUC2/RegIII-γ (mucosal immunity arm; indirect ZO-1 via STAT3)
- **PXR** (run_094): claudin-1/occludin/ZO-1 direct transcription in IEC (structural tight junction arm)

These are additive, not redundant. PXR pathway is the 4th independent gut barrier mechanism. Source organism: L. reuteri (already in protocol; produces IPA alongside IAd without IS co-production).

### Gut Barrier Mechanism Taxonomy (Complete as of run_094)

| Mechanism | Agent | Target | Run |
|---|---|---|---|
| 1. Akkermansia TLR2 | Akkermansia pasteurized | Claudin-3 ↑ | run_026 |
| 2. Butyrate HDAC | Tributyrin/L. reuteri | Claudin-4/ZO-1 gene expression | run_032 |
| 3. Zinc MLCK/Zonulin | Zinc bisglycinate 15-30 mg | ZO-1 protein stability + MLCK ↓ | run_059 |
| 4. IPA → PXR | L. reuteri (IPA co-production) | Claudin-1/occludin/ZO-1 transcription | run_094 |
| 5. AhR/IL-22 | L. reuteri (IAd) | MUC2/RegIII-γ mucosal defense | run_054 |

L. reuteri alone covers mechanisms 2 (partial; butyrate consortium), 4 (IPA → PXR), and 5 (IAd → AhR). It is the highest-leverage single probiotic for gut barrier in the protocol.

### PXR → TLR4 Suppression: Signal 1A Upstream Reduction

```
IPA → PXR → TLR4 gene transcription ↓
→ Fewer TLR4 receptors on intestinal epithelium
→ Same luminal LPS → less TLR4 engagement → less MyD88 → IKKβ → NF-κB
→ Less portal inflammatory cytokine entry → dermal macrophage Signal 1A priming ↓
```

IPA/PXR contributes to Signal 1A reduction upstream via two routes: physical barrier (claudin-1 → less LPS translocation) AND receptor density (TLR4 ↓ → less sensitivity to LPS that does translocate).

### HCQ Triple Node Benefit (Updated Protocol Logic)

The IDO1/tryptophan axis (run_091) extends to Node C via IPA/PXR:

```
High IFN-α (Node D elevated)
    → IDO1 ↑ → tryptophan depleted
    → Fork A: IAd ↓ → AhR ↓ → Treg ↓ → Node A ↓
    → Fork B: IPA ↓ → PXR ↓ → claudin-1 ↓ → Node C ↑ (I-FABP ↑)

HCQ → IFN-α ↓ → IDO1 ↓ → tryptophan preserved
    → Fork A restored: IAd ↑ → Treg ↑ → Node A ↑
    → Fork B restored: IPA ↑ → claudin-1 ↑ → Node C ↓
```

**Triple non-responder pattern** (Node D elevated + Node A below target + Node C elevated): IDO1-mediated tryptophan depletion is the candidate unifying mechanism. HCQ specialist referral addresses all three nodes simultaneously via the IDO1 axis. This pattern (D+A+C non-response) is now a specific HCQ indication within the framework.

### Node C Non-Responder Update

If I-FABP persistently elevated (>150 pg/mL) despite Akkermansia + butyrate + zinc (mechanisms 1-3):
1. Check Node D (IFN-α2 Simoa): if elevated → IDO1 → IPA depletion likely contributing
2. Check tryptophan intake: adequate protein diet supports all IPA production routes
3. If Node D normal: consider whether L. reuteri is established (IPA source for mechanism 4)

*Protocol_integration.md Part 9at — 2026-04-12 | IPA PXR NR1I2 claudin-1 occludin ZO-1 tight junction 4th gut barrier L. reuteri TLR4 suppression Signal 1A HCQ triple node benefit Node C IDO1 tryptophan | run_094*

---

## Part 9au — KLK5 → Bradykinin → B2R → TRPV1 Sensitization: Second KLK5 → M8 Pathway (run_095)

### Framework Context

KLK5 drives M8 via TWO parallel routes:
1. **KLK5 → LL-37 → TRPV1 direct activation** (run_015; established)
2. **KLK5 → kallidin → B2R → TRPV1 sensitization** (run_095; new)

Route 2 lowers TRPV1 threshold rather than activating it directly — meaning elevated Loop 1 activity makes ALL TRPV1 triggers (heat, spicy food, sun, TRPA1 co-activation) disproportionately potent.

### ACE-I vs ARB Selection Guidance (T1DM Rosacea)

| Medication | RAAS benefit | Bradykinin | TRPV1 effect | Preference |
|---|---|---|---|---|
| ACE-I (lisinopril, ramipril) | Ang II ↓ → NLRP3/NF-κB ↓ | ACE inhibited → accumulates | B2R → TRPV1 sensitization ↑ | Second choice if flushing prominent |
| ARB (losartan, irbesartan) | AT1R blocked → same benefit | ACE not inhibited → normal degradation | No B2R/TRPV1 worsening | Preferred in T1DM rosacea with active flushing |

**Clinical decision**: If a T1DM rosacea patient on ACE-I reports worsened flushing (distinct from cough), discuss ARB switch with prescriber. Both are ADA-guideline approved for T1DM nephroprotection; ARB mechanistically superior for rosacea-flushing phenotype.

### B1R Amplification Note

During active rosacea flares, IL-1β (from NLRP3 → Loop 2) upregulates B1R expression. Anti-NLRP3 protocol → IL-1β ↓ → B1R ↓ → less bradykinin sensitization during flares. This is an additional anti-M8 benefit of Loop 2 management not previously documented in the protocol.

### Loop 1 Management → Bradykinin Reduction

All existing Loop 1 interventions that reduce KLK5 activity also reduce kallidin generation:
- Spermidine/LEKTI (run_060), AzA (run_082), topical ivermectin (run_046), skin pH acidification

No new agents required. The mechanistic value: explains why Loop 1 control improves neurogenic symptoms beyond just reducing LL-37 — it also reduces bradykinin-mediated TRPV1 sensitization, lowering the threshold for all flushing triggers.

*Protocol_integration.md Part 9au — 2026-04-12 | KLK5 bradykinin kallidin B2R B1R TRPV1 sensitization PKC PGE2 PKA Loop 1 M8 bridge ACE-I paradox ARB T1DM KKS NLRP3 B1R upregulation | run_095*

---

## Part 9av — Non-Canonical Inflammasome: NLRP3 Bypass + Loop 2 Non-Responder Protocol (run_096)

### Framework Context

The non-canonical inflammasome (cytosolic LPS → caspase-4/5 → GSDMD) bypasses all 7 NLRP3 inhibition mechanisms in the protocol. It represents a Loop 2 activity driver that persists even when NLRP3 is pharmacologically suppressed.

**Critical insight for non-responders**: Persistent erythema/flushing/inflammation despite comprehensive anti-NLRP3 protocol (BHB + colchicine + SIRT1/melatonin + zinc + spermidine + AMPK + NR/SIRT3) → non-canonical pyroptosis from cytosolic LPS is a candidate co-driver. The clinical marker is Node C (I-FABP elevated) indicating ongoing LPS translocation.

### Loop 2 Non-Responder Tiered Protocol (Updated with Run_096)

```
Loop 2 non-responder (persistent NLRP3 activity despite anti-NLRP3 tier):
    
Step 1: Confirm Node C (I-FABP)
    > 150 pg/mL → gut LPS translocation confirmed → non-canonical caspase-4/5 active
    
Step 2: If Node C elevated → intensify gut barrier (all 4 mechanisms):
    Tier A: Akkermansia pasteurized (claudin-3; run_026) — ensure present
    Tier B: Tributyrin/L. reuteri (claudin-4/ZO-1; run_032) — confirm dose
    Tier C: Zinc bisglycinate 25-30 mg/day (ZO-1/MLCK; run_059) — optimize
    Tier D: L. reuteri IPA → PXR → claudin-1 (run_094) — same organism as Tier B
    
Step 3: Reduce gram-negative dysbiosis source
    → Confirm low-FODMAP during flares (reduces fermentation substrates for gram-negative)
    → Evaluate for SIBO if gastroparesis suspected (T1DM)
    
Step 4: If Node C controlled but Loop 2 persists → consider HMGB1 suppression as indirect lever
    → Better canonical NLRP3 control → less pyroptosis → less HMGB1 → less non-canonical feed-forward
    → Review anti-NLRP3 protocol completeness
```

### Node C Monitoring: Updated Mechanistic Basis

Node C (I-FABP target <150 pg/mL) now covers THREE gut-to-dermis pathways:
1. LPS → TLR4 → NF-κB → Signal 1A priming (canonical) — established from run_001
2. Cytosolic LPS → caspase-4/5 → GSDMD (non-canonical pyroptosis bypass) — run_096
3. LPS → HMGB1-LPS complex → caspase-4/5 feed-forward — run_096

Node C is the single most important monitoring marker for LPS-driven disease: it reflects gut permeability that feeds all three LPS-dependent inflammation pathways.

### ACE-I note (from run_095 + run_096 combined)

T1DM patients on ACE-I with elevated Node C AND active flushing → two separate concerns:
1. Bradykinin accumulation → B2R → TRPV1 sensitization (run_095: ARB preferred)
2. Gut LPS → caspase-4/5 → non-canonical pyroptosis (run_096: gut barrier priority)

These are independent. Addressing both: (a) ARB switch if flushing-dominant phenotype; (b) gut barrier intensification if Node C elevated.

*Protocol_integration.md Part 9av — 2026-04-12 | non-canonical inflammasome caspase-4 caspase-5 GSDMD LPS cytosol HMGB1 Loop 2 non-responder Node C gut barrier T1DM endotoxemia | run_096*

---

## Part 9aw — VIP/PACAP: M8 Neuropeptide Triad + Mast Cell Anti-Histamine Insufficiency (run_097)

### Framework Context

M8 neurogenic neuropeptide coverage is now complete: SP (run_019) + CGRP (runs 015/093) + VIP/PACAP (run_097). All three co-released from the same facial C-fibers. Three parallel non-IgE mast cell activation routes; three parallel vasodilation mechanisms.

### Clinical Implication: Why Antihistamines Are Insufficient for Neurogenic Rosacea

Antihistamines (H1 blockers: cetirizine, loratadine) block H1R consequences of mast cell histamine release. They do not:
- Block VIP/PACAP → VPAC1/PAC1 → mast cell degranulation (VIP/PACAP-driven degranulation continues)
- Block CGRP → vasodilation (CLR/RAMP1, not H1R)
- Block VIP → VPAC2 → vasodilation (VPAC2, not H1R)
- Prevent tryptase release (→ PAR-2 → KLK5)

Anti-histamines reduce only ONE product of mast cell degranulation. The vasodilation from CGRP + VIP + PACAP + SP/NK1R/endothelial-NO is unaffected.

**Better M8 management strategy (layered approach):**

| Intervention | What it blocks | Evidence |
|---|---|---|
| Mast cell stabilizers (cromolyn, ketotifen; run_042) | All mast cell degranulation routes (broad) | Moderate |
| TRPV1 management (run_015) | C-fiber SP/CGRP/VIP/PACAP release at source | Established |
| TRPA1 agonist reduction (run_093) | C-fiber activation from 4-HNE/food triggers | Established |
| Bradykinin/B2R reduction (run_095) | TRPV1 sensitization → less trigger-responsiveness | Established |
| Antihistamines | H1R consequences of histamine only | Limited/symptom |
| Brimonidine/oxymetazoline (topical; not in protocol) | Downstream α2-adrenergic vasoconstriction | Symptomatic |

For M8-dominant rosacea: mast cell stabilizer + upstream C-fiber activation reduction is mechanistically superior to antihistamine monotherapy.

### PACAP → HPA: Fast Neurogenic HPA Activation

Stress triggers (emotional, sensory) → TRPV1/TRPA1 → PACAP → PAC1 on hypothalamic PVN → immediate CRH → HPA axis. This is the mechanism for rapid flush onset with emotional stress — faster than cytokine-mediated HPA (IL-1β → CRH route takes minutes; PACAP neuropeptide route takes seconds). No protocol modification needed; explains clinical observation of instant stress-triggered flush before any inflammatory cytokine elevation.

*Protocol_integration.md Part 9aw — 2026-04-12 | VIP PACAP VPAC1 VPAC2 PAC1 neurogenic neuropeptide mast cell non-IgE antihistamine insufficiency HPA CRH layered M8 management | run_097*

---

## Part 9ax — ER Stress / UPR: 12th NF-κB Mechanism + Loop 4 Positive Feedback + SIRT1 6th Mechanism (run_098)

### Non-Responder IL-6 Protocol Implication

If IL-6 remains elevated despite full NF-κB suppression protocol (all 11 mechanisms: colchicine + sulforaphane + vagal + CAPE + MK-7 + ivermectin + L-citrulline + calcitriol + GLP-1 + PPARγ + SIRT6):

**Candidate mechanism**: IRE1α → XBP1s → NF-κB-independent IL-6 transcription from ER-stressed macrophages or sebaceous cells. IRE1α → TRAF2 → NF-κB operates from inside the ER membrane — all 11 NF-κB suppression pathways target extracellular-to-nuclear signal chains and cannot block IRE1α/TRAF2.

**Management lever**: Reduce upstream ER stress:
1. **Niacinamide → SIRT1 → HSF1 → HSP70/BiP** (6th SIRT1 mechanism): ensure niacinamide 500mg/day is in place; consider NR upgrade (run_090) for SIRT3/SIRT6/SIRT1 maximal coverage
2. **Sulforaphane → Nrf2 → HO-1/NQO1** (run_027): oxidative load ↓ → ER protein oxidation ↓ → IRE1α/ATF6 ↓
3. **SIRT3 → SOD2 → mROS ↓** (run_090): mROS → protein carbonylation → ER stress; SIRT3/NR reduces this
4. **AzA → 4-HNE ↓** (run_082): 4-HNE Michael adducts ER proteins → IRE1α/ATF6; AzA interrupts ATF6/SREBP2/squalene loop

### SIRT1 Six-Mechanism Summary (Updated)

| # | SIRT1 target | Mechanism | Protocol source |
|---|---|---|---|
| 1 | NLRP3 Lys254 | NLRP3 inhibition (run_031) | Niacinamide |
| 2 | NF-κB p65 Lys310 | NF-κB ↓ (run_031) | Niacinamide |
| 3 | PGC-1α | Mitochondrial biogenesis (run_031) | Niacinamide |
| 4 | FOXO3a | SOD2/catalase/mitophagy (run_031) | Niacinamide |
| 5 | Beclin-1/LC3 | Autophagy induction (run_031) | Niacinamide |
| 6 | HSF1 Lys208 | HSP70/BiP → ER stress ↓ (run_098) | Niacinamide |

All six mechanisms are activated by the same niacinamide → NAD⁺ → SIRT1 pathway. No new agents needed for ER stress coverage.

### T1DM β Cell Notes (run_098)

**Three β cell death mechanisms now in framework:**
1. Intraislet NLRP3 → IL-1β → iNOS → β cell apoptosis (run_043)
2. CTL-mediated cytotoxicity (MHC-I upregulation; run_088 HCQ mechanism)
3. IFN-α → PERK → eIF2α → CHOP → β cell apoptosis (run_098) — HCQ → IFN-α ↓ benefits this pathway too

**HCQ four-node coverage** (updated from run_088 analysis):
- Node D ↓ (direct IFN-α → TLR7/9 block)
- Node A ↑ (IDO1 → tryptophan → IAd → Treg; run_091)
- Node C ↓ (IDO1 → IPA → PXR → claudin-1; run_094)
- β cell ↑ (IFN-α → PERK → CHOP ↓; run_098)

*Protocol_integration.md Part 9ax — 2026-04-12 | ER stress UPR IRE1α XBP1s TRAF2 IKKβ NF-κB 12th mechanism ATF6 SREBP2 squalene Loop 4 SIRT1 HSF1 HSP70 BiP T1DM β cell PERK CHOP HCQ four nodes | run_098*

---

## Part 9ay — IL-33 / ST2 / TSLP: Alarmin Mast Cell Activation + Loop 1 Amplification (run_099)

### Updated Mast Cell Activation Overview

Rosacea mast cells can be activated via five routes. Only one is IgE-dependent (standard allergic); four are IgE-independent:

| Route | Activation signal | Therapeutic lever |
|---|---|---|
| IgE-dependent | IgE + allergen → FcεRI crosslinking | Antihistamines (H1R) + avoidance |
| NK1R | SP from C-fibers (run_019) | TRPV1/TRPA1 reduction → less SP |
| MRGPRX2 | CGRP from C-fibers (run_093) | TRPV1/TRPA1 reduction → less CGRP |
| VPAC1/PAC1 | VIP/PACAP from C-fibers (run_097) | TRPV1/TRPA1 reduction → less VIP/PACAP |
| **ST2** | **IL-33 from UV-damaged keratinocytes (run_099)** | **UV protection + calcitriol/VDR + mast cell stabilizer** |

**Clinical take**: Antihistamines block only the downstream histamine effects — not any of the four non-IgE activation routes. Mast cell stabilizers (quercetin, EGCG, cromolyn/ketotifen if prescribed) act on all five routes. For neurogenic routes (1-3), upstream TRPV1/TRPA1 management reduces trigger sensitivity. For the alarmin route (4), UV protection and VDR/calcitriol reduce IL-33 release.

### Tryptase → PAR-2 → Loop 1: Clinical Implication

Mast cell degranulation via ST2 releases tryptase → tryptase cleaves PAR-2 on keratinocytes → KLK5 ↑ → Loop 1 amplification. This creates a UV → mast cell → Loop 1 arc:

**Pattern**: UV-predominant trigger pattern + Loop 1 non-responder → consider whether alarmin route is feeding Loop 1. If ivermectin/AzA managing KLK5 but UV exposure ongoing → residual alarmin-driven Loop 1 amplification.

**Management step**: Reinforce UV protection + calcitriol adequacy (Node E: 25(OH)D3 > 60 ng/mL; VDR-mediated keratinocyte photoprotection) + confirm mast cell stabilizer (quercetin/EGCG) in place.

### Post-UV Persistent Flare Pattern

UV releases IL-33 (acute mast cell degranulation) + TSLP (mast cell priming → upregulates ST2 → lowers threshold for 24-48h post-UV). Explains multi-day flare elevation after UV exposure that outlasts the initial acute flush.

**Management**: UV avoidance remains mechanistically critical. Physical sunscreen (zinc oxide, titanium dioxide) preferred (chemical UV filters may transiently penetrate barrier). Note: calcitriol/VDR → keratinocyte differentiation → more robust barrier → less UV penetration reaching keratinocyte nuclei.

### sST2 and Node A: Additional Rationale for Treg Correction

Tregs produce soluble ST2 (sST2) — decoy receptor for IL-33. Patients with low Node A (Foxp3+ Treg < 5% CD4+) have reduced sST2 → more free IL-33 → enhanced mast cell degranulation:

```
Node A ↓ → sST2 ↓ → IL-33 → ST2 → mast cell ↑
```

**Additional point for Node A correction decision** (AKG + Vitamin C → Foxp3 TSDR demethylation, runs 086-087): Beyond T cell polarization, Treg expansion restores sST2 brake on IL-33/mast cell axis. Patients with low Node A + UV-predominant triggers are candidates for this mechanism.

### Chymase → Ang II: Reinforces ARB Over ACE-I (Third Mechanism)

Mast cell chymase → local skin Ang II independent of ACE. ACE inhibitors cannot block this.

**Cumulative ARB reasoning for T1DM rosacea with active flushing:**
1. Systemic RAAS: ARB blocks AT1R wherever Ang II comes from (ACE or chymase)
2. Bradykinin: ACE-I → bradykinin accumulation → B2R → TRPV1 → worsened flushing (run_095)
3. Local skin RAAS: Mast cell chymase → Ang II bypasses ACE entirely (run_099)

In any T1DM rosacea patient where RAAS management is indicated (e.g., nephroprotection): ARB > ACE-I for all three independent mechanistic reasons. Document in clinical note if switching patient from ACE-I to ARB: reduces flushing risk while maintaining RAAS/nephroprotective benefit.

### T1DM Notes (run_099)

IL-33 → ST2 on islet macrophages → IL-1β → β cell. Evidence: Guo 2014 J Immunol — ST2-KO NOD mice show delayed T1DM onset. Serum sST2 elevated in T1DM patients (Bartleson 2020 JCI Insight) — likely compensatory. β cell ER stress (run_098: PERK/CHOP) → necroptosis → IL-33 nuclear release → ST2 → IL-1β feed-forward. HCQ → IFN-α ↓ → PERK ↓ → less β cell necroptosis → less islet IL-33 release: this is now HCQ's 5th T1DM-relevant mechanism (add to HCQ four-node coverage as: **Node D/β cell PERK/CHOP/IL-33 chain**).

### Monitoring (no new nodes; existing coverage applies)

| IL-33 relevant | T-index / Node | Management |
|---|---|---|
| UV-driven IL-33 → mast cell | Node E (Vitamin D/VDR) | 25(OH)D3 > 60 ng/mL |
| Treg/sST2 deficit | Node A (Foxp3+ Treg) | AKG + Vitamin C if < 8% CD4+ |
| Mast cell tryptase → KLK5 | No dedicated node; Loop 1 clinical | Ivermectin/AzA + mast cell stabilizer |
| Chymase → Ang II | No dedicated node | ARB in RAAS-indicated patients |

*Protocol_integration.md Part 9ay — 2026-04-12 | IL-33 ST2 TSLP alarmin mast cell tryptase chymase PAR-2 KLK5 Loop 1 UV keratinocyte ARB sST2 Treg Node A Node E T1DM islet | run_099*

---

## Part 9az — MAIT Cells: Gut Dysbiosis → Innate IL-17; T1DM Depletion; L. reuteri and HCQ MAIT Mechanisms (run_100)

### New Mechanistic Context for Existing Protocol Agents

Run_100 adds mechanistic depth to two already-recommended agents. No new agents or monitoring changes.

**L. reuteri — MAIT suppression mechanism (new):**
L. reuteri does not produce 5-OP-RU (the MR1 ligand that activates MAIT cells) — it produces riboflavin but does not complete the biosynthesis pathway to the unstable azomethine intermediate. Proteobacteria (E. coli, Klebsiella, H. pylori) do. L. reuteri → competitive displacement of proteobacteria → less 5-OP-RU → less MAIT activation → less IL-23-independent IL-17.

This means L. reuteri suppresses IL-17 production via three distinct mechanisms now mapped:
1. **IAd/AhR/Treg (run_054)**: L. reuteri → IPA → AhR → Treg expansion → Th17 suppression
2. **IPA/PXR/claudin-1 (run_094)**: gut barrier → less LPS → less Signal 1A
3. **MAIT/5-OP-RU (run_100)**: competitive proteobacteria displacement → less innate IL-17

Probiotic compliance and strain specificity are reinforced: L. reuteri (not a generic Lactobacillus species) specifically addresses all three mechanisms. Strain specificity matters.

**HCQ — MAIT protection mechanism (new, 5th HCQ benefit):**
HCQ → IFN-α ↓ → MAIT exhaustion ↓ → functional MAIT pool maintained → better gut microbial surveillance → less proteobacteria expansion. This is an additional rationale for HCQ in Node D-elevated patients: beyond the direct IFN-α → TLR7/9 block and IDO1/tryptophan benefits, HCQ preserves MAIT cell function, which in turn suppresses the innate IL-17 arm.

**Updated HCQ benefit summary:**
1. Node D ↓ (TLR7/9 → IFN-α block; run_088)
2. Node A ↑ (IDO1 → tryptophan → IAd → Treg; run_091)
3. Node C ↓ (IDO1 → IPA → PXR → claudin-1; run_094)
4. β cell protection (IFN-α → PERK → CHOP ↓; run_098)
5. **MAIT protection (IFN-α → MAIT exhaustion ↓ → gut surveillance maintained; run_100)**

### IL-17 Source Taxonomy (Updated)

Three distinct IL-17 sources now in framework:

| IL-17 source | Activation pathway | IL-23 required | Speed | Suppression strategy |
|---|---|---|---|---|
| Th17 | IL-6 + TGF-β → RORγt → IL-23 stabilization | YES | Days | Node A (Treg) + IL-23 blockade (run_079) |
| Th22 | IL-6 → AhR → IL-22 (also some IL-17; run_080) | Variable | Days | AhR management |
| **MAIT** | **5-OP-RU → MR1 → TCR + IL-12/IL-18** | **NO** | **Hours** | **L. reuteri + HCQ** |

Clinical implication: A patient with persistent IL-17 elevation despite optimal Th17 suppression (Node A correction + Node C gut barrier + Th17 management) → MAIT-derived IL-17 component may be active. Reinforce L. reuteri compliance and H. pylori screening (H. pylori is among the highest 5-OP-RU producers; H. pylori → MAIT hyperactivation is documented).

### T1DM-Specific Notes

Richardson 2016: MAIT cell depletion at T1DM onset. In T1DM patients on this protocol:
- IFN-α monitoring (Node D) addresses the primary driver of MAIT exhaustion
- HCQ in Node D-elevated patients has a fifth mechanistic benefit (MAIT)
- H. pylori eradication (if present; M7 run_030) removes one of the highest 5-OP-RU sources

MAIT depletion is not directly reversible by any current protocol element. However: IFN-α suppression (HCQ) → less exhaustion → slower depletion rate. Long-term: reducing the chronic MAIT activation burden (via L. reuteri + H. pylori eradication + IFN-α suppression) may help preserve the residual MAIT pool.

### Monitoring: No New Nodes

MAIT cell frequency is measurable (Vα7.2+CD161+ or MR1-tetramer staining), but not currently recommended as a routine monitoring parameter. It is technically complex and clinically actionable mainly for specialist T1DM centers. No T-index modification required.

*Protocol_integration.md Part 9az — 2026-04-12 | MAIT MR1 5-OP-RU riboflavin L. reuteri probiotic specificity HCQ five benefits IL-17 sources Th17 Th22 MAIT T1DM H. pylori | run_100*

---

## Part 9ba — Complement: Signal 1E (5th NLRP3 Priming); UV Composite; T1DM C4A Null (run_101)

### Signal 1E — Clinical Decision Rules

**Five independent NLRP3 priming signals:**

| Signal | Source | Suppress how |
|---|---|---|
| 1A (NF-κB/LPS) | Gut dysbiosis | Gut barrier (Node C) + TLR4 management |
| 1B (ISGF3/IFN-α) | HERV-W/M3 | HCQ (Node D); IFN-α monitoring |
| 1C (HIF-1α) | OSA/succinate | CPAP; PPAR-α/omega-3 |
| 1D (STAT3/leptin) | Metabolic/obesity | GLP-1R; lifestyle |
| **1E (AP-1/C5a)** | **Complement** | **Gut barrier (less LPS) + UV protection + H. pylori eradication** |

Signal 1E is not suppressed by any of the 11 NF-κB suppression pathways. The upstream lever is: less complement activation = less C5a. Downstream: the 7 NLRP3 inhibitors act at NLRP3 activation, not priming — they remain effective regardless of which priming signal is active.

**Non-responder with persistent NLRP3/IL-1β despite 4 upstream signals managed**: Consider Signal 1E. Check: (a) H. pylori status (eradication if positive); (b) UV compliance (complement is a UV-triggered inflammatory pathway); (c) Node C (gut barrier — less LPS → less alternative complement).

### UV Composite Model (New Framework Synthesis)

UV is now mapped to 5 distinct independent inflammatory mechanisms across 5 time windows:
1. IL-33 → ST2 → mast cell (run_099; seconds)
2. Complement → C3a/C5a → mast cell + NLRP3 (run_101; minutes)
3. TSLP → mast cell priming (run_099; hours)
4. Keratinocyte NLRP3 → IL-1β (run_048; hours)
5. HERV-W/IFN-α → Signal 1B (run_040; hours-days)

**Clinical implication**: UV-triggered flares are the most refractory because they activate mechanisms across hours to days. Management strategy: comprehensive UV protection (physical sunscreen + calcitriol/VDR) is mechanistically the highest-leverage UV intervention, reducing all five mechanisms simultaneously at the source.

### T1DM C4A Null (Non-Actionable; Context Only)

C4A null allele (~30% of T1DM patients): impaired apoptotic cell clearance → β cell autoantigen exposure → accelerated anti-islet immunity. Not addressable by protocol. Provides mechanistic context for rapid progressors — patients with C4A null + other risk signals may benefit from specialist T1DM care escalation. Document in context when evaluating T1DM + rosacea patients with rapid progression despite protocol adherence.

*Protocol_integration.md Part 9ba — 2026-04-12 | complement C3a C5a Signal 1E NLRP3 5 priming signals AP-1 UV composite H. pylori C4A T1DM non-responder | run_101*

---

## Part 9bb — γδ T Cells + NK Cells: NKG2D/MICA; HMBPP/BTN3A1; NK-ADCC; L. reuteri 4th Mechanism (run_102)

### L. reuteri Four-Mechanism IL-17 Suppression (Updated)

L. reuteri is now documented to suppress IL-17 production via four distinct mechanisms:

| Mechanism | Pathway | Run |
|---|---|---|
| 1 | IAd/AhR → Treg expansion | run_054 |
| 2 | IPA/PXR → claudin-1/gut barrier → less LPS | run_094 |
| 3 | Competitive 5-OP-RU displacement (MAIT suppression) | run_100 |
| 4 | Competitive HMBPP displacement (Vγ9Vδ2 suppression) | run_102 |

Clinical implication: L. reuteri has more mechanistic justification than any single other probiotic in the protocol. Strain specificity matters — generic "Lactobacillus" products may not provide mechanisms 3 and 4 (which depend on competitive displacement of specific proteobacteria). DSM 17938 and ATCC PTA 6475 are the strains with the most mechanistic support.

### HCQ 6-Mechanism Summary (T1DM Context)

| # | HCQ benefit | Mechanism | Run |
|---|---|---|---|
| 1 | Node D ↓ | TLR7/9 → IFN-α block | run_088 |
| 2 | Node A ↑ | IDO1 → tryptophan → IAd → Treg | run_091 |
| 3 | Node C ↓ | IDO1 → IPA → PXR → claudin-1 | run_094 |
| 4 | β cell ER stress ↓ | IFN-α → PERK → CHOP ↓ | run_098 |
| 5 | MAIT protection | IFN-α → MAIT exhaustion ↓ | run_100 |
| 6 | NK-ADCC ↓ | HERV-W ↓ + anti-islet IgG ↓ → NK activation ↓ | run_102 |

All six operate through IFN-α suppression or anti-autoimmune consequences of IFN-α reduction. For Node D-elevated T1DM rosacea patients, HCQ has a compelling multi-target benefit profile justifying specialist consultation.

### β Cell Death Mechanisms: Complete Six-Mechanism Overview

| # | Mechanism | Intervention | Run |
|---|---|---|---|
| 1 | NLRP3 → IL-1β → iNOS | Colchicine/BHB/7 NLRP3 inhibitors | run_043 |
| 2 | CTL cytotoxicity via MHC-I | HCQ → IFN-α ↓ → MHC-I normalized | run_088 |
| 3 | IFN-α → PERK → CHOP → apoptosis | HCQ → IFN-α ↓; SIRT1/HSF1/BiP | run_098 |
| 4 | IL-33 → islet macrophage → IL-1β | HCQ → IFN-α ↓ → PERK ↓ → less necroptosis | run_099 |
| 5 | Complement C5a → Signal 1E → NLRP3 | Gut barrier + UV + H. pylori eradication | run_101 |
| 6 | NK-ADCC: anti-islet IgG → CD16 | HCQ → IgG ↓ + HERV-W ↓ | run_102 |

The only mechanism not primarily addressed by existing protocol is #5 (complement C5a; upstream gut barrier/UV control). Mechanisms 1-4 and 6 are covered by NLRP3 inhibitors + HCQ in combination.

### NKGD2/MICA — Non-Responder Flag

**Pattern**: UV-dominant triggers + persistent IL-17 despite TRPV1/TRPA1 control + mast cell stabilizers → NKG2D/MICA stress-surveillance contribution may be active.

**Management**: Reinforce UV protection + calcitriol/VDR (keratinocyte resilience → less stress → less MICA) + niacinamide (SIRT1 → HSF1 → BiP → ER stress ↓ → MICA ↓). No specific NKG2D blocker available clinically.

*Protocol_integration.md Part 9bb — 2026-04-12 | γδ T cells NK NKG2D MICA HMBPP BTN3A1 L. reuteri 4 mechanisms HCQ 6 benefits T1DM β cell 6 death mechanisms NK-ADCC HERV-W | run_102*

---

## Part 9bc — Regulatory B Cells (Bregs/B10): IL-10; Node A 5th Input; Akkermansia + Butyrate New Mechanisms; HCQ 7th Benefit (run_103)

### Node A Upstream Input Map (Complete, run_103)

Five upstream pathways now identified that induce Foxp3+ Tregs (Node A):

| # | Pathway | Protocol element | Run |
|---|---|---|---|
| 1 | IAd → AhR → Foxp3 | L. reuteri (IPA/IAd production) | run_054 |
| 2 | AKG/Vit C → TET2 → TSDR demethylation | AKG + Vitamin C supplementation | runs 086/087 |
| 3 | GLP-1R → PKA → Foxp3 | GLP-1 agonists (T1DM context) | run_073 |
| 4 | VDR/calcitriol → Foxp3 | Calcitriol/Vitamin D (Node E) | run_039 |
| 5 | **Breg (ICOS-L + IL-10 + TGF-β) → contact-dependent Foxp3** | **Gut barrier → B10 pool maintenance** | **run_103** |

Node A non-responders to AKG/Vitamin C (Foxp3 TSDR demethylation) may have Breg depletion as co-factor. Management: address gut barrier (Node C → less LPS → less TLR4 → less plasmablast bias → relative B10 restoration) + IFN-α management (HCQ → B10 preserved).

### Akkermansia Updated Mechanism Count

Akkermansia muciniphila now has three documented mechanisms in the framework:
1. Claudin-3/occludin tight junction restoration (run_026)
2. Amuc_1100 → TLR2 → B10/Breg induction (run_103)
3. A2 protein → GPR41 → gut motility context (run_026 extension, minor)

Akkermansia protocol justification is further reinforced.

### Butyrate Three-Mechanism Summary

Butyrate (from gut microbiome / prebiotic fiber support):
1. HDAC inhibition → claudin-4/occludin → gut barrier (run_032)
2. Foxp3 demethylation → Treg stabilization (runs 086/087)
3. HDAC inhibition → B10 cell differentiation in GALT (run_103)

All three are HDAC-dependent. A single intervention — prebiotic fiber increasing butyrate-producing bacteria (Faecalibacterium prausnitzii, Roseburia) — provides all three benefits.

### HCQ 7-Mechanism T1DM Summary

| # | Benefit | Pathway |
|---|---|---|
| 1 | Node D ↓ | TLR7/9 → IFN-α block (run_088) |
| 2 | Node A ↑ | IDO1 → Treg (run_091) |
| 3 | Node C ↓ | IDO1 → IPA → claudin-1 (run_094) |
| 4 | β cell ER stress ↓ | PERK → CHOP ↓ (run_098) |
| 5 | MAIT protection | IFN-α → MAIT exhaustion ↓ (run_100) |
| 6 | NK-ADCC ↓ | HERV-W ↓ + IgG ↓ (run_102) |
| 7 | **B10/Breg preserved** | **IFN-α ↓ → IRF7 → B10 ↓ prevented (run_103)** |

*Protocol_integration.md Part 9bc — 2026-04-12 | Breg B10 Node A 5 inputs Akkermansia Amuc_1100 butyrate HCQ 7 benefits T1DM gut barrier IgA complement | run_103*

---

## Part 9bd — Tfh / GC: Autoantibody Origin; Quercetin 7th Mechanism; Tfr and Node A; HCQ GC Suppression (run_104)

### Completed Autoantibody Causal Chain

The framework now has a complete causal chain from gut dysbiosis to complement/NK-ADCC autoantibody-driven inflammation:

```
M1/M3 dysbiosis + antigen release →
IL-6 (STAT3 → BCL6) + IFN-α (Tfh1) → Tfh expansion →
GC in lymph nodes → IL-21/AID → high-affinity IgG →
Anti-keratinocyte IgG → C1q → complement C5a (runs 064/101) →
Anti-islet IgG → NK-ADCC (run_102)
```

All upstream interventions in the protocol reduce the IgG load downstream:
- Gut barrier (Node C) → less antigen → less BCR activation → less Tfh
- IL-6 reduction (multiple agents) → less BCL6 induction → less Tfh
- HCQ → IFN-α ↓ → less Tfh1 + Tfr precursor maintained
- Node A correction → Treg → Tfr precursor pool
- Quercetin → JAK1/3 → GC B cell survival ↓ (new mechanism)

### Quercetin 7-Mechanism Consolidated Summary

| # | Mechanism | Target | Run |
|---|---|---|---|
| 1 | Mast cell stabilization | Mast cell degranulation ↓ | run_042 |
| 2 | C1q binding inhibition | Classical complement ↓ | run_042/064 |
| 3 | PPARγ → NF-κB transrepression | Macrophage NF-κB ↓ | run_077 |
| 4 | PPARγ → RORγt ↓ | Th17 differentiation ↓ | run_079 |
| 5 | IDO1 inhibition | Tryptophan preservation → IAd → Treg ↑ | run_091 |
| 6 | TLR9 partial inhibition | CpG-driven IFN-α ↓ | run_088 context |
| 7 | JAK1/3 → IL-21R/STAT3 in GC B cells | Affinity maturation ↓ → IgG ↓ | run_104 |

Quercetin now addresses: mast cell, complement, NF-κB, Th17, Treg, IFN-α, AND GC/autoantibody — spanning nearly every major inflammatory axis in the framework from a single agent already in protocol.

### Node A and Tfr: Clinical Note

AKG + Vitamin C → Foxp3 TSDR demethylation → Treg ↑ → Tfr precursor pool ↑. In patients with persistent autoantibody-driven inflammation (rising anti-islet titers despite gut barrier management): Node A correction may reduce unrestrained GC via Tfr restoration (partial). Combined HCQ (→ IL-2 preservation + Tfr maintenance) + Node A correction = dual Tfr support strategy.

*Protocol_integration.md Part 9bd — 2026-04-12 | Tfh BCL6 GC autoantibody IgG Tfr Node A quercetin 7 mechanisms HCQ T1DM complement NK-ADCC | run_104*

---

## Part 9be — PTX3: Tissue-Local Complement; FGF-2 Counter-Regulation; Loop 2 Arc; Node B Extension (run_105)

### Local vs. Systemic Complement Activation: Clinical Distinction

Run_101 established complement C3a/C5a as major inflammatory mediators. Run_105 adds the LOCAL initiation mechanism. For clinical interpretation:

| Complement Initiator | Source | Detectable As | When Elevated |
|---|---|---|---|
| CRP → C1q (systemic) | Liver | Serum CRP | Systemic inflammation, infective |
| IgG → C1q (adaptive) | GC/plasma cells | Anti-islet/anti-keratinocyte IgG | Chronic autoimmune phase |
| Alternative pathway (UV) | Oxidized lipids/DAMPs | C3d skin deposits | UV-triggered acute flares |
| **PTX3 → C1q (local)** | **Mast cell/macrophage/endothelial** | **Serum PTX3 > 3.4 ng/mL** | **Local tissue inflammation** |

**Practical implication**: A T1DM rosacea patient with active skin flares but normal CRP and no detectable anti-keratinocyte IgG may have local PTX3-driven complement as the dominant mechanism. Node B (hsCRP + IL-6 + waist) may be falsely reassuring. If PTX3 ≥ 3.4 ng/mL in this patient → assume local classical complement active → add quercetin dose emphasis (C1q-binding inhibition, mechanism 2) + reinforce colchicine compliance (IL-1β block → reduces PTX3 induction).

### FGF-2 and the ETR Telangiectasia Mechanism

New mechanistic understanding for patients in whom telangiectasias continue to accumulate despite controlled active inflammation (low hsCRP, controlled Node B):

```
Between-flare quiescent phase:
  PTX3 LOW → FGF-2 NO LONGER sequestered →
  FGF-2 acts on FGFR1 on endothelial cells →
  Progressive vessel expansion → telangiectasia accumulation
```

Intervention gap identified: no agent in current protocol directly targets FGF-2-driven angiogenesis. Agents with anti-angiogenic properties relevant to consider:
- **Niacinamide**: documented to reduce erythema and possibly telangiectasia (indirect SIRT1/mitochondrial mechanism; run_025/031); no direct FGF-2 data
- **Calcitriol/VDR** (run_039): VDR activation has some anti-angiogenic effects in epithelial tissue; no rosacea-FGF-2 data
- **Omega-3/PPAR-α** (run_089): PPAR-α activates downstream of fatty acid oxidation; limited anti-angiogenic FGF-2 data
- **No protocol agent directly inhibits FGF-2 signaling**: this is an acknowledged gap if ETR telangiectasia is the primary complaint

Protocol note: For patients with predominantly ETR (telangiectasias, persistent erythema > papulopustular) and elevated PTX3: the complement→IL-1β→PTX3 feedback loop may be driving both inflammation AND indirectly enabling FGF-2 accumulation (PTX3 elevated = complement active; when flare resolves and PTX3 drops, FGF-2 acts). Breaking the Loop 2→PTX3→complement arc with colchicine + quercetin reduces both complement damage AND, paradoxically, may allow sustained (non-inflammatory) PTX3 at lower levels that maintain some FGF-2 sequestration. No intervention for the inter-flare FGF-2 window currently in protocol.

### Loop 2 Non-Responder: Updated Arc Map

For patients where Signal 1E (C5a→AP-1→NLRP3) is dominant and Loop 2 is active, the full arc is now:

```
Loop 2 active:
NLRP3 → IL-1β → PTX3 ↑ → C1q → C5a → AP-1 → NLRP3 (not NF-κB)
↓
Cannot be interrupted by: NF-κB suppressors (11 pathways)
CAN be interrupted by:
  → Colchicine (IL-1β secretion + NLRP3 assembly ↓)
  → Quercetin (C1q-binding inhibition → less classical complement activation)
  → BHB / SIRT1 (NLRP3 assembly ↓)
  → AMPK/spermidine (NLRP3 Ser291 ↓)
```

Signal 1E + Loop 2 + PTX3 arc = the most NF-κB-resistant NLRP3 amplification circuit identified in the framework. Clinical marker: patient with 11 NF-κB-suppressor drugs showing partial response, microalbuminuria rising, PTX3 elevated, CRP normal → this arc is likely active. Priority: colchicine dose optimization + quercetin dose verification.

### HCQ and PTX3

HCQ → TLR7/9 block → IFN-α ↓ → NF-κB ↓ (indirect) → PTX3 ↓ (moderate). HCQ does not directly reduce IL-1β or TNF-α-driven PTX3 induction. For PTX3-dominant patients, colchicine remains the primary upstream blockade.

### T1DM Specific: PTX3 as Microalbuminuria Biomarker

For T1DM rosacea patients: Annual monitoring addition (if available):
- Serum PTX3 (upper normal: ~3.4 ng/mL)
- Rising PTX3 + microalbuminuria in same patient = convergent evidence for gut dysbiosis→endotoxemia→local complement→glomerular/islet damage loop
- Intervention priority in this scenario: Node C (gut barrier) → reduce endotoxemia → reduce TLR4/NF-κB → reduce PTX3 source. This reinforces the hierarchy: Node C management upstream of all complement mechanisms.

*Protocol_integration.md Part 9be — 2026-04-12 | PTX3 C1q complement FGF-2 ETR telangiectasia Loop 2 colchicine quercetin T1DM microalbuminuria Node B Node C HCQ | run_105*

---

## Part 9bf — S1P / SphK1 / S1PR: EGCG 4th Mechanism; β Cell Ceramide Management; T1DM Trafficking (run_106)

### Protocol Additions and Clarifications

**EGCG: Updated to 4 Mechanisms**

| # | Mechanism | Evidence |
|---|---|---|
| 1 | PPARγ activation → NF-κB transrepression | run_077 |
| 2 | Nrf2 activation → antioxidant/HO-1 | run_027 context |
| 3 | IDO1 inhibition → tryptophan preservation → IAd → Treg | run_091 |
| 4 | **SphK1 inhibition → S1P↓ → TRAF2/NF-κB↓** | **run_106 (Pchejetski 2010; Bao 2014)** |

EGCG now interrupts two independent NF-κB activation routes directly: PPARγ transrepression (mechanism 1; generic NF-κB transrepression) and SphK1 inhibition (mechanism 4; specifically blocks TNF-α-driven SphK1→TRAF2→IKKβ). In patients where TNF-α is the dominant mast cell product driving NF-κB, EGCG's SphK1 inhibition may be clinically important. Dose: EGCG already in protocol (from green tea extract or EGCG caps); no dose change needed.

**NF-κB Suppression Updated to 13 Mechanisms**

SphK1→S1P→TRAF2→IKKβ is the 13th NF-κB mechanism. The new mechanism is specifically relevant when TNF-α is the dominant activating cytokine. Protocol agents addressing it:
- EGCG (SphK1 inhibition; mechanisms 1+4)
- Sulforaphane (Nrf2/CBP competition; run_027)
- Omega-3/PPAR-α (run_089; indirect TRAF2/NF-κB reduction via HIF-1α/succinate ↓)
- TNF-α upstream reduction (mast cell stabilization → less TNF-α → less SphK1 activation)

No new agents needed — existing protocol already addresses the SphK1 node via EGCG.

### T1DM: Glycemic/Lipid Management → Ceramide:S1P Rheostat

For T1DM patients, the 7th β cell death mechanism (glucolipotoxicity → ceramide:S1P shift) is METABOLICALLY actionable — independent of immune management:

**Priority interventions for T1DM ceramide:S1P management:**
1. Reduce palmitate exposure: reduced dietary saturated fat (palmitate C16:0 → SMase → ceramide → NLRP3 Signal 2; run_043)
2. Tight glycemic control: less glucolipotoxicity → less SMase activation → less ceramide
3. EGCG: SphK1 preservation → more S1P → pro-survival rheostat maintained
4. Omega-3 EPA/DHA: partial SMase inhibition; shifts LDL-C and FFA composition toward less palmitoyl ceramide production

Protocol note: For T1DM rosacea patients with elevated fasting triglycerides or high saturated fat intake + active rosacea + deteriorating β cell reserve → ceramide/SphK1 management directly relevant. HbA1c alone does not capture glucolipotoxicity peaks (postprandial lipemia); fasting TG + ApoB can serve as proxies.

### Mast Cell S1PR2 Amplification: Clinical Significance

For patients with persistent IgE-mediated mast cell activity (documented allergen sensitization, elevated specific IgE, seasonal rosacea flares coinciding with allergen seasons):

- S1PR2 amplification: S1P (elevated in inflammatory state) → lowers IgE degranulation threshold
- This means: even low-level allergen exposure in a high-S1P environment can trigger amplified mast cell response
- Protocol implication: in IgE-dominant patients, reducing the inflammatory S1P load (EGCG→SphK1↓) is an ADJUNCT to mast cell stabilization — it raises the degranulation threshold back toward baseline
- No new agents needed: EGCG + ketotifen (mast cell stabilizer) combination addresses both sides: S1PR2 threshold (via SphK1↓) and direct mast cell membrane stabilization

### S1PR1/FTY720: Not Recommending, But Understanding

FTY720 (fingolimod) is FDA-approved for MS but NOT recommended in this protocol — it requires specialist monitoring (cardiac, ophthalmologic, infection risk). The mechanism (autoreactive T cell sequestration via S1PR1) provides mechanistic context:

- Patients with T1DM + rosacea who are started on fingolimod for a concurrent MS indication → may also benefit via reduced autoreactive T cell islet infiltration + reduced skin-homing T cells
- If a T1DM rosacea patient has MS and begins fingolimod: flag for potential rosacea improvement monitoring (T cell trafficking reduction may reduce ETR/PPR activity as additional benefit)

This is the only clinical note for FTY720/S1PR1 — not a protocol recommendation.

*Protocol_integration.md Part 9bf — 2026-04-12 | S1P SphK1 S1PR ceramide EGCG 4th mechanism NF-κB 13 pathways β cell mast cell S1PR2 FTY720 T1DM | run_106*

---

## Part 9bg — Leukotrienes: 5-LOX/BLT1/CysLT1; Mast Cell Three-Layer Management; T1DM BLT1; Omega-3 EPA Dose Rationale (run_107)

### Mast Cell Three-Layer Management: Updated Framework

| Layer | Target | Agents | Mechanism |
|---|---|---|---|
| Initiation prevention | Mast cell degranulation threshold | Ketotifen 1mg BID, quercetin, cromolyn | Membrane stabilization; cAMP ↑ |
| Propagation prevention | CysLT1 on neighboring mast cells | **Montelukast 10mg QD** (prescription) | CysLT1 competitive antagonist |
| End-receptor blockade | H1 (histamine), EP4 (PGE2), BLT1 (LTB4) | Cetirizine; omega-3; quercetin | Receptor-level downstream blockade |

Montelukast is NOT currently in the standard protocol, but is recommended for patients who have:
- Concurrent asthma or allergic rhinitis (already indicated for those conditions)
- Rosacea + urticaria overlap (urticarial rosacea subtype)
- Inadequate response to initiation-prevention agents alone (ketotifen + quercetin sufficient for most; montelukast for refractory)
- CAUTION: FDA black-box warning for neuropsychiatric events; avoid in patients with depression, anxiety, or suicidal ideation history

### Omega-3 EPA Dose: BLT1 Rationale

The T1DM BLT1 mechanism adds a new quantitative target for EPA dosing:
- Competitive 5-LOX substrate effect: EPA:AA ratio in cell membranes determines LTB4 vs. LTB5 production
- To shift ratio meaningfully: EPA plasma level needs to be elevated; typically requires ≥1.5-2g EPA/day from supplementation
- Protocol current dose (run_033 context): EPA+DHA 2-3g/day total → at typical EPA:DHA = 1:1 → ~1-1.5g EPA/day
- For T1DM patients with active insulitis markers (rising anti-islet IgG, HbA1c deterioration): consider EPA-enriched formula (3:1 or higher EPA:DHA ratio) to maximize competitive 5-LOX substrate effect for BLT1 suppression

### T1DM Protocol Addition: BLT1/LTB4 Monitoring (Optional)

For T1DM rosacea patients with evidence of active autoimmunity (positive anti-GAD/IA-2 antibodies, C-peptide declining):
- Urinary LTE4 (spot urine LTE4/creatinine ratio): accessible biomarker of systemic CysLT production; normal <100 pg/mg creatinine
- If LTE4 elevated → CysLT production active → confirm omega-3 compliance + consider EPA dose increase
- Not standard of care but mechanistically informative for refractory T1DM autoimmunity management

*Protocol_integration.md Part 9bg — 2026-04-12 | Leukotrienes 5-LOX CysLT1 BLT1 mast cell montelukast omega-3 EPA T1DM islet homing urinary LTE4 | run_107*

---

### Part 9bh — LXA4/ATL/FPR2 Resolution Axis: Protocol Implications (run_108)

This run completes the arachidonic acid bifurcation map:
- **Pro-inflammatory arm** (runs 055, 107): COX-2 → PGE2; 5-LOX → LTB4/CysLTs
- **Pro-resolving arm** (run_108): 15-LOX-1 → LXA4 → FPR2 → Annexin A1

#### No New Agents Required — Mechanism Explains Existing Protocol Choices

The striking finding from run_108 is that the protocol's existing agents (aspirin, omega-3, vitamin D, EGCG) are ALREADY driving LXA4/ATL production. The mechanism was previously unexplained; run_108 fills it in:

1. **Low-dose aspirin (existing: run_055 context)**: aspirin-acetylated COX-2 + AA → ATL (15-epi-LXA4). The anti-inflammatory benefit of low-dose aspirin in rosacea is now mechanistically attributed to ATL production, not just COX-2 inhibition. Does NOT block EPA-derived AT-resolvins (aspirin-acetylated COX-2 still processes EPA).

2. **Omega-3 EPA/DHA (existing: run_020, run_033)**: EPA → AT-resolvins (established) + EPA competes 5-LOX → less LTB4 → more AA available for 15-LOX → more LXA4. Dual mechanism now explicit.

3. **Vitamin D / calcitriol (existing: run_012)**: VDR → 15-LOX ↑ → LXA4 ↑. Fourth calcitriol benefit. Vitamin D repletion targets (serum 25-OH-D ≥40-60 ng/mL) already in protocol; run_108 adds resolution-axis rationale.

4. **EGCG (existing: run_008 context)**: SphK1 inhibition (run_106) + Nrf2 (run_008) + NF-κB; M2 polarization promotion → 15-LOX ↑. Indirect LXA4 augmentation.

#### Aspirin Caution in Rosacea: ATL vs. COX-2 Trade-off

Low-dose aspirin (81mg) → substantial ATL production with minimal COX-2-mediated PGE2 suppression. Full-dose aspirin (325mg+) → greater COX-2 suppression but potentially more GI/platelet risk and may suppress PGI2 (endothelial-protective prostacyclin). Protocol recommendation: maintain low-dose aspirin (81mg/day) specifically for ATL benefit when tolerated; avoid COX-2-selective NSAIDs (celecoxib) which eliminate both PGE2 AND ATL.

#### Annexin A1: Marker for Steroid Weaning

For patients who have been using topical corticosteroids and need to taper (steroid rosacea prevention): the ANXA1 mechanism predicts that abrupt steroid cessation → ANXA1 withdrawal → rebound inflammation. Protocol strategy during taper:
- Begin low-dose aspirin + increase omega-3 dose 2 weeks BEFORE starting corticosteroid taper
- This pre-loads ATL/LXA4 → FPR2 → ANXA1 endogenous pathway to substitute for corticosteroid-driven ANXA1
- Taper can proceed with reduced rebound risk
- NOT standard of care; mechanistically plausible from run_108 but clinical validation lacking

#### Node A / T1DM: LXA4 Treg Induction

For T1DM patients in node A monitoring phase:
- LXA4 → FPR2 → TGF-β → Foxp3: moderate confidence (Levy 2001; Serhan 2014); not yet T1DM-validated
- Vitamin D repletion (4th benefit: VDR → 15-LOX → LXA4 → FPR2 → Treg) = compounding Treg benefit
- No new monitoring required; track VD levels as standard (already in T-index v4)

#### Mast Cell Management: Adding the Endogenous Brake

The mast cell management framework now has a fourth layer beyond stabilizer + montelukast + antihistamine:
1. Mast cell stabilizer (ketotifen/cromolyn): prevent initial IgE/MRGPRX2/ST2 degranulation
2. Montelukast (CysLT1 antagonist): prevent CysLT1-driven autocrine propagation
3. Antihistamine: block histamine H1R
4. **LXA4/ATL (via aspirin + omega-3 + VD)**: restore endogenous FPR2 → Gαi → degranulation ↓ brake

Layer 4 is the only layer that reinforces endogenous inhibition rather than pharmacologically blocking specific pathways. It works continuously as long as resolution mediator production is maintained by the protocol.

*Protocol_integration.md Part 9bh — 2026-04-12 | LXA4 ATL aspirin-triggered FPR2 Annexin A1 ANXA1 mast cell endogenous inhibitor VDR 15-LOX vitamin D calcitriol 4th benefit T1DM Node A Treg aspirin low-dose omega-3 synergy steroid rosacea taper | run_108*

---

### Part 9bi — NLRP6 Gut Mucus Axis: Protocol Implications for Refractory Dysbiosis (run_109)

#### The Refractory Dysbiosis Pattern

For rosacea patients who fail to maintain improvement after probiotic courses, the NLRP6/histamine feedback loop provides the explanation and the solution:

**Pattern:** Probiotic course → improvement during treatment → relapse 4-8 weeks after stopping
**Mechanism:** Proteobacteria histamine → NLRP6 inhibition → mucus ↓ → proteobacteria recolonize after probiotic pressure removed
**Fix:** Break the lock-in by simultaneously addressing NLRP6 inhibition (reduce histamine) AND supporting NLRP6 activation (taurine + fiber)

#### Protocol Addition: Refractory Gut Dysbiosis Protocol (add-on, not first-line)

For patients with:
- Documented gut dysbiosis (Node C elevated, I-FABP > 200 pg/mL)
- Prior probiotic course with transient response only
- Low-histamine diet not yet implemented

Add all of the following simultaneously (not sequentially):

**Step 1: Histamine reduction (NLRP6 disinhibition)**
- Low-histamine diet: eliminate aged cheeses, fermented foods, red wine, canned fish, vinegar for minimum 6 weeks
- DAO enzyme supplement: 1 capsule before meals (DiAmine Oxidase enzyme supplementation; degrades dietary histamine in gut lumen)
- H2 blocker (famotidine 10mg PRN): reduces histamine-producing bacteria burden indirectly; LOW evidence for gut bacterial suppression specifically
- NOTE: low-histamine diet ALSO reduces mast cell triggers (synergy with existing mast cell stabilization protocol)

**Step 2: NLRP6 agonism**
- Taurine 1.5g/day: mechanistically supported (Levy 2015 Cell); LOW CONFIDENCE for clinical dysbiosis reversal; safe at this dose
- Dietary fiber upgrade: transition from generic fiber to prebiotic fiber specifically:
  - Inulin/FOS (chicory root, Jerusalem artichoke, garlic): generates butyrate + propionate → NLRP6 agonism
  - Psyllium husk (5g twice daily): direct goblet cell stimulation independent of NLRP6
  - Minimize fructans (wheat, onion, garlic) only if FODMAP sensitivity confirmed
- Butyrate supplement (sodium butyrate 600mg/day OR tributyrin 300mg/day): additive to run_034 butyrate protocol; now has NLRP6 agonism as 4th mechanism (prior: tight junction, Treg, HDAC)

**Step 3: Sustained probiotics with different strain selection**
- Current protocol: L. reuteri (primary; run_016/054) + Akkermansia (run_026)
- Addition for refractory cases: Bifidobacterium longum (histamine non-producing) + Lactobacillus acidophilus (taurine conjugation support)
- AVOID: histamine-producing Lactobacillus strains (L. buchneri, L. hilgardii) — these would worsen NLRP6 inhibition

#### Monitoring: Node C + Urinary Histamine

For patients on refractory dysbiosis protocol:
- Node C (I-FABP) at 6 weeks: should decrease if NLRP6 lock-in breaking
- Optional: urinary histamine or plasma histamine at baseline vs. 6 weeks (not standard of care; mechanistically informative)
- Response criterion: I-FABP reduction >30% at 6 weeks = protocol effective; continue full combination
- Non-response: consider GI specialist referral for H. pylori eradication (M7 mountain amplification via NLRC4 mechanism) + comprehensive stool microbiome analysis

#### NLRC4: No New Protocol Element

NLRC4/flagellin pathway: reduces proteobacteria → reduces flagellin → reduces NLRC4 activation. The intervention (probiotic + fiber to reduce proteobacteria) is already in protocol. NLRC4 provides mechanistic explanation but not a new intervention.

#### T1DM: NLRP6 Agonism as Pre-Diagnosis Strategy

For T1DM-rosacea patients or rosacea patients with rising anti-islet antibodies (early autoimmunity):
- NLRP6 agonism protocol (taurine + prebiotic fiber) aims to reduce systemic LPS exposure → reduce islet NLRP3 Signal 1 priming
- This is UPSTREAM prevention, not islet-specific treatment
- Priority order: if anti-GAD or anti-IA-2 positive, escalate NLRP6 agonism protocol to high priority alongside Node A monitoring intensification

*Protocol_integration.md Part 9bi — 2026-04-12 | NLRP6 gut mucus histamine feedback loop refractory dysbiosis DAO enzyme taurine prebiotic fiber Bifidobacterium low-histamine diet Node C I-FABP monitoring T1DM upstream prevention | run_109*

---

### Part 9bj — Hepcidin / Iron Axis: Protocol Monitoring Updates and Clinical Implications (run_110)

#### Node B Update: Ferritin as Inflammation Proxy

Serum ferritin is now formalized as a Node B secondary monitoring marker:
- **Primary purpose:** proxy for IL-6-driven hepcidin activity and macrophage iron sequestration
- **Interpretation:**
  - Ferritin >200 ng/mL (women) / >300 ng/mL (men) + low-normal serum iron + normal hemoglobin = anemia of chronic inflammation pattern → active hepcidin elevation → active IL-6 → Node B inflammation suboptimally controlled
  - Do NOT treat with iron supplementation in this pattern
  - Treat the underlying IL-6 source (Node B protocol, NF-κB suppressors)
- **Frequency:** every 3 months alongside hsCRP + IL-6 + waist (existing Node B panel)
- **Exception:** ferritin can be acutely elevated in iron overload (hereditary hemochromatosis), infection, hemolysis, malignancy — exclude before attributing to chronic inflammation

#### T1DM Additions: Selenium + HFE Consideration

**Selenium adequacy (NEW):**
- Mechanism: selenium → selenocysteine → GPX4 (glutathione peroxidase 4) → phospholipid hydroperoxide reduction → ferroptosis protection in β cells
- Target: plasma selenium 120-150 µg/L (reference range 70-120 in many labs but this is a minimum; optimal for GPX4 activity is higher)
- Source: 2-3 Brazil nuts/day (150-200 µg selenium) OR selenium yeast 100-200 µg/day
- Caution: selenium toxicity at >400 µg/day; do not over-supplement; hair loss and garlic breath at excess levels
- This is a NEW protocol addition motivated by the β cell ferroptosis protection mechanism
- Priority: LOW-MODERATE (mechanistically supported; no T1DM selenium RCT for β cell protection specifically)

**HFE genotyping (optional, not routine):**
- For T1DM patients with persistently elevated ferritin (>400 ng/mL) despite inflammatory control: consider HFE C282Y/H63D genotyping
- HFE C282Y homozygous → hemochromatosis workup → phlebotomy may protect β cells from iron overload
- HFE heterozygous → modest iron loading; monitor serum ferritin; ensure selenium adequacy
- Not standard of care; reserve for refractory cases with unexplained ferritin elevation

#### ME/CFS Protocol: Iron Supplementation Guidance

For ME/CFS patients with the ferritin-high / serum-iron-low pattern:
1. **Do NOT start oral iron supplementation** — this feeds macrophage Fenton load and worsens inflammation
2. **Explain mechanism to patient**: the body is holding iron in macrophages (not truly deficient); supplementation will not help
3. **Target the driver**: reduce IL-6 via protocol (NF-κB suppression, gut barrier, Node B elements)
4. **If symptomatic anemia (Hgb <10 g/dL)**: refer to hematology for IV iron evaluation — but note IV iron can cause acute inflammatory flare in ME/CFS via Fenton; discuss risk/benefit
5. **Monitor ferritin as response marker**: successful protocol management → IL-6 ↓ → hepcidin ↓ → macrophage FPN1 restored → iron released → serum iron normalizes → ferritin ↓ toward normal range (may take 3-6 months)

#### Rosacea: Topical Lactoferrin (Optional, Low Evidence)

For patients with persistent telangiectatic/phymatous rosacea who have tried standard protocol without full response:
- Topical lactoferrin cream (if available): iron chelation in dermis → Fenton ↓ → local NLRP3 priming ↓
- Evidence level: 1 small RCT (n=30; Berardesca 2012); not standard of care; add only if mainstream therapies insufficient
- Mechanism: lactoferrin binds Fe³⁺ in skin microenvironment → reduces Fenton chemistry from microhemorrhage-derived iron in telangiectatic skin

*Protocol_integration.md Part 9bj — 2026-04-12 | Hepcidin iron ferritin Node B monitoring selenium GPX4 ferroptosis T1DM HFE ME/CFS iron supplementation failure oral iron macrophage Fenton rosacea lactoferrin | run_110*

---

### Part 9bk — Osteopontin: Diagnosing and Managing OPN-Mediated Treg Displacement (run_111)

#### Clinical Scenario: Normal Node A + Persistent Rosacea

This is the specific diagnostic scenario that run_111 addresses:
- Patient on protocol for ≥3 months
- Node A: Foxp3+ Tregs NORMAL (>8% CD4+) in blood
- Node B: hsCRP/IL-6 persistently elevated
- Rosacea: still active (papules, flushing, telangiectasia progression)

**Previous framework explanation:** inadequate. Tregs are present → should suppress → but don't → mechanism unclear.

**Run_111 explanation:** OPN from persistently elevated M1 macrophages → CD44 on Tregs → tissue Treg displacement. Blood Treg count is normal because Tregs are present in circulation; they are selectively prevented from functioning at the inflamed skin site.

#### Diagnostic Protocol Update

For the above clinical scenario:
1. **Confirm OPN hypothesis**: request plasma OPN (commercial ELISA; not widely available in standard panels but reference labs offer it). Elevated OPN (>40-50 ng/mL in context of normal Treg count + active rosacea) = OPN-Treg displacement pattern.
2. **Alternative**: if plasma OPN unavailable, ferritin elevated (run_110) + Node B elevated + normal Node A = combined inflammatory load suggestive of M1-driven OPN
3. **Exclude other Node A suppressors**: confirm EGCG and IDO1 pathway is adequate (run_091 HCQ context); if Node D (IFN-α) elevated → HCQ already indicated → HCQ also reduces M1 → OPN indirectly

#### Management: Intensify M1 Suppression

For the OPN-Treg displacement scenario:
1. **EGCG dose optimization**: ensure 400-600mg EGCG/day (OPN gene promoter has both NF-κB and AP-1 sites — EGCG's dual NF-κB + AP-1 suppression = maximal OPN suppression)
2. **Colchicine adherence**: 0.6mg twice daily if tolerated; most potent protocol NF-κB suppressor → OPN ↓
3. **Add or increase omega-3**: EPA ≥1.5g/day → M2 polarization → OPN from M2 is substantially lower than from M1
4. **Increase prebiotic fiber + butyrate**: M2 polarization via butyrate → OPN ↓
5. **DO NOT** add more Treg-stimulating agents (AKG/Vit C, extra calcitriol) as primary response — Tregs are present, not depleted; stimulating more Tregs does not fix Treg displacement

#### T1DM Integration: OPN as Disease Progression Marker

For T1DM-rosacea patients:
- Plasma OPN correlates with insulitis activity; rising OPN = worsening islet inflammation
- In patients with positive anti-GAD/IA-2 antibodies and rising OPN: likely active insulitis → intensify gut barrier protocol (NLRP6/run_109) + M1 suppression + BLT1 management (omega-3 EPA; run_107)
- OPN measurement is NOT standard of care for T1DM; use as optional escalation trigger in refractory cases

*Protocol_integration.md Part 9bk — 2026-04-12 | Osteopontin OPN SPP1 Node A Treg displacement normal Treg blood persistent rosacea OPN plasma marker M1 suppression EGCG colchicine omega-3 M2 polarization T1DM insulitis marker | run_111*

---

### Part 9bl — Framework Saturation Note (post-run_111 sweep)

**No protocol changes.** The post-run_111 gap sweep found no mechanism clearing the multi-disease threshold for a dedicated run_112. All remaining candidates assessed and killed or confirmed already covered.

**Protocol_integration final state:**
- All 111 mechanistic runs are integrated
- T-index v4: Nodes A-F + B12/Mg²⁺ + optional secondary markers (plasma OPN, ferritin) fully populated
- Protocol elements: probiotic/prebiotic arm, barrier arm, M1 suppression arm, Treg support arm, SPM/resolution arm, iron monitoring arm — all active
- Monitoring thresholds: Node A (Foxp3+/CD25+ Tregs ≥8% CD4+), Node B (CRP/TNF-α), Node C (TJ integrity via FBHM/lactulose), Node D (IFN-α proxies), Node E (Th17), Node F (cortisol/HPA); plus ferritin (iron-Fenton risk), optional OPN (M1-Treg displacement)

**Threshold for future protocol update:**
If a new run (>run_111) is executed per the saturation override criteria in THEWALL.md Phase 4 Extension 86, return here and append Part 9bm with the relevant protocol integration.

**FRAMEWORK STATUS: COMPLETE | 111 runs | 2026-04-12 | sigma method v7**

*Protocol_integration.md Part 9bl — 2026-04-12 | SATURATION NOTE | no protocol changes | framework complete | 111 runs integrated | T-index v4 final state | future run threshold documented | sigma method v7*

---

### Part 9bm — TXNIP: Glucose-Driven NLRP3 Amplifier — Honeymoon T1DM Protocol Guidance (run_112)

**TXNIP adds to existing protocol without new agents.** All therapeutic leverage comes from existing elements gaining new mechanistic justification:

#### Calcitriol — 5th Anti-Inflammatory Mechanism

VDR binds VDRE in the TXNIP gene promoter → TXNIP transcription ↓ → less free TXNIP → less NLRP3 Signal 2 in β cells and dermal macrophages. This is mechanistically additive to:
1. VDR → Foxp3+ Treg induction (run_018/056)
2. VDR → cathelicidin antimicrobial
3. VDR → NLRP3/PYCARD suppression (run_056)
4. VDR → 15-LOX → LXA4 (run_108)
5. **VDR → TXNIP ↓ (run_112)**

**Node E monitoring (25(OH)D3 ≥60 ng/mL) is now supported by five independent anti-inflammatory mechanisms.** For T1DM patients in particular: achieving and maintaining Node E target directly suppresses the glucose-driven β cell NLRP3 loop via TXNIP.

#### BHB — 2nd NLRP3 Suppression Mechanism

BHB inhibits ChREBP nuclear activity → TXNIP transcription ↓ → less NLRP3 Signal 2 from the glucose arm. This is additive to direct NLRP3 PYD binding (run_037). Protocol elements already supporting BHB:
- Moderate low-glycemic diet → reduced insulin spikes → mild endogenous ketosis
- Optional exogenous BHB supplement (2-3g/day; run_037 already documents)

**For T1DM patients during honeymoon: BHB supplementation provides dual TXNIP protection.**

#### EGCG and Sulforaphane — New TXNIP Suppression Arm

Nrf2 → thioredoxin (TRX) ↑ → more TRX available to sequester TXNIP → less free TXNIP → less NLRP3 Signal 2. This is an additional mechanism for existing EGCG/sulforaphane protocol elements.

#### NEW T1DM Honeymoon Protocol Guidance

This is the key clinical addition from run_112 — **not present in any prior run:**

> **T1DM Honeymoon Period (preserved C-peptide >0.2 nmol/L): Glucose-Specific Protocol**
>
> 1. **CGM target more aggressive than standard T1DM:** Time-above-range >180 mg/dL should approach zero. Every glucose excursion activates TXNIP → NLRP3 in residual β cells.
>
> 2. **Dietary glycemic index prioritized:** Avoid acute glucose spikes (simple carbohydrates) specifically because of TXNIP ChREBP activation. Low-GI diet prevents ChREBP→TXNIP surge even when total carbohydrates are moderate.
>
> 3. **BHB supplementation rationale strongest during honeymoon:** ChREBP inhibition + direct NLRP3 block = dual protection of residual β cells. Start during honeymoon, maintain through first 2 years.
>
> 4. **Node E priority in honeymoon:** VDR→TXNIP↓ makes achieving 25(OH)D3 ≥60 ng/mL even more critical during the period when β cell mass is partially preserved.
>
> 5. **Monitoring:** C-peptide at 3-month intervals during honeymoon (standard); C-peptide decline rate is the proxy for TXNIP-loop severity.

#### Rosacea: Loop 2 Therapeutic Implications

Three ROS→NLRP3 Signal 2 arms now identified for phymatous/high-oxidative-load rosacea:
- mtROS arm: SIRT3 (run_090) → target with NR/NMN
- Fenton arm: selenium/GPX4 + lactoferrin (run_110) → target iron load
- TXNIP arm: Nrf2/EGCG/sulforaphane → TRX ↑ + calcitriol → TXNIP ↓

For Loop 2 non-responders with phymatous or sebaceous-dominant subtype: assess all three arms. Protocol should include Nrf2 support (sulforaphane) as part of anti-Loop 2 strategy.

*Protocol_integration.md Part 9bm — 2026-04-12 | TXNIP ChREBP glucose-driven NLRP3 Signal 2 9th beta cell death T1DM honeymoon tight glucose control BHB dual mechanism calcitriol 5th benefit EGCG TRX Nrf2 rosacea Loop 2 third ROS arm 5th calcitriol anti-inflammatory mechanism | run_112*

---

### Part 9bn — A20/TNFAIP3: NF-κB Brake Failure, GWAS Stratification, and Continuous Protocol Rationale (run_113)

#### Background

Run_113 analyzes A20 (TNFAIP3), the primary NF-κB negative feedback protein. A20 is absent as a primary mechanism from all 112 prior runs. Its depletion under chronic inflammation explains:
1. Why rosacea progresses from ETR (episodic) to PPR (persistent) phenotype
2. Why T1DM insulitis accelerates over time despite unchanged immune trigger levels
3. Why continuous protocol outperforms pulsed/episodic protocol

#### New Monitoring: TNFAIP3 Genotyping

Add to **T-index v4 optional panel** (alongside HFE genotyping from run_110):

> **TNFAIP3 genotyping** (rs2327832, rs6920220):
> - Risk allele(s) present → A20 haploinsufficiency → impaired NF-κB self-termination → recommend aggressive continuous NF-κB suppression protocol from initial presentation
> - Interpretation: 0 risk alleles (low NF-κB brake impairment; standard protocol); 1 risk allele (moderate; prioritize HCQ + quercetin at full dose); 2 risk alleles (high; add colchicine + LDN early; close Node B monitoring)
> - One-time test; does not change with disease state

This is the second genetic stratification test after HFE C282Y/H63D (run_110). Together they identify:
- Iron-driven NLRP3 non-responders (HFE risk allele) → emphasize lactoferrin/selenium
- NF-κB brake-impaired non-responders (TNFAIP3 risk allele) → emphasize continuous NF-κB protocol

#### Continuous vs. Pulsed Protocol: Mechanistic Justification

A20's feedback dynamics explain why **continuous protocol is mechanistically superior** to episodic/pulsed use:

| Protocol type | A20 dynamics | NF-κB outcome |
|---|---|---|
| Continuous suppression | A20 demand reduced → A20 levels recover → internal brake restored | NF-κB sustained low; both external (protocol) + internal (A20) brakes active |
| Pulsed (flare-only) | During off-periods: chronic triggers → A20 consumed → baseline NF-κB rises | Each flare starts from higher NF-κB baseline; protocol effectiveness diminishes over disease course |
| Post-discontinuation | A20 had recovered → provides residual brake for weeks | Explains 2-6 week delayed relapse after stopping continuous protocol (not just pharmacokinetics) |

**Clinical implication:** Patients who report "the protocol worked but stopped working" may have experienced A20 depletion from a period of pulsed use that allowed NF-κB setpoint to shift. Reinstate continuous protocol; allow 4-8 weeks for A20 recovery.

#### Butyrate: Third Independent Mechanism

Butyrate (from run_032 rifaximin/prebiotic/probiotic protocol arm) now has three mechanistically distinct anti-inflammatory actions:
1. HDAC inhibition → histone acetylation → anti-inflammatory gene expression (run_032 primary)
2. NLRP3 direct suppression → reduces Loop 2 Signal 2 threshold (run_032)
3. **NEW — A20 recovery via TLR4 load reduction**: butyrate → improved gut barrier + restored gut microbiome → less LPS translocation → less chronic TLR4 activation → less A20 demand → A20 levels recover → NF-κB self-termination restored

This third mechanism is distinct: mechanisms 1 and 2 suppress inflammatory outputs; mechanism 3 reduces the input load that depletes A20.

#### Rosacea Clinical Insight: ETR → PPR Prevention

A20's depletion model predicts that rosacea phenotype progression is not inevitable — it is driven by sustained A20 consumption. Protocol implication:

> **Phenotype progression prevention:** Early continuous protocol initiation (at ETR stage, before PPR) preserves A20 levels by reducing chronic TLR4/KLK5 activation load → NF-κB cannot establish its chronic self-sustaining state. Late initiation (at PPR stage) may require more time to restore A20 levels because the NF-κB setpoint has already shifted upward.

This is a new argument for **early protocol initiation** in rosacea patients, even before significant disease burden.

#### T1DM: 10th β Cell Death Mechanism and Protocol Amplification

A20 haploinsufficiency (TNFAIP3 risk allele) in T1DM patients creates:
- Lower threshold for β cell apoptosis (TNF-α/IFN-γ-mediated; A20 protection reduced)
- Higher probability of β cell necroptosis (RIP1 not K48-ubiquitinated → necrosome forms → DAMP release → IL-33 + HMGB1 → insulitis amplification)

**For T1DM patients with TNFAIP3 risk allele:**
- Prioritize run_032 (butyrate) + run_112 (tight glucose control) → reduce both TLR4 load and TXNIP-driven activation simultaneously
- A20 haploinsufficiency + TXNIP glucose loop = double impairment of β cell self-protection; these patients have highest β cell loss rate and most benefit from combined NF-κB suppression + glycemic control

*Protocol_integration.md Part 9bn — 2026-04-12 | A20 TNFAIP3 NF-κB brake deubiquitinase TRAF6 RIP1 haploinsufficiency T1DM GWAS 6q23 TNFAIP3 genotyping monitoring HFE second genetic stratification 10th beta cell death RIP1 necroptosis continuous vs pulsed protocol A20 depletion positive feedback rosacea ETR PPR phenotype progression butyrate third mechanism | run_113*

---

### Part 9bo — GSK-3β/Foxp3 Protein Stability and Berberine (run_114)

#### Background: The Induction-Destruction Gap

The existing Node A support protocol (calcitriol/VDR → Foxp3 induction; AKG + Vitamin C → TET2 → TSDR demethylation) increases Foxp3 transcription and epigenetic stability. Run_114 identifies a parallel, protein-level mechanism that destroys Foxp3 after it's produced: GSK-3β (constitutively active in inflammatory conditions) phosphorylates Foxp3 Ser418 → STUB1 ubiquitinates it → proteasomal degradation. This "induction-destruction dissociation" explains Node A non-responders: good Foxp3 mRNA, good TSDR methylation, but Foxp3 protein is continuously degraded.

#### New Protocol Element: Berberine

> **Berberine** (OTC; isoquinoline alkaloid from Berberis vulgaris, Coptis chinensis, Phellodendron amurense)
> - **Dose:** 500 mg BID with meals (1000 mg/day); can increase to 500 mg TID (1500 mg/day) for T1DM glucose benefit
> - **Primary mechanism here:** GSK-3β inhibition → Foxp3 Ser418 NOT phosphorylated → Foxp3 protein stable → Treg function preserved
> - **When to add:** Node A non-responder after VDR/calcitriol (Node E ≥60 ng/mL) + TET2/AKG protocol are optimized
> - **Safety:** Does NOT deplete B12 (advantage over metformin; run_085). Monitor blood glucose in insulin-dependent T1DM (additive glucose-lowering with AMPK activation). No significant herb-drug interactions at 1000 mg/day.

#### Node A Non-Responder Algorithm (Updated)

```
Node A persistently low (<8% Foxp3+ CD4+) despite protocol:
    
    1. Check Node D (IFN-α2 Simoa) → if >0.05 fg/mL → HCQ [pre-existing]
    2. Check Node E (25(OH)D3) → if <60 ng/mL → calcitriol optimization [pre-existing]
    3. Check AKG/TET2 compliance → if inadequate → reinforce + Vitamin C [pre-existing]
    4. NEW: If 1-3 optimized but Node A still low → 
          Suspect: GSK-3β constitutively active (chronic TNF-α/IL-6 → PI3K/Akt impaired)
          Add: Berberine 500 mg BID
          Mechanism: berberine → GSK-3β inhibition → Foxp3 protein stabilized
          Monitor: Node A at 3 months post-berberine initiation
```

#### Synergy: Berberine + Calcitriol = Dual-Level Treg Support

- **Calcitriol** (existing): VDR → Foxp3 mRNA induction → more Foxp3 transcription
- **Berberine** (new): GSK-3β inhibition → Foxp3 protein stabilized → longer protein half-life

Together: calcitriol ensures more Foxp3 is made; berberine ensures more of what's made survives. This is the first **dual-level** Treg support combination in the protocol (transcriptional induction + protein stability).

#### T1DM-Specific: Berberine During Honeymoon

During the T1DM honeymoon period (C-peptide preserved), berberine provides three simultaneous benefits:
1. **GSK-3β → Foxp3 preservation in islet Tregs** → better immune tolerance of residual β cells
2. **GSK-3β → β cell MCL-1/BAD → anti-apoptotic** (11th β cell death mechanism prevented)
3. **AMPK activation → glucose lowering → less TXNIP activation** (run_112 rationale reinforced)

Berberine is thus the protocol element with the broadest T1DM honeymoon benefit: Treg function + direct β cell protection + metabolic glucose management in a single OTC compound.

**Interaction note:** Berberine + metformin (if used in T1DM management) → additive AMPK activation → enhanced glucose lowering → insulin dose may need reduction. Stagger timing (berberine with meals, metformin with other meals) to separate peaks.

#### Rosacea: Completing the ETR→PPR Prevention Protocol

Run_113 (A20) and run_114 (GSK-3β) together explain why rosacea progresses despite partial protocol response:
- A20 depletion → NF-κB brake fails → Loop 2 persistent
- GSK-3β → Foxp3 protein destroyed → Treg brake fails → Loop 2 uninhibited

Both run on the same platform: chronic inflammation → each brake progressively consumed/destroyed. The convergence point is that early continuous protocol (run_113 rationale) AND early berberine addition (run_114 rationale) prevent both brake failures from establishing, keeping rosacea in the reversible ETR phenotype.

*Protocol_integration.md Part 9bo — 2026-04-12 | GSK-3β Foxp3 protein stability STUB1 berberine OTC Node A non-responder 4th branch calcitriol+berberine dual-level Treg T1DM honeymoon triple benefit induction-destruction dissociation 11th beta cell death MCL-1 berberine+metformin interaction rosacea ETR PPR A20+GSK-3β convergence | run_114*

---

### Part 9bp — CARD9/CBM/Mycobiome: Caprylic Acid as New OTC Element (run_115)

#### New Protocol Element: Caprylic Acid / MCT Oil

**Mechanism:** Caprylic acid (C8:0) and capric acid (C10:0) in MCT oil disrupt fungal cell membranes (medium-chain fatty acids → membrane disorganization → osmotic lysis). Targets:
- **Gut Candida** (caprylic acid C8:0): reduces Dectin-1/CARD9 gut activation → less gut NF-κB/IL-17 → less intestinal permeability
- **Skin Malassezia** (capric acid C10:0, topical): toxic to Malassezia above C8 threshold (run_033 established); MCT oil applied topically reduces Malassezia load

**Dosing (oral):** MCT oil 1 teaspoon/day with food → increase to 3 teaspoons/day over 1–2 weeks as tolerated
- Titrate slowly: caprylic/capric acid can cause nausea, cramping, loose stool at initiation
- Therapeutic range: 5–15g MCT oil/day (each teaspoon ≈ 5g, containing ~3g C8:0 + ~1.5g C10:0)
- Food equivalents: coconut oil (~8% caprylic acid), but concentrated MCT oil provides therapeutic dose more reliably

**Patient selection:** Prioritize in:
1. T1DM with gut symptoms + high glycemic variability (Candida-prone due to glucose-rich gut lumen)
2. Rosacea with seborrheic dermatitis overlap (Malassezia-heavy phenotype)
3. ME/CFS with gut dysbiosis / self-reported yeast overgrowth
4. CARD9 rs4077515 normal allele (higher CARD9 responsiveness; test if genetic panel used)
5. Stool Candida culture positive or elevated Candida IgG serology

**Monitoring:**
- Stool Candida culture (Sabouraud agar) at baseline and 3 months for T1DM gut phenotype
- Candida IgG/IgA serology: estimates systemic fungal immune exposure (optional)
- CARD9 rs4077515 genotyping: 3rd genetic stratification point (add to optional panel alongside HFE, TNFAIP3)

#### Connection to Existing Protocol Elements

**Caprylic acid + butyrate (complementary antifungal mechanisms):**
- Butyrate: HDAC inhibition → Candida yeast-to-hypha suppression (butyrate 4th mechanism; run_115)
- Caprylic acid: direct membrane disruption → Candida cell death
- Different mechanisms → additive for gut Candida management; use together for maximal effect
- No interaction concern; timing flexible (can be with same meal)

**Caprylic acid + A20/run_113 upstream connection:**
- Fungal CARD9 activation → MALT1 protease → cleaves A20/TNFAIP3 (Staal 2011 Immunity)
- MCT oil reduces gut/skin fungal load → less CARD9 → less MALT1 → less A20 destruction
- Caprylic acid is therefore upstream support for the A20 preservation rationale of run_113
- In rosacea: Malassezia-heavy patients → both CARD9/MALT1-A20 cleavage AND chronic inflammation A20 depletion; MCT oil addresses the fungal arm

**Caprylic acid + berberine (run_114):**
- Berberine: some in vitro antifungal vs. Candida, but primary mechanism is GSK-3β inhibition
- Caprylic acid: primary mechanism is membrane disruption; more potent and specific for gut Candida
- Complementary; no interaction concern; together they address both the fungal load and the downstream signaling

#### 15th NF-κB Mechanism and Clinical Context

CARD9/CBM → TAK1 → IKKβ → NF-κB (fungal-specific C-type lectin arm) is the first non-TLR, non-cytokine NF-κB mechanism in the framework. Clinical significance:
- In patients with persistent rosacea flares despite full protocol (incl. berberine/run_114 + continuous protocol/run_113): consider adding MCT oil + antifungal skin management → may address the CARD9/Th17 input driving residual inflammation
- Malassezia-driven IL-17 cannot be suppressed by NF-κB inhibitors (berberine, calcitriol) without also addressing the Dectin-2 upstream trigger
- Th17/IL-17 → KLK5 amplification connects to Loop 1 (existing non-responder loop) — fungal axis adds a new Loop 1 feeding mechanism

#### T1DM Gut Mycobiome Protocol

In T1DM patients with gut-prominent phenotype (bloating, altered motility, high glycemic variability correlated with gut state):
1. **Screen**: stool Candida culture + Candida IgG
2. **If positive**: add MCT oil 1–3 tsp/day (titrate as above)
3. **Concurrent**: butyrate (existing protocol) → butyrate 4th mechanism (HDAC → Candida hypha suppression) additive with MCT oil direct kill
4. **Monitor**: repeat stool Candida culture at 3 months; glycemic variability tracking
5. **Rationale**: Candida → CARD9 → NF-κB + Th17 → gut permeability → antigen spillover → systemic immune activation → islet immune injury. Treating Candida reduces this cascade.

*Protocol_integration.md Part 9bp — 2026-04-12 | CARD9 CBM complex Dectin-2 Dectin-1 Malassezia Candida mycobiome caprylic acid MCT oil OTC new element gut antifungal CARD9 S12N rs4077515 stool Candida monitoring 3rd genetic stratification A20 MALT1 cleavage run_113 upstream 15th NF-κB butyrate 4th mechanism complementary | run_115*

---

### Part 9bq — ALOX12/12(S)-HETE: Baicalein as New OTC 12-LOX Inhibitor (run_116)

#### New Protocol Element: Baicalein / Chinese Skullcap (Scutellaria baicalensis)

**Mechanism:** Baicalein (active aglycone from Scutellaria baicalensis) chelates the catalytic iron of 12-LOX (ALOX12) → inhibits 12(S)-HETE production. In T1DM insulitis: cytokines (IL-1β/IFN-γ) → STAT1 → ALOX12 ↑ in β cells → 12-HETE → GSH depletion → caspase-3 → β cell death (12th mechanism). In rosacea: keratinocyte 12-HETE → BLT2 → neutrophil recruitment → Loop 2 amplification.

**Dose:** 500–1500 mg/day of standardized Scutellaria baicalensis root extract (containing 45-65% baicalin) with meals. Titrate from 500 mg; some patients feel mild sedation at initiation (due to other Scutellaria alkaloids — dose-dependent, usually resolves).

**Quality note:** Use reputable brands with tested baicalin content. Case reports of hepatotoxicity have been associated with adulterated or very high-dose products. Standard supplemental doses (up to 1500 mg/day baicalin) have a reasonable safety profile.

**Patient selection — when to add baicalein:**
1. **T1DM honeymoon period with active insulitis markers** (positive GAD/IA-2 antibodies, falling C-peptide): 12-LOX is cytokine-induced during active insulitis. Strongest T1DM rationale (Bleich 1995 evidence tier).
2. **Rosacea Loop 2 non-responder** with persistent neutrophil infiltration despite NLRP3/colchicine protocol: consider 12-HETE as a BLT2-mediated neutrophil chemoattraction contributing to Loop 2 persistence.
3. **ME/CFS with platelet activation** (elevated plasma 12-HETE, platelet microthrombi, post-exertional crash pattern consistent with platelet hyperactivation): baicalein → 12-HETE ↓ → anti-platelet aggregation effect.

#### LOX Protocol Map (Post-run_116 Complete)

| Run | LOX arm | Product | Intervention |
|-----|---------|---------|-------------|
| run_020 | Platelet/tissue 12-LOX + 15-LOX (DHA) | Maresins, AT-resolvins | Omega-3 EPA/DHA |
| run_107 | 5-LOX (ALOX5) | LTB4, CysLTs | Omega-3 EPA (LTB5) + montelukast |
| run_108 | 15-LOX-1 (ALOX15) | LXA4, ATL, LXB4 | Omega-3 + aspirin (ATL) |
| **run_116** | **ALOX12 (β cell/keratinocyte)** | **12(S)-HETE** | **Baicalein (Scutellaria)** |

All four LOX arms now covered with specific interventions.

#### T1DM Honeymoon: Triple β Cell Protection Layer (ALOX12 + run_112-114)

During the T1DM honeymoon (active insulitis, residual C-peptide):
- **TXNIP arm (run_112)**: Glucose → ChREBP → TXNIP → NLRP3 → β cell death #9 → BHB + calcitriol
- **A20/RIP1 arm (run_113)**: A20 depletion → RIP1 necroptosis → β cell death #10 → continuous protocol + butyrate
- **GSK-3β/MCL-1 arm (run_114)**: GSK-3β → MCL-1↓/BAD → apoptosis → β cell death #11 → berberine
- **ALOX12 arm (run_116)**: Cytokine → ALOX12 → 12-HETE → GSH depletion → caspase-3 → β cell death #12 → baicalein + omega-3 + sulforaphane

Each arm is mechanistically independent; combined protocol addresses four distinct β cell death pathways simultaneously during the honeymoon window.

#### Synergy Profile
- **Baicalein + omega-3**: additive — omega-3 reduces AA substrate; baicalein inhibits the enzyme; together reduce 12-HETE at two levels
- **Baicalein + sulforaphane**: complementary — sulforaphane → Nrf2 → GSH synthesis ↑ (GSH replenishment); baicalein prevents 12-HETE-mediated GSH depletion (upstream prevention). Together: prevent depletion AND replenish.
- **Baicalein + berberine**: complementary — different β cell death pathways; no interaction concern
- **Baicalein + colchicine**: different targets (12-LOX vs. microtubule/NLRP3); no interaction concern

*Protocol_integration.md Part 9bq — 2026-04-12 | ALOX12 12-LOX 12(S)-HETE baicalein Scutellaria baicalensis Chinese skullcap 12th beta cell death T1DM honeymoon rosacea Loop 2 neutrophil BLT2 LOX protocol map complete baicalein+omega-3 baicalein+sulforaphane triple beta cell protection | run_116*

---

### Part 9br — mPGES-1/EP3: AKBA/Boswellia as Targeted PGE2 Inhibitor (run_117)

#### New Protocol Element: AKBA / Boswellia serrata Extract

**Mechanism:** AKBA (acetyl-11-keto-β-boswellic acid) inhibits mPGES-1 → blocks PGE2 production from COX-2's PGH2 product. More specific than NSAIDs: PGI2 is preserved (PGH2 diverted to prostacyclin synthesis). Also inhibits IKKβ → NF-κB suppression (12th suppression pathway).

**Dose:** 300–500 mg of standardized Boswellia serrata extract (≥30% boswellic acids, ≥20% AKBA content), 2–3 times/day **with fatty meals** (fat increases boswellic acid absorption 2–3x; bioavailability is poor on empty stomach). Total 600–1500 mg/day.

**Patient selection — when to add AKBA:**
1. **T1DM honeymoon** (first priority): EP3-mediated GSIS impairment in surviving β cells; AKBA → mPGES-1 ↓ → less EP3 stimulation → partial restoration of insulin secretion from living β cells. Add with berberine + baicalein for multi-mechanism β cell support.
2. **Rosacea ETR with prominent flushing** (second priority): mPGES-1 inhibition → less PGE2/EP4 vasodilation; better tolerated than NSAIDs (PGI2 preserved). Consider if flushing non-responsive to existing protocol.
3. **Rosacea PPR** with persistent macrophage-driven Loop 2: AKBA → mPGES-1 + IKKβ/NF-κB dual blockade → additive with colchicine.
4. ME/CFS with neuroinflammation pattern: bonus tier — weak evidence but mechanistically plausible.

#### T1DM Honeymoon: New "Functional Recovery" Target

The EP3/GSIS mechanism introduces a new therapeutic goal for the honeymoon period: **restoring insulin secretion from surviving β cells** (not just preventing their death).

Current honeymoon protocol targets (death prevention):
- TXNIP (run_112): BHB + calcitriol
- A20/RIP1 (run_113): continuous protocol + butyrate  
- GSK-3β/MCL-1 (run_114): berberine
- ALOX12/12-HETE (run_116): baicalein

New honeymoon target (functional restoration):
- **mPGES-1/EP3 (run_117): AKBA** → surviving β cells secrete more insulin despite ongoing low-level insulitis

Monitoring correlate: C-peptide should be measured BEFORE and AFTER addition of AKBA to establish a functional baseline. If C-peptide improves with AKBA (without other protocol changes), this confirms EP3-mediated suppression was contributing.

#### Selectivity Advantage Over NSAIDs for Rosacea

| Intervention | PGE2 | PGI2 | TXA2 | Notes |
|-------------|------|------|------|-------|
| NSAIDs (COX-2 inh.) | ↓↓ | ↓↓ | ↓↓ | Blocks all prostanoids; renal/cardiac risk |
| Aspirin | ↓ | ↓ (irreversible COX-1) | ↓↓ | Also acetylated-COX-2 → ATL (run_108 benefit) |
| **AKBA (mPGES-1 inh.)** | **↓↓** | **→ (preserved/↑)** | **→ (preserved)** | **Selectively reduces PGE2 only** |

This selectivity means AKBA is the preferred OTC prostanoid intervention for rosacea — it reduces the flushing-driving PGE2/EP4 without compromising the vasculoprotective PGI2.

#### Synergy Profile
- **AKBA + colchicine**: NLRP3 ↓ (colchicine) + NF-κB/mPGES-1 ↓ (AKBA) = dual Loop 2 attenuation from different nodes
- **AKBA + omega-3**: omega-3 reduces AA (mPGES-1 substrate); AKBA inhibits mPGES-1 enzyme → two-tier PGE2 reduction
- **AKBA + baicalein (run_116)**: different eicosanoid arms (PGE2 vs. 12-HETE); together address two distinct inflammatory lipid mediators
- **AKBA + berberine (run_114)**: both benefit T1DM honeymoon via different mechanisms; additive β cell support

*Protocol_integration.md Part 9br — 2026-04-12 | mPGES-1 PTGES PGE2 EP3 PTGER3 beta cell GSIS functional impairment AKBA boswellic acid Boswellia serrata IKKβ NF-κB suppression rosacea EP4 vasodilation PGI2 T1DM honeymoon functional recovery C-peptide monitoring selectivity NSAIDs omega-3 colchicine baicalein berberine synergy | run_117*

---

### Part 9bs — IL-37/SIGIRR: Downstream IL-1 Family Brake + T-Index v5 (run_118)

#### IL-37 Mechanism vs. Existing NLRP3 Protocol

The current Loop 2 protocol (BHB, colchicine, AMPK) suppresses IL-1β/IL-18 PRODUCTION.
IL-37/SIGIRR suppresses IL-1 family RECEPTOR SIGNALING after cytokine release. These are
strictly complementary:

```
Stimulus (LPS, crystals, ATP, reactive oxygen species)
    ↓
NLRP3 activation → caspase-1 → IL-1β + IL-18 secreted
    |                               ↓
    | [BHB/colchicine block here]   IL-1R1/IL-18Rα → IRAK1 → NF-κB → iNOS → NO
    |                               ↑
    |               [IL-37/SIGIRR/TOLLIP block here]
    |                               ↑
    +--- Caspase-1 also cleaves pro-IL-37b → IL-37b → autoregulatory brake
```

Non-canonical IL-1β (caspase-4/5 arm, run_096) bypasses NLRP3 → bypasses BHB/colchicine →
still blocked downstream by SIGIRR → strongest argument for why IL-37 is non-redundant.

#### T-Index v5 — Serum IL-37 as New Monitoring Component

| Component | What it measures | Target |
|-----------|-----------------|--------|
| IL-37 (new) | IL-1 family anti-inflammatory brake capacity | >400 pg/mL |
| OPN/SPP1 (Node E) | Th1 activation / macrophage polarization | <50 ng/mL |
| Ferritin (optional) | Iron-NLRP3 axis | within normal |
| Existing nodes A-F | Various inflammatory + regulatory markers | per protocol |

**Serum IL-37 clinical interpretation:**
- <200 pg/mL + non-response to NLRP3 suppression protocol: diagnose IL-37 brake insufficiency
  phenotype → add aggressive VitD3 optimization + EGCG; recheck IL-37 at 8 weeks
- <200 pg/mL + adequate VitD3 (25-OHD3 >50 ng/mL): consider genetic IL-37 polymorphism
  (rs3811047 associated with reduced IL-37 expression in inflammatory conditions); no therapeutic
  change beyond confirming EGCG in protocol
- >400 pg/mL: brake adequate; serum IL-37 monitors maintained; no new action

#### VitD3 and EGCG Cross-Mechanism Insight

**Vitamin D3 (run_056 existing):**
- NEW mechanism identified: 1α,25(OH)2D3 → VDR → IL-37 gene promoter activation (VDRE
  element in IL-37 promoter confirmed by Mohamud 2015 Allergy) → IL-37 ↑ in macrophages
  and keratinocytes
- Clinical use: after achieving 25-OHD3 >50 ng/mL (8-12 weeks), serum IL-37 should rise
  if patient is VDR-responsive; IL-37 non-response despite adequate VitD3 → add EGCG

**EGCG/GTE (run_091 existing):**
- NEW mechanism identified: EGCG → partial NF-κB attenuation → de-represses IL-37 promoter
  (NF-κB at baseline SUPPRESSES IL-37; partial reduction → IL-37 de-repression)
- Dosing: existing protocol dose (GTE 400-800 mg/day) sufficient; no change
- Pharmacodynamic marker: serum IL-37 at 4 weeks post-EGCG addition

#### T1DM Honeymoon Integration

IL-37 adds to the honeymoon protocol — focused on prevention of ongoing β cell damage:

| Mechanism | Run | Action | β Cell Effect |
|-----------|-----|--------|---------------|
| TXNIP/NLRP3 | 112 | BHB + calcitriol | reduces NLRP3-driven death |
| A20/RIP1 | 113 | continuous protocol + butyrate | prevents necroptosis + A20 preservation |
| GSK-3β/MCL-1 | 114 | berberine | apoptosis resistance |
| ALOX12/12-HETE | 116 | baicalein | 12(S)-HETE-driven apoptosis ↓ |
| mPGES-1/EP3 | 117 | AKBA | functional GSIS restoration |
| **IL-37/SIGIRR** | **118** | **VitD3/EGCG → IL-37 ↑** | **iNOS/NO-driven death ↓** |

Six simultaneous β cell protection mechanisms now addressable in T1DM honeymoon context.

Serum IL-37 measurement added to honeymoon monitoring protocol:
- Baseline IL-37 at T1DM diagnosis
- After VitD3 + EGCG optimization (8 weeks): target >400 pg/mL
- Low IL-37 at diagnosis (especially <200) = poor honeymoon prognosis indicator

*Protocol_integration.md Part 9bs — 2026-04-12 | IL-37 SIGIRR TIR8 TOLLIP IRAK1 NF-κB downstream brake nuclear SMAD3 IL-37b beta cell protection iNOS NO VDR EGCG serum IL-37 T-index v5 monitoring rosacea Li 2018 T1DM Ye 2019 Bulau 2014 Mohamud 2015 honeymoon six-mechanism integration | run_118*
