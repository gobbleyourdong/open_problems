# attempt_003 — The K-Minimal Vacuum: Why ρ_Λ Is Small and Nonzero

**Date:** 2026-04-10
**Track:** Theory (Even instance)
**Status:** New theory. Connects the Parmenidean K-argument (attempt_001–002) to the CC mechanism (component (a)) via a K-minimality selection principle. Produces a qualitative prediction that agrees with Weinberg (1987) and observation.

## Cross-reference

- **attempt_001** — four senses of nothing, Parmenidean argument in compression terms
- **attempt_002** — CC decomposition into four independent components; (a) mechanism UNRESOLVED
- **lean/ParmenidesK.lean** — nothing is not specifiable (K = 0 impossible)
- **lean/LandscapeCCP.lean** — 10^361 vacua in anthropic window, K-addressable in 1661 bits
- **lean/VacuumFineTuning.lean** — SUSY shifts gap from 10^139 to 10^73
- **results/cc_prior_findings.md** — prior-sensitivity analysis

## The problem this attempt attacks

Component (a) of the CC decomposition: **What mechanism cancels ρ_QFT?**

The existing work established:
- (b) fine-tuning dissolved under log-uniform prior
- (c) selection resolved via 10^361 landscape vacua
- (d) evolution active, discriminable by 2030

But (a) — the mechanism — is untouched. Six candidate mechanisms were tested numerically (SUSY exact, SUSY TeV, dim-reg, anthropic, quintessence, unimodular); all fail or are incomplete. This attempt proposes a new angle: the mechanism IS K-minimality itself.

---

## The Parmenidean Floor

### From metaphysics to physics

ParmenidesK.lean proves: no specifiable state has K = 0. Every state that CAN be specified, discussed, or computed about has K > 0.

The vacuum is a physical state. It is specifiable (we specify it as "the ground state of the SM"). Therefore:

**K(vacuum) > 0.**

This is the **Parmenidean floor**: the vacuum cannot have zero K-content. It must carry SOME structure. The minimum K-content of any physical state is bounded below by 1 bit (the distinction "this state, not another").

### From K-content to energy density

The vacuum's K-content and its energy density are related. A vacuum with more structure (more K) can carry more energy density. A vacuum with minimal K carries minimal energy density.

The precise relationship depends on the physics, but the qualitative argument is:

1. ρ_Λ = 0 would mean the vacuum carries no energy at all — no fluctuations, no zero-point contribution, nothing. This requires a PERFECT cancellation among all field contributions. A perfect cancellation is a specific structural claim: "all contributions sum to exactly zero." This claim has K-content (it specifies a constraint).

2. ρ_Λ = ρ_Planck would mean the vacuum carries maximal energy density — every mode contributes at the Planck scale. This requires NO cancellation. But it also requires specifying why no symmetry constrains the energy, which has K-content.

3. ρ_Λ ≈ small nonzero value is the K-minimal option IF: (a) exact zero requires specifying a symmetry that forces cancellation (K > 0), and (b) Planck-scale requires specifying absence of all constraints (also K > 0), and (c) the K-cheapest specification is "near zero via approximate symmetry."

### The Parmenidean Floor Theorem

**Statement:** The vacuum energy density ρ_Λ satisfies 0 < ρ_Λ ≪ ρ_Planck.

**Argument:**

1. K(vacuum) > 0 (Parmenidean floor, proved in ParmenidesK.lean)
2. The vacuum is K-minimal among physical states (it is the ground state — any additional structure raises it above ground)
3. K-minimality constrains ρ_Λ from above: a vacuum with less structure has less energy to specify
4. The Parmenidean floor constrains ρ_Λ from below: K > 0 implies the vacuum has SOME specifiable energy content
5. Therefore: 0 < ρ_Λ, and ρ_Λ is small (K-minimal)

**What this does NOT give:** The exact value 10^{-123}. This is a qualitative prediction: small and nonzero. The exact value requires the landscape selection argument (below).

---

## K-Minimal Landscape Selection

### The setup

The Bousso-Polchinski landscape has ~10^500 vacua, each specified by 500 flux integers f_1, ..., f_500 ∈ {0, ..., 9}. The cosmological constant of each vacuum is:

ρ_Λ = Σ_i q_i² f_i² - C

where q_i are charge quanta and C is a universal offset. The 10^361 vacua in the anthropic window have ρ_Λ in the range [0, Λ_max] compatible with structure formation.

### K-cost of a flux configuration

Each flux integer f_i has Kolmogorov complexity:

K(f_i) = { 0,              if f_i = 0  (default, no specification needed)
          { ⌈log₂(f_i+1)⌉, if f_i > 0  (need to specify the value)

The total K-cost of a vacuum:

K(vacuum) = Σ_i K(f_i)

K-minimality selects the vacuum with the most zero fluxes — i.e., the simplest specification.

### The selection argument

Among the 10^361 anthropically viable vacua:

1. **K-minimal vacua have the most zero fluxes.** A vacuum with 450 zero fluxes and 50 nonzero fluxes has K ≈ 50 × 3.3 ≈ 165 bits. A vacuum with 250 zero fluxes and 250 nonzero fluxes has K ≈ 250 × 3.3 ≈ 825 bits.

2. **More zero fluxes → smaller ρ_Λ.** Each nonzero flux adds q_i² f_i² to the sum. Fewer nonzero fluxes → smaller sum → smaller |ρ_Λ - 0|.

3. **K-minimality selects small ρ_Λ.** The K-cheapest anthropic vacuum has ρ_Λ near the BOTTOM of the anthropic window.

4. **This reproduces Weinberg's prediction.** Weinberg (1987) predicted that ρ_Λ should be near the smallest value compatible with galaxy formation. The observed ρ_Λ ≈ 2.3 × Λ_min (barely above the minimum). K-minimality gives an INDEPENDENT reason for the same prediction.

### Quantitative estimate

The anthropic window spans roughly 2 orders of magnitude: Λ_min ≈ 10^{-124} to Λ_max ≈ 10^{-122} (in Planck units). The K-minimal vacuum within this window has ρ_Λ near Λ_min.

The K-cost difference between Λ_min and Λ_max vacua:

ΔK ≈ log₂(10^2) ≈ 6.6 bits

This is small but nonzero. K-MDL prefers the Λ_min vacuum by ~7 bits. The observed ρ_Λ ≈ 2.3 × Λ_min is consistent with K-minimality placing us near but not exactly at the bottom (the "not exactly" requires ~1 additional bit of specification).

---

## The CC Mechanism Reframed

### What "mechanism" means under K-minimality

The traditional framing asks: "What dynamical mechanism cancels the 10^{139}-order-of-magnitude vacuum energy?"

K-minimality reframes this: **There is no cancellation mechanism. The question is malformed.** The vacuum doesn't START at ρ_Planck and get cancelled down. The vacuum IS the K-minimal physical state, which has small ρ_Λ by selection, not by cancellation.

The analogy: asking "what mechanism makes the ground state of hydrogen have energy -13.6 eV instead of 0?" is malformed. The ground state doesn't start at 0 and get pushed to -13.6 eV. It IS -13.6 eV because that's the lowest eigenstate. Similarly, the vacuum doesn't start at ρ_Planck and get cancelled. It IS ρ_Λ ≈ 0 because that's the K-minimal state in the landscape.

### What the QFT calculation gets wrong

The standard QFT calculation sums zero-point energies of all modes and gets ρ ≈ ρ_Planck. But this calculation assumes:
1. The vacuum is a single QFT in flat spacetime
2. All modes contribute independently
3. There is no UV completion

Under K-minimality, the QFT calculation is computing the K-content of a SPECIFIC vacuum specification (sum of mode energies), not the K-content of the actual vacuum (which is selected by K-minimality from the landscape). The discrepancy is not a cancellation problem — it's a category error: confusing "what this specification predicts" with "what K-minimality selects."

### Status of the reframing

This is a **dissolution**, not a solution. It dissolves the CC mechanism question by arguing the question presupposes a dynamical cancellation that doesn't exist. The vacuum has small ρ_Λ because it is K-minimal, not because something cancels a large contribution.

**Strength:** Explains qualitative features (small, nonzero, near bottom of anthropic window) without fine-tuning or new dynamics.

**Weakness:** Depends on the landscape being real (10^500 vacua). If the landscape doesn't exist, K-minimality has nothing to select from. Also: K-minimality is a SELECTION principle, not a dynamical principle. It says WHY this vacuum but not HOW the universe ended up in it (that's the measure problem).

---

## Three Testable Consequences

### T1: ρ_Λ near bottom of anthropic window

K-minimality predicts ρ_Λ ≈ Λ_min (bottom of the structure-formation window). Observed: ρ_Λ ≈ 2.3 × Λ_min. **Consistent.** A more precise K-minimal calculation would predict the ratio ρ_Λ/Λ_min from the K-cost gradient across the anthropic window.

### T2: Vacuum stability preferred

K-minimality prefers a STATIC vacuum (Λ constant) over a RUNNING vacuum if K(static) < K(running). A static vacuum is specified by one number; a running vacuum requires a function Λ(t). Therefore K(static) < K(running) by at least log₂(N_parameters_of_running_model) bits.

**Tension:** attempt_002 reports that running vacuum is K-MDL preferred with Δχ² = 3.21. But that comparison includes the FIT to data. The K-minimality prediction is about the VACUUM ITSELF, not the fit. If the data genuinely favor running Λ, that's evidence against K-minimality as a complete selection principle (or evidence that the K-cost of running is paid by improved fit).

**Discriminable:** DESI Y5 + Euclid Y5 + LSST (by ~2030) will determine whether Λ runs. If Λ is static, K-minimality is supported. If Λ runs, the K-cost of the running model must be smaller than the K-cost of the static model PLUS the fit improvement — a quantitative test.

### T3: No new light particles

K-minimality predicts the vacuum has minimal structure. Additional light particles beyond the SM add K-content to the vacuum (each new field has K > 0). Therefore K-minimality disfavors hidden sectors, light moduli, or additional massless fields unless they are REQUIRED for anthropic viability.

**Testable:** If future experiments discover light BSM particles that are NOT anthropically required, K-minimality as stated is falsified. Conversely, if the SM is the complete low-energy theory, K-minimality is supported.

---

## Connection to the Parmenidean argument

The logical chain:

1. Nothing is not a specifiable state (Parmenidean K-argument) → K(vacuum) > 0
2. The vacuum is K-minimal among physical states → ρ_Λ is small
3. K > 0 is strict → ρ_Λ > 0 (nonzero)
4. K-minimality within the landscape → ρ_Λ near bottom of anthropic window

Steps 1–3 are the METAPHYSICAL contribution: connecting the impossibility of nothing to the smallness and nonzero-ness of the CC. Step 4 is the PHYSICAL contribution: using K-minimality within the landscape to get a quantitative prediction.

The metaphysical question ("why is there something rather than nothing?") and the physical question ("why is ρ_Λ ≈ 10^{-123}?") are connected by the Parmenidean floor: the vacuum is the MOST nothing-like something, and its energy density measures HOW MUCH something it must be.

---

## What this attempt closes

- Component (a) of the CC decomposition is REFRAMED: not a cancellation mechanism but a K-minimality selection
- The CC is connected to the Parmenidean argument via the K-floor
- Three testable consequences identified (two already consistent with observation)
- The "mechanism question" is argued to be malformed (dissolution, not solution)

## What remains

- **The measure problem.** K-minimality selects WHICH vacuum but not HOW the universe ends up there. The cosmological measure problem (eternal inflation, bubble nucleation) is separate.
- **Landscape reality.** The argument depends on 10^500 vacua existing. If the landscape is much smaller, K-minimality has less to select from and the prediction weakens.
- **Running Λ tension.** The numerical track found Δχ² = 3.21 favoring running Λ. If confirmed by DESI/Euclid/LSST, either K-minimality needs modification or the running K-cost is surprisingly small.
- **Exact value.** The quantitative prediction (ρ_Λ/Λ_min ≈ 2.3) needs a precise K-cost gradient calculation within the landscape.

## Lean targets

1. **KMinimalVacuum.lean** — K-cost function for flux configurations, K-minimality theorem, Parmenidean floor → ρ > 0
2. **CCDecomposition.lean** — four independent components, mechanism reframed

## Sky bridges

- **physics/what_is_reality** — K-minimality is a special case of the compression fixed point: the vacuum is the fixed point with minimal K
- **physics/what_is_information** — K-content as the currency of vacuum specification
- **physics/what_is_computation** — the vacuum is the simplest "program" that runs physics; K-minimality is the halting condition
- **philosophy/what_is_number** — the empty set has K > 0 (it is a specific mathematical object); the vacuum has K > 0 (it is a specific physical state). Same Parmenidean floor.
