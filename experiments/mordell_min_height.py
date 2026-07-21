"""Smale's Height Bound Hypothesis, empirically, on Mordell equations.

HBH (Smale 1998): a solvable positive-genus curve has an integer solution of
log-height polynomial in s(f) — this is what would put the positive-genus
stratum in NP. For y² = x³ + k, s ≈ log|k|, so the probe is the ratio
r(k) = log(min-height solution) / log|k|. We sweep x ≤ XMAX harvesting the
FIRST (hence minimal-height) integral point for every |k| ≤ K, then report
the record ratios and — just as importantly — the k that stay unresolved
inside the sweep: HBH stress candidates whose minimal points (if any) are
large (e.g. k = −1090, whose known point has x = 28187351, beyond XMAX).

Run: .venv/bin/python experiments/mordell_min_height.py [K] [XMAX]
Writes experiments/data/mordell_min_heights.csv.
"""
import csv
import math
import sys
from math import isqrt
from pathlib import Path

K = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
XMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 10**6


def main() -> None:
    first: dict[int, tuple[int, int]] = {}
    lo = -round(K ** (1 / 3)) - 2
    for x in range(lo, XMAX + 1):
        c = x * x * x
        if c + K < 0:
            continue
        ylo = isqrt(max(c - K, 0))
        for y in range(ylo, isqrt(c + K) + 1):
            k = y * y - c
            if k != 0 and abs(k) <= K and k not in first:
                first[k] = (x, y)
    rows = []
    for k, (x, y) in sorted(first.items()):
        h = max(abs(x), abs(y), 2)
        ratio = math.log(h) / math.log(max(abs(k), 2))
        rows.append((k, x, y, round(ratio, 3)))
    out = Path(__file__).parent / "data" / "mordell_min_heights.csv"
    out.parent.mkdir(exist_ok=True)
    with out.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["k", "x_min", "y_min", "log_height_over_log_k"])
        w.writerows(rows)
    unresolved = sorted(set(range(-K, K + 1)) - set(first) - {0})
    top = sorted(rows, key=lambda r: -r[3])[:10]
    print(f"solvable within sweep: {len(first)} of {2*K} values of k")
    print(f"unresolved (no point with x ≤ {XMAX}): {len(unresolved)}")
    print("record HBH ratios log(height)/log|k|:")
    for k, x, y, r in top:
        print(f"  k={k:>6}  (x,y)=({x},{y})  ratio={r}")
    print(f"sample unresolved k (HBH stress candidates): {unresolved[:15]}")
    print(f"-> {out}")


if __name__ == "__main__":
    main()
