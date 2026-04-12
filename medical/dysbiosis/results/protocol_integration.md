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
