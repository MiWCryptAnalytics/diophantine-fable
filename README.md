# diophantine-fable

*A working expedition against Smale's 5th problem.*

## The quest

On 2026-07-19 it was reported that Smale's 16th problem — the Jacobian
Conjecture — had fallen: a degree-7 polynomial map ℂ³ → ℂ³ with Jacobian
determinant identically −2 that sends three distinct points to (−1/4, 0, 0).
Constant nonzero Jacobian, yet not injective. We re-verified the object
symbolically at this project's kickoff ([scripts/verify_jc_counterexample.py](scripts/verify_jc_counterexample.py));
the algebra is self-certifying, whatever its provenance.

The next morning, this repository was opened against a neighboring peak,
**Smale's 5th problem**:

> Can one decide whether a Diophantine equation f(x, y) = 0 (input f ∈ ℤ[u,v]
> of size s) has an integer solution in time 2^(s^c) — that is, in
> exponential time?

(Our first citation sweep corrected the problem statement itself: popular
renderings — including Wikipedia's — print a single-exponential bound
(2^s)^c, but Smale's paper asks for 2^(s^c), verified against the primary
source. The expedition's first casualty was its own epigraph; see
[notes/frontier.md](notes/frontier.md).)

This is a different kind of mountain. #16 could fall to one clever algebraic
object; #5 is a decidability-and-complexity question where **even plain
decidability** (Hilbert's 10th problem in two variables) is open. Nobody
resolves that in a weekend, and this repo does not pretend to. Instead it
mounts a two-track research program in which every phase produces standalone
value — and it documents the journey as it goes (see [notes/log.md](notes/log.md),
the beating heart of the project).

## Why this problem bites

- **A hardness floor with a twist.** Deciding ax² + by = c over the
  *naturals* is NP-complete (Manders–Adleman 1978); but over ℤ that same
  equation sits in NP ∩ coNP, and Lagarias (1979) proved all binary
  quadratics over ℤ are in NP. Whether two-variable H10 over ℤ is NP-hard
  at all is itself open — one of this program's Track B targets.
- **Witnesses are too big to exhibit.** The least solution of x² − 61y² = 1
  is (1766319049, 226153980); in general Pell fundamental solutions have
  ~2^Θ(√d) digits — *doubly* exponential in the input size. Any (2^s)^c
  algorithm must decide **without materializing solutions**.
- **Siegel's structure theorem.** An irreducible plane curve carries
  infinitely many integer points only if it has genus 0 and ≤ 2 places at
  infinity — those parts are Pell-like and tame. The entire difficulty is the
  finitely many "sporadic" integer points on everything else, i.e. *effective
  Siegel/Mordell* with single-exponential height bounds: a 90-year-old wall.
- **The gap in miniature.** For y² = x³ + k, Hall's conjecture predicts
  integral points polynomial in |k|; the *proven* (Baker-type) bounds are
  doubly exponential in log|k|. Closing any such gap **is** Smale-#5 progress.

## The two tracks

**Track A — prove.** Assemble the decidable strata with rigorous complexity
accounting (target theorem A1: inputs whose components are all genus 0 decide
in single-exponential time), tabulate the best proven height bounds per
family, and attack the smallest family where single-exponential is open.

**Track B — disprove.** Strengthen the hardness floor (implement and extend
the Manders–Adleman reduction), and hunt for families beyond Pell whose
minimal solutions are doubly exponential while their decision is *not*
trivially structural — barrier results against whole classes of algorithms.

Both tracks share one engine: the `smale5` package.

## The honesty discipline

The solver **never overclaims**. Every answer is one of:

- `YES` — with a verified witness, or a certified symbolic solution when the
  witness is astronomically large (a Pell orbit index is a proof too);
- `NO` — with a finite, re-checkable certificate: a modulus, a sign argument,
  a completed orbit scan, an unconditional PARI Thue list;
- `UNDECIDED` — with the exact bound that was exhausted. This is the honest
  frontier, visible in code: the pipeline *confesses* on y² = x³ + 7, whose
  classical unsolvability proof is global, not a congruence.

A small trophy from day one: **x³ − 2y³ = 19** passes every prime-power
congruence filter up to 81, yet PARI certifies it unsolvable — the smallest
member of our zoo where NO lives strictly beyond local reasons.

## What works today

| Stratum | Method | Verdict quality |
|---|---|---|
| linear | Bézout / extended gcd | complete |
| all binary quadratics | ellipse window · parabola congruence classes · split-form divisors · **LMM/PQa class search + Pell orbit walk mod M** | complete (caps confessed) |
| rational-function graphs (deg 1 in x or y) | pseudo-division + crossover window | complete |
| deg-2 fibers, constant lead, square-class ≤ 2 | discriminant modulo squares → conic + divisibility as an orbit congruence | complete (caps confessed) |
| Thue F(x,y) = m, deg ≥ 3 | PARI `thueinit(·,1)` — unconditional | complete |
| univariate components | rational root theorem | complete |
| everything else | obstructions (ℝ, prime powers ≤ 81) + bounded search | YES or honest UNDECIDED |

Plus: Smale size measure s(f), factorization into components, and a Siegel
classifier that only claims a genus it can certify.

## Layout

- `smale5/` — the package: `poly.py`, `classify.py`, `solvers/`, `families/`.
- `notes/log.md` — **the research log**: decisions, dead ends, small
  discoveries, next steps. Updated every session; start reading here.
- `notes/frontier.md` — the claim map, each claim tagged
  machine-verified / cited / pending-verification.
- `scripts/` — archival verifications. `tests/` — 29 golden tests against
  classical results (Pell fundamental solutions, CF period parity, Thue
  certifications, honest-UNDECIDED expectations).

## Setup

```sh
python3 -m venv .venv
.venv/bin/pip install -e ".[dev,pari]"
.venv/bin/python -m pytest -q
.venv/bin/python -m smale5 "x^2 - 61*y^2 - 1"
```

PARI/GP (via cypari2) enables the unconditional Thue decisions; without it
the toolkit degrades to sympy-only and reports wider `UNDECIDED` ranges.

## First summit (2026-07-22)

The expedition's first theorem-shaped result is drafted and twice
adversarially refereed: **pure cubic Thue equations x³ − d·y³ = m decide,
with full solution lists, in deterministic, unconditional 2^(O(s)) time**
— a worst-case bound absent from the literature (closest prior: Smart,
ANTS-II 1996). Manuscript: [papers/cubic-thue-exp.md](papers/cubic-thue-exp.md);
the story, including the three traps it survived, is in
[notes/log.md](notes/log.md).

## Roadmap

- **Phase 2 (Track A):** genus-0 parametrization stratum + the A1
  complexity write-up; per-family table of best proven height bounds.
- **Phase 3 (Track B):** Manders–Adleman reduction as verified code;
  extremal minimal-solution growth measurements over `families/`.
- **Phase 4:** synthesis — exactly what stands between these results and
  Smale #5, as sharpened sub-conjectures.

*Expedition journal in [notes/log.md](notes/log.md). Onward.*
