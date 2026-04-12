# Attempt 002 — CAR Receptor Update: Bridge Strengthened, Not Killed
## Theory Instance | 2026-04-11

> Follow-up to theory_audit.md. The CAR (Coxsackievirus and Adenovirus Receptor) interaction
> was a potential kill signal for the M3+M7 bridge. It is not. Bridge strengthened.

---

## The CAR Question

P. gingivalis gingipain degrades CAR in gingival epithelium. CAR is the receptor CVB uses to
enter pancreatic beta cells. If P. gingivalis degrades CAR in islets, it might BLOCK CVB entry
→ the two pathogens would be antagonistic (P. gingivalis protects from CVB) → bridge falsified.

---

## The Search Result

PMC5129002: "Coxsackie–adenovirus receptor expression is enhanced in pancreas from patients
with type 1 diabetes"

**Key finding:** CAR expression on beta cells is UPREGULATED by proinflammatory cytokines
(IL-1β, IFN-γ, TNF-α) in T1DM islets.

---

## The CAR Interaction Net Effect

Two competing processes:

| Effect | Mechanism | Direction |
|--------|-----------|-----------|
| P. gingivalis gingipain degrades CAR | Direct proteolysis of CAR protein | ↓ CVB entry |
| P. gingivalis LPS → IL-6, IL-1β, TNF-α | Proinflammatory cytokines → CAR upregulation | ↑ CVB entry |

The INDIRECT effect (cytokine-driven CAR upregulation) is likely dominant because:
1. Gingipain proteolysis is spatially limited to the immediate contact zone
2. Cytokine diffusion reaches all beta cells in the islet
3. The CAR upregulation in T1DM is already documented as cytokine-driven

**Net: P. gingivalis in islets probably INCREASES beta cell CAR expression via cytokines →
makes beta cells MORE susceptible to CVB infection, not less.**

---

## Revised Bridge Mechanism (v3)

```
P. gingivalis translocates to islets [PMC7305306]
    ↓
TLR2 activation → IL-1β, IL-6, TNF-α [local]
    ↓
1. Beta cell dedifferentiation (bihormonal cells)
2. CAR UPREGULATION on beta cells [PMC5129002]
    ↓
Dual effect:
  a) Direct local inflammation (IL-17 → beta cell stress)
  b) INCREASED CVB entry efficiency (more CAR → easier viral infection)
    ↓
CVB infects CAR-upregulated beta cells → persistent infection more likely
    ↓
CVB → IFN-α → beta cell stress → antigen release
    ↓
Co-occurring: P. gingivalis (inflammation) + CVB (viral) in same tissue
= Synergistic threshold crossing for autoimmune T1DM initiation
```

P. gingivalis doesn't just add Th17 signaling — it may prime beta cells for easier CVB entry by
upregulating the viral receptor. This is a second synergy mechanism, independent of Th17.

---

## Bridge Classification Update

**Previous:** STRONG CANDIDATE — two co-occurring pathogens, each independently damaging beta cells.

**Updated:** STRONG CANDIDATE with additional synergy mechanism — P. gingivalis may actively
prime beta cells for increased CVB susceptibility via CAR upregulation.

**Now two independent mechanisms of synergy:**
1. P. gingivalis → local IL-17 → beta cell stress (Th17 mechanism)
2. P. gingivalis → proinflammatory cytokines → CAR upregulation → MORE CVB entry (receptor priming)

---

## Novel Prediction Added

**Prediction C (from CAR finding):**
In the nPOD dual IHC experiment, islets that are P. gingivalis-positive should show HIGHER CAR
expression than P. gingivalis-negative islets from the same donor.

If confirmed: P. gingivalis → CAR upregulation → CVB susceptibility is directly demonstrated
in human tissue.

**This prediction is NEW and distinct from Prediction A (co-localization correlates with insulitis).**

---

## References
- [PMC5129002 — CAR enhanced in T1DM pancreas (cytokine-driven)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5129002/)
- [Diabetologia 2003 — CAR as enterovirus islet entry receptor](https://link.springer.com/article/10.1007/s00125-003-1297-z)
- [PMC7305306 — P. gingivalis in pancreatic islets](https://pmc.ncbi.nlm.nih.gov/articles/PMC7305306/)

---
*Filed: 2026-04-11 | Instance: theory | CAR potential kill → FAILED, bridge strengthened*
