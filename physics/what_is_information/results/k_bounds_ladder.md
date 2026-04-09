# results/k_bounds_ladder.md — The K-Information Bounds Ladder

**Date:** 2026-04-09
**Type:** Analytical synthesis of numerical results

## The ladder

All numerical work in this track converges on a hierarchy of K-bounds. From smallest to largest:

```
K = 0
  │
  │  All-zero string. Trivially compressible.
  │  k_conservation.py: erasure approaches this (ΔK = -0.034 to near-zero)
  │
K ≈ 10–100 bits
  │
  │  Physical constants. Fine structure constant (17 bits), electron mass (20 bits),
  │  cosmological parameters (44 bits). k_spec_completeness.py.
  │
K ≈ 21 834 bits (21.8 kbits)
  │
  │  All known physics. SM Lagrangian + 19 SM parameters + GR + ΛCDM initial conditions.
  │  k_spec_completeness.py: CERTIFIED.
  │  Key comparison: Python interpreter ≈ 8 Mbits. Linux kernel ≈ 400 Mbits.
  │  The laws of physics are K-simpler than software.
  │
K ≈ 10^3 – 10^6 bits
  │
  │  Biological systems. E. coli minimal genome (~50 000 bits). Human neuroscience
  │  laws (~10^6 bits). sk_bekenstein_bounds.py (K_laws estimates).
  │  These are MUCH larger than the physical laws but still tiny vs S_holo.
  │
K_LZ78 (string) ≈ n / log₂(n) bits   [lower bound for random strings]
  │
  │  From LZ78 theory: a random string of n symbols over |Σ| alphabet has at least
  │  n/log₂(n) × log₂(|Σ|) distinct LZ78 phrases → phrase count ≈ n/log₂(n).
  │  sk_lz78.py: confirmed for random_bytes (norm ≈ 6.7 ≈ 8×n/log₂(n) for n=10000).
  │  This is the tight LOWER BOUND for K-proxy of structureless random strings.
  │
K_gzip(string) ≤ H(string) × n [crude upper bound via Shannon]
  │
  │  For any string, its gzip ratio is bounded above by its Shannon entropy
  │  (gzip can always achieve at least Shannon compression asymptotically).
  │  sk_plane.py: confirmed — random_bytes (H=7.98, gzip=1.00) and π digits (H=3.32, gzip=0.51).
  │
K(state) ≤ S_holo = 10^124 bits   [holographic upper bound]
  │
  │  From the holographic principle: S_max = π R² c³/(G ħ) for a sphere of radius R.
  │  No physical state in the observable universe can have K > S_holo.
  │  sk_bekenstein_bounds.py: confirmed for all 8 physical systems.
  │  simulation_cost.py: confirmed — this is why Planck-simulation requires > this budget.
  │
K → ∞
  │
  │  Quantum measurement outcomes: each -log₂(P) bits of K-information enters the
  │  physical record. Over the universe's history: N_decoherence × avg(-log₂(P)) bits.
  │  From holographic_evolution.py: N_dec ≈ 10^120, avg K per measurement ≈ 1 bit → 10^120 bits total.
  │  (Still within S_holo = 10^124.)
```

## The key gaps in the ladder

1. **Gap between K_laws (21 834 bits) and K_LZ78(string):** 
   Physical laws are K-simple (21.8 kbits) but their outputs (physical states) can have K
   from 0 (all-zeros) to 10^124 bits (random quantum states). The laws are a GENERATOR —
   their K is small; the output's K depends on quantum measurement history.

2. **Gap between K_LZ78 lower bound and K_true:**
   gzip and LZ78 are lower bounds on K (they can't compress below the true K). For
   globally-algorithmic strings (π, LCG), they OVERESTIMATE K. The true K gap is:
   K_true(π digits) = O(1) but K_LZ78(π digits) ≈ 0.14n. Gap: 0.14n bits / O(1) = ∞.

3. **Gap between K_string and K_region (R1):**
   The holographic bound gives S_holo for a region. For K_region, no analogous formula exists.
   From k_conservation.py: K is not conserved, so no conservation law can bound it.
   The tight lower bound on K in a region requires computational complexity theory
   (what programs can run in the physical laws' Hilbert space?). This is R1's residue.

## What this resolves and what it doesn't

**Resolved:** K is bounded above by S_holo (holographic). K has no conservation law
(k_conservation.py). K of physical laws ≈ 21 834 bits (k_spec_completeness.py).
The S/K gap at cosmic scale is 10^119.6.

**Open (R1):** The tight lower bound on K in a physical region. Not from thermodynamics
(2nd law constrains S, not K). Must come from computational complexity (what K-functions
are physically realizable given the SM Lagrangian + initial conditions?). This requires:
- Physical Church-Turing: every physically realizable process has a finite K-specification
- Circuit lower bounds: minimum circuit depth to compute a physical process's dynamics
- These are the same open questions as P vs NP and computational complexity foundations

## Summary

The K-bounds ladder has three firm entries (K=0, K_laws=21 834, K_holo=10^124) and one
gap (the tight lower bound for physical states). The gap is the central open problem of
what_is_information's R1, and it requires computational complexity theory to close.
