"""Cap schedules: the bridge between the analyzed algorithm and the artifact.

Theorem A1's algorithm carries budgets growing like 2^(c·s); a fixed-cap
implementation is only a truncation of it (interrogation-panel finding,
2026-07-21: in-scope inputs went UNDECIDED at s = 26). `scaled(s)` grows the
iteration caps exponentially from s = 21 up to a hard ceiling — the honest
truncation point that the docs advertise. The CF cap grows like the square
root of the boost because its cost is quadratic in the steps walked.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Caps:
    enum: int = 2_000_000       # residue-class and window scans
    divisor: int = 10**15       # magnitude ceiling for factor-and-enumerate
    pell_scan: int = 2_000_000  # LMM representative search steps
    pell_walk: int = 2_000_000  # orbit-walk steps mod M
    cf: int = 50_000            # continued-fraction period steps (cost ~ quadratic)


DEFAULT = Caps()
_BOOST_CEILING = 256


def scaled(s: int) -> Caps:
    boost = min(2 ** max(s - 21, 0), _BOOST_CEILING)
    root = max(int(boost ** 0.5), 1)
    return Caps(enum=DEFAULT.enum * boost,
                divisor=DEFAULT.divisor,
                pell_scan=DEFAULT.pell_scan * boost,
                pell_walk=DEFAULT.pell_walk * boost,
                cf=DEFAULT.cf * root)
