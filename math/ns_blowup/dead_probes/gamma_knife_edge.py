"""Γ trajectories at the knife edge: ν=2.5e-4 and ν=3e-4"""
import sys, torch, json, numpy as np
sys.path.insert(0, 'ns_blowup')
from sweep import SweepSolver

dev = 'cuda' if torch.cuda.is_available() else 'cpu'

results = []
for nu, tag, max_steps in [(2.5e-4, 'nu2.5e-4', 25000), (3e-4, 'nu3e-4', 25000)]:
    print(f'=== Γ trajectory: {tag} (ν={nu}) ===')
    solver = SweepSolver(Nr=64, Nz=128, L=1/6, nu=nu, device=dev,
                          ic_type='luo_hou', amplitude=100.0)
    u1, omega1 = solver.init_ic()
    
    t, dt, step = 0.0, 1e-7, 0
    gammas = []
    
    for step in range(max_steps):
        if step % 50 == 0:
            psi1 = solver.solve_poisson(omega1)
            du1_dz = solver._ddz(u1)
            stretching = 2.0 * u1 * du1_dz
            S = (omega1 * stretching).sum().item()
            
            domega1_dr = solver.D_r @ omega1
            domega1_dz = solver._ddz(omega1)
            P = (domega1_dr**2 + domega1_dz**2).sum().item()
            
            nuP = nu * P
            denom = abs(S) + abs(nuP) + 1e-30
            gamma_val = (S - nuP) / denom
            om1 = omega1.abs().max().item()
            gammas.append({'t': t, 'gamma': gamma_val, 'S': S, 'nuP': nuP, 'om1': om1})
            
            if step % 2000 == 0:
                print(f'  step={step} t={t:.6f} G={gamma_val:+.4f} S={S:.2e} nP={nuP:.2e} |w|={om1:.2e}')
        
        if omega1.abs().max().item() > 1e8:
            print(f'  BLOWUP at step={step}, t={t:.8f}')
            break
        
        u1, omega1, _, _ = solver.step_rk4(u1, omega1, dt)
        t += dt
        u_r_dummy = torch.zeros_like(u1)
        dt = solver.compute_dt(u_r_dummy, u_r_dummy, omega1, dt)
    
    g_arr = np.array([g['gamma'] for g in gammas])
    zero_crossings = np.sum(np.diff(np.sign(g_arr)) != 0)
    print(f'  Samples: {len(gammas)}, Zero crossings: {zero_crossings}')
    print(f'  G range: [{g_arr.min():.4f}, {g_arr.max():.4f}]')
    print(f'  G>0: {(g_arr>0).sum()}/{len(g_arr)}')
    print()
    results.append({'tag': tag, 'nu': nu, 'data': gammas})

with open('ns_blowup/results/gamma_knife_edge.json', 'w') as f:
    json.dump(results, f)
print('SAVED to gamma_knife_edge.json')
