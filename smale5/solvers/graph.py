"""Components of degree 1 in one variable: graphs y = −B(x)/A(x).

The simplest genus-0 stratum beyond conics, and the first where the
single-exponential decision is fully rigorous by elementary means (Runge's
method in miniature): an integer point needs A(x) | B(x), hence
A(x) | R̂(x) where ℓ·B = Q̂·A + R̂ is integer pseudo-division with
deg R̂ < deg A. So either R̂(x) = 0 (finitely many integer roots) or
|A(x)| ≤ |R̂(x)|, which confines x to an explicit window of size 2^(O(s)).
Everything outside the window is a proof of NO.
"""
from __future__ import annotations

import math

import sympy as sp

from ..decision import Decision, Status, no, undecided, yes
from ..poly import X, Y, is_solution

_WINDOW_CAP = 10**7


def solve_graph(gpoly) -> Decision | None:
    """Decide components with degree exactly 1 in x or in y (total degree ≥ 3;
    lower degrees have complete solvers already). None if not applicable."""
    for main, other, swap in ((Y, X, False), (X, Y, True)):
        if gpoly.degree(main) == 1:
            return _solve(gpoly, main, other, swap)
    return None


def _mk(x0: int, y0: int, swap: bool):
    return (y0, x0) if swap else (x0, y0)


def _solve(g, main, other, swap) -> Decision:
    p = sp.Poly(g.as_expr(), main)
    A_expr, B_expr = p.all_coeffs()
    A = sp.Poly(A_expr, other)
    B = sp.Poly(B_expr, other)

    # A(r) = B(r) = 0 for an integer r: a whole line of solutions.
    common = sp.Poly(sp.gcd(A.as_expr(), B.as_expr()), other)
    if common.total_degree() >= 1:
        for r in common.ground_roots():
            if r.is_integer:
                w = _mk(int(r), 0, swap)
                assert is_solution(g, w)
                return yes("graph-common-root", w,
                           f"A and B vanish at {int(r)}: a line of solutions")

    if A.total_degree() == 0:
        a = int(A.coeffs()[0])
        for x0 in range(abs(a)):
            bv = int(B.eval(x0))
            if bv % a == 0:
                w = _mk(x0, -(bv // a), swap)
                assert is_solution(g, w)
                return yes("graph-congruence", w, f"x ≡ {x0} (mod {abs(a)})")
        return no("graph-congruence", {"modulus": abs(a)},
                  "B(x) ≢ 0 (mod a) for every residue class")

    Aq = sp.Poly(A.as_expr(), other, domain="QQ")
    Bq = sp.Poly(B.as_expr(), other, domain="QQ")
    q, r = sp.div(Bq, Aq)
    denoms = [sp.Rational(c).q for c in (list(q.coeffs()) + list(r.coeffs()))]
    ell = math.lcm(*denoms) if denoms else 1
    Qh = sp.Poly((q * ell).as_expr(), other)
    Rh = sp.Poly((r * ell).as_expr(), other)

    if Rh.is_zero:
        # ℓ·B = Q̂·A exactly: y = −Q̂(x)/ℓ, integer iff ℓ | Q̂(x).
        for x0 in range(ell):
            qv = int(Qh.eval(x0))
            if qv % ell == 0:
                w = _mk(x0, -(qv // ell), swap)
                assert is_solution(g, w)
                return yes("graph-exact-division", w,
                           f"x ≡ {x0} (mod {ell}): infinite solution family")
        return no("graph-exact-division", {"modulus": ell},
                  "Q̂(x) ≢ 0 (mod ℓ) for every residue class")

    candidates = set()
    for r0 in Rh.ground_roots():
        if r0.is_integer:
            candidates.add(int(r0))
    a_coeffs = [abs(int(c)) for c in A.all_coeffs()]
    r_coeffs = [abs(int(c)) for c in Rh.all_coeffs()]
    window = 2 + (sum(a_coeffs[1:]) + sum(r_coeffs)) // a_coeffs[0]
    if window > _WINDOW_CAP:
        return undecided("graph-window", bound=_WINDOW_CAP,
                         detail=f"crossover window {window} exceeds cap")
    candidates.update(range(-window, window + 1))
    for x0 in sorted(candidates, key=abs):
        av, bv = int(A.eval(x0)), int(B.eval(x0))
        if av == 0:
            continue  # B(x0) ≠ 0 here (common roots handled above)
        if bv % av == 0:
            w = _mk(x0, -(bv // av), swap)
            assert is_solution(g, w)
            return yes("graph-window", w)
    return no("graph-window", {"window": window},
              f"A(x) | B(x) forces R̂(x) = 0 or |x| < {window}; all candidates fail")
