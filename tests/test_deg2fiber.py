import random

import sympy as sp

from smale5 import decide
from smale5.decision import Status
from smale5.poly import X, Y, is_solution, normalize, parse
from smale5.solvers.deg2fiber import solve_deg2_fiber, solve_pure_square_fiber
from smale5.solvers.search import bounded_search


def test_panel_counterexample_family_now_decided():
    # y² = 2x⁴ + x² — the interrogation panel's classifier counterexample:
    # square-class 2x²+1, so it rides the Pell conic w² − 2x² = 1.
    dec = solve_deg2_fiber(parse("y^2 - 2*x^4 - x^2"))
    assert dec is not None and dec.status is Status.YES


def test_cuspidal_cubic():
    dec = solve_deg2_fiber(parse("y^2 - x^3"))  # square class x: parabola conic
    assert dec is not None and dec.status is Status.YES


def test_planted_nontrivial_yes_via_conic_path():
    # (y + (x+7))² = (x²+30)²(2x²+1): E = x²+30 has no integer root, so the
    # decision must come through the conic + divisibility-congruence path.
    f = normalize((Y + X + 7) ** 2 - (X**2 + 30) ** 2 * (2 * X**2 + 1))
    dec = solve_deg2_fiber(f)
    assert dec is not None and dec.status is Status.YES
    assert dec.method == "deg2fiber"
    assert is_solution(f, dec.certificate)


def test_certified_no_via_orbit_congruence():
    # (3y+1)² = x²(2x²+1): needs 3 | xw−1 along w²−2x²=1, but x·w ≡ 0 (mod 3)
    # on the whole Pell orbit — a NO only the congruence walk can certify.
    f = parse("9*y^2 + 6*y + 1 - 2*x^4 - x^2")
    dec = solve_deg2_fiber(f)
    assert dec is not None and dec.status is Status.NO


def test_mordell_stays_out_of_scope():
    # y² = x³ + 7 has squarefree cubic square-class: honestly not this stratum.
    assert solve_deg2_fiber(parse("y^2 - x^3 - 7")) is None


def test_through_pipeline():
    dec = decide("9*y^2 + 6*y + 1 - 2*x^4 - x^2")
    assert dec.status is Status.NO


def test_specimen_zero_falls():
    """The census's smallest undecided polynomial: (x+1)y² = −(x³−x²+1)
    forces (x+1) | 1, so x ∈ {0,−2} — both fail the square test. NO,
    despite genus 1: Runge slips past the elliptic wall."""
    dec = solve_pure_square_fiber(parse("x^3 - x^2 + x*y^2 + y^2 + 1"))
    assert dec is not None and dec.status is Status.NO
    assert decide("x^3 - x^2 + x*y^2 + y^2 + 1").status is Status.NO


def test_pure_square_yes_and_swap():
    dec = solve_pure_square_fiber(parse("(x+2)*y^2 - x^3 - 1"))
    assert dec is not None and dec.status is Status.YES
    assert is_solution(parse("(x+2)*y^2 - x^3 - 1"), dec.certificate)
    mirrored = solve_pure_square_fiber(parse("y^3 - y^2 + y*x^2 + x^2 + 1"))
    assert mirrored is not None and mirrored.status is Status.NO


def test_planted_fuzz_against_search_oracle():
    rng = random.Random(20260721)
    checked = 0
    for _ in range(40):
        B0 = sum(rng.randint(-6, 6) * X**i for i in range(rng.randint(1, 3)))
        E0 = sum(rng.randint(-5, 5) * X**i for i in range(rng.randint(1, 3)))
        Q0 = sum(rng.randint(-4, 4) * X**i for i in range(3))
        f_expr = sp.expand((Y + B0) ** 2 - E0**2 * Q0)
        f = normalize(f_expr)
        if f.degree(Y) != 2 and f.degree(X) != 2:
            continue
        dec = solve_deg2_fiber(f)
        if dec is None:
            continue
        checked += 1
        assert dec.status in (Status.YES, Status.NO), (f, dec)
        if dec.status is Status.YES and isinstance(dec.certificate, tuple):
            assert is_solution(f, dec.certificate)
        if dec.status is Status.NO:
            oracle = bounded_search(f, 60)
            assert oracle.status is not Status.YES, (f, oracle)
    assert checked >= 15  # the family must actually exercise the stratum
