"""A1-v2 prototype: the Pell orbit walk lifted to pure cubic fields.

Decide x³ − d·y³ = m (d cubefree, not a cube) WITHOUT search: a solution is
an element γ = x − y·α (α = ∛d) of norm m in K = ℚ(α); K is a complex cubic
field, so its unit group is ⟨−1, ε⟩ of rank 1, and every norm-m element is
(class representative) · (±ε^k). "Being of Thue shape" is one linear
condition — the α²-coordinate of γ·ε^k vanishes — i.e. a zero of an order-3
linear recurrence with dominant root: a Skolem instance of the decidable
kind. This prototype walks k ∈ [−K0, K0] and validates the resulting
decision and FULL solution set against PARI's certified thue() on a grid.

The K0 cutoff is the honest gap between prototype and theorem: the A1-v2
note (notes/A1v2-cubic-thue.md) records what a proof needs (an explicit
dominant-root bound on the last vanishing index).

Run: .venv/bin/python experiments/cubic_orbit_prototype.py
"""
import time

import cypari2

pari = cypari2.Pari()

K0 = 60
DS = [2, 3, 5, 6, 7, 10, 11, 12, 13, 15, 17, 19, 20, 22]
M_RANGE = 40


MAX_K_SEEN = [0]


def orbit_solutions(d: int, m: int):
    """All (x, y) with x³ − d·y³ = m via class reps × unit orbit."""
    bnf = pari.bnfinit(f"x^3 - {d}", 1)
    eps = pari(f"bnfinit(x^3-{d},1).fu")[0]
    reps = pari.bnfisintnorm(bnf, m)
    found = set()
    for rep in reps:
        g = pari.Mod(rep, f"x^3 - {d}")
        for direction, unit in ((1, eps), (-1, 1 / eps)):
            cur = g if direction == 1 else g * unit  # avoid double k=0
            k = 0 if direction == 1 else 1
            for _ in range(K0 + 1):
                for cand in (cur, -cur):
                    lifted = pari.lift(cand)
                    c0 = pari.polcoef(lifted, 0)
                    c1 = pari.polcoef(lifted, 1)
                    c2 = pari.polcoef(lifted, 2)
                    if c2 == 0 and pari.denominator(c0) == 1 \
                            and pari.denominator(c1) == 1:
                        x, y = int(c0), -int(c1)
                        if x**3 - d * y**3 == m:
                            found.add((x, y))
                            MAX_K_SEEN[0] = max(MAX_K_SEEN[0], k)
                cur = cur * unit
                k += 1
    return found


def pari_thue_solutions(d: int, m: int):
    tnf = pari.thueinit(f"x^3 - {d}", 1)
    out = set()
    for v in pari.thue(tnf, m):
        out.add((int(v[0]), int(v[1])))
    return out


def main() -> None:
    t0 = time.time()
    cases = agree = disagreements = 0
    yes_cases = 0
    for d in DS:
        for m in [m for m in range(-M_RANGE, M_RANGE + 1) if m != 0]:
            ours = orbit_solutions(d, m)
            ref = pari_thue_solutions(d, m)
            cases += 1
            if ours == ref:
                agree += 1
                if ref:
                    yes_cases += 1
            else:
                disagreements += 1
                print(f"MISMATCH d={d} m={m}: orbit={sorted(ours)} "
                      f"thue={sorted(ref)}")
    print(f"{cases} cases: {agree} exact solution-set agreements "
          f"({yes_cases} solvable), {disagreements} mismatches "
          f"({time.time() - t0:.1f}s, walk cutoff K0={K0}, "
          f"max vanishing index |k| = {MAX_K_SEEN[0]})")


if __name__ == "__main__":
    main()
