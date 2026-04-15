# attempt_001 — The Demodex Ocular Axis: Anterior Blepharitis, MGD, Chalazion

> Scope: how three clinically-separate eyelid entities share one upstream
> driver. Establishes the mechanistic backbone for attempt_002 (tea tree
> oil evidence synthesis).

---

## Species partitioning on the eyelid

The eyelid hosts both Demodex species in distinct niches:

| Species | Size | Location on eyelid | Substrate | Associated disease |
|---------|------|--------------------|-----------|---------------------|
| *D. folliculorum* | 300–400 µm | Lash follicle, head-down, 2–6 mites/follicle in disease | Follicular keratinocytes, sebum | **Anterior blepharitis** (cylindrical collarettes) |
| *D. brevis* | 150–200 µm | Meibomian gland duct + acinus | Meibum (modified sebum) | **Posterior blepharitis / MGD**, **chalazion** |

D. brevis is the harder one to detect clinically because it sits deeper. It
also has a longer reproductive cycle (~18 days vs ~14 for D. folliculorum)
and tolerates the meibomian gland's thermal gradient. D. brevis infestation
is specifically associated with MGD and chalazion in multiple case-control
series (Liang 2014 — 69% of pediatric chalazion vs 20% of controls; Kabataş
2017 — D. brevis found in 67% of chalazion specimens on confocal microscopy).

## The cylindrical collarette — the clinical signature

A lash pulled from an uninfested follicle is clean at its base. A lash
from a Demodex-infested follicle has a cylindrical waxy sleeve (the
"collarette") wrapped around the basal 1–2 mm. This is:

- Mite cuticle fragments, mite feces, and follicular keratin
- **Pathognomonic** for Demodex when present (Gao 2005 Ophthalmology)
- Visible on slit-lamp at 25× or higher; easy to miss at routine exam
- Present on 60–100% of lashes in symptomatic Demodex blepharitis

Absence of collarettes does not rule out Demodex (especially D. brevis in
MGD/chalazion, which does not produce visible lash-base signs). Presence is
near-conclusive.

## Why the three entities co-occur

```
Upstream:
    Demodex density ↑ on lid margin
    ↓
    Mixed D. folliculorum (superficial) + D. brevis (deep)
    ↓
Three downstream expressions, often in the same patient:

    1. D. folliculorum at lash base
       → mechanical irritation + B. oleronius release (when mites die)
       → TLR4 / TLR2 / Dectin-1 activation on lid-margin keratinocytes
       → NF-κB → IL-8, IL-1β, KLK5
       → anterior blepharitis (itching, crusting, collarettes, lash loss)

    2. D. brevis in meibomian gland duct
       → mechanical obstruction of gland outflow
       → meibum stagnation + bacterial colonization (Staph, Cutibacterium)
       → lipase-mediated meibum hydrolysis → free fatty acids
       → MGD: lid-margin telangiectasia, foamy meibum, gland dropout
       → evaporative dry eye (tear film instability)

    3. D. brevis in acinar lumen + residual obstruction
       → gland rupture or persistent plugging
       → meibum extravasation into periglandular tissue
       → lipogranulomatous inflammation (chronic, sterile)
       → chalazion (firm, painless nodule)
```

The three can present alone or together. When a patient has refractory
chalazion + dry eye + itching + rosacea skin, this is not four separate
problems — it is four expressions of one infestation, amplified by host
factors.

## Host factors that elevate density

1. **Age.** Demodex prevalence is 0% in young children and approaches 95%
   by age 70 (Post 1963, Forton 2012). Density climbs throughout
   adulthood. Most clinically significant infestation is in adults >40.

2. **Rosacea.** Demodex density on the face is ~10× higher in rosacea
   patients (10–18/cm² vs 0.7–1.5/cm² controls, Forton 2012). Because the
   ophthalmic branch of the trigeminal nerve innervates both eyelid and
   central face, and because meibomian glands are homologous with
   sebaceous glands, ocular and cutaneous rosacea co-occur in 60% of
   cases (Two 2014). Rosacea patients with eyelid symptoms should be
   assumed Demodex-positive until proven otherwise.

3. **Androgens / sebum output.** Demodex feeds on sebum. Anything that
   increases sebum — puberty, androgens, high-GI diet, insulin resistance
   — feeds mite density. This is the same mechanism tying T1DM and other
   insulin-elevating states to rosacea + blepharitis (cross-link to
   `../dysbiosis/results/protocol_integration.md` M5 diet arm).

4. **Ocular surface IgG defect / mucosal immunity.** Chronic ocular surface
   inflammation (Sjögren's, graft-vs-host, atopic kerato-conjunctivitis)
   lowers the mite-density threshold for symptomatic disease.

5. **Topical steroid use on the face or lids.** Prednisolone drops,
   topical steroids for dermatitis, chronic antihistamine eye drops — all
   reduce local immune surveillance and allow Demodex blooms.

6. **Immunosuppression.** HIV, chemotherapy, immunosuppressants — all
   associated with explosive Demodex proliferation (demodicosis), often
   with secondary rosacea-like facial dermatitis.

## The *Bacillus oleronius* bridge

`../dysbiosis/numerics/run_046_demodex_rosacea_nlrp3.md` established that the
rosacea immune response is directed against *Bacillus oleronius*, the
endosymbiont gram-negative bacterium inside Demodex. The same bridge
applies on the eyelid:

- Demodex dies in the follicle or gland → cuticle ruptures → *B. oleronius*
  LPS and peptidoglycan released
- B. oleronius LPS → TLR4 on keratinocytes and lid-margin dendritic cells
  → NF-κB → NLRP3 priming + IL-8
- B. oleronius peptidoglycan → NOD1/NOD2 → RIP2 → K⁺ efflux → NLRP3
  activation (Signal 2)
- Result: the same dual-signal inflammasome activation that drives rosacea
  skin also drives blepharitis symptoms

Clinically: patients seropositive for anti-B. oleronius IgG have higher
rates of both facial rosacea and ocular rosacea / blepharitis (Lacey 2011).
The eyelid is not a separate immunological compartment — it is
mechanistically the same organ as facial skin with a different anatomic
substrate (meibomian gland instead of facial sebaceous gland).

## Why chalazion recurs despite "treatment"

Standard chalazion management:

1. Warm compress (10 min 4×/day)
2. Lid massage
3. If persistent: intralesional triamcinolone or incision & curettage

None of these steps address Demodex. The chalazion is drained or
steroid-dissolved, but:

- Demodex density at the lid margin is unchanged
- Adjacent meibomian glands remain colonized
- New chalazia appear on the same or adjacent lashes within months

This is the signature of treating the downstream lesion without breaking
the upstream loop. Gao 2007 and Liang 2018 both report substantial drops in
recurrence when tea tree oil lid hygiene is added to standard chalazion
management. The intervention is acaricidal, not anti-inflammatory — the
inflammation resolves on its own once the substrate (mite + endosymbiont
burden) is reduced.

## Open questions (for gap.md)

1. Why does chronic lid-margin inflammation NOT predict chalazion in most
   patients? The rosacea → ocular rosacea → MGD → chalazion path has
   variable penetrance. What host factor gates chalazion specifically?
   (Candidate: MMP-9 activity, lid-margin blood flow, lymphatic drainage.)

2. Does D. brevis density in the meibomian gland predict chalazion
   recurrence better than D. folliculorum density at the lash base? Could
   stratify patients into "anterior-dominant" (TTO lid scrub responsive) vs
   "posterior-dominant" (may need meibomian gland expression + TTO gel
   vs oral ivermectin).

3. What is the true Demodex-attributable fraction of "idiopathic"
   chalazion? The existing data suggests ≥60% but is not population-level.

4. Does the *B. oleronius* seropositivity test (research use only) have
   any clinical role? Could predict severe-disease phenotype and guide
   acaricidal-therapy duration.

5. Can meibography (infrared imaging of meibomian gland architecture) be
   used to track acaricidal-therapy response and guide maintenance
   dosing? Meibomian gland dropout is irreversible — early intervention
   matters.

---

*Filed: 2026-04-15 | attempt_001 in medical/blepharitis/ | Cross-links: dysbiosis/run_046, POD/attempt_005*
*Next: attempt_002 — tea tree oil / terpinen-4-ol evidence synthesis*
