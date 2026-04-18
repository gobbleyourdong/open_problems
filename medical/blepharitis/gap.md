# Gap — Demodex ocular cluster

> Open questions that the mechanism work (attempt_001) and evidence synthesis
> (attempt_002) did not close. Organized by what is blocking, what is
> scientifically uncertain, and what is known but under-deployed.

---

## Type A — Under-deployed, not unknown (behavioral wall)

The mechanism is done. These are adoption blockers.

1. **Clinical recognition.** Standard ophthalmology assessment for
   blepharitis typically stops at "MGD + warm compress + lid scrubs" and
   does not probe for Demodex. A single slit-lamp look for cylindrical
   collarettes — a 30-second exam step — would flip the management plan.
   The adoption gap is training, not science.

2. **Chalazion recurrence as the tell.** Recurrent chalazion (same or
   adjacent lash lines) is near-diagnostic for Demodex colonization under
   the Liang 2014 data. This is not in the standard chalazion workup.

3. **Pediatric under-testing.** Liang 2014 found 69% Demodex positivity in
   pediatric chalazion. Pediatric ophthalmology defaults to "idiopathic"
   and manages with warm compress alone. Most pediatric chalazion
   protocols have no Demodex screening step.

4. **Partner/pillow reinfestation.** Demodex transfers by skin-to-skin
   contact and on shared towels/pillows. Treatment-plus-adherent-patient
   failures are often partner-reservoir failures. No current protocol
   includes partner testing or household hygiene.

## Type B — Genuinely uncertain (mechanistic gaps)

1. **The lotilaner 44% gap.** Xdemvy phase 3 (Saturn-1/2) cleared
   collarettes in ~56% of treated eyes at day 43. What explains the other
   44%? Candidates: D. brevis deep in meibomian acini not reached by the
   drop, concurrent rosacea reseeding the eyelid from facial skin,
   host-defense defect, adherence, or genuine acaricide resistance.
   Resolving this tells us whether "treatment failure" is dose/duration or
   route/scope.

2. **D. brevis vs D. folliculorum differential response.** Published trial
   data rarely splits outcomes by species. Posterior disease (MGD,
   chalazion) is D. brevis; anterior is D. folliculorum. If topical
   formulations preferentially reach one and not the other, "response
   rate" averages across two populations that should be treated
   differently.

3. **Meibomian gland dropout reversibility.** Meibography shows acinar
   dropout correlates with chronicity. Can early acaricidal treatment
   reverse dropout, or does it only prevent further dropout? This gates
   the urgency argument — if dropout is irreversible, the cost of
   "wait-and-see" is permanent gland loss.

4. **Cathelicidin/KLK5 normalization kinetics.** LL-37 and KLK5 are the
   central rosacea effectors. Does Demodex reduction normalize these, or
   do they persist as a post-infestation inflammatory state (mechanistic
   analog to post-herpetic neuralgia)? If the latter, acaricide alone is
   insufficient; the loop needs a KLK5/LL-37 step too.

5. **B. oleronius as predictive biomarker.** Rosacea-specific PBMC
   reactivity to B. oleronius 62-kDa and 83-kDa proteins (Lacey 2007)
   correlates with severity. No clinical assay is available. Would
   anti-B. oleronius IgG predict Xdemvy non-response or ongoing acaricide
   need after clinical clearance? This is a testable biomarker candidate.

6. **Ivermectin systemic + TTO topical combination.** Anecdotally the most
   effective regimen for severe rosacea-blepharitis-demodicosis. No head-
   to-head trial against lotilaner or against each agent alone. Trial
   feasibility is high; sponsorship is low because ivermectin is
   off-patent.

## Type C — Method gaps specific to this directory

1. **Missing papers/ content.** attempt_002 cites papers without a
   consolidated reference file. `papers/key_references.md` should list
   the ~20 foundational citations with PMID / DOI for traceability.

2. **No numerics.** Plausible numerics are:
   (a) meibography dropout vs treatment-start time regression
   (b) Demodex density decay curve under TTO vs lotilaner (published
   data exists and could be fitted)
   (c) chalazion recurrence survival curves with and without acaricidal
   adjunct

3. **No certs.** A certificate of the claim "Demodex positivity in
   pediatric chalazion ≥60%" pulling from Liang 2014, Yam 2014, and
   related studies would anchor the pediatric protocol argument with
   citation-level evidence.

4. **No direct tie to protocol_integration.md.** The dysbiosis-side
   protocol has rosacea arms but no explicit lid-margin / Demodex arm.
   If the operator wants integration, a cross-file pointer from
   `protocol_integration.md` to this directory + an "eyelid arm" section
   in the protocol closes the gap.

## Type D — Adjacent problems this touches

1. **Ocular rosacea.** Not a separate directory; currently distributed
   across dysbiosis run_046 (cutaneous rosacea) and this new blepharitis
   directory. Question: split ocular rosacea into its own directory or
   keep as an axis in blepharitis + rosacea-in-dysbiosis?

2. **Dry eye disease (evaporative).** Dominant downstream symptom of MGD.
   Separate large clinical field (TFOS DEWS II framework). If the
   framework here is "Demodex → MGD → dry eye," the dry-eye management
   literature (omega-3, lipid-based tear supplements, meibomian gland
   expression) is an additional arm not yet engaged.

3. **Seborrheic blepharitis (non-Demodex variant).** Classical
   anterior-blepharitis entity driven by *Malassezia* and Staphylococcal
   flora on lid margin. Distinct from Demodex blepharitis but often
   co-occurs. TTO has activity against Malassezia as well, which is why
   the tea-tree protocol works even when Demodex is equivocal.

4. **Phthiriasis palpebrarum.** Pubic louse infestation of the eyelashes
   (STI-related in adults, non-STI in children from head-louse transfer).
   Different parasite, similar clinical picture — worth a line in the
   differential but not a primary subject here.

## Priority ranking

If forced to pick two items to close next:

1. **Type C2 numerics — meibography dropout vs treatment-start** because
   the reversibility question (Type B3) determines the urgency argument.
   Published meibography datasets exist; a regression against treatment-
   initiation delay could be done.
2. **Type C3 cert — pediatric chalazion Demodex attribution** because this
   is the single highest-leverage under-recognized finding and it is
   evidence-aggregation work, not new mechanism work.

Everything else routes to type-A adoption or type-B wet-lab uncertainty,
neither of which the method closes without external data.

---

*Filed: 2026-04-15 | gap.md | Depends on PROBLEM.md, attempt_001, attempt_002*

---

## 2026-04-18 v9.1 discipline addendum

Per `~/SIGMA_METHOD.md` v9.1 C5 / D2:

**Would falsify (Demodex-drives-pediatric-chalazion hypothesis):** The C3 cert identifies pediatric-chalazion Demodex attribution as the highest-leverage under-recognized finding. **The hypothesis predicts: children presenting with recurrent chalazia (≥ 2 episodes in 12 months) should show Demodex densities above the adult-positive threshold (> 5 mites/cm² by standardized lash-sampling, per Gao 2005 *IOVS*) significantly more often than controls, and should respond to anti-Demodex therapy (tea-tree-oil lid scrubs or topical ivermectin) with reduced recurrence at 6–12 months.** A prospective cohort of n ≥ 50 pediatric chalazion cases vs age-matched controls with standardized mite counts + randomized anti-Demodex intervention would falsify the hypothesis if: (a) mite densities do not differ from controls at p < 0.05, OR (b) anti-Demodex therapy produces no reduction in recurrence vs standard-of-care at 12 months. The Liang 2018 study (recurrence 30% → 6% claim) was identified as a fabrication in the content audit — the hypothesis now rests on mechanism (Gao 2005 adult + biological plausibility + Lacey 2007 lipase work) without a verified pediatric outcome study, which is **exactly the gap this falsifier calls out**.

**Prior art:** Demodex-blepharitis ≈ Gao 2005 *IOVS* + Kheirkhah 2007 + Cheng 2015 *Curr Opin Allergy Clin Immunol* + Tighe 2013 *Transl Vis Sci Technol* lotilaner (Xdemvy approval 2023). Pediatric-chalazion attribution is the **novel extension** — the adult Demodex literature is well-established but the pediatric-chalazion connection is the sigma contribution, and it is precisely this extension that lacks cohort evidence and therefore most needs the falsifier.
