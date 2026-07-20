"""Named families used as test data and as the extremal-growth measurement set."""
from ..poly import parse


def pell(d: int):
    """x² − d·y² = 1. For nonsquare d > 0 always solvable; fundamental solutions
    can have exponentially many digits in the bit-size of d (the central
    obstruction to search-based algorithms for Smale #5)."""
    return parse(f"x^2 - {d}*y^2 - 1")


def mordell(k: int):
    """y² = x³ + k. Genus 1: finitely many integral points (Siegel), effective
    via Baker with bounds doubly exponential in log|k| — the proven-vs-conjectured
    (Hall) gap in miniature."""
    return parse(f"y^2 - x^3 - ({k})")


def thue_cubic(m: int):
    """x³ − 2y³ = m. Thue equation: finitely many solutions, unconditionally
    decidable (PARI thue with certified flag)."""
    return parse(f"x^3 - 2*y^3 - ({m})")
