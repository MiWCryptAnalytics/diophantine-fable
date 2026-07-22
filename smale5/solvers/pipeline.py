"""The decision pipeline: cheap certificates first, then per-component
structure, with UNDECIDED as the honest terminal state.

Soundness contract: a YES witness satisfies f (verified); a NO is returned
only when every irreducible component carries its own NO certificate (a
solution of f is a solution of some component, and conversely)."""
from __future__ import annotations

import sympy as sp

from ..budget import scaled
from ..classify import components, thue_shape
from ..decision import Decision, Status, no, undecided, yes
from ..poly import X, Y, is_solution, normalize, parse, size
from . import deg2fiber, graph, local, linear, quadratic, search, thue_pari


def decide(f, search_bound: int = 2000) -> Decision:
    poly = parse(f) if isinstance(f, str) else normalize(f)
    if poly.is_zero:
        return yes("zero-polynomial", (0, 0), "f ≡ 0: every point is a solution")
    if poly.total_degree() == 0:
        return no("nonzero-constant", int(poly.coeffs()[0]))

    quick = search.bounded_search(poly, 25)
    if quick.status is Status.YES:
        return quick
    for obstruction in (local.real_obstruction(poly), local.local_obstruction(poly)):
        if obstruction is not None:
            return obstruction

    caps = scaled(size(poly))
    per_component = []
    for g in components(poly):
        dec = _solve_component(g, search_bound, caps)
        if dec.status is Status.YES:
            assert is_solution(poly, dec.certificate) if isinstance(dec.certificate, tuple) else True
            return dec
        per_component.append((g, dec))

    if all(dec.status is Status.NO for _, dec in per_component):
        if len(per_component) == 1:
            return per_component[0][1]
        return no("components",
                  [(str(g.as_expr()), dec.method) for g, dec in per_component],
                  "every irreducible component has a NO certificate")
    summary = "; ".join(f"{g.as_expr()}: {dec.status.value}[{dec.method}]"
                        for g, dec in per_component)
    return undecided("pipeline", bound=search_bound, detail=summary)


def _solve_component(g: sp.Poly, H: int, caps) -> Decision:
    if g.degree(Y) == 0:
        return _univariate(g, X)
    if g.degree(X) == 0:
        return _univariate(g, Y)
    d = g.total_degree()
    if d == 1:
        return linear.solve_linear(g)
    if d == 2:
        return quadratic.solve_quadratic(g, caps=caps)
    if g.degree(Y) == 1 or g.degree(X) == 1:
        dec = graph.solve_graph(g)
        if dec is not None:
            return dec
    if g.degree(Y) == 2 or g.degree(X) == 2:
        dec = deg2fiber.solve_deg2_fiber(g, caps=caps)
        if dec is not None:
            return dec
        dec = deg2fiber.solve_pure_square_fiber(g, caps=caps)
        if dec is not None:
            return dec
    ts = thue_shape(g)
    if ts is not None:
        F, m = ts
        _, factors = F.factor_list()
        if m != 0 and len(factors) == 1 and factors[0][1] == 1:
            dec = thue_pari.solve_thue(F, m, g)
            if dec is not None:
                return dec
    obstruction = local.local_obstruction(g)
    if obstruction is not None:
        return obstruction
    return search.bounded_search(g, H)


def _univariate(g: sp.Poly, var) -> Decision:
    """Component depending on one variable: lines. ground_roots finds ALL
    rational roots (complete by the rational root theorem)."""
    p = sp.Poly(g.as_expr(), var)
    for r in p.ground_roots():
        if r.is_integer:
            w = (int(r), 0) if var is X else (0, int(r))
            assert is_solution(g, w)
            return yes("univariate-lines", w, f"{var} = {int(r)} is a line of solutions")
    return no("univariate-lines", detail="no integer root (rational root theorem)")
