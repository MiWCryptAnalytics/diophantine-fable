"""Fast NO certificates: congruence and sign obstructions.

An integer solution of f = 0 survives reduction mod every m and evaluation
over ℝ, so failure of either is a finite, re-checkable proof of NO.
"""
from __future__ import annotations

import sympy as sp

from ..decision import Decision, no
from ..poly import coeff_dict


def _prime_power_moduli(limit: int = 81) -> list[int]:
    out = []
    for p in sp.primerange(2, limit + 1):
        m = p
        while m <= limit:
            out.append(m)
            m *= p
    return sorted(out)


MODULI = _prime_power_moduli()


def local_obstruction(poly, moduli=None) -> Decision | None:
    terms = coeff_dict(poly)
    for m in (moduli or MODULI):
        if not _solvable_mod(terms, m):
            return no("local-obstruction", certificate={"modulus": m},
                      detail=f"f(x,y) ≢ 0 (mod {m}) for all {m}² residue pairs")
    return None


def _solvable_mod(terms, m: int) -> bool:
    max_j = max(j for _, j in terms)
    for x in range(m):
        # collapse to a univariate in y: c_j = Σ_i a_ij x^i (mod m)
        cy = [0] * (max_j + 1)
        for (i, j), a in terms.items():
            cy[j] = (cy[j] + a * pow(x, i, m)) % m
        for y in range(m):
            acc = 0
            for j in range(max_j, -1, -1):
                acc = (acc * y + cy[j]) % m
            if acc == 0:
                return True
    return False


def real_obstruction(poly) -> Decision | None:
    """Sufficient sign-definiteness check: every monomial has even exponents in
    both variables and the same sign as the (nonzero) constant term, so
    |f(x,y)| ≥ |f(0,0)| > 0 on all of ℝ²."""
    terms = coeff_dict(poly)
    const = terms.get((0, 0), 0)
    if const == 0:
        return None
    sgn = 1 if const > 0 else -1
    if all(i % 2 == 0 and j % 2 == 0 and sgn * a > 0 for (i, j), a in terms.items()):
        return no("real-obstruction", certificate="sign-definite",
                  detail="all monomials even in x and y with the sign of the "
                         f"constant term {const}; |f| ≥ {abs(const)} on ℝ²")
    return None
