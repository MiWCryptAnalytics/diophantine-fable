"""Track B: empirical envelope of Pell fundamental-solution growth.

For each nonsquare d ≤ LIMIT, compute the fundamental solution (t, u) of
x² − d·y² = 1 and record d whenever digits(t) sets a new record. The records
chart the doubly-exponential-witness barrier: s(f) grows like log d while
record digits grow like ~√d = 2^Θ(s) — witnesses of magnitude 2^(2^Θ(s)).

Run: .venv/bin/python experiments/pell_growth.py [LIMIT]
Writes experiments/data/pell_records.csv and prints the record table.
"""
import csv
import math
import sys
import time
from pathlib import Path

import sympy as sp

from smale5.families import pell
from smale5.poly import size
from smale5.solvers.pell import cf_fundamental

LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 20000


def main() -> None:
    t0 = time.time()
    records = []
    best = 0
    for d in range(2, LIMIT + 1):
        if sp.integer_nthroot(d, 2)[1]:
            continue
        (t, _u), _ = cf_fundamental(d)
        digits = len(str(t))
        if digits > best:
            best = digits
            records.append((d, size(pell(d)), digits, round(digits / math.sqrt(d), 4)))
    out = Path(__file__).parent / "data" / "pell_records.csv"
    out.parent.mkdir(exist_ok=True)
    with out.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["d", "s(f)", "digits_of_t", "digits_per_sqrt_d"])
        w.writerows(records)
    print(f"{'d':>7} {'s(f)':>5} {'digits(t)':>10} {'digits/√d':>10}")
    for row in records:
        print(f"{row[0]:>7} {row[1]:>5} {row[2]:>10} {row[3]:>10}")
    print(f"\n{len(records)} records among nonsquare d ≤ {LIMIT} "
          f"({time.time() - t0:.1f}s) -> {out}")


if __name__ == "__main__":
    main()
