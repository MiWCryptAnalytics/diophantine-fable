import sympy as sp

from smale5.decision import Status
from smale5.poly import is_solution, parse
from smale5.solvers.linear import solve_linear
from smale5.solvers.local import local_obstruction, real_obstruction
from smale5.solvers.pell import (cf_fundamental, decide_pell_like,
                                 lmm_representatives, nagell_representatives)
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


def test_pell_like_matches_bruteforce_small():
    """LMM-based decisions must agree with exhaustive search wherever search
    can see: brute YES forces solver YES; solver NO forces brute silence."""
    for D in (2, 3, 5, 6, 7, 8, 10, 11, 12, 13):
        for N in range(-20, 21):
            if N == 0:
                continue
            dec = decide_pell_like(D, N)
            assert dec.status in (Status.YES, Status.NO), (D, N, dec)
            brute = None
            for y in range(0, 300):
                rhs = N + D * y * y
                if rhs >= 0:
                    r, exact = sp.integer_nthroot(rhs, 2)
                    if exact:
                        brute = (int(r), y)
                        break
            if brute is not None:
                assert dec.status is Status.YES, (D, N, brute, dec)
            if dec.status is Status.YES:
                x, y = dec.certificate
                assert x * x - D * y * y == N, (D, N, dec)
            else:
                assert brute is None, (D, N, brute)


def test_lmm_agrees_with_nagell_solvability():
    """Both representative searches are complete on small inputs, so their
    solvability verdicts must coincide exactly."""
    for D in (2, 3, 5, 6, 7, 10, 13):
        (t, u), neg = cf_fundamental(D)
        for N in range(-15, 16):
            if N == 0:
                continue
            lmm = lmm_representatives(D, N, neg)
            nag = nagell_representatives(D, N, t, u)
            assert lmm is not None and nag is not None
            assert bool(lmm) == bool(nag), (D, N, lmm, nag)


def test_pell_like_huge_unit_via_lmm():
    """D = 1000099 (Lenstra's monster): the fundamental solution has hundreds
    of digits, so any Nagell/search-based method is hopeless — LMM must still
    decide instantly. This is the single-exponential claim made executable."""
    (t, _u), _neg = cf_fundamental(1000099)
    assert len(str(t)) > 200
    for N in (2, 3, 5, 7, -3):
        dec = decide_pell_like(1000099, N)
        assert dec.status in (Status.YES, Status.NO), (N, dec)
        if dec.status is Status.YES and isinstance(dec.certificate, tuple):
            x, y = dec.certificate
            assert x * x - 1000099 * y * y == N


def test_cf_cap_confesses_instead_of_hanging():
    """Interrogation-panel catch: cf_fundamental was the one uncapped
    exponential loop — this conic (Δ ≈ 2×10²³) used to hang for ~10¹¹ steps."""
    dec = solve_quadratic(parse(
        "-117045681093*x^2 - 629408638379*x*y - 402519276592*y^2"
        " - 388027523941*x - 82120207152*y - 957350659965"))
    assert dec.status is Status.UNDECIDED
    assert dec.method == "pell-cf"


def test_large_delta_no_str_crash():
    """Interrogation-panel catch: len(str(t)) exceeded CPython's int→str digit
    limit for Δ ≳ 10⁹, crashing exactly the large-unit YES instances."""
    f = parse("x^2 - 1000000007*y^2 + 49123")
    dec = solve_quadratic(f)
    assert dec.status in (Status.YES, Status.UNDECIDED)
    if dec.status is Status.YES and isinstance(dec.certificate, tuple):
        assert is_solution(f, dec.certificate)
    str(dec)  # printing must not raise either


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
