# Prime Numbers

Campaign directory for prime number conjectures. Not a Clay Millennium problem
(RH is the closest), but the richest area for brute-force computation in number
theory.

## Targets

1. **Goldbach's conjecture** — every even n > 2 is a sum of two primes. Verified
   to 4×10¹⁸ (Oliveira e Silva 2014). Questions: how does the number of
   representations r(n) grow? Are there any even n with r(n) = 1 beyond 4?

2. **Twin prime conjecture** — infinitely many p such that p+2 is prime.
   Current: gap ≤ 246 (Polymath 8b after Zhang 2013 + Maynard 2014). The
   distribution of prime gaps is the key computational target.

3. **Polignac's conjecture** — every even k appears infinitely often as a gap
   between consecutive primes.

4. **Prime races** — Chebyshev's bias: π(x;4,3) usually exceeds π(x;4,1), but
   there are infinitely many sign-flips (Littlewood 1914). First crossing:
   x = 26,861 (Leech 1957).

5. **π(x) vs Li(x)** — Gauss conjectured π(x) < Li(x) always; Littlewood 1914
   proved infinitely many crossings. First crossing: above 10¹⁹ (Skewes
   1933 upper bound was 10^(10^(10^34))).

6. **Prime gaps** — max gap g(p) between consecutive primes below p.
   Cramér's conjecture: g(p) ~ (log p)². Record gaps are tabulated (OEIS A005250).

## Campaign Status: 29 Certs, 29 Scripts + sieve_core

### Infrastructure
- `numerics/sieve_core.py` — Eratosthenes sieve (bytearray, ~1s for 10^8), primes_up_to, Li(x), π(x)

### Certs by Category

**Elementary structure** (5):
- `initial_findings.md` — 11 classical results from a single sieve
- `constellations_and_deficit.md` — Goldbach r(n), Hardy-Littlewood deficit
- `gap_records.md` — all 25 record gaps ≤ 10^8 match OEIS A005250 perfectly
- `mersenne_perfect_verified.md` — 15 Mersenne primes via Lucas-Lehmer, Euclid-Euler
- `carmichael_verified.md` — 105 Carmichael numbers, Korselt criterion, growth rate = Harman 2/7

**Hardy-Littlewood / Bateman-Horn** (5):
- `hardy_littlewood_verified.md` — k-tuple constants to 0.01% (twins, sexy, triplets, quadruplets)
- `polignac_verified.md` — **ALL 50 even gaps d ≤ 100 match HL to 0.2%** (best HL verification)
- `n2_plus_1_verified.md` — Landau's 4th problem, BH for n²+1 at 0.05%
- `sophie_germain_verified.md` — SG primes (same C_2 as twins), Cunningham chains match OEIS A005602
- `cramer_gap_model.md` — Poisson model, gap 6 > gap 2, Pintz tail correction

**Distribution** (3):
- `dirichlet_chebyshev_bias.md` — QNR > QR across 9 moduli, Leech 1957 reproduced exactly
- `erdos_kac_verified.md` — Hardy-Ramanujan mean, Erdős-Kac variance, primorial 19# champion
- `ramanujan_primes_verified.md` — 560 Ramanujan primes, OEIS A104272 match, Bertrand strengthening

**Analytic / PNT** (4):
- `explicit_formula_verified.md` — 200 zeros capture 97% of Li(x) deficit at x=10^6
- `skewes_littlewood_verified.md` — Li(x) > π(x) bias, Bays-Hudson bound 10^316
- `mertens_chebyshev.md` — M(x), ψ(x), PNT error terms
- `euler_products_verified.md` — ζ(s) = Π_p verified, Mertens' 2nd+3rd theorems, Meissel-Mertens M

**Riemann theory / RMT** (3):
- `von_mangoldt_NT_verified.md` — N(T) counting formula, S(T) Selberg CLT at 500 zeros
- `prime_zeta_verified.md` — P(s) = Σ μ(k)/k · log ζ(ks), float-exact at s ≥ 3
- `montgomery_pair_correlation.md` — GUE fits 26× better than Poisson, level repulsion confirmed

**Constants** (3):
- `artin_verified.md` — 12 bases, Hooley correction for a=5 (20/19) verified
- `brun_constant.md` — HL tail extrapolation to 7×10^-6 precision
- `apery_constant_verified.md` — ζ(3) via 3 methods, Apéry recurrence 15 digits in 6 steps

**Summatory functions** (2):
- `liouville_polya_verified.md` — Pólya verified ≤ 10^7, Σλ(n)/n² = π²/15 to 11 digits
- `dickman_smooth_verified.md` — Dickman ρ via RK4, HT refinement cuts error from 10% to 1%

**Rare classes** (2):
- `rare_primes_verified.md` — Wieferich {1093,3511}, Wilson {5,13,563}, Wall-Sun-Sun ∅
- `lehmer_totient_verified.md` — no composite φ(n)|(n-1) found, near-misses all 2p

**Algebraic / elliptic** (2):
- `sato_tate_verified.md` — ⟨cos 2θ⟩ = -1/2 at 36σ, CM detection 100%
- `kummer_irregular_verified.md` — 28 irregular primes ≤ 500, OEIS A000928 exact, Bernoulli witnesses

### Cross-domain bridges
- **→ BSD**: Sato-Tate angles → L(E,1) smoothed sum (`birch_swinnerton_dyer/certs/bsd_lvalue_rank0.md`)
- **→ RH**: Explicit formula, N(T), Montgomery GUE, Euler products, Mertens/Liouville all ⇔ RH
- **→ Algebra**: Kummer irregular primes → cyclotomic class groups → FLT
