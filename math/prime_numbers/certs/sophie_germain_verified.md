# Sophie Germain Primes & Cunningham Chains — HL to 0.05%, A092816 + A005602 Perfect

## Date: 2026-04-08

## The result

**229,568 Sophie Germain primes p ≤ 5 × 10⁷** found, matching OEIS A092816
exactly at every cumulative scale, and Hardy-Littlewood prediction to **0.05%**.

**All 6 Cunningham chain length records ≤ 10⁸** (k = 2 through 7) match
OEIS A005602 exactly.

## Sophie Germain primes

A **Sophie Germain prime** is a prime p such that 2p + 1 is also prime.
The corresponding 2p + 1 is called a **safe prime**.

Named after Sophie Germain (1776-1831), who in 1823 used them in the
first major progress on Fermat's Last Theorem after Fermat himself: she
proved that **if p is a Sophie Germain prime, then the first case of FLT
holds for exponent p** — i.e., x^p + y^p = z^p has no solutions with
p ∤ xyz. This single result eliminated infinitely many potential FLT
counterexamples.

### OEIS A092816 verification (count of SG primes < 10^k)

| k | observed | OEIS A092816 | match |
|---|----------|--------------|-------|
| 1 | 3 | 3 | ✓ |
| 2 | 10 | 10 | ✓ |
| 3 | 37 | 37 | ✓ |
| 4 | 190 | 190 | ✓ |
| 5 | 1,171 | 1,171 | ✓ |
| 6 | 7,746 | 7,746 | ✓ |
| 7 | 56,032 | 56,032 | ✓ |

**Perfect agreement at every scale.** First 20 SG primes:
```
2, 3, 5, 11, 23, 29, 41, 53, 83, 89, 113, 131, 173, 179, 191,
233, 239, 251, 281, 293
```

## Hardy-Littlewood prediction (BH for f_1 = n, f_2 = 2n+1)

The Bateman-Horn singular series for the polynomial pair (n, 2n+1) is
**identical to that of twin primes**:
```
C_BH(SG) = ∏_p (1 - ω(p)/p) / (1 - 1/p)²
```
where for each prime:
- ω(2) = 1 (only n ≡ 0 mod 2 gives f_1 = 0; 2n+1 is always odd)
- ω(p) = 2 for p ≥ 3 (the roots are n = 0 and n = (p-1)/2)

These are exactly the same as the twin prime ω-counts. So
```
C_BH(SG) = C_BH(twin) = 2 C_2 ≈ 1.3203
```
where C_2 ≈ 0.6601618 is the **twin prime constant**.

The asymptotic prediction:
```
π_SG(N) ≈ 2 C_2 · ∫_2^N dt / (log t · log(2t + 1))
```
For large t, log(2t+1) ≈ log(2t) ≈ log t, so this is essentially Li_2(N).

### Verification at N = 5 × 10⁷

| Quantity | Value |
|----------|-------|
| Twin prime constant C_2 | 0.6601618158 |
| Integral ∫_2^N dt/(log t · log(2t+1)) | 173,777.03 |
| **Predicted π_SG(N)** | **229,442** |
| **Observed π_SG(N)** | **229,568** |
| **Ratio** | **1.0005** |

**0.05% match at N = 5 × 10⁷** — pristine confirmation of the Bateman-Horn
prediction for a non-twin prime k-tuple. This pairs with `polignac_verified.md`
(also 0.2% precision across 50 even gaps) as the strongest empirical
support for the HL/BH framework.

## Cunningham chains of the first kind

A **Cunningham chain of the first kind** is a sequence of primes
p_0, p_1, p_2, ... where p_{i+1} = 2 p_i + 1. Each consecutive pair is
a Sophie Germain pair. The **length** is the number of primes in the chain.

Cunningham chains are the "longer cousins" of SG pairs, and progressively
rarer: a length-k chain requires k consecutive SG-style primality lifts.

### OEIS A005602 verification (smallest p starting a chain of length ≥ k)

| k | smallest start (observed) | OEIS A005602 | match |
|---|--------------------------|--------------|-------|
| 2 | 2 | 2 | ✓ |
| 3 | 2 | 2 | ✓ |
| 4 | 2 | 2 | ✓ |
| 5 | 2 | 2 | ✓ |
| 6 | 89 | 89 | ✓ |
| **7** | **1,122,659** | **1,122,659** | **✓** |

**All 6 records match exactly.**

### The famous chains

**The chain starting at 2** (length 5):
```
2 → 5 → 11 → 23 → 47
```
Each of 2, 5, 11, 23, 47 is prime; 2·47 + 1 = 95 = 5 · 19 is composite,
ending the chain. This is the "primer" Cunningham chain known since the
discovery of safe primes.

**The chain starting at 89** (length 6):
```
89 → 179 → 359 → 719 → 1439 → 2879
```
First chain to break out of the small range — the smallest length-6 chain.

**The chain starting at 1,122,659** (length 7):
```
1,122,659 → 2,245,319 → 4,490,639 → 8,981,279 → 17,962,559
         → 35,925,119 → 71,850,239
```
The smallest length-7 Cunningham chain. Each step roughly doubles. The
last term, 71,850,239, is just barely below 10⁸ — explaining why
length-7 chains require sieving to ~10⁸ to find.

(Length-8 starts at 19,099,919 with chain ending at 2,444,789,759 — beyond
our 10⁸ sieve.)

### Why Cunningham chains thin out

Each step of a Cunningham chain requires the lift "2p + 1 is prime",
which is a Sophie Germain condition. Heuristically, P(2p + 1 prime | p prime)
≈ 2 C_2 / log(2p+1) ≈ C_2 / log p. So:
```
P(chain length ≥ k starting at p) ≈ ∏_{i=0}^{k-1} (C_2 / log(2^i p))
                                    ≈ (C_2 / log p)^k
```
The chain count grows much faster than the prime count itself decays —
there are infinitely many chains predicted at every length, but the
smallest one of length k grows like
```
exp(k · log log...)  (roughly e^{k} · k!)
```
which is super-exponential in k. So length 8 needs p ~ 2 × 10⁷, length 9
needs p ~ 8 × 10⁷, length 10 needs p ~ 10¹⁰, length 12 needs p ~ 10¹³, etc.

## The cryptographic angle

Sophie Germain primes (and safe primes) are foundational to **Diffie-Hellman
key exchange**, **DSA signatures**, and **ElGamal encryption**:
- A safe prime q = 2p + 1 has the property that the multiplicative group
  Z_q^* has order 2p, with subgroup of order p generated by any quadratic
  residue
- Working in this prime-order subgroup makes the discrete log problem
  cleanly hard (only the trivial subgroup of order 2 to worry about)
- Without safe primes, you'd need to verify the order of your generator
  in a possibly composite-order subgroup

Standardized cryptographic safe primes (e.g., the RFC 3526 "MODP" groups
for Internet Key Exchange) are 1024-bit, 2048-bit, 3072-bit safe primes
with specific structures. Finding them required searches that took
substantial CPU time in the 1990s; today's safe primes use even larger sizes.

### The "first SG primes" you'd actually use in cryptography

For 2048-bit DH, you need a safe prime q ≈ 2^2048 with q - 1 = 2p where
p is prime. The HL prediction gives one safe prime per ~log²(2^2048) ≈
2 × 10⁶ candidates near the right size. Finding one takes minutes on
modern hardware. The randomness of which specific safe prime gets used
does NOT need to be cryptographically secure — only the discrete log
inside it does.

## Sophie Germain's FLT contribution

Germain's theorem (1823, published in Legendre's Théorie des Nombres):
> If p is an odd prime and 2p + 1 is also prime, then the equation
> x^p + y^p = z^p has no integer solutions with p ∤ xyz.

This is the **first case of FLT**. Germain's proof was elementary and
remarkably elegant. She also generalized to: if there exists an auxiliary
prime q = 2kp + 1 satisfying certain conditions, the same conclusion
holds. She used this to prove FLT first case for many small p directly.

**FLT was proven completely by Wiles 1995** via modular forms and
elliptic curves — a vastly more powerful machinery. Germain's theorem
is now superseded as a tool, but it remains historically iconic as
the first systematic technique for FLT.

## Sigma Method observation

This cert combines **two perfect numerical confirmations**:
1. **HL/BH prediction at 0.05% precision** — the second-most-precise
   verification of the Bateman-Horn machinery (after `polignac_verified.md`
   at 0.2% across 50 gaps).
2. **OEIS A092816 + A005602 perfect match** — exhaustive search agreement
   with the canonical reference data at every cumulative scale.

The "same constant as twin primes" identity (C_BH(SG) = C_BH(twin) = 2 C_2)
is itself a **deep structural fact**: it tells us that polynomial pairs
with the same ω-pattern have identical singular-series prefactors,
regardless of the specific polynomials. This is the BH framework's
universality made manifest.

The Cunningham chain results are a **nice combinatorial layer on top**:
they capture how SG-like conditions COMPOUND across iterated polynomials,
giving exponentially-rare configurations that are nonetheless completely
predictable from the local prime densities.

## Reproducibility

Script: `numerics/sophie_germain.py`
Dependencies: numpy, math, scipy.integrate.quad, sieve_core.
Runtime: ~10 seconds (sieve to 10⁸ + SG check + Cunningham chain scan).
