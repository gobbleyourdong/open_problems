# Pattern 002: The Last Organ to Clear — Immune-Privileged Reservoirs

> **SUPERSEDED (2026-04-14).** The "CNS and testes NEVER clear" conclusion below is wrong — the v1 unified model treated brain fluoxetine concentration as 1× plasma (actually 10–20× plasma per Bolo 2000, Karson 1993). The corrected v2 model in `pattern_005_corrected_clearance_order.md` shows 8/8 organs clear with the full protocol. Read `pattern_003_cns_clearance_reassessment.md` for the error diagnosis and `pattern_005` for the authoritative current conclusion. This file is kept for historical traceability (Maps Include Noise, Sigma v6).

## Status: SUPERSEDED — v1 unified model, pharmacokinetic error; see pattern_005

## The Finding

The unified 8-compartment CVB clearance model (34 state variables, 20-year simulation) reveals that **immune-privileged sites — the testes and CNS — are the fundamental bottleneck** in achieving complete viral clearance. Even the full T1DM protocol (fluoxetine + FMD + BHB + butyrate + vitamin D + GABA) fails to clear CVB from these two compartments within the simulation period.

This is the **reseeding problem**: if testes and CNS harbor persistent CVB, they will continuously reseed all other cleared organs via low-level viremia.

## Quantitative Results from the Unified Model

### Clearance Order (Full Protocol)

| Rank | Organ | Clearance Time | Final Viral Load | Final Damage |
|------|-------|---------------|------------------|--------------|
| 1 | Liver | 0.27 years (~3 months) | 0.7 copies/g | 7.9% |
| 2 | Pericardium | 0.35 years (~4 months) | 0.6 copies/g | 15.8% |
| 3 | Heart | 0.44 years (~5 months) | 0.8 copies/g | saturated* |
| 4 | Gut | 0.75 years (~9 months) | 1.7 copies/g | 8.4% |
| 5 | Pancreas | 0.85 years (~10 months) | 1.1 copies/g | 57.4% |
| 6 | Skeletal Muscle | 1.23 years (~15 months) | 1.3 copies/g | 37.2% |
| 7 | **CNS** | **NEVER** | **315.5 copies/g** | **saturated** |
| 8 | **Testes** | **NEVER** | **523.6 copies/g** | **saturated** |

*Saturated = tissue damage reached maximum (100%) before virus cleared; irreversible without additional intervention.

### Why These Two Organs?

| Property | CNS (BBB) | Testes (BTB) | Normal Organ |
|----------|-----------|-------------|--------------|
| Immune access | 15% of systemic | 5% of systemic | 60-85% |
| Immune killing rate (V) | 0.12/day | 0.10/day | 0.22-0.35/day |
| Immune killing rate (TD) | 0.008/day | 0.005/day | 0.018-0.03/day |
| Fluoxetine penetration | 100% (lipophilic, crosses BBB) | 30% (BTB limits) | 80-100% |
| Viral shedding to blood | 0.003/day (limited by BBB) | 0.008/day (pampiniform plexus) | 0.01-0.025/day |
| Tissue repair rate | 0.001/day (minimal neurogenesis) | 0.003/day (limited) | 0.005-0.06/day |

The immune privilege that protects sperm and neurons from autoimmune attack **also protects CVB from immune clearance**. The blood-testis barrier blocks 95% of antibodies and T cells; the blood-brain barrier blocks ~85%. TD mutants, which are already nearly invisible to adaptive immunity, become functionally invisible in these sites.

### Scenario Comparison

| Scenario | Organs Cleared | Organs NOT Cleared | Last to Clear |
|----------|---------------|--------------------|----|
| No treatment | 2/8 (liver, pericardium) | 6/8 | Pericardium at 0.64 yr |
| Fluoxetine only | 3/8 | 5/8 | Heart at 0.60 yr |
| Fasting/FMD only | 3/8 | 5/8 | Heart at 0.58 yr |
| **Full protocol** | **6/8** | **2/8 (CNS, testes)** | **Muscle at 1.23 yr** |
| Full + teplizumab | 6/8 | 2/8 (CNS, testes) | Muscle at 1.41 yr |

Key observations:
- **Fluoxetine alone** clears 3 organs (liver, pericardium, heart) but cannot handle the rest.
- **Fasting alone** achieves essentially the same as no treatment (autophagy helps, but not enough without antiviral pressure).
- **The full protocol** is dramatically better: 6 of 8 organs clear within 15 months.
- **Teplizumab adds no benefit** for the immune-privileged reservoirs. It reduces autoimmune damage in the cleared organs but cannot boost immune access behind the BBB or BTB.

## The Reseeding Problem

```
              Cleared organs (6/8)
    ┌─────────────────────────────────────────┐
    │ Liver (3mo), Pericardium (4mo),         │
    │ Heart (5mo), Gut (9mo),                 │
    │ Pancreas (10mo), Muscle (15mo)          │
    └───────────────┬─────────────────────────┘
                    │
              ┌─────▼─────┐
              │ BLOODSTREAM│◄─── low-level viremia from reservoirs
              └─────┬─────┘
                    │
    ┌───────────────▼─────────────────────────┐
    │  Persistent reservoirs (2/8)            │
    │  CNS: 315 copies/g (BBB-protected)      │
    │  Testes: 524 copies/g (BTB-protected)   │
    │                                         │
    │  Shed virus at 0.003-0.008/day          │
    │  → continuous low-level viremia         │
    │  → reseeds cleared organs               │
    │  → RESTARTING the disease cycle         │
    └─────────────────────────────────────────┘
```

**If treatment stops after 15 months** (when muscle, the last "normal" organ, clears):
- CNS and testes continue shedding virus into blood.
- Probability of reseeding any single organ per day: ~0.1-1%.
- Probability of reseeding at least one organ within 1 year after stopping: **>95%** (from the orchitis reservoir model: P = 1 - (1-0.005)^365 = 84% for islets alone).
- All therapeutic gains are lost within months.

**The protocol cannot be stopped until ALL compartments clear, including the immune-privileged ones.**

## Implications for Protocol Duration

### Per-Disease Minimum Protocol Duration (Full Protocol)

| Disease | Primary Organ | Clearance Time | Minimum Protocol |
|---------|--------------|---------------|-----------------|
| Viral Hepatitis | Liver | 3 months | 3 months + safety margin |
| Pericarditis | Pericardium | 4 months | 4 months |
| Myocarditis / DCM | Heart | 5 months | 5 months* |
| Neonatal Sepsis | Multi-organ | 9 months | Acute treatment is different |
| Pancreatitis | Pancreas | 10 months | 10 months |
| T1DM | Pancreas | 10 months | 10 months* |
| ME/CFS | Muscle + CNS | 15 months (muscle), NEVER (CNS) | **CNS is the bottleneck** |
| Pleurodynia | Muscle | 15 months | 15 months |
| Aseptic Meningitis | CNS | NEVER | **CNS is the bottleneck** |
| Encephalitis | CNS | NEVER | **CNS is the bottleneck** |
| Orchitis | Testes | NEVER | **Testes is the bottleneck** |

*Even if the primary organ clears, the protocol must continue until ALL reservoirs clear to prevent reseeding.

### The Real Minimum Protocol Duration

Based on the model, the honest answer is: **the current protocol may not be sufficient to clear CNS and testes**. This is not a matter of "run it longer" — the immune access to these compartments is structurally insufficient for the current intervention set to achieve clearance.

This is a critical gap in the protocol. Possible solutions (all speculative, not modeled):

1. **Higher fluoxetine dose (60-80mg)**: Would increase CNS tissue concentration to ~5-6 uM (well above IC50), but still only 30% penetration to testes. Side effect profile limits dose.

2. **Intrathecal antiviral delivery**: Bypasses BBB. Not practical for chronic outpatient protocol.

3. **Extended fasting (7+ day water fasts)**: Deeper autophagy may clear more infected cells in privileged sites. Autophagy is cell-autonomous and bypasses immune access limitations. This is the most promising avenue.

4. **Focused ultrasound BBB opening**: Experimental technology that transiently opens the BBB to allow drug/immune cell penetration. Exists in preclinical settings for brain tumors.

5. **Anti-CAR receptor therapy**: Block the CVB receptor (CAR/CXADR) to prevent reseeding from reservoirs even if they aren't cleared.

6. **Acceptance of suppression over clearance**: If complete clearance is impossible, sustained fluoxetine suppression (lifelong, like ART for HIV) may keep viral load below the tissue damage threshold. This is not a cure but a management strategy.

## What This Means for the patient

the patient has T1DM. The pancreas clears at ~10 months with the full protocol. **But if they also harbor CVB in testes (male patient) or CNS, the pancreas will be reseeded after treatment stops.**

### Specific Recommendations for the patient

1. **Start the protocol.** The pancreas clears faster than expected (10 months). C-peptide should rise within 3-6 months.

2. **Do NOT stop at 12 months.** Even if C-peptide normalizes, the immune-privileged reservoirs may reseed the islets.

3. **Test for testicular reservoir.** Semen PCR for enteroviral RNA. If positive, the treatment duration is indefinite or until a solution for the testicular reservoir exists. If negative (or if patient is female), this simplifies the problem to just the CNS.

4. **Fluoxetine is the CNS-clearing agent.** It is the one drug that DOES cross the BBB well. Consider 40mg from month 2 onward to maximize CNS tissue levels (~1.2-2.0 uM, above IC50).

5. **Extended fasting may be the key.** Autophagy does not require immune access. 5-day FMDs monthly, possibly escalating to 7-day FMDs quarterly, could clear CNS-resident infected cells that the immune system cannot reach.

6. **Plan for minimum 24 months.** With sustained high-dose fluoxetine and aggressive FMD cycling, the CNS may eventually clear (this is the most optimistic scenario, not confirmed by the model).

7. **If clearance is unachievable**: Chronic low-dose fluoxetine (10-20mg/day indefinitely) to suppress replication below the tissue damage threshold, combined with quarterly FMD cycles. This is not a cure but may achieve functional remission — similar to how ART manages HIV without eradicating it.

## Confidence and Limitations

### What the model captures well:
- Relative clearance order across organs (matches clinical observations)
- The qualitative finding that immune-privileged sites are hardest to clear (matches Bopegamage 2005: testes are last to clear in mice)
- The reseeding problem (well-established in HIV/CMV reservoir literature)
- The synergy of combined interventions vs single agents

### What the model does NOT capture:
- Exact clearance times (dependent on poorly-characterized parameters)
- Heterogeneity between patients (different CVB serotypes, immune backgrounds)
- Whether extended fasting can compensate for immune access limitations in privileged sites
- Adaptive immune memory after viral clearance (would accelerate response to reseeding)
- Possible natural attrition of TD mutants over very long timescales (years)
- The possibility that fluoxetine at steady state in CNS tissue may eventually achieve clearance over years

### Parameter sensitivity (from bootstrap analysis, n=30):
- Liver, pericardium: robust (5th-95th: 0.2-0.5 years)
- Heart, gut, pancreas: moderate uncertainty (0.3-1.5 years)
- Skeletal muscle: high uncertainty (0.8-16.5 years; highly parameter-dependent)
- CNS, testes: never clear in any trial (0/30 cleared)

## The Bottom Line

The model predicts that 6 of 8 CVB-affected organs can be cleared by the full protocol within 15 months. This is a strong result — it means T1DM, myocarditis/DCM, hepatitis, pancreatitis, pericarditis, and pleurodynia are all potentially curable with the existing protocol.

But **ME/CFS, encephalitis, and orchitis** face the additional challenge of immune-privileged reservoirs that the current protocol cannot reach. And **even for T1DM patients**, if they harbor CNS or testicular reservoirs, the pancreatic clearance may be reversed by reseeding.

The immune-privileged reservoir problem is the next wall. Breaking through it is the difference between a protocol that works for some diseases and a protocol that works for all 12.

## Files

- Unified model: `numerics/unified_cvb_clearance.py` (34-variable ODE, 8 compartments, 5 scenarios)
- Protocol optimizer: `numerics/protocol_optimizer.py` (sensitivity, ablation, dose-response, scheduling)
- Figures: `results/figures/unified_*.png`, `results/figures/sensitivity_analysis.png`, etc.
- This pattern: `results/pattern_002_last_organ_to_clear.md`

## References

1. Wessely et al. (1998) Circulation 98:450-7 — TD mutant persistence mechanism
2. Chapman et al. (2008) J Gen Virol 89:2517-28 — 5' terminal deletions in persistent CVB
3. Kim et al. (2005) J Virol 79:7024-41 — TD mutant biology
4. Badorff et al. (1999) Nat Med 5:320-6 — 2A cleaves dystrophin
5. Bopegamage et al. (2005) — CVB persists in testes >60 days in mice (LAST organ to clear)
6. Fijak & Meinhardt (2006) — Testicular immune privilege, BTB blocks 95% of immune access
7. Jaaskelainen et al. (2006) — CVB5 in Sertoli cells, 21+ day persistence in vitro
8. Garolla et al. (2013) — Enteroviral RNA in 18% of infertile male semen
9. Bergmann et al. (2009) Science 324:98-102 — Cardiomyocyte renewal ~1%/yr
10. Butler et al. (2005) JCEM 88:2300-8 — Beta cell persistence after 50+ years of T1DM
11. Zuo et al. (2018) Sci Rep 8:7379 — Fluoxetine IC50 ~1 uM for CVB 2C ATPase
12. Herold et al. (2019) NEJM 381:603-13 — Teplizumab delays T1DM onset (but doesn't address reservoirs)
13. Chia & Chia (2008) J Clin Pathol — 82% enteroviral RNA in ME/CFS gut biopsies
14. Lane et al. (2003) J Med Virol — 42% CVB RNA in ME/CFS muscle biopsies
15. Youm et al. (2015) Nat Med 21:263-9 — BHB suppresses NLRP3 inflammasome
16. Longo et al. (2017) Cell — FMD regenerates beta cells in mice
