"""
Brun's theorem and Brun's constant.

Brun (1919): The sum
    B_2 = Σ_{p, p+2 both prime} (1/p + 1/(p+2))
      = (1/3 + 1/5) + (1/5 + 1/7) + (1/11 + 1/13) + (1/17 + 1/19) + ...
converges.

This is in striking contrast with Σ_p 1/p (diverges like log log x), and
it was the first proof that twin primes are "sparser" than all primes.
The convergence is a consequence of the Brun sieve.

**Brun's constant** B_2 is the value of this sum:
    B_2 = 1.902160583104...

Nicely (1994) computed B_2(10^14) ≈ 1.90216054. His search for this
constant famously uncovered the Pentium FDIV bug. Sebah-Gourdon (2002)
extended to 10^16 with B_2(10^16) ≈ 1.902160583.

The convergence of B_2(n) → B_2 is very slow — only logarithmically fast.
At n = 10^8, we expect B_2(n) ≈ 1.80, leaving a ~0.10 tail to extrapolate.

## Hardy-Littlewood tail

Assuming the Hardy-Littlewood twin prime conjecture:
    π_2(x) ~ 2 C_2 · x / (log x)²,  C_2 = 0.6601618158468...
we can estimate the tail:
    B_2 - B_2(n) ≈ Σ_{p > n, twin} 2/p
                ≈ 2 · ∫_n^∞ [2 C_2 / (log t)²] · (1/t) dt
                = 4 C_2 · ∫_n^∞ dt / (t (log t)²)
                = 4 C_2 / log n
So B_2 ≈ B_2(n) + 4 C_2 / log n.
"""
import numpy as np
from math import log
from sieve_core import sieve


def brun_partial_sums(N, checkpoints=None):
    """Return list of (x, B_2(x), count_twins) at each checkpoint ≤ N."""
    if checkpoints is None:
        checkpoints = [10**k for k in range(2, 9)]
    is_prime = sieve(N)
    checkpoints = sorted([c for c in checkpoints if c <= N])
    results = []
    partial = 0.0
    count = 0
    c_idx = 0
    for p in range(3, N - 1):
        if is_prime[p] and is_prime[p + 2]:
            partial += 1.0 / p + 1.0 / (p + 2)
            count += 1
        # Record at checkpoints when p crosses them
        while c_idx < len(checkpoints) and p == checkpoints[c_idx]:
            results.append((checkpoints[c_idx], partial, count))
            c_idx += 1
    while c_idx < len(checkpoints):
        results.append((checkpoints[c_idx], partial, count))
        c_idx += 1
    return results


def hl_tail_estimate(x, C_2=0.6601618158468695):
    """Hardy-Littlewood estimate for the tail B_2 - B_2(x)."""
    return 4 * C_2 / log(x)


def main():
    N = 10**8
    print(f"Brun's constant B_2 = Σ_twin primes (1/p + 1/(p+2))")
    print(f"Computing B_2(x) for x up to {N}")
    print("=" * 72)

    # Reference values
    B_2_reference = 1.902160583104  # Sebah-Gourdon best estimate
    C_2 = 0.6601618158468695  # Twin prime constant

    print(f"Reference: B_2 ≈ {B_2_reference}")
    print(f"Twin prime constant C_2 = {C_2}")
    print()

    checkpoints = [10**k for k in range(2, 9)]
    results = brun_partial_sums(N, checkpoints)

    print(f"{'x':>12} {'B_2(x)':>14} {'twins':>10} {'tail est':>12} "
          f"{'B_2 extrap':>14} {'Δ ref':>12}")
    print("-" * 80)
    for x, b, cnt in results:
        tail = hl_tail_estimate(x, C_2)
        extrap = b + tail
        delta = extrap - B_2_reference
        print(f"{x:>12} {b:>14.8f} {cnt:>10} {tail:>12.8f} "
              f"{extrap:>14.8f} {delta:>+12.8f}")

    print()
    print("The 'extrap' column adds the HL tail estimate 4·C_2/log x")
    print("to the partial sum. If the HL twin prime conjecture holds,")
    print("extrap → B_2 as x → ∞.")
    print()

    # Linear convergence of B_2(x) in 1/log x (regression)
    print("Regression: B_2(x) = B_2 - α / log x")
    print("-" * 72)
    xs = [r[0] for r in results if r[0] >= 10**4]
    bs = [r[1] for r in results if r[0] >= 10**4]
    inv_logs = [1.0 / log(x) for x in xs]
    # Least squares: B_2(x) = a + b * (1/log x)
    X = np.array(inv_logs)
    Y = np.array(bs)
    X_mean = X.mean()
    Y_mean = Y.mean()
    slope = ((X - X_mean) * (Y - Y_mean)).sum() / ((X - X_mean) ** 2).sum()
    intercept = Y_mean - slope * X_mean
    print(f"  Fit: B_2(x) ≈ {intercept:.6f} + ({slope:.4f}) / log x")
    print(f"  → B_2 (extrap from linear fit) ≈ {intercept:.6f}")
    print(f"  → HL predicts slope = -4 C_2 = {-4 * C_2:.4f}")
    print(f"  Reference B_2 = {B_2_reference}")
    print(f"  |fit - ref| = {abs(intercept - B_2_reference):.6f}")

    # Brun vs Mertens contrast
    print()
    print("CONTRAST: Σ 1/p over all primes (Euler) vs over twins (Brun)")
    print("-" * 72)
    is_prime = sieve(N)
    mertens = 0.0
    targets = [100, 1000, 10**4, 10**5, 10**6, 10**7, 10**8]
    t_idx = 0
    records = []
    for p in range(2, N + 1):
        if is_prime[p]:
            mertens += 1.0 / p
        if t_idx < len(targets) and p == targets[t_idx]:
            records.append((p, mertens))
            t_idx += 1
    twin_map = {r[0]: r[1] / 2 for r in results}  # twin-only side
    print(f"{'x':>12} {'Σ 1/p (all)':>16} {'Σ 1/p (twin)':>16} {'ratio':>10}")
    for x, m in records:
        tw = twin_map.get(x, 0.0)
        print(f"{x:>12} {m:>16.6f} {tw:>16.6f} {tw/m:>10.4f}")
    print()
    print("Σ 1/p (all) → log log x + M diverges (Euler 1737)")
    print("Σ 1/p (twin) → B_2/2 ≈ 0.951 converges (Brun 1919)")


if __name__ == '__main__':
    main()
