import pytest

from smale5.poly import evaluate, is_solution, parse, size


def test_parse_uv_synonyms():
    assert parse("u*v - 6") == parse("x*y - 6")


def test_size_smale_dense():
    f = parse("x^2 - 61*y^2 - 1")
    # d=2 has 6 slots; coefficients 1, -61, -1 give 1+6+1, empty slots 1 each
    assert size(f) == 11
    # the dense measure charges for sparsity: x^5 - 1 has (5+1)(5+2)/2 = 21 slots
    assert size(parse("x^5 - 1")) == 21


def test_normalization_clears_denominators():
    assert parse("x/2 - 1") == parse("x - 2")


def test_rejects_unknown_symbols():
    with pytest.raises(ValueError):
        parse("x^2 + z")


def test_rejects_charset_legal_non_polynomials():
    for bad in ("x/y", "1/x", "x^x", "2^x", "1/0", "()"):
        with pytest.raises(ValueError):
            parse(bad)


def test_evaluate_and_witness():
    f = parse("x^2 - 61*y^2 - 1")
    assert evaluate(f, 1766319049, 226153980) == 0
    assert is_solution(f, (1766319049, 226153980))
    assert not is_solution(f, (2, 1))
