# attempt_002 — Binary vs Ternary: The Efficiency Gap

**Date:** 2026-04-09
**Status:** Open. The theoretical efficiency argument is clean; the practical argument is context-dependent. Ternary is provably denser per symbol, but "density per symbol" is not the only metric, and the combination that favors binary is physical not informational.

## The question

Is binary the most efficient computational substrate, or is ternary (or higher radix) measurably better? If ternary is better in some sense, why did binary win, and is that winning a local optimum or a global minimum?

## The clean information-theoretic part

For a number N, the minimum number of digits in base r is ⌈log_r(N+1)⌉. The total "information content" of a number-digit-system pair is:
- Symbols per number: log_r(N)
- Bits per symbol: log_2(r)
- Bits total: log_r(N) · log_2(r) = log_2(N)

This is base-invariant. So the question "how efficient is base r?" is NOT about information content — that's the same regardless of base. It's about some OTHER cost function.

### Hardware-cost framing (radix economy)

Define hardware cost as: (number of digits) × (states per digit). For a number N:
- Digits needed: ⌈log_r N⌉
- States per digit: r
- Cost: r · log_r N = (r / ln r) · ln N

Minimize r / ln r over r ≥ 2:
- d/dr (r / ln r) = (ln r - 1) / (ln r)^2
- Zero at ln r = 1, i.e. r = e ≈ 2.718
- Minimum value: e ≈ 2.718

So the OPTIMAL hardware radix is e ≈ 2.718. Since radix must be an integer, ternary (r=3) is closest to the optimum and is STRICTLY better than binary (r=2) by this metric:
- Binary: 2 / ln 2 ≈ 2.885
- Ternary: 3 / ln 3 ≈ 2.731
- Quaternary: 4 / ln 4 ≈ 2.885 (ties with binary)
- Quinary: 5 / ln 5 ≈ 3.107 (worse)

**Theoretical gap:** ternary is about 5.3% more efficient than binary under the radix-economy metric. This is mathematically real and not disputed.

## Why binary won anyway

The radix-economy metric assumes equal cost per state. In physical electronics, this is false:

### Noise margin

A binary gate distinguishes TWO voltage levels. Noise margin is half the voltage range. A ternary gate distinguishes THREE levels. Noise margin is a third of the voltage range. For the same supply voltage, ternary logic has 33% less noise margin than binary. To recover binary's noise margin, ternary needs 1.5× the supply voltage, which increases power consumption quadratically (P = V²/R).

### Fan-out and amplification

Binary has two stable states per transistor (cutoff, saturation). Ternary requires an active mid-level, which is amplifier territory, not switching territory. Transistors as amplifiers consume orders of magnitude more power than transistors as switches. Power efficiency favors binary by 10-100×, which dwarfs the 5% information-theoretic gain.

### Manufacturing and verification

Binary state validation is a single threshold test. Ternary requires two thresholds with narrower margins. Manufacturing tolerances, temperature drift, and aging all affect ternary more than binary. Yield is lower; test time is higher.

### Historical inertia

The Setun computer (USSR, 1958) was built with balanced ternary and outperformed binary machines of its era on some benchmarks. It lost not on technical grounds but on ecosystem: no ternary software, no ternary standards, no ternary chipsets. The efficiency gain was real; the switching cost was prohibitive.

## The conjecture

**The efficiency gap between binary and ternary is ~5.3% on information-theoretic metrics but NEGATIVE on physical-hardware metrics. The combination is dominated by physical noise margins, amplification costs, and ecosystem lock-in. Under current electronic substrates, binary is not just a local optimum — it is globally optimal when the cost function includes noise margin and power.**

The conjecture is falsifiable by:
1. A new substrate where ternary noise margin is comparable to binary (e.g., optical with three polarization states, memristors with three resistance states)
2. A new amplification technology where mid-level transistor states don't cost more power than switching states
3. A workload where information-theoretic efficiency dominates physical efficiency (e.g., memory storage at ultra-low voltage)

## Sub-questions

1. **Under what substrate would ternary win?** — formalize the power/noise/yield tradeoff and find conditions where 3 / ln 3 < 2 / ln 2 at the PHYSICAL level.
2. **Is the 5.3% gap reachable in practice?** — how much of the theoretical advantage is lost to ternary-specific overheads even in the best case?
3. **What about higher radix?** — base-4 matches binary in radix economy but loses on physical grounds. Base-10 (decimal) has a large penalty. Is there ANY substrate where base-4 or base-5 wins?

## Counterexamples / failure modes

- **Optical computing** — photon states can be polarization, phase, or wavelength. Multi-state photonic gates are feasible, and the noise margin argument doesn't apply the same way. Ternary or even higher-radix optical might win.
- **Neuromorphic computing** — biological neurons use analog continuous signals, not binary. If "radix" is interpreted as effective state count, neurons have thousands. They are massively parallel at the cost of per-element precision. This may be the dominant substrate for certain tasks (pattern recognition) but not universal computation.
- **Quantum computing** — qubits are 2-state, but qutrits (3-state) and higher are also studied. In quantum, the relevant metric is different (decoherence time, gate fidelity). The binary-ternary question may transfer to quantum with different answers.

## What would a proof look like

The conjecture ("binary is globally optimal under physical constraints") is not provable in the mathematical sense — it is an engineering claim about specific substrates. The rigorous form is:

> For electronic substrates with noise N, signal-to-noise ratio S/N, power-per-transistor P, and manufacturing tolerance T, the expected cost of a ternary computer that performs K operations is C_ternary(K) > C_binary(K) whenever N/S > f(P, T) for some explicit f.

This is a tractable optimization problem in physical electronics, not a theorem of pure mathematics.

## Sky bridges

- **what_is_information** (S/K bifurcation) — base choice is an S-cost question, not a K-cost question. The K content is base-invariant.
- **what_is_computation** (Church-Turing) — any base computes the same functions. The efficiency question is about resource cost, not function class.
- **what_is_number** (base-dependence of "special" numbers) — the prominence of 3-6-9 patterns in base 10 is a base artifact, same way radix economy is a base optimization.
- **Landauer bound** — irreversible bit erasure costs kT ln 2. Ternary erasure costs kT ln 3 ≈ 1.585 × kT ln 2. Per bit, binary is strictly cheaper thermodynamically.

## Numerical followups (to add to ../numerics/)

- `radix_economy_curve.py` — plot r / ln r over [2, 10], mark integer radices
- `ternary_noise_margin.py` — simulate ternary gate with realistic noise, compute yield vs supply voltage
- `landauer_per_digit.py` — compute thermodynamic cost per digit for bases 2-10

## Status

Open. The theoretical piece (radix economy, e as optimum) is settled. The empirical piece (which substrate makes ternary practical) is an engineering research problem, not a theorem. The conjecture — that binary is globally optimal under current physical substrates — is believable but not rigorously proved.
