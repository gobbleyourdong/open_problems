# physics/ — Testable Predictions from the Numerical Track

**Date:** 2026-04-09
**Scope:** Predictions from the K-information framework that are empirically accessible

This document collects all testable predictions emerging from Phase 3 numerical work. Each prediction is marked with: the source script, the specific quantitative claim, and the experimental path to test it.

---

## Category 1: Near-term (testable within 5 years)

### P1. Euclid: f·σ₈ shift (what_is_nothing)

**Prediction:** If DESI 2024's w₀=-0.827 is correct, structure growth f·σ₈ at z=0.5 should be +1.76% above ΛCDM.
**Specific:** f·σ₈(ΛCDM) = 0.4744; f·σ₈(DESI) = 0.4827 (Δ = 0.0083)
**Timeline:** Euclid Year 3 (2028) reaches σ(f·σ₈) ≈ 0.007 → this shift is 1.2σ with Euclid alone, 3σ combined with DESI Year 5
**Outcome:**
- If confirmed (+1.76%): running vacuum model preferred (K=40 bits, same as ΛCDM); ΛCDM disfavored
- If not seen (<0.5σ): ΛCDM strongly preferred; DESI 2024 tension was systematic error
**Source:** dark_energy_eos_findings.md, euclid_discriminant_findings.md

### P2. Hypothermia extends the specious present (what_is_time)

**Prediction:** Patients cooled to 33°C (306K) should report a 24% longer specious present.
**Specific:** SP(306K) = 3.18s vs SP(310K) = 2.56s (baseline); Q10 ≈ 1.7 for SP
**Measurement:** Temporal order judgment tasks under mild controlled hypothermia
**Outcome:**
- If confirmed (+20-30%): Kramers mechanism confirmed as specious present driver
- If Q10 measured at 2-4: additional non-Kramers mechanisms (enzymatic) also contribute
**Source:** temperature_SP_findings.md, specious_present_derivation.md

### P3. Fever shortens the specious present (what_is_time)

**Prediction:** Patients at 42°C (315K) should report a 23% shorter specious present.
**Specific:** SP(315K) = 1.97s (-23% vs baseline)
**Complication:** cognitive impairment at high fever — need to control
**Source:** temperature_SP_findings.md

### P4. K-change rate per Wolfram class (what_is_computation)

**Prediction:** K-change rate (in bytes/step) discriminates Wolfram's 4 classes:
- Class 2 (periodic): 8.77 bytes/step
- Class 4 (universal): 32.59 bytes/step
- Class 3 (chaotic): 37.97 bytes/step
**Testable:** Apply to real physical systems that can be Wolfram-classified
- Weather: should show Class 3 range (≈38 bytes/step of K-change)
- Heartbeat: should show Class 2 range (≈9 bytes/step)
- Neural dynamics: should show Class 4 range (≈33 bytes/step)
**Source:** cellular_automata_K_findings.md

### P5. Brain temperature sensitivity (what_is_change + what_is_time)

**Prediction:** Kramers rate Q10 ≈ 1.7 for neural ion channel gating
**Specific:** Kramers crossing rate at 300K / Kramers at 310K = 1.74×
**Measurement:** Ion channel patch-clamp recordings at different temperatures
**Outcome:**
- If Q10 ≈ 1.7: Kramers mechanism confirmed for neural K-change
- If Q10 ≈ 2-4: enzymatic/conformational changes dominate (not pure Kramers)
**Source:** kramers_neural_findings.md, temperature_SP_findings.md

---

## Category 2: Medium-term (5-15 years, requires next-generation experiments)

### P6. FERMI next-generation: sub-Planckian LIV (what_is_reality)

**Prediction:** Linear LIV ruled out at 7.2× Planck energy (already done: GRB 090510).
A next-generation γ-ray telescope (100 GeV, 10 Gpc) would probe to 8.4×10^8 × E_P.
**Specific:** If such a telescope observes a GRB at z≈10, 100 GeV photons with Δt < 0.01s:
- E_P_min would reach 10^37 eV = 8.4×10^8 × E_P
- Any simulator must use cells ≤ l_P / (8.4×10^8) — 10^9 times sub-Planckian
**Outcome:** Further strengthens the simulation impossibility argument
**Source:** simulation_detectability_findings.md, lv_bounds_findings.md

### P7. Euclid + DESI Year 5: w₀ measurement to σ(w₀) < 0.07 (what_is_nothing)

**Prediction:** If w₀ = -0.827 (DESI 2024), σ(w₀) < 0.07 (DESI Y5) → 3.5σ confirmation of w ≠ -1
**K-MDL consequence:** Running vacuum (K=40 bits) becomes preferred over ΛCDM
**Timeline:** DESI Year 5: 2027-2028
**Source:** dark_energy_eos_findings.md

### P8. Proton decay observation (what_is_reality, TOE K-debt)

**Prediction:** SM+GR is preferred over string theory until proton decay is confirmed.
String theory's K-debt = 2161 bits; proton decay at τ ~ 10^34 years is a unique string prediction.
**Specific:** Hyper-Kamiokande (2027+) could observe p→π⁰+e⁺ or p→K⁺+ν at τ ~ 10^34-35 years
**K-MDL consequence:** A single proton decay observation would pay off ~1000 bits of string K-debt (log₂(τ_predicted/τ_SM) bits of precision advantage)
**Source:** toe_k_findings.md, toe_k_debt_cert.md

---

## Category 3: Long-term or fundamentally inaccessible

### P9. Black hole Page curve K-recovery (what_is_reality, R2 discriminant)

**Prediction (K-informationalism):** Late-time Hawking radiation does NOT recover K-structure (K stays ≈0 throughout evaporation)
**Prediction (S-informationalism):** Late-time Hawking radiation DOES recover K-structure (Page curve: K increases after Page time)
**Status:** **INACCESSIBLE** — for any astrophysical BH, t_evap >> 10^67 years
**Source:** black_hole_k_findings.md, k_informationalism_thesis.md

### P10. Big Bang low-entropy explanation (what_is_time, R3 open)

**Prediction:** The K-information framework fully accounts for WHY entropy increases from any low-entropy starting point (2nd law + Lyapunov). But it does NOT explain WHY the Big Bang started with low entropy.
**Required:** Quantum cosmology (Hartle-Hawking wave function, Penrose CCC) — currently beyond any experiment
**Source:** big_bang_k_resolution.md, cosmological_entropy_findings.md

---

## Summary table

| # | Prediction | Quantitative claim | Timeline | Status |
|---|---|---|---|---|
| P1 | Euclid f·σ₈ shift | +1.76% above ΛCDM | 2028 | **High priority** |
| P2 | Hypothermia SP | +24% at 33°C | Available now | **High priority** |
| P3 | Fever SP | -23% at 42°C | Available now | Needs controls |
| P4 | Wolfram K-change | Class 2=8.77, Class 4=32.6 bytes/step | Available now | Testable in systems biology |
| P5 | Neural Q10 | Q10≈1.7 for ion channels | Available now | Patch clamp |
| P6 | Next-gen LIV | Sub-Planckian constraint | 15+ years | Instrument limited |
| P7 | DESI Y5 w₀ | σ(w₀)<0.07 confirming w≠-1 | 2027-2028 | Underway |
| P8 | Proton decay | τ ~ 10^34-35 years | 5-15 years | Hyper-K |
| P9 | BH Page curve | K-recovery after Page time | INACCESSIBLE | >10^67 years |
| P10 | Big Bang entropy | Why low S at t=0 | INACCESSIBLE | Requires quantum cosmology |

**The three most testable, unambiguous predictions:** P1 (Euclid, 2028), P2 (hypothermia SP, immediate), P5 (neural Q10, immediate).
