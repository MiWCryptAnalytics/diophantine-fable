from smale5.decision import Status
from smale5.poly import is_solution, parse
from smale5.solvers.linear import solve_linear
from smale5.solvers.local import local_obstruction, real_obstruction
from smale5.solvers.pell import cf_fundamental, decide_pell_like
from smale5.solvers.quadratic import solve_quadratic


def test_linear_yes_and_no():
    dec = solve_linear(parse("3*x + 5*y - 1"))
    assert dec.status is Status.YES
    assert solve_linear(parse("2*x + 4*y - 3")).status is Status.NO


def test_local_obstruction_sum_of_squares():
    dec = local_obstruction(parse("x^2 + y^2 - 3"))
    assert dec is not None and dec.status is Status.NO
    assert local_obstruction(parse("x^2 + y^2 - 25")) is None


def test_real_obstruction():
    dec = real_obstruction(parse("x^2 + y^2 + 1"))
    assert dec is not None and dec.status is Status.NO


def test_cf_fundamental_classics():
    assert cf_fundamental(2) == ((3, 2), (1, 1))
    assert cf_fundamental(3) == ((2, 1), None)
    (t, u), neg = cf_fundamental(61)
    assert neg == (29718, 3805)
    assert t == 1766319049 and u == 226153980


def test_pell_negative_one_parity():
    # x² − 3y² = −1 unsolvable (even CF period); x² − 2y² = −1 solvable.
    assert decide_pell_like(3, -1).status is Status.NO
    dec = decide_pell_like(2, -1)
    assert dec.status is Status.YES and dec.certificate == (1, 1)


def test_generalized_pell_representatives():
    dec = decide_pell_like(2, 7)
    assert dec.status is Status.YES
    x, y = dec.certificate
    assert x * x - 2 * y * y == 7
    assert decide_pell_like(5, 2).status is Status.NO


def test_quadratic_pell_conic():
    f = parse("x^2 - 61*y^2 - 1")
    dec = solve_quadratic(f)
    assert dec.status is Status.YES
    assert is_solution(f, dec.certificate)

    f2 = parse("2*x^2 - 3*y^2 - 5")
    dec2 = solve_quadratic(f2)
    assert dec2.status is Status.YES
    assert is_solution(f2, dec2.certificate)

    # x² − 3y² = −1 via the full conic path (bypasses the pipeline's local check)
    assert solve_quadratic(parse("x^2 - 3*y^2 + 1")).status is Status.NO


def test_quadratic_ellipse():
    dec = solve_quadratic(parse("x^2 + y^2 - 26"))
    assert dec.status is Status.YES
    assert solve_quadratic(parse("x^2 + y^2 - 21")).status is Status.NO


def test_quadratic_rect_hyperbola():
    dec = solve_quadratic(parse("x*y - 6"))
    assert dec.status is Status.YES
    # (2x+1)(2y+1) = 4 has no odd·odd = 4 splitting
    assert solve_quadratic(parse("4*x*y + 2*x + 2*y - 3")).status is Status.NO


def test_quadratic_parabola():
    dec = solve_quadratic(parse("y^2 - 2*x - 1"))
    assert dec.status is Status.YES
    assert solve_quadratic(parse("x^2 + 4*y^2 + 4")).status is Status.NO
