#!/usr/bin/env python3
"""
Independent verifier for NS regularity SOS certificates.

Usage:
    python verify_certificates.py certs/N3_K18.json
    python verify_certificates.py certs/   # verify all JSONs in directory

For each certificate: builds the Putinar residual matrix from stored (λ,μ),
rounds to 6-digit rationals, checks all eigenvalues ≥ -1e-6 and floor > 0.
No dependencies beyond numpy and standard library.
"""
import numpy as np
import json
import sys
import os
import time
from fractions import Fraction
from itertools import product as iproduct

def make_basis(k):
    k = np.asarray(k, dtype=float)
    kh = k / np.linalg.norm(k)
    if abs(kh[0]) < 0.9:
        e1 = np.cross(kh, [1, 0, 0])
    else:
        e1 = np.cross(kh, [0, 1, 0])
    e1 /= np.linalg.norm(e1)
    return e1, np.cross(kh, e1)

def build_Q_and_W(ks, signs):
    N = len(ks)
    bases = [make_basis(k) for k in ks]
    W = np.zeros((3, 2*N))
    for j in range(N):
        e1, e2 = bases[j]
        W[:, 2*j] = signs[j] * e1
        W[:, 2*j+1] = signs[j] * e2
    WtW = W.T @ W
    M_S = np.zeros((2*N, 2*N))
    for a in range(3):
        for b in range(3):
            L = np.zeros(2*N)
            for j in range(N):
                e1, e2 = bases[j]
                K2j = np.dot(ks[j], ks[j])
                ke1 = np.cross(ks[j], e1) / K2j
                ke2 = np.cross(ks[j], e2) / K2j
                L[2*j] += signs[j] * (-0.5) * (ke1[a]*ks[j][b] + ks[j][a]*ke1[b])
                L[2*j+1] += signs[j] * (-0.5) * (ke2[a]*ks[j][b] + ks[j][a]*ke2[b])
            M_S += np.outer(L, L)
    return WtW, 9 * WtW - 8 * M_S

def verify_one(entry):
    """Verify a single certificate entry. Returns (pass, min_eig, floor)."""
    ks = [np.array(k) for k in entry['k_vectors']]
    N = len(ks)

    patterns = []
    seen = set()
    for signs in iproduct([-1, 1], repeat=N):
        canon = tuple(s * signs[0] for s in signs)
        if canon not in seen:
            seen.add(canon)
            patterns.append(signs)

    all_WtW = {}; all_Q = {}
    for s in patterns:
        WtW, Q = build_Q_and_W(ks, s)
        all_WtW[s] = WtW; all_Q[s] = Q

    D_blocks = []
    for j in range(N):
        D = np.zeros((2*N, 2*N))
        D[2*j, 2*j] = 1; D[2*j+1, 2*j+1] = 1
        D_blocks.append(D)

    worst_eig = float('inf')
    worst_floor = float('inf')

    for cert in entry['certs']:
        if cert.get('status', '') not in ['optimal', 'optimal_inaccurate']:
            return False, -999, -999

        s = tuple(cert['signs'])
        lam = np.array(cert['lambda'])
        mu = np.array(cert['mu'])

        other = [t for t in patterns if t != s]
        region = [all_WtW[s] - all_WtW[t] for t in other]

        # Round to 6-digit rationals
        lam_r = [float(Fraction(float(l)).limit_denominator(10**6)) for l in lam]
        mu_r = [float(Fraction(float(m)).limit_denominator(10**6)) for m in mu]

        # Build residual
        residual = all_Q[s].copy()
        for j in range(N):
            residual -= lam_r[j] * D_blocks[j]
        for i in range(len(other)):
            residual -= mu_r[i] * region[i]

        eigs = np.linalg.eigvalsh(residual)
        floor = sum(lam_r)

        worst_eig = min(worst_eig, eigs[0])
        worst_floor = min(worst_floor, floor)

    return worst_eig >= -1e-6 and worst_floor > 0, worst_eig, worst_floor

def verify_file(path):
    """Verify all certificates in a JSON file."""
    with open(path) as f:
        data = json.load(f)

    n_total = len(data['certificates'])
    n_pass = 0
    n_fail = 0
    worst_eig = float('inf')
    worst_floor = float('inf')

    t0 = time.time()
    for i, entry in enumerate(data['certificates']):
        ok, eig, floor = verify_one(entry)
        if ok:
            n_pass += 1
            worst_eig = min(worst_eig, eig)
            worst_floor = min(worst_floor, floor)
        else:
            n_fail += 1
            if n_fail <= 5:
                print(f'  FAIL config {i}: eig={eig:.2e} floor={floor:.4f}')

        if (i + 1) % max(1, n_total // 10) == 0:
            elapsed = time.time() - t0
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            print(f'  [{i+1}/{n_total}] pass={n_pass} fail={n_fail} '
                  f'rate={rate:.0f}/s')

    elapsed = time.time() - t0
    print(f'\n  File: {path}')
    print(f'  N={data["N"]}, K²≤{data["K2max"]}')
    print(f'  Configs: {n_total}')
    print(f'  Passed: {n_pass}/{n_total}')
    print(f'  Failed: {n_fail}')
    print(f'  Worst eigenvalue: {worst_eig:.2e}')
    print(f'  Worst floor: {worst_floor:.4f}')
    print(f'  Time: {elapsed:.1f}s')
    return n_fail == 0

def main():
    if len(sys.argv) < 2:
        print('Usage: python verify_certificates.py <file.json or directory>')
        sys.exit(1)

    target = sys.argv[1]
    if os.path.isdir(target):
        files = sorted(f for f in os.listdir(target) if f.endswith('.json'))
        all_ok = True
        for f in files:
            print(f'\n=== Verifying {f} ===')
            ok = verify_file(os.path.join(target, f))
            if not ok:
                all_ok = False
        if all_ok:
            print(f'\n*** ALL FILES VERIFIED ***')
        else:
            print(f'\n*** SOME FILES FAILED ***')
    else:
        ok = verify_file(target)
        if ok:
            print(f'\n*** VERIFIED ***')
        else:
            print(f'\n*** FAILED ***')

if __name__ == '__main__':
    main()
