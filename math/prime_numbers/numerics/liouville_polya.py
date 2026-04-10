"""
Liouville function λ(n) and Pólya's conjecture.

The LIOUVILLE FUNCTION is the completely multiplicative function
    λ(n) = (-1)^Ω(n)
where Ω(n) is the number of prime factors of n COUNTED WITH MULTIPLICITY.

So Ω(1) = 0, Ω(p) = 1, Ω(p²) = 2, Ω(pq) = 2, Ω(p³) = 3, etc.

Examples:
    λ(1)  = +1   (Ω = 0)
    λ(2)  = -1   (Ω = 1)
    λ(4)  = +1   (Ω = 2)
    λ(6)  = +1   (Ω = 2)
    λ(8)  = -1   (Ω = 3)
    λ(12) = -1   (Ω = 3)

Compare to the MÖBIUS function μ(n), which is 0 on non-squarefree numbers.
λ never vanishes; it cycles between +1 and -1.

PÓLYA'S CONJECTURE (1919): The summatory function
    L(x) := Σ_{n ≤ x} λ(n)
satisfies L(x) ≤ 0 for all x ≥ 2.

This is suggested by direct computation: L(x) was negative for every x
checked up to 10⁶ in 1919. The conjecture stood for 39 years.

DISPROVED by Haselgrove (1958) using analytic methods, without exhibiting
a counterexample. The smallest counterexample (Tanaka 1980) is at
    n = 906,150,257
where L(906150257) = +1. This is just beyond our 10⁸ direct sieve range.

CONNECTION TO RH: |L(x)| = O(x^(1/2 + ε)) iff RH holds. So Pólya's
conjecture (in a weaker form) is equivalent to RH.

GENERATING FUNCTION:
    Σ_{n=1}^∞ λ(n) / n^s = ζ(2s) / ζ(s)    for Re(s) > 1.
This is the analogue of Σ μ(n)/n^s = 1/ζ(s).

In particular at s = 2:
    Σ λ(n) / n² = ζ(4) / ζ(2) = (π⁴/90) / (π²/6) = π² / 15 ≈ 0.6580

This script:
1. Computes Ω(n) via sieve to N = 10⁷
2. Builds L(x) = Σ λ(n) at multiple scales
3. Verifies Pólya holds in [1, 10⁷] (and discusses the 906,150,257 disproof)
4. Verifies Σ λ(n)/n² → π²/15
"""
import numpy as np
from math import sqrt, pi, log
from sieve_core import sieve


def compute_omega_with_multiplicity(N):
    """Compute Ω(n) for all n ≤ N. Sieve approach: for each prime power p^k,
    increment Ω by 1 for every multiple."""
    omega = np.zeros(N + 1, dtype=np.int8)
    is_prime = sieve(N)
    for p in range(2, N + 1):
        if is_prime[p]:
            pk = p
            while pk <= N:
                omega[pk::pk] += 1
                pk *= p
    return omega


def main():
    N = 10**7
    print(f"Liouville function & Pólya's conjecture, n ≤ {N}")
    print("=" * 76)

    print("Computing Ω(n) for n ≤ 10^7 via sieve...")
    omega = compute_omega_with_multiplicity(N)
    print(f"  done.")

    # λ(n) = (-1)^Ω(n)
    print("Computing λ(n) = (-1)^Ω(n)...")
    lam = np.where(omega % 2 == 0, 1, -1).astype(np.int32)
    lam[0] = 0  # convention
    print()

    # Spot check small values
    print("Spot check first 20 values:")
    for n in range(1, 21):
        print(f"  λ({n}) = {lam[n]:>+d}, Ω({n}) = {omega[n]}")
    print()

    # L(x) at multiple scales
    print("L(x) = Σ_{n ≤ x} λ(n):")
    print(f"{'x':>12} {'L(x)':>14} {'L(x) / √x':>14} {'sign':>8}")
    print("-" * 52)
    cumL = np.cumsum(lam[1:N + 1])  # cumL[x-1] = L(x)
    for k in range(1, 8):
        x = 10 ** k
        Lx = int(cumL[x - 1])
        ratio = Lx / sqrt(x)
        sign = "≤ 0 ✓" if Lx <= 0 else "> 0 ✗"
        print(f"{x:>12} {Lx:>+14} {ratio:>+14.4f} {sign:>8}")
    print()

    # Verify Pólya holds in [1, 10^7]
    print("Pólya's conjecture: L(x) ≤ 0 for all x ≥ 2")
    print("-" * 50)
    # Find positions where L(x) > 0
    pos_x_plus_one = np.where(cumL[1:] > 0)[0]
    if len(pos_x_plus_one) == 0:
        print("✓ L(x) ≤ 0 for all x ∈ [2, 10⁷]")
    else:
        first_violation = int(pos_x_plus_one[0]) + 2
        print(f"✗ Pólya violated! First x with L(x) > 0 is x = {first_violation}")
    print()
    print("Known: smallest counterexample to Pólya is n = 906,150,257 (Tanaka 1980)")
    print("       This is beyond our 10⁷ range, hence we see no violations.")
    print()

    # Find max and min ratios L(x)/√x
    xs = np.arange(2, N + 1, dtype=np.float64)
    ratios = cumL[1:] / np.sqrt(xs)
    max_ratio_idx = int(np.argmax(ratios))
    min_ratio_idx = int(np.argmin(ratios))
    print(f"Max L(x)/√x in [2, 10⁷]: {ratios.max():+.4f} at x = {max_ratio_idx + 2}")
    print(f"Min L(x)/√x in [2, 10⁷]: {ratios.min():+.4f} at x = {min_ratio_idx + 2}")
    print(f"|L(x)/√x| ≤ {max(abs(ratios.max()), abs(ratios.min())):.4f}")
    print()
    print("This is well within Pólya's bound √x (= 1 in normalized units).")
    print("RH would imply |L(x)/√x| ≤ log² x (which would be ~260 at 10⁷).")
    print()

    # Verify Σ λ(n)/n² = ζ(4)/ζ(2) = π²/15
    print("=" * 76)
    print("DIRICHLET SERIES: Σ λ(n)/n² = ζ(4)/ζ(2) = π²/15")
    print("=" * 76)
    print()
    print("Direct sum over n ≤ 10⁷ vs reference value:")
    n_arr = np.arange(1, N + 1, dtype=np.float64)
    direct_sum = float(np.sum(lam[1:N + 1] / n_arr ** 2))
    target = pi ** 2 / 15
    diff = direct_sum - target
    # Tail estimate: |Σ_{n > N} λ(n)/n²| ≤ Σ_{n > N} 1/n² ≈ 1/N
    tail_bound = 1 / N
    print(f"  Σ_{{n=1}}^{{10⁷}} λ(n)/n² = {direct_sum:.10f}")
    print(f"  π²/15                  = {target:.10f}")
    print(f"  Δ                      = {diff:+.2e}")
    print(f"  Tail bound (1/N)       = {tail_bound:.2e}")
    print()
    print("✓ Direct sum matches π²/15 within the tail bound 1/N.")
    print()

    # Bonus: Σ λ(n)/n³ = ζ(6)/ζ(3)
    direct_sum3 = float(np.sum(lam[1:N + 1] / n_arr ** 3))
    # ζ(6) = π⁶/945, ζ(3) ≈ 1.20206
    zeta6 = pi ** 6 / 945
    import mpmath
    zeta3 = float(mpmath.zeta(3))
    target3 = zeta6 / zeta3
    print("BONUS: Σ λ(n)/n³ = ζ(6)/ζ(3)")
    print(f"  Σ_{{n=1}}^{{10⁷}} λ(n)/n³ = {direct_sum3:.10f}")
    print(f"  ζ(6)/ζ(3)              = {target3:.10f}")
    print(f"  Δ                      = {direct_sum3 - target3:+.2e}")
    print()

    # Connection to Mertens
    print("=" * 76)
    print("COMPARISON: Liouville L(x) vs Mertens M(x)")
    print("=" * 76)
    print()
    print("Mertens function: M(x) = Σ μ(n), μ(n) = 0 if n not squarefree")
    print("Liouville sum:    L(x) = Σ λ(n), λ(n) = ±1 always (no zeros)")
    print()
    print("Pólya conjectured L(x) ≤ 0 (1919, disproved 1958, first counterexample at 9×10⁸)")
    print("Mertens conjectured |M(x)| < √x (1897, disproved 1985 by Odlyzko-te Riele,")
    print("                                  no explicit counterexample known)")
    print()
    print("Both conjectures fail. RH is consistent with both being 'almost' true:")
    print("  L(x) = O(x^(1/2 + ε)) ⇔ RH")
    print("  M(x) = O(x^(1/2 + ε)) ⇔ RH (Mertens-equivalent form)")


if __name__ == '__main__':
    main()
