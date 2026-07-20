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

## 2026-07-20 — publication prep

- Rewrote `README.md` as the quest document: the JC backstory, why #5 is a
  different kind of mountain (NP-hard floor; doubly-exponential Pell
  witnesses; Siegel structure; the Hall-vs-Baker gap), the two tracks, the
  honesty discipline, and the day-one trophies (x³−2y³=19; the honest
  UNDECIDED on y²=x³+7).
- Standing rule adopted at the user's request: **every session appends to
  this log** — the narrative of decisions and discoveries is a first-class
  deliverable, not an afterthought.
- Literature agent still out; frontier claims remain [P] until it reports
  and the citation-verification pass runs.

## 2026-07-20 — the Nagell trap, the LMM fix, and first growth data

- **A real bug in our complexity story, caught by writing it down.** While
  drafting the accounting for theorem target A1, noticed that the
  generalized-Pell representative search used Nagell's window
  y ≤ u·√|N|/√(2(t∓1)) — and the fundamental unit u has *exponentially many
  digits* in s. The scan was doubly exponential, silently betraying the
  single-exponential thesis of the whole quadratic layer. Moral for the
  eventual A1 write-up: complexity claims must be audited per bound, not per
  "we have an algorithm".
- **Fix: the LMM/PQa method.** Class representatives now come from
  continued-fraction expansions of (z + √D)/|m| over square divisors f² | N
  and square roots z² ≡ D (mod |m|), with every candidate verified by direct
  big-integer arithmetic (sidestepping the literature's sign conventions).
  Representative search is now period-bounded — single-exponential, no u
  anywhere. Validated three ways: 400-case brute-force agreement, exact
  solvability match against the old Nagell scan where both apply, and
  hand-worked PQa runs (x² − 2y² = 7: the z = ±3 expansions produce (−3, 1)
  and (3, 1), as computed on paper before coding).
- **Lenstra's monster, tamed.** d = 1000099: our CF computes the fundamental
  t with **1128 digits** (computed here, not quoted); the negative Pell
  equation is unsolvable (even period); x² − 1000099y² = N decides instantly
  for sample N. Search-based methods are hopeless here by construction —
  this is the single-exponential claim made executable.
- **First Track B data** (`experiments/pell_growth.py`, 0.1s for d ≤ 20000):
  33 record-setting d; digits(t) climbs 10 → 278 while s(f) goes 13 → 22,
  with digits/√d rising ≈1.3 → ≈2.2. Empirically log t ≈ 2√d, i.e. witness
  magnitude 2^(2^Θ(s)) — the doubly-exponential envelope as machine data
  (`experiments/data/pell_records.csv`).
- **Program note:** the pre-plan literature agent was stopped by the user;
  the frontier [P] tags stay pending until a citation pass is green-lit.

## 2026-07-20 — A1 drafted; citation workflow in flight

- **`notes/A1.md` v1.** The theorem we can actually prove today: components
  of degree ≤ 2 or univariate ⇒ decidable in 2^{O(s)}, with the full cost
  accounting per stratum (CF unit, LMM, orbit walk each bounded 2^{O(s)};
  the write-up explicitly marks where log t is *stored* — fine — versus
  where it must never enter a *bound* — the Nagell trap, institutionalized
  as a lesson).
- **The gap ladder is the real yield.** G1: genus-0/≤2-places/deg ≥ 3 via
  Sendra–Winkler parametrization (next implementation milestone). G2: the
  program's first crisp open question — *is {f : all components genus 0}
  decidable in 2^{O(s)} uniformly in the degree?* — fixed degree likely
  follows from Thue bounds (awaiting citation shapes). G3: effective Siegel,
  the wall; single-exp effective Siegel ⇒ Smale #5 positive, converse not
  claimed.
- **Citation workflow launched** (nine adversarial verifiers, one per
  frontier claim: Smale's formulation, Manders–Adleman, Siegel 1929, Baker
  bound shapes, effective-Mordell routes, Hall/GPZ, H10 variable counts,
  PARI thueinit flag semantics, Pell regulator growth). Results will
  reconcile the [P] tags in `frontier.md`.
