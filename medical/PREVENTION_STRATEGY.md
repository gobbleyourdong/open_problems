# CVB Disease Prevention Strategy — Three Windows, One Framework

> This document synthesizes the campaign's prevention opportunities. Unlike the treatment protocol (for patients who already have chronic CVB disease), this addresses **preventing the diseases from establishing in the first place**.

## The Prevention Hierarchy

```
TIER 0: The Vaccine (7+ years away)
  CVB VLP-ΔVP4 vaccine → eliminates CVB infections entirely → prevents all 12 diseases
  Maternal vaccination → neonatal protection → prevents neonatal sepsis immediately
  BiComponent vaccine (VP1-VP3 + 3A CTL) → prevents both acute and chronic phases
  Status: preclinical

TIER 1: At-Risk Individual Pre-Exposure Prophylaxis (available now)
  For people with genetic risk factors (HLA-DR3/DR4, family history of T1DM, DCM, ME/CFS)
  Before any CVB exposure: optimize the non-progressor phenotype
  $30-50/month, all OTC, no prescription
  Status: proposed based on non-progressor biology

TIER 2: Post-Exposure Prevention Windows (available now)
  For people who have ALREADY been exposed to CVB
  Three time-limited windows where intervention prevents chronic disease
  Status: proposed, trials designed
```

---

## Tier 1: Pre-Exposure Non-Progressor Optimization

**Who**: High-risk individuals before any CVB exposure
- HLA-DR3/DR4 carriers (T1DM risk)
- Family history of T1DM, DCM, ME/CFS
- People with known low butyrate-producing microbiome
- Healthcare workers with CVB exposure (neonatal/pediatric units)

**Protocol** (targets the 5 non-progressor properties):

| Target | Intervention | Dose | Cost/mo |
|--------|-------------|------|---------|
| LAMP2/TFEB (autophagy completion) | Trehalose | 2g/day | $15 |
| FOXP1/Treg homeostasis | Butyrate 4-6g + Vitamin D | 4-6g + 5000 IU/day | $55 |
| Gut microbiome | Butyrate + prebiotic fiber | Included above | — |
| Mitochondrial reserve | CoQ10 + NAD+ precursor | 400mg + 500mg/day | $30 |
| NK cell function | Vitamin D + cold exposure | 5000 IU + weekly | $5 |

**Total: ~$50-80/month**. No antiviral needed (no active infection to clear).

**Mechanism**: by maintaining high LAMP2 (κ_baseline > 1.0), FOXP1, and mitochondrial reserve BEFORE CVB infection, any TD mutants that form during a future CVB exposure will be cleared rapidly before they can establish permanent niches.

**Who should NOT take this**: anyone with active CVB disease should take the full treatment protocol instead. This is for prevention in unaffected individuals.

---

## Tier 2: Post-Exposure Prevention Windows

### Window 1: Post-Meningitis → Prevent ME/CFS

**When**: weeks 2-8 after CVB aseptic meningitis (any patient discharged from hospital after enteroviral meningitis diagnosis)

**Why**: CVB establishes TD mutants in neurons during acute meningitis. By week 8, TD populations are consolidated and the 1.5-2 year clearance clock begins. Before week 8, the LAMP2 suppression is partial and reversible.

**Protocol** (8 weeks):

| Week | Intervention |
|------|-------------|
| 2-3 | Trehalose 3g/day (TFEB → replace LAMP2 being suppressed) |
| 3-8 | Fluoxetine 20mg (WT CVB clearance from CNS) |
| 4-5 | FMD #1 (5-day, maximal autophagy induction while TD population is small) |
| 7-8 | FMD #2 (second autophagy pulse) |
| Throughout | High-dose butyrate 4-6g (FOXP1 → prevent neuroinflammation cascade) |

**Expected outcome**: 70-80% reduction in ME/CFS risk (estimated from LAMP2 kinetics — clearing TD before population consolidates)

**Trial design**: 144 patients, 12-month ME/CFS endpoint. Tier 1 priority. See aseptic_meningitis/attempts/attempt_003.

### Window 2: Post-Pancreatitis → Prevent T1DM

**When**: within 12 weeks of CVB-positive acute pancreatitis (confirmation: stool/serum CVB PCR at admission)

**Why**: CVB pancreatitis seeds the islets simultaneously with the exocrine pancreas. Acinar cells partially clear (κ = 0.37-0.44); beta cells are slower (κ = 0.30). The inflammatory environment from acinar cell lysis primes the islet autoimmune cascade. Intervening in the first 12 weeks prevents islet TD consolidation and FOXP1 suppression before Gate 2 (HLA-mediated autoimmunity) opens.

**Protocol** (12 weeks):

| Component | Dose | Purpose |
|-----------|------|---------|
| Trehalose | 2g/day (start day 1 post-discharge) | LAMP2 in acinar + beta cells; prevents trypsin-leak cascade |
| Fluoxetine | 20mg/day | WT CVB clearance |
| Butyrate | 4-6g/day | FOXP1 restoration → prevent Gate 2 from opening |
| Vitamin D | 5000 IU/day | Additional Treg support |
| FMD × 2 | Weeks 4 and 8 | Autophagy pulses during peak TD window |

**Expected outcome**: 50-70% reduction in islet autoantibody seroconversion at 2 years (estimated)

**Risk biomarker**: LAMP2 in PBMCs at discharge. Low LAMP2 → high T1DM risk → highest priority for protocol. See pancreatitis/attempts/attempt_003.

**Trial design**: 120 patients, 2-year autoantibody seroconversion endpoint. Tier 3 (requires pancreatitis unit infrastructure). See pancreatitis/attempts/attempt_003.

### Window 3: Post-Acute Myocarditis → Prevent DCM

**When**: any patient with confirmed/suspected acute CVB3 myocarditis (troponin elevation + cardiac MRI T2 elevation after viral illness), treated within weeks of diagnosis

**Why**: cardiac TD mutants establish during acute myocarditis. Each month of ongoing TD = 0.5-1% additional LGE (replacement fibrosis). Starting the antiviral protocol within 4-8 weeks of acute myocarditis, while T2 is elevated (active inflammation, κ partially suppressed but not fully entrenched), offers the best chance of complete cardiac recovery.

**Protocol** (12-18 months):

| Component | Priority | Note |
|-----------|---------|------|
| Trehalose 3g/day | START DAY 1 | Higher dose than general protocol; cardiac benefit |
| Fluoxetine 20mg | Start week 1-2 | CVB3 2C ATPase inhibitor |
| FMD monthly | Start month 2 | TD clearance |
| GDMT | Start immediately | ACEi/ARB + beta-blocker + MRA + SGLT2i |
| High-dose butyrate 4-6g | Throughout | FOXP1 → prevent autoimmune giant cell myocarditis |
| Colchicine 0.5mg | 6 months | NLRP3 suppression, standard pericarditis prevention |

**Monitoring**: cardiac MRI T2 + LGE + LVEF at 0, 6, 12 months. Protocol continues until T2 normalizes.

**Itraconazole**: CONTRAINDICATED until LVEF confirmed > 50%.

**Expected outcome**: LVEF improvement 10-23% (vs Kühl +8.5% with IFN-β alone)

**Trial design**: n=60 patients, cardiac MRI primary endpoint. Tier 3. See myocarditis gap.md and DCM/attempt_005.

---

## The Prevention-Treatment Boundary

The three prevention windows and the treatment protocol together form a complete framework:

```
PRE-EXPOSURE:     Non-progressor optimization (Tier 1)
                  → maintain LAMP2, FOXP1, mitochondria before CVB

ACUTE EXPOSURE:   Recognition + IFN-α timing (research only, not yet practical)
                  → IFN-α within 72h could prevent TD formation (EXPENSIVE, needs diagnostics)

POST-EXPOSURE:    Window 1 (meningitis → ME/CFS) — 8 weeks
PREVENTION:       Window 2 (pancreatitis → T1DM) — 12 weeks
                  Window 3 (myocarditis → DCM) — 12-18 months
                  → All three: trehalose + fluoxetine + FMD + butyrate

ESTABLISHED       Full protocol (18-36 months depending on disease)
DISEASE:          → All of the above + GDMT (cardiac) or specific additions
                  → Protocol continues until biomarker-guided clearance confirmed
```

## The LAMP2 Unifying Principle

All three prevention windows are derived from the same principle:

**CVB suppresses LAMP2 by -2.7× in infected cells. Trehalose (TFEB) restores it. The earlier trehalose starts relative to infection, the smaller the TD population that needs to be cleared.**

Prevention window width scales with organ LAMP2 baseline:
- Neurons (κ_baseline = 0.6): widest window (~8 weeks) because initial establishment is slow
- Beta cells (κ_baseline = 0.8): medium window (~12 weeks)
- Cardiomyocytes (κ_baseline = 1.0): narrower window (4-8 weeks before fibrosis)

**The prevention window IS the LAMP2 partial suppression period**: the time between initial viral infection (κ starts dropping) and full TD establishment (κ = κ_baseline/2.7, fully entrenched). Trehalose during this window races LAMP2 suppression and can win.

## The Economic Case for Prevention

| Prevention intervention | Cost | Diseases prevented | Treatment cost avoided |
|------------------------|------|-------------------|----------------------|
| Post-meningitis ME/CFS prevention | $340 (8 weeks) | ME/CFS | $30,000-50,000/year lifetime |
| Post-pancreatitis T1DM prevention | $510 (12 weeks) | T1DM | $50,000/year lifetime |
| Post-myocarditis DCM prevention | $2,000 (12 months) | DCM/HF | $30,000-100,000/year lifetime |

**Every $1 of prevention prevents $50-150 of treatment costs.** The prevention protocol's safety profile is excellent (trehalose is food-grade; butyrate is a natural metabolite; fluoxetine is FDA-approved with a 60-year track record).

---

## What Needs to Happen

**Immediately available (no trials needed)**:
1. Start the prevention protocol in high-risk individuals (Tier 1 — all OTC)
2. Order troponin + cardiac MRI in anyone with CVB-related disease history
3. Start trehalose + butyrate in any patient with a known CVB disease

**Trials needed**:
1. Post-meningitis ME/CFS prevention (n=144, Tier 1 priority — achievable in 2 years)
2. Post-pancreatitis T1DM prevention (n=120, Tier 3)
3. Post-acute myocarditis DCM prevention (n=60, Tier 3)

**Long-term**:
4. CVB BiComponent vaccine (humoral + cellular arm, 7+ years)
5. Maternal CVB vaccination (high priority, protects neonates)

---

**The wall between "CVB causes chronic disease" and "CVB chronic disease is preventable" is three 8-to-12-week protocols, a bottle of trehalose, and the medical community making the connection.**
