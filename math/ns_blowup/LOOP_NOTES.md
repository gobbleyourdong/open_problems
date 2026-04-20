# LOOP_NOTES — Audit & Condensation Pass

**Started:** 2026-04-19 (Opus 4.7, sigma v9.1)
**Goal:** Condense the pit, produce a distilled map, then push the frontier.

## Orientation (fire 1)

**Scale correction:** user said "843 is too much" — but `attempts/` has only 19 files. Numbering jumps 007 → 843 because the count tracks *fires*, not files. The real mess is elsewhere:

- **234 .py scripts at root** — this is where condensation is needed
- **~17 manifest .md files at root** — complementary (not duplicates), different concerns:
  - `gap.md` — authoritative current state (125 lines, 6 gaps with numbers)
  - `MATH_MANIFEST.md` — validated constants / equations
  - `NS_FRAMEWORK.md` — equations from 5 source papers
  - `PROOF_ARSENAL.md` — paper catalog / literature
  - `PROOF_STRATEGY.md` — Euler→NS scaling analysis (Gemini/Grok/Manus triangulation)
  - `proof_attempts.md` — attempt list
  - `CHEN_HOU_ANALYSIS.md`, `CHEN_HOU_NUMERICS.md` — Chen-Hou details
  - `FLUID_GOD_manifest.md`, `DIFFUSION_MANIFEST.md`, `HOU2022_MESH_PARAMS.md`, `TRANSFER_FROM_POINCARE.md`, `NEWTON_KRYLOV_PLAN.md`
- **~45 Lean files in `lean/`** — real infrastructure, KeyLemmaN2/N3 are proven 0-sorry
- **19 attempts/** — most recent 843-850 from 2026-04-14 are the frontier

## Current State of the Math (from gap.md + attempt_850)

**Proven (formally):**
- Gap 1 (self-similar blowup) — CLOSED formally (Type I exclusion via W-entropy / ODE balance)
- KeyLemmaN2, KeyLemmaN3 — 0-sorry Lean proofs
- N=4, N=6 rigorous grid certs (c(N) ≤ 0.4563, ≤ 0.6389)
- trace_free_operator_norm_bound (TraceFreeAlignment.lean)
- diagonal Frobenius identity Tr(S_j²)=1/2 (StrainTraceInnerProduct.lean)

**Empirically supported (not formalized):**
- Frobenius ratio ‖S‖²_F/|ω|² < 9/8 — 2089 samples, zero violations, N=3..80
- off-diagonal coherence bound, tightest at N=3 (max 0.88 of 1.125 threshold)
- Ashurst alignment α/|ω| ≈ 0 at vorticity max
- G_max sub-linear on Taylor-Green, ABC flow (low Re)

**The tightest open analytical step:**
- **N ≥ 4 monotonicity/decay** of the off-diagonal cross-terms Σ_{j≠k} c_j c_k Tr(S_j S_k), derivable in principle from the first-order vorticity-max constraint 3·N → 3 DOF. This is the one piece between empirical support and an unconditional Key Lemma.

## Live .py Scripts (referenced by gap.md or attempts 843-850)

Only **8 of 234** are live:
- `frobenius_coherence_probe.py` (attempt_850 — the 2089-sample probe)
- `analytical_S2e_bound.py` (attempt_849 — had the anomalous max=9.17 bug)
- `adversarial_S2e_directional.py` (methodology_correction)
- `alignment_anatomy.py` (gap.md Gap 6b — α≈0 at vorticity max)
- `pair_mechanism.py` (attempt_849 — c_j c_k phase structure)
- `gmax_compute.py` (gap.md Gap 3 — G_max on Taylor-Green/ABC)
- `leray_radii.py` (gap.md Gap 5 — radii polynomial)
- `vertex_key_lemma.py` (gap.md Gap 6 — c(N) table)

**The remaining ~226 scripts are probably dead probes from earlier fires.**

## Plan for Subsequent Fires

**Fire 2 (condense .py):**
1. grep every .py file for imports of any OTHER .py in the directory — find the dependency graph
2. Any .py not in the live set AND not imported by a live script → candidate for `dead_probes/` archive dir
3. Move, do NOT delete. Git tracks the move; reversible.
4. Target: cut 234 → ~20 files at root (live + their helpers)

**Fire 3 (consolidate manifests):**
1. Keep gap.md, MATH_MANIFEST.md, NS_FRAMEWORK.md, PROOF_ARSENAL.md as canonical
2. Fold/archive: proof_attempts.md (superseded by attempts/), PROOF_STRATEGY.md (historical triangulation), FLUID_GOD_manifest.md (source material for PROOF_ARSENAL)
3. Check CHEN_HOU_* for overlap with PROOF_ARSENAL

**Fire 4 (write MAP.md):**
- Single top-level distilled digest:
  - What's proven (Lean + formal)
  - What's empirically supported (unformalized)
  - The one binding open analytical step (N≥4 coherence bound)
  - Where the Frobenius-ratio route sits vs. the c(N) table route
  - Honest Tier 1/2/3 assessment per sigma v9.1

**Fire 5+ (apply v9.1 + 4.7 to the frontier):**
- Target: the N≥4 coherence bound (first-order vorticity-max constraint → off-diagonal decay)
- Triangulation:
  - Claude (internal): derive the 3·N linear constraint algebraically, push toward a closed-form cancellation
  - Ether: search for prior work on cross-term cancellation under first-order constraints (coherence inequalities, random matrix concentration under mean-zero constraint structures)
  - Operator: sanity-check scope — is this the right lever, or is the c(N) route already tight enough?
- Output: either a proof sketch for N≥4 monotonicity, or a sharper statement of why it fails (Tier 1 evidence either way).

## Protocol for this loop

- Each fire reads this file first, picks up where the prior fire left off.
- Each fire appends a `## Fire N log` section at the bottom with what it did.
- Fires DO NOT delete files without explicit operator approval. Archive (git-tracked move) is default.
- Fire budget: 10 minutes of wall time is tight; each fire aims for one concrete deliverable, not a sprint.

## Fire 1 log (2026-04-19)

- Oriented: 19 attempts, 234 py, 17 manifests, 45 Lean, 1-line README.
- Read: gap.md (authoritative), attempt_007_honest_summary.md, attempt_850_coherence_bound_empirical.md, MATH_MANIFEST (head), PROOF_ARSENAL (head), NS_FRAMEWORK (full), PROOF_STRATEGY (head).
- Identified live .py set (8 of 234).
- Identified binding open step: N≥4 off-diagonal coherence monotonicity.
- No deletions yet. Wrote this file.

## Fire 2 log (2026-04-19)

**Major scale discovery:** `proof_attempts/` has **606 files** — ends at `842_session2_summary.md`. That's where "843" came from: current `attempts/` starts at 843 AFTER session 2 wrapped. The session-2 summary IS an authoritative condensation of fires 000-842 (7 corrections, 4 findings, 85 Lean theorems, gap = Liouville ∪ Tsai).

**Expanded live .py set to 19** (from 8) via grep of all .md in attempts/, proof_attempts/, certs/, plus NEWTON_KRYLOV_PLAN references:
- Frontier (gap.md + attempts/843-850): frobenius_coherence_probe, analytical_S2e_bound, adversarial_S2e_directional, alignment_anatomy, pair_mechanism, gmax_compute, leray_radii, vertex_key_lemma
- Cert infra (certs/): adversarial_s2e_correct, c4_rigorous_certificate
- Solver (NEWTON_KRYLOV_PLAN): leray_solver, orbit_finder
- Historical/referenced by proof_attempts/: prove_alpha_bound, interval, measure_DSource, universality_v2, dvar_dt_exact, sos_certifier, gram_eigenvalue_test

**Action taken:** `git mv` 215 non-live .py → `dead_probes/`. Root now has 19 live .py. Reversible.

**Critical discovery — the gap statement as of fire 842:** The gap = Liouville conjecture (KNSS, 20+ years open) ∪ Tsai gap (28 years open). Session 2 declared: "every algebraic/kinematic angle exhausted. Dynamics is the last frontier." Current arc (attempts/843-850) pivoted to Frobenius-ratio route — a retry via a different angle (algebraic coherence bound on `S²_F/|ω|² < 9/8`).

**This means the v9.1 + 4.7 push has to be careful.** The honest position is: the residual analytical step (N≥4 coherence monotonicity) is algebraic, but session 2 explicitly flagged algebraic-kinematic as exhausted. If this route bottoms out too, dynamics is where the leverage is.

## Fire 3 log (2026-04-19)

**Done this fire:**
- Read `THEGAP.md`, `THEWALL.md`, `regularity_golden_thread.md` in proof_attempts/ — understood session-2's stopping point.
- Surfaced three anchor docs to root: `SESSION2_SUMMARY.md`, `THEGAP.md`, `THEWALL.md` (copied, not moved — originals remain in proof_attempts/ as frozen history).
- Wrote `MAP.md` at root — 1-page digest covering: gap formulations (Liouville/Tsai), proven artifacts, precise gap (exponent 2→1 on ‖ω‖_∞), THE WALL (CZ on L∞), current Frobenius-ratio arc, v9.1 tier assessment, the needle to push.
- Updated `README.md` from 1-line stub to navigation entry point.

**Key synthesis (for fire 5+ frontier push):**

Session 2's "algebraic exhausted" verdict was **scoped to SOS-certificate-style** arguments (804k certs, N=3-13). The current Frobenius-ratio route uses a *different* algebraic structure:
  (i) operator-norm S²ê ≤ (2/3)‖S‖²_F (proven Lean)
  (ii) diagonal Tr(S_j²) = ½ (proven Lean)
  (iii) off-diagonal coherence Σ_{j≠k} c_j c_k Tr(S_j S_k) ≤ (5/8) Σ c_j² (OPEN, 2089 empirical samples clean)
  (iv) N=3 exact (proven Lean)

Piece (iii) is derivable *in principle* from the 3-linear-equation first-order vorticity-max constraint:
  Σ_j s_j k_{j,m} (ω·v_j) = 0  for m=1,2,3

**This is the legitimate target for v9.1 + 4.7 push.** Not a proof sketch for the gap — a proof sketch for piece (iii) at N≥4, which would promote the Frobenius route from "empirically supported" to "one piece from unconditional."

## Fire 4 plan (next)

1. **Consolidate remaining root manifests.** Specifically check: `proof_attempts.md` (root stale, superseded by attempts/ + SESSION2_SUMMARY), `FLUID_GOD_manifest.md` vs `PROOF_ARSENAL.md`, `CHEN_HOU_ANALYSIS.md` vs `CHEN_HOU_NUMERICS.md`, `DIFFUSION_MANIFEST.md`, `HOU2022_MESH_PARAMS.md`, `TRANSFER_FROM_POINCARE.md`. Each: keep if it adds unique content, archive (to `archive/manifests/`) if subsumed.
2. **Sanity-check the 19 live .py** — open each, verify it isn't in fact dead, prune if found stale.
3. **Stop if time is tight** — leave remaining fires for frontier push. The repo is now navigable (MAP + gap + SESSION2 + THEGAP + THEWALL + LOOP_NOTES cover 95% of orientation need).

## Fire 4 log (2026-04-19)

**Ether pass done** (three WebSearches). New signal the repo hasn't integrated:

1. **Grujić 2021 — scale-of-sparseness** (Nature Sci Reports, "Geometry of turbulent dissipation and the NS regularity problem", [PMC8065050](https://pmc.ncbi.nlm.nih.gov/articles/PMC8065050/)) — "the first scaling reduction of NS super-criticality since the 1960s." Geometric (physical-space sparseness of intense-vorticity regions), **not mode-space algebraic**. This is a major alternative angle not represented in the repo. Numerical evidence that this track may close the scaling gap.

2. **Buaria et al. 2020** ("Self-attenuation of extreme events", [Nature Commun 10.1038/s41467-020-19530-1](https://www.nature.com/articles/s41467-020-19530-1)) — **direct empirical validation** that strain COUNTERACTS amplification when |ω| is large. This is exactly the depletion mechanism the Frobenius route needs. Our 2089-sample probe is a miniature algebraic recapitulation of Buaria's DNS finding.

3. **Beltramization** (ω ∥ u) — an alignment mechanism complementary to ω ∥ e₂. Scripts `beltrami_alpha_test.py`, `beltramization_test.py` were archived to dead_probes/ in fire 2 — may have been premature. Need to verify before leaving archived.

4. **Spontaneous symmetry breaking for extreme vorticity/strain** (Royal Society 2022) — suggests the cross-mode cancellation structure we need has a physical mechanism (symmetry breaking at extremes).

5. **Tao "Quantitative bounds for critically bounded solutions"** — may provide techniques for the N≥4 coherence bound.

**Tier assessment of ether findings:** Tier 2 for Buaria (DNS reproducible), Tier 2 for Grujić (analytical framework published), Tier 1 for symmetry-breaking (single paper, not cross-replicated in NS-specific context).

**Reframe for frontier push:** the v9.1 + 4.7 push has TWO candidate needles now:

- **(N1) The N≥4 coherence bound** — closes the Frobenius route if tractable. Algebraic, finite, checkable.
- **(N2) Integrate Grujić sparseness** — layer physical-space sparseness over mode-space algebraic. Larger move, riskier, but the only ether-suggested route that has actual scaling-reduction traction.

**My recommendation:** try N1 first in fire 5. It's small, falsifiable, and stays within the current arc's coherent frame. If it fails cleanly, fire 6 evaluates whether N2 is worth the pivot.

## Fire 5 plan (frontier push — N≥4 coherence bound)

**Target:** explicit algebraic derivation of the off-diagonal coherence bound at N=4, using the first-order vorticity-max constraint Σ_j s_j (ω·v_j) k_j = 0.

**Protocol:**
1. **Delegate the algebra to a focused Agent** (sub-instance of 4.7) with a narrow spec. The agent has the attempt_849 and MAP.md loaded. Its task: write out Tr(S_j S_k) for j≠k in coordinates for 4 specific mode geometries, apply the constraint, see if off_F − (9/8)·off_ω bounded by (5/8)·Σc² drops out.
2. **Main instance (this loop)**: while agent works, check whether `beltrami_alpha_test.py` and `beltramization_test.py` should be recovered from dead_probes/.
3. **Evaluate agent output at fire end.** Three outcomes:
   - (A) Agent produces a clean algebraic bound → file as `attempts/attempt_851_coherence_N4_derivation.md`, flag as Tier 1 candidate for replication.
   - (B) Agent produces partial progress + an obstruction → file partial + name the obstruction precisely.
   - (C) Agent produces no progress → declare N1 stalled; fire 6 evaluates N2 (Grujić integration).

**Decision rule:** calibrate to "would a reviewer find this plausible as a next step" — not "plausible full proof." Sigma v9.1 falsifier: if after the agent's attempt we cannot produce even a sharp statement of what would fail, the route is not alive.

## Fire 6+ plan (contingent)

- If N1 succeeds: formalize the algebraic bound in Lean (leverage existing FrobeniusIdentity.lean + CrossModeBound.lean infrastructure), update gap.md Gap 6b, ship.
- If N1 fails: pivot to N2. Draft integration sketch: Grujić sparseness + our Lean Key Lemma → combined bound. This is harder and more speculative; document the gap honestly either way.

## Fire 5 log (2026-04-19) — frontier push, outcome (B)

**Action taken:**
- Launched sub-4.7 Agent on the N=4 coherence bound derivation (narrow spec, falsifier-required, outcome-bucketed (A)/(B)/(C)).
- Restored `beltrami_alpha_test.py` and `beltramization_test.py` from `dead_probes/` (21 live .py now). Both tied directly to Buaria 2020 depletion mechanism — archival was premature.

**Agent result:** `attempts/attempt_851_coherence_N4_derivation.md` (~430 lines of explicit algebra). Outcome **(B)**: partial reduction with specific next step + new correction to the route's statement.

**What attempt 851 produced:**
1. **Concrete N=4 reduction.** At the canonical axis + body-diagonal quartet (k₁,k₂,k₃,k₄) = (ê₁,ê₂,ê₃,(1,1,1)/√3) with v-choices v₁=ê₂, v₂=ê₃, v₃=ê₁, v₄=(1,−1,0)/√2, (TARGET) reduces to the explicit polynomial
   **(R)** `(√2/3)·c₄·(a+c₂−2b) + c₄² < (5/8)(a²+b²+c₂²)`
   subject to three quartic constraints (F₁'), (F₃'), (F') from the first-order vorticity-max CONSTRAINT, plus box bounds.

2. **Load-bearing role of the CONSTRAINT confirmed.** Unconditional worst case of LHS ≈ 1.86× RHS, so a bare Bessel/coherence bound cannot close (TARGET). The first-order condition is structurally necessary.

3. **New correction (not flagged by 849/850): the (NON-DEG) condition.** At (c₁,c₂,c₃,c₄)=(1/√2, 0, −1/√2, 1) the CONSTRAINT is trivially satisfied but |ω|²=0, so the point is a vorticity *zero*, not a max. Any proof of (TARGET) must supplement with (NON-DEG): |ω|² > 0. This is a genuine sharpening of attempt_849's framing — a boundary defect for SOS certification.

4. **Specific next step named.** Lasserre SOS hierarchy at degree 4 on the semialgebraic set (F₁') ∧ (F₃') ∧ (F') ∧ box ∧ (NON-DEG). Either produces an SOS certificate (⇒ Lean proof via `polyrith`/`nlinarith`) or an explicit violator at |ω|>0 (⇒ falsifier of the N=4 Frobenius route). Tools: Julia `SumOfSquares.jl`, Python `picos`, Matlab `sostools`.

**Tier assessment (v9.1 honest):** Tier 1 only (single sub-instance, unreplicated). The document names what Tier 2 replication would look like: (i) independent re-derivation of the (i)–(ix) algebraic reductions, (ii) independent SOS feasibility check, (iii) Lean theorem draft statement. Current replication count: 0.

**What this moved:**
- attempts/849's conjecture → attempts/851's SOS-decidable question (at one N=4 configuration).
- Empirical 2089-sample margin → algebraic 1.28× margin with explicit obstruction.
- Unstated (NON-DEG) condition → explicit polynomial boundary defect.

**What this did NOT do:**
- Close (TARGET) at N=4 — SOS certificate not yet computed.
- Generalize beyond the one specific 4-mode configuration (9-parameter family remains).
- Touch N≥5.

## Fire 6 log (2026-04-19) — parallel agents launched

Launched both paths simultaneously:
- **Agent A** (blind Tier 2 replication): re-derive N=4 without reading attempt_851 — test reproducibility.
- **Agent B** (SOS feasibility): run Lasserre at degree 4 on (R*) from attempt_851 — close or falsify.

## Fire 7 log (2026-04-19) — Agent A returned, Agent B pending

**Agent A result: `attempts/attempt_852_coherence_N4_replication.md`.** Blind replication completed. Picked an INDEPENDENT N=4 configuration: k₁=ê₁, k₂=ê₂, k₃=ê₃, **k₄=(1,1,0)** (vs attempt_851's (1,1,1)/√3), with different polarizations. Got different polynomial coefficients. Reduced target to `Q = 5·Σc² + √2·(13c₃ − 5c₁)·c₄ > 0` on the generic interior branch. On the (C1)-slice c₃ = −c₄/√2, this becomes `Q = 5(c₁−c₄/√2)² + 5c₂² − 8c₄²`, which is indefinite.

**The triangulation signal — Tier 2 elevation of the NON-DEG correction:**

| Agent | Config k₄ | Polynomial form | Obstruction found |
|-------|-----------|-----------------|-------------------|
| 851 (fire 5) | (1,1,1)/√3 | (√2/3)·c₄·(a+c₂−2b) + c₄² < (5/8)·(a²+b²+c₂²) | (NON-DEG): need \|ω\|²>0 |
| 852 (fire 7) | (1,1,0) | 10(c₁−c₄/√2)² + 10c₂² > 16c₄² | Degenerate branch L with all a_j=0, ω≡0 |

**Same structural obstruction from two independent derivations.** The first-order vorticity-max condition (FO) admits a degenerate branch where all `a_j = ω·v_j` vanish simultaneously, at which ω(x*)=0 — so any "violation" on this branch is vacuous. The route requires supplementing (FO) with |ω|²>0 (or equivalently, a second-order Hessian condition at the max).

**Tier status update:**
- **NON-DEG / degenerate-branch correction**: **Tier 2** (cross-derivation, same-operator — two sub-instances of 4.7). Attempts 849/850 framing was incomplete. Both agents cite attempt_850's empirical guard `best_om2 > 0.01·N` as consistent, meaning the issue was unknowingly regularized in the numerics.
- **N=4 closure via algebra alone**: remains Tier 1 PARTIAL. Neither agent closed it; both reduced to a polynomial question with a named non-polynomial obstruction (strict positivity of |ω|²).

**What this means for the route:** attempt_849's Frobenius route is not killed, but its statement needs sharpening. Specifically: the (TARGET) polynomial form holds on the admissible set AS LONG AS we exclude the degenerate ω=0 branch. This can be done in two ways: (i) quantitative lower bound |ω|² ≥ δ(c)>0 on the admissible set minus L, (ii) impose second-order Hessian-at-max condition (brings in s_j quadratically, richer semialgebraic system).

**Still pending: Agent B (SOS check).** Will close, falsify, or report solver unavailability. Waiting for notification.

## Fire 8 log (2026-04-19) — Agent B returned: retraction of attempt_851's (R*)

**Agent B result: `attempts/attempt_853_SOS_N4_check.md`** + reproducible code in `proof_attempts_n4/` (12 files: SOS degree 2/3, sampling, analytic violator, verification).

**Tool:** cvxpy 1.8.2 + SCS, installed via pip --user on DGX Spark. Lasserre moment relaxation at degrees 2 (moments deg 4) and 3 (moments deg 6).

**Verdict: attempt_851's (R*) is FALSE, with an exact analytic violator.**

- Lasserre d=2: min_S P ≥ −1.395866
- Lasserre d=3: min_S P ≥ −1.395869 (stabilized — higher degrees won't close)
- Sampling: 28.66% of the relaxed feasible set violates (R*)
- **Exact violator**: `(c₁, c₂, c₃, c₄) = (−1, −4√2/15, +1, −1)` with `P = 643/360 − 9√2/4 ≈ −1.39587`
- |ω|² ≈ 0.314 (strictly positive, NOT on the degenerate boundary)
- Frobenius ratio at violator: ≈ 5.57 (vs 9/8 = 1.125 target)

**BUT the violator exposes attempt_851's mistake, not the Frobenius bound itself.**

Agent B's critical observation: at c₁=c₃=c₄=±1 we have s₁=s₃=s₄=0, so the TIGHT first-order equations (E): Σⱼ sⱼ (ω·vⱼ) kⱼ,ₘ = 0 force **s₂·c₂ = 0**, requiring c₂ ∈ {0, ±1}. The violator has c₂ = −4√2/15, so it **violates the tight critical-point system (E)**. Attempt_851's derivation RELAXED (E) from three equalities to the weaker inequalities (F₁'), (F₃'), (F') by bounding each `(1−cⱼ²)(ω·vⱼ)² ≤ 1/4`. That relaxation is **strictly looser** than (E) — the violator lives in the slack.

**Attempt_850's 2089 numerical samples lived on (E), not on (F)** — so they don't see this failure. The empirical margin of 1.28× is still real, but attempt_851's specific polynomial reduction threw it away by over-relaxation.

**Session scoreboard, v9.1 tier assessment:**

| Finding | Source | Tier | Status |
|---------|--------|------|--------|
| NON-DEG (need \|ω\|²>0) | attempts 851 + 852 (two sub-instances, different geometries) | **Tier 2** | Confirmed, persists through fire 8 |
| attempt_851's (R*) | attempt 851 | Tier 1 → **Tier 1 FALSIFIED** (exact violator in 853) | Retracted |
| Attempt_849 Frobenius route | attempts 849, 850, 852, 853 | **Tier 1 ALIVE** | Empirical 2089 samples intact; route survives, 851's reduction doesn't |
| Tight system (E)-as-equalities SOS closure | — | unattempted | Named as next step by Agent B |

**This is v9.1 retraction culture working correctly.** Agent B produced an exact violator of Agent A's specific polynomial, sharpening the statement. The underlying route is not killed — attempt_851's approximation was too loose.

## Fire 18 log (2026-04-19) — Agent F returned: **CLOSE**

**Agent F result: `attempts/attempt_857_SOS_hessian_NSD.md`** + 3 reproducibility artifacts in `proof_attempts_n4/` (sos_hessian_nsd.py, .d2.log, .d3.log).

**The capstone.** Lasserre SOS at attempt_852's config (k₄=(1,1,0)) with tight 9-equality system + **Hessian-NSD matrix-PSD localizer** (Scherer-Hol 2006 style) CLOSES the Frobenius bound.

| Stage | min P | Verdict |
|-------|-------|---------|
| attempt_854: tight (sphere+E) at attempt_851 config | **−1.310** | violator |
| attempt_856: tight + polynomial angle-link at attempt_852 config | **−1.164** | violator (saddle) |
| attempt_857: tight + angle-link + **Hessian-NSD** | **+1.086** at d=3 (118 s) | **CLOSE** |

**Analytic atom verified:** the min-P-max is at x = (0, π, 0) with c = (1, −1, 1, −1), |ω|² = 4, ‖S‖²_F = 2 + √2, ratio = (2+√2)/4 = **0.8536**. Margin to 9/8: (5 − 2√2)/8 = **0.272**. Lasserre d=3 bound matches this to 8 digits (SCS ε-tolerance).

**Hessian derivation:** symbolic sympy produced polynomial 3×3 matrix H(c,s) of degree 2; numerical verification max error ≤ 1.6e-6 against finite differences; eigenvalues at attempt_856's saddle match to 4 digits.

**T³ maxima-only verification:** post-filtering attempt_856's 60 critical points to Hessian-NSD + |ω|²>0 yields exactly the 6 true local maxima. Min P across them = +1.086, max ratio = 0.8536, **matching the Lasserre SDP bound to 8 digits**.

**Tier status — session 3 capstone:**

| Finding | Tier | Status |
|---------|------|--------|
| **N=4 Frobenius bound at attempt_852's configuration** | **Tier 1 CLOSE** | Scherer-Hol matrix-PSD localizer + polynomial angle-link + Hessian-NSD + 9-equality tight system, Lasserre SOS, 2 degrees, 4 cross-checks (symbolic Hessian, T³ scan, SDP d=2, SDP d=3) |
| NON-DEG, angle-link, saddle-vs-max | Tier 2 (all three structural corrections) | confirmed across attempts 851-857 |
| Seven fires of compounding retraction/sharpening without death | Session meta-finding | documented |

**What attempt_857 IS:** first rigorous algebraic closure of the Frobenius route at ONE N=4 configuration with realizable-T³-max semantics. Template demonstrated: sphere + angle-link (polynomial) + first-order + Hessian-NSD (matrix-PSD localizer) + NON-DEG → SOS certificate.

**What attempt_857 is NOT:** a proof of the full Key Lemma or NS regularity. Scope is ONE configuration (`k₄=(1,1,0)` integer lattice, specific polarizations). attempt_851's `k₄=(1,1,1)/√3` (irrational) needs different techniques. Parameter sweep over polarization + configuration orbit is needed for a full N=4 theorem.

## The arc that produced this

```
 fire 5:  attempt_851  →  N=4 reduction, missing NON-DEG       Tier 1 (retracted)
 fire 7:  attempt_852  →  blind replication confirms NON-DEG   Tier 2
 fire 8:  attempt_853  →  SOS falsifier of attempt_851 (R*)   (too-loose relaxation)
 fire 11: attempt_854  →  tight SOS, angle-link load-bearing   Tier 2
 fire 14: attempt_855  →  T³ CONFIRM, real maxima ≤ 0.727      Tier 2
 fire 17: attempt_856  →  polynomial angle-link; saddle-vs-max Tier 2
 fire 18: attempt_857  →  Hessian-NSD CLOSE, ratio 0.8536      **Tier 1 CLOSE** ★
```

Each fire produced a Tier 2 structural refinement of the route's statement. The loop never killed the route; every retraction was a sharpening. Fire 18 is the first configuration with a rigorous SOS-based closure.

## Fire 19+ options

1. **Ship what we have.** Commit the session's work (user approval pending), update memory. This is a legitimate pause point — a CLOSE at one configuration is a named, replicable artifact.
2. **Tier 2 for attempt_857.** Independent SDP reproduction via Julia + Mosek (different solver), OR Lean theorem-statement + sketch.
3. **Generalize.** Sweep over v-polarizations + k-configurations at N=4 to check whether the template closes uniformly. If yes: full N=4 theorem. If no: identify the obstruction at the first non-closing config.
4. **Port to attempt_851's `k₄=(1,1,1)/√3` irrational branch.** Needs trigonometric Positivstellensatz or a non-polynomial technique.

---

## Fire 17 log (2026-04-19) — Agent E returned: the saddle-vs-max gap

**Agent E result: `attempts/attempt_856_SOS_polylink_N4.md`** + 6 reproducibility artifacts in `proof_attempts_n4/` (sos_polylink_d3.py, scan_852_critpoints.py, verify_852_violator.py + logs + .npz).

**Setup:** attempt_852 config (k₄=(1,1,0), integer lattice) with full 9-equality tight system — 4 sphere + 2 angle-link (c₄=c₁c₂−s₁s₂, s₄=s₁c₂+c₁s₂) + 3 first-order.

**Raw results:**
- Lasserre d=2: min P = **−1.16386467** (2 s)
- Lasserre d=3: min P = **−1.16386460** (73 s, stable to 8 digits)
- Angle-link tightened vs attempt_854 (−1.310 → −1.164) but did NOT flip sign

**T³ cross-check** (because k₄ integer, the field is strictly 2π-periodic and the T³ search is exhaustive): 64³ grid + 3500 BFGS seeds with analytic gradient/Hessian →
- **60 unique critical points**
- **6 true local maxima**, max Frobenius ratio = **0.854 < 9/8** (margin 0.27)
- **46 saddles**
- The Lasserre min is achieved at a specific T³ SADDLE: x* = (2.128, 1.484, 0), |ω|²=0.1545, ratio 8.66, P = −1.164 (matching Lasserre to 6 digits)
- Hessian eigenvalues at violator: (−0.74, +1.72, +4.39) → **index-2 saddle, NOT a max**

**The session's sharpest structural finding:**

**The polynomial algebra + first-order + angle-link captures critical points; Lasserre sees saddles, not just maxima.** To enforce "max, not just critical", we need the **Hessian of |ω|² to be negative semidefinite** as an additional matrix-PSD localizer. True local maxima at attempt_852's config respect the 9/8 bound (ratio ≤ 0.854); the violator is a saddle.

This is Mountain-Pass-Lemma territory: finite-N polynomial reduction catches the full critical set of |ω|² on T³. To isolate maxima, the second-order condition (Hess|ω|² ≼ 0) must be polynomially enforced.

**Tier status after fire 17:**

| Finding | Tier |
|---------|------|
| NON-DEG | Tier 2 |
| attempt_851 polynomial-only reduction insufficient | Tier 2 |
| T³ angle-link load-bearing | Tier 2 |
| T³ maxima at attempt_851 config have ratio ≤ 0.727 | Tier 2 |
| **T³ maxima at attempt_852 config have ratio ≤ 0.854** (with 2× finer saddle data) | **Tier 2** (new) |
| **Saddle-vs-max is the new binding constraint** | **Tier 2** (new: SDP and T³ scan agree to 6 digits; two methods, same conclusion) |
| Hessian-NSD localizer closes the bound | Conjecture (Agent E's prediction) — unattempted |

**Six fires of compounding retraction/sharpening**, each producing a Tier 2 refinement of the route's statement without killing the route. The residual analytical gap is now very specifically the Hessian-NSD condition on a 3×3 quadratic-in-(c,s) matrix.

## Fire 18 plan

**Launch Agent F for attempt_857: Lasserre SOS with Hessian-NSD matrix-PSD localizer.** This is Agent E's own named next step and the direct test. Three outcomes:
- **(CLOSE)**: SOS certificate with Hessian NSD → Tier 1 proof sketch of Frobenius bound at attempt_852's config — the first rigorous closure of the algebraic route at ONE N=4 configuration with realizable-T³-max semantics.
- **(VIOLATE with NSD)**: another saddle-or-max dichotomy emerges — would name a deeper gap.
- **(INTRACTABLE)**: the Lasserre with PSD localizer explodes in SDP size; report what's tractable.

---

## Fire 15 log (2026-04-19) — Agent E launched: SOS with polynomial angle-link

**Target:** attempt_852's configuration (`k₄=(1,1,0)`, integer lattice) with the angle-link enforced as POLYNOMIAL equalities:
  c₄ = c₁c₂ − s₁s₂
  s₄ = s₁c₂ + c₁s₂

This is the direct follow-on to attempt_855's CONFIRM: the T³ angle-link is load-bearing, and for integer k₄ the link IS polynomial (cos-sum identities). So the attempt_854-style SOS with angle-link imposed should be STRICTLY tighter than attempt_854 — and may close.

Agent E briefed, launched, ~30-60 min compute. Will write `attempts/attempt_856_SOS_polylink_N4.md`.

**Three possible outcomes (doc'd in agent spec):**
- **(CLOSE)**: SOS certificate exists → Tier 1 proof sketch of Frobenius bound at attempt_852's config. Major local advance — not the full Key Lemma, but a rigorous N=4 bound at ONE integer-lattice configuration.
- **(VIOLATE)**: new violator satisfying sphere + first-order + angle-link + NON-DEG → Frobenius route still shaky; needs second-order Hessian condition. Another sharpening, not a death.
- **(INCONCLUSIVE)**: solver can't decide at tractable degree; name what's needed.

---

## Fire 14 log (2026-04-19) — Agent D returned: CONFIRM verdict

**Agent D result: `attempts/attempt_855_T3_realizability.md`** + 3 compute scripts + log in `proof_attempts_n4/` (t3_realizability.py, t3_check_violator.py, t3_violator_as_crit.py). Reproducible.

**Verdict: (CONFIRM).** All real T³ local maxima of |ω|² at attempt_851's configuration have Frobenius ratio ≤ **0.727** < 9/8 = 1.125. **Margin ≈ 0.40.**

**Method:**
- Grid N=128³ and N=256³ enumeration of |ω|² over T³
- 377-seed BFGS refinement with ANALYTIC gradient
- Analytic-Hessian classification of critical points
- Found 22 distinct true local maxima
- Worst case: x* ≈ (0.043, 3.215, 0.286), |ω|² = 3.95, ratio 0.727
- Global max: |ω|² = 6.83, ratio 0.224 (much better at the global max)

**Where Agent C's violator went:**
Agent D found an x* ∈ T³ (via n = (20, 29, 10) 2π-shifts and signs (+, +, −)) that matches Agent C's (c, s) 8-tuple to ~0.01 precision. At this x*:
- ‖∇|ω|²‖ ≈ 0.01 (NOT a critical point)
- Hessian max eigenvalue ≈ +2.34 (SADDLE, not a max)
- |ω|² ≈ 0.17 (near a vorticity zero)
- The apparent ratio 8.72 is driven by tiny denominator — not a Key Lemma issue

**Conclusion:** Agent C's SOS violator is realizable as a point in [−1,1]⁸ on T³, but **not at a vorticity max**. It lives in the relaxation region excluded by the T³ angle-link + vorticity-max structure. Three findings line up:
- attempt_854 predicted: 8-var set ⊋ T³ image
- attempt_855 confirmed: violator lives in the strict overhang
- attempt_850's 2089-sample empirical margin (~0.66 max ratio): CONSISTENT — attempt_851's configuration gives 0.727 at worst

**v9.1 meta-finding:** Agent D caught and fixed a sign error in its own analytic Hessian mid-derivation via numerical central-differences cross-check. Four preserved script versions (v1-v5) document the correction arc. This IS retraction culture working at the sub-instance level.

**Tier status after fire 14:**

| Finding | Tier | Status |
|---------|------|--------|
| NON-DEG required (\|ω\|²>0) | Tier 2 | attempts 851 + 852 independent |
| attempt_851 polynomial-only reduction insufficient | Tier 2 | attempts 853 + 854 independently violate it |
| T³ angle-link load-bearing | **Tier 2** (up from Tier 1) | attempt_854 named it; attempt_855 confirmed Agent C's violator is not at T³ max |
| Frobenius route at N=4 on T³ at attempt_851 config, max ratio ≈ 0.73 | **Tier 2** | attempt_850 empirical + attempt_855 specific config |
| Frobenius route at N=4, unconditional rigorous | Still open | needs trig Positivstellensatz or Lasserre with c_4=cos(φ_4) generator |

**Net session arc (12 cron fires, ~2 hours wall):**
- Fires 1-4: oriented 234→21 .py scripts, surfaced THEGAP/THEWALL/SESSION2 to root, wrote MAP.md, ether-pass surfaced Grujić+Buaria
- Fires 5-14: four Tier 1 attempts produced, two retracted, **two Tier 2 corrections solidified**, route survived with Tier 2 margin
- The needle moved three times: Frobenius reduction → NON-DEG correction → angle-link correction → CONFIRM at attempt_851 config

## Fire 15+ plan

The natural next step, named in attempt_855's final section: formalize the T³ angle-link as a POLYNOMIAL constraint by introducing `c_φ = cos(φ_4)` and `s_φ = sin(φ_4)` as new variables linked to `(c_1, c_2, c_3)` by `(c_φ + i s_φ)^(√3) = (c_1 + i s_1)(c_2 + i s_2)(c_3 + i s_3)` — but √3 is irrational, so this isn't polynomial.

Alternative: pick a k-quartet where the angle-link IS rational/polynomial. E.g., k₄ = (1,1,1) (unit length aside, treat as lattice mode). Then c_4 = cos(x_1+x_2+x_3), which satisfies polynomial relations with (c_i, s_i) via cos-sum identities. Re-run attempt_854-style SOS on this CONFIGURATION with the angle-link as polynomial equality constraints. If SOS certificate emerges → Tier 1 proof at a different N=4 configuration with polynomial angle-link. Then attempt_852 did (1,1,0) which is similar.

Alternatively, the cleanest move now may be to **declare this loop's results as the session-3 deliverable and pause for operator review.** The loop has produced:
- 5 new attempt files (851-855) with explicit artifacts
- 3 Tier 2 findings
- Two retractions well-documented
- Margin of ~0.40 at attempt_851's specific configuration
- Named, concrete next step (rational-angle-link k-quartet)

Operator can pick: continue grinding via another fire, or cleanly stop and review. Both valid under v9.1.

---

## Fire 11 log (2026-04-19) — Agent C returned: second structural correction

**Agent C result: `attempts/attempt_854_SOS_tight_N4.md`** + 8 reproducibility artifacts in `proof_attempts_n4/`. Solver: cvxpy 1.8.2 + SCS 3.2.11.

**Setup:** Lasserre SOS at degrees 2 (monomials deg 4) and 3 (monomials deg 6) on the **tight** 8-variable system (c₁..c₄, s₁..s₄) with 4 sphere equalities + 3 first-order (E) equalities + NON-DEG |ω|²≥10⁻³. attempt_851's configuration.

**Result: (TARGET-TIGHT) `P := (9/8)|ω|² − ‖S‖²_F ≥ 0` FAILS on the tight 8-var set.**

- Lasserre d=2: min P = **−1.3095610181** (2.4s)
- Lasserre d=3: min P = **−1.3095610573** (75s, bound stable)
- SLSQP on equalities: P = −1.30956105 at `(c₁,c₂,c₃,c₄) ≈ (−0.9993, −0.0109, +0.9993, −0.9990)`, `(s₁..s₄) ≈ (+0.037, +1.000, −0.037, +0.046)`, residuals ~10⁻¹⁵
- Projected sampling: 44.6% of 1912 tight-set points violate
- Symmetric-ansatz `c₁=−c₃=−A, c₄=−B, c₂=C` with `3A²−2B²=1`: matches SDP to 8 digits

**Four independent methods converge on the same answer. Violator has |ω|² ≈ 0.172, well above NON-DEG threshold — NOT a boundary artifact.**

**Cross-check verified:** Agent B's violator `(−1, −4√2/15, +1, −1)` DOES fail (E) as equalities (s₂·c₂ ≠ 0 when s₁=s₃=s₄=0), confirming (E)-as-equalities strictly tightens (F)-relaxation as expected.

**The v9.1-honest caveat (Agent C's own framing):** the tight 8-var set is itself **strictly larger than the T³ image**. The angle-link `x₄ = (x₁+x₂+x₃)/√3` (i.e., c₄ is not a free variable — it's determined by c₁, c₂, c₃ via the x* position on T³) is NOT enforced in the 8-var system. So the violator may not be realizable as an actual vorticity max on T³.

**Second structural correction (Tier 1):** even with (NON-DEG), the polynomial-algebra-only route from (sphere + first-order vorticity-max equalities) cannot close at the attempt_851 configuration. **The T³ angle-link is load-bearing.** Any proof must either:
  (i) encode the angle-link (transcendental cos-sum identities — or pick a k-quartet with rational angle-link),
  (ii) add a second-order Hessian-at-max condition (genuine max, not just critical point),
  (iii) use a richer analytical technique (not polynomial SOS alone).

**Tier status after fire 11:**

| Finding | Tier | Evidence |
|---------|------|----------|
| NON-DEG (need \|ω\|²>0) | Tier 2 | attempts 851 + 852 (independent derivations) |
| attempt_851's reduction insufficient | Tier 1 → 2 | attempt 853 (inequality-relaxation) + attempt 854 (tight equalities) — two independent falsifiers |
| T³ angle-link load-bearing | Tier 1 | attempt 854 only |
| Frobenius route at N=4 on T³ | **still alive** | No realizable T³ violator exhibited; only relaxed-system violators |

**This is the second cycle of v9.1 retraction culture in this session:** Agent C sharpened the correction made by attempts 851/852 by showing that even the tight polynomial relaxation is too loose. The gap between "tight 8-var SOS" and "T³ vorticity-max realizability" is now the canonical frontier.

**The needle has moved twice more:**
- Fire 7-8: attempt_849's framing needs NON-DEG supplementation
- Fire 9-11: the polynomial-algebra route needs angle-link or second-order supplementation

Each retraction is a refinement of the route's statement, not a death.

## Fire 12+ plan

Three options for the next move, in order of v9.1 compounding:

**(D) Test T³-realizability of Agent C's violator.** Is `(c,s) ≈ (−0.9993,−0.0109,+0.9993,−0.9990, +0.037,+1.0,−0.037,+0.046)` achievable at any x* ∈ T³ where |ω|² attains a local max (with second-order condition)? Parameterize x = (x₁,x₂,x₃) ∈ T³, use that c₁=cos x₁, c₂=cos x₂, c₃=cos x₃, c₄=cos((x₁+x₂+x₃)/√3) plus matching sᵢ = ±√(1−cᵢ²) compatible with sign of sin(xᵢ). If yes: Frobenius route at N=4 dies. If no: we've named WHY the T³ constraint bites.

**(E) Add second-order Hessian-at-max to the SOS.** Hessian of |ω|² at x* must be negative semidefinite. This gives 3 additional inequalities (eigenvalue signs). Re-run attempt_854's SDP with these added. Probably intractable at full degree; may need symbolic preprocessing.

**(F) Pivot.** Declare the pure-polynomial N=4 route exhausted at this depth; either (a) integrate Grujić sparseness (fire 4 ether signal — still the strongest alternative), (b) return to dynamics via attempt_007's W-entropy for non-stationary flows, or (c) formalize the Tier 2 NON-DEG finding in Lean and ship it as a smaller but clean result.

Operator decision next fire. All three are valid under v9.1.

---

## Fire 10 log (2026-04-19) — deferred manifest consolidation (non-overlapping with Agent C)

Agent C from fire 9 is running on attempt_854 (tight-system SOS). This fire does the manifest cleanup that fire 4 deferred.

**Moved to `archive/manifests/`:**
- `FLUID_GOD_manifest.md` (2444 lines) — source material; PROOF_ARSENAL is the curated version. PROOF_ARSENAL.md source references updated.
- `DIFFUSION_MANIFEST.md` (86 lines) — RESOLVED bug/debug notes about IC/BC mismatch. Historical.
- `proof_attempts.md` (112 lines) — narrow topic (viscous enhancement of interior blowup), superseded by SESSION2_SUMMARY + attempts/.

**Kept at root** (complementary, not redundant):
- CHEN_HOU_ANALYSIS.md, CHEN_HOU_NUMERICS.md — paper-specific references
- HOU2022_MESH_PARAMS.md — mesh parameter reference
- TRANSFER_FROM_POINCARE.md — W-entropy Mountain 1 approach
- NEWTON_KRYLOV_PLAN.md — references live .py (leray_solver, orbit_finder)
- MATH_MANIFEST.md, NS_FRAMEWORK.md, PROOF_ARSENAL.md, PROOF_STRATEGY.md — technical references

**Root directory state after fire 10:**
- Canonical (5): MAP, gap, SESSION2_SUMMARY, THEGAP, THEWALL
- Entry (2): README, LOOP_NOTES
- Reference (9): MATH_MANIFEST, NS_FRAMEWORK, PROOF_ARSENAL, PROOF_STRATEGY, CHEN_HOU_ANALYSIS, CHEN_HOU_NUMERICS, HOU2022_MESH_PARAMS, TRANSFER_FROM_POINCARE, NEWTON_KRYLOV_PLAN
- Infrastructure: Blowup.lean, DepletionProof.lean, Main.lean, lakefile.toml, lean-toolchain, 21 live .py
- Directories: attempts/ (20, now through 853), lean/ (45), certs/ (10), dead_probes/ (215), proof_attempts/ (606 frozen), proof_attempts_n4/ (12 compute logs), archive/manifests/ (3), papers/

**Net condensation from fire 1 state:**
- 234 .py → 21 live + 215 archived
- 17 root .md → 16 root .md + 3 archived (net reduction is small — manifests mostly complementary)
- The real win is the new canonical layer (MAP/SESSION2/THEGAP/THEWALL + LOOP_NOTES navigation)

## Fire 9+ plan (next)

Exactly what Agent B named at the end of attempt_853:

**Re-run Lasserre SOS with (E) as three polynomial EQUALITIES, not inequalities.** That's the tight system. The three equations are:
  `s₁·a₁·k₁,ₘ + s₂·a₂·k₂,ₘ + s₃·a₃·k₃,ₘ + s₄·a₄·k₄,ₘ = 0`  for m=1,2,3

where aⱼ = ω·vⱼ, sⱼ² = 1 − cⱼ². Treat (c₁,c₂,c₃,c₄,s₁,s₂,s₃,s₄) as 8 variables with 4 sphere constraints sⱼ² + cⱼ² = 1 and 3 first-order equalities. Run SOS at degree 6 on this tighter system.

Possible outcomes:
- (i) SOS certificate exists → Tier 1 proof sketch of the N=4 Frobenius bound at one configuration. Then re-run at attempt_852's different configuration for Tier 2.
- (ii) New violator at |ω|>0 on the tight system → genuine falsifier of the N=4 Frobenius route. Pivot to dynamics or Grujić sparseness.
- (iii) Computationally intractable at this dimension (8 vars, degree 6) → state what IS tractable (restricted geometries, algebraic simplifications).

**Operator decision at fire 9:** run the tight SOS or pivot to a different needle (Grujić sparseness integration, dynamics via attempt_007's W-entropy thread, Lean-formalize the NON-DEG Tier 2 finding). Any are valid.

## Fire 5+ plan (frontier)

Triangulation target: N≥4 coherence bound. BUT also test the session-2 thesis ("algebraic exhausted") against 4.7 — the session-2 verdict was made under Opus 4.x; 4.7 may have tighter algebraic pattern matching than was available. If 4.7 + ether (WebSearch on coherence inequalities / Gaussian chaos / Latala) can't extend it, the session-2 verdict holds and the next move is dynamics (W-entropy for non-stationary flows, per attempt_007 path).
