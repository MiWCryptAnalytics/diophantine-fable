"""The Census: every f ∈ ℤ[x,y] of dense size s ≤ SMAX, decided.

Enumerates all primitive polynomials of exact dense Smale-size s (ascending,
so the SMALLEST open problems surface first), canonicalized under the
16-element symmetry group (x↔y, sign flips, global negation), and runs the
full pipeline on each. Outputs:
  - per-s decision statistics (the toolkit's honest coverage metric),
  - the minimal-s UNDECIDED specimens — the concrete polynomials where the
    frontier of Smale #5 begins,
  - any crash or timeout (the census doubles as a fuzzer).

Run: .venv/bin/python experiments/census.py [SMAX]
Writes experiments/data/census_stats.json and census_specimens.jsonl
incrementally (safe to inspect mid-run).
"""
import json
import signal
import sys
import time
from collections import Counter
from math import gcd
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from smale5 import decide  # noqa: E402
from smale5.decision import Status  # noqa: E402
from smale5.poly import X, Y  # noqa: E402

SMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 12
DATA = Path(__file__).parent / "data"
DATA.mkdir(exist_ok=True)
SPECIMENS = DATA / "census_specimens.jsonl"
STATS = DATA / "census_stats.json"
GRID = 4
PER_POLY_TIMEOUT = 3  # seconds


class _Timeout(Exception):
    pass


def _alarm(_sig, _frm):
    raise _Timeout


def slots_for(d):
    return [(i, j) for i in range(d + 1) for j in range(d + 1 - i)]


def gen_exact(slots, s):
    """All coefficient tuples whose dense cost is exactly s."""
    n = len(slots)

    def dfs(idx, budget):
        if idx == n:
            if budget == 0:
                yield ()
            return
        rem = n - idx - 1
        for c in range(1, budget - rem + 1):
            if c == 1:
                vals = (0, 1, -1)
            else:
                lo, hi = 1 << (c - 1), (1 << c) - 1
                vals = tuple(v for a in range(lo, hi + 1) for v in (a, -a))
            for v in vals:
                yield from ((v,) + rest for rest in dfs(idx + 1, budget - c))

    yield from dfs(0, s)


def canonical(slots, coeffs):
    """Minimal representative under (x↔y) × (x→−x) × (y→−y) × (f→−f)."""
    d = dict(zip(slots, coeffs))
    best = None
    for swap in (False, True):
        for sx in (1, -1):
            for sy in (1, -1):
                for sf in (1, -1):
                    var = tuple(
                        sf * (sx ** (j if swap else i)) * (sy ** (i if swap else j))
                        * d.get((j, i) if swap else (i, j), 0)
                        for (i, j) in slots)
                    if best is None or var < best:
                        best = var
    return best == tuple(coeffs)


def grid_root(slots, coeffs):
    terms = [(i, j, a) for (i, j), a in zip(slots, coeffs) if a]
    for xv in range(-GRID, GRID + 1):
        for yv in range(-GRID, GRID + 1):
            if sum(a * xv**i * yv**j for i, j, a in terms) == 0:
                return True
    return False


def main() -> None:
    signal.signal(signal.SIGALRM, _alarm)
    t0 = time.time()
    all_stats = {}
    SPECIMENS.write_text("")
    for s in range(3, SMAX + 1):
        tally = Counter()
        methods = Counter()
        for d in range(1, 4):
            slots = slots_for(d)
            if len(slots) > s:
                continue
            for coeffs in gen_exact(slots, s):
                if not any(a for (i, j), a in zip(slots, coeffs) if i + j == d):
                    continue  # degree exactly d, else double-counted
                nz = [abs(a) for a in coeffs if a]
                if not nz or (len(nz) >= 1 and gcd(*nz, 0) > 1):
                    continue  # primitive representatives only
                if not canonical(slots, coeffs):
                    continue
                tally["total"] += 1
                if grid_root(slots, coeffs):
                    tally["YES"] += 1
                    continue
                expr = sp.Add(*[a * X**i * Y**j
                                for (i, j), a in zip(slots, coeffs) if a])
                try:
                    signal.alarm(PER_POLY_TIMEOUT)
                    dec = decide(expr, search_bound=64)
                    if dec.status is Status.UNDECIDED:
                        signal.alarm(3 * PER_POLY_TIMEOUT)
                        dec = decide(expr, search_bound=3000)
                    signal.alarm(0)
                except _Timeout:
                    tally["TIMEOUT"] += 1
                    with SPECIMENS.open("a") as fh:
                        fh.write(json.dumps({"s": s, "f": str(expr),
                                             "status": "TIMEOUT"}) + "\n")
                    continue
                except Exception as exc:  # census doubles as fuzzer
                    signal.alarm(0)
                    tally["CRASH"] += 1
                    with SPECIMENS.open("a") as fh:
                        fh.write(json.dumps({"s": s, "f": str(expr),
                                             "status": "CRASH",
                                             "error": repr(exc)}) + "\n")
                    continue
                tally[dec.status.value] += 1
                methods[dec.method] += 1
                if dec.status is Status.UNDECIDED:
                    with SPECIMENS.open("a") as fh:
                        fh.write(json.dumps({"s": s, "f": str(expr),
                                             "status": "UNDECIDED",
                                             "method": dec.method,
                                             "detail": dec.detail}) + "\n")
        all_stats[s] = {"tally": dict(tally), "methods": dict(methods)}
        STATS.write_text(json.dumps(
            {"smax_done": s, "elapsed_s": round(time.time() - t0, 1),
             "stats": all_stats}, indent=2))
        und = tally.get("UNDECIDED", 0) + tally.get("TIMEOUT", 0)
        print(f"s={s}: {tally.get('total', 0)} canonical polys, "
              f"YES={tally.get('YES', 0)} NO={tally.get('NO', 0)} "
              f"UNDECIDED={und} CRASH={tally.get('CRASH', 0)} "
              f"[{time.time() - t0:.0f}s]", flush=True)
    print("census complete ->", STATS)


if __name__ == "__main__":
    main()
