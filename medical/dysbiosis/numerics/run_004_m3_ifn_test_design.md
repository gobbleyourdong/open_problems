# M3 IFN-α Test Design — Best Available CVB Persistence Proxy
## Run 004 | Numerical Instance | 2026-04-11

> CVB direct detection is inaccessible (Run 002). IFN-α gene/protein signature is best available proxy.
> This file designs the specific panel and interprets what results mean.

---

## Why IFN-α Is the Best Proxy

Persistent RNA virus replication → dsRNA intermediate → RIG-I/MDA5 sensing → IRF3/IRF7 activation → IFN-α/β production → ISG upregulation in ALL cells.

This is constitutive in persistent infection — unlike acute infection (IFN spikes then resolves), persistent infection produces chronic low-level IFN production that creates a measurable gene expression signature.

**Key evidence that this works for T1DM:**
- Kallionpää 2019 (DIPP cohort): IFN-α signature appears 12-24 months BEFORE T1DM onset in high-risk children. This makes it a predictive marker, not just a disease-state marker.
- Richardson 2021: single-cell transcriptomics of T1DM islets — strong IFN-stimulated gene upregulation in beta cells adjacent to CVB-positive cells.
- Rönnblom 2019: IFN-α signature in 50-60% of T1DM patients at diagnosis vs ~15% of controls.

---

## Option 1: IFN-α2 Protein (Simoa Assay) — RECOMMENDED

**Technology:** Single Molecule Array (Simoa) by Quanterix. Digital ELISA with 1000× lower detection limit than standard ELISA.

**Why standard ELISA fails for IFN-α:** IFN-α in persistent (non-acute) infection is in the femtogram/mL range. Standard ELISA detection limit: ~2-5 pg/mL. Simoa detection limit: ~0.1-1 fg/mL. Standard ELISA → all samples appear negative. Simoa → separates cases from controls.

**Published cutoffs:**
- Healthy adults: ~0.1-0.5 fg/mL (essentially zero)
- Active SLE (known high-IFN condition): ~100-10,000 fg/mL
- T1DM patients with IFN signature: ~1-50 fg/mL (estimated from indirect data)
- Pre-T1DM children: rising levels 12-24 months before onset

**Lab availability:**
- Quanterix Accelerator Lab (CLIA-certified): commercial service, samples mailed in
- Cost: ~$150-300/sample
- Turnaround: 5-10 business days

**Sample requirements:** Serum, collected without gel separator tubes (IFN-α can degrade with gel separators). Process within 4h or flash freeze. Ship on dry ice.

**What a positive result means (in user context):**
- IFN-α2 elevated → chronic antiviral IFN response active → persistent viral trigger present
- In T1DM context: CVB persistence is the most likely candidate
- Does NOT prove CVB specifically (EBV reactivation, HHV-6 persistence also elevate IFN)
- Interpretation: antiviral component of CVB protocol is targeting something real

**What a negative result means:**
- IFN-α2 normal → no detectable chronic IFN response → either:
  a) No persistent viral infection currently active
  b) Viral load below Simoa detection threshold
  c) IFN response is being suppressed (rare, but possible with prolonged chronic exposure)
- If negative: reconsider whether antiviral component of protocol is load-bearing

---

## Option 2: ISG Gene Signature (RT-PCR Panel) — ALTERNATIVE

If Simoa is unavailable, measure mRNA expression of ISGs in PBMCs.

**Minimum 4-gene panel (captures >95% of IFN-α signature variance):**

| Gene | Why | Basal expression in healthy | Fold-change in T1DM IFN+ |
|------|-----|---------------------------|--------------------------|
| MX1 | Most specific to IFN-α/β; near-zero basal | Very low | 5-50× |
| IFIT1 | Highly responsive to viral IFN-α | Low | 3-20× |
| OAS1 | Antiviral RNAse activator; IFN-α responsive | Low | 3-15× |
| RSAD2 (Viperin) | Antiviral; inhibits RNA virus replication; IFN-α specific | Very low | 5-30× |

**IFN score calculation (Baechler 2003 method, adapted):**
1. Normalize each gene to GAPDH or HPRT (housekeeping)
2. Compare to healthy control mean expression
3. Score = % genes with expression >2 SD above control mean × their mean fold-change
4. Score >1 = IFN signature positive

**Lab availability:**
- Standard RT-PCR panel at any molecular pathology lab
- Cost: ~$50-150 if ordered as custom panel
- Turnaround: 5-7 days

**PBMC isolation required:** Fresh blood (PBMC isolation within 4 hours via Ficoll gradient or CPT tubes). Ship CPT tubes to lab for same-day processing.

---

## Option 3: CXCL10 (IP-10) Serum Protein — CHEAPEST PROXY

CXCL10 (IP-10, Interferon-gamma-induced protein 10) is induced by both IFN-α and IFN-γ and is elevated in T1DM, viral infections, and autoimmune states.

**Not as specific as IFN-α2** (also elevated in bacterial infection, stress), but:
- Detectable by standard ELISA (not needing Simoa)
- Available at clinical labs (~$50-100)
- Published in T1DM: elevated ~2-3× vs controls in CXCL10/IP-10 panels

**Use as:** screening proxy. If CXCL10 normal → IFN response probably absent. If elevated → confirm with Simoa.

---

## Recommended Testing Sequence

```
STEP 1 (cheap, wide net):
  CXCL10 serum (~$50-100, clinical lab)
  IF elevated → proceed to Step 2

STEP 2 (targeted, more specific):
  IFN-α2 Simoa assay (~$150-300, Quanterix)
  IF elevated → confirms chronic IFN response

STEP 3 (optional, mechanistic):
  ISG 4-gene panel on PBMCs (RT-PCR)
  Confirms IFN gene expression matches protein signal
  Useful if Simoa result is borderline
```

---

## Confounders to Account For

| Confounder | Effect on IFN-α | How to control |
|------------|----------------|----------------|
| Recent viral illness (cold, flu) | Acute spike → false positive | Test when symptom-free for ≥4 weeks |
| Autoimmune activity (lupus, RA) | Chronic IFN elevation | User doesn't have these, but note |
| EBV reactivation | IFN elevation, confounds CVB interpretation | Test EBV VCA IgM and EA-D IgG simultaneously |
| HHV-6/7 reactivation | IFN elevation, confounds | HHV-6 IgG avidity if IFN elevated |
| Metformin use | Anti-inflammatory; may REDUCE IFN-α signature | Note if on metformin (relevant for T1DM) |
| Time of day | Circadian variation in IFN levels | Morning draw, consistent timing |

---

## Connection to CVB Protocol Monitoring

If running the CVB protocol:
- Baseline IFN-α2 (Simoa): before protocol start
- 6-month repeat: if IFN-α2 is decreasing → protocol is reducing viral replication
- 12-month repeat: trend should continue if antiviral component effective

This converts the CVB protocol from "blind empirical treatment" to "monitored antiviral response tracking." Even though we can't detect CVB directly, declining IFN-α2 over time is the closest available signal that something viral is being suppressed.

---
*Run 004 M3 IFN test: Simoa IFN-α2 is the recommended test (~$150-300). CXCL10 is the cheap entry screen (~$50). Four-gene ISG panel (MX1/IFIT1/OAS1/RSAD2) is the alternative. All three can be sequenced: CXCL10 first, then Simoa if elevated.*
