"""
Apéry's constant ζ(3) and its irrationality.

ζ(3) = Σ_{n=1}^∞ 1/n³ ≈ 1.20205690315959428539973816151...

UNTIL 1978, it was unknown whether ζ(3) was rational or irrational.

APÉRY (1978): ζ(3) is IRRATIONAL.

Apéry's proof was a tour-de-force of formal power series, hypergeometric
identities, and continued fraction theory. The key tool was the
**Apéry-style alternating series**:
    ζ(3) = (5/2) · Σ_{n=1}^∞ (-1)^(n-1) / (n³ · binomial(2n, n))

This series converges EXPONENTIALLY (the n-th term is ~ 2^(-2n)),
much faster than the direct sum Σ 1/n³ which converges as O(1/N²).

The IRRATIONALITY proof uses Apéry's recurrence:
    a_0 = 1, a_1 = 5
    b_0 = 0, b_1 = 6
    n³ a_n = (34n³ - 51n² + 27n - 5) a_{n-1} - (n-1)³ a_{n-2}
    n³ b_n = (34n³ - 51n² + 27n - 5) b_{n-1} - (n-1)³ b_{n-2}

Then b_n / a_n → ζ(3) very rapidly. The trick is that a_n, b_n grow like
α^n where α ≈ 22.95, while the difference |b_n/a_n - ζ(3)| decays like
α^(-2n), giving a Diophantine "good approximation" that can only be
satisfied by an irrational ζ(3).

STATUS OF OTHER ODD ZETAS:
- ζ(5), ζ(7), ζ(9), ... — IRRATIONALITY UNKNOWN.
- Rivoal (2000): infinitely many ζ(2k+1) are irrational.
- Zudilin (2001): at least one of ζ(5), ζ(7), ζ(9), ζ(11) is irrational.
- The status of any specific ζ(2k+1) for k ≥ 2 remains OPEN.

This script computes ζ(3) by THREE methods:
1. Direct sum Σ 1/n³  (slow, O(1/N²) convergence)
2. Apéry's alternating series  (exponential convergence)
3. Apéry's recurrence  (exponential convergence in a different sense)
And compares all three to high-precision mpmath ζ(3).
"""
import mpmath
from math import comb


def direct_sum(N):
    """Direct: ζ(3) ≈ Σ_{n=1}^N 1/n³. Convergence O(1/N²)."""
    return sum(1.0 / n ** 3 for n in range(1, N + 1))


def apery_alternating_sum(N):
    """Apéry's accelerated series:
    ζ(3) = (5/2) Σ_{n=1}^∞ (-1)^(n-1) / (n³ · C(2n, n))
    Truncated to n ≤ N. Convergence O(2^(-2N))."""
    s = 0.0
    for n in range(1, N + 1):
        sign = 1.0 if n % 2 == 1 else -1.0
        s += sign / (n ** 3 * comb(2 * n, n))
    return 2.5 * s


def apery_recurrence(N):
    """Compute b_N / a_N where a, b satisfy Apéry's recurrence.
    Uses mpmath for b_n (which are rational, not integer).
    a_n are integers; b_n involve harmonic sums."""
    mpmath.mp.dps = 40
    if N == 0:
        return 0.0
    # a_n: integers, use the recurrence exactly
    a = [mpmath.mpf(1), mpmath.mpf(5)]
    b = [mpmath.mpf(0), mpmath.mpf(6)]
    if N == 1:
        return float(b[1] / a[1])
    for n in range(2, N + 1):
        coeff = 34 * n ** 3 - 51 * n ** 2 + 27 * n - 5
        n3 = n ** 3
        nm13 = (n - 1) ** 3
        a_n = (coeff * a[-1] - nm13 * a[-2]) / n3
        b_n = (coeff * b[-1] - nm13 * b[-2]) / n3
        a.append(a_n)
        b.append(b_n)
    return float(b[N] / a[N])


def main():
    print("Apéry's constant ζ(3) — three methods")
    print("=" * 76)

    # Reference value (50 dps)
    mpmath.mp.dps = 50
    ref = float(mpmath.zeta(3))
    ref_high_prec = mpmath.zeta(3)
    print(f"Reference (mpmath @ 50 dps): {mpmath.nstr(ref_high_prec, 30)}")
    print(f"Reference (float):           {ref}")
    print()

    # ============================
    # Method 1: Direct sum
    # ============================
    print("METHOD 1: Direct sum ζ(3) ≈ Σ_{n=1}^N 1/n³")
    print("Convergence rate: error ~ 1/(2N²) (Euler-Maclaurin tail)")
    print(f"{'N':>10} {'estimate':>22} {'error':>14}")
    print("-" * 50)
    for N in [10, 100, 1000, 10000, 100000, 1000000]:
        est = direct_sum(N)
        err = abs(est - ref)
        print(f"{N:>10} {est:>22.16f} {err:>14.2e}")
    print()

    # ============================
    # Method 2: Apéry's alternating series
    # ============================
    print("METHOD 2: Apéry's alternating series")
    print("ζ(3) = (5/2) Σ (-1)^(n-1) / (n³ · binomial(2n, n))")
    print("Convergence rate: exponential, ~ 2^(-2N)")
    print(f"{'N':>6} {'estimate':>22} {'error':>14}")
    print("-" * 46)
    for N in [3, 5, 10, 15, 20, 25, 30, 40]:
        est = apery_alternating_sum(N)
        err = abs(est - ref)
        print(f"{N:>6} {est:>22.16f} {err:>14.2e}")
    print()

    # ============================
    # Method 3: Apéry's recurrence
    # ============================
    print("METHOD 3: Apéry's recurrence")
    print("a_n, b_n via integer recurrence; b_n / a_n → ζ(3)")
    print("Convergence rate: |b_n/a_n - ζ(3)| ~ α^(-2n), α ≈ 22.95")
    print(f"{'N':>6} {'b_N / a_N':>22} {'error':>14}")
    print("-" * 46)
    for N in [1, 2, 3, 4, 5, 7, 10, 15]:
        est = apery_recurrence(N)
        err = abs(est - ref)
        print(f"{N:>6} {est:>22.16f} {err:>14.2e}")
    print()

    # ============================
    # Convergence comparison
    # ============================
    print("=" * 76)
    print("CONVERGENCE COMPARISON: digits of accuracy after various 'effort'")
    print("=" * 76)
    print()
    print(f"{'method':>25} {'1 digit':>12} {'5 digits':>12} {'10 digits':>12} "
          f"{'15 digits':>12}")
    print("-" * 76)

    # For each method, find how many terms are needed for various accuracies
    def find_steps(method_fn, target_err, max_steps=10**7):
        for n in range(1, max_steps + 1):
            err = abs(method_fn(n) - ref)
            if err < target_err:
                return n
            if n > 1000 and method_fn == direct_sum:
                # Too slow; use closed-form estimate for direct sum
                # error ≈ 1/(2N²)
                pass
        return None

    # For direct sum, use the closed-form 1/(2N²)
    targets = [1e-1, 1e-5, 1e-10, 1e-15]
    direct_needs = [int((1 / (2 * t)) ** 0.5 + 1) for t in targets]
    apery_alt_needs = []
    for t in targets:
        for n in range(1, 100):
            if abs(apery_alternating_sum(n) - ref) < t:
                apery_alt_needs.append(n)
                break
    apery_rec_needs = []
    for t in targets:
        for n in range(1, 100):
            if abs(apery_recurrence(n) - ref) < t:
                apery_rec_needs.append(n)
                break

    print(f"{'Direct Σ 1/n³':>25} {direct_needs[0]:>12} {direct_needs[1]:>12} "
          f"{direct_needs[2]:>12} {direct_needs[3]:>12}")
    print(f"{'Apéry alt series':>25} {apery_alt_needs[0]:>12} {apery_alt_needs[1]:>12} "
          f"{apery_alt_needs[2]:>12} {apery_alt_needs[3]:>12}")
    print(f"{'Apéry recurrence':>25} {apery_rec_needs[0]:>12} {apery_rec_needs[1]:>12} "
          f"{apery_rec_needs[2]:>12} {apery_rec_needs[3]:>12}")
    print()
    print("Apéry's accelerated series gives ~2 digits per step (one binomial),")
    print("while the direct sum needs ~10^15/2 terms for 15-digit accuracy.")
    print("The acceleration ratio: ~10^14 fewer operations.")
    print()

    # Status of other zeta values
    print("=" * 76)
    print("STATUS OF ODD ZETA IRRATIONALITY")
    print("=" * 76)
    print()
    print("ζ(2)  = π²/6           PROVEN irrational (Euler 1735, Lambert 1761)")
    print("ζ(3)  = 1.20205690...   PROVEN irrational (Apéry 1978)")
    print("ζ(4)  = π⁴/90          PROVEN irrational")
    print("ζ(5)  = 1.03692775...   IRRATIONALITY OPEN")
    print("ζ(7)  = 1.00834927...   IRRATIONALITY OPEN")
    print("ζ(9)  = 1.00200839...   IRRATIONALITY OPEN")
    print("ζ(11) = 1.00049418...   IRRATIONALITY OPEN")
    print()
    print("Partial results:")
    print("- Rivoal (2000): infinitely many ζ(2k+1) are irrational.")
    print("- Zudilin (2001): at least one of {ζ(5), ζ(7), ζ(9), ζ(11)} is irrational.")
    print()
    print("These are all 'qualitative' results — they tell us SOME odd zetas")
    print("must be irrational, but not which ones. ζ(3) remains the only odd")
    print("zeta whose irrationality is proven INDIVIDUALLY.")


if __name__ == '__main__':
    main()
