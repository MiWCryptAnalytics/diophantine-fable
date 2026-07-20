from smale5.classify import classify
from smale5.families import mordell, pell, thue_cubic
from smale5.poly import parse


def _single(f):
    comps = classify(f)
    assert len(comps) == 1
    return comps[0]


def test_pell_curve_is_infinite_candidate():
    c = _single(pell(61))
    assert c.genus == 0
    assert c.points_at_infinity == 2
    assert c.siegel == "infinite-candidate"


def test_mordell_is_genus_one_finite():
    c = _single(mordell(7))
    assert c.genus == 1
    assert c.siegel == "finite"


def test_thue_cubic_is_genus_one_finite():
    c = _single(thue_cubic(5))
    assert c.genus == 1
    assert c.siegel == "finite"


def test_quartic_thue_genus_three():
    c = _single(parse("x^4 + y^4 - 17"))
    assert c.genus == 3
    assert c.siegel == "finite"


def test_circle_is_honest_candidate():
    # genus 0 with 2 (complex) points at infinity meets Siegel's necessary
    # condition even though an ellipse has finitely many integer points —
    # the label is routing metadata, not a decision.
    c = _single(parse("x^2 + y^2 - 25"))
    assert c.genus == 0
    assert c.points_at_infinity == 2
    assert c.siegel == "infinite-candidate"


def test_reducible_splits():
    comps = classify(parse("(x^2 - 61*y^2 - 1) * (x + y)"))
    assert len(comps) == 2
