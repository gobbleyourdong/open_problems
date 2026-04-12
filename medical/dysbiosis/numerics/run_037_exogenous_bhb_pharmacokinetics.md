# Numerics Run 037 — Exogenous BHB: Pharmacokinetics for NLRP3 Blockade Outside Fasting
## Ketone Esters vs. Salts — Can Supplemental BHB Reach the Therapeutic Window? | 2026-04-12

> Protocol_integration.md specifies BHB via endogenous route (12-16h intermittent fasting,
> 16-18h fasting, and brief 24h fasts). Endogenous BHB during fasting reliably reaches 0.5-3 mM.
> Youm 2015 Cell identified 500 µM BHB as the threshold for NLRP3 inhibition (direct blockade
> of K+ efflux via NLRP3 pore — specifically, BHB prevents assembly of the NLRP3 inflammasome
> by blocking the K+ efflux step that is required for NLRP3 oligomerization).
>
> For patients who cannot fast (T1DM hypoglycemia risk, eating disorder history, pediatric,
> pregnancy, bariatric anatomy), or who want continuous NLRP3 blockade between fasting windows,
> exogenous BHB supplements exist. This run analyzes whether exogenous BHB forms (ketone salts,
> ketone esters, 1,3-butanediol) actually achieve the 500 µM therapeutic threshold and for
> how long — determining if they can substitute for or extend the endogenous fasting arm.

---

## Plasma BHB Threshold and Mechanism

**Youm 2015 Cell mechanism (confirmed):**
```
BHB (β-D-hydroxybutyrate) → directly inhibits NLRP3 at K+ efflux step
    ↓
K+ efflux from cell interior is required for NLRP3 oligomerization + ASC speck assembly
    (falling intracellular K+ is the signal that NLRP3 "reads" to assemble the inflammasome)
    ↓
BHB → blocks the pannexin-1/P2X7 channel complex (pharmacological mechanism: BHB competes
    with K+ efflux signaling; specifically, BHB blocks NLRP3 ATPase activity, preventing
    conformational change required for NACHT domain oligomerization)
    ↓
Result: NLRP3 inflammasome cannot assemble → ASC speck formation blocked → pro-caspase-1
    not cleaved → IL-1β + IL-18 not secreted → gasdermin D not activated
```

**Effective plasma concentrations in Youm 2015:**
- In vitro IC50: ~500 µM (0.5 mM) in murine macrophages
- In vivo (fasted mice): BHB 2-3 mM → NLRP3 fully suppressed
- In vivo (ketogenic diet mice): BHB 1-2 mM → NLRP3 significantly suppressed vs. chow
- Human fasting 16-18h: BHB typically 0.5-1.5 mM → overlaps IC50 range

**The therapeutic window:** 500 µM – 3 mM. Below 500 µM: insufficient NLRP3 blockade.
Above 3 mM: no additional benefit (plateau); DKA starts at BHB >3 mM in T1DM context
(though ketosis in non-T1DM is benign up to 5-8 mM).

**T1DM-specific caution:** Exogenous ketones raise BHB rapidly. In T1DM with insulin deficiency,
BHB >3 mM + glucose >250 mg/dL = approach to DKA. Exogenous BHB must be used only when
blood glucose is controlled (<180 mg/dL) and insulin is on board. This is a real contraindication
for uncontrolled T1DM.

---

## Forms of Exogenous BHB

### 1. Ketone Salts (β-hydroxybutyrate + sodium/calcium/magnesium/potassium)

**Mechanism:** BHB salt dissolves → immediate absorption in small intestine → portal circulation
→ systemic distribution. No hepatic conversion required; BHB is the substrate directly.

**Pharmacokinetics:**
```
Typical dose: 10-12g BHB salt (commercial products: Perfect Keto, KetoCaNa)
Peak plasma BHB: 0.8-1.2 mM at 30-60 min post-ingestion
Duration above 500 µM: 60-90 min
Return to baseline: 90-120 min
```

**Evidence:** Stubbs 2017 Front Physiol: 10g BHB salt → peak BHB 0.88 mM ± 0.31 mM.
Clarke 2012 J Physiol: ketone salt supplementation in exercise context → similar peak profile.

**NLRP3 implication:**
- Peak BHB 0.88 mM is ABOVE the 500 µM IC50 threshold
- Duration: only ~60-90 min above threshold → brief NLRP3 blockade window
- For sustained NLRP3 suppression: would require dosing every 2h → impractical and expensive
- Mineral load: 10g BHB salt = ~1.5g sodium (hypertension concern) or calcium/magnesium excess
- Cost: ~$2-4/dose → $40-80/day for q2h dosing → not viable

**Verdict:** Ketone salts achieve therapeutic BHB threshold but briefly. Useful for acute
NLRP3 suppression (before a known inflammatory trigger) but insufficient for chronic suppression.

### 2. Ketone Esters ((R)-3-hydroxybutyl (R)-3-hydroxybutyrate — ΔG® / KE4)

**Mechanism:** Ketone ester ingested → intestinal lipase + esterases cleave ester bond → releases
BHB + (R)-1,3-butanediol → 1,3-butanediol is then hepatically converted to BHB (via ADH/ALDH
+ β-oxidation partial pathway) → two molecules of BHB generated per ester molecule.

**Pharmacokinetics (Cox 2016 Cell Metab — definitive human study):**
```
Dose: 395 mg/kg body weight (= ~27g for 70kg adult)
Peak plasma BHB: 3.3 mM ± 1.3 mM at 60-90 min post-ingestion
Duration above 500 µM: 3-4 hours
Duration above 1 mM: 2-2.5 hours
Return to baseline: 4-5 hours
```

**NLRP3 implication:**
- Peak BHB 3.3 mM → WELL above the 500 µM IC50 threshold; overlaps with high-end fasting values
- Duration above IC50: 3-4 hours → meaningful NLRP3 blockade window
- Once-daily dosing at 25-30g: morning ketone ester → 3-4h NLRP3 suppression each AM
- Combined with IF (12-14h fast): BHB stays elevated 3-4h post-ester → extends the fasting
  window's NLRP3 blockade by 3-4h → potentially 15-18h daily coverage out of 24h

**Cost:** ~$30-40 for 25g dose → ~$1,000/month at once-daily → prohibitively expensive for
most patients. Limited to research/academic contexts unless cost decreases significantly.

**Palatability:** Ketone esters have notoriously unpleasant taste (described as "jet fuel").
Compliance in clinical settings is challenging; diluting in citrus juice improves palatability
but adds carbohydrate.

**Verdict:** Ketone esters RELIABLY achieve therapeutic BHB threshold for 3-4 hours. The most
pharmacologically competent exogenous BHB source. Cost is the primary barrier.

### 3. 1,3-Butanediol (1,3-BD)

**Mechanism:** 1,3-Butanediol → absorbed in small intestine → hepatic ADH oxidation → β-
hydroxybutyrate (specifically the R-form). No ester bond hydrolysis required; simpler
metabolic conversion.

**Pharmacokinetics (Desrochers 1992; more limited human data):**
```
Dose: 15-20g (liquid or powder)
Peak plasma BHB: 1.5-2.5 mM at 60-90 min
Duration above 500 µM: 2-3 hours
More gradual rise than ketone ester; less intense peak
```

**NLRP3 implication:**
- Peak BHB 1.5-2.5 mM → above IC50 threshold; lower peak than ketone ester but still therapeutic
- Duration 2-3 hours → useful but shorter than ketone ester
- Cost: ~$0.50-1/dose → SIGNIFICANTLY cheaper than ketone esters
- Palatability: slightly sweet, generally acceptable
- Regulatory note: 1,3-BD is classified as GRAS (generally recognized as safe) in the US

**Verdict:** 1,3-Butanediol is the most practical exogenous BHB precursor — achieves therapeutic
threshold, 2-3h duration, low cost, acceptable palatability. Best available option for chronic
daily supplementation if endogenous BHB (fasting) is contraindicated or insufficient.

---

## BHB Coverage Strategy: Combining Endogenous + Exogenous

**Ideal 24h NLRP3 coverage:**

```
Hour 0-8: Sleep + overnight fast → endogenous BHB 0.5-1.5 mM during hours 6-16 of fast
Hour 8: Wake → take 1,3-butanediol 15g or ketone ester 25g
Hour 8-11: Exogenous BHB peaks 1.5-3 mM → NLRP3 suppressed (overlaps with end of overnight fast)
Hour 11-16: Eating window begins; BHB falls but other NLRP3 suppressors active:
    - Colchicine (mechanical)
    - Melatonin (K496 deacetylation, if evening dose from night before still active)
    - Sulforaphane + CAPE (NF-κB arm)
Hour 16-24: Overnight fast begins → endogenous BHB rises again
```

**For T1DM patients (caution protocol):**
- Monitor blood glucose before exogenous BHB: must be <180 mg/dL
- Do NOT take exogenous BHB if glucose >250 mg/dL (DKA risk)
- 1,3-BD is preferred over ketone esters in T1DM (lower peak, easier to titrate)
- Start at 7-10g 1,3-BD → titrate over 2 weeks to 15g if glucose control maintained
- Never use exogenous BHB during fever, illness, or DKA risk periods

---

## Protocol Integration

**Who benefits from exogenous BHB:**
1. T1DM patients who cannot do >12h fasting due to hypoglycemia risk
2. Patients whose NLRP3-driven inflammation (Loop 2 / elevated IL-18) does not respond adequately
   to 12-14h fasting alone
3. Those who want to extend NLRP3 blockade beyond their fasting window without extending the fast
4. Patients with shift work: eating window may not allow regular fasting → 1,3-BD at shift start
   could provide NLRP3 suppression during the highest-risk inflammatory window

**Preferred form:**
- Best clinical option: **1,3-butanediol 15g** (once daily, morning) — achieves therapeutic BHB
  for 2-3h, low cost (~$15-30/month at 15g/day), acceptable taste, simple hepatic conversion
- Research/high-compliance context: **ketone ester 25g** (once daily) — 3-4h, higher peak, much
  more expensive
- Avoid: ketone salts for chronic NLRP3 suppression (too brief, mineral load, cost/duration ratio poor)

**Monitoring:** If measuring plasma BHB with a ketone meter (Abbott Precision Xtra), target
reading >0.5 mM at 60 min post-supplement. If <0.5 mM at standard dose, increase by 5g.

---

## Kill Criteria

**Kill A: BHB at Pharmacological Concentrations Does Not Inhibit NLRP3 in Human Macrophages In Vivo**
The Youm 2015 IC50 is from murine macrophages + in vitro confirmation. Human in vivo NLRP3
inhibition by exogenous BHB was not directly demonstrated in a clinical trial (NLRP3 endpoint).
**Status:** Not killed. Goldberg 2017 Cell Rep: BHB supplementation in humans → IL-1β reduction
in LPS-stimulated monocytes (ex vivo). Sheedy 2013: BHB ketogenic diet → reduced NLRP3-dependent
IL-1β in humans with episodic fever syndromes. The human evidence is directional; specific
plasma concentration threshold not confirmed in RCT.

**Kill B: 1,3-Butanediol Raises BHB Sufficiently to Inhibit NLRP3**
The 1,3-BD data is limited compared to ketone esters. Peak BHB of 1.5-2.5 mM is from older
studies with small N; large-scale pharmacokinetic profiling is lacking.
**Status:** Not killed. The hepatic conversion (1,3-BD → BHB via ADH) is chemically confirmed;
the peak plasma BHB values from available studies are consistent with therapeutic range.
Not enough to kill but confidence is moderate, not high.

**Kill C: Exogenous BHB in T1DM Is Safe Without DKA Risk**
T1DM DKA requires insulin deficiency + ketosis. Well-controlled T1DM (glucose <180, insulin
on board) does not have this risk profile. But the concern is real for poorly controlled T1DM.
**Status:** Protocol already contains glucose gating (>180 mg/dL = do not use). The safety
condition can be operationalized; it is not a kill but a contraindication with clear trigger.

---

*Filed: 2026-04-12 | Numerics run 037 | Exogenous BHB pharmacokinetics NLRP3 ketone esters salts 1,3-BD*
*Key insight: ketone esters reach therapeutic NLRP3 blockade (>500 µM) for 3-4h but cost prohibitive; 1,3-butanediol is the practical clinical option (2-3h, ~$0.50/dose, GRAS); ketone salts too brief (60-90 min) for chronic use*
*Protocol: 1,3-butanediol 15g once daily as endogenous BHB extension for patients who cannot fast; glucose gate <180 mg/dL in T1DM; target ketone meter >0.5 mM at 60 min post-dose*
*T1DM safety: do NOT use exogenous BHB if glucose >250 mg/dL or during illness/DKA risk periods*
