"""Pell machinery: continued fractions, fundamental units, and deciding
x² − D·y² = N (optionally under congruence conditions) WITHOUT enumerating
integer points.

This module is the toolkit's showpiece of the Smale-#5 moral: minimal
solutions can have exponentially many digits in the input size (so search is
hopeless), yet solvability is decided by (1) Nagell's bound, which confines
one representative of each solution class to a small window, and (2) walking
each class's orbit under the fundamental automorphism σ *modulo M*, which is
finite and purely periodic. A hit is reconstructed (or certified symbolically
when the witness would be astronomically large); a completed scan with no hit
is a proof of NO.
"""
from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from ..decision import Decision, no, undecided, yes


def is_square(n: int) -> bool:
    return n >= 0 and sp.integer_nthroot(n, 2)[1]


def cf_fundamental(D: int):
    """Continued fraction of √D (D > 0 nonsquare): returns ((t,u), neg) where
    (t,u) is the least solution of t² − D·u² = 1 and neg is the least solution
    of x² − D·y² = −1, or None (exists iff the CF period is odd)."""
    a0, exact = sp.integer_nthroot(D, 2)
    a0 = int(a0)
    if exact:
        raise ValueError("D must be nonsquare")
    m, dd, a = 0, 1, a0
    p_prev, p = 1, a0
    q_prev, q = 0, 1
    while True:
        m = dd * a - m
        dd = (D - m * m) // dd
        a = (a0 + m) // dd
        p_prev, p = p, a * p + p_prev
        q_prev, q = q, a * q + q_prev
        if a == 2 * a0:
            break
    x1, y1 = p_prev, q_prev  # convergent just before the period closes
    if x1 * x1 - D * y1 * y1 == 1:
        return (x1, y1), None
    assert x1 * x1 - D * y1 * y1 == -1
    return (x1 * x1 + D * y1 * y1, 2 * x1 * y1), (x1, y1)


@dataclass
class OrbitCongruence:
    """Acceptance test on residues: accept(x mod M, y mod M) with lifts in [0,M)."""
    modulus: int
    accept: object  # callable (xm, ym) -> bool


def decide_pell_like(D: int, N: int, cong: OrbitCongruence | None = None,
                     recover=None, scan_cap: int = 2_000_000,
                     walk_cap: int = 2_000_000,
                     witness_digit_cap: int = 2_000_000) -> Decision:
    """Decide ∃(x,y) ∈ ℤ²: x² − D·y² = N, and cong(x,y) if given.

    D > 0 nonsquare. `recover(x, y)` may map a raw Pell solution to a witness
    in original coordinates (returning None to reject); it is only called on
    exact solutions that already passed the congruence test.
    """
    if N == 0:
        # D nonsquare: x² = D·y² forces (0,0).
        if cong is None or cong.accept(0, 0):
            w = (0, 0) if recover is None else recover(0, 0)
            return yes("pell-trivial", w, "only solution of x² = D·y² is (0,0)")
        return no("pell-trivial", detail="only candidate (0,0) fails congruences")

    (t, u), neg = cf_fundamental(D)

    if N == 1:
        base = [(1, 0)]
        completeness = "x²−Dy²=1: all solutions are ±σ^k(1,0)"
    elif N == -1:
        if neg is None:
            return no("pell-period-parity",
                      detail=f"x²−{D}y²=−1 unsolvable: continued fraction of "
                             f"√{D} has even period")
        base = [neg]
        completeness = "x²−Dy²=−1: all solutions are ±σ^k(x₁,y₁)"
    else:
        # Nagell: each class of x²−Dy²=N has a representative with
        # 0 ≤ y ≤ u·√|N| / √(2(t∓1)). We scan the (larger) t−1 bound for both
        # signs of N — enlarging the window never hurts completeness.
        B = sp.integer_nthroot((u * u * abs(N)) // max(2 * (t - 1), 1), 2)[0] + 2
        if B > scan_cap:
            return undecided("pell-nagell", bound=scan_cap,
                             detail=f"representative bound {B} exceeds scan cap")
        base = []
        for yv in range(B + 1):
            rhs = N + D * yv * yv
            if is_square(rhs):
                base.append((int(sp.integer_nthroot(rhs, 2)[0]), yv))
        completeness = f"Nagell representative scan complete up to y ≤ {B}"

    if cong is None:
        if base:
            xw, yw = base[0]
            w = (xw, yw) if recover is None else recover(xw, yw)
            return yes("pell-representative", w)
        return no("pell-nagell-complete", certificate={"D": D, "N": N},
                  detail=completeness + "; no class representatives exist")

    # Orbit walk mod M. Seeds: all sign variants of every representative
    # (classes come in ± and conjugate pairs; the walk itself covers all k ∈ ℤ
    # because σ mod M is invertible, so its orbit is a pure cycle).
    M = cong.modulus
    seeds = []
    for (xv, yv) in base:
        for sx in (1, -1):
            for sy in (1, -1):
                s = (sx * xv, sy * yv)
                if s not in seeds:
                    seeds.append(s)
    steps_total = 0
    periods = []
    for seed in seeds:
        sx, sy = seed
        start = (sx % M, sy % M)
        state = start
        k = 0
        while True:
            if cong.accept(*state):
                return _reconstruct(D, N, seed, k, t, u, recover,
                                    witness_digit_cap)
            state = ((t * state[0] + D * u * state[1]) % M,
                     (u * state[0] + t * state[1]) % M)
            k += 1
            steps_total += 1
            if state == start:
                periods.append(k)
                break
            if steps_total > walk_cap:
                return undecided("pell-orbit-walk", bound=walk_cap,
                                 detail=f"orbit walk mod {M} exceeded step cap")
    return no("pell-orbit-scan", certificate={"D": D, "N": N, "modulus": M},
              detail=f"{completeness}; all {len(seeds)} sign-variant orbits "
                     f"walked one full period mod {M} (periods {periods}); "
                     "no residue satisfies the congruences")


def _reconstruct(D, N, seed, k, t, u, recover, digit_cap) -> Decision:
    est_digits = (k + 1) * (len(str(t)) + len(str(seed[0])) + 1)
    if est_digits > digit_cap:
        return yes("pell-orbit-certificate",
                   {"D": D, "N": N, "class": seed, "power": k},
                   detail=f"solution σ^{k}(seed): the orbit identity keeps "
                          f"x²−{D}y²={N} and the congruence was checked exactly "
                          f"mod the walk modulus; ≈{est_digits} digits, not "
                          "materialized")
    x, y = seed
    for _ in range(k):
        x, y = t * x + D * u * y, u * x + t * y
    assert x * x - D * y * y == N
    if recover is not None:
        w = recover(x, y)
        assert w is not None, "congruence-accepted solution failed recovery"
        return yes("pell-orbit", w, f"σ^{k} applied to class representative {seed}")
    return yes("pell-orbit", (x, y), f"σ^{k} applied to class representative {seed}")
