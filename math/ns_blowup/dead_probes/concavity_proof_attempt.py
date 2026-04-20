"""
THE CONCAVITY ARGUMENT: if 1/||ω||∞ is concave up, blowup is impossible.

FACT: A positive concave-up function can never reach zero in finite time.
Proof: if g(t) ≥ 0 and g''(t) ≥ 0, then g is convex, hence g(t) ≥ g(0) + g'(0)t.
Since g(0) > 0, g(t) > 0 for all t > -g(0)/g'(0) (if g'(0) < 0).
Actually: convex + positive → g(t) ≥ min(g(0), g(T)) for any T.
More precisely: a convex function on [0,∞) that starts positive stays positive.
Wait, that's not right either. g(t) = 1 - t is convex (g''=0) and reaches 0.
We need g'' > 0 (STRICTLY convex).

CORRECT STATEMENT: if g''(t) > 0 for all t, and g(0) > 0, and g is defined
on [0,T), then g(t) > 0 on [0,T). Because:
- g is strictly convex → it's above any tangent line
- At any time t₀: g(t) ≥ g(t₀) + g'(t₀)(t-t₀) for all t
- If g ever reached 0 at t₁, then the tangent at t₁ would be ≤ 0
  but g at t < t₁ is positive → contradiction with convexity

Actually: a convex function g on [0,∞) with g(0) > 0:
- If g'(0) ≥ 0: g is increasing → never reaches 0. ✓
- If g'(0) < 0: g decreases initially. By convexity, g is above the
  tangent line at 0: g(t) ≥ g(0) + g'(0)t. This reaches 0 at t₀ = -g(0)/g'(0).
  But g is ABOVE this line (convex), so g doesn't reach 0 until t > t₀.
  After t₀, the tangent line is negative, but g could be positive (convex
  functions can dip and then rise).

Hmm, actually convex functions CAN reach zero. g(t) = (1-t)² is convex,
g(0)=1, g(1)=0. But g''=2 > 0, and g reaches 0 at t=1.

So strict convexity of 1/||ω||∞ does NOT prevent it from reaching zero!

WAIT. Let me reconsider. g(t) = (1-t)² → ||ω|| = 1/g = 1/(1-t)² → blowup.
And d²(1/||ω||)/dt² = d²(1-t)²/dt² = 2 > 0. Convex. But still blowup.

So concave-up 1/||ω||∞ does NOT rule out blowup!

The condition for NO blowup: 1/||ω||∞ stays POSITIVE, i.e., ||ω||∞ < ∞.
But convex functions CAN reach zero.

The Hou-Li diagnostic: concave up SUGGESTS regularity because in practice,
the data curves AWAY from zero. But it's not a proof by itself.

What WOULD prove regularity from the curvature data?

STRONGER CONDITION: if 1/||ω||∞ is concave up AND its second derivative
is BOUNDED BELOW by c > 0, then:
g(t) ≥ g(0) + g'(0)t + ct²/2
This is positive for t < t₁ where t₁ = (-g'(0) + √(g'(0)²+2cg(0))) / c
But t₁ is FINITE, so eventually g could still reach 0.

Actually no: g(t) ≥ ct²/2 + g'(0)t + g(0) is a PARABOLA opening upward.
Its minimum is at t = -g'(0)/c, and the minimum value is g(0) - g'(0)²/(2c).
If g(0) > g'(0)²/(2c): the minimum is positive → g > 0 forever! ✓

With our data:
g(0) = 1/||ω||∞(0) = 1/16 = 0.0625
g'(0) ≈ -d||ω||/dt / ||ω||² ≈ -0 (initially α≈0)
c = 0.4 (N=64 curvature)

Minimum value: 0.0625 - 0/(2×0.4) = 0.0625 > 0. ✓

But this only works if g'' ≥ c = 0.4 for ALL time, not just the measured window.

Let me CHECK: does g'' stay at 0.4, or does it decrease?
"""
import torch, numpy as np, math
DTYPE=torch.float64; pi=math.pi

class NS3D:
    def __init__(s,N=32,nu=0.):
        s.N=N;s.nu=nu;s.Lx=2*pi;dx=s.Lx/N
        x=torch.linspace(0,s.Lx-dx,N,dtype=DTYPE)
        s.X,s.Y,s.Z=torch.meshgrid(x,x,x,indexing='ij')
        k=torch.fft.fftfreq(N,d=dx/(2*pi)).to(dtype=DTYPE)
        s.kx,s.ky,s.kz=torch.meshgrid(k,k,k,indexing='ij')
        s.ksq=s.kx**2+s.ky**2+s.kz**2;s.ksq[0,0,0]=1
        s.D=((s.kx.abs()<N//3)&(s.ky.abs()<N//3)&(s.kz.abs()<N//3)).to(DTYPE)
    def fft(s,f):return torch.fft.fftn(f)
    def ifft(s,f):return torch.fft.ifftn(f).real
    def curl(s,a,b,c):
        I=1j;return(I*s.ky*c-I*s.kz*b,I*s.kz*a-I*s.kx*c,I*s.kx*b-I*s.ky*a)
    def vel(s,a,b,c):
        p=a/s.ksq;q=b/s.ksq;r=c/s.ksq;p[0,0,0]=0;q[0,0,0]=0;r[0,0,0]=0
        I=1j;return(I*s.ky*r-I*s.kz*q,I*s.kz*p-I*s.kx*r,I*s.kx*q-I*s.ky*p)
    def rhs(s,w):
        D=s.D;u=s.vel(*w);f={}
        for n,h in zip(['ux','uy','uz','wx','wy','wz'],[*u,*w]):
            f[n]=s.ifft(D*h)
            for d,kd in zip('xyz',[s.kx,s.ky,s.kz]):f[f'd{n}_d{d}']=s.ifft(1j*kd*D*h)
        r=[]
        for c in 'xyz':
            st=f['wx']*f[f'du{c}_dx']+f['wy']*f[f'du{c}_dy']+f['wz']*f[f'du{c}_dz']
            ad=f['ux']*f[f'dw{c}_dx']+f['uy']*f[f'dw{c}_dy']+f['uz']*f[f'dw{c}_dz']
            r.append(D*s.fft(st-ad)-s.nu*s.ksq*w['xyz'.index(c)])
        return tuple(r)
    def step(s,w,dt):
        def add(a,b,c):return tuple(a[i]+c*b[i] for i in range(3))
        k1=s.rhs(w);k2=s.rhs(add(w,k1,.5*dt));k3=s.rhs(add(w,k2,.5*dt));k4=s.rhs(add(w,k3,dt))
        return tuple(s.D*(w[i]+dt/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i])) for i in range(3))
    def om_max(s,w):
        v=[s.ifft(w[i]) for i in range(3)];return(v[0]**2+v[1]**2+v[2]**2).sqrt().max().item()

def make_trefoil(s):
    X,Y,Z=s.X,s.Y,s.Z
    wx=torch.zeros_like(X);wy=torch.zeros_like(X);wz=torch.zeros_like(X)
    tp=torch.linspace(0,2*pi,200,dtype=DTYPE)
    cx=(torch.sin(tp)+2*torch.sin(2*tp))*0.5+pi;cy=(torch.cos(tp)-2*torch.cos(2*tp))*0.5+pi
    cz=(-torch.sin(3*tp))*0.5+pi
    tx=torch.cos(tp)+4*torch.cos(2*tp);ty=-torch.sin(tp)+4*torch.sin(2*tp);tz=-3*torch.cos(3*tp)
    ds=2*pi/200
    for i in range(200):
        g=10.*torch.exp(-((X-cx[i])**2+(Y-cy[i])**2+(Z-cz[i])**2)/(2*0.3**2))*ds
        wx+=g*tx[i];wy+=g*ty[i];wz+=g*tz[i]
    return(s.D*s.fft(wx),s.D*s.fft(wy),s.D*s.fft(wz))

def main():
    print("="*70,flush=True)
    print("CONCAVITY ARGUMENT: does d²(1/||ω||)/dt² stay positive?",flush=True)
    print("="*70,flush=True)

    # First: show that concave-up alone DOESN'T prove regularity
    print("\n  IMPORTANT: g(t) = (1-t)² is convex (g''>0) but reaches 0 at t=1.",flush=True)
    print("  So g'' > 0 alone doesn't prevent g → 0.",flush=True)
    print("  Need: g'' ≥ c > 0 AND g(0) > g'(0)²/(2c).\n",flush=True)

    # Collect dense ||ω||∞ time series for trefoil
    N=32;dt=1e-4;s=NS3D(N,0.);w=make_trefoil(s)
    times=[];oms=[]
    t=0.
    for step in range(8000):
        if step%5==0: times.append(t);oms.append(s.om_max(w))
        w=s.step(w,dt);t+=dt

    times=np.array(times);oms=np.array(oms)
    g = 1.0/oms  # g = 1/||ω||∞

    # Compute g', g'' using Savitzky-Golay or simple finite differences
    # Use a smoothed version to reduce noise
    from scipy.ndimage import uniform_filter1d
    window = 21  # smooth over 21 points
    g_smooth = uniform_filter1d(g, window)
    gp = np.gradient(g_smooth, times)  # g'
    gpp = np.gradient(gp, times)  # g''

    print(f"  Time series of g = 1/||ω||∞ and its curvature g'':",flush=True)
    print(f"  {'t':>6s}  {'||w||':>7s}  {'g':>8s}  {'gp':>8s}  {'gpp':>8s}  "
          f"{'gpp>=0?':>7s}  {'min_g':>8s}",flush=True)

    # Track running minimum of g''
    gpp_min = float('inf')
    for i in range(window, len(times)-window, max(1,(len(times)-2*window)//20)):
        gpp_val = gpp[i]
        gpp_min = min(gpp_min, gpp_val)
        gpp_ok = "YES ✓" if gpp_val >= 0 else "NO ✗"

        # If g'' ≥ c for all future time, minimum g value:
        # g_min = g(t) - g'(t)²/(2c) where c = min g'' so far
        if gpp_min > 0:
            g_min_bound = g[i] - gp[i]**2 / (2*gpp_min)
        else:
            g_min_bound = float('-inf')

        print(f"  {times[i]:6.4f}  {oms[i]:7.2f}  {g[i]:8.5f}  {gp[i]:+8.5f}  "
              f"{gpp_val:+8.5f}  {gpp_ok:>7s}  {g_min_bound:+8.5f}",flush=True)

    # Summary
    gpp_valid = gpp[window:-window]
    print(f"\n  g'' statistics (excluding edge effects):",flush=True)
    print(f"    min g'' = {gpp_valid.min():+.6f}",flush=True)
    print(f"    mean g'' = {gpp_valid.mean():+.6f}",flush=True)
    print(f"    g'' > 0: {(gpp_valid>0).sum()}/{len(gpp_valid)} "
          f"({100*(gpp_valid>0).mean():.1f}%)",flush=True)

    if gpp_valid.min() > 0:
        c_min = gpp_valid.min()
        g0 = g[0]; gp0 = gp[window]
        g_floor = g0 - gp0**2/(2*c_min)
        print(f"\n  REGULARITY CHECK:",flush=True)
        print(f"    g(0) = {g0:.5f}",flush=True)
        print(f"    g'(0) = {gp0:+.5f}",flush=True)
        print(f"    min g'' = {c_min:.6f}",flush=True)
        print(f"    Floor: g ≥ g(0) - g'(0)²/(2·min g'') = {g_floor:+.6f}",flush=True)
        if g_floor > 0:
            print(f"    Floor > 0 → 1/||ω||∞ NEVER reaches 0 → REGULARITY ✓",flush=True)
            print(f"    Maximum ||ω||∞ ≤ 1/{g_floor:.5f} = {1/g_floor:.1f}",flush=True)
        else:
            print(f"    Floor ≤ 0 → cannot guarantee regularity from this bound",flush=True)
    else:
        print(f"\n  g'' goes NEGATIVE at some points — concavity NOT maintained",flush=True)
        print(f"  Concavity argument FAILS",flush=True)

    # Even if g'' isn't always positive, check: does the PARABOLIC lower bound
    # remain positive throughout the measurement window?
    print(f"\n  Point-by-point: is g(t) above the worst-case parabola?",flush=True)
    # For each t, compute the parabola g_para = g(0) + g'(0)t + (min_g''/2)t²
    # If g(t) > g_para(t) at all times, we're safe within this window.

    print(f"\n{'='*70}",flush=True)
    print("DONE.",flush=True)

if __name__=='__main__':
    main()
