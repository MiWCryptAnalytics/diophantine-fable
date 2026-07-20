"""Archival verification of the July 2026 Jacobian Conjecture counterexample
(Smale problem #16), independently re-checked at this project's kickoff.

F: ℂ³ → ℂ³ below has Jacobian determinant ≡ −2 yet identifies three points —
a polynomial map with constant nonzero Jacobian that is not injective, i.e. a
counterexample to the Jacobian Conjecture in dimension 3.

Run: .venv/bin/python scripts/verify_jc_counterexample.py
"""
import sympy as sp

x, y, z = sp.symbols("x y z")

F = sp.Matrix([
    (1 + x*y)**3 * z + y**2 * (1 + x*y) * (4 + 3*x*y),
    y + 3*x*(1 + x*y)**2 * z + 3*x*y**2 * (4 + 3*x*y),
    2*x - 3*x**2*y - x**3*z,
])

POINTS = [(0, 0, sp.Rational(-1, 4)),
          (1, sp.Rational(-3, 2), sp.Rational(13, 2)),
          (-1, sp.Rational(3, 2), sp.Rational(13, 2))]


def main() -> None:
    det = sp.expand(F.jacobian([x, y, z]).det())
    assert det == -2, det
    print("Jacobian determinant ≡", det)
    images = [tuple(F.subs(dict(zip((x, y, z), p)))) for p in POINTS]
    for p, img in zip(POINTS, images):
        print(f"F{p} = {img}")
    assert len(set(images)) == 1
    assert len(set(POINTS)) == 3
    print("Constant nonzero Jacobian + non-injective: Jacobian Conjecture fails in dim 3.")


if __name__ == "__main__":
    main()
