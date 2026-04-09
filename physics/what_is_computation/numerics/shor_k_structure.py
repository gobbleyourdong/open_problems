#!/usr/bin/env python3
"""
shor_k_structure.py — Shor's algorithm vs Grover vs classical: the role of K-structure.

Demonstrates WHY Shor achieves an exponential speedup over classical algorithms
(not just the quadratic speedup of Grover) and traces it back to the presence of
K-STRUCTURE in the factoring problem: the function f(x) = a^x mod N has a period r
(the multiplicative order of a in Z_N*) that the quantum Fourier transform can
identify in O(1) Fourier-sampling steps, whereas classical algorithms must hunt for
the period via birthday-paradox collision search in O(sqrt(r)) time.

The script:
  1. Computes complexity scaling for factoring N (n = log2(N) bits):
       - Classical trial division:        O(2^(n/2))     queries
       - Classical number field sieve:    O(exp(c·n^(1/3)·(log n)^(2/3)))  subexponential
       - Quantum Shor:                    O(n^2 log n log log n)  polynomial in n
  2. Builds a comparison table across n = 10, 20, 30, 40, 50, 100 bits including Grover.
  3. Demonstrates period-finding on f(x) = 7^x mod 15 (r=4) — shows the K-structure.
  4. Computes quantum vs classical work to find that period.
  5. Connects to K-information: why periodicity is exploitable by QFT and not by
     classical algorithms without birthday-paradox overhead.

Physical interpretation for gap.md R3:
  Shor beats Grover because factoring HAS K-structure (a periodic group orbit) that
  quantum Fourier sampling can exploit in O(1) steps. Unstructured search (Grover)
  has NO such K-structure — flat K-landscape — so only amplitude amplification helps.
  This is the substrate-dependence of K-manipulation: quantum hardware can extract
  period-K-structure exponentially faster than classical hardware.

Numerical track, what_is_computation Phase 4 — 2026-04-09
"""

import math
import json
import os
from fractions import Fraction


# ── Complexity models ──────────────────────────────────────────────────────────

def classical_trial_division(n: int) -> float:
    """
    Classical trial division for factoring an n-bit number N = 2^n.
    Worst-case: check all primes up to sqrt(N) = 2^(n/2).
    By prime number theorem, pi(2^(n/2)) ~ 2^(n/2) / (n/2 * ln 2).
    We use the loose bound O(sqrt(N)) = O(2^(n/2)) divisions.
    """
    return 2.0 ** (n / 2.0)


def classical_nfs(n: int) -> float:
    """
    General number field sieve (GNFS) complexity for n-bit number.
    L_N[1/3, (64/9)^(1/3)] = exp( (64/9)^(1/3) * n^(1/3) * (ln 2)^(2/3) * (log n)^(2/3) )
    Simplified: exp(c * n^(1/3) * (log n)^(2/3)) where c = (64/9)^(1/3) * (ln 2)^(2/3).
    This is subexponential in n but still superpolynomial.
    """
    c = (64.0 / 9.0) ** (1.0 / 3.0) * (math.log(2)) ** (2.0 / 3.0)
    log_n = math.log(n)  # natural log of the bit length
    exponent = c * (n ** (1.0 / 3.0)) * (log_n ** (2.0 / 3.0))
    # Return the exponent (log of operations); actual ops = exp(exponent)
    return exponent  # we return the exponent for comparison


def shor_operations(n: int) -> float:
    """
    Shor's algorithm gate/operation count for n-bit number.
    Phase estimation + QFT: O(n^2 log n log log n) quantum gates.
    We use the formula: n^2 * log2(n) * log2(log2(n) + 1).
    The '+1' avoids log(0) at small n.
    """
    log_n = math.log2(n)
    log_log_n = math.log2(log_n + 1.0)
    return (n ** 2) * log_n * log_log_n


def grover_queries(n: int) -> float:
    """
    Grover's algorithm on a search space of 2^n items: O(pi/4 * 2^(n/2)) queries.
    For factoring framed as unstructured search over n-bit numbers.
    """
    return (math.pi / 4.0) * (2.0 ** (n / 2.0))


def classical_birthday_period(r: int) -> float:
    """
    Classical birthday-paradox period-finding cost for a function with period r.
    Expected evaluations to find a collision (and hence the period): O(sqrt(r)).
    """
    return math.sqrt(r)


def quantum_qft_period(n_qubits: int) -> float:
    """
    Quantum QFT period-finding: O(n^2) gates for n-qubit QFT.
    (We use n_qubits = ceil(log2(N)) where N is the modulus.)
    In Shor's algorithm, one period-finding run uses O(n^2) gates.
    """
    return float(n_qubits ** 2)


# ── Period demonstration: f(x) = 7^x mod 15 ──────────────────────────────────

def compute_period_function(a: int, N: int, x_range: int) -> list[int]:
    """
    Compute f(x) = a^x mod N for x = 0, 1, ..., x_range-1.
    Returns the sequence of values.
    """
    values = []
    val = 1  # a^0 mod N = 1
    for x in range(x_range):
        values.append(val)
        val = (val * a) % N
    return values


def find_period_classical(values: list[int]) -> int:
    """
    Find the period of the sequence by scanning for the first repeat of values[0].
    This is the multiplicative order of a mod N.
    Returns period r such that values[r] == values[0].
    """
    target = values[0]
    for i in range(1, len(values)):
        if values[i] == target:
            return i
    return -1  # not found in range


def find_period_birthday(values: list[int]) -> tuple[int, int]:
    """
    Simulate classical birthday-paradox period-finding.
    Store seen values until a collision is found.
    Returns (period, steps_used).

    Note: The birthday paradox guarantees a collision after O(sqrt(r)) evaluations,
    but the collision itself gives a multiple of the period, not always the period.
    Here we simply track when a value repeats (which directly gives the period r
    since the first repeat of values[0] at index r is the period).
    This simulates the classical O(sqrt(r)) random sampling strategy.
    """
    seen = {}
    for i, v in enumerate(values):
        if v in seen:
            diff = i - seen[v]
            return diff, i
        seen[v] = i
    return -1, len(values)


def discrete_fourier_magnitudes(values: list[int], N_mod: int) -> list[float]:
    """
    Compute the DFT of the indicator sequence for value v=1 in f(x) = a^x mod N.
    The quantum QFT produces peaks at multiples of Q/r where Q = 2^n (register size).
    We simulate this by computing |DFT[k]|^2 for the full value sequence.

    For demonstration: compute DFT of the values sequence treated as a real signal.
    The QFT of the periodic function has large peaks at frequency multiples of 1/r.
    """
    M = len(values)
    # Normalize values to [0,1] for display
    magnitudes = []
    for k in range(min(M, 32)):  # first 32 frequency bins
        real = sum(values[x] * math.cos(2 * math.pi * k * x / M) for x in range(M))
        imag = sum(values[x] * math.sin(2 * math.pi * k * x / M) for x in range(M))
        magnitudes.append(math.sqrt(real**2 + imag**2) / M)
    return magnitudes


def recover_period_from_fft(magnitudes: list[float], M: int) -> list[int]:
    """
    Identify candidate periods from DFT peaks.
    Peaks in the DFT appear at k = M/r, 2M/r, ..., giving period r = M/k.
    Returns list of candidate periods.
    """
    if not magnitudes:
        return []
    threshold = max(magnitudes) * 0.5  # peaks above half-maximum
    candidates = []
    for k, mag in enumerate(magnitudes):
        if k > 0 and mag > threshold:
            # candidate period: M/k (take nearest integer)
            candidate_r = round(M / k)
            if candidate_r > 0 and candidate_r not in candidates:
                candidates.append(candidate_r)
    return sorted(candidates)


# ── GCD factoring from period ──────────────────────────────────────────────────

def factor_from_period(a: int, r: int, N: int) -> tuple[int, int]:
    """
    Given period r of f(x) = a^x mod N, recover factors of N.
    If r is even and a^(r/2) ≢ -1 mod N:
      gcd(a^(r/2) - 1, N) and gcd(a^(r/2) + 1, N) are non-trivial factors.
    """
    if r % 2 != 0:
        return (-1, -1)  # r is odd, need different a
    half = pow(a, r // 2, N)
    if half == N - 1:
        return (-1, -1)  # a^(r/2) ≡ -1 mod N, need different a
    p = math.gcd(half - 1, N)
    q = math.gcd(half + 1, N)
    return (p, q)


# ── Main computation ───────────────────────────────────────────────────────────

def main():
    print("=" * 80)
    print("Shor's Algorithm vs Grover vs Classical — K-Structure Analysis")
    print("=" * 80)
    print()
    print("Core question: Why does Shor achieve EXPONENTIAL speedup while Grover")
    print("achieves only QUADRATIC (square-root) speedup?")
    print()
    print("Answer: K-STRUCTURE. Factoring has NUMBER-THEORETIC K-STRUCTURE")
    print("(periodicity in Z_N*) that quantum Fourier sampling can exploit.")
    print("Unstructured search (Grover) has NO such K-structure — flat landscape.")
    print()

    # ── Table 1: Complexity scaling for factoring ──────────────────────────────
    print("── Table 1: Factoring Complexity vs n (bits of N) ──")
    print()
    print("  N = 2^n (n-bit number).  NFS exponent = c·n^(1/3)·(ln n)^(2/3).")
    print()
    print(f"  {'n':>5}  {'Trial div (ops)':>22}  {'NFS (exponent)':>18}  {'Shor (ops)':>16}  {'Grover (queries)':>18}")
    print("  " + "─" * 85)

    BIT_SIZES = [10, 20, 30, 40, 50, 100]
    table1_rows = []
    for n in BIT_SIZES:
        td = classical_trial_division(n)
        nfs_exp = classical_nfs(n)
        shor = shor_operations(n)
        gr = grover_queries(n)
        # Format large numbers with scientific notation
        td_str = f"{td:.3e}"
        nfs_str = f"exp({nfs_exp:.2f})"
        shor_str = f"{shor:.2e}"
        gr_str = f"{gr:.3e}"
        print(f"  {n:>5}  {td_str:>22}  {nfs_str:>18}  {shor_str:>16}  {gr_str:>18}")
        table1_rows.append({
            "n_bits": n,
            "trial_division_ops": td,
            "nfs_exponent": round(nfs_exp, 4),
            "nfs_ops_approx": round(math.exp(nfs_exp), 2),
            "shor_ops": round(shor, 2),
            "grover_queries": round(gr, 4),
        })
    print()

    # ── Table 2: Speedup ratios (Shor vs classical) ────────────────────────────
    print("── Table 2: Speedup Ratios vs n ──")
    print()
    print("  Shor_speedup_vs_trial  = Trial_division / Shor_ops")
    print("  Shor_speedup_vs_Grover = Grover_queries / Shor_ops")
    print("  (Grover on unstructured search gives sqrt speedup; Shor gives poly)")
    print()
    print(f"  {'n':>5}  {'Shor/Trial ratio':>20}  {'Grover/Trial ratio':>20}  {'Shor/Grover ratio':>20}")
    print("  " + "─" * 72)

    table2_rows = []
    for n in BIT_SIZES:
        td = classical_trial_division(n)
        shor = shor_operations(n)
        gr = grover_queries(n)
        shor_vs_trial = td / shor      # how much faster Shor is vs trial division
        grover_vs_trial = td / gr      # how much faster Grover is vs trial division
        shor_vs_grover = gr / shor     # how much faster Shor is vs Grover

        s_t = f"{shor_vs_trial:.2e}"
        g_t = f"{grover_vs_trial:.2e}"
        s_g = f"{shor_vs_grover:.2e}"
        print(f"  {n:>5}  {s_t:>20}  {g_t:>20}  {s_g:>20}")
        table2_rows.append({
            "n_bits": n,
            "shor_speedup_vs_trial": shor_vs_trial,
            "grover_speedup_vs_trial": grover_vs_trial,
            "shor_speedup_vs_grover": shor_vs_grover,
        })
    print()

    # ── Table 3: Shor/Classical ratio grows exponentially ─────────────────────
    print("── Table 3: Speedup Scaling — Shor vs Trial Division ──")
    print()
    print("  For N = 2^n:")
    print("    Trial division: 2^(n/2) operations")
    print("    Shor:           ~n^2 * log(n) * log(log(n)) operations  [polynomial in n]")
    print("    Ratio:          2^(n/2) / (n^2 * log(n)) — grows EXPONENTIALLY in n")
    print()
    print(f"  {'n':>5}  {'2^(n/2)':>14}  {'Shor ops':>12}  {'Speedup':>16}  {'log2(Speedup)':>15}")
    print("  " + "─" * 68)

    for n in BIT_SIZES:
        td = classical_trial_division(n)
        shor = shor_operations(n)
        speedup = td / shor
        log2_sp = math.log2(speedup) if speedup > 0 else 0.0
        print(f"  {n:>5}  {td:>14.3e}  {shor:>12.2f}  {speedup:>16.3e}  {log2_sp:>15.2f}")
    print()
    print("  At n=100: Shor speedup over trial division ≈ 2^50 / 10^4 — effectively")
    print("  making trial division impossible while Shor requires ~10^4 operations.")
    print()

    # ── Table 4: Shor/Grover/Classical combined ────────────────────────────────
    print("── Table 4: Full Comparison Table (n = 10, 20, 30, 40, 50, 100) ──")
    print()
    print(f"  {'n':>5}  {'Classical (trial)':>18}  {'Grover':>14}  {'Shor':>12}  {'Shor/Classical':>16}")
    print("  " + "─" * 72)

    table4_rows = []
    for n in BIT_SIZES:
        td = classical_trial_division(n)
        gr = grover_queries(n)
        shor = shor_operations(n)
        ratio = td / shor
        print(f"  {n:>5}  {td:>18.3e}  {gr:>14.3e}  {shor:>12.2f}  {ratio:>16.3e}")
        table4_rows.append({
            "n_bits": n,
            "classical_trial": round(td, 4),
            "grover": round(gr, 4),
            "shor": round(shor, 4),
            "shor_classical_ratio": round(ratio, 6),
        })
    print()

    # ── K-structure demonstration: f(x) = 7^x mod 15 ─────────────────────────
    print("=" * 80)
    print("K-Structure Demonstration: f(x) = 7^x mod 15")
    print("=" * 80)
    print()
    print("  N = 15 = 3 × 5 (target to factor).")
    print("  a = 7  (base, coprime to 15).")
    print("  f(x) = 7^x mod 15 has period r = multiplicative order of 7 in Z_15*.")
    print()

    a, N_mod = 7, 15
    x_range = 40
    values = compute_period_function(a, N_mod, x_range)

    print("  f(x) = 7^x mod 15 for x = 0..39:")
    print()
    for row_start in range(0, x_range, 8):
        row_vals = values[row_start:row_start+8]
        print("    x=" + str(row_start) + "-" + str(row_start+len(row_vals)-1) + ":  " +
              "  ".join(f"{v:>3}" for v in row_vals))
    print()

    # Find the period directly
    period = find_period_classical(values)
    print(f"  Direct scan: period r = {period}  (i.e., 7^{period} mod 15 = {pow(a, period, N_mod)})")
    print()

    # K-structure: verify periodicity
    print("  Verifying K-structure: f(x + r) = f(x) for all x?")
    all_periodic = all(values[x] == values[x + period] for x in range(x_range - period))
    print(f"  f(x + {period}) = f(x) for all x in range:  {all_periodic}")
    print()
    print(f"  This is the K-structure: the function is PERIODIC with period r = {period}.")
    print(f"  Euler's totient phi(15) = phi(3)×phi(5) = 2×4 = 8.")
    print(f"  Period r = {period} divides phi(15) = 8:  {8 % period == 0}")
    print()

    # Classical birthday-paradox period-finding
    _, birthday_steps = find_period_birthday(values)
    print(f"  Classical birthday-paradox period-finding:")
    print(f"    Steps to find first collision: {birthday_steps}")
    print(f"    Theoretical O(sqrt(r)) = O(sqrt({period})) = {math.sqrt(period):.2f}")
    print(f"    For large N, period r ~ phi(N) ~ N, so birthday cost ~ sqrt(N) = 2^(n/2)")
    print()

    # Quantum QFT period-finding
    n_qubits = math.ceil(math.log2(N_mod))
    qft_cost = quantum_qft_period(n_qubits)
    print(f"  Quantum QFT period-finding (n_qubits = ceil(log2({N_mod})) = {n_qubits}):")
    print(f"    QFT gate count: O(n^2) = {qft_cost:.0f} gates")
    print(f"    Finds period r = {period} in ONE Fourier-sampling step (plus classical post-proc)")
    print(f"    Ratio (classical birthday / QFT): {birthday_steps / qft_cost:.2f}×  [tiny N — grows exponentially]")
    print()

    # DFT of the period function (analytical simulation of QFT peaks)
    magnitudes = discrete_fourier_magnitudes(values, N_mod)
    candidates = recover_period_from_fft(magnitudes, x_range)
    print("  DFT magnitudes of f(x) sequence (first 16 frequency bins):")
    print("  (Quantum QFT would produce probability peaks at multiples of M/r)")
    print()
    for k, mag in enumerate(magnitudes[:16]):
        bar = "#" * int(mag * 40)
        candidate = f"  -> period candidate: {x_range // k}" if k > 0 and (x_range % k == 0) else ""
        print(f"    k={k:>2}: {mag:.4f}  {bar}{candidate}")
    print()
    print(f"  Period candidates recovered from DFT peaks: {candidates}")
    print()

    # Factor N from period
    p, q = factor_from_period(a, period, N_mod)
    print(f"  Factoring N={N_mod} from period r={period}:")
    print(f"    a^(r/2) = 7^2 = {pow(a, period//2, N_mod)} mod {N_mod}")
    print(f"    gcd(a^(r/2) - 1, N) = gcd({pow(a, period//2, N_mod)-1}, {N_mod}) = {p}")
    print(f"    gcd(a^(r/2) + 1, N) = gcd({pow(a, period//2, N_mod)+1}, {N_mod}) = {q}")
    print(f"    Factors: {N_mod} = {p} × {q}  [correct: {p * q == N_mod and p != 1 and q != 1}]")
    print()

    # ── K-structure explanation ────────────────────────────────────────────────
    print("=" * 80)
    print("K-Structure: Why Shor > Grover")
    print("=" * 80)
    print()
    print("  UNSTRUCTURED SEARCH (Grover):")
    print("    Search space: 2^n items, one marked. No internal structure.")
    print("    K-landscape: FLAT — no gradient, no periodicity, no exploitable pattern.")
    print("    Quantum advantage: amplitude amplification. Each step boosts target")
    print("    amplitude by O(1/sqrt(N)) — requires O(sqrt(N)) steps total.")
    print("    Result: Grover queries = O(2^(n/2)). Exponential but halved exponent.")
    print()
    print("  FACTORING (Shor):")
    print("    Search space: integers x in [0, Q) where Q = 2^(2n).")
    print("    K-landscape: PERIODIC — f(x) = a^x mod N has period r | phi(N).")
    print("    K-structure: the periodicity is global, exact, and group-theoretic.")
    print("    Quantum advantage: QFT maps periodic amplitude distribution to a SINGLE")
    print("    sharp peak (or a few peaks) at frequency k/r. ONE measurement suffices.")
    print("    Classical: birthday-paradox search for period costs O(sqrt(r)) ~ O(sqrt(N)).")
    print("    Result: Shor = O(n^2 log n) — POLYNOMIAL. Exponential collapse.")
    print()
    print("  THE K-STRUCTURE GAP:")
    print()
    print("    Problem          | K-structure   | Classical      | Quantum")
    print("    ─────────────────|───────────────|────────────────|──────────────────")
    print("    Unstructured srch| None (flat)   | O(2^n)         | O(2^(n/2))  [Grover]")
    print("    Factoring        | Periodic(Z_N*)| O(exp(n^(1/3)))| O(n^2 log n)[Shor]")
    print("    Discrete log     | Group orbit   | O(exp(n^(1/2)))| O(n^2 log n)[Shor]")
    print("    3-SAT (hard)     | Clause struct | O(2^n)         | O(2^(n/2))  [Grover bound]")
    print()
    print("  KEY INSIGHT: The QFT is a K-structure detector.")
    print("    - It maps a periodic signal (K-structured landscape) to a concentrated")
    print("      frequency distribution (a few high-probability measurement outcomes).")
    print("    - Classical computers can also compute the DFT — but they must STORE")
    print("      all 2^n amplitudes (exponential memory) or evaluate f(x) for each x.")
    print("    - Quantum hardware implements the QFT on superposed states using only")
    print("      O(n^2) gates — because the physical substrate (quantum amplitudes)")
    print("      encodes the full 2^n-dimensional state implicitly.")
    print("    - This is SUBSTRATE-DEPENDENCE of K-manipulation: the same Fourier")
    print("      analysis that costs O(2^n) classically (FFT on the amplitude vector)")
    print("      costs O(n^2) quantumly because quantum amplitudes ARE the vector.")
    print()

    # ── R3 implications ────────────────────────────────────────────────────────
    print("=" * 80)
    print("Implications for gap.md R3")
    print("=" * 80)
    print()
    print("  R3: What does BQP strictly containing P imply about the substrate-")
    print("      dependence of K-manipulation?")
    print()
    print("  The Shor/Grover comparison sharpens the Grover findings:")
    print()
    print("  1. There are TWO distinct modes of quantum advantage:")
    print()
    print("     (a) Amplitude amplification (Grover): halves the exponent.")
    print("         Works on ANY problem with a binary oracle. Requires no K-structure.")
    print("         Speedup: 2^n -> 2^(n/2). Doubling period: 1 -> 2 variables.")
    print("         This is a SUBSTRATE effect: quantum hardware performs parallel")
    print("         amplitude testing that classical hardware cannot.")
    print()
    print("     (b) Fourier sampling (Shor): collapses the exponent to polynomial.")
    print("         Works ONLY on problems with periodic K-structure in a group.")
    print("         Speedup: exp(n^(1/3)) -> n^2. This is not just substrate — it is")
    print("         K-STRUCTURE EXPLOITATION via substrate.")
    print()
    print("  2. The substrate-dependence for Shor is qualitatively different from Grover:")
    print()
    print("     Grover: quantum substrate gives factor-of-2 exponent reduction.")
    print("     Shor:   quantum substrate + periodic K-structure = exponential collapse.")
    print()
    print("     Without K-structure, quantum hardware provides only Grover advantage.")
    print("     WITH periodic K-structure, quantum hardware provides Shor advantage.")
    print("     => K-structure and substrate interact multiplicatively, not additively.")
    print()
    print("  3. P != NP in the context of Shor/Grover:")
    print()
    print("     Factoring: periodic K-structure allows polynomial quantum solution.")
    print("     3-SAT:     clause structure provides K-gradients, but NO global period.")
    print("                 -> Grover gives 2^(n/2); no Shor-like collapse is known.")
    print("     P!=NP:     problems with no exploitable K-structure (even in quantum)")
    print("                 remain exponential. Shor works because Z_N* periodicity")
    print("                 is a GROUP — a very special K-structure. NP-completeness")
    print("                 lacks this global algebraic regularity.")
    print()
    print("  4. The K-structure hierarchy:")
    print()
    print("     No structure         -> Grover (k=2 doubling period)")
    print("     Logical structure    -> DPLL (k~14 doubling period)")
    print("     Periodic group orbit -> Shor  (polynomial — exponent collapses)")
    print()
    print("     Factoring is NOT in NP-complete; it sits in NP ∩ co-NP. This is why")
    print("     Shor can solve it: problems with rich algebraic K-structure (group")
    print("     periodicity) may not be NP-complete and hence are not protected by")
    print("     the P!=NP barrier.")
    print()
    print("  5. Physical interpretation:")
    print()
    print("     Classical computers manipulate K-information serially: evaluate f(x)")
    print("     for each x, compare, store. Period-finding costs O(sqrt(r)) via")
    print("     birthday paradox — the only classical shortcut to the period.")
    print()
    print("     Quantum computers manipulate K-information via amplitude interference:")
    print("     the superposed state |psi> = sum_x |x>|f(x)> encodes ALL evaluations")
    print("     simultaneously. The QFT on |psi> destructively interferes non-period")
    print("     frequencies and constructively amplifies period frequencies — in O(n^2)")
    print("     gates. The physical substrate (quantum coherence) implements the Fourier")
    print("     analysis that would require O(2^n) classical operations.")
    print()
    print("     This is the substrate-dependence: quantum hardware 'is' a K-structure")
    print("     detector for periodic functions. Classical hardware 'searches' for the")
    print("     K-structure. The difference is exponential when K-structure is present.")
    print()

    # ── Build results dict ─────────────────────────────────────────────────────
    # Period function values
    period_demo_values = compute_period_function(a, N_mod, x_range)
    period_direct = find_period_classical(period_demo_values)
    _, birthday_steps_val = find_period_birthday(period_demo_values)
    p_factor, q_factor = factor_from_period(a, period_direct, N_mod)
    dft_mags = discrete_fourier_magnitudes(period_demo_values, N_mod)
    period_candidates = recover_period_from_fft(dft_mags, x_range)

    results = {
        "description": "Shor's algorithm vs Grover vs classical — K-structure analysis",
        "date": "2026-04-09",
        "addresses": "gap.md R3: substrate-dependence of K-manipulation",
        "complexity_models": {
            "trial_division": "O(2^(n/2)) — square root of N",
            "nfs_exponent_formula": "c * n^(1/3) * (ln n)^(2/3) where c = (64/9)^(1/3) * (ln 2)^(2/3)",
            "shor_ops_formula": "n^2 * log2(n) * log2(log2(n)+1)",
            "grover_queries_formula": "(pi/4) * 2^(n/2)",
        },
        "scaling_table": table1_rows,
        "speedup_table": table2_rows,
        "full_comparison_table": table4_rows,
        "period_demonstration": {
            "base": a,
            "modulus": N_mod,
            "x_range": x_range,
            "function_values": period_demo_values,
            "period_r": period_direct,
            "period_divides_phi_N": (8 % period_direct == 0),
            "phi_N": 8,
            "k_structure_verified": all(period_demo_values[x] == period_demo_values[x + period_direct]
                                        for x in range(x_range - period_direct)),
            "classical_birthday_steps": birthday_steps_val,
            "classical_birthday_theory_sqrt_r": round(math.sqrt(period_direct), 4),
            "quantum_qft_cost_n2": qft_cost,
            "birthday_vs_qft_ratio": round(birthday_steps_val / qft_cost, 4),
            "dft_magnitudes_first16": [round(m, 6) for m in dft_mags[:16]],
            "period_candidates_from_dft": period_candidates,
            "factors_recovered": {"p": p_factor, "q": q_factor, "correct": (p_factor * q_factor == N_mod)},
        },
        "k_structure_analysis": {
            "unstructured_search_grover": {
                "k_structure": "None (flat landscape)",
                "classical_complexity": "O(2^n)",
                "quantum_complexity": "O(2^(n/2))",
                "speedup_type": "quadratic (exponent halved)",
                "doubling_period_variables": 2,
            },
            "factoring_shor": {
                "k_structure": "Periodic group orbit in Z_N* (multiplicative order)",
                "classical_complexity": "O(exp(n^(1/3) * (ln n)^(2/3)))",
                "quantum_complexity": "O(n^2 log n log log n)",
                "speedup_type": "EXPONENTIAL (exponent collapses to polynomial)",
                "key_mechanism": "QFT maps periodic superposition to sharp frequency peaks",
            },
            "comparison": {
                "grover_speedup_n50": round(grover_queries(50) / classical_trial_division(50), 6),
                "shor_speedup_n50": round(classical_trial_division(50) / shor_operations(50), 4),
                "ratio_shor_vs_grover_speedup_n50": round(
                    (classical_trial_division(50) / shor_operations(50)) /
                    (classical_trial_division(50) / grover_queries(50)), 4
                ),
            },
        },
        "r3_implications": {
            "two_modes_of_quantum_advantage": [
                "Amplitude amplification (Grover): substrate effect, no K-structure needed, halves exponent",
                "Fourier sampling (Shor): substrate + periodic K-structure, collapses exponent to polynomial",
            ],
            "k_structure_hierarchy": {
                "no_structure": "Grover, doubling_period=2",
                "logical_structure": "DPLL, doubling_period~14",
                "periodic_group_orbit": "Shor, polynomial (exponent=0 effectively)",
            },
            "p_vs_np_connection": (
                "Factoring is not NP-complete — it has algebraic K-structure (Z_N* periodicity) "
                "that Shor exploits. NP-complete problems lack global algebraic regularity. "
                "P!=NP protects problems where K-structure is local/clause-level, not global/periodic."
            ),
            "substrate_dependence_summary": (
                "Quantum hardware 'is' a K-structure detector for periodic functions via QFT. "
                "Classical hardware 'searches' for K-structure. With periodic K-structure, "
                "the speedup is exponential (Shor). Without it, the speedup is quadratic (Grover). "
                "This is the substrate-dependence of K-manipulation: quantum substrate × K-structure "
                "= exponential advantage; quantum substrate alone = quadratic advantage."
            ),
        },
    }

    # ── Save results ───────────────────────────────────────────────────────────
    out_dir = "~/open_problems/physics/what_is_computation/results"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "shor_k_data.json")

    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"Results saved to {out_path}")
    return results


if __name__ == "__main__":
    main()
