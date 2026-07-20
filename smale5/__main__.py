"""CLI: .venv/bin/python -m smale5 "x^2 - 61*y^2 - 1" """
import argparse

from . import classify, decide, parse, size


def main() -> None:
    ap = argparse.ArgumentParser(prog="smale5",
                                 description="Decide f(x,y)=0 over the integers (honestly).")
    ap.add_argument("polynomial", help="e.g. 'x^2 - 61*y^2 - 1' (u,v accepted)")
    ap.add_argument("--bound", type=int, default=2000,
                    help="fallback search bound H (default 2000)")
    args = ap.parse_args()

    f = parse(args.polynomial)
    print(f"f(x,y) = {f.as_expr()}")
    print(f"size s(f) = {size(f)}")
    for comp in classify(f):
        print(f"  component {comp.poly.as_expr()}: kind={comp.kind} deg={comp.degree} "
              f"genus={comp.genus} pts∞={comp.points_at_infinity} siegel={comp.siegel}")
    print(decide(f, search_bound=args.bound))


if __name__ == "__main__":
    main()
