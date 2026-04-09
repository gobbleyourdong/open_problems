"""
Can we close the BKM log gap using the self-depletion?

Standard BKM: blowup iff ∫||ω||∞ dt = ∞
Standard bound: d||ω||∞/dt ≤ C||ω||∞² (quadratic → blowup possible)

Our extra structure: at max-|ω| point, dα/dt ≤ -α² + R
with R = O(|ω|²) but the COEFFICIENT is small (C ≈ 0.03).

This gives: α ≤ √R ≈ 0.17||ω|| (bounded at the max point)
Then: d||ω||∞/dt = α·||ω||∞ ≤ 0.17||ω||∞² (SAME quadratic but with coefficient 0.17)

The standard BKM coefficient is C = 1 (or some O(1) constant).
Ours is 0.17. But BOTH give quadratic → possible blowup.

KEY QUESTION: can the Riccati structure give BETTER than quadratic?

The Riccati: dα/dt = -α² + C|ω|²
At equilibrium: α = √C·|ω|
But |ω| itself evolves: d|ω|/dt = α|ω| = √C·|ω|²

So: d|ω|/dt = √C·|ω|² → |ω| = |ω|₀/(1-√C·|ω|₀·t) → blowup at T*=1/(√C·|ω|₀)

With C=0.03: T* = 1/(0.17×17) ≈ 0.34.
But actual evolution to t=0.8: |ω| only reaches 38 (no blowup).
Predicted at t=0.8 from the formula: |ω|₀/(1-0.17×17×0.8) = 17/(1-2.3) = -13 (already past T*!)

This means the Riccati equilibrium α = √C·|ω| is NOT maintained.
α is BELOW the equilibrium because the Riccati takes time to relax.

The TRANSIENT Riccati dynamics might save us:
- Initially α = 0 (from IC)
- α grows toward √C·|ω|
- But |ω| also changes during this growth
- The coupled system might have sub-quadratic growth

Let me solve the COUPLED ODE system:
  dα/dt = -α² + C|ω|²
  d|ω|/dt = α·|ω|

and check if |ω| blows up or stays bounded.
"""
import numpy as np
from scipy.integrate import solve_ivp
import sys

def coupled_riccati(t, y, C):
    """dα/dt = -α² + C|ω|², d|ω|/dt = α|ω|"""
    alpha, omega = y
    dalpha = -alpha**2 + C*omega**2
    domega = alpha*omega
    return [dalpha, domega]

def test_coupled_system():
    print("="*70,flush=True)
    print("COUPLED RICCATI-VORTICITY ODE: does |ω| blow up?",flush=True)
    print("="*70,flush=True)
    print("  dα/dt = -α² + C|ω|²",flush=True)
    print("  d|ω|/dt = α·|ω|",flush=True)
    print("  C = effective pressure coefficient\n",flush=True)

    omega0 = 17.0  # trefoil initial

    for C in [0.01, 0.03, 0.05, 0.10, 0.20, 0.25, 0.30]:
        alpha0 = 0.0  # start from zero

        # Solve
        def event_blowup(t, y, C):
            return y[1] - 1e6  # detect blowup
        event_blowup.terminal = True
        event_blowup.direction = 1

        try:
            sol = solve_ivp(coupled_riccati, [0, 5.0], [alpha0, omega0],
                           args=(C,), max_step=0.001, method='RK45',
                           events=lambda t,y: event_blowup(t,y,C),
                           dense_output=True)

            t_final = sol.t[-1]
            omega_final = sol.y[1,-1]
            alpha_final = sol.y[0,-1]

            if omega_final > 1e5:
                # Find blowup time
                T_star = t_final
                print(f"  C={C:.2f}: BLOWUP at T*≈{T_star:.4f}  "
                      f"|ω|₀·T*={omega0*T_star:.3f}  "
                      f"α_eq=√C·|ω|₀={np.sqrt(C)*omega0:.3f}",flush=True)
            else:
                print(f"  C={C:.2f}: |ω|(5.0)={omega_final:.2f}  "
                      f"α(5.0)={alpha_final:.4f}  NO BLOWUP by t=5",flush=True)

            # Print trajectory
            ts = np.linspace(0, min(t_final, 2.0), 20)
            ys = sol.sol(ts)
            print(f"    {'t':>6s}  {'α':>8s}  {'|ω|':>10s}  {'d|ω|/dt':>10s}  {'α/√C|ω|':>8s}",flush=True)
            for i in range(0, len(ts), max(1,len(ts)//8)):
                a = ys[0,i]; om = ys[1,i]
                dom = a*om
                eq_ratio = a/(np.sqrt(C)*om+1e-30)
                print(f"    {ts[i]:6.3f}  {a:+8.4f}  {om:10.2f}  {dom:+10.2f}  {eq_ratio:8.3f}",flush=True)
            print(flush=True)

        except Exception as e:
            print(f"  C={C:.2f}: solver error: {e}",flush=True)

    # KEY: what value of C separates blowup from regularity?
    print(f"\n{'='*70}",flush=True)
    print("CRITICAL C: binary search for blowup threshold",flush=True)
    print(f"{'='*70}",flush=True)

    C_lo, C_hi = 0.0, 1.0
    for _ in range(30):
        C_mid = (C_lo + C_hi) / 2
        try:
            sol = solve_ivp(coupled_riccati, [0, 10.0], [0.0, omega0],
                           args=(C_mid,), max_step=0.001, method='RK45')
            if sol.y[1,-1] > 1e6:
                C_hi = C_mid  # blowup
            else:
                C_lo = C_mid  # no blowup
        except:
            C_hi = C_mid

    C_crit = (C_lo + C_hi) / 2
    print(f"\n  Critical C = {C_crit:.6f}",flush=True)
    print(f"  Below C_crit: bounded |ω| (regularity)",flush=True)
    print(f"  Above C_crit: blowup",flush=True)
    print(f"  Our measured C ≈ 0.03",flush=True)
    print(f"  Margin: C_crit / C_measured = {C_crit/0.03:.1f}×",flush=True)

    # Also: does the coupled system ALWAYS blow up for C > 0?
    print(f"\n  Theoretical prediction:",flush=True)
    print(f"  At Riccati equilibrium: α = √C·|ω|",flush=True)
    print(f"  Then d|ω|/dt = √C·|ω|² → blowup for ANY C > 0",flush=True)
    print(f"  But: the equilibrium is only reached ASYMPTOTICALLY",flush=True)
    print(f"  The TRANSIENT dynamics matter\n",flush=True)

    # Check: does starting at α=0 vs α=equilibrium matter?
    print("  Starting from α=0 (realistic) vs α=√C·|ω|₀ (equilibrium):",flush=True)
    for C in [0.03]:
        for alpha0_frac in [0.0, 0.5, 1.0]:
            a0 = alpha0_frac * np.sqrt(C) * omega0
            sol = solve_ivp(coupled_riccati, [0, 10.0], [a0, omega0],
                           args=(C,), max_step=0.001)
            if sol.y[1,-1] > 1e6:
                # Find T*
                idx = np.argmax(sol.y[1] > 1e5)
                Ts = sol.t[idx] if idx > 0 else '>10'
                print(f"    α₀={a0:.3f} ({alpha0_frac:.0%} equil): BLOWUP at T*≈{Ts}",flush=True)
            else:
                print(f"    α₀={a0:.3f} ({alpha0_frac:.0%} equil): |ω|(10)={sol.y[1,-1]:.2f}",flush=True)

    print(f"\n{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    test_coupled_system()
