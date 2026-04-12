# Attempt 004 — M3 CVB Persistence → T1DM
## Mountain 3 — Virome dysbiosis

---

## Mountain
M3 — CVB 5'UTR-deleted persistent form → T1DM initiation and maintenance

## Hypothesis
A non-cytolytic, 5'UTR-deleted Coxsackievirus B variant persists in pancreatic islet beta cells in a subset of T1DM patients. This persistent infection drives chronic IFN-α production, beta cell stress, and islet inflammation that maintains the autoimmune destruction cycle beyond the initial viral trigger.

## Evidence Base (from numerics)
- `run_001_kill_matrix.md`: P3.1 (CVB in T1DM islets) = 2/3 FOR; P3.2 (EBV-MS 3/3 — strongest causal evidence in field)
- `run_002_m3_detection_stack.md`: detection stack; IFN-α as best proxy; TinyHealth FASTQ = no CVB info
- `run_004_m3_ifn_test_design.md`: IFN-α2 Simoa protocol; CXCL10 → Simoa → ISG panel cascade

## Mechanistic Chain
```
Acute CVB infection (childhood) → standard immune clearance → MOST people clear it fully
                                                              ↓
In genetically susceptible subset (HLA-DR3/4 + viral factors):
CVB 5'UTR deletion event → non-cytolytic variant persists in islets
     ↓
Persistent dsRNA (replication intermediate) → MDA5/RIG-I → chronic IFN-α
     ↓
Beta cell stress (IFN-α → ER stress → unfolded protein response → apoptosis)
Beta cell antigen exposure → islet-autoreactive T cell priming/maintenance
     ↓
Progressive insulitis → T1DM onset + maintenance
```

## Kill Test
**Kill criterion A:** IFN-α2 Simoa assay shows NO elevation in T1DM patients vs controls. (Would suggest CVB persistence is not producing a detectable IFN response in most T1DM patients.)

**Kill criterion B:** DiViD-scale study with virome-enriched sequencing shows CVB detection rates equal in T1DM vs matched controls.

**Status: PARTIALLY TESTED (VP1 IHC: 2/3). IFN-α2 Simoa: NOT TESTED for this user.**

## Supporting Predictions
1. Declining IFN-α2 over time correlates with C-peptide preservation (beta cell preservation) → validates that CVB suppression = beta cell benefit
2. OSBP inhibition (Protocol component) specifically reduces IFN-α2 (blocks cholesterol delivery required for CVB replication)
3. EBV co-infection elevates IFN-α2 further → combined CVB+EBV → higher IFN signature

## Evidence FOR: 2/3
VP1 IHC in islets: 30-60% T1DM vs 5-15% controls. Kallionpää 2019: IFN-α signature precedes T1DM onset. Richardson 2021: IFN-α gene expression in T1DM islets. EBV-MS (Bjornevik 2022) establishes that viral persistence → autoimmunity is a real mechanism pattern.

## Evidence AGAINST: 1/3
CVB detection rate in islets is ~40-50% in T1DM — which means 50-60% of T1DM patients show NO CVB. Either CVB is one of several routes to T1DM, or detection methods miss it in the other cases. Not all T1DM is CVB-driven.

## Current Status
[x] ACTIVE — strengthening but not fully confirmed

## Stall Point
The missing measurement is a monitoring assay. We can detect that IFN-α signature is elevated at diagnosis, but we cannot track CVB persistence over time without repeated pancreatic biopsies. IFN-α2 Simoa is the proxy for monitoring, but it hasn't been validated as a CVB-specific signal vs other viral triggers.

## Sky Bridge
SKY BRIDGE: M3 (CVB) ↔ M7 (P. gingivalis Th17) — see `attempt_002_m3m7_co_conspiracy.md`

## Next Action for Theory
1. Order CXCL10 serum → if elevated, proceed to IFN-α2 Simoa — this converts the CVB protocol from blind to monitored
2. Literature: are there published IFN-α2 Simoa measurements in T1DM cohorts? What are typical levels at diagnosis vs healthy controls?
3. If IFN-α2 elevated at baseline: serial measurement every 6 months would be the first longitudinal CVB monitoring data for this case

---
*Attempt filed: 2026-04-11 | Instance: numerics (Phase 1 deposit)*
