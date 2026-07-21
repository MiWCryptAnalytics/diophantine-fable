"""Components a·y² + B(x)·y + C(x) with CONSTANT leading coefficient whose
discriminant D = B² − 4aC has square-class of degree ≤ 2.

Complete the square: (2ay + B(x))² = D(x) = E(x)²·Q₀(x) with Q₀ the
discriminant modulo squares. Away from the integer roots of E, an integer
point forces w = (2ay + B)/E to be an integer with w² = Q₀(x) — a CONIC —
plus the divisibility 2a | E(x)·w − B(x), which is a fixed-modulus congruence
because a is constant. So the whole stratum rides the quadratic layer's
ExtraCong machinery, Pell orbit walk included: the panel's counterexample
family y² = 2x⁴ + x² is now *decided*, not merely correctly classified.
Degree of Q₀ ≥ 3 (genus ≥ 1: Mordell &c.) is honestly out of scope: None.
"""
from __future__ import annotations

import sympy as sp

from ..budget import DEFAULT, Caps
from ..decision import Decision, Status, no, undecided, yes
from ..poly import X, Y, is_solution
from .pell import is_square
from .quadratic import ExtraCong, solve_quadratic

_CONST_FACTOR_CAP = 10**15


def solve_deg2_fiber(gpoly, caps: Caps = DEFAULT) -> Decision | None:
    """None when the component is not in this stratum (non-constant leading
    coefficient, square-class degree ≥ 3, or an oversized constant factor)."""
    for main, other, swap in ((Y, X, False), (X, Y, True)):
        if gpoly.degree(main) == 2:
            p = sp.Poly(gpoly.as_expr(), main)
            lead = sp.Poly(p.all_coeffs()[0], other)
            if lead.total_degree() == 0:
                return _solve(gpoly, p, other, swap, caps)
    return None


def _witness(g, xv: int, yv: int, swap: bool):
    w = (yv, xv) if swap else (xv, yv)
    assert is_solution(g, w), (g, w)
    return w


def _solve(g, p, other, swap, caps) -> Decision | None:
    a_lead, B_expr, C_expr = p.all_coeffs()
    a = int(a_lead)
    Bp = sp.Poly(B_expr, other)
    Cp = sp.Poly(C_expr, other)
    m2a = abs(2 * a)
    D = sp.Poly(sp.expand(Bp.as_expr() ** 2 - 4 * a * Cp.as_expr()), other)

    if D.is_zero:
        # 4a·g = (2ay + B(x))²: solutions are exactly 2a | B(x).
        for xr in range(m2a):
            bv = int(Bp.eval(xr))
            if bv % (2 * a) == 0:
                return yes("deg2fiber-double-root",
                           _witness(g, xr, -(bv // (2 * a)), swap),
                           f"x ≡ {xr} (mod {m2a}): a line's worth of solutions")
        return no("deg2fiber-double-root", {"modulus": m2a},
                  "B(x) ≢ 0 (mod 2a) for every residue class")

    split = _square_class(D, other)
    if split is None:
        return None
    Ep, Q0p = split
    if Q0p.total_degree() > 2:
        return None  # genus ≥ 1 fiber: not this stratum

    # E(r) = 0 forces (2ay + B(r))² = 0: solutions off the conic route.
    for r in Ep.ground_roots() if Ep.total_degree() >= 1 else []:
        if r.is_integer:
            rv = int(r)
            bv = int(Bp.eval(rv))
            if bv % (2 * a) == 0:
                return yes("deg2fiber-E-root",
                           _witness(g, rv, -(bv // (2 * a)), swap),
                           f"E({rv}) = 0 and 2a | B({rv})")

    if Q0p.total_degree() == 0:
        q = int(Q0p.coeffs()[0])
        if q <= 0 or not is_square(q):
            return no("deg2fiber-nonsquare-class", {"Q0": q},
                      "T² = E(x)²·Q₀ needs E(x) = 0 (integer roots exhausted) "
                      "since Q₀ is not a positive square")
        w0 = int(sp.integer_nthroot(q, 2)[0])
        for sign in (1, -1):
            for xr in range(m2a):
                num = sign * int(Ep.eval(xr)) * w0 - int(Bp.eval(xr))
                if num % (2 * a) == 0:
                    return yes("deg2fiber-constant-class",
                               _witness(g, xr, num // (2 * a), swap),
                               f"2ay = ±E(x)·{w0} − B(x) at x ≡ {xr} (mod {m2a})")
        return no("deg2fiber-constant-class", {"modulus": m2a},
                  "neither sign branch admits a residue class")

    conic = sp.Poly(sp.expand(Y**2 - Q0p.as_expr().subs(other, X)), X, Y)

    def accept(xr: int, wr: int) -> bool:
        return (int(Ep.eval(xr)) * wr - int(Bp.eval(xr))) % (2 * a) == 0

    dec = solve_quadratic(conic, extra=ExtraCong(m2a, accept), caps=caps)
    if dec.status is Status.YES and isinstance(dec.certificate, tuple):
        xv, wv = dec.certificate
        num = int(Ep.eval(xv)) * wv - int(Bp.eval(xv))
        assert num % (2 * a) == 0
        return yes("deg2fiber", _witness(g, xv, num // (2 * a), swap),
                   f"conic point via [{dec.method}]")
    if dec.status is Status.YES:
        return yes("deg2fiber-orbit-certificate", dec.certificate,
                   "conic solvable with the divisibility congruence; witness "
                   "not materialized — " + dec.detail)
    if dec.status is Status.NO:
        return no("deg2fiber", dec.certificate,
                  "conic-with-congruence complete "
                  f"[{dec.method}] and E-root scan exhausted")
    return undecided("deg2fiber", dec.certificate, dec.detail)


def _square_class(D: sp.Poly, other):
    """D = E² · Q₀ with Q₀ = the square class (odd-multiplicity part times the
    squarefree part of the constant). None if the constant is too big to
    factor — callers must fall through, never guess."""
    try:
        c0, factors = D.sqf_list()
    except Exception:
        return None
    c0 = int(c0)
    if abs(c0) > _CONST_FACTOR_CAP:
        return None
    f0, s0 = 1, (1 if c0 > 0 else -1)
    for prime, e in sp.factorint(abs(c0)).items():
        f0 *= prime ** (e // 2)
        if e % 2:
            s0 *= prime
    E_expr, Q_expr = sp.Integer(f0), sp.Integer(s0)
    for fac, mult in factors:
        E_expr *= fac.as_expr() ** (mult // 2)
        if mult % 2:
            Q_expr *= fac.as_expr()
    Ep = sp.Poly(sp.expand(E_expr), other)
    Q0p = sp.Poly(sp.expand(Q_expr), other)
    assert sp.expand(Ep.as_expr() ** 2 * Q0p.as_expr() - D.as_expr()) == 0
    return Ep, Q0p
