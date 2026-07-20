import random

import pytest

from smale5 import decide, parse
from smale5.decision import Status
from smale5.families import mordell, pell, thue_cubic
from smale5.poly import is_solution
from smale5.solvers import thue_pari


def test_trivial_cases():
    assert decide("0").status is Status.YES
    assert decide("5").status is Status.NO
    assert decide("x - x").status is Status.YES


def test_pell_61_end_to_end():
    dec = decide(pell(61))
    assert dec.status is Status.YES


def test_mordell_minus_2_yes():
    dec = decide(mordell(-2))  # y² = x³ − 2 has (3, ±5)
    assert dec.status is Status.YES


def test_mordell_7_is_honestly_undecided():
    # y² = x³ + 7 has no integer solutions, but the classical proof is global
    # (not a congruence); our pipeline must confess UNDECIDED, not guess.
    dec = decide(mordell(7), search_bound=50)
    assert dec.status is Status.UNDECIDED


@pytest.mark.skipif(not thue_pari.available(), reason="PARI backend not present")
def test_thue_certified_decisions():
    dec_yes = decide(thue_cubic(1))
    assert dec_yes.status is Status.YES
    # m=5 dies locally (cubes mod 9), so use m=19: every local filter passes
    # and only the certified global argument (PARI) yields the NO.
    dec_local = decide(thue_cubic(5))
    assert dec_local.status is Status.NO
    assert dec_local.method == "local-obstruction"
    dec_no = decide(thue_cubic(19))
    assert dec_no.status is Status.NO
    assert dec_no.method == "pari-thue"


def test_reducible_yes_through_one_component():
    dec = decide("(x^2 + y^2 + 1) * (3*x + 5*y - 1)")
    assert dec.status is Status.YES


def test_reducible_all_components_no():
    dec = decide("(x^2 + y^2 + 1) * (2*x + 4*y - 3)")
    assert dec.status is Status.NO


def test_planted_solutions():
    rng = random.Random(20260720)
    for _ in range(5):
        x0, y0 = rng.randint(-40, 40), rng.randint(-40, 40)
        f = parse(f"(x - ({x0}))^2 + (y - ({y0}))^2")
        dec = decide(f)
        assert dec.status is Status.YES
        assert is_solution(f, dec.certificate)
