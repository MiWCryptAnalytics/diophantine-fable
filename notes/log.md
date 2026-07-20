# Research log

## 2026-07-20 — kickoff

- **Context**: the day after the reported disproof of the Jacobian Conjecture
  (Smale #16). Independently re-verified here by full symbolic expansion
  (`scripts/verify_jc_counterexample.py`): the degree-7 map ℂ³→ℂ³ has Jacobian
  determinant ≡ −2 and identifies (0,0,−1/4), (1,−3/2,13/2), (−1,3/2,13/2)
  — constant nonzero Jacobian, non-injective. The object is self-certifying
  regardless of the report's provenance.
- **Target**: Smale #5 — decide f(x,y)=0 over ℤ² in time (2^s)^c. Two-track
  program per the approved plan (see `notes/frontier.md` for the claim map).
- **Built today**: venv (`.venv`, Python 3.14, sympy 1.14, cypari2 against
  system PARI 2.17.4); `smale5` package — parser + Smale size measure, Siegel
  classification (certified-genus-only honesty), solver pipeline: real/local
  obstructions, linear (Bézout), the complete binary-quadratic layer (rect
  hyperbola divisors, parabola congruence classes, ellipse window scan, split
  hyperbola, and the Pell orbit walk that decides indefinite conics via
  residue cycles *without materializing solutions*), PARI-certified Thue
  decisions, bounded search with explicit bounds. 29 golden tests green.
- **Nice find for the test suite**: x³ − 2y³ = 19 passes every prime-power
  filter ≤ 81 yet PARI certifies it unsolvable — a minimal example of "the NO
  lives beyond congruences".
- **Environment gotchas**: all Python via `.venv/bin/python` (user
  requirement); never call `gp` (shell-aliased to `git push` on this machine)
  — use `/usr/bin/gp` or cypari2.

### Open next steps
- Fold in the literature agent's status report; citation-verify
  `notes/frontier.md` (multi-agent workflow authorized).
- Track A theorem target A1: uniform single-exponential complexity write-up
  for inputs with no positive-genus components (the quadratic layer built
  today is most of the machinery; needs the genus-0 parametrization stratum
  and the complexity accounting).
- Track B: implement Manders–Adleman reduction; extremal growth measurements
  over `families/`.
