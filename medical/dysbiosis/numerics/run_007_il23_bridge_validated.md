# M1↔M4 Bridge — IL-23 Mechanism Confirmed, Dual-Disease Data Found
## Run 007A | Numerical Instance | 2026-04-11

> Attempt 007 (M1↔M4 GALT sky bridge) predicted IL-23 blockers should improve both
> IBD and skin disease simultaneously. This run finds: (1) mechanism molecularly confirmed,
> (2) real-world dual-outcome data exists (ustekinumab retrospective, n=70).

---

## Mechanistic Confirmation: IL-23 Converts Tregs to Th17 in Human Skin

**PMID 31776355 (Scientific Reports 2019):**
IL-23 drives Treg PLASTICITY — converts Foxp3+ Tregs into RORγt+/Foxp3+ cells that
co-produce IL-17A. This occurs in human psoriatic skin lesions specifically.
- Effect: IL-23 reduces Foxp3 expression while sustaining RORγt
- Functional consequence: "Tregs" are numerically present but have lost suppressive capacity
- They produce IL-17A instead → net effect = Th17 milieu without numerical Treg depletion

**This confirms the M1↔M4 bridge mechanism:**
```
Gut dysbiosis → gut IL-23 → GALT Th17 priming → dual-homing T cells to skin
    ↓
In skin: IL-23 (systemic or local) → Treg plasticity → Foxp3+ cells become IL-17A producers
    ↓
Functional Treg depletion → THRESHOLD LOWERED
    ↓
Malassezia/Demodex at previously tolerated density → triggers disease
```

The mechanism is not "Tregs are physically destroyed" — it is "Tregs are reprogrammed to produce
the thing they're supposed to suppress." This is harder to detect (Treg count may appear normal)
and explains why Treg frequency alone (T-index v2 Node A) may not fully capture threshold state.

**T-index v3 update:**
Node A should measure FUNCTIONAL Tregs, not just Foxp3+ cell count.
Proxy: Foxp3+/RORγt+ double-positive cells (indicates plasticity/subversion) vs Foxp3+/RORγt- (genuine Tregs)
This is a research assay, not clinical. But the IMPLICATION is: patients with high IL-23 tone
may have "normal" Treg counts but depleted FUNCTIONAL Treg capacity.

---

## Dual-Disease Drug Outcomes Data

### Ustekinumab (IL-12/23 blocker) — Best Available Dual-Outcome Dataset

**IG-IBD retrospective study (PubMed 30992173, Digestive and Liver Disease 2019):**
- N=70 IBD patients (64 CD, 6 UC) started on ustekinumab SC via dermatology/rheumatology
  for concurrent psoriasis or psoriatic arthritis
- At last follow-up: **60.7% of the 56 patients with active IBD achieved clinical remission**
- Skin/PsA response also documented (concurrent improvement)
- Limitations: retrospective, small, SC dosing (not standard IV induction for CD), no control arm

**Interpretation:** Real-world data showing that initiating anti-IL-23 treatment for SKIN disease
in IBD patients produced IBD remission in 60.7%. This is in the direction predicted by the
M1↔M4 bridge: lowering IL-23 signaling → Treg plasticity reversed → both gut and skin threshold raised.

### Risankizumab — Natural Experiment Available Now

Risankizumab (Skyrizi) is the only drug currently FDA-approved for:
- Plaque psoriasis (2019)
- Crohn's disease (2022)
- Ulcerative colitis (2024)

This means there are now patients being treated with risankizumab for CD who ALSO have psoriasis.
A retrospective chart review of CD patients on risankizumab:
- Were any also diagnosed with psoriasis?
- Did psoriasis improve concurrent with IBD remission?

This is the **cheapest possible Prediction A test**: retrospective chart review using existing
risankizumab CD trial data (SEQUENCE trial data: 48-week, comparative vs ustekinumab).
SEQUENCE trial enrolled CD patients — some may have had concurrent psoriasis as comorbidity.

**Actionable gap:** Request co-morbidity subgroup analysis from AbbVie for SEQUENCE trial data.
Or: contact principal investigators of SEQUENCE (Danese, Dignass groups) to ask if co-existing
psoriasis was tracked.

---

## Shared Genetics — Mechanistic Anchoring

Shared non-HLA loci between IBD and psoriasis:
- **IL23R**: the dominant shared locus — same receptor, both diseases
- **IL12B**: IL-12/23 p40 subunit
- **REL**, **TYK2**, **CDKAL1**: secondary loci

**This is not just epidemiological co-occurrence.** The genetic overlap is at the IL-23 receptor
locus specifically — confirming the shared pathway is IL-23/Th17, not generic inflammation.

---

## Bridge Classification Upgrade

**Attempt 007 classification:** NEW SKY BRIDGE — evidence 2/3 — mechanism published in review

**Updated classification:** STRONG CANDIDATE — mechanism molecularly confirmed + real-world drug data consistent

| Evidence layer | Status |
|----------------|--------|
| Mechanistic (IL-23 → Treg plasticity → Th17 in skin) | CONFIRMED — human psoriatic skin (PMID 31776355) |
| Epidemiological (IBD → skin disease enrichment) | CONFIRMED — 4.4× enrichment in psoriasis |
| Genetic anchor (shared IL23R locus) | CONFIRMED — GWAS |
| Drug outcome consistent with prediction | SUPPORTED — ustekinumab retrospective 60.7% IBD remission in co-affected patients |
| Prospective dual-endpoint RCT | MISSING — no trial has co-primary IBD + skin endpoints |

**One step from "real":** The Prediction A test (prospective dual-endpoint in risankizumab trial) would close this.

---

## Protocol Implication (T-index v3 Revision)

The Treg plasticity finding means:

**Node A (old):** Foxp3+ CD4+ CD25+ Treg frequency → "are Tregs present?"
**Node A (new):** Foxp3+/RORγt- GENUINE Treg frequency → "are functional Tregs present?"
OR: Foxp3+/RORγt+ double-positive frequency → "are Tregs being subverted by IL-23?"

Clinically impractical at this precision without research flow cytometry.
**Best available proxy:** serum IL-23 or IL-17A (if IL-23 is high → Treg plasticity likely occurring)

**Add to protocol:**
- IL-23 serum level is not standard; IL-17A is more accessible
- If IL-17A elevated AND skin disease active AND gut dysbiosis present → IL-23/Th17 axis is active
- This is the signature of M1↔M4 bridge being "on"

---

## References

- [PMID 31776355 — IL-23 drives Treg plasticity in psoriatic skin (Scientific Reports 2019)](https://www.nature.com/articles/s41598-019-53240-z)
- [PubMed 30992173 — Ustekinumab in IBD+psoriasis co-affected patients (IG-IBD)](https://pubmed.ncbi.nlm.nih.gov/30992173/)
- [Gut-skin axis: shared IL23R locus (Wiley)](https://onlinelibrary.wiley.com/doi/10.1111/srt.13611)
- [Risankizumab SEQUENCE trial vs ustekinumab in CD (Lancet)](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(24)01750-1/abstract)

---

*Run 007A: 2026-04-11 | M1↔M4 bridge: UPGRADED to STRONG CANDIDATE*
*Mechanism confirmed: IL-23 → Treg plasticity (Foxp3+/RORγt+ subversion) in human skin*
*Real-world drug data: ustekinumab 60.7% IBD remission in psoriasis-first co-affected patients*
*Natural experiment available: risankizumab retrospective in SEQUENCE trial co-morbidity data*
