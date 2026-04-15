# Patient-Zero Actionability Audit — 2026-04-14 (iteration 3)

> Phase 0 re-check (sibling note) named the current binding constraint as
> *execution of the decisive test* — IFN-α2 Simoa + T-index panel + physician
> review. This audit asks a concrete question: are the patient-facing
> execution artifacts actually ready, or do they lag the framework?

---

## Files audited

| File | Lines | Last updated | Role |
|------|------:|--------------|------|
| `medical/PATIENT_ZERO_SCREENING.md` | 141 | 2026-04-09 | 12-disease CVB screen; 4-tier panel |
| `medical/PATIENT_ZERO_TIMELINE.md` | 330 | 2026-04-09 | month-by-month protocol trajectory |
| `medical/FOR_YOUR_DOCTOR.md` | 128 | 2026-04-09 | 60-second pitch + lab list + monitoring schedule |
| `medical/t1dm/patient_zero_lab_order.py` | 206 | 2026-04-09 | reportlab script → 3-tier lab PDF |
| `medical/t1dm/patient_zero_protocol.py` | 284 | 2026-04-09 | protocol steps PDF |
| `medical/dysbiosis/results/protocol_integration.md` | 6250 | 2026-04-14 | canonical framework protocol (ref) |

Finding 1: **five days of divergence.** Since 2026-04-09, 0 commits touched
patient-zero files. In the same 5 days, the dysbiosis loop committed runs
148–170 + associated protocol_integration updates (~15 commits). The
mechanistic side kept generating; the execution side froze.

---

## Content divergence

The canonical protocol (protocol_integration.md) defines the decisive
measurement as the **T-index panel**: Node A (Tregs), Node B (CRP/TNF-α),
Node C (I-FABP — intestinal barrier damage), Node D (IFN-α proxies —
specifically Simoa ultra-sensitive assay), Node E (Th17), Node F (cortisol),
plus ferritin and optional OPN.

Grep across all 5 patient-facing files:

- `I-FABP` → 0 matches
- `IFN-α2 Simoa` / `Simoa` → 0 matches
- `Node A`/`B`/`C`/`D` (the T-index framing) → 0 matches
- `T-index` → 0 matches

The framework's decisive test is absent from every document that the patient
would actually hand to a physician. Specifically:

| Required by decisive test | In patient-facing docs? | Gap |
|---------------------------|:------------------------:|-----|
| I-FABP (Node C) | No | barrier damage not measurable |
| IFN-α2 Simoa (Node D) | Partial — generic "IFN-α" in SCREENING/lab_order; not Simoa assay | cannot separate chronic low-grade IFN-α from acute spikes |
| HLA genotype | No | cannot stratify "rosacea risk beyond HLA" per decisive test |
| Treg flow CD4+CD25+FOXP3+ | SCREENING Tier 4 only; not in FOR_YOUR_DOCTOR | doctor won't order if not in pitch |
| Ferritin (iron-Fenton) | SCREENING Tier 1; not in FOR_YOUR_DOCTOR pitch | doctor won't order if not in pitch |
| OPN (M1-Treg displacement) | No | optional per protocol, entirely missing |

The doctor-facing pitch (FOR_YOUR_DOCTOR.md) would produce C-peptide +
HbA1c + standard CMP + troponin/BNP + Vit D + CVB serology. That is a
reasonable T1DM-with-CVB-curiosity workup, but it is NOT what the
framework says to measure.

---

## Cross-file coherence

The 4 patient-facing lab lists (SCREENING, lab_order.py, FOR_YOUR_DOCTOR,
T-index in protocol_integration) do not agree with each other:

| Test | FOR_YOUR_DOCTOR | SCREENING | lab_order.py | T-index |
|------|:-:|:-:|:-:|:-:|
| C-peptide (fast + stim) | ✓ | ✓ | ✓ | — |
| HbA1c | ✓ | ✓ | ✓ | — |
| hs-CRP | ✓ | ✓ | ✓ | ✓ (Node B) |
| hs-troponin I / BNP | ✓ | ✓ | — | — |
| 25-OH Vit D | ✓ | ✓ | ✓ | — |
| GAD65 / IA-2 / ZnT8 | — | ✓ | ✓ | — |
| hs-troponin I / BNP | ✓ | ✓ | — | — |
| IFN-α (generic) | — | ✓ | ✓ | — |
| **IFN-α2 Simoa (specific)** | — | — | — | ✓ |
| **I-FABP** | — | — | — | ✓ |
| Zonulin | — | — | ✓ | — |
| D-lactate | — | — | ✓ | — |
| Treg flow | — | ✓ (T4) | — | ✓ (Node A) |
| Ferritin | — | ✓ | — | ✓ |
| CVB nAb / VP1 | ✓ | ✓ | ✓ | — |
| **HLA genotype** | — | — | — | (implicit) |

Each document was internally reasonable at its date, but they were not
reconciled. A physician reading FOR_YOUR_DOCTOR.md would order a
smaller set than a patient who hands over the SCREENING PDF. Neither is
the T-index. All three diverge from the canonical protocol.

---

## What the Phase 0 finding looks like, concretely

The Phase 0 re-check named the wall as "execution + measurement, not more
mechanism." Evidence from this audit:

1. **5-day freeze** on the patient-facing execution layer while mechanism-side
   generated 20+ runs. The loop's implicit routing is "add runs" not
   "update execution artifacts."
2. **The decisive test is not orderable** — it exists only in
   protocol_integration.md, not in any doctor-facing / patient-facing /
   lab-order artifact.
3. **Three incompatible lab panels** exist side-by-side. Under execution
   pressure (patient at a physician's office with 15 minutes), one of
   them would be used; it would not be the T-index; the framework's
   decisive prediction would therefore not be tested.

This is exactly the v7 behavioral-wall pattern: the mechanism exists, the
test exists on paper, and the wall is the handoff to the patient's
recurring-action system. The method was climbing the mechanism mountain
well past the point where the binding constraint had moved to execution.

---

## Concrete next steps (if the user picks this direction)

1. **Single source of truth for the lab panel.** Either SCREENING.md, the
   lab_order.py PDF, or FOR_YOUR_DOCTOR.md — pick one and have the
   others reference it. Add: I-FABP, IFN-α2 Simoa (specify Simoa, not
   generic IFN-α), HLA genotype, explicit Treg flow, ferritin, OPN.

2. **Doctor-pitch alignment.** FOR_YOUR_DOCTOR.md is the binding document
   for the 15-minute encounter. It needs the T-index items embedded,
   with the same "what each test is for" justification style it already
   uses. The current pitch is good; the content is out-of-date.

3. **Decision matrix re-alignment.** patient_zero_lab_order.py has a
   C-peptide decision matrix. Good primitive. Needs corresponding matrices
   for IFN-α2 Simoa (low = CVB not active; high = CVB mechanism dominant)
   and I-FABP (normal = barrier OK, skip barrier arm; elevated = barrier
   first). Without these, the measurements are collected but unused.

4. **Update latency policy.** When protocol_integration.md adds a decisive
   biomarker, a patient-facing document should update within the same
   commit — otherwise the framework's sharpest predictions never reach
   the layer that matters. This is the v5 Convention Beats Instruction
   move: make it structural (pre-commit hook flagging unreferenced new
   biomarkers) rather than operator-vigilance.

---

## Status against the original loop items

- Item 1 (standing wave): done; consolidator see-through on runs 150–170.
- Item 2 (trinity audit): done; admission filter, not convergence.
- Item 3 (Phase 0 re-check): done; wall has shifted to behavioral.
- Iter 2 (drift timeline + cross-directory): done; intensive + extensive
  shapes of the same structural failure.
- Iter 3 (this note, patient-zero actionability): done; behavioral wall
  is concretely observable as 5-day freeze on the execution layer +
  decisive test not present in any orderable document.

The natural stop point: further expansion produces diminishing returns on
the same finding. The binding action is no longer analysis — it is to
update the patient-facing layer to match the framework's current decisive
test. That is outside the method's core competence (it's patient-physician
coordination work) and should be handed off rather than looped on.

---

*Filed: 2026-04-14 iteration 3 | Patient-zero actionability audit | Sigma v8*
*Companions: standing_wave_150_170.md, phase0_recheck_2026-04-14.md, cross_directory_drift.md, confirmation_bias_audit.md*
*Does not modify patient-facing files — that is the operator's call, since it affects what a real physician will see*
