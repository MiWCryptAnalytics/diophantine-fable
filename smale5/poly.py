"""f ∈ ℤ[u,v]: parsing, normalization, and Smale's size measure s(f)."""
from __future__ import annotations

import math

import sympy as sp

X, Y = sp.symbols("x y")

_ALLOWED_CHARS = set("0123456789+-*/^() \t\nxyuv")


def parse(text: str) -> sp.Poly:
    """Parse a polynomial in x,y (u,v accepted as synonyms) into ℤ[x,y].

    The zero set in ℤ² is invariant under clearing rational denominators and
    dividing by integer content, so the result is always primitive with
    integer coefficients.
    """
    bad = set(text) - _ALLOWED_CHARS
    if bad:
        raise ValueError(f"disallowed characters in polynomial: {sorted(bad)!r}")
    expr = sp.sympify(text.replace("^", "**"),
                      locals={"x": X, "y": Y, "u": X, "v": Y}, rational=True)
    return normalize(expr)


def normalize(expr) -> sp.Poly:
    """Expand, clear denominators, and strip integer content. Zero set unchanged."""
    if isinstance(expr, sp.Poly):
        expr = expr.as_expr()
    poly = sp.Poly(sp.expand(sp.together(sp.sympify(expr))), X, Y)
    if poly.is_zero:
        return poly
    coeffs = [sp.Rational(c) for c in poly.coeffs()]
    if not all(c.is_rational for c in coeffs):
        raise ValueError("coefficients must be rational so f can be scaled into ℤ[u,v]")
    denom = math.lcm(*(int(c.q) for c in coeffs))
    poly = sp.Poly(sp.expand(poly.as_expr() * denom), X, Y)
    _content, poly = poly.primitive()
    return poly


def size(poly: sp.Poly) -> int:
    """Smale-style input size: total degree + Σ (1 + bitlength|a|) over coefficients."""
    if poly.is_zero:
        return 1
    bits = sum(1 + abs(int(c)).bit_length() for c in poly.coeffs())
    return poly.total_degree() + bits


def coeff_dict(poly: sp.Poly) -> dict[tuple[int, int], int]:
    return {(i, j): int(c) for (i, j), c in poly.terms()}


def evaluate(poly: sp.Poly, x0: int, y0: int) -> int:
    total = 0
    for (i, j), a in poly.terms():
        total += int(a) * x0**i * y0**j
    return total


def is_solution(poly: sp.Poly, witness) -> bool:
    x0, y0 = witness
    return evaluate(poly, int(x0), int(y0)) == 0
