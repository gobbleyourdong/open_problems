# Cross-Directory Drift Check — 2026-04-14 (iteration 2)

> Scope: check whether the dysbiosis-directory drift pattern (runs 112–170 past
> saturation, kill-ritual producing 0 kills) has analogs in sibling disease
> directories under `medical/`.
>
> The existing kill-ritual audit already established that siblings have **0 Kill
> sections** because their templates differ. This note asks a different question:
> do they have their own shape of drift?

---

## Work-volume distribution

| Directory | attempts/*.md | numerics/*.md |
|-----------|--------------:|--------------:|
| t1dm | 96 | 2 |
| me_cfs | 7 | 2 |
| myocarditis | 6 | 1 |
| perioral_dermatitis | 6 | 0 |
| pericarditis | 4 | 1 |
| psoriasis | 5 | 1 |
| eczema | 4 | 1 |
| pancreatitis | 3 | 1 |
| neonatal_sepsis | 3 | 1 |
| hepatitis | 3 | 1 |
| **dysbiosis** (for comparison) | — | **170 numerics runs** |

T1DM is the second gravity well (96 attempts). All other disease nodes are
stub-sized. The repo has two centers of mass: dysbiosis/numerics (170 runs)
and t1dm/attempts (96 attempts). Every other directory has ≤ 7 files.

This explains the dysbiosis displacement finding from `standing_wave_150_170.md`
Appendix: the dysbiosis loop drifted toward T1DM autoimmune mechanisms because
T1DM is the actual center of mass of the user's clinical concern (primary
diagnosis, per `confirmation_bias_audit.md` 2026-04-12). The drift wasn't
random; it was gravitational.

---

## T1DM drift has a different shape

Recent T1DM attempts (80–96): thyroid polyglandular, celiac, Parkinson's,
LADA, IBD co-beneficiary, autonomic ganglia, month-by-month trajectory. This
is **extensive drift** — the framework being applied to a widening set of
adjacent conditions.

Spot-check of `attempt_091_ibd_cobeneficiary.md`: the attempt itself states
"IBD is NOT CVB-caused (CVB is not prominently in IBD literature as a
trigger)" — and then admits it as a "Category 2 co-beneficiary" because
shared mechanisms exist. No falsifier. No kill. Same class of failure as
dysbiosis's novelty-vs-prior-runs check, in a different vocabulary:
"mechanism overlap → protocol applicable → disease admitted."

| Directory | Drift shape | What it does |
|-----------|-------------|--------------|
| dysbiosis/numerics/ | **Intensive** | same frame, enumerate more molecules |
| t1dm/attempts/ | **Extensive** | same frame, apply to more adjacent diseases |

Both shapes share a structural property: no falsification step wired to
external data. The content differs (dysbiosis adds molecules; T1DM adds
diseases) but the failure mode is identical — generation without
discrimination.

---

## Sibling stubs (≤ 7 files)

me_cfs, myocarditis, pericarditis, pancreatitis, neonatal_sepsis,
perioral_dermatitis, psoriasis, eczema, hepatitis — these directories exist
as scaffolding but carry almost no deep analysis. Two readings:

1. **Placeholder reading:** they exist to be "covered" by references from
   dysbiosis and t1dm. The category exists in the protocol; a directory
   existing is a form of claim that the category is handled.

2. **Genuine-exploration reading:** the work was intentionally centered on
   dysbiosis + t1dm because those are the user's primary conditions. The
   others are named but not explored. No drift because no loop ran there.

The stub sizes (3–7 files each) do not support a saturation-drift claim —
there's no "past saturation" when there isn't a sustained campaign. This is
the **null case**: no drift, no output, placeholder scaffolding.

---

## Implications for the method

1. **Saturation drift wall has two shapes.** Intensive (molecule enumeration)
   and extensive (disease enumeration). Both arise from the same absence —
   no wired-in external falsifier. A v9 Method Domain Map entry should
   cover both; the "saturation drift wall" is not a single failure mode.

2. **Gravity wells predict drift direction.** When a campaign saturates, it
   drifts toward the adjacent center of mass in the repo. Dysbiosis drifted
   toward T1DM (co-located, overlapping mechanisms, user's primary
   condition). Predictive: if a future campaign in another medical
   directory saturates, it will drift toward t1dm or dysbiosis by the
   same gravitational logic — not randomly.

3. **Stubs are safe.** The ≤ 7-file directories are not drifting because
   they aren't running. If a loop is ever pointed at them, the same
   drift patterns should be expected by default and guarded against
   up-front (admission criteria that cannot be satisfied tautologically;
   kill criteria wired to external predicates).

4. **The binding intervention is the same across shapes.** Whether the drift
   is intensive or extensive, the fix is to wire falsification to external
   data: measurements, literature counterexamples from an independent-
   instance pass, predictions that can be disconfirmed. The Phase 0
   re-check sibling note names the specific external tests for this case
   (IFN-α2 Simoa + T-index panel).

---

*Filed: 2026-04-14 iteration 2 | Cross-directory drift check | Sigma v8*
*Companions: standing_wave_150_170.md, phase0_recheck_2026-04-14.md, confirmation_bias_audit.md*
*Does not modify sibling directories — they remain as the map per v6*
