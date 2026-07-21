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

## 2026-07-20 — panel resurrected; the dense size lands in code

- The first interrogation run died of token exhaustion — all four hostile
  reviewers hit the session usage limit mid-audit, returning zero verdicts
  (a fitting hazard for an expedition: the panel starved on the glacier).
  Relaunched from the saved script after the quota reset.
- Folded the citation pass's last correction into code: `smale5.poly.size`
  now implements Smale's **dense** convention (every exponent slot ≤ d
  contributes ≥ 1). Pell-61's size drops 13 → 11; x⁵ − 1 costs all 21 slots.
  Sparse and dense are polynomially related, so 2^(s^c) membership is
  convention-independent — noted in A1.md, and the growth-records CSV was
  regenerated under the new measure.

## 2026-07-21 — the interrogation panel reports: the math held, the code bled

Four hostile reviewers, ~490k tokens, ~450,000 oracle-checked decisions.
Headline: **zero wrong verdicts anywhere** — the LMM reviewer alone threw
420k adversarial cases (including a direct class-completeness attack and a
sympy cross-check of every NO), the quadratic reviewer 12,300 more, the
pipeline reviewer 10,141 — the mathematics of the solver stack survived
everything. But the panel earned its keep with four real defects:

1. **CRITICAL — classifier unsound direction** (break-pipeline). My genus
   formula used `sqf_part(disc)` — the *radical* — where the field
   ℚ(x)(√D) is determined by D *modulo squares*: even-multiplicity factors
   must vanish, not survive once. So y² = 2x⁴ + x² (square class 2x²+1,
   genus 0, infinite Pell family (x_k, x_k·s_k)) was certified genus 1 and
   labeled "finite" — falsifying the classifier docstring's own safety
   claim. Fixed via `sqf_list` keeping odd-multiplicity factors only;
   regression family in tests.
2. **CRITICAL — crash on the showcase path** (audit-a1). `len(str(t))`
   exceeds CPython's 4300-digit int→str limit for Δ ≳ 10⁹ — the crash hit
   *precisely the astronomically-large-witness inputs the certificate path
   was built for*. Fixed with bit_length arithmetic plus a safe formatter
   for all certificate/detail rendering (huge witnesses print as
   "<int ~N digits>").
3. **MAJOR — the one uncapped loop** (break-quadratic + break-pipeline,
   independently). `cf_fundamental` walked the CF period with no budget:
   Δ ≈ 2×10²³ conics hang for ~10¹¹ steps; 81 of 150 big-coefficient fuzz
   conics hit it. Now step-capped with an UNDECIDED confession
   ("pell-cf"), restoring the never-hang contract.
4. **MAJOR — A1's theorem-to-code sentence was false** (audit-a1). The caps
   are constants, so the pipeline is a (sound, honest) *truncation* of the
   analyzed algorithm — in-scope inputs went UNDECIDED at s = 26. A1
   rephrased truthfully; size-scaled budgets queued as follow-up. Two A1
   lemmas also corrected: the PQa run bound is pre-period O(log|m|) + the
   reduced-class cycle (not O(ℓ(√Δ))), and the completeness argument now
   states honestly that conjugation lands outside ⟨σ⟩×{±1} and is covered
   by the four-variant seeding.

Also: parse() no longer leaks raw sympy exceptions ("x/y", "x^x" → clean
ValueError), and the recover-hook API hazard the LMM reviewer flagged is
closed (rejections now yield honest UNDECIDED instead of silent-YES/assert).
42 tests green. The ledger for the day: adversarial review found nothing
wrong with the *theorems* and four things wrong with the *artifact* —
exactly the asymmetry you want to discover before anyone else does.

- **G1's first slice.** New solver `smale5/solvers/graph.py` decides every
  component of degree 1 in one variable — the graphs y = −B(x)/A(x), any
  total degree — completely and in single-exponential time. The argument is
  Runge in miniature: A(x) | B(x) forces A(x) | R̂(x) for the integer
  pseudo-remainder ℓB = Q̂A + R̂ with deg R̂ < deg A, so either x is an
  integer root of R̂ or |A(x)| ≤ |R̂(x)| pins |x| inside an explicit window
  ≤ 2 + Σ|coeffs|. Exact-division and constant-denominator branches reduce
  to single congruences (infinite families detected, not searched).
- Theorem A1-v1 now reads: degree ≤ 2, OR univariate, OR degree 1 in one
  variable. First strictly-new coverage beyond the Lagarias stratum. A
  pleasing NO exemplar: y·(x²+3) = x³ + 2 — no congruence obstruction, the
  window argument alone certifies it. 38 tests green.

- **Second workflow: `interrogate-findings`.** The citation pass checks the
  literature; nobody had yet attacked *us*. Four hostile reviewers now
  running: `break-lmm` (independent brute-force decider fuzzing D ≤ 300,
  |N| ≤ 400 plus squareful-N edge cases), `break-quadratic` (5000+ fuzzed
  conics vs a search oracle across every Δ branch), `audit-a1` (referee
  hunting for hidden doubly-exponential steps — sqrt_mod root counts over
  squareful moduli, PQa pre-period claims, orbit seed coverage), and
  `break-pipeline` (end-to-end fuzz + classifier soundness against
  provably-infinite families). Verdicts feed regression tests.
## 2026-07-20 — the citation machine reports: our epigraph was wrong

Nine verifiers, 236 tool calls, ~463k tokens: six claims confirmed (with
sharpenings), three corrected — and the corrections cut deep. In order of
pain:

1. **The problem statement itself.** Smale asks for time **2^(s^c)** —
   exponential time proper — not the single-exponential (2^s)^c we (and
   Wikipedia, whose rendering conflicts with the primary PDF and with
   Lagarias's quotation of the AMS reprint) had. The size measure is dense:
   every exponent slot ≤ d contributes, so s ≥ ~(d+1)(d+2)/2. Consequences:
   A1's 2^{O(s)} is comfortably *stronger* than Smale's budget, and his
   Height Bound Hypothesis frames the NP route for positive genus.
2. **The Thue sting.** Bugeaud–Győry bounds are polynomial in coefficient
   *magnitude* — exponential in bit-size — so even fixed-degree-3 Thue is
   not known decidable in 2^(s^c) via height bounds. G2 rewritten: the open
   route is compact-representation decision (Pell-style
   decide-without-exhibit, one rung up). This kills our hoped-for A1-v2
   shortcut and replaces it with a better question.
3. **The hardness floor was mis-scoped.** Manders–Adleman NP-completeness is
   an ℕ-statement; the ℤ-variant is NP ∩ coNP (quadratic residuosity — and
   the verifier caught an *error in the authors' own 1978 tech report*
   claiming poly-time via Jacobi symbols). Lagarias 1979: binary quadratics
   over ℤ in NP and in 2^{O(L)} — so our A1 deg-2 stratum is his theorem,
   now credited. New Track B question: is two-variable H10 over ℤ NP-hard
   at all?
4. **Attribution fixes.** The 9-unknowns theorem is Matiyasevich's, written
   up by Jones 1982 (we had it backwards); Siegel 1929 appeared in the
   Abhandlungen, not the Sitzungsberichte (Wikipedia again).
5. **Post-cutoff intelligence.** Alpöge–Lawrence, *Conditional algorithmic
   Mordell* (2024: algorithm for C(K) conditional on Hodge+Tate+Fontaine–
   Mazur); Garcia-Fritz–Pasten 2025 (unconditional effective heights, enough
   automorphisms); Bennett–Ghadermarzi solved Mordell for |k| ≤ 10⁷ (2015 —
   our GPZ 10⁴ figure was stale); Elkies' record Hall ratio 46.6; H10
   undecidable over rings of integers of all number fields (2024–25); ℤ[i]
   in 18 unknowns (2026). Two-variable H10: still open in both directions.

`frontier.md` rewritten with citations ([P] → [C] throughout); README's
epigraph corrected; A1.md re-budgeted and re-credited. All 73 citations
archived in `notes/citations/2026-07-20-frontier-verification.json`. House
rule from here on: primary sources only.

- **Hall-ratio sweep** (`experiments/hall_ratios.py`, 3.9s to x = 10⁷):
  rediscovered the classical extremal point from scratch — x = 5234,
  y = 378661, x³ − y² = −17, ratio √x/|k| ≈ 4.2557 — and it is one of only
  THREE records up to ten million. The sparsity is the finding: sporadic
  points on Mordell equations are not just hard to bound, they are freakishly
  rare, which is why nature gives us so little data to fit G3 against
  (`experiments/data/hall_records.csv`).
