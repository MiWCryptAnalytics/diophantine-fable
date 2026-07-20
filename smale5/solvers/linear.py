"""a·x + b·y + c = 0: solvable over ℤ iff gcd(a,b) | c (Bézout)."""
from __future__ import annotations

import math

from ..decision import Decision, no, yes
from ..poly import coeff_dict, is_solution


def _ext_gcd(a: int, b: int):
    """(g, s, t) with a·s + b·t = g = gcd(a,b) ≥ 0."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    if old_r < 0:
        old_r, old_s, old_t = -old_r, -old_s, -old_t
    return old_r, old_s, old_t


def solve_linear_coeffs(a: int, b: int, c: int) -> Decision:
    if a == 0 and b == 0:
        if c == 0:
            return yes("linear-trivial", (0, 0), "0 = 0")
        return no("linear-trivial", c, f"{c} ≠ 0")
    g = math.gcd(a, b)
    if (-c) % g:
        return no("linear-gcd", {"gcd": g},
                  f"gcd({a},{b}) = {g} does not divide {-c}")
    g2, s, t = _ext_gcd(a, b)
    assert g2 == g
    k = (-c) // g
    witness = (int(s) * k, int(t) * k)
    assert a * witness[0] + b * witness[1] + c == 0
    return yes("linear-gcd", witness)


def solve_linear(poly) -> Decision:
    terms = coeff_dict(poly)
    dec = solve_linear_coeffs(terms.get((1, 0), 0), terms.get((0, 1), 0),
                              terms.get((0, 0), 0))
    if dec.status.value == "YES":
        assert is_solution(poly, dec.certificate)
    return dec
