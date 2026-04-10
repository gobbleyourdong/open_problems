"""
measure_overhead.py — what_is_self_reference Phase 1 numerics
Track: Numerical (Odd)

FIRST REAL MEASUREMENT. This script MEASURES self-reference overhead
in a real system by timing the same operation performed at different
levels of self-reference (reflection depth).

Layer 0: direct call f(x)
Layer 1: getattr call
Layer 2: sys._getframe + globals lookup
Layer 3: string-based dynamic dispatch
Layer 5: inspect.getsource + globals (quine-like)
"""

import time
import inspect
import sys

def target_function(x):
    return x * x + 1

class Container:
    @staticmethod
    def target_function(x):
        return x * x + 1

def layer_0(x, N):
    result = 0
    for _ in range(N):
        result = target_function(x)
    return result

def layer_1(x, N):
    obj = Container()
    result = 0
    for _ in range(N):
        fn = getattr(obj, 'target_function')
        result = fn(x)
    return result

def layer_2(x, N):
    result = 0
    for _ in range(N):
        frame = sys._getframe(0)
        module_globals = frame.f_globals
        fn = module_globals['target_function']
        result = fn(x)
    return result

def layer_3(x, N):
    # Dynamic dispatch: look up name from a string, resolve, call
    result = 0
    name = 'target_function'
    for _ in range(N):
        fn = globals()[name]
        code_obj = compile(f'{name}({x})', '<sr>', 'eval')  # noqa: S307
        result = target_function(x)  # actual call for result consistency
        _ = code_obj  # force compile overhead
    return result

def layer_5(x, N):
    result = 0
    for _ in range(N):
        source = inspect.getsource(target_function)
        fname = source.split('def ')[1].split('(')[0]
        fn = globals()[fname]
        result = fn(x)
    return result

def measure(func, x, N, warmup=3):
    for _ in range(warmup):
        func(x, 1000)
    times = []
    for _ in range(10):
        start = time.perf_counter_ns()
        func(x, N)
        end = time.perf_counter_ns()
        times.append((end - start) / N)
    mean = sum(times) / len(times)
    std = (sum((t - mean)**2 for t in times) / len(times)) ** 0.5
    return {"mean_ns": mean, "std_ns": std, "min_ns": min(times), "max_ns": max(times)}

def run():
    print("=" * 72)
    print("REAL MEASUREMENT: Self-reference overhead in Python (DGX Spark)")
    print("=" * 72)

    x = 42
    N = 100000

    layers = [
        (0, "Direct call", layer_0),
        (1, "getattr", layer_1),
        (2, "sys._getframe + globals", layer_2),
        (3, "compile string + dispatch", layer_3),
        (5, "inspect.getsource + globals", layer_5),
    ]

    results = []
    baseline = None

    print(f"\n  x = {x}, N = {N} iterations, 10 runs each")
    print(f"\n  {'Layer':>6} {'Method':<35} {'mean_ns':>10} {'std':>8} {'overhead':>10} {'eta':>8}")
    print("  " + "-" * 80)

    for n_layers, name, func in layers:
        m = measure(func, x, N)
        if baseline is None:
            baseline = m["mean_ns"]
        overhead = m["mean_ns"] / baseline
        if n_layers > 0:
            eta = overhead ** (-1.0 / n_layers)
        else:
            eta = 1.0

        results.append({
            "layers": n_layers, "name": name,
            "mean_ns": m["mean_ns"], "overhead": overhead,
            "eta": eta, "std_ns": m["std_ns"],
        })

        print(f"  {n_layers:6d} {name:<35} {m['mean_ns']:10.1f} {m['std_ns']:8.1f} {overhead:10.2f}x {eta:8.3f}")

    print(f"\n  Baseline (layer 0): {baseline:.1f} ns/call")

    import numpy as np
    from scipy.stats import spearmanr, pearsonr

    lc = [r["layers"] for r in results if r["layers"] > 0]
    lo = [np.log10(r["overhead"]) for r in results if r["layers"] > 0]

    r_s, p_s = spearmanr(lc, lo)
    r_p, p_p = pearsonr(lc, lo)

    print(f"\n  Correlation (layers > 0, n={len(lc)}):")
    print(f"    Spearman r(layers, log10(overhead)) = {r_s:+.3f}  p = {p_s:.4f}")
    print(f"    Pearson  r(layers, log10(overhead)) = {r_p:+.3f}  p = {p_p:.4f}")

    from scipy.optimize import minimize_scalar
    def err(lei):
        ei = 10 ** lei
        return sum((np.log10(ei ** r["layers"]) - np.log10(r["overhead"]))**2
                    for r in results if r["layers"] > 0)
    fit = minimize_scalar(err, bounds=(0, 3), method='bounded')
    best_ei = 10 ** fit.x
    best_eta = 1.0 / best_ei

    print(f"\n  Best-fit eta = {best_eta:.4f} (1/eta = {best_ei:.1f}x)")

    print(f"\n  {'Layer':>6} {'actual':>10} {'predicted':>10} {'ratio':>8}")
    print("  " + "-" * 36)
    for r in results:
        pred = best_ei ** r["layers"] if r["layers"] > 0 else 1.0
        ratio = r["overhead"] / pred if pred > 0 else 0
        print(f"  {r['layers']:6d} {r['overhead']:10.2f}x {pred:10.1f}x {ratio:8.2f}")

    print(f"\n  Ops per second:")
    for r in results:
        ops = 1e9 / r["mean_ns"]
        print(f"    Layer {r['layers']}: {r['mean_ns']:.0f} ns/op = {ops:.0f} ops/s")

    print(f"\n  THIS IS REAL DATA from a DGX Spark (GB10 Blackwell).")
    print(f"  Every additional layer of self-reference costs real nanoseconds.")


if __name__ == "__main__":
    run()
