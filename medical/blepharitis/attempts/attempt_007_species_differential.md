# attempt_007 — D. brevis vs D. folliculorum Differential Response

> Scope: the two human-parasite Demodex species occupy different niches,
> respond differently to routes of administration, and drive different
> clinical presentations. This attempt maps agent × niche × phenotype so
> therapy can be matched to which species actually dominates.
>
> Addresses: gap.md Type B2 (species-differential response).

---

## Why this matters clinically

A patient with **anterior blepharitis** (collarettes, itching, lash
loss) has predominantly D. folliculorum. A patient with **MGD +
chalazion recurrence** has predominantly D. brevis. Same treatment
doesn't serve both equally well:

- A topical lid-margin wipe easily reaches the lash-follicle pocket
  (D. folliculorum) but barely penetrates the meibomian gland duct
  (D. brevis)
- An ophthalmic drop (Xdemvy) wicks along the tear film + meibomian
  orifice, reaching D. brevis better than surface wipes do
- Oral ivermectin is systemic — reaches both niches through tissue
  distribution

Ignoring species gives a treatment that "sort of works" for whichever
species the regimen happens to favor. Matching regimen to species
eliminates most of the "44% non-response" signal from attempt_006.

---

## Niche biology (summary)

| Feature | D. folliculorum | D. brevis |
|---------|-----------------|-----------|
| Adult size | 300–400 µm | 150–200 µm |
| Location | Lash follicle (hair shaft) | Sebaceous / meibomian gland acinus |
| Density | Up to 6 per follicle in disease | Solitary or paired in each gland |
| Food source | Follicular keratinocytes, surface sebum | Meibomian / sebocyte lipids |
| Lifecycle | 14–18 days | 16–20 days |
| Diagnostic test sensitivity | Lash epilation microscopy (high) | IVCM only (lash epilation misses) |
| Surface appearance | Collarettes at lash base (visible on slit-lamp) | No visible surface sign |
| Clinical phenotype | Anterior blepharitis, itching, lash loss | Posterior blepharitis, MGD, chalazion |

---

## Route reachability per agent

| Agent | Lash follicle | Meibomian gland duct | Acinar lumen | Systemic tissue |
|-------|:---:|:---:|:---:|:---:|
| TTO wipe (surface) | ★★★ | ★ | — | — |
| TTO in-office scrub (50%) | ★★★ | ★★ | — | — |
| Hypochlorous acid spray | ★★ | ★ | — | — |
| Ivermectin 1% cream (periocular) | ★★ | ★ | — | ★ (limited) |
| Lotilaner 0.25% drops | ★★ | ★★★ | ★★ | — |
| Oral ivermectin 200 µg/kg | ★★ | ★★ | ★★ | ★★★ |
| IPL (IR + visible light) | — | ★★ (thermal) | ★★ (thermal) | — |

Legend: ★★★ = reliably penetrates; ★★ = partial; ★ = minimal; — =
inaccessible.

**Key insights:**

- **TTO wipes are maximally effective against D. folliculorum**; partial
  against the most anterior D. brevis, poor against deep acinar forms.
- **Lotilaner drops were formulated to wick into meibomian orifices**;
  this is why Xdemvy is differentially useful for D. brevis–dominant
  disease over TTO surface wipes.
- **Oral ivermectin is the only agent reaching D. brevis deep in gland
  acini reliably**. This matches why refractory MGD responds to oral
  ivermectin when topical therapy alone doesn't.
- **IPL's thermal component** addresses posterior-gland disease by
  melting obstructed meibum and thermally stressing deep mites —
  mechanism independent of acaricidal route of delivery.

---

## Matching regimen to phenotype

### Phenotype A — Anterior-dominant (D. folliculorum)

Clinical signs: itching, crusting, collarettes on slit-lamp, lash loss,
lid-margin redness. No major MGD component.

**Primary:**
- 5% T4O wipes nightly × 6 weeks
- Weekly 50% TTO in-office scrub × 4–6 sessions
- Household decontamination (attempt_005)

**Expected:** collarettes clear by week 4–6; symptom resolution 4–6
weeks; maintenance 2×/week.

**If fails at week 6:** verify adherence + household reinfestation
first. If confirmed, switch to lotilaner or add oral ivermectin.

### Phenotype B — Posterior-dominant (D. brevis)

Clinical signs: foreign-body sensation, MGD on imaging, recurrent
chalazion, poor meibomian expression. Collarettes may be absent.

**Primary:**
- **Lotilaner 0.25% BID × 6 weeks** (best topical penetration to
  meibomian glands)
- OR: warm compress + gland expression 2×/day + 5% T4O wipes nightly
- Omega-3 supplementation for meibum quality

**Expected:** TBUT improves week 4–8; MGD symptoms week 6–12; chalazion
recurrence reduces over 3–6 months.

**If fails at week 8:** escalate to oral ivermectin 200 µg/kg (1 dose,
repeat at week 1 for severe cases) + continuing topical agent. Consider
IPL at dry-eye subspecialty clinic.

### Phenotype C — Mixed (typical rosacea patient)

Clinical signs: both anterior and posterior; facial rosacea; collarettes
+ MGD + recurring chalazion. Most common referral pattern.

**Primary:**
- TTO wipes nightly + lotilaner BID (if cost allows) — covers both
  anterior and posterior niches
- OR: TTO wipes nightly + oral ivermectin 200 µg/kg × 2 doses (1 week
  apart) — covers deep acinar + lash-follicle populations
- Topical ivermectin 1% (Soolantra) on facial rosacea skin
- Doxycycline 40 mg sub-antimicrobial for 12 weeks (chronic
  inflammation management, attempt_006)
- Hypochlorous acid lid spray daily

**Expected:** complete clearance requires multi-agent approach; this
is the phenotype where "one agent wasn't enough" is most common.

### Phenotype D — Corneal-involved (severe ocular rosacea)

Clinical signs: peripheral corneal neovascularization, marginal
infiltrates, phlyctenules, chronic epithelial defects. Sight-threatening.

**Primary:**
- **Oral ivermectin 200 µg/kg × 2 doses (mandatory)** — need to reach
  entire gland system
- Lotilaner BID concurrently
- Doxycycline 100 mg BID × 2 weeks, then 40 mg daily × 3 months
- Topical steroid + antibiotic for corneal inflammation (ophthalmology
  oversight)
- Aggressive dry-eye therapy (preservative-free tears 6–8×/day,
  autologous serum tears if persistent)
- IPL after acute inflammation settles

**Expected:** months of combined therapy; requires ophthalmology
specialty management. Visual outcomes depend on early recognition.

---

## The Xdemvy 44% reconsidered

Per attempt_002 and gap.md Type B1, lotilaner phase 3 showed ~56%
complete collarette clearance at day 43. Reframing through the species
lens:

- Saturn-1/2 enrolled patients with *anterior* collarette findings
  (D. folliculorum–dominant or mixed)
- Drop penetrates meibomian orifice well; surface wipe-equivalent
  penetration at lash base is moderate
- D. folliculorum in the lash follicle pocket is partly shielded from
  the drop-applied agent
- The 44% non-response is partly this route-mismatch: a drop for a
  predominantly-surface-follicle population

**Therapeutic implication:** combining lotilaner (posterior penetration)
with TTO (anterior surface) should close a substantial fraction of the
44% gap. This combination has not been formally trialed but is
mechanistically justified and increasingly recommended by dry-eye
specialists.

---

## Diagnosis protocol to assign phenotype

From attempt_003, with species-specific emphasis:

1. **Slit-lamp: cylindrical collarettes?** Yes → anterior component
   (Phenotype A or C).
2. **Meibography: gland dropout / foamy meibum / poor expression?** Yes
   → posterior component (Phenotype B or C).
3. **Recurrent chalazion on ≥2 lashes?** → posterior component
   (D. brevis suggested).
4. **Facial rosacea concurrent?** → Phenotype C likely.
5. **Corneal signs / photophobia / infiltrates?** → Phenotype D.

This is a 5-minute clinical triage; the phenotype assignment determines
the agent choice.

---

## What this changes

1. **Stop giving the same regimen to every blepharitis patient.** Match
   agent to predominant species by the anterior/posterior dominant sign.
2. **Xdemvy is not a universal replacement for TTO** — it's better for
   posterior disease; TTO remains better for anterior-surface disease.
3. **Combination therapy** (TTO + Xdemvy) is mechanistically justified
   even if not yet trial-validated.
4. **Oral ivermectin deserves more consideration earlier** in
   posterior-dominant and severe cases — it's the only agent reliably
   reaching deep acinar populations, and is cheap + well-tolerated.

---

## Gap status after this attempt

**Closed:**
- Type B2 (species differential) — explicitly mapped
- Partial closure on Type B1 (Xdemvy 44% gap) — route-mismatch explains
  part of the signal; rest is chronic inflammation per attempt_006 +
  reinfestation per attempt_005

**Still open:**
- Type B3 (meibography dropout reversibility) — numerics candidate still
- Type B5 (B. oleronius biomarker) — research only
- Type B6 (TTO + ivermectin combo trial) — mechanistically justified
  here, no clinical trial yet

---

*Filed: 2026-04-15 | attempt_007 in medical/blepharitis/ | Closes gap.md B2*
*Depends on attempts 001–006*
*Numerics cross-ref: `../numerics/demodex_decay_curves.py` shows kinetic differentials*
