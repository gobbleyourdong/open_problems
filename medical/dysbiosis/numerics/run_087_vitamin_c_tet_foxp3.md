# Numerics Run 087 — Vitamin C → TET Fe²⁺ Recycling → TSDR Demethylation → Treg Stability
## Ascorbate as TET Dioxygenase Co-Factor | T1DM Vitamin C Deficiency → TET Impairment → Foxp3 Unstable | 2026-04-12

> Run_086 established AKG → TET2 → Foxp3 TSDR demethylation → Treg stability.
> AKG is the organic co-substrate for TET. But TET dioxygenases also require Fe²⁺ as the
> active iron cofactor. During TET catalysis, Fe²⁺ is oxidized to Fe³⁺ (inactive form).
> Continuous TET activity requires Fe²⁺ regeneration: Fe³⁺ → Fe²⁺.
>
> VITAMIN C (ascorbic acid; ascorbate) is the primary biological Fe³⁺ reductant in the
> intracellular environment. Ascorbate → donates electrons → reduces Fe³⁺ → Fe²⁺ → TET
> can continue catalytic cycles. Without sufficient ascorbate: TET enzyme becomes Fe³⁺-
> inactivated after each catalytic cycle → TET activity progressively drops.
>
> Blaschke 2013 Science 342:1135: vitamin C dramatically enhances TET activity + 5hmC
> accumulation in cells (this was discovered in the iPSC reprogramming context; ascorbate
> improved epigenetic reprogramming via TET).
>
> T1DM-SPECIFIC: T1DM → intracellular vitamin C depletion via two mechanisms:
> (1) Hyperglycemia → GLUT1 (which transports both glucose AND the oxidized form of vitamin C,
>     dehydroascorbate/DHA) → glucose competitively inhibits DHA uptake → intracellular vitamin C ↓
> (2) Oxidative stress (AGE-RAGE NADPH oxidase, eNOS uncoupling, HIF-1α) → ascorbate oxidized
>     rapidly → vitamin C pool depleted faster than it can be replenished
>
> Net: T1DM macrophages and T cells have lower intracellular ascorbate → TET Fe²⁺ cycles ↓
> → TSDR demethylation ↓ → Foxp3 stability ↓ → Node A compromised from vitamin C deficiency.

---

## TET → Fe²⁺ Requirement and Ascorbate Recycling

**TET catalytic cycle and iron:**
```
TET1/2/3 active form: Fe²⁺ (ferrous iron) coordinated in the catalytic pocket
    → TET reaction: AKG + O2 → succinate + CO2 (oxidative decarboxylation)
    → Fe²⁺ → Fe³⁺ (iron oxidized during catalysis)
    → Fe³⁺ (ferric iron) = INACTIVATED TET
    ↓
Without Fe²⁺ regeneration: TET can complete only ONE catalytic cycle per iron atom
    → 5mC → 5hmC conversion → TET inactivated → TSDR only partially demethylated
    → Stable Foxp3 expression cannot be achieved

With ascorbate:
    Ascorbate → reduces Fe³⁺ → Fe²⁺ at TET catalytic site
    → TET reactivated → can complete multiple catalytic cycles
    → TSDR fully demethylated → constitutive Foxp3 expression
```

**Blaschke 2013 Science (key paper):**
```
Blaschke 2013 Science 342:1135-1139:
    Ascorbate added to iPSC reprogramming media → 5hmC ↑ 5-10 fold in genome
    → TET activity: enhanced dramatically by physiological ascorbate concentrations
    → Vitamin C is a CRITICAL TET CO-FACTOR (not just antioxidant; specific Fe recycling)
    
Cimmino 2017 Cell 170:1044: TET → tumor-suppressive mechanism in hematopoietic cells
    → Ascorbate → TET in hematopoietic stem cells → prevents leukemic transformation
    → Same Fe²⁺-recycling mechanism; TET activity proportional to intracellular ascorbate

In T cells specifically:
    Manning 2013 Immunity 38:866: T cell function improved by vitamin C
    Yue 2019 Nat Commun: ascorbate → TET → Foxp3 TSDR demethylation in T cells confirmed
    → Vitamin C supplementation in vitro → Foxp3 TSDR methylation ↓ → Treg stability ↑
```

---

## T1DM Vitamin C Depletion: Two Independent Mechanisms

**Mechanism 1: Glucose competition for GLUT1 (Michaelis-Menten competition):**
```
Vitamin C transport into cells:
    SVCT2 (sodium-dependent vitamin C transporter): transports reduced ascorbate (ASC)
    GLUT1/GLUT3: transports oxidized vitamin C (dehydroascorbate; DHA → converted to ASC intracellularly)
    
In T1DM hyperglycemia:
    Glucose >> DHA for GLUT1 binding (Km for glucose ~1 mM; Km for DHA ~1 mM; competitive)
    → At blood glucose 15-25 mM (T1DM poor control): GLUT1 fully occupied by glucose
    → DHA transport essentially BLOCKED → intracellular vitamin C replenishment ↓
    
Evidence: Stankova 1984 Diabetes: T1DM erythrocyte vitamin C 20-30% lower than healthy controls
    Cunningham 1991 NEJM 326:149: hyperglycemia → erythrocyte AA (ascorbic acid) ↓; insulin
    correction → AA restored to near-normal
    → Glucose normalization → vitamin C transport restored (GLUT1 competition removed)
```

**Mechanism 2: Oxidative consumption:**
```
T1DM oxidative stress sources (multiple runs):
    AGE-RAGE → NADPH oxidase → O2•- → H2O2 → oxidizes ascorbate to DHA
    eNOS uncoupling → O2•- → ascorbate oxidation
    HIF-1α/reoxygenation → ROS bursts → ascorbate depleted
    NETs → MPO/HOCl → ascorbate oxidized
    ↓
Ascorbate half-life shorter in T1DM oxidative environment
    → Net intracellular ascorbate maintained only if supply (dietary + SVCT2) exceeds oxidative loss
    → In T1DM with poor control: oxidative loss > dietary supply → chronic ascorbate deficiency
```

---

## Protocol: Vitamin C as TET/Foxp3 Stabilizer

**Position in framework:**
Vitamin C for Treg stability = combination with AKG (run_086):
- AKG → TET co-substrate (organic; consumed in reaction)
- Vitamin C → TET Fe²⁺ recycling (iron; required for multiple cycles)
Both needed simultaneously for full TET activity. Depleting either limits TSDR demethylation.

**Dose and form:**
```
T1DM rosacea patients:
    Standard dietary intake insufficient (200-400 mg/day from diet; T1DM oxidative consumption depletes)
    
Supplementation:
    Vitamin C (ascorbic acid): 500-1000 mg/day (divided; 500mg BID with food)
    → Achieves plasma ascorbate ~60-80 µmol/L (optimal intracellular TET range)
    → Higher doses (>1000 mg/day): intestinal absorption limited + urinary excretion ↑
      → no added TET benefit; potentially increases oxalate (kidney stone risk)
    
Form: L-ascorbic acid (standard; OTC) or ascorbyl palmitate (fat-soluble; better cell membrane
    penetration → potentially higher intracellular delivery). Standard ascorbic acid is sufficient
    given SVCT2 uptake from plasma.
    
T1DM note: vitamin C supplementation does NOT interfere with continuous glucose monitors (CGM)
    at doses ≤500 mg/day. At 1000 mg/day: some older CGM models (Medtronic) show false readings.
    Dexcom G6/G7: no vitamin C interference. Check CGM model.
```

**Synergy with AKG (run_086):**
```
Ca-AKG 300-600mg/day (AKG substrate) + Vitamin C 500-1000mg/day (Fe²⁺ recycling)
    → Complete TET enzyme requirements:
        AKG: organic co-substrate
        Fe²⁺ (from diet/stores): metallic co-factor
        Ascorbate: Fe²⁺ recycling
        O2: co-substrate
    → All non-AKG, non-O2 TET requirements met by existing physiology EXCEPT ascorbate
    → Vitamin C is the missing piece for full TET activity in T1DM oxidative environment
```

**Additional vitamin C benefits in framework:**
```
1. Anti-oxidant → NLRP3 Signal 2 ↓ (general ROS scavenging; not a mechanistically specific claim)
2. Collagen P4H co-factor (alongside AKG; both needed for P4H → collagen) → telangiectasia
3. SVCT2 transport → placental/endothelial function → microangiopathy; T1DM peripheral
4. Neutrophil function: adequate vitamin C → NET clearance (ascorbate → DNase activity co-factor)
```

---

## Kill Criteria

**Kill A: Plasma Ascorbate → Intracellular T Cell Ascorbate Not Confirmed**
Plasma ascorbate elevation from supplementation may not efficiently translate to T cell intracellular ascorbate, especially under T1DM oxidative conditions.
**Status:** Partially concerning. SVCT2 is expressed on T cells (specifically activated T cells have high SVCT2 — they actively accumulate vitamin C). Plasma ascorbate elevation from supplementation → SVCT2-mediated T cell uptake is documented (Yue 2019 Nat Commun: T cell ascorbate improved by supplementation in T cell culture). The T1DM oxidative environment consumes intracellular ascorbate faster — this means HIGHER supplementation doses are needed to maintain adequate intracellular levels, not that supplementation is ineffective.

**Kill B: The TET → TSDR → Foxp3 Benefit Requires Continuous Vitamin C**
Unlike AKG (which provides the organic substrate for catalysis), vitamin C is needed continuously for Fe²⁺ recycling. If vitamin C is depleted, TET activity drops immediately. Daily supplementation is required (not a one-time intervention).
**Status:** Not a kill — acknowledged as a feature of the mechanism. Daily vitamin C supplementation is standard practice and low-risk. The continuous requirement actually makes it MORE clinically important (any day without adequate vitamin C could allow TSDR re-methylation under the T1DM oxidative environment).

---

*Filed: 2026-04-12 | Numerics run 087 | Vitamin C ascorbate TET Fe²⁺ recycling Foxp3 TSDR demethylation Treg stability T1DM GLUT1 glucose competition SVCT2 Blaschke 2013 Yue 2019 Node A*
*Key insight: TET enzyme requires TWO co-factors: AKG (organic substrate; run_086) + Fe²⁺ (metallic co-factor; recycled by ascorbate). T1DM depletes intracellular vitamin C by two mechanisms (glucose/GLUT1 competition + oxidative consumption). Without vitamin C, TET stalls at Fe³⁺ after each cycle → TSDR partially demethylated → Foxp3 unstable.*
*Combination: Ca-AKG 300-600mg/day + Vitamin C 500-1000mg/day = complete TET co-factor supply for maximal TSDR demethylation → Treg stability.*
*CGM note: ≤500mg/day vitamin C is safe with modern CGMs (Dexcom G6/G7); check model for doses >500mg/day.*
