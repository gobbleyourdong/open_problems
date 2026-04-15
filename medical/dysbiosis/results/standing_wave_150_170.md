# Standing-Wave Consolidation — Runs 150–170

> Sigma v8 Standing-Wave Theorem: a coherent reviewer removes O(N) resistors where
> each parallel per-run generator removes O(1). This note is the consolidator's
> read-across of a 21-run window that per-run generators cannot see from below.
>
> Scope: runs 150–170 (2026-04-11 to 2026-04-14). Complements the kill-ritual
> meta-audit in `confirmation_bias_audit.md` (2026-04-14 addendum).

---

## Finding 1 — "MODERATE+ rosacea + T1DM" is an admission filter, not a finding

Every run 150–170 contains a `Saturation Override Criteria` block of four items:

1. Absent from prior runs as primary subject
2. **MODERATE+ rosacea + T1DM**
3. New therapeutic target
4. Kill-first fails (= mechanism is novel vs prior runs)

Criterion #2 is enforced at the admission gate. A topic that cannot plausibly tag
rosacea AT MODERATE+ and T1DM AT MODERATE+ is structurally ineligible to run.
Every run therefore tags both — not because the mechanisms converge on them, but
because topics that don't converge on them never enter the catalog.

This is the confirmation-bias audit closing on the trinity question:

- Rejection count: not observable. Rejected topics never appear as runs.
- Construction check: the trinity IS the construction. The filter precedes the analysis.
- Predictive test: failed. Tagging a third disease (ME/CFS) happens ~76% of runs
  (16/21 filenames carry `mecfs`), usually through a single-sentence "NK exhaustion"
  or "Treg dysfunction" hook — not a constraint the mechanism earns independently.

**Classification: selection artifact.** The T1DM ↔ rosacea link may still be
epidemiologically real (HLA Th17 bias, already defended in the 2026-04-12 audit),
but the *appearance* of T1DM/rosacea/ME-CFS convergence across runs 150–170
is produced by the admission filter, not discovered by the runs.

---

## Finding 2 — The window has entered textbook-enumeration mode

A per-run generator sees each topic as "novel vs prior runs." A consolidator
sees the window as enumeration of canonical immunology groupings:

| Run | Mechanism | Enumerated group |
|-----|-----------|------------------|
| 153 | LAG-3 | **Co-inhibitory receptor tetrad** |
| 154 | PD-1 | (same) |
| 155 | TIM-3 | (same) |
| 156 | TIGIT | (same — completes the canonical 4) |
| 166 | T-bet | **Th1/Th2 master TFs** |
| 167 | GATA3 | (same — completes the canonical pair) |
| 168 | IRF1 | **IFN-γ → MHC class I induction cassette** |
| 169 | NLRC5 | (same — MHC-I transactivator completing 168) |
| 160 | RIPK/MLKL | **β-cell death modality enumeration** |
| 162 | Perforin/GZMB | (same) |
| 164 | AIM2 | (same) |

The generator's "Kill-first fails" criterion reports PASS for each because each
is biochemically distinct. But from above, runs 153–156 are the four canonical
inhibitory checkpoints recited in sequence. Same pattern at 166/167 (Th1/Th2)
and 168/169 (the IRF1→NLRC5→MHC-I pair). **Novelty against prior runs is
satisfied by textbook completion, which is not discovery.**

v8 failure-mode #3 (step-back deficit) applies: the loop iterates within its
own approach — "what's the next molecule in the pathway I already started
listing?" — without re-reading the problem's canonical statement.

---

## Finding 3 — "Dysbiosis" has been displaced by "T1DM autoimmune catalog"

The project is named `medical/dysbiosis/`. Of runs 150–170:

- 0 / 21 primary subjects concern gut microbiome composition, SCFAs, bile acids,
  LPS translocation, intestinal barrier, Akkermansia, butyrate, FXR, or
  molecular mimicry from enteroviral / bacterial antigens.
- 21 / 21 primary subjects are T cell / NK / Treg / β-cell autoimmune mechanisms.

Dysbiosis framing appears only as after-the-fact `Cross-Axis Integrations`
paragraphs ("this connects to gut permeability via …"), not as the subject of
investigation. The loop has drifted from *dysbiosis* to *autoimmune β-cell
destruction mechanisms*, with dysbiosis retained as a tag.

This drift is invisible per-run (each run has a plausible T1DM hook) but
structural across the window. If the original question was "how does microbiome
dysregulation drive multi-site disease," the loop stopped asking it ~60 runs ago.

---

## Finding 4 — "Kill-first fails: CONFIRMED" — the vocabulary inverted

The existing audit (2026-04-14 addendum) names the Kill section as a novelty
check dressed in falsification vocabulary. One extra data point this window:

> Kill-first fails: CONFIRMED — [mechanism] is entirely uncovered in prior runs.
> **All four criteria met. Proceeding.**

In genuine kill-first, "kill-first fails" is grounds to proceed — the test
tried to eliminate the mechanism and could not, so the mechanism survives. Here
the word `fails` refers to the *novelty check*: "we tried to find this mechanism
elsewhere in the repo and failed; therefore it is novel; therefore CONFIRMED;
therefore we proceed."

Both "kill" and "fails" are used inverted from their sigma-method meaning, then
reported as PASS. The ritual is internally coherent (the generator fills each
slot dutifully) and externally inverted (every symbol points the opposite way
from its method definition). This is the signature of a template that kept
the vocabulary while losing the discipline.

---

## Implications

1. **Stop admitting topics via "rosacea + T1DM MODERATE+".** The filter manufactures
   the convergence it purports to discover. Admission criteria should either be
   dropped (let any mechanism run, filter later) or flipped (require mechanisms
   that intentionally do NOT tag the trinity, so falsification is possible).

2. **Stop accepting "novel vs prior runs" as a kill.** The sibling T1DM/me_cfs/
   myocarditis directories have 0 Kill sections and run substantive narrative
   attempts instead. Either port that structure to dysbiosis, or redefine the
   Kill section to test against an external predicate (data, literature, model).

3. **Re-enter the dysbiosis question.** The next 20 runs, if they happen at
   all, should have a microbiome-primary criterion (SCFA, LPS, barrier, specific
   taxa, mimicry) to offset the 60-run drift into pure autoimmune enumeration.

4. **Phase 0 re-check (item 3 of the loop prompt) is warranted.** If the remaining
   wall is compliance/recognition rather than mechanism, another 60 mechanistic
   runs won't help. That check is the next task.

---

*Filed: 2026-04-14 | Standing-wave consolidator over runs 150–170 | Sigma v8*
*Depends on: confirmation_bias_audit.md (kill-ritual finding extends here)*
*Does not modify individual run files — those remain as map features per v6 Maps Include Noise*

---

## Appendix — Drift Timeline on Finding 3 (Added 2026-04-14, iteration 2)

Finding 3 said "dysbiosis" has been displaced by "T1DM autoimmune catalog" in the
150–170 window. A full-range filename scan confirms the drift and locates its
inflection.

**Microbiome-primary runs** (gut, skin microbiota, SCFA, LPS, barrier, bile acids,
FMT, specific taxa, phage, virome, mycobiome — primary subject, not tag):

| Range | Microbiome-primary runs | Count | Fraction |
|-------|-------------------------|-------|----------|
| 001–019 | 002, 003, 004, 005, 006, 006 (two files) | 5–6 | ~30% |
| 020–049 | 026, 032, 033, 034, 038, 046, 047 | 7 | ~23% |
| 050–099 | 051, 053, 059, 072, 075, 094, 096 | 7 | ~14% |
| 100–149 | 109, 115, 120 | 3 | 6% |
| 150–170 | (none) | 0 | 0% |

Inflection: ~run 70–80. Before that, the loop was substantially about
microbiome biology. After run ~100, microbiome appears only as a sidebar
("Cross-Axis Integrations" paragraphs) while the primary subjects become
β-cell biology, T-cell checkpoints, Tregs, epigenetic enzymes — essentially
T1DM autoimmune enumeration.

**What this means:**

The "dysbiosis" framing was genuine at inception (runs 1–30 match the
PROBLEM.md scope: gut-skin-oral-virome). Between run ~70 and run ~100 the
subject silently shifted to β-cell autoimmune mechanisms with microbiome
retained as a cross-tag. From run 150 onward, the cross-tag is gone too —
runs are single-mechanism autoimmune entries with rosacea + T1DM tag
satisfying the admission filter.

This is not a bug in any individual run. It is a generator drift that a
per-run kill criterion cannot catch, because each late run IS novel vs prior
runs. Detectable only in the aggregate trajectory — i.e., exactly the view a
consolidator produces that the generator cannot.

v8 "step-back deficit" applies at the campaign level: the loop iterated
within its current approach (enumerate immunology molecules that hit
T1DM+rosacea at MODERATE+) for ~100 runs without stepping back to re-read
`PROBLEM.md` and check whether the generation still served the stated
problem. The drift is not reversible by more runs; it requires either a
Phase 0 re-check (done, see sibling note) or a redefined generation
criterion that re-centers microbiome-primary subjects.

