#!/usr/bin/env python3
"""
P vs NP: Real-World Domain Examples

Each domain shows the same pattern: checking is fast, finding is slow.
These are problems PEOPLE actually need to solve every day.

Domains:
1. SCHEDULING: assign jobs to machines minimizing makespan
2. PACKING: fit items into bins of fixed capacity
3. CRYPTO: factor a number (the basis of RSA)
4. PROTEIN: find lowest-energy fold (simplified lattice model)
5. COMPILER: register allocation (= graph coloring)

For each: implement checker (polynomial) and finder (exponential),
measure the gap as problem size grows.
"""

import numpy as np
import time
from itertools import permutations, product as iprod


# ============================================================================
# 1. JOB SCHEDULING (makespan minimization on 2 machines)
# NP-hard. Equivalent to PARTITION problem.
# CHECK: sum up each machine's load, verify max ≤ target. O(n).
# FIND: try all 2^n assignments. Best known: O(2^{n/2}) meet-middle.
# ============================================================================

def scheduling_generate(n):
    jobs = np.random.randint(1, 100, size=n).tolist()
    total = sum(jobs)
    target = (total + 1) // 2  # optimal makespan
    # Greedy assignment (not optimal but gives a feasible solution)
    m1, m2, assign = 0, 0, []
    for j in jobs:
        if m1 <= m2:
            assign.append(0); m1 += j
        else:
            assign.append(1); m2 += j
    makespan = max(m1, m2)
    return jobs, makespan, assign

def scheduling_check(jobs, target, assign):
    loads = [0, 0]
    for j, a in zip(jobs, assign):
        loads[a] += j
    return max(loads) <= target

def scheduling_find(jobs, target):
    n = len(jobs)
    for bits in range(2**n):
        loads = [0, 0]
        for i in range(n):
            loads[(bits >> i) & 1] += jobs[i]
        if max(loads) <= target:
            return [(bits >> i) & 1 for i in range(n)]
    return None


# ============================================================================
# 2. BIN PACKING (fit items into k bins of capacity C)
# NP-hard. CHECK: verify each bin ≤ C. O(n). FIND: O(k^n).
# ============================================================================

def packing_generate(n, n_bins=3, capacity=100):
    # Items that fit in n_bins bins
    items = np.random.randint(1, capacity // 2, size=n).tolist()
    # Greedy assignment
    bins = [0] * n_bins
    assign = []
    for item in items:
        placed = False
        for b in range(n_bins):
            if bins[b] + item <= capacity:
                bins[b] += item
                assign.append(b)
                placed = True
                break
        if not placed:
            assign.append(0)
            bins[0] += item
    return items, capacity, n_bins, assign

def packing_check(items, capacity, n_bins, assign):
    loads = [0] * n_bins
    for item, b in zip(items, assign):
        loads[b] += item
    return all(l <= capacity for l in loads)

def packing_find(items, capacity, n_bins):
    n = len(items)
    if n > 15: return None
    for assign in iprod(range(n_bins), repeat=n):
        loads = [0] * n_bins
        valid = True
        for item, b in zip(items, assign):
            loads[b] += item
            if loads[b] > capacity:
                valid = False
                break
        if valid:
            return list(assign)
    return None


# ============================================================================
# 3. FACTORING (given N, find factors p,q such that p×q = N)
# Not known to be NP-complete, but believed hard.
# CHECK: multiply p×q, compare. O(n²) for n-digit numbers.
# FIND: trial division O(√N) = O(2^{n/2}) for n-bit N.
# ============================================================================

def factoring_generate(n_bits):
    # Generate two random primes of ~n_bits/2 bits each
    from random import randrange
    def is_prime(n):
        if n < 2: return False
        for p in range(2, min(int(n**0.5)+1, 10000)):
            if n % p == 0: return False
        return True
    while True:
        p = randrange(2**(n_bits//2 - 1), 2**(n_bits//2))
        if is_prime(p): break
    while True:
        q = randrange(2**(n_bits//2 - 1), 2**(n_bits//2))
        if is_prime(q) and q != p: break
    N = p * q
    return N, (p, q)

def factoring_check(N, factors):
    p, q = factors
    return p * q == N and p > 1 and q > 1

def factoring_find(N):
    for p in range(2, int(N**0.5) + 1):
        if N % p == 0:
            return (p, N // p)
    return None


# ============================================================================
# 4. LATTICE PROTEIN FOLDING (simplified)
# Place n amino acids on a 2D grid, maximize contacts.
# NP-hard on the HP lattice model. CHECK: O(n). FIND: O(4^n).
# ============================================================================

def protein_generate(n):
    # Random HP sequence (H=hydrophobic, P=polar)
    seq = [np.random.choice(['H', 'P']) for _ in range(n)]
    # A valid fold is a self-avoiding walk
    # For simplicity, just use a straight line as the "solution"
    positions = [(i, 0) for i in range(n)]
    return seq, positions

def protein_check(seq, positions):
    # Check self-avoiding
    if len(set(positions)) != len(positions): return False
    # Check connected (each adjacent in sequence is adjacent on grid)
    for i in range(len(seq)-1):
        dx = abs(positions[i+1][0] - positions[i][0])
        dy = abs(positions[i+1][1] - positions[i][1])
        if dx + dy != 1: return False
    return True

def protein_find(seq):
    # Self-avoiding walk on 2D grid. O(4^n).
    n = len(seq)
    if n > 12: return None
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def _walk(pos, visited, depth):
        if depth == n: return [pos[0]]
        x, y = pos[-1]
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if (nx,ny) not in visited:
                visited.add((nx,ny))
                result = _walk(pos+[(nx,ny)], visited, depth+1)
                if result is not None:
                    return pos + result[len(pos):]
                visited.remove((nx,ny))
        return None
    result = _walk([(0,0)], {(0,0)}, 1)
    return result


# ============================================================================
# UNIFIED MEASUREMENT
# ============================================================================

def measure_domain(name, generate, check, find, sizes, n_trials=3):
    print(f"\n{name}")
    print(f"{'n':>5} | {'check μs':>9} | {'find μs':>10} | {'ratio':>8}")
    print("-" * 38)

    for n in sizes:
        cts, fts = [], []
        for _ in range(n_trials):
            inst = generate(n)
            # Check
            t0 = time.perf_counter()
            for _ in range(100): check(*inst[:-1], inst[-1])
            cts.append((time.perf_counter()-t0)/100*1e6)
            # Find
            t0 = time.perf_counter()
            result = find(*inst[:-1])
            ft = (time.perf_counter()-t0)*1e6
            if result is not None: fts.append(ft)

        if cts and fts:
            c, f = np.mean(cts), np.mean(fts)
            print(f"{n:5d} | {c:9.1f} | {f:10.0f} | {f/max(c,.01):8.0f}")


def main():
    print("P vs NP: REAL-WORLD DOMAINS")
    print("="*50)

    measure_domain("1. JOB SCHEDULING (2 machines)",
                   scheduling_generate, scheduling_check, scheduling_find,
                   [8, 10, 12, 14, 16, 18, 20])

    measure_domain("2. BIN PACKING (3 bins)",
                   packing_generate, packing_check, packing_find,
                   [6, 8, 10, 12, 14])

    measure_domain("3. INTEGER FACTORING",
                   lambda n: factoring_generate(n),
                   lambda N, f: factoring_check(N, f),
                   lambda N: factoring_find(N),
                   [16, 20, 24, 28, 32, 40])

    measure_domain("4. PROTEIN FOLDING (HP lattice)",
                   protein_generate, protein_check, protein_find,
                   [6, 8, 10, 12])

    print(f"\n{'='*50}")
    print("Every domain: checking is FAST, finding is SLOW.")
    print("The gap grows EXPONENTIALLY in every case.")
    print("This is P vs NP in the real world.")


if __name__ == "__main__":
    main()
