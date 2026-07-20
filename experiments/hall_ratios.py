"""Track B: Hall's conjecture in the wild.

For x³ − y² = k ≠ 0, Hall's ratio r(x) = √x / |k|. Hall's conjecture (strong
form, now usually stated with an ε) says r is bounded; the known record
examples are astonishingly sparse. We sweep x ≤ LIMIT recording every new
record ratio — rediscovering the classical extremal points from scratch and
charting how rare near-collisions of x³ and y² really are. Mordell equations
with tiny |k| and huge x are exactly the sporadic points that make effective
Siegel hard (gap G3 in notes/A1.md).

Run: .venv/bin/python experiments/hall_ratios.py [LIMIT]
Writes experiments/data/hall_records.csv.
"""
import csv
import math
import sys
import time
from math import isqrt
from pathlib import Path

LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 10_000_000


def main() -> None:
    t0 = time.time()
    records = []
    best = 0.0
    for x in range(2, LIMIT + 1):
        c = x * x * x
        y = isqrt(c)
        for yy in (y, y + 1):
            k = c - yy * yy
            if k == 0:
                continue
            r = math.sqrt(x) / abs(k)
            if r > best:
                best = r
                records.append((x, yy, k, round(r, 4)))
    out = Path(__file__).parent / "data" / "hall_records.csv"
    out.parent.mkdir(exist_ok=True)
    with out.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["x", "y", "k = x^3 - y^2", "hall_ratio"])
        w.writerows(records)
    print(f"{'x':>9} {'y':>14} {'k':>8} {'sqrt(x)/|k|':>12}")
    for row in records:
        print(f"{row[0]:>9} {row[1]:>14} {row[2]:>8} {row[3]:>12}")
    print(f"\n{len(records)} records for x ≤ {LIMIT} ({time.time() - t0:.1f}s) -> {out}")


if __name__ == "__main__":
    main()
