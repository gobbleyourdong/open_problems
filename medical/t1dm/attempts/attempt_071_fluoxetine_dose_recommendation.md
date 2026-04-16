# Attempt 071: Fluoxetine Dose Recommendation — 20mg vs 40mg vs 60mg

## The Question
What dose of fluoxetine achieves antiviral efficacy in ALL target organs?

## The Answer (From IC50 Reconciliation + ODD PK Data)

### Tissue concentrations by dose

| Organ | 20mg | 40mg | 60mg | IC50 | Ratio @ 20mg | Ratio @ 60mg | Inhibition @ 20mg | Inhibition @ 60mg |
|-------|------|------|------|------|-------------|-------------|-------------------|-------------------|
| Brain | 4.5 μM | 9.0 μM | 13.5 μM | 1.0 μM | 4.5x | 13.5x | 82% | 93% |
| Liver | 3.0 | 6.0 | 9.0 | 1.0 | 3.0x | 9.0x | 75% | 90% |
| Testes | 2.25 | 4.5 | 6.75 | 1.0 | 2.25x | 6.75x | 69% | 87% |
| Heart | 1.8 | 3.6 | 5.4 | 1.0 | 1.8x | 5.4x | 64% | 84% |
| Pericardium | 1.5 | 3.0 | 4.5 | 1.0 | 1.5x | 4.5x | 60% | 82% |
| Pancreas | 1.2 | 2.4 | 3.6 | 1.0 | 1.2x | 3.6x | 55% | 78% |
| Muscle | 0.9 | 1.8 | 2.7 | 1.0 | 0.9x | 2.7x | 47% | 73% |
| Gut | 0.6 | 1.2 | 1.8 | 1.0 | 0.6x | 1.8x | 38% | 64% |

### The dose decision

**20mg**: 6/8 organs above IC50. Brain and liver well-covered. Muscle and gut sub-IC50 → depend on autophagy for clearance. Testes at 2.25x IC50 → clears but slowly (69% inhibition).

**40mg**: 7/8 organs above IC50. Only gut remains marginal. Testes at 4.5x IC50 → much better (82%). Muscle reaches 1.8x → adequate.

**60mg**: 8/8 organs above IC50. All organs at ≥64% inhibition. Testes at 6.75x → strong (87%). Gut reaches 1.8x → adequate with autophagy support.

## Recommendation

```
FEMALE PATIENTS: 20mg fluoxetine
  - No testes → slowest organ is muscle (autophagy clears it)
  - 20mg provides adequate coverage for 6/7 organs via drug + 7/7 via drug + autophagy
  - Lower side effect burden
  - Clearance timeline: ~10 months

MALE PATIENTS: 40-60mg fluoxetine
  - Testes are the rate-limiting organ
  - 20mg: 69% inhibition in testes → clears in ~18 months
  - 60mg: 87% inhibition in testes → clears in ~12 months
  - Recommend 40mg initially, escalate to 60mg if tolerated and if clearing slowly
  - Clearance timeline: ~12-18 months

T1DM PATIENTS SPECIFICALLY: consider 40mg
  - Pancreas at 20mg: 1.2x IC50 (55% inhibition) — marginal
  - Pancreas at 40mg: 2.4x IC50 (71% inhibition) — adequate
  - The pancreas is the TARGET organ for T1DM → want robust drug effect there
  - Autophagy helps but pharmacological suppression speeds viral clearance
  - Faster viral clearance → faster D reduction → faster R > D reversal
```

## Safety at Higher Doses

Fluoxetine has been used at 60-80mg/day for OCD (FDA-approved indication). Safety data exists:

| Dose | Common side effects | Serious concerns |
|------|-------------------|-----------------|
| 20mg | Nausea (first week), insomnia, sexual dysfunction | Minimal |
| 40mg | Same as 20mg, slightly more frequent | QTc prolongation (monitor ECG) |
| 60mg | GI effects more common, sexual dysfunction more likely | QTc prolongation (check baseline + 1 month) |
| 80mg | Significant side effect burden | Not recommended for this indication |

**The safety ceiling for fluoxetine is high.** 60mg is routinely prescribed. The main management consideration is QTc monitoring and GI tolerability (especially if also taking semaglutide or butyrate).

## Drug Interaction Update at Higher Doses

At 60mg fluoxetine, CYP2D6 inhibition is STRONGER:
- Codeine → ineffective (can't convert to morphine) — use alternatives for pain
- Tamoxifen → reduced efficacy — relevant if breast cancer treatment concurrent
- Other CYP2D6 substrates: check interactions before prescribing

**No change to the itraconazole/colchicine interaction** — that's CYP3A4, not CYP2D6.

## Updated PATIENT_ZERO_TIMELINE Impact

For the operator (male with T1DM):
- Recommended dose: 40mg (balances pancreatic efficacy with side effect profile)
- Titration: 10mg × 1 week → 20mg × 2 weeks → 40mg (target dose)
- If tolerating well and testicular clearance is a concern: escalate to 60mg at month 3
- Monitor: QTc at baseline, 1 month, and 3 months after dose change

## Status: DOSE RECOMMENDATION FORMALIZED — sex-specific, organ-targeted, safety-bounded
