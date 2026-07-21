from smale5 import decide
from smale5.decision import Status
from smale5.poly import is_solution, parse
from smale5.solvers.graph import solve_graph


def test_graph_yes_via_remainder_root():
    f = parse("y*(x^2 + 1) - x^3 - 5")
    dec = solve_graph(f)
    assert dec.status is Status.YES
    assert is_solution(f, dec.certificate)


def test_graph_certified_no():
    # y = (x^3+2)/(x^2+3): remainder -3x+2 has no integer root and outgrows
    # nothing — the window argument is a complete proof of NO.
    dec = solve_graph(parse("y*(x^2 + 3) - x^3 - 2"))
    assert dec.status is Status.NO
    assert dec.method == "graph-window"


def test_graph_exact_division_family():
    dec = solve_graph(parse("y*(x + 1) - x^2 + 1"))  # y = x - 1 exactly
    assert dec.status is Status.YES


def test_graph_constant_denominator():
    assert solve_graph(parse("2*y - x^3 - 1")).status is Status.YES
    dec = solve_graph(parse("4*y - 2*x^3 - 1"))
    assert dec.status is Status.NO
    assert dec.method == "graph-congruence"


def test_graph_swapped_orientation():
    f = parse("x*(y^2 + 3) - y^3 - 2")  # same curve, roles exchanged
    dec = solve_graph(f)
    assert dec.status is Status.NO


def test_graph_through_pipeline():
    assert decide("y*(x^2 + 3) - x^3 - 2").status is Status.NO
    dec = decide("y*(x^2 + 1) - x^3 - 5")
    assert dec.status is Status.YES
