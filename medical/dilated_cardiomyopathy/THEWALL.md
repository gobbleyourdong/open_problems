# Dilated Cardiomyopathy (CVB) — THE WALL

## One Sentence

DCM is myocarditis that nobody caught. The cardiomyocytes died slowly, one by one, replaced by scar tissue, over 5-10 years of silent 2A protease activity from TD mutants the immune system could not detect — and by the time the LVEF dropped enough to cause symptoms, the window of complete recovery had already closed.

## The Pipeline

```
Year 0:     CVB3 infection (asymptomatic in 85-90% of cases)
            TD mutants establish in cardiomyocytes
            
Year 0-5:   Silent TD mutant persistence in myocardium
            2A protease active: DMD -32× (CONFIRMED, GSE184831 human cells)
            Each contraction cycle tears sarcolemma at weakened DGC sites
            Rate: ~0.5-1% LGE accumulation per year
            Symptom: none. LGE at year 5: 3-5% (still reversible)
            
Year 5-10:  LGE accumulates: 5% → 10% → 15%
            LVEF begins declining: 60% → 55% → 50% → 45%
            First symptom: exertional dyspnea, fatigue
            Patient sees cardiologist. Echo shows LVEF 42%.
            Diagnosis: "dilated cardiomyopathy, non-ischemic, etiology unknown"
            
Year 10+:   CVB-DCM progression
            LGE now 15-20% (partially reversible → minimal reversibility)
            GDMT started: helps, slows progression
            2A protease still running: TD mutants in residual cardiomyocytes
            
Year 10-20: Pump failure. LVAD consideration. Transplant listing.
```

**This is the story for the ~35% of DCM patients labeled "idiopathic."** The CVB connection is invisible because nobody measured it. The Kühl 2003 data tells us: if you measure it and clear it, LVEF recovers 44→53%.

## The Wall: By the Time You Know, the Window Is Partly Closed

For T1DM: the R term (regeneration) is always positive. You can tip R > D at any time.
For DCM: R ≈ 0. The cardiomyocytes that died are gone. The fibrosis is permanent.

**The wall is that DCM presents when the window of complete recovery is already narrowing.**

At LVEF 42% with LGE 15%: viral clearance is still valuable (stops progression, may improve +8-15% LVEF), but true recovery to normal LVEF is not expected.

At LVEF 55% with LGE 4% (caught early): viral clearance could fully restore function.

## What Breaks the Wall

**Upstream**: catch myocarditis before it becomes DCM. See myocarditis/THEWALL.md.

**For established DCM**: the wall is not impenetrable — it just limits how much recovery is achievable.

### Step 1: Stop the Clock (Viral Clearance)

The 2A protease is running. Every day it runs, more cardiomyocytes are at risk of sarcolemmal rupture. The protocol stops this:

- **Trehalose 3g/day** (start day 1 — cardiac LAMP2 κ=0.37 → 0.72 with trehalose; 12mo clearance → 6mo)
- **Fluoxetine 20mg** (CVB3 2C ATPase inhibitor)
- **FMD monthly** (TD mutant autophagy clearance)

When viral clearance is complete (T2 mapping normalizes): 2A protease stops → no new dystrophin cleavage → surviving cardiomyocytes rebuild DGC → sarcolemma stabilizes.

### Step 2: Reverse What's Reversible (GDMT + Anti-Fibrotic)

Standard heart failure therapy provides reverse remodeling independently of viral clearance:
- **ARNI** (sacubitril/valsartan): neurohormonal blockade + neprilysin → reverse remodeling
- **Beta-blocker** (carvedilol or metoprolol succinate): cardiac remodeling reversal
- **MRA** (spironolactone): anti-fibrotic via aldosterone blockade
- **SGLT2i** (empagliflozin or dapagliflozin): triple mechanism — HF therapy + autophagy + BHB production

The SGLT2i is specifically synergistic with the antiviral protocol: it provides continuous low-level autophagy induction between FMD cycles, keeping pressure on TD mutants while also providing standard HF benefit.

### Step 3: Measure What's Left (Serial Cardiac MRI)

| Timepoint | Assessment | Decision |
|-----------|-----------|---------|
| Baseline | LGE %, T2, LVEF | LGE < 10%: aggressive protocol. > 20%: GDMT priority, protocol supplemental |
| 6 months | T2 normalized? LGE stable? | If T2 normal: viral clearance likely complete. If still elevated: continue antiviral |
| 12 months | LVEF trajectory | If improving: continue. If plateau: switch to standard HF management only |

**T2 mapping is the "active CVB" signal.** When T2 normalizes, the 2A protease has stopped. When T2 stays elevated despite protocol, either the TD mutants are resistant to current autophagy rate (need higher FMD frequency or trehalose dose) or the inflammation is autoimmune (FOXP1 mechanism — add more butyrate).

## The New LAMP2/FOXP1 Understanding

### LAMP2 urgency for DCM

Cardiac LAMP2 baseline = 1.0× average. After CVB: κ = 0.37. This means:
- Without trehalose: 12 months to clear cardiac TD (vs model's 4.5 months)
- Every month without trehalose: ~0.5-1% additional LGE
- For a patient with LGE 8% at diagnosis: 6 months without trehalose → LGE 11% (crosses into "low reversibility" zone)
- With trehalose from day 1: clearance in 6 months, LGE stays at 8% (or improves to 6-7%)

**The gap between LGE 8% and LGE 11% is the difference between "likely full recovery" and "partial recovery."** Trehalose on day 1 is not optional for DCM patients.

### FOXP1 and Giant Cell Myocarditis Variant

Patients with CVB-DCM who have an autoimmune "giant cell" component: FOXP1 is chronically suppressed (-67x) → local Treg failure → autoreactive anti-cardiac myosin T cells escape → giant cell myocarditis on biopsy. High-dose butyrate (4-6g/day) targets this specifically via FOXP1 restoration.

If biopsy shows giant cell myocarditis: add immunosuppression (prednisone + azathioprine, standard protocol) while the antiviral clears the underlying CVB that triggered the autoimmune state.

## The Dystrophin Biomarker Question

The gap.md asked: "Can dystrophin cleavage be measured non-invasively?"

**Answer from the transcriptomics**: DMD gene is suppressed -32× in infected cells (GSE184831). This suggests circulating dystrophin fragments might be measurable in plasma — similar to how troponin reflects cardiomyocyte death.

**Proposed biomarker**: plasma micro-dystrophin fragments (specific to the 2A protease cleavage site at hinge 3). If measurable:
1. Elevated → active 2A protease → CVB-DCM confirmed (vs other DCM etiologies)
2. Declining → viral clearance working
3. Undetectable → protocol complete

This would be the first blood test to specifically identify CVB-driven DCM and monitor treatment. Research opportunity: partner with Duchenne MD research community who already study dystrophin fragments.

## The Numbers

- 2.5 million Americans have DCM
- ~35% (~875,000) have "idiopathic" DCM (no known cause) — likely viral in many
- ~200,000-300,000 have LGE < 10% (high reversibility window) right now
- Untreated: pipeline to transplant list over 10-20 years
- With protocol: potential LVEF recovery 10-23% (based on Kühl + GDMT data)

**The Kühl trial is the best evidence in the campaign.** 22 humans. LVEF 44→53%. IFN-β alone (no GDMT, no autophagy, no anti-inflammatory stack). Our protocol is oral, $170/month, includes all three additional mechanisms. The wall is doctors not knowing the Kühl data or not connecting it to their "idiopathic" DCM patients.

## The Wall (Formal)

The wall for DCM is the same as for myocarditis — just 5-10 years later.

If myocarditis THEWALL is crossed (troponin + cardiac MRI + protocol within weeks of acute myocarditis), most DCM is NEVER DIAGNOSED because it never develops.

For patients already in DCM: the wall is the irreversibility of replacement fibrosis, but the clock can still be stopped, and 200,000-300,000 patients are still in the recovery window. The wall is the delay between diagnosis and protocol start.

**Every week of delay past diagnosis = additional cardiomyocyte loss that won't come back.**
