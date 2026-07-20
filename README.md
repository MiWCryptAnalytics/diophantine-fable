# diophantine-fable

A research toolkit for **Smale's 5th problem**: given f ∈ ℤ[u,v] of input size s, decide
whether f(x,y) = 0 has an integer solution in single-exponential time (2^s)^c.
Even plain decidability (two-variable Hilbert's 10th) is open; this repo maps the frontier
and builds the decision machinery for everything that *is* decidable.

Core discipline: the solver **never overclaims**. Every answer is one of

- `YES` with a verified witness (or a certified solution family),
- `NO` with a finite, re-checkable certificate (a modulus, a sign argument, a
  complete Pell orbit scan, an unconditional PARI Thue result),
- `UNDECIDED` with the exact bound that was exhausted — this is the honest frontier.

## Layout

- `smale5/` — the package: parsing/size (`poly.py`), Siegel classification
  (`classify.py`), solver pipeline (`solvers/`), test families (`families/`).
- `notes/` — research log and the citation-annotated frontier map.
- `scripts/` — archival verifications (including the Jacobian Conjecture
  counterexample check that motivated this project).
- `tests/` — golden tests against classical results.

## Setup

```sh
python3 -m venv .venv
.venv/bin/pip install -e ".[dev,pari]"
.venv/bin/python -m pytest -q
.venv/bin/python -m smale5 "x^2 - 61*y^2 - 1"
```

PARI/GP (via cypari2) enables unconditional Thue-equation decisions; without it the
toolkit degrades to sympy-only and reports wider `UNDECIDED` ranges.
