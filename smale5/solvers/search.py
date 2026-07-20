"""Bounded exhaustive search — never a proof of NO, always honest about H."""
from __future__ import annotations

from ..decision import Decision, undecided, yes
from ..poly import coeff_dict


def bounded_search(poly, H: int) -> Decision:
    terms = list(coeff_dict(poly).items())

    def val(xv: int, yv: int) -> int:
        return sum(a * xv**i * yv**j for (i, j), a in terms)

    for r in range(H + 1):
        if r == 0:
            ring = [(0, 0)]
        else:
            ring = [(x, y) for x in range(-r, r + 1) for y in (-r, r)]
            ring += [(x, y) for x in (-r, r) for y in range(-r + 1, r)]
        for (x, y) in ring:
            if val(x, y) == 0:
                return yes("search", (x, y), f"found at max-norm {r}")
    return undecided("search", bound=H,
                     detail=f"no solution with max(|x|,|y|) ≤ {H}")
