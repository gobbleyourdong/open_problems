"""
SOS Certifier for the Navier-Stokes Key Lemma
Proves Q = 9|ω|² - 8|S|² > 0 at the vertex max for given k-configurations.

Usage:
    python sos_certifier.py --N 3 --K2max 9                    # certify, print results
    python sos_certifier.py --N 4 --K2max 9 --save-certs       # certify + save certificates
    python sos_certifier.py --N 4 --K2max 9 --sample 1000      # sample instead of exhaustive
    python sos_certifier.py --verify certs/N3_K18.json          # verify saved certificates
"""
import numpy as np
import cvxpy as cp
from itertools import combinations, product as iproduct
import argparse
import time
import json
import os
import sys

def get_K_shell(K2):
    R = int(np.sqrt(K2)) + 1
    vecs = []
    for kx in range(-R, R+1):
        for ky in range(-R, R+1):
            for kz in range(-R, R+1):
                if kx*kx + ky*ky + kz*kz == K2:
                    vecs.append(np.array([kx, ky, kz], dtype=float))
    half = []; seen = set()
    for v in vecs:
        t = tuple(v.astype(int)); neg = tuple(-x for x in t)
        if t not in seen and neg not in seen:
            half.append(v); seen.add(t)
    return half

def make_basis(k):
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
                K2j = ks[j] @ ks[j]
                ke1 = np.cross(ks[j], e1) / K2j
                ke2 = np.cross(ks[j], e2) / K2j
                L[2*j] += signs[j] * (-0.5) * (ke1[a]*ks[j][b] + ks[j][a]*ke1[b])
                L[2*j+1] += signs[j] * (-0.5) * (ke2[a]*ks[j][b] + ks[j][a]*ke2[b])
            M_S += np.outer(L, L)
    return WtW, 9 * WtW - 8 * M_S

def sos_certify(ks):
    """Run SOS certification for a k-config.
    Returns (certified: bool, min_floor: float, certificates: list)."""
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
        all_WtW[s] = WtW
        all_Q[s] = Q

    D_blocks = []
    for j in range(N):
        D = np.zeros((2*N, 2*N))
        D[2*j, 2*j] = 1
        D[2*j+1, 2*j+1] = 1
        D_blocks.append(D)

    min_floor = float('inf')
    all_ok = True
    certificates = []

    for s in patterns:
        Q_s = all_Q[s]
        other = [t for t in patterns if t != s]
        region_mats = [all_WtW[s] - all_WtW[t] for t in other]

        lam = cp.Variable(N)
        mu = cp.Variable(len(other), nonneg=True)

        mat = Q_s
        for j in range(N):
            mat = mat - lam[j] * D_blocks[j]
        for i in range(len(other)):
            mat = mat - mu[i] * region_mats[i]

        try:
            prob = cp.Problem(cp.Maximize(cp.sum(lam)), [mat >> 0])
            prob.solve(solver='SCS', verbose=False, max_iters=20000, eps=1e-7)

            if prob.status in ['optimal', 'optimal_inaccurate']:
                floor = sum(lam.value)
                if floor <= 0:
                    all_ok = False
                min_floor = min(min_floor, floor)
                certificates.append({
                    'signs': list(s),
                    'lambda': lam.value.tolist(),
                    'mu': mu.value.tolist(),
                    'floor': float(floor),
                    'status': prob.status
                })
            else:
                all_ok = False
                certificates.append({'signs': list(s), 'status': prob.status})
        except Exception as e:
            all_ok = False
            certificates.append({'signs': list(s), 'status': f'error: {e}'})

    return all_ok, min_floor, certificates

def verify_certificate(ks, cert):
    """Verify a saved certificate by checking the residual matrix is PSD."""
    N = len(ks)
    s = tuple(cert['signs'])
    lam = np.array(cert['lambda'])
    mu = np.array(cert['mu'])

    _, Q_s = build_Q_and_W(ks, s)

    # Build D blocks
    D_blocks = []
    for j in range(N):
        D = np.zeros((2*N, 2*N))
        D[2*j, 2*j] = 1; D[2*j+1, 2*j+1] = 1
        D_blocks.append(D)

    # Build region matrices
    patterns = []
    seen = set()
    for signs in iproduct([-1, 1], repeat=N):
        canon = tuple(si * signs[0] for si in signs)
        if canon not in seen:
            seen.add(canon); patterns.append(signs)
    other = [t for t in patterns if t != s]
    all_WtW = {}
    for t in [s] + other:
        WtW, _ = build_Q_and_W(ks, t)
        all_WtW[t] = WtW
    region_mats = [all_WtW[s] - all_WtW[t] for t in other]

    # Build residual: Q - ΣλD - Σμ(region)
    residual = Q_s.copy()
    for j in range(N):
        residual -= lam[j] * D_blocks[j]
    for i in range(len(other)):
        residual -= mu[i] * region_mats[i]

    eigs = np.linalg.eigvalsh(residual)
    min_eig = eigs[0]
    floor = sum(lam)
    return min_eig > -1e-6 and floor > 0, min_eig, floor

def main():
    parser = argparse.ArgumentParser(description='SOS Certifier for NS Key Lemma')
    parser.add_argument('--N', type=int, default=3, help='Number of modes')
    parser.add_argument('--K2max', type=int, default=9, help='Max K² shell')
    parser.add_argument('--sample', type=int, default=0, help='Sample size (0=exhaustive)')
    parser.add_argument('--ks', type=str, default='', help='Specific k-vectors')
    parser.add_argument('--save-certs', action='store_true', help='Save certificates to JSON')
    parser.add_argument('--verify', type=str, default='', help='Verify a saved certificate file')
    parser.add_argument('--resume', action='store_true', help='Resume from checkpoint if available')
    args = parser.parse_args()

    # Verification mode
    if args.verify:
        print(f'Verifying {args.verify}...')
        with open(args.verify) as f:
            data = json.load(f)
        n_ok = 0; n_fail = 0
        for entry in data['certificates']:
            ks = [np.array(k) for k in entry['k_vectors']]
            for cert in entry['certs']:
                ok, min_eig, floor = verify_certificate(ks, cert)
                if ok: n_ok += 1
                else: n_fail += 1
        print(f'Verified: {n_ok} pass, {n_fail} fail')
        return

    # Single config mode
    if args.ks:
        ks = [np.array([float(x) for x in k.split(',')]) for k in args.ks.split()]
        print(f'Testing: {[tuple(k.astype(int)) for k in ks]}')
        ok, floor, certs = sos_certify(ks)
        print(f'Result: {"✓ CERTIFIED" if ok else "✗ FAILED"}, floor = {floor:.4f}')
        return

    # Collect k-vectors
    all_k = []
    for K2 in range(1, args.K2max + 1):
        all_k.extend(get_K_shell(K2))
    print(f'K²=1..{args.K2max}: {len(all_k)} k-vectors')

    N = args.N
    if args.sample > 0:
        np.random.seed(42)
        n_test = args.sample
        configs = [tuple(np.random.choice(len(all_k), N, replace=False)) for _ in range(n_test)]
    else:
        configs = list(combinations(range(len(all_k)), N))
        n_test = len(configs)
    print(f'Testing {n_test} N={N} configs...')

    # Certificate storage
    cert_output = [] if args.save_certs else None
    cert_dir = 'ns_blowup/certs'
    if args.save_certs:
        os.makedirs(cert_dir, exist_ok=True)

    # Resume from checkpoint if available
    start_idx = 0
    checkpoint_file = f'{cert_dir}/N{N}_K{args.K2max}.checkpoint.json' if args.save_certs else None
    if args.resume and checkpoint_file and os.path.exists(checkpoint_file):
        with open(checkpoint_file) as f:
            ckpt = json.load(f)
        start_idx = ckpt['next_idx']
        n_cert = ckpt['n_certified']
        n_fail = ckpt['n_failures']
        worst_floor = ckpt['min_floor']
        cert_output = ckpt['certificates']
        print(f'Resuming from checkpoint: {start_idx}/{n_test} '
              f'(cert={n_cert} fail={n_fail} floor≥{worst_floor:.2f})')
    else:
        n_cert = 0; n_fail = 0; worst_floor = float('inf')

    t0 = time.time()
    checkpoint_interval = max(1, n_test // 10)

    for i in range(start_idx, n_test):
        config = configs[i]
        ks = [all_k[j] for j in config]
        ok, floor, certs = sos_certify(ks)
        if ok:
            n_cert += 1
            worst_floor = min(worst_floor, floor)
            if cert_output is not None:
                cert_output.append({
                    'config_id': i,
                    'k_vectors': [k.tolist() for k in ks],
                    'certified': True,
                    'floor': float(floor),
                    'certs': certs
                })
        else:
            n_fail += 1
            shells = sorted([int(k @ k) for k in ks])
            print(f'  FAIL config {i}: K²={shells}')
            if cert_output is not None:
                cert_output.append({
                    'config_id': i,
                    'k_vectors': [k.tolist() for k in ks],
                    'certified': False,
                    'certs': certs
                })

        if (i + 1) % checkpoint_interval == 0:
            elapsed = time.time() - t0
            done_this_run = i + 1 - start_idx
            rate = done_this_run / elapsed if elapsed > 0 else 0
            eta = (n_test - i - 1) / rate if rate > 0 else 0
            print(f'  [{i+1}/{n_test}] cert={n_cert} fail={n_fail} '
                  f'floor≥{worst_floor:.2f} rate={rate:.1f}/s ETA={eta/60:.0f}min')
            # Save checkpoint
            if checkpoint_file and cert_output is not None:
                with open(checkpoint_file, 'w') as f:
                    json.dump({
                        'next_idx': i + 1,
                        'n_certified': n_cert,
                        'n_failures': n_fail,
                        'min_floor': float(worst_floor),
                        'certificates': cert_output
                    }, f)
                sys.stdout.flush()

    elapsed = time.time() - t0
    print(f'\n=== SOS CERTIFICATION COMPLETE ===')
    print(f'N={N}, K²≤{args.K2max}')
    print(f'Tested: {n_test}')
    print(f'Certified: {n_cert}/{n_test} ({100*n_cert/n_test:.1f}%)')
    print(f'Failures: {n_fail}')
    print(f'Min floor: {worst_floor:.4f}')
    print(f'Time: {elapsed:.0f}s ({elapsed/60:.1f}min)')
    if n_fail == 0:
        print(f'*** ALL CERTIFIED ***')

    # Save certificates
    if cert_output is not None:
        outfile = f'{cert_dir}/N{N}_K{args.K2max}.json'
        with open(outfile, 'w') as f:
            json.dump({
                'N': N,
                'K2max': args.K2max,
                'n_configs': n_test,
                'n_certified': n_cert,
                'n_failures': n_fail,
                'min_floor': float(worst_floor),
                'time_seconds': elapsed,
                'certificates': cert_output
            }, f)
        fsize = os.path.getsize(outfile) / (1024*1024)
        print(f'Certificates saved to {outfile} ({fsize:.1f} MB)')
        # Remove checkpoint after successful completion
        if checkpoint_file and os.path.exists(checkpoint_file):
            os.remove(checkpoint_file)
            print(f'Checkpoint removed: {checkpoint_file}')

if __name__ == '__main__':
    main()
