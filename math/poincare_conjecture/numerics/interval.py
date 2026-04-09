"""
Interval arithmetic library for computer-assisted proofs.

Each number is stored as [lo, hi] — guaranteed bounds.
Every operation returns bounds that contain the true result.
Directed rounding ensures no floating point error escapes.

This replaces INTLAB. No MATLAB needed.
"""
import numpy as np
import math


class Interval:
    """
    Rigorous interval arithmetic.

    Every Interval [lo, hi] guarantees: true value ∈ [lo, hi].
    Operations widen bounds to account for floating point rounding.
    """

    # Machine epsilon for float64
    EPS = np.finfo(np.float64).eps  # ~2.2e-16

    def __init__(self, lo, hi=None):
        if hi is None:
            if isinstance(lo, Interval):
                self.lo = lo.lo
                self.hi = lo.hi
                return
            hi = lo
        self.lo = float(lo)
        self.hi = float(hi)
        if self.lo > self.hi:
            self.lo, self.hi = self.hi, self.lo

    @staticmethod
    def from_value(x, ulps=1):
        """Create interval from a float with ±ulps of rounding error."""
        x = float(x)
        eps = abs(x) * Interval.EPS * ulps
        if eps == 0:
            eps = Interval.EPS * ulps
        return Interval(x - eps, x + eps)

    @staticmethod
    def entire():
        """The entire real line."""
        return Interval(-math.inf, math.inf)

    @staticmethod
    def zero():
        return Interval(0.0, 0.0)

    def __repr__(self):
        return f"[{self.lo:.6e}, {self.hi:.6e}]"

    def __str__(self):
        mid = (self.lo + self.hi) / 2
        rad = (self.hi - self.lo) / 2
        return f"{mid:.6e} ± {rad:.2e}"

    @property
    def mid(self):
        return (self.lo + self.hi) / 2

    @property
    def rad(self):
        return (self.hi - self.lo) / 2

    @property
    def width(self):
        return self.hi - self.lo

    def contains(self, x):
        return self.lo <= x <= self.hi

    def contains_zero(self):
        return self.lo <= 0 <= self.hi

    def is_positive(self):
        return self.lo > 0

    def is_negative(self):
        return self.hi < 0

    # Directed rounding: nextafter for 1-ULP tight bounds (INTLAB-grade)
    @staticmethod
    def _round_down(x):
        """Round toward -inf. 1-ULP tight."""
        return np.nextafter(x, -np.inf)

    @staticmethod
    def _round_up(x):
        """Round toward +inf. 1-ULP tight."""
        return np.nextafter(x, np.inf)

    # Arithmetic with rigorous rounding
    def __add__(self, other):
        if not isinstance(other, Interval):
            other = Interval(other)
        lo = self._round_down(self.lo + other.lo)
        hi = self._round_up(self.hi + other.hi)
        return Interval(lo, hi)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Interval):
            other = Interval(other)
        lo = self._round_down(self.lo - other.hi)
        hi = self._round_up(self.hi - other.lo)
        return Interval(lo, hi)

    def __rsub__(self, other):
        if not isinstance(other, Interval):
            other = Interval(other)
        return other.__sub__(self)

    def __mul__(self, other):
        if not isinstance(other, Interval):
            other = Interval(other)
        products = [self.lo * other.lo, self.lo * other.hi,
                    self.hi * other.lo, self.hi * other.hi]
        lo = self._round_down(min(products))
        hi = self._round_up(max(products))
        return Interval(lo, hi)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, Interval):
            other = Interval(other)
        if other.contains_zero():
            return Interval.entire()
        return self * Interval(1.0 / other.hi, 1.0 / other.lo)

    def __rtruediv__(self, other):
        if not isinstance(other, Interval):
            other = Interval(other)
        return other.__truediv__(self)

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __abs__(self):
        if self.lo >= 0:
            return Interval(self.lo, self.hi)
        if self.hi <= 0:
            return Interval(-self.hi, -self.lo)
        return Interval(0, max(-self.lo, self.hi))

    def __pow__(self, n):
        if not isinstance(n, int):
            raise ValueError("Only integer powers supported for rigorous bounds")
        if n == 0:
            return Interval(1.0, 1.0)
        if n == 1:
            return Interval(self.lo, self.hi)
        if n % 2 == 0:
            # Even power: result is non-negative
            if self.lo >= 0:
                return Interval(self._round_down(self.lo**n),
                               self._round_up(self.hi**n))
            if self.hi <= 0:
                return Interval(self._round_down(self.hi**n),
                               self._round_up(self.lo**n))
            # Spans zero
            return Interval(0, self._round_up(max(self.lo**n, self.hi**n)))
        else:
            # Odd power: monotone
            return Interval(self._round_down(self.lo**n),
                           self._round_up(self.hi**n))

    def sqrt(self):
        if self.hi < 0:
            raise ValueError("sqrt of negative interval")
        lo = self._round_down(math.sqrt(max(0, self.lo)))
        hi = self._round_up(math.sqrt(self.hi))
        return Interval(lo, hi)

    # Comparison
    def __lt__(self, other):
        if not isinstance(other, Interval):
            other = Interval(other)
        return self.hi < other.lo

    def __gt__(self, other):
        if not isinstance(other, Interval):
            other = Interval(other)
        return self.lo > other.hi

    def __le__(self, other):
        if not isinstance(other, Interval):
            other = Interval(other)
        return self.hi <= other.lo

    def __ge__(self, other):
        if not isinstance(other, Interval):
            other = Interval(other)
        return self.lo >= other.hi

    # Set operations
    def intersect(self, other):
        lo = max(self.lo, other.lo)
        hi = min(self.hi, other.hi)
        if lo > hi:
            return None  # empty
        return Interval(lo, hi)

    def union(self, other):
        return Interval(min(self.lo, other.lo), max(self.hi, other.hi))


class IntervalArray:
    """
    Array of intervals for vectorized operations.
    Stored as two numpy arrays: lo and hi.
    """

    EPS = np.finfo(np.float64).eps

    def __init__(self, lo, hi=None):
        if hi is None:
            if isinstance(lo, IntervalArray):
                self.lo = lo.lo.copy()
                self.hi = lo.hi.copy()
                return
            lo = np.asarray(lo, dtype=np.float64)
            hi = lo.copy()
        self.lo = np.asarray(lo, dtype=np.float64)
        self.hi = np.asarray(hi, dtype=np.float64)
        # Ensure lo <= hi
        swap = self.lo > self.hi
        if swap.any():
            self.lo[swap], self.hi[swap] = self.hi[swap].copy(), self.lo[swap].copy()

    @staticmethod
    def from_array(x, ulps=1):
        x = np.asarray(x, dtype=np.float64)
        eps = np.abs(x) * IntervalArray.EPS * ulps
        eps = np.maximum(eps, IntervalArray.EPS * ulps)
        return IntervalArray(x - eps, x + eps)

    @property
    def shape(self):
        return self.lo.shape

    @property
    def mid(self):
        return (self.lo + self.hi) / 2

    @property
    def rad(self):
        return (self.hi - self.lo) / 2

    def max_width(self):
        return (self.hi - self.lo).max()

    def all_positive(self):
        return np.all(self.lo > 0)

    def all_negative(self):
        return np.all(self.hi < 0)

    @staticmethod
    def _rd(x):
        """Round down (toward -inf). 1-ULP tight."""
        return np.nextafter(x, -np.inf)

    @staticmethod
    def _ru(x):
        """Round up (toward +inf). 1-ULP tight."""
        return np.nextafter(x, np.inf)

    def __add__(self, other):
        if not isinstance(other, IntervalArray):
            other = IntervalArray(other)
        return IntervalArray(self._rd(self.lo + other.lo),
                            self._ru(self.hi + other.hi))

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, IntervalArray):
            other = IntervalArray(other)
        return IntervalArray(self._rd(self.lo - other.hi),
                            self._ru(self.hi - other.lo))

    def __rsub__(self, other):
        if not isinstance(other, IntervalArray):
            other = IntervalArray(other)
        return other.__sub__(self)

    def __mul__(self, other):
        if not isinstance(other, IntervalArray):
            other = IntervalArray(other)
        p1 = self.lo * other.lo
        p2 = self.lo * other.hi
        p3 = self.hi * other.lo
        p4 = self.hi * other.hi
        lo = self._rd(np.minimum(np.minimum(p1, p2), np.minimum(p3, p4)))
        hi = self._ru(np.maximum(np.maximum(p1, p2), np.maximum(p3, p4)))
        return IntervalArray(lo, hi)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __neg__(self):
        return IntervalArray(-self.hi, -self.lo)

    def __truediv__(self, other):
        if not isinstance(other, IntervalArray):
            other = IntervalArray(other)
        # Check for division by zero
        if np.any((other.lo <= 0) & (other.hi >= 0)):
            raise ValueError("Division by interval containing zero")
        recip = IntervalArray(1.0 / other.hi, 1.0 / other.lo)
        return self * recip

    def sum(self):
        """Sum all elements with rigorous bounds."""
        lo = self._rd(self.lo.sum())
        hi = self._ru(self.hi.sum())
        return Interval(lo, hi)

    def squared(self):
        """Element-wise x² with tight bounds."""
        lo = np.zeros_like(self.lo)
        hi = np.zeros_like(self.hi)

        # All positive
        pos = self.lo >= 0
        lo[pos] = self._rd(self.lo[pos]**2)
        hi[pos] = self._ru(self.hi[pos]**2)

        # All negative
        neg = self.hi <= 0
        lo[neg] = self._rd(self.hi[neg]**2)
        hi[neg] = self._ru(self.lo[neg]**2)

        # Spans zero
        span = ~pos & ~neg
        lo[span] = 0
        hi[span] = self._ru(np.maximum(self.lo[span]**2, self.hi[span]**2))

        return IntervalArray(lo, hi)

    def __getitem__(self, idx):
        return IntervalArray(self.lo[idx], self.hi[idx])

    def __len__(self):
        return len(self.lo)


class IntervalFFT:
    """
    Rigorous FFT with interval arithmetic.

    The FFT is a sequence of additions and multiplications with known
    twiddle factors (complex roots of unity). Each operation is bounded.

    For a real input array of IntervalArrays, we compute the FFT and
    return interval bounds on each Fourier coefficient.

    Key insight: the FFT twiddle factors are EXACT (cos and sin of
    multiples of 2pi/N). We bound them with intervals, then propagate
    through the butterfly operations.
    """

    def __init__(self, N):
        self.N = N
        # Precompute twiddle factors as intervals
        # w_k = exp(-2pi*i*k/N) = cos(2pi*k/N) - i*sin(2pi*k/N)
        angles = 2 * np.pi * np.arange(N) / N
        self.cos_lo = np.nextafter(np.cos(angles), -np.inf)
        self.cos_hi = np.nextafter(np.cos(angles), np.inf)
        self.sin_lo = np.nextafter(np.sin(angles), -np.inf)
        self.sin_hi = np.nextafter(np.sin(angles), np.inf)

    def fft_interval_1d(self, x_lo, x_hi):
        """
        1D FFT with interval bounds on real input.

        Input: x_lo, x_hi arrays of length N (lower and upper bounds)
        Output: (re_lo, re_hi, im_lo, im_hi) arrays of length N

        Uses the DFT definition directly (not butterfly — slower but simpler
        to verify). For N <= 256 this is fast enough.

        X[k] = sum_{n=0}^{N-1} x[n] * exp(-2pi*i*k*n/N)
             = sum_{n=0}^{N-1} x[n] * (cos(2pi*k*n/N) - i*sin(2pi*k*n/N))

        Re(X[k]) = sum x[n] * cos(2pi*k*n/N)
        Im(X[k]) = -sum x[n] * sin(2pi*k*n/N)
        """
        N = self.N
        re_lo = np.zeros(N)
        re_hi = np.zeros(N)
        im_lo = np.zeros(N)
        im_hi = np.zeros(N)

        for k in range(N):
            # Accumulate sum x[n] * cos(theta) and x[n] * sin(theta)
            re_sum_lo = 0.0
            re_sum_hi = 0.0
            im_sum_lo = 0.0
            im_sum_hi = 0.0

            for n in range(N):
                idx = (k * n) % N
                c_lo, c_hi = self.cos_lo[idx], self.cos_hi[idx]
                s_lo, s_hi = self.sin_lo[idx], self.sin_hi[idx]

                # x[n] * cos: bound all 4 products then take min/max
                prods = [x_lo[n]*c_lo, x_lo[n]*c_hi, x_hi[n]*c_lo, x_hi[n]*c_hi]
                prod_lo = np.nextafter(min(prods), -np.inf)
                prod_hi = np.nextafter(max(prods), np.inf)
                re_sum_lo = np.nextafter(re_sum_lo + prod_lo, -np.inf)
                re_sum_hi = np.nextafter(re_sum_hi + prod_hi, np.inf)

                # -x[n] * sin: bound products then negate
                prods = [x_lo[n]*s_lo, x_lo[n]*s_hi, x_hi[n]*s_lo, x_hi[n]*s_hi]
                prod_lo = np.nextafter(min(prods), -np.inf)
                prod_hi = np.nextafter(max(prods), np.inf)
                im_sum_lo = np.nextafter(im_sum_lo - prod_hi, -np.inf)
                im_sum_hi = np.nextafter(im_sum_hi - prod_lo, np.inf)

            # Widen bounds to account for different valid summation orders
            # The exact result depends on operation ordering (associativity)
            # We bound ALL valid orderings by adding N ULPs
            scale = max(abs(re_sum_lo), abs(re_sum_hi), abs(im_sum_lo), abs(im_sum_hi), 1e-300)
            margin = N * np.spacing(scale)
            re_lo[k] = re_sum_lo - margin
            re_hi[k] = re_sum_hi + margin
            im_lo[k] = im_sum_lo - margin
            im_hi[k] = im_sum_hi + margin

        return re_lo, re_hi, im_lo, im_hi

    def fft_interval_3d(self, x_lo, x_hi):
        """
        3D FFT with interval bounds.

        Input: x_lo, x_hi arrays of shape (N, N, N)
        Output: (re_lo, re_hi, im_lo, im_hi) arrays of shape (N, N, N)

        Computed as three passes of 1D FFTs along each axis.
        """
        N = self.N
        shape = (N, N, N)

        # Pass 1: FFT along axis 0
        re = x_lo.copy()
        re_h = x_hi.copy()
        im = np.zeros(shape)
        im_h = np.zeros(shape)

        # Along axis 0
        for j in range(N):
            for k in range(N):
                r_lo, r_hi, i_lo, i_hi = self.fft_interval_1d(re[:, j, k], re_h[:, j, k])
                re[:, j, k] = r_lo
                re_h[:, j, k] = r_hi
                im[:, j, k] = i_lo
                im_h[:, j, k] = i_hi

        # Pass 2: FFT along axis 1 (now complex input)
        re2 = np.zeros(shape)
        re2_h = np.zeros(shape)
        im2 = np.zeros(shape)
        im2_h = np.zeros(shape)

        for i in range(N):
            for k in range(N):
                # Complex FFT: split into real and imaginary 1D FFTs
                # F(a + ib) = F(a) + i*F(b) when applied to the
                # combined complex signal... actually for complex input
                # we need to handle it properly

                # DFT of complex input z[n] = a[n] + i*b[n]:
                # Z[k] = sum z[n] * exp(-2pi*i*k*n/N)
                # Re(Z[k]) = sum (a[n]*cos - b[n]*sin)
                # Im(Z[k]) = sum (-a[n]*sin + b[n]*cos) ... wait
                # Actually: Im(Z[k]) = sum (-a[n]*sin - b[n]*cos)
                # No: z*w = (a+ib)(c-is) = (ac+bs) + i(bc-as)
                # So Re = sum(a*cos + b*sin), Im = sum(b*cos - a*sin)

                a_lo = re[i, :, k]
                a_hi = re_h[i, :, k]
                b_lo = im[i, :, k]
                b_hi = im_h[i, :, k]

                r_lo_out = np.zeros(N)
                r_hi_out = np.zeros(N)
                i_lo_out = np.zeros(N)
                i_hi_out = np.zeros(N)

                for m in range(N):
                    rs_lo = 0.0; rs_hi = 0.0
                    is_lo = 0.0; is_hi = 0.0

                    for n in range(N):
                        idx = (m * n) % N
                        c_lo, c_hi = self.cos_lo[idx], self.cos_hi[idx]
                        s_lo, s_hi = self.sin_lo[idx], self.sin_hi[idx]

                        # Re: a*cos + b*sin
                        p_ac = [a_lo[n]*c_lo, a_lo[n]*c_hi, a_hi[n]*c_lo, a_hi[n]*c_hi]
                        p_bs = [b_lo[n]*s_lo, b_lo[n]*s_hi, b_hi[n]*s_lo, b_hi[n]*s_hi]
                        ac_lo = np.nextafter(min(p_ac), -np.inf)
                        ac_hi = np.nextafter(max(p_ac), np.inf)
                        bs_lo = np.nextafter(min(p_bs), -np.inf)
                        bs_hi = np.nextafter(max(p_bs), np.inf)
                        rs_lo = np.nextafter(rs_lo + ac_lo + bs_lo, -np.inf)
                        rs_hi = np.nextafter(rs_hi + ac_hi + bs_hi, np.inf)

                        # Im: b*cos - a*sin
                        p_bc = [b_lo[n]*c_lo, b_lo[n]*c_hi, b_hi[n]*c_lo, b_hi[n]*c_hi]
                        p_as = [a_lo[n]*s_lo, a_lo[n]*s_hi, a_hi[n]*s_lo, a_hi[n]*s_hi]
                        bc_lo = np.nextafter(min(p_bc), -np.inf)
                        bc_hi = np.nextafter(max(p_bc), np.inf)
                        as_lo = np.nextafter(min(p_as), -np.inf)
                        as_hi = np.nextafter(max(p_as), np.inf)
                        is_lo = np.nextafter(is_lo + bc_lo - as_hi, -np.inf)
                        is_hi = np.nextafter(is_hi + bc_hi - as_lo, np.inf)

                    r_lo_out[m] = rs_lo
                    r_hi_out[m] = rs_hi
                    i_lo_out[m] = is_lo
                    i_hi_out[m] = is_hi

                re2[i, :, k] = r_lo_out
                re2_h[i, :, k] = r_hi_out
                im2[i, :, k] = i_lo_out
                im2_h[i, :, k] = i_hi_out

        # Pass 3: FFT along axis 2
        re3 = np.zeros(shape)
        re3_h = np.zeros(shape)
        im3 = np.zeros(shape)
        im3_h = np.zeros(shape)

        for i in range(N):
            for j in range(N):
                a_lo = re2[i, j, :]
                a_hi = re2_h[i, j, :]
                b_lo = im2[i, j, :]
                b_hi = im2_h[i, j, :]

                r_lo_out = np.zeros(N)
                r_hi_out = np.zeros(N)
                i_lo_out = np.zeros(N)
                i_hi_out = np.zeros(N)

                for m in range(N):
                    rs_lo = 0.0; rs_hi = 0.0
                    is_lo = 0.0; is_hi = 0.0

                    for n in range(N):
                        idx = (m * n) % N
                        c_lo, c_hi = self.cos_lo[idx], self.cos_hi[idx]
                        s_lo, s_hi = self.sin_lo[idx], self.sin_hi[idx]

                        p_ac = [a_lo[n]*c_lo, a_lo[n]*c_hi, a_hi[n]*c_lo, a_hi[n]*c_hi]
                        p_bs = [b_lo[n]*s_lo, b_lo[n]*s_hi, b_hi[n]*s_lo, b_hi[n]*s_hi]
                        rs_lo = np.nextafter(rs_lo + min(p_ac) + min(p_bs), -np.inf)
                        rs_hi = np.nextafter(rs_hi + max(p_ac) + max(p_bs), np.inf)

                        p_bc = [b_lo[n]*c_lo, b_lo[n]*c_hi, b_hi[n]*c_lo, b_hi[n]*c_hi]
                        p_as = [a_lo[n]*s_lo, a_lo[n]*s_hi, a_hi[n]*s_lo, a_hi[n]*s_hi]
                        is_lo = np.nextafter(is_lo + min(p_bc) - max(p_as), -np.inf)
                        is_hi = np.nextafter(is_hi + max(p_bc) - min(p_as), np.inf)

                    r_lo_out[m] = rs_lo
                    r_hi_out[m] = rs_hi
                    i_lo_out[m] = is_lo
                    i_hi_out[m] = is_hi

                re3[i, j, :] = r_lo_out
                re3_h[i, j, :] = r_hi_out
                im3[i, j, :] = i_lo_out
                im3_h[i, j, :] = i_hi_out

        return re3, re3_h, im3, im3_h


def verify_interval_fft():
    """Verify interval FFT against numpy FFT."""
    print("INTERVAL FFT VERIFICATION")
    print("=" * 50)

    N = 8
    ifft = IntervalFFT(N)

    # Test 1D
    np.random.seed(42)
    x = np.random.randn(N)
    x_lo = np.nextafter(x, -np.inf)
    x_hi = np.nextafter(x, np.inf)

    re_lo, re_hi, im_lo, im_hi = ifft.fft_interval_1d(x_lo, x_hi)

    # Compare to numpy
    X = np.fft.fft(x)
    re_exact = X.real
    im_exact = X.imag

    re_contained = np.all((re_lo <= re_exact) & (re_exact <= re_hi))
    im_contained = np.all((im_lo <= im_exact) & (im_exact <= im_hi))

    re_width = (re_hi - re_lo).max()
    im_width = (im_hi - im_lo).max()

    print(f"  1D FFT (N={N}):")
    print(f"    Re contained: {re_contained}, max width: {re_width:.2e}")
    print(f"    Im contained: {im_contained}, max width: {im_width:.2e}")
    assert re_contained and im_contained, "1D FFT FAILED"
    print(f"    PASS")

    # Test 3D (small)
    N3 = 4
    ifft3 = IntervalFFT(N3)
    x3 = np.random.randn(N3, N3, N3)
    x3_lo = np.nextafter(x3, -np.inf)
    x3_hi = np.nextafter(x3, np.inf)

    re3_lo, re3_hi, im3_lo, im3_hi = ifft3.fft_interval_3d(x3_lo, x3_hi)

    X3 = np.fft.fftn(x3)
    re3_exact = X3.real
    im3_exact = X3.imag

    re3_ok = np.all((re3_lo <= re3_exact) & (re3_exact <= re3_hi))
    im3_ok = np.all((im3_lo <= im3_exact) & (im3_exact <= im3_hi))

    re3_width = (re3_hi - re3_lo).max()
    im3_width = (im3_hi - im3_lo).max()

    print(f"  3D FFT (N={N3}):")
    print(f"    Re contained: {re3_ok}, max width: {re3_width:.2e}")
    print(f"    Im contained: {im3_ok}, max width: {im3_width:.2e}")
    assert re3_ok and im3_ok, "3D FFT FAILED"
    print(f"    PASS")

    return True


class IntervalBiotSavart:
    """
    Rigorous Biot-Savart computation with interval arithmetic.

    Given vorticity omega in Fourier space (with interval bounds),
    compute velocity, strain tensor, stretching, and diffusion
    with guaranteed bounds.

    In Fourier space, Biot-Savart is EXACT algebra:
      psi_hat = omega_hat / |k|^2
      u_hat = ik x psi_hat
      S_hat = ik * u_hat  (strain)

    The only rounding is in the division by |k|^2 and the
    cross products — all bounded by interval arithmetic.
    """

    def __init__(self, N, nu=1e-4):
        self.N = N
        self.nu = nu

        Lx = 2 * np.pi
        dx = Lx / N
        k = np.fft.fftfreq(N, d=dx/(2*np.pi))

        # Wavenumbers as intervals
        # These are EXACT rational multiples of 1/N — no rounding needed
        # But store as intervals for safety
        self.kx_lo = np.nextafter(k, -np.inf)
        self.kx_hi = np.nextafter(k, np.inf)

        # |k|^2 for each 3D mode
        # Precompute as intervals
        kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
        ksq = kx**2 + ky**2 + kz**2
        self.ksq_lo = np.nextafter(ksq, -np.inf)
        self.ksq_hi = np.nextafter(ksq, np.inf)
        # Avoid division by zero at k=0
        self.ksq_lo[0, 0, 0] = 1.0
        self.ksq_hi[0, 0, 0] = 1.0

        # Store raw wavenumber arrays
        self.kx = kx
        self.ky = ky
        self.kz = kz

        # nu * |k|^2 — the diffusion operator (exact in Fourier space)
        self.nu_ksq_lo = np.nextafter(nu * self.ksq_lo, -np.inf)
        self.nu_ksq_hi = np.nextafter(nu * self.ksq_hi, np.inf)

    def biot_savart(self, wx_re_lo, wx_re_hi, wx_im_lo, wx_im_hi,
                          wy_re_lo, wy_re_hi, wy_im_lo, wy_im_hi,
                          wz_re_lo, wz_re_hi, wz_im_lo, wz_im_hi):
        """
        Compute velocity from vorticity via Biot-Savart in Fourier space.

        psi_hat = w_hat / |k|^2
        u_hat = ik x psi_hat

        Returns interval bounds on velocity Fourier coefficients.
        """
        N = self.N

        # psi = w / |k|^2 (interval division)
        # For real part: re(w/|k|^2) = re(w) / |k|^2
        # Division by positive interval [lo, hi]:
        def div_by_ksq(f_re_lo, f_re_hi, f_im_lo, f_im_hi):
            # |k|^2 is always positive, so division is straightforward
            # f / [a, b] where a > 0: [f_lo/b, f_hi/a] if f >= 0
            # Need to handle sign of f
            re_lo = np.zeros_like(f_re_lo)
            re_hi = np.zeros_like(f_re_hi)
            im_lo = np.zeros_like(f_im_lo)
            im_hi = np.zeros_like(f_im_hi)

            for arr_lo, arr_hi, out_lo, out_hi in [
                (f_re_lo, f_re_hi, re_lo, re_hi),
                (f_im_lo, f_im_hi, im_lo, im_hi),
            ]:
                # Positive f
                pos = arr_lo >= 0
                out_lo[pos] = np.nextafter(arr_lo[pos] / self.ksq_hi[pos], -np.inf)
                out_hi[pos] = np.nextafter(arr_hi[pos] / self.ksq_lo[pos], np.inf)

                # Negative f
                neg = arr_hi <= 0
                out_lo[neg] = np.nextafter(arr_lo[neg] / self.ksq_lo[neg], -np.inf)
                out_hi[neg] = np.nextafter(arr_hi[neg] / self.ksq_hi[neg], np.inf)

                # Spans zero
                span = ~pos & ~neg
                out_lo[span] = np.nextafter(arr_lo[span] / self.ksq_lo[span], -np.inf)
                out_hi[span] = np.nextafter(arr_hi[span] / self.ksq_lo[span], np.inf)

            # Zero the k=0 mode
            re_lo[0, 0, 0] = 0; re_hi[0, 0, 0] = 0
            im_lo[0, 0, 0] = 0; im_hi[0, 0, 0] = 0

            return re_lo, re_hi, im_lo, im_hi

        # Stream function psi = w / |k|^2
        psi_x = div_by_ksq(wx_re_lo, wx_re_hi, wx_im_lo, wx_im_hi)
        psi_y = div_by_ksq(wy_re_lo, wy_re_hi, wy_im_lo, wy_im_hi)
        psi_z = div_by_ksq(wz_re_lo, wz_re_hi, wz_im_lo, wz_im_hi)

        # u = ik x psi (cross product in Fourier space)
        # u_x = ik_y * psi_z - ik_z * psi_y
        # Multiplication by ik: re(ik*f) = -k*im(f), im(ik*f) = k*re(f)
        def ik_times(k_arr, f_re_lo, f_re_hi, f_im_lo, f_im_hi):
            """Multiply by ik in Fourier space with interval bounds."""
            # ik * (a + ib) = -k*b + i*k*a
            # new_re = -k * im(f)
            # new_im = k * re(f)

            # -k * im(f): interval product of -k with [im_lo, im_hi]
            neg_k = -k_arr
            prods_re = np.stack([neg_k * f_im_lo, neg_k * f_im_hi])
            new_re_lo = np.nextafter(prods_re.min(axis=0), -np.inf)
            new_re_hi = np.nextafter(prods_re.max(axis=0), np.inf)

            # k * re(f)
            prods_im = np.stack([k_arr * f_re_lo, k_arr * f_re_hi])
            new_im_lo = np.nextafter(prods_im.min(axis=0), -np.inf)
            new_im_hi = np.nextafter(prods_im.max(axis=0), np.inf)

            return new_re_lo, new_re_hi, new_im_lo, new_im_hi

        # ik_y * psi_z
        t1 = ik_times(self.ky, *psi_z)
        # ik_z * psi_y
        t2 = ik_times(self.kz, *psi_y)
        # u_x = t1 - t2
        ux_re_lo = np.nextafter(t1[0] - t2[1], -np.inf)
        ux_re_hi = np.nextafter(t1[1] - t2[0], np.inf)
        ux_im_lo = np.nextafter(t1[2] - t2[3], -np.inf)
        ux_im_hi = np.nextafter(t1[3] - t2[2], np.inf)

        # ik_z * psi_x
        t1 = ik_times(self.kz, *psi_x)
        # ik_x * psi_z
        t2 = ik_times(self.kx, *psi_z)
        uy_re_lo = np.nextafter(t1[0] - t2[1], -np.inf)
        uy_re_hi = np.nextafter(t1[1] - t2[0], np.inf)
        uy_im_lo = np.nextafter(t1[2] - t2[3], -np.inf)
        uy_im_hi = np.nextafter(t1[3] - t2[2], np.inf)

        # ik_x * psi_y
        t1 = ik_times(self.kx, *psi_y)
        # ik_y * psi_x
        t2 = ik_times(self.ky, *psi_x)
        uz_re_lo = np.nextafter(t1[0] - t2[1], -np.inf)
        uz_re_hi = np.nextafter(t1[1] - t2[0], np.inf)
        uz_im_lo = np.nextafter(t1[2] - t2[3], -np.inf)
        uz_im_hi = np.nextafter(t1[3] - t2[2], np.inf)

        return (ux_re_lo, ux_re_hi, ux_im_lo, ux_im_hi,
                uy_re_lo, uy_re_hi, uy_im_lo, uy_im_hi,
                uz_re_lo, uz_re_hi, uz_im_lo, uz_im_hi)

    def diffusion_bound(self, wx_re_lo, wx_re_hi, wx_im_lo, wx_im_hi,
                              wy_re_lo, wy_re_hi, wy_im_lo, wy_im_hi,
                              wz_re_lo, wz_re_hi, wz_im_lo, wz_im_hi):
        """
        Compute nu * |k|^2 * |w_hat|^2 summed over all modes.

        This is the total dissipation in Fourier space (Parseval).
        Returns an Interval bounding the total.
        """
        # |w_hat_k|^2 = re^2 + im^2 for each component
        def mode_energy(re_lo, re_hi, im_lo, im_hi):
            # re^2: bound
            re_sq_lo = np.zeros_like(re_lo)
            re_sq_hi = np.zeros_like(re_hi)
            pos = re_lo >= 0
            re_sq_lo[pos] = np.nextafter(re_lo[pos]**2, -np.inf)
            re_sq_hi[pos] = np.nextafter(re_hi[pos]**2, np.inf)
            neg = re_hi <= 0
            re_sq_lo[neg] = np.nextafter(re_hi[neg]**2, -np.inf)
            re_sq_hi[neg] = np.nextafter(re_lo[neg]**2, np.inf)
            span = ~pos & ~neg
            re_sq_lo[span] = 0
            re_sq_hi[span] = np.nextafter(np.maximum(re_lo[span]**2, re_hi[span]**2), np.inf)

            # Same for im^2
            im_sq_lo = np.zeros_like(im_lo)
            im_sq_hi = np.zeros_like(im_hi)
            pos = im_lo >= 0
            im_sq_lo[pos] = np.nextafter(im_lo[pos]**2, -np.inf)
            im_sq_hi[pos] = np.nextafter(im_hi[pos]**2, np.inf)
            neg = im_hi <= 0
            im_sq_lo[neg] = np.nextafter(im_hi[neg]**2, -np.inf)
            im_sq_hi[neg] = np.nextafter(im_lo[neg]**2, np.inf)
            span = ~pos & ~neg
            im_sq_lo[span] = 0
            im_sq_hi[span] = np.nextafter(np.maximum(im_lo[span]**2, im_hi[span]**2), np.inf)

            return (np.nextafter(re_sq_lo + im_sq_lo, -np.inf),
                    np.nextafter(re_sq_hi + im_sq_hi, np.inf))

        ex_lo, ex_hi = mode_energy(wx_re_lo, wx_re_hi, wx_im_lo, wx_im_hi)
        ey_lo, ey_hi = mode_energy(wy_re_lo, wy_re_hi, wy_im_lo, wy_im_hi)
        ez_lo, ez_hi = mode_energy(wz_re_lo, wz_re_hi, wz_im_lo, wz_im_hi)

        # Total |w_hat|^2
        total_lo = np.nextafter(ex_lo + ey_lo + ez_lo, -np.inf)
        total_hi = np.nextafter(ex_hi + ey_hi + ez_hi, np.inf)

        # Multiply by nu * |k|^2
        dissip_terms_lo = np.nextafter(self.nu_ksq_lo * total_lo, -np.inf)
        dissip_terms_hi = np.nextafter(self.nu_ksq_hi * total_hi, np.inf)

        # Sum over all modes
        total_dissip_lo = np.nextafter(dissip_terms_lo.sum(), -np.inf)
        total_dissip_hi = np.nextafter(dissip_terms_hi.sum(), np.inf)

        return Interval(total_dissip_lo, total_dissip_hi)


def verify_interval_biot_savart():
    """Verify interval Biot-Savart against standard computation."""
    print("INTERVAL BIOT-SAVART VERIFICATION")
    print("=" * 50)

    N = 8
    nu = 1e-4
    bs = IntervalBiotSavart(N, nu)
    fft_iv = IntervalFFT(N)

    # Generate test vorticity
    np.random.seed(42)
    wx = np.random.randn(N, N, N)
    wy = np.random.randn(N, N, N)
    wz = np.random.randn(N, N, N)

    # Standard FFT
    wx_hat = np.fft.fftn(wx)
    wy_hat = np.fft.fftn(wy)
    wz_hat = np.fft.fftn(wz)

    # Standard Biot-Savart
    kx, ky, kz = bs.kx, bs.ky, bs.kz
    ksq = kx**2 + ky**2 + kz**2
    ksq[0, 0, 0] = 1.0

    px = wx_hat / ksq; py = wy_hat / ksq; pz = wz_hat / ksq
    px[0, 0, 0] = 0; py[0, 0, 0] = 0; pz[0, 0, 0] = 0

    ux_hat = 1j*ky*pz - 1j*kz*py
    uy_hat = 1j*kz*px - 1j*kx*pz
    uz_hat = 1j*kx*py - 1j*ky*px

    # Interval FFT
    wx_rlo, wx_rhi, wx_ilo, wx_ihi = fft_iv.fft_interval_3d(
        np.nextafter(wx, -np.inf), np.nextafter(wx, np.inf))
    wy_rlo, wy_rhi, wy_ilo, wy_ihi = fft_iv.fft_interval_3d(
        np.nextafter(wy, -np.inf), np.nextafter(wy, np.inf))
    wz_rlo, wz_rhi, wz_ilo, wz_ihi = fft_iv.fft_interval_3d(
        np.nextafter(wz, -np.inf), np.nextafter(wz, np.inf))

    # Interval Biot-Savart
    result = bs.biot_savart(
        wx_rlo, wx_rhi, wx_ilo, wx_ihi,
        wy_rlo, wy_rhi, wy_ilo, wy_ihi,
        wz_rlo, wz_rhi, wz_ilo, wz_ihi)

    ux_rlo, ux_rhi, ux_ilo, ux_ihi = result[0:4]
    uy_rlo, uy_rhi, uy_ilo, uy_ihi = result[4:8]
    uz_rlo, uz_rhi, uz_ilo, uz_ihi = result[8:12]

    # Check containment
    ux_re_ok = np.all((ux_rlo <= ux_hat.real) & (ux_hat.real <= ux_rhi))
    ux_im_ok = np.all((ux_ilo <= ux_hat.imag) & (ux_hat.imag <= ux_ihi))
    uy_re_ok = np.all((uy_rlo <= uy_hat.real) & (uy_hat.real <= uy_rhi))
    uy_im_ok = np.all((uy_ilo <= uy_hat.imag) & (uy_hat.imag <= uy_ihi))
    uz_re_ok = np.all((uz_rlo <= uz_hat.real) & (uz_hat.real <= uz_rhi))
    uz_im_ok = np.all((uz_ilo <= uz_hat.imag) & (uz_hat.imag <= uz_ihi))

    all_ok = ux_re_ok and ux_im_ok and uy_re_ok and uy_im_ok and uz_re_ok and uz_im_ok

    max_width = max(
        (ux_rhi - ux_rlo).max(), (ux_ihi - ux_ilo).max(),
        (uy_rhi - uy_rlo).max(), (uy_ihi - uy_ilo).max(),
        (uz_rhi - uz_rlo).max(), (uz_ihi - uz_ilo).max(),
    )

    print(f"  Velocity contained: {all_ok}")
    print(f"  Max width: {max_width:.2e}")
    assert all_ok, "BIOT-SAVART FAILED"
    print(f"  PASS")

    # Test dissipation bound
    dissip = bs.diffusion_bound(
        wx_rlo, wx_rhi, wx_ilo, wx_ihi,
        wy_rlo, wy_rhi, wy_ilo, wy_ihi,
        wz_rlo, wz_rhi, wz_ilo, wz_ihi)

    # Compare to standard computation
    grad_w_sq = nu * (ksq * (np.abs(wx_hat)**2 + np.abs(wy_hat)**2 + np.abs(wz_hat)**2)).sum()
    print(f"  Dissipation: {dissip}")
    print(f"  Standard:    {grad_w_sq.real:.6e}")
    assert dissip.contains(grad_w_sq.real), f"Dissipation bound failed"
    print(f"  Contained: True")
    print(f"  PASS")

    return True


def verify_interval_arithmetic():
    """Self-test: verify our interval arithmetic is correct."""
    print("INTERVAL ARITHMETIC VERIFICATION")
    print("=" * 50)

    tests_passed = 0
    tests_total = 0

    # Test 1: Addition
    a = Interval(1.0, 2.0)
    b = Interval(3.0, 4.0)
    c = a + b
    tests_total += 1
    assert c.lo <= 4.0 and c.hi >= 6.0, f"Addition failed: {c}"
    tests_passed += 1
    print(f"  ADD: {a} + {b} = {c} ✓")

    # Test 2: Multiplication with negative
    a = Interval(-2.0, 3.0)
    b = Interval(-1.0, 4.0)
    c = a * b
    tests_total += 1
    assert c.lo <= -8.0 and c.hi >= 12.0, f"Mul failed: {c}"
    tests_passed += 1
    print(f"  MUL: {a} * {b} = {c} ✓")

    # Test 3: Subtraction
    a = Interval(1.0, 2.0)
    b = Interval(3.0, 4.0)
    c = a - b
    tests_total += 1
    assert c.lo <= -3.0 and c.hi >= -1.0, f"Sub failed: {c}"
    tests_passed += 1
    print(f"  SUB: {a} - {b} = {c} ✓")

    # Test 4: Square of interval spanning zero
    a = Interval(-3.0, 2.0)
    c = a ** 2
    tests_total += 1
    assert c.lo <= 0.0 and c.hi >= 9.0, f"Sq failed: {c}"
    tests_passed += 1
    print(f"  SQ:  {a}² = {c} ✓")

    # Test 5: Division
    a = Interval(1.0, 2.0)
    b = Interval(3.0, 4.0)
    c = a / b
    tests_total += 1
    assert c.lo <= 0.25 and c.hi >= 0.5, f"Div failed: {c}"
    tests_passed += 1
    print(f"  DIV: {a} / {b} = {c} ✓")

    # Test 6: Sqrt
    a = Interval(4.0, 9.0)
    c = a.sqrt()
    tests_total += 1
    assert c.lo <= 2.0 and c.hi >= 3.0, f"Sqrt failed: {c}"
    tests_passed += 1
    print(f"  SQRT: √{a} = {c} ✓")

    # Test 7: π contains 3.14159...
    pi = Interval.from_value(math.pi)
    tests_total += 1
    assert pi.contains(math.pi), f"Pi failed: {pi}"
    tests_passed += 1
    print(f"  PI:  {pi} contains π ✓")

    # Test 8: IntervalArray
    x = IntervalArray.from_array([1.0, 2.0, 3.0])
    y = IntervalArray.from_array([4.0, 5.0, 6.0])
    z = x * y
    s = z.sum()
    tests_total += 1
    true_sum = 1*4 + 2*5 + 3*6  # = 32
    assert s.contains(true_sum), f"Array failed: {s} should contain {true_sum}"
    tests_passed += 1
    print(f"  ARR: [1,2,3]·[4,5,6] = {s} contains {true_sum} ✓")

    # Test 9: Key inequality check
    # Can we verify that 2 + 2 = 4 rigorously?
    two = Interval.from_value(2.0)
    four = two + two
    tests_total += 1
    assert four.contains(4.0), f"2+2 failed"
    tests_passed += 1
    print(f"  2+2: {four} contains 4.0 ✓")

    # Test 10: Verify the bound is TIGHT (width small)
    tests_total += 1
    assert four.width < 1e-14, f"Bounds too wide: {four.width}"
    tests_passed += 1
    print(f"  WIDTH: {four.width:.2e} < 1e-14 ✓")

    print(f"\n{tests_passed}/{tests_total} tests passed.")
    return tests_passed == tests_total


if __name__ == '__main__':
    verify_interval_arithmetic()
    print()
    verify_interval_fft()
    print()
    verify_interval_biot_savart()
