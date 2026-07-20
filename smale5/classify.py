"""Siegel classification of the irreducible components of f(x,y) = 0.

Labels are ROUTING metadata, not decisions:

- "infinite-candidate": the necessary conditions of Siegel's theorem for
  infinitely many integral points hold (genus 0, ≤ 2 visible points at
  infinity). It does NOT assert that infinitely many — or any — exist.
- "finite": certified finiteness of integral points. Claimed only when the
  geometric genus is certified ≥ 1, or genus 0 with ≥ 3 points at infinity
  that are all smooth (so visible points = places on the normalization and
  Siegel's theorem applies).
- "unknown": we could not certify a genus. Honesty over coverage.

Caveat recorded once here: when the curve is singular at infinity, a visible
point can split into several places on the normalization, so a small visible
count does not bound the place count. That can only turn a true "finite" into
"infinite-candidate"/"unknown" — never the unsound direction.
"""
from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from .poly import X, Y

_T = sp.Symbol("t_")


@dataclass
class Component:
    poly: sp.Poly
    kind: str                       # "curve" | "vertical-lines" | "horizontal-lines"
    degree: int
    genus: int | None               # geometric genus when certified, else None
    points_at_infinity: int | None  # distinct points of the projective closure on Z=0
    smooth_at_infinity: bool | None
    siegel: str                     # "infinite-candidate" | "finite" | "unknown" | "lines"


def components(f: sp.Poly) -> list[sp.Poly]:
    """Irreducible factors over ℚ (zero set of f = union of their zero sets)."""
    _, factors = f.factor_list()
    return [sp.Poly(fac.as_expr(), X, Y) for fac, _ in factors]


def classify(f: sp.Poly) -> list[Component]:
    return [classify_component(g) for g in components(f)]


def classify_component(g: sp.Poly) -> Component:
    d = g.total_degree()
    if g.degree(Y) == 0:
        return Component(g, "vertical-lines", d, None, None, None, "lines")
    if g.degree(X) == 0:
        return Component(g, "horizontal-lines", d, None, None, None, "lines")

    pts_inf, smooth_inf = _points_at_infinity(g)
    genus = _certified_genus(g)

    if genus is not None and genus >= 1:
        siegel = "finite"
    elif genus == 0 and pts_inf >= 3 and smooth_inf:
        siegel = "finite"
    elif genus == 0 and pts_inf <= 2:
        siegel = "infinite-candidate"
    else:
        siegel = "unknown"
    return Component(g, "curve", d, genus, pts_inf, smooth_inf, siegel)


def _points_at_infinity(g: sp.Poly):
    """Distinct points of the projective closure on the line at infinity.

    Roots of the leading form LF(X,Y) in P¹(ℚ̄): the distinct roots of
    LF(t,1), plus [1:0] when deg LF(t,1) < deg LF.
    """
    d = g.total_degree()
    lf = sum(int(a) * X**i * Y**j for (i, j), a in g.terms() if i + j == d)
    pt = sp.Poly(sp.expand(lf.subs({X: _T, Y: 1})), _T)
    if pt.is_zero:  # cannot happen for g of degree d, kept for safety
        return None, None
    degp = pt.total_degree()
    distinct = 0 if degp == 0 else sp.degree(sp.sqf_part(pt.as_expr()), gen=_T)
    extra = 1 if degp < d else 0
    count = int(distinct) + extra
    # LF squarefree as a binary form ⟺ pt squarefree and the [1:0] root simple.
    smooth = (int(distinct) == degp) and (d - degp) <= 1
    return count, smooth


def _certified_genus(g: sp.Poly) -> int | None:
    d = g.total_degree()
    if d <= 2:
        return 0
    for main, other in ((Y, X), (X, Y)):
        if g.degree(main) == 2:
            genus = _genus_deg2_fiber(g, main, other)
            if genus is not None:
                return genus
    thue = thue_shape(g)
    if thue is not None:
        F, m = thue
        if m != 0 and _binary_form_squarefree(F):
            # No affine singular points (Euler: dF = xFx + yFy, so Fx=Fy=0 on
            # F=m forces m=0) and squarefree LF keeps infinity smooth: the
            # projective closure is a smooth plane curve.
            return (d - 1) * (d - 2) // 2
    if d <= 6:
        smooth = _is_smooth_projective(g)
        if smooth:
            return (d - 1) * (d - 2) // 2
    return None


def _genus_deg2_fiber(g: sp.Poly, main, other) -> int | None:
    """g quadratic in `main`: birational to w² = disc(other); genus from its
    squarefree part (multiplying by squares does not change ℚ(x,√D))."""
    p = sp.Poly(g.as_expr(), main)
    coeffs = p.all_coeffs()
    if len(coeffs) != 3:
        return None
    A, B, C = coeffs
    D = sp.expand(B**2 - 4 * A * C)
    if D == 0:
        return None
    sf = sp.sqf_part(D)
    m = sp.degree(sf, gen=other)
    if m is sp.S.NegativeInfinity or m <= 2:
        return 0
    return (int(m) - 1) // 2


def thue_shape(g: sp.Poly):
    """Return (F, m) when g = F(x,y) − m with F homogeneous of degree ≥ 3."""
    d = g.total_degree()
    if d < 3:
        return None
    m = 0
    for (i, j), a in g.terms():
        if i + j == d:
            continue
        if i == j == 0:
            m = -int(a)
        else:
            return None
    F = sp.Poly(sum(int(a) * X**i * Y**j for (i, j), a in g.terms() if i + j == d), X, Y)
    return F, m


def _binary_form_squarefree(F: sp.Poly) -> bool:
    d = F.total_degree()
    pt = sp.Poly(sp.expand(F.as_expr().subs({X: _T, Y: 1})), _T)
    degp = 0 if pt.is_zero else pt.total_degree()
    distinct = 0 if degp == 0 else int(sp.degree(sp.sqf_part(pt.as_expr()), gen=_T))
    return distinct == degp and (d - degp) <= 1


def _is_smooth_projective(g: sp.Poly) -> bool | None:
    """Smoothness of the projective closure: the ideal (F_X, F_Y, F_Z) has no
    projective zeros ⟺ its only affine zero is the origin ⟺ zero-dimensional
    (a homogeneous variety is a cone: finite ⟹ {0})."""
    Xh, Yh, Zh = sp.symbols("Xh_ Yh_ Zh_")
    d = g.total_degree()
    F = sum(int(a) * Xh**i * Yh**j * Zh**(d - i - j) for (i, j), a in g.terms())
    try:
        G = sp.groebner([sp.diff(F, v) for v in (Xh, Yh, Zh)], Xh, Yh, Zh,
                        order="grevlex")
        return bool(G.is_zero_dimensional)
    except Exception:
        return None
