"""Track B, one rung up: fundamental-unit growth in pure cubic fields.

For the Thue family x³ − d·y³ = 1 the role of the Pell fundamental solution
is played by the fundamental unit ε of ℚ(∛d) (complex cubic, unit rank 1).
We record d whenever the digit-size of ε's coefficients sets a record —
charting the same doubly-exponential-witness envelope that killed
search-based methods in the quadratic layer, now for the stratum where even
exponential-time decidability is open (frontier: the Thue sting).

Regulators are computed by PARI under GRH (bnfinit); record rows are
re-certified with bnfcertify (unconditional) and flagged if certification
was skipped.

Run: .venv/bin/python experiments/thue_unit_growth.py [LIMIT]
Writes experiments/data/cubic_unit_records.csv.
"""
import csv
import sys
import time
from pathlib import Path

import cypari2
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from smale5.poly import parse, size  # noqa: E402

pari = cypari2.Pari()
LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 2000


def cubefree_non_cube(d: int) -> bool:
    if sp.integer_nthroot(d, 3)[1]:
        return False
    return all(e < 3 for e in sp.factorint(d).values())


def unit_digits(d: int) -> tuple[float, int]:
    reg = float(pari(f"bnfinit(x^3-{d},1).reg"))
    fu = pari(f"lift(bnfinit(x^3-{d},1).fu[1])")
    digits = 0
    for i in range(3):
        c = pari.polcoef(fu, i)
        num = int(pari.numerator(c))
        digits = max(digits, (abs(num).bit_length() * 30103) // 100000)
    return reg, digits


def main() -> None:
    t0 = time.time()
    records, best = [], -1
    for d in range(2, LIMIT + 1):
        if not cubefree_non_cube(d):
            continue
        reg, digits = unit_digits(d)
        if digits > best:
            best = digits
            certified = bool(pari(f"bnfcertify(bnfinit(x^3-{d},1))"))
            s = size(parse(f"x^3 - {d}*y^3 - 1"))
            records.append((d, s, round(reg, 2), digits, certified))
    out = Path(__file__).parent / "data" / "cubic_unit_records.csv"
    out.parent.mkdir(exist_ok=True)
    with out.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["d", "s(f)", "regulator", "unit_coeff_digits", "certified"])
        w.writerows(records)
    print(f"{'d':>6} {'s(f)':>5} {'regulator':>12} {'digits':>7} {'cert':>5}")
    for row in records:
        print(f"{row[0]:>6} {row[1]:>5} {row[2]:>12} {row[3]:>7} {str(row[4]):>5}")
    print(f"\n{len(records)} records for cubefree non-cube d ≤ {LIMIT} "
          f"({time.time() - t0:.1f}s) -> {out}")


if __name__ == "__main__":
    main()
