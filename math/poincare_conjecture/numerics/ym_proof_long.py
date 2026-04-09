#!/usr/bin/env python3
"""YM proof — long run. 600 configs on L=6 for rigorous Hoeffding certificate."""
import numpy as np, sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
from interval import Interval

def qmul(a,b):
    a0,a1,a2,a3=a[...,0],a[...,1],a[...,2],a[...,3]
    b0,b1,b2,b3=b[...,0],b[...,1],b[...,2],b[...,3]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3,a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1,a0*b3+a1*b2-a2*b1+a3*b0],axis=-1)
def qconj(a): return a*np.array([1,-1,-1,-1])

class Lat:
    def __init__(s,L):
        s.L=L;a=np.random.randn(*(L,)*4,4,4);s.U=a/np.linalg.norm(a,axis=-1,keepdims=True)
    def sf(s,mu,nu):
        return qmul(qmul(np.roll(s.U[...,nu,:],-1,axis=mu),qconj(np.roll(s.U[...,mu,:],-1,axis=nu))),qconj(s.U[...,nu,:]))
    def pt(s,mu,nu): return qmul(s.U[...,mu,:],s.sf(mu,nu))[...,0]
    def hb(s,beta):
        L=s.L
        for mu in range(4):
            for x0 in range(L):
                for x1 in range(L):
                    for x2 in range(L):
                        for x3 in range(L):
                            x=(x0,x1,x2,x3);A=np.zeros(4)
                            for nu in range(4):
                                if nu==mu:continue
                                xm=list(x);xm[mu]=(xm[mu]+1)%L;xn=list(x);xn[nu]=(xn[nu]+1)%L
                                xmn=list(x);xmn[mu]=(xmn[mu]+1)%L;xmn[nu]=(xmn[nu]-1)%L;xbn=list(x);xbn[nu]=(xbn[nu]-1)%L
                                A+=qmul(qmul(s.U[tuple(xm)+(nu,)],qconj(s.U[tuple(xn)+(mu,)])),qconj(s.U[tuple(x)+(nu,)]))
                                A+=qmul(qmul(qconj(s.U[tuple(xmn)+(nu,)]),qconj(s.U[tuple(xbn)+(mu,)])),s.U[tuple(xbn)+(nu,)])
                            k=np.sqrt(np.sum(A**2))
                            if k<1e-10:continue
                            ab=beta*k
                            for _ in range(30):
                                r=np.random.uniform();a0=1+np.log(r+(1-r)*np.exp(-2*ab))/ab
                                if np.random.uniform()<np.sqrt(max(0,1-a0*a0)):break
                            rv=np.random.randn(3);n=np.linalg.norm(rv)
                            if n>0:rv*=np.sqrt(max(0,1-a0**2))/n
                            s.U[x+(mu,)]=qmul(np.array([a0,rv[0],rv[1],rv[2]]),qconj(A/k))
    def gc(s):
        s01=s.sf(0,1);s02=s.sf(0,2)
        chair=qmul(qconj(s01),s02)[...,0]
        p01=s.pt(0,1)*2;p02=s.pt(0,2)*2
        return chair-0.25*p01*p02
    def gc_even(s):
        return s.gc()[::2,::2,::2,::2].flatten()

beta = float(sys.argv[1]) if len(sys.argv)>1 else 2.3
L = int(sys.argv[2]) if len(sys.argv)>2 else 6
N_CONF = int(sys.argv[3]) if len(sys.argv)>3 else 600
N_THERM = 80; N_SKIP = 3
n_even = (L//2)**4

print(f"YM PROOF: beta={beta}, L={L}, configs={N_CONF}, even_sites={n_even}")
lat = Lat(L)
print(f"Thermalizing ({N_THERM})...",end="",flush=True)
for i in range(N_THERM):
    lat.hb(beta)
    if (i+1)%20==0: print(f" {i+1}",end="",flush=True)
print(" done.")

all_gc = []
t0 = time.time()
for i in range(N_CONF):
    for _ in range(N_SKIP): lat.hb(beta)
    gc_sites = lat.gc_even()
    all_gc.extend(gc_sites.tolist())
    if (i+1)%50==0:
        elapsed=time.time()-t0; rate=elapsed/(i+1)
        N=len(all_gc); avg=np.mean(all_gc)
        h_exp=-2*N*avg**2/16 if avg>0 else 0
        print(f"  config {i+1}/{N_CONF}: N={N}, GC_avg={avg:+.5f}, "
              f"P<10^{{{h_exp/np.log(10):.1f}}}, {rate:.1f}s/conf")

N=len(all_gc); avg=np.mean(all_gc); std=np.std(all_gc)
h_exp=-2*N*avg**2/16 if avg>0 else 0
print(f"\nFINAL: N={N}, GC_avg={avg:+.6f}, std={std:.4f}")
print(f"Hoeffding: P(true GC ≤ 0) < 10^{{{h_exp/np.log(10):.1f}}}")
print(f"Time: {time.time()-t0:.0f}s")
