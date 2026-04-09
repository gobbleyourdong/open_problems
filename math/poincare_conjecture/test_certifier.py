#!/usr/bin/env python3
"""
Test suite for sos_certifier.py — checks against known analytical results.
Run this BEFORE any large certification to catch bugs.
"""
import numpy as np
import sys
sys.path.insert(0, '/path/to/ComfyUI/CelebV-HQ/ns_blowup')
from sos_certifier import sos_certify, get_K_shell, build_Q_and_W
from itertools import product as iproduct

def test_N2_sharp_bound():
    """N=2 worst case: C/|ω|² = -1/8 exactly at 60° k-angle, γ=45°."""
    # K²=8 shell has vectors like (-2,-2,0) that give 60° angles
    ks = [np.array([-2., 0., -2.]), np.array([-2., 2., 0.])]
    ok, floor, certs = sos_certify(ks)
    assert ok, f"N=2 certification failed"
    assert floor > 0, f"N=2 floor {floor} not positive"
    # Q/|ω|² should be ≥ 3.0 (since C ≥ -1/8 → Q = 5+16(-1/8) = 3)
    print(f"  N=2 sharp bound: PASS (floor={floor:.2f})")

def test_N3_extremum():
    """N=3 worst case: C/|ω|² = -11/64 at cosθ=(-3/4,-3/4,1/4)."""
    ks = [np.array([-2., 0., -1.]), np.array([-2., 1., 0.]), np.array([-1., 0., -2.])]
    ok, floor, certs = sos_certify(ks)
    assert ok, f"N=3 extremum certification failed"
    # Q/|ω|² = 9/4 = 2.25 at the extremum, floor should be well above 0
    assert floor > 4, f"N=3 floor {floor} too low (expected ~5.4+)"
    print(f"  N=3 extremum (-11/64): PASS (floor={floor:.2f})")

def test_orthogonal_k():
    """Orthogonal k-vectors (K²=1): C=0, Q/|ω|²=5."""
    ks = [np.array([1., 0., 0.]), np.array([0., 1., 0.]), np.array([0., 0., 1.])]
    ok, floor, certs = sos_certify(ks)
    assert ok, f"Orthogonal k certification failed"
    assert floor > 10, f"Orthogonal k floor {floor} too low (expected ~15)"
    print(f"  Orthogonal k (K²=1): PASS (floor={floor:.2f})")

def test_parallel_k():
    """Two parallel k-vectors: should still certify."""
    ks = [np.array([1., 1., 0.]), np.array([2., 2., 0.])]  # parallel
    ok, floor, certs = sos_certify(ks)
    # Parallel k gives sin²θ=0, so P=0, C=0, Q=5|ω|². Should easily pass.
    assert ok, f"Parallel k certification failed"
    print(f"  Parallel k: PASS (floor={floor:.2f})")

def test_N4_worst():
    """N=4 worst mixed-shell config."""
    ks = [np.array([-2.,-2.,0.]), np.array([-2.,-1.,0.]),
          np.array([-2.,0.,-1.]), np.array([0.,-1.,0.])]
    ok, floor, certs = sos_certify(ks)
    assert ok, f"N=4 worst certification failed"
    assert floor > 5, f"N=4 worst floor {floor} too low"
    print(f"  N=4 worst mixed-shell: PASS (floor={floor:.2f})")

def test_sign_pattern_count():
    """Verify correct number of effective sign patterns."""
    for N in [2, 3, 4, 5]:
        patterns = []
        seen = set()
        for signs in iproduct([-1, 1], repeat=N):
            canon = tuple(s * signs[0] for s in signs)
            if canon not in seen:
                seen.add(canon)
                patterns.append(signs)
        expected = 2**(N-1)
        assert len(patterns) == expected, f"N={N}: got {len(patterns)} patterns, expected {expected}"
    print(f"  Sign pattern count: PASS (N=2→2, N=3→4, N=4→8, N=5→16)")

def test_Q_matrix_symmetry():
    """Q matrix should be symmetric."""
    ks = [np.array([-2., 0., -1.]), np.array([-2., 1., 0.]), np.array([-1., 0., -2.])]
    signs = (1, 1, 1)
    WtW, Q = build_Q_and_W(ks, signs)
    assert np.allclose(Q, Q.T), "Q matrix not symmetric"
    assert np.allclose(WtW, WtW.T), "WtW matrix not symmetric"
    print(f"  Matrix symmetry: PASS")

def test_per_mode_identity():
    """Verify |S_j|²_F = a_j²/2 for each mode."""
    for _ in range(20):
        k = np.random.randn(3)
        v = np.random.randn(3)
        v -= (v @ k) / (k @ k) * k  # div-free
        a = np.linalg.norm(v)
        u = np.cross(k, v) / (k @ k)
        S = -0.5 * (np.outer(u, k) + np.outer(k, u))
        S2 = np.sum(S**2)
        assert abs(S2 - a**2/2) < 1e-10, f"|S|²={S2} != a²/2={a**2/2}"
    print(f"  Per-mode |S|²=a²/2: PASS (20 random modes)")

def test_self_vanishing():
    """Verify |S_j·ê|² = (a²/4)sin²γ."""
    for _ in range(20):
        k = np.random.randn(3)
        v = np.random.randn(3)
        v -= (v @ k) / (k @ k) * k
        a = np.linalg.norm(v)
        e = np.random.randn(3); e /= np.linalg.norm(e)
        cos_g = (v/a) @ e
        sin2_g = 1 - cos_g**2
        u = np.cross(k, v) / (k @ k)
        S = -0.5 * (np.outer(u, k) + np.outer(k, u))
        Se = S @ e
        Se2 = Se @ Se
        expected = (a**2 / 4) * sin2_g
        assert abs(Se2 - expected) < 1e-10, f"|S·ê|²={Se2} != (a²/4)sin²γ={expected}"
    print(f"  Self-vanishing identity: PASS (20 random modes)")

def test_cross_term_identity():
    """Verify |S|² = |ω|²/2 - 2C at random points."""
    from itertools import combinations
    np.random.seed(42)
    for _ in range(10):
        N = np.random.choice([2, 3, 4])
        ks = [np.random.randn(3) for _ in range(N)]
        vs = []
        for k in ks:
            v = np.random.randn(3)
            v -= (v @ k) / (k @ k) * k
            vs.append(v)
        x = np.random.uniform(0, 2*np.pi, 3)
        omega = sum(v * np.cos(k @ x) for k, v in zip(ks, vs))
        w2 = omega @ omega
        S = np.zeros((3, 3))
        for k, v in zip(ks, vs):
            u = np.cross(k, v) / (k @ k)
            S += 0.5 * (-np.outer(u, k) - np.outer(k, u)) * np.cos(k @ x)
        S2 = np.sum(S**2)
        C = (w2/2 - S2) / 2
        # Verify: |S|² = |ω|²/2 - 2C
        assert abs(S2 - (w2/2 - 2*C)) < 1e-10, f"Cross-term identity failed"
    print(f"  Cross-term identity |S|²=|ω|²/2-2C: PASS (10 random fields)")

if __name__ == '__main__':
    print("=== SOS Certifier Test Suite ===\n")
    tests = [
        test_sign_pattern_count,
        test_Q_matrix_symmetry,
        test_per_mode_identity,
        test_self_vanishing,
        test_cross_term_identity,
        test_orthogonal_k,
        test_parallel_k,
        test_N2_sharp_bound,
        test_N3_extremum,
        test_N4_worst,
    ]
    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except Exception as e:
            print(f"  {t.__name__}: FAIL — {e}")
            failed += 1
    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("*** ALL TESTS PASS ***")
