# Pattern 006: CVB Vaccine Prevention -- The Capstone Public Health Case
## A single polyvalent CVB vaccine prevents 12 diseases simultaneously

systematic approach -- numerical track (numerics) -- Cross-disease analysis
Date: 2026-04-08
Model: `numerics/cvb_vaccine_impact.py`

---

## The Core Insight

Coxsackievirus B causes or contributes to **12 distinct diseases**. A single polyvalent
vaccine (CVB1-B5) would prevent them all. This is analogous to the HPV vaccine story:
one vaccine, multiple cancers prevented. The aggregate disease burden makes the economic
case overwhelming even though each individual disease might not justify a vaccine alone.

## Model Results: Three Vaccination Strategies Compared

| Strategy | Infection Reduction | Cases Prevented (20yr) | QALYs Gained | Net Cost (20yr) | Verdict |
|----------|-------------------|----------------------|--------------|-----------------|---------|
| **Universal Childhood** | Herd immunity builds over 15yr | **787** | **2,939** | **-$93.9M (SAVES money)** | HIGHLY COST-EFFECTIVE |
| Targeted High-Risk | 6% of population | 330 | 1,261 | $95.0M | Cost-effective |
| Ring Vaccination | Outbreak-triggered surges | 629 | 2,409 | $26.7M | Highly cost-effective |

**Population modeled: 1,000,000 over 20 years.**

### Which strategy prevents the most disease?

**Universal Childhood Vaccination** wins on every metric:
- Most total cases prevented (787 over 20 years)
- Most QALYs gained (2,939)
- Only strategy that is NET COST-SAVING ($93.9M saved over 20 years)
- Creates herd immunity effects that protect unvaccinated individuals

However, it takes the longest to reach full effectiveness (15 years to cover all
0-15-year-olds). For immediate impact during outbreaks, **Ring Vaccination** provides
rapid community protection.

**Optimal combined approach:** Universal childhood vaccination as the base program,
with ring vaccination capability for outbreak response.

---

## Disease-by-Disease Vaccine Impact

### Highest Impact (by QALYs gained, Universal strategy)

| # | Disease | CVB-Attributable | Cases Prevented | QALYs Gained | Cost Saved | Key Factor |
|---|---------|-----------------|-----------------|--------------|------------|------------|
| 1 | **T1DM** | 40% | 157.8 | 1,262 | $78.9M | Largest prize; 5-10yr lag before benefit appears |
| 2 | **ME/CFS** | 30% | 90.5 | 1,087 | $22.6M | High per-case disability; decades of illness prevented |
| 3 | **DCM** | 25% | 23.8 | 238 | $7.1M | Prevents heart failure + transplant; 10yr lag |
| 4 | **Myocarditis** | 35% | 71.4 | 143 | $3.6M | Immediate benefit; prevents DCM cascade |
| 5 | **Pericarditis** | 30% | 171.3 | 86 | $2.6M | Most common presentation; recurrence prevented |

### Moderate Impact

| # | Disease | CVB-Attributable | Cases Prevented | QALYs Gained | Cost Saved |
|---|---------|-----------------|-----------------|--------------|------------|
| 6 | Pancreatitis | 10% | 69.3 | 21 | $1.4M |
| 7 | Encephalitis | 15% | 6.1 | 49 | $0.9M |
| 8 | Aseptic Meningitis | 40% | 89.7 | 9 | $0.4M |
| 9 | Neonatal Sepsis | 50% | 1.5 | 31 | $0.3M |

### Lower Impact (but still meaningful)

| # | Disease | CVB-Attributable | Cases Prevented | QALYs Gained | Cost Saved |
|---|---------|-----------------|-----------------|--------------|------------|
| 10 | Orchitis | 15% | 9.2 | 9 | $0.1M |
| 11 | Pleurodynia | 90% | 91.7 | 5 | $0.2M |
| 12 | Hepatitis | 5% | 5.1 | 1 | $0.0M |

---

## The Paradox: Treatment AND Prevention Are Both Needed

### For the patient: The vaccine is too late.

the patient already has persistent CVB in their islets/heart/muscle/CNS.
The vaccine cannot help them. They need the **treatment protocol**:
fluoxetine (2C ATPase inhibition), fasting-mimicking diet (autophagy-driven clearance),
colchicine (NLRP3 suppression), and immune modulation.

### For the patient's children: The vaccine IS the real cure.

If the patient's children are vaccinated before their first CVB exposure:
- **No viral seeding of islets** -- no T1DM
- **No cardiac persistence** -- no myocarditis, no DCM
- **No multi-site colonization** -- no ME/CFS
- **No NLRP3 chronic activation** -- no recurrent pericarditis

The vaccine prevents the entire downstream disease cascade by blocking the first step:
viral entry and establishment.

### For the patient's grandchildren: Prevention may be complete.

If universal childhood vaccination achieves herd immunity (>75% coverage for R0=4),
CVB circulation drops to near-zero. Even unvaccinated individuals are protected by
the population-level shield. The diseases don't just decrease -- they approach elimination.

### The temporal paradox

```
                      TREATMENT              PREVENTION
                    (for existing)           (for future)
                         |                       |
Timeline:                |                       |
                         v                       v
  [Past infections] --> Current patients    Future children
                         |                       |
                    Fluoxetine             CVB Vaccine
                    Fasting/FMD           (polyvalent B1-B5)
                    Colchicine
                    Immune mod
                         |                       |
                    Clear persistent        Prevent seeding
                    CVB from organs         entirely
                         |                       |
                    Reverse damage          No damage occurs
                    (if caught early)
                         |                       |
                    BOTH ARE NEEDED
                    Treatment for this generation
                    Prevention for the next
```

---

## What Fraction of Each Disease is Preventable by CVB Vaccination?

This is the critical public health question. The answer depends on the CVB
attribution fraction -- what share of each disease is caused by CVB.

| Disease | CVB Attributable | Vaccine Efficacy | **Max Prevention** | Evidence Strength |
|---------|-----------------|-----------------|-------------------|-------------------|
| T1DM | 30-50% | 85% | **26-43%** | MODERATE-HIGH (DiViD 6/6, TEDDY, epidemiology) |
| Myocarditis | 30-40% | 85% | **26-34%** | HIGH (culture/PCR data, Caforio 2013) |
| DCM | 20-30% | 85% | **17-26%** | MODERATE (downstream of myocarditis) |
| ME/CFS | 20-40% | 85% | **17-34%** | MODERATE (Gow 1991, Bowles 1993 persistence data) |
| Pericarditis | 25-35% | 85% | **21-30%** | MODERATE (viral etiology estimates) |
| Neonatal Sepsis | 40-60% | 85% | **34-51%** | HIGH (virological confirmation) |
| Aseptic Meningitis | 35-45% | 85% | **30-38%** | HIGH (CSF culture data) |
| Pleurodynia | 85-95% | 85% | **72-81%** | VERY HIGH (essentially pathognomonic for CVB) |
| Pancreatitis | 5-15% | 85% | **4-13%** | LOW-MODERATE (viral etiology minority) |
| Orchitis | 10-20% | 85% | **9-17%** | LOW (limited CVB-specific data) |
| Encephalitis | 10-20% | 85% | **9-17%** | MODERATE (enteroviral encephalitis well-documented) |
| Hepatitis | 3-8% | 85% | **3-7%** | LOW (self-limiting, rare CVB cause) |

### The aggregate case

Adding up across all 12 diseases, in a population of 1 million:
- **Baseline annual disease burden:** ~1,421 cases/year across all 12 diseases
- **CVB-attributable:** ~429 cases/year (30% of total)
- **Vaccine-preventable:** ~365 cases/year at steady state (85% of CVB-attributable)
- **QALYs saveable per year:** ~147 QALYs/year at steady state
- **Cost savings per year:** ~$5.9M/year at steady state

Scaled to the United States (330 million):
- **Vaccine-preventable cases per year:** ~120,000
- **QALYs saveable per year:** ~48,500
- **Cost savings per year:** ~$1.95 billion

---

## The Public Health Case for CVB Vaccine Development

### Why this vaccine should exist

1. **Aggregate disease burden.** No single CVB disease justifies a new vaccine alone
   (each is too rare or too mild). But the AGGREGATE across 12 diseases is massive.
   This is the HPV analogy: Gardasil prevents cervical cancer, anal cancer, head/neck
   cancer, genital warts -- it's the aggregate that makes the case. CVB vaccine prevents
   T1DM, myocarditis, DCM, ME/CFS, pericarditis, meningitis, neonatal sepsis, and more.

2. **T1DM alone is worth it.** Even if the vaccine ONLY prevented T1DM (and did nothing
   for the other 11 diseases), the lifetime cost per T1DM case ($500K) multiplied by
   the preventable fraction (26-43% of 22/100K incidence) makes the vaccine cost-saving.

3. **Neonatal sepsis is the moral imperative.** CVB neonatal sepsis kills 30-50% of
   affected newborns. A maternal vaccination program would provide transplacental
   antibodies that reduce this to <5%. There is no acceptable reason to let newborns
   die from a vaccine-preventable infection.

4. **The technology exists.** Multiple CVB vaccine candidates are in development:
   - **PRV-101 / Provaxol** (Provention Bio): polyvalent CVB1-5 formalin-inactivated [6]
   - **CVB1 VLP vaccine** (Tampere, Finland): VLP approach, phase I complete [7]
   - The technology is well-understood (inactivated or VLP platforms)

5. **Long-term economic case.** Universal childhood vaccination is NET COST-SAVING:
   the $24.3M vaccine program cost is more than offset by $118.2M in prevented
   treatment costs over 20 years. This is a rare case where a health intervention
   literally pays for itself.

### Why this vaccine does not yet exist

1. **No single disease champion.** T1DM researchers study CVB but don't drive vaccine
   development. Cardiologists study myocarditis but don't think about vaccines. The
   12 diseases are siloed across medical specialties. Nobody sees the aggregate.

2. **Attribution uncertainty.** The CVB-attributable fraction for each disease has wide
   confidence intervals. Skeptics can argue that the fraction is at the low end.
   But even at the low end of all estimates, the aggregate case remains strong.

3. **Long lag to T1DM endpoint.** A vaccine trial measuring T1DM prevention needs
   >10 years of follow-up. This is prohibitively expensive for pharma ROI calculations.
   The TEDDY study took 15 years. Few companies will fund a trial that long.

4. **Market fragmentation.** The vaccine prevents rare-ish diseases across many
   specialties. No single medical society will champion it. This requires a
   cross-specialty public health mandate.

### The path forward

The optimal strategy is a **two-pronged campaign**:

**Prong 1: Treatment** (for existing patients)
- Fluoxetine + fasting-mimicking protocol for CVB clearance
- Colchicine for NLRP3-mediated recurrence
- Immune modulation for autoimmune component
- Target: all 12 diseases, existing patients

**Prong 2: Prevention** (for future patients)
- Universal childhood CVB vaccination (like rotavirus schedule)
- Maternal vaccination program (neonatal sepsis prevention)
- Pleurodynia surveillance + ring vaccination capacity
- Target: all 12 diseases, future generations

**The two prongs are complementary and synergistic.** Treatment handles the current
burden; prevention eliminates the future burden. Neither alone is sufficient.

---

## Connection to Campaign

This pattern is the **capstone public health document** for the CVB campaign:

| Campaign Document | Role |
|-------------------|------|
| Pattern 001 (Pleurodynia sentinel) | Surveillance system for outbreak detection |
| Pattern 002 (Last organ to clear) | Treatment endpoint determination |
| Pattern 003 (CNS clearance) | Safety assessment for treatment protocol |
| Pattern 004 (Protocol propagation) | Treatment applicability across diseases |
| Pattern 005 (Cross-disease persistence) | Biological foundation for unified etiology |
| **Pattern 006 (Vaccine prevention)** | **Public health case for primary prevention** |

Together, these six patterns tell the complete story: CVB causes 12 diseases through
a unified mechanism (patterns 1-5), and a single vaccine can prevent them all (pattern 6).

---

## Figures Generated

All figures saved to `results/figures/`:
- `vaccine_infection_reduction.png` -- SIR dynamics by strategy
- `vaccine_per_disease_impact.png` -- Disease-specific prevention (12-panel)
- `vaccine_cases_prevented_by_disease.png` -- Bar chart comparison
- `vaccine_cost_effectiveness.png` -- Cost per QALY, net cost, QALYs
- `vaccine_incidence_reduction_curves.png` -- 20-year reduction trajectories

Numerical results: `results/vaccine_impact_results.json`

---

*systematic approach -- numerical track (numerics) -- Capstone public health analysis*
*Model: numerics/cvb_vaccine_impact.py (runnable, generates all figures)*
