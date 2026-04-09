# Attempt 002: Pleurodynia-T1DM Epidemiological Correlation — Mining the Historical Data

## The Hypothesis
Epidemic pleurodynia outbreaks should temporally correlate with T1DM incidence spikes in the same geographic regions, with a lag of 1-5 years (time from CVB infection to clinical T1DM).

## The Data Sources

### Pleurodynia outbreaks (historical)
- CDC MMWR reports: enteroviral surveillance data (US, 1970-present)
- European enteroviral surveillance networks
- Bornholm Island original data (1930s, Danish records)
- WHO enteroviral reports

### T1DM incidence
- SEARCH for Diabetes in Youth Study (US, 2001-present)
- EURODIAB Incidence Study (Europe, 1989-present)
- National diabetes registries (Scandinavia — excellent population data)
- ICD code data from insurance databases

### The Analysis

```
For each geographic region R and year Y:
  1. Count pleurodynia/enteroviral cases: P(R, Y)
  2. Count T1DM new diagnoses: T(R, Y)
  3. Cross-correlate with lag τ: Corr[P(R, Y), T(R, Y+τ)] for τ = 0 to 10 years
  4. If peak correlation at τ = 2-5 years: supports temporal sequence hypothesis
```

### Expected results
- Positive cross-correlation at τ = 2-5 years (T1DM diagnosis peaks 2-5 years after enteroviral outbreak)
- Stronger in pediatric populations (shorter lag: virus → autoimmunity → diagnosis)
- Strongest in regions with good enteroviral AND T1DM surveillance (Scandinavia)

### Historical test case: Bornholm Island
- Major pleurodynia outbreak 1930s, well-documented
- Danish diabetes registry exists
- Did Bornholm have elevated T1DM incidence in 1935-1945?
- **This is a natural experiment that already happened — just need to find the data.**

## The Seasonal Signal
CVB is seasonal: summer/fall peaks (fecal-oral transmission, swimming, water sources).
T1DM diagnosis has a seasonal peak too: winter (but diagnosis, not onset).

```
Onset vs Diagnosis:
  CVB infection: summer/fall (Year 0)
  Autoimmune cascade begins: fall/winter (Year 0)
  Silent destruction: Years 0-X
  Clinical T1DM (80-90% beta cell loss): Year X

  If the lag is ~6-12 months: autumn CVB → winter/spring T1DM
  This matches the observed winter T1DM diagnosis peak!
```

## What This Study Proves (If Positive)

1. **Causal link**: CVB outbreaks → T1DM incidence (with predictable lag)
2. **Prevention justification**: suppressing CVB outbreaks prevents T1DM
3. **Early warning**: pleurodynia outbreaks become T1DM early warning signals
4. **Vaccine urgency**: CVB vaccine prevents both pleurodynia AND downstream T1DM

## What This Study Can't Prove

- Individual-level causation (ecological fallacy — population correlation ≠ individual causation)
- The specific mechanism (could be any CVB disease, not specifically pleurodynia)
- Whether antiviral treatment during pleurodynia prevents T1DM (needs intervention trial)

## Immediate Action (numerical track Task)

**REQUEST TO ODD INSTANCE:**
1. Pull CDC enteroviral surveillance data (NREVSS) by year, serotype, region
2. Pull SEARCH/EURODIAB T1DM incidence data by year, age, region
3. Compute cross-correlation with lags 0-10 years
4. Plot: heat map of correlation strength by lag and region
5. Test Bornholm Island specifically if Danish data accessible

This is a data analysis/epidemiology task — pure numerics.

## Status: EPIDEMIOLOGICAL STUDY DESIGN — leverages existing data, no new collection needed
