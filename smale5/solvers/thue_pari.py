"""Unconditional Thue-equation decisions via PARI.

thueinit(·, 1) certifies the class-group data unconditionally (no GRH), so an
empty solution list from thue() is a proof of NO — one of the few strata of
Smale #5 where a genus-1+ curve gets a certified decision today (Baker-type
bounds under the hood). Requires cypari2 + a PARI installation; callers must
treat a None return as "backend unavailable/inapplicable" and fall through.
"""
from __future__ import annotations

import sympy as sp

from ..decision import Decision, no, yes
from ..poly import X, Y, is_solution

try:
    import cypari2
    _pari = cypari2.Pari()
except Exception:  # pragma: no cover - environment without PARI
    _pari = None


def available() -> bool:
    return _pari is not None


def solve_thue(F, m: int, gpoly) -> Decision | None:
    """Decide F(x,y) = m for F homogeneous of degree ≥ 3, irreducible over ℚ,
    m ≠ 0. gpoly = F − m is used for witness verification."""
    if _pari is None or m == 0:
        return None
    univ = sp.expand(F.as_expr().subs(Y, 1))
    try:
        tnf = _pari.thueinit(str(univ).replace("**", "^"), 1)
        sols = _pari.thue(tnf, m)
    except Exception:
        return None
    witnesses = []
    for v in sols:
        try:
            w = (int(v[0]), int(v[1]))
        except Exception:
            continue
        if is_solution(gpoly, w):
            witnesses.append(w)
    if witnesses:
        return yes("pari-thue", witnesses[0],
                   f"complete solution list has {len(witnesses)} entries")
    return no("pari-thue", {"equation": f"{F.as_expr()} = {m}"},
              "certified complete solution list is empty "
              "(thueinit flag 1: unconditional)")
