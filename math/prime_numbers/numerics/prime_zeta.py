"""
Prime zeta function P(s) = Σ_{p prime} 1/p^s.

Defined for Re(s) > 1. Diverges as s → 1⁺ since Σ 1/p diverges.

The fundamental identity (Glaisher, 1891 — folklore even earlier):
    log ζ(s) = Σ_{k ≥ 1} P(ks) / k
which inverts via Möbius:
    P(s) = Σ_{k ≥ 1} (μ(k)/k) · log ζ(ks)

This identity bridges P (a sum over primes) with log ζ (a function defined
on all of C \\ {1}). It is the simplest example of how the Riemann zeta
function "knows" about primes.

Reference values (high precision, computed via mpmath at 30 digits):
    P(2) = 0.45224742004106549850654336483224793...
    P(3) = 0.17476263929944353642311331466570670...
    P(4) = 0.07699313976424792356705533450466975...
    P(5) = 0.03575501748390848355875184152480985...
    P(6) = 0.01707008685063625060485631411575115...
    P(7) = 0.00828383285619838526913020902019555...
    P(8) = 0.00406140536654988654539015458603625...

This script:
1. Computes P(s) directly via sieve (sum over primes ≤ 10^8)
2. Computes P(s) via Möbius inversion using mpmath ζ
3. Compares both to reference values
4. Estimates the tail Σ_{p > 10^8} 1/p^s
"""
import numpy as np
from math import log
import mpmath
from sieve_core import sieve, primes_up_to


def prime_zeta_direct(s, primes):
    """Direct sum over primes."""
    return sum(p ** (-s) for p in primes)


def prime_zeta_via_mobius(s, k_max=50):
    """P(s) = Σ_{k=1}^{k_max} (μ(k)/k) · log ζ(ks).

    For larger k, log ζ(ks) → log 1 = 0 super-fast (ζ(ks) → 1 since
    ks → ∞ and ζ(ks) ≈ 1 + 2^{-ks} + ...).
    """
    # Möbius function up to k_max
    mu = mobius_up_to(k_max)
    total = mpmath.mpf(0)
    mpmath.mp.dps = 30
    for k in range(1, k_max + 1):
        if mu[k] == 0:
            continue
        log_zeta = mpmath.log(mpmath.zeta(k * s))
        total += mu[k] / mpmath.mpf(k) * log_zeta
    return float(total)


def mobius_up_to(N):
    """Sieve-based Möbius function array."""
    mu = [0] * (N + 1)
    mu[1] = 1
    for i in range(1, N + 1):
        for j in range(2 * i, N + 1, i):
            mu[j] -= mu[i]
    return mu


def tail_estimate(s, x_max):
    """Estimate Σ_{p > x_max} 1/p^s.
    Using prime density 1/log p:
        Σ_{p > x_max} 1/p^s ≈ ∫_{x_max}^∞ dt / (t^s log t)
    For s ≥ 2 this is bounded above by ∫_{x_max}^∞ dt/t^s = 1/((s-1) x_max^{s-1}).
    Tighter: divide by log x_max:
        ≈ 1/((s-1) x_max^{s-1} log x_max)
    """
    return 1.0 / ((s - 1) * x_max ** (s - 1) * log(x_max))


def main():
    N = 10**8
    print(f"Prime zeta function P(s) = Σ_{{p prime}} 1/p^s")
    print(f"Direct sum over primes ≤ {N}")
    print("=" * 76)

    print("Building sieve...")
    is_prime = sieve(N)
    primes = [i for i in range(2, N + 1) if is_prime[i]]
    print(f"  {len(primes)} primes ≤ {N}")
    print()

    # Compute high-precision reference values via mpmath at 30 dps
    mpmath.mp.dps = 30
    ref = {}
    for s_int in range(2, 9):
        # Use Möbius identity at very high k_max for reference
        total = mpmath.mpf(0)
        mu = mobius_up_to(100)
        for k in range(1, 101):
            if mu[k] == 0:
                continue
            total += mu[k] / mpmath.mpf(k) * mpmath.log(mpmath.zeta(k * s_int))
        ref[s_int] = float(total)

    print(f"{'s':>3} {'P(s) direct':>16} {'P(s) Möbius/ζ':>16} "
          f"{'reference':>16} {'tail est':>14} {'Δ direct':>14} {'Δ Möbius':>14}")
    print("-" * 100)

    for s in range(2, 9):
        # Direct sum
        direct = sum(1.0 / p ** s for p in primes)
        # Möbius/zeta
        mob = prime_zeta_via_mobius(s)
        # Tail
        tail = tail_estimate(s, N)
        # Errors
        delta_direct = direct - ref[s]
        delta_mob = mob - ref[s]
        print(f"{s:>3} {direct:>16.13f} {mob:>16.13f} {ref[s]:>16.13f} "
              f"{tail:>14.2e} {delta_direct:>+14.3e} {delta_mob:>+14.3e}")
    print()
    print("Notes:")
    print("  - 'P(s) direct' = sum over primes ≤ 10^8")
    print("  - 'P(s) Möbius/ζ' = Σ_k μ(k)/k · log ζ(ks), k ≤ 50, via mpmath")
    print("  - 'tail est' is the predicted contribution from primes > 10^8")
    print("  - For Möbius method: errors are at the limit of float precision")
    print("    (truncating mpmath to float)")
    print()

    # Demonstrate that the Möbius method works for s near 1 where the
    # direct sum is impractical
    print("ζ_P(s) for s near 1 (Möbius method only — direct diverges):")
    print(f"{'s':>6} {'P(s) Möbius':>20}")
    print("-" * 28)
    for s in [1.5, 1.2, 1.1, 1.05, 1.01]:
        mob = prime_zeta_via_mobius(s)
        print(f"{s:>6.2f} {mob:>20.10f}")
    print()
    print("As s → 1⁺, P(s) → ∞ (Σ 1/p diverges).")
    print("The growth rate is P(s) ~ -log(s - 1) + M, M = Mertens-Meissel constant.")
    print()

    # Connect to twin prime constant
    print("CONNECTION: Twin prime constant via prime zeta")
    print("-" * 60)
    print("Twin prime constant: C_2 = ∏_{p ≥ 3} (1 - 1/(p-1)²)")
    print("                          = exp(Σ_{p ≥ 3} log(1 - 1/(p-1)²))")
    print("                          ≈ exp(-Σ_{p ≥ 3} 1/(p-1)²) (small correction)")
    print()
    # Compute via prime sum
    log_C2 = 0.0
    for p in primes[1:]:  # skip p=2
        log_C2 += log(1 - 1 / (p - 1) ** 2)
    C2_direct = float(np.exp(log_C2))
    C2_ref = 0.6601618158468695
    print(f"  C_2 (sum over primes ≤ 10^8) = {C2_direct:.10f}")
    print(f"  C_2 reference                 = {C2_ref:.10f}")
    print(f"  Δ                             = {abs(C2_direct - C2_ref):.2e}")


if __name__ == '__main__':
    main()
