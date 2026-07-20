import pytest

from smale5.poly import evaluate, is_solution, parse, size


def test_parse_uv_synonyms():
    assert parse("u*v - 6") == parse("x*y - 6")


def test_size_pell_61():
    f = parse("x^2 - 61*y^2 - 1")
    # coefficients 1, -61, -1 -> (1+1) + (1+6) + (1+1) = 11 bits, degree 2
    assert size(f) == 13


def test_normalization_clears_denominators():
    assert parse("x/2 - 1") == parse("x - 2")


def test_rejects_unknown_symbols():
    with pytest.raises(ValueError):
        parse("x^2 + z")


def test_evaluate_and_witness():
    f = parse("x^2 - 61*y^2 - 1")
    assert evaluate(f, 1766319049, 226153980) == 0
    assert is_solution(f, (1766319049, 226153980))
    assert not is_solution(f, (2, 1))
