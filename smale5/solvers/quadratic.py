"""Complete decision layer for degree-2 equations
a·x² + b·xy + c·y² + d·x + e·y + g₀ = 0 — the fully classical stratum of
Smale #5. Every branch either decides with a re-checkable certificate or
returns UNDECIDED with the exhausted cap; the indefinite nonsquare branch
decides via the Pell orbit walk and never enumerates integer points.

All branches lean on one identity (a ≠ 0):
    4a·f = (2ax + by + d)² − Δ·y² + β·y + γ,
    Δ = b² − 4ac,  β = 4ae − 2bd,  γ = 4ag₀ − d².
"""
from __future__ import annotations

import sympy as sp

from ..decision import Decision, Status, no, undecided, yes
from ..poly import X, Y, coeff_dict, is_solution
from .linear import solve_linear_coeffs
from .pell import OrbitCongruence, decide_pell_like, is_square

_DIVISOR_CAP = 10**15
_ENUM_CAP = 2_000_000


def solve_quadratic(gpoly) -> Decision:
    dec = _solve(coeff_dict(gpoly))
    if dec.status is Status.YES and isinstance(dec.certificate, tuple):
        assert is_solution(gpoly, dec.certificate), (gpoly, dec)
    return dec


def _solve(terms) -> Decision:
    a = terms.get((2, 0), 0); b = terms.get((1, 1), 0); c = terms.get((0, 2), 0)
    d = terms.get((1, 0), 0); e = terms.get((0, 1), 0); g0 = terms.get((0, 0), 0)
    if a == 0 and c == 0:
        if b == 0:
            raise ValueError("quadratic part vanishes; route to the linear solver")
        return _rect_hyperbola(b, d, e, g0)
    if a == 0:
        dec = _solve({(j, i): v for (i, j), v in terms.items()})
        if dec.status is Status.YES and isinstance(dec.certificate, tuple):
            xv, yv = dec.certificate
            return Decision(dec.status, dec.method, (yv, xv), dec.detail + " (x↔y)")
        return dec
    delta = b * b - 4 * a * c
    if delta == 0:
        return _parabola(a, b, d, e, g0)
    if delta < 0:
        return _ellipse(a, b, d, e, g0, delta)
    k = int(sp.integer_nthroot(delta, 2)[0])
    if k * k == delta:
        return _split_hyperbola(a, b, c, d, e, g0, k)
    return _pell_conic(a, b, d, e, g0, delta)


def _rect_hyperbola(b: int, d: int, e: int, g0: int) -> Decision:
    """b·xy + d·x + e·y + g₀ = 0  ⟺  (bx+e)(by+d) = ed − b·g₀."""
    W = e * d - b * g0
    if W == 0:
        if (-e) % b == 0:
            return yes("hyperbola-degenerate", ((-e) // b, 0), "bx+e = 0 line")
        if (-d) % b == 0:
            return yes("hyperbola-degenerate", (0, (-d) // b), "by+d = 0 line")
        return no("hyperbola-degenerate",
                  detail=f"(bx+e)(by+d) = 0 requires {b} | {e} or {b} | {d}")
    if abs(W) > _DIVISOR_CAP:
        return undecided("hyperbola-divisors", bound=_DIVISOR_CAP,
                         detail=f"|W| = {abs(W)} too large to factor")
    for p0 in sp.divisors(abs(W)):
        for p in (p0, -p0):
            q = W // p
            if (p - e) % b == 0 and (q - d) % b == 0:
                return yes("hyperbola-divisors", ((p - e) // b, (q - d) // b),
                           f"divisor pair {p}·{q} = {W}")
    return no("hyperbola-divisors", {"W": W},
              "all divisor pairs of W checked; none lift to integers")


def _parabola(a: int, b: int, d: int, e: int, g0: int) -> Decision:
    """Δ = 0: (2ax + by + d)² + β·y + γ = 0."""
    beta = 4 * a * e - 2 * b * d
    gamma = 4 * a * g0 - d * d
    if beta == 0:
        rhs = -gamma
        if rhs < 0 or not is_square(rhs):
            return no("parabola-square", {"rhs": rhs},
                      "(2ax+by+d)² = −γ has no integer square root")
        X0 = int(sp.integer_nthroot(rhs, 2)[0])
        for Xv in sorted({X0, -X0}):
            dec = solve_linear_coeffs(2 * a, b, d - Xv)
            if dec.status is Status.YES:
                return yes("parabola-square", dec.certificate,
                           f"2ax+by+d = {Xv}")
        return no("parabola-square", detail="neither sign of the root lifts (Bézout)")
    # X = 2ax+by+d must satisfy: β | X²+γ  and  2a | X − b·y − d with
    # y = −(X²+γ)/β. Both depend only on X mod M = |2aβ|.
    M = abs(2 * a * beta)
    if M > _ENUM_CAP:
        return undecided("parabola-congruence", bound=_ENUM_CAP,
                         detail=f"residue modulus {M} exceeds cap")
    for r in range(M):
        if (r * r + gamma) % beta:
            continue
        yv = -((r * r + gamma) // beta)
        num = r - b * yv - d
        if num % (2 * a):
            continue
        return yes("parabola-congruence", (num // (2 * a), yv),
                   f"admissible class X ≡ {r} (mod {M})")
    return no("parabola-congruence", {"modulus": M},
              "no residue class for X = 2ax+by+d is admissible")


def _ellipse(a: int, b: int, d: int, e: int, g0: int, delta: int) -> Decision:
    """Δ < 0: (2ax+by+d)² + (−Δ)y² + βy + γ = 0 confines y to a finite window."""
    A2 = -delta
    beta = 4 * a * e - 2 * b * d
    gamma = 4 * a * g0 - d * d
    disc0 = beta * beta - 4 * A2 * gamma
    if disc0 < 0:
        return no("ellipse-empty", detail="(−Δ)y² + βy + γ > 0 for all real y")
    s = int(sp.integer_nthroot(disc0, 2)[0])
    ylo = (-beta - s - 1) // (2 * A2)          # floor, deliberately widened
    yhi = -((-(-beta + s + 1)) // (2 * A2))    # ceil,  deliberately widened
    if yhi - ylo > _ENUM_CAP:
        return undecided("ellipse-scan", bound=_ENUM_CAP,
                         detail=f"y-window width {yhi - ylo} exceeds cap")
    for yv in range(ylo, yhi + 1):
        rhs = -(A2 * yv * yv + beta * yv + gamma)
        if rhs < 0 or not is_square(rhs):
            continue
        X0 = int(sp.integer_nthroot(rhs, 2)[0])
        for Xv in sorted({X0, -X0}):
            num = Xv - b * yv - d
            if num % (2 * a) == 0:
                return yes("ellipse-scan", (num // (2 * a), yv))
    return no("ellipse-scan", {"window": (ylo, yhi)},
              f"complete scan of y ∈ [{ylo}, {yhi}]")


def _split_hyperbola(a, b, c, d, e, g0, k) -> Decision:
    """Δ = k² > 0: 4ak²·f + W = Λ₁·Λ₂ with integer linear forms
    Λ₁ = 2akx + k(b+k)y + ks,  Λ₂ = 2akx + k(b−k)y + kr."""
    ks = d * (b + k) - 2 * a * e
    kr = 2 * a * e - d * (b - k)
    W = ks * kr - 4 * a * g0 * k * k
    f_expr = a*X**2 + b*X*Y + c*Y**2 + d*X + e*Y + g0
    L1e = 2*a*k*X + k*(b + k)*Y + ks
    L2e = 2*a*k*X + k*(b - k)*Y + kr
    if sp.expand(L1e * L2e - 4*a*k*k*f_expr - W) != 0:  # defensive identity check
        return undecided("split-hyperbola", detail="internal identity check failed")
    if W == 0:
        for (A, B, C) in ((2*a*k, k*(b + k), ks), (2*a*k, k*(b - k), kr)):
            dec = solve_linear_coeffs(A, B, C)
            if dec.status is Status.YES:
                return yes("split-hyperbola", dec.certificate, "one factor line has integer points")
        return no("split-hyperbola", detail="neither factor line has integer points (Bézout)")
    if abs(W) > _DIVISOR_CAP:
        return undecided("split-hyperbola", bound=_DIVISOR_CAP,
                         detail=f"|W| = {abs(W)} too large to factor")
    for p0 in sp.divisors(abs(W)):
        for p in (p0, -p0):
            q = W // p
            ynum = p - q - (ks - kr)
            if ynum % (2 * k * k):
                continue
            yv = ynum // (2 * k * k)
            xnum = p - k * (b + k) * yv - ks
            if xnum % (2 * a * k):
                continue
            return yes("split-hyperbola", (xnum // (2 * a * k), yv),
                       f"divisor pair {p}·{q} = {W}")
    return no("split-hyperbola", {"W": W}, "all divisor pairs of W checked")


def _pell_conic(a, b, d, e, g0, delta) -> Decision:
    """Δ > 0 nonsquare: with X = 2ax+by+d, P = Δy + (bd−2ae):
    P² − Δ·X² = N = (bd−2ae)² − Δ(d²−4a·g₀). Recovery of (x,y) is a pair of
    congruences on (P, X) mod M = |2aΔ|, decided by the Pell orbit walk."""
    r1 = b * d - 2 * a * e
    N = r1 * r1 - delta * (d * d - 4 * a * g0)
    M = abs(2 * a * delta)

    def accept(Pm: int, Qm: int) -> bool:
        if (Pm - r1) % delta:
            return False
        yv = (Pm - r1) // delta
        return (Qm - b * yv - d) % (2 * a) == 0

    def recover(P: int, Q: int):
        if (P - r1) % delta:
            return None
        yv = (P - r1) // delta
        num = Q - b * yv - d
        if num % (2 * a):
            return None
        return (num // (2 * a), yv)

    return decide_pell_like(delta, N, cong=OrbitCongruence(M, accept),
                            recover=recover)
