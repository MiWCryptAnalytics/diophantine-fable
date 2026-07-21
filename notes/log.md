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

## 2026-07-20 — the interrogation panel, and Hall's needle in the haystack

- **Second workflow: `interrogate-findings`.** The citation pass checks the
  literature; nobody had yet attacked *us*. Four hostile reviewers now
  running: `break-lmm` (independent brute-force decider fuzzing D ≤ 300,
  |N| ≤ 400 plus squareful-N edge cases), `break-quadratic` (5000+ fuzzed
  conics vs a search oracle across every Δ branch), `audit-a1` (referee
  hunting for hidden doubly-exponential steps — sqrt_mod root counts over
  squareful moduli, PQa pre-period claims, orbit seed coverage), and
  `break-pipeline` (end-to-end fuzz + classifier soundness against
  provably-infinite families). Verdicts feed regression tests.
- **Hall-ratio sweep** (`experiments/hall_ratios.py`, 3.9s to x = 10⁷):
  rediscovered the classical extremal point from scratch — x = 5234,
  y = 378661, x³ − y² = −17, ratio √x/|k| ≈ 4.2557 — and it is one of only
  THREE records up to ten million. The sparsity is the finding: sporadic
  points on Mordell equations are not just hard to bound, they are freakishly
  rare, which is why nature gives us so little data to fit G3 against
  (`experiments/data/hall_records.csv`).

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

## 2026-07-20 — theorem A1-v1 grows a clause: rational-function graphs

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

## 2026-07-21 — clause (iv): the panel's counterexample family, decided

- **Budget schedules land** (`smale5/budget.py`): the caps now grow like
  2^(s−21) up to a hard interactivity ceiling, closing the panel's fourth
  finding properly — its concrete s = 26 parabola gap is a regression test
  that decides (NO: −7 is not a QR mod 13, and 13 | 300001). A1's
  theorem-to-code paragraph rewritten to match reality.
- **The ExtraCong refactor**: the whole quadratic layer now accepts an
  extra congruence accept(x mod K, y mod K) with completeness preserved on
  every branch — finite scans filter, line families walk one full residue
  cycle, and the Pell path enlarges its walk modulus to |2aΔ|·K. This is
  the plumbing that lets higher strata *ride* the conic machinery.
- **New stratum, A1 clause (iv)** (`smale5/solvers/deg2fiber.py`):
  components a·y² + B(x)y + C(x) with constant lead whose discriminant has
  square-class of degree ≤ 2. Complete the square: (2ay+B)² = E(x)²·Q₀(x);
  off E's integer roots, w = (2ay+B)/E is forced integral with w² = Q₀(x)
  — a conic — plus the fixed-modulus divisibility 2a | E(x)w − B(x). The
  panel's y² = 2x⁴ + x² family is now *decided*, not merely correctly
  classified. Flagship pair: (y+x+7)² = (x²+30)²(2x²+1) → YES via a Pell
  conic point with the congruence riding along (E rootless, so no
  shortcut); (3y+1)² = x²(2x²+1) → **NO certified by a complete orbit scan
  mod 576** — on the whole Pell orbit of w²−2x²=1, x·w ≡ 0 (mod 3), never
  ≡ 1. Mordell equations (square-class degree 3) honestly return None and
  fall through. 50 tests green, including a 40-case planted fuzz against
  the search oracle.
- **The journal itself needed a bugfix**: anchor-based edits had eaten two
  section headings and scrambled the chronology — restored from the file
  and reordered. Even the log gets the honesty discipline.
- Next targets unchanged: G1 general parametrization; A1-v2
  compact-representation cubic Thue.

## 2026-07-21 — the Pell walk climbs a rung: cubic Thue via unit orbits

The best session yet. The citation pass's sharpest sting was that even
degree-3 Thue equations aren't known decidable in exponential time — height
bounds are hopeless. Today the program answered with a *reduction*:

- **The idea.** For x³ − d·y³ = m, K = ℚ(∛d) is a complex cubic field:
  unit rank 1. A solution is γ = x − y·α of norm m; all norm-m elements are
  (class rep)·(±ε^k); and "being of Thue shape" is the **vanishing of the
  α²-coordinate of γ·ε^k** — a zero of an order-3 linear recurrence with
  dominant root. Deciding that is a Skolem instance of the classically
  decidable kind, and the modulus gap (3/2)·regulator per step means the
  last vanishing index should be O(1 + log|m|/R).
- **The prototype** (`experiments/cubic_orbit_prototype.py`): class reps
  via bnfisintnorm, walk the unit orbit, harvest coordinate-vanishing
  points. Validated against PARI's certified thue on 14 fields × 80 values
  of m: **1120/1120 exact solution-set agreements, zero mismatches, 2.5
  seconds — and the maximum vanishing index across the entire grid is 3.**
  The window-bound conjecture is now data-backed; its proof plan is
  elementary embedding inequalities, *no linear forms in logarithms* —
  which is the whole point.
- **The envelope, one rung up** (`experiments/thue_unit_growth.py`): the
  fundamental unit of ℚ(∛d) reaches 1593-digit coefficients by s = 20
  (Pell managed ~145 at the same size), every record bnfcertify'd
  unconditionally. Search is deader than ever; the walk doesn't care —
  it materializes at most ε^±4.
- **Where the wall moved** (`notes/A1v2-cubic-thue.md`): cubic Thue in EXP
  now *follows from* (a) the window bound (elementary, conjectured, max
  observed 3) and (b) certified bnf data in exponential time — the
  compact-representations kernel where Buchmann-school methods live. The
  G2 wall transformed from "height bounds are doubly exponential" into a
  concrete computational-algebraic-number-theory question. Totally real
  cubics (rank 2, no dominant root) deferred with eyes open.
- Next: prove the window bound for pure cubics; citation pass on Skolem
  order-3 attribution and certified-bnfinit complexity; then promote the
  prototype into `smale5/solvers/` as A1 clause (v).

## 2026-07-21 — where Baker hides: a self-caught overclaim

Sat down to write the window-bound proof with explicit constants and
promptly refuted my own headline. The elementary dominant-root argument is
real — but it only bounds the **positive** orbit direction (small
solutions). For k ≪ 0, the complex pair dominates, and exact vanishing of
the α²-coordinate demands |cos(φ + k·arg μ)| ≲ λ^{3k/2}: the unit's angle
must approximate π/2 (mod π) *super-exponentially well*. Bounding the last
such k is an inhomogeneous **linear form in logarithms** — Baker was never
avoided, only localized into a single inequality. Fittingly, the big
solutions (|y| large, real embedding tiny) live exactly on that side; an
elementary bound there would have made Thue effective without Baker, which
should have smelled wrong a session earlier.

The ledger is net positive, though:

- **The reduction is now unconditional modulo bnf** — better than the
  conjectural version. Both window directions are effectively bounded
  (elementary + one Baker–Wüstholz inequality), each 2^{O(s)}, each orbit
  step 2^{O(s)} bit-ops: *pure-cubic Thue in EXP follows from certified
  unit/class data in EXP*, full stop. The conjecture is demoted to what it
  always was: an empirical observation (max index 3) about how tiny the
  windows are in practice.
- **Priority caveat recorded**: unit-orbit + one Baker inequality is
  morally the classical Tzanakis–de Weger / Bilu–Hanrot pipeline. Our
  plausible contribution is the explicit EXP-modulo-bnf accounting and the
  empirical window sharpness — flagged for verification, not assumed.
- **Second citation workflow launched** (five verifiers): Skolem order-3
  attribution (MST/Vereshchagin), certified-bnf complexity, the minimal
  complex-cubic regulator (x³−x−1, R ≈ 0.281), bnfisintnorm's exact
  semantics (completeness/GRH), and — the one that matters most — whether
  "Thue in EXP modulo bnf" is already stated in the literature. An honest
  "nobody states this" would mark our first genuinely publishable
  increment; an honest "it's in Bilu–Hanrot §5" would save us from
  embarrassment. Either answer is a win.

Moral for the log's collection: *the negative direction of an orbit is
where the analysis gets honest.* Twice now (Nagell's window, the elementary
window) the trap was an argument that worked beautifully in the direction
where nothing interesting lives.

## 2026-07-21 — the citation pass upgrades A1-v2 to a theorem program

Five verifiers, 176 tool calls, and every verdict moved us forward:

- **The "modulo bnf" hypothesis is dischargeable.** For fixed degree,
  certified class group + units are unconditionally computable in
  deterministic |Δ|^(1/2+o(1)) = 2^(O(s)) (Lenstra 1992 Thm 5.5; Schoof
  2008 §11, Arakelov class group; units in compact representation). The
  reduction's hypothesis was never a wall — it was already proven.
- **The theorem is a citable gap.** Nobody states worst-case
  "fixed-degree Thue in EXP" — not Tzanakis–de Weger, not Bilu–Hanrot,
  not the books. Closest prior: Smart, ANTS-II 1996 ("we seem to be a
  long way off from a 'good' algorithm"), a per-method practical
  estimate. So the assembly target — **pure-cubic Thue decidable in
  2^(O(s)) unconditionally** — is real, new-as-stated, and must be
  positioned against Smart. Three bookkeeping-hard items remain:
  norm-equation step complexity, rep unit-reduction, explicit negative-
  window constants (Min Sha 2019 supplies explicit dominant-root
  thresholds — the exact missing tool).
- **Corrections taken on the chin**: "Skolem meets Bayes" does not exist
  (phantom memory; the real papers are Skolem-Meets-Schanuel and
  Skolem-Meets-Bateman–Horn); the minimal-regulator attribution is
  Astudillo–Díaz y Díaz–Friedman 2016, not Artin; bnfisintnorm reps are
  NOT size-reduced (the docs' own example overflows 100 GB expanded —
  unit-reduce before walking) and are GRH-conditional without
  bnfcertify. The prototype's completeness survives: it walks ⟨±ε⟩ ⊇
  the norm-positive unit orbits PARI quotients by.
- 57 citations archived (`notes/citations/2026-07-21-a1v2-verification
  .json`).

## 2026-07-22 — the errata note drafted, machine-checked

- `notes/AM-errata.md`: the citable-gap-#3 note in paper shape — E1 (the
  misprinted trivial set), E2 (the Thm 2.4.1 bound bug: counterexample
  ⟨27, 1343⟩ and the 3^k > 1+Σ|aᵢ| repair), E3/E4 (minor), and M (the
  AKS modernization with the faithful/unfaithful bookkeeping, stated as
  the theorem we would defend). `scripts/verify_am_erratum.py` makes
  E1/E2 executable: the false YES (27·(−3)+2)·(−17) = 1343 and its
  closure at k = 3 are asserted in-repo. TODO list includes the courtesy
  step: these are living authors' early results — contact before
  posting.
- Census: s = 12 grinding; 805 specimens logged already beyond s ≤ 11.

## 2026-07-22 — the adversarial series: a death, a resurrection, and errata

Ran the adversarial agents in series (quota discipline), interpreting
between. Two agents sufficed for the most consequential day of Track B:

- **Agent 1 (the STOC-1977 reader) killed our candidate reduction in one
  line**: (ax+1)y = c is solvable over ℤ by x = 0, y = c — always. The
  trivial divisor d = 1 sits in every congruence class; no CRT
  rigidification can excise it. The proposal was dead on arrival — and
  the same agent then found that **the intended conclusion is 48-year-old
  prior art we (and the landscape survey) had missed**: Adleman–Manders
  themselves proved x² − a²y² = c and x(x+ay) = c γ-complete and random
  complete over ℤ (ERL M78/30 §2.3, "Reductions that Lie" FOCS 1979).
- **Agent 2 (hostile referee) verified everything against page scans**,
  guard-railed the citation discipline (printed theorems: unfaithful
  completeness unconditionally, faithful only under ERH; the AKS
  substitution — certification consumes no nondeterminism — makes the
  faithful version unconditional), and confirmed the bug Agent 1 found in
  the memo's Thm 2.4.1 with an explicit false-YES witness: ⟨27, 1343⟩,
  where (27·(−3)+2)·(−17) = 1343 rides the negative divisor −79 ≡ 2
  (mod 27) that the printed bound fails to exclude. Repair: 3^k > 1+Σ|aᵢ|.
  Two further errata surfaced (a sign slip, a ≤/≥ typo). A foundational
  1978 memo, debugged by the expedition.
- **The frontier corrects, hard**: two-variable H10 over ℤ IS hard under
  randomized reductions — **L ∈ P ⟹ NP = coNP** — and has been since
  1978. Our "no hardness known" (inherited from the landscape survey,
  which missed §2.3 of the very memo it cited) is struck. The real Track
  B target is now crisp: **deterministic NP-hardness = Adleman–McCurley
  O33a**, open since 1979. And the structural poetry: the hardness
  anchors live in our split-hyperbola stratum — the factoring-shaped
  corner of the quadratic layer — while Baker's decidability conjecture
  plus this hardness sketches exactly the "decidable but not in P"
  picture Smale's problem list anticipates.
- Citable-gap ledger grows to three: cubic-Thue-EXP, HBH⟹NP, and now
  **the A–M errata note** (misprinted theorems, the bound bug +
  counterexample + repair, the AKS modernization bookkeeping).

## 2026-07-21 — the Census names the frontier; the war council's first find

- **The smallest open problems have addresses now.** The Census cleared
  s ≤ 9 completely (14,802 polynomials, zero escapes) and then hit the
  wall at **s = 10: 76 undecided of 43,439** — and triage says **75 of
  the 76 are certified genus-1 curves**. The elliptic wall is empirically
  exactly where the theory put it: decidable in principle (Baker–Coates),
  not yet in the toolkit. Specimen zero of the expedition:
  x³ − x² + xy² + y² + 1 = 0. And one glorious outlier — a cubic the
  classifier can't even pin (x³ − x²y − x² − xy² + xy + x + y³ + y + 1),
  the smallest mystery object in the census. s = 11 adds 2,755 more;
  s = 12 still grinding in the background.
- **The war council starved again** (three attackers + skeptic hit the
  session limit — second panel casualty of the expedition; resumption
  queued), but the landscape surveyor returned heavy: **Baker conjectured
  two-variable H10 over ℤ is decidable** (Jones 1981 §5); nobody has ever
  claimed NP-hardness; Tung's ∀∃ class is coNP-complete via covering
  congruences; **our DIVIS problem is in NP** (two proofs — one is our
  own window bound, one via 2025 one-parametric Presburger — and nobody
  has studied its hardness); and the single most promising pathway found:
  **Adleman–Manders' γ-complete linear divisibility problem transfers to
  the one equation (ax+1)y = c over ℤ if a CRT sign-rigidification
  closes the ± gap** — randomized NP-hardness of two-variable H10 as a
  concrete target, colliding productively with Baker's decidability
  conjecture. All agent-reported citations flagged [P] pending our own
  verification (`notes/trackB-hardness.md`).
- **A second citable-gap theorem target logged**: "HBH ⟹ two-variable
  H10 ∈ NP" — Smale posed the hypothesis, nobody assembled the theorem;
  the pieces (Silverman's refined Siegel + Lagarias certificates + HBH)
  are all on our bench. Also: Silverman TCS 2000 gives a sharper
  infinitude criterion than classify.py encodes — upgrade queued.

## 2026-07-21 — the Census and the war council

Two creative engines launched while the A1-v2 citations verify:

- **The Census** (`experiments/census.py`, running in background): enumerate
  *every* primitive f ∈ ℤ[x,y] of dense size s ≤ 12 (canonicalized under
  the 16-element symmetry group), decide each with the full pipeline, and
  find **the smallest open Diophantine problems in existence** — the
  literal specimens where the frontier of Smale #5 begins. Doubles as a
  fuzzer (crashes and timeouts are recorded as specimens too) and yields
  the toolkit's first honest coverage metric. Early returns: **complete
  coverage through s = 9** — all 14,802 canonical polynomials decide, zero
  UNDECIDED, zero crashes. The first escapee is expected around s = 11–12
  (Mordell shapes need 10 slots plus constant bits).
- **The hardness attack panel** (workflow, 4 attackers + hostile skeptic):
  a genuine assault on our own Track B question — *is two-variable H10
  over ℤ NP-hard?* Angles: (1) range gadgets (can poly-size curves force
  x ∈ [0, N] while leaving y usable — the variable-budget wall made
  precise); (2) a brand-new problem our graph stratum generated:
  **DIVIS = {(A,B) : ∃x ∈ ℤ, A(x) | B(x)}** — NP-hard via CRT/knapsack
  selection, or in NP via compressed witnesses?; (3) the barrier
  direction: a Siegel/Bézout/Bombieri–Pila argument that poly-size range
  gadgets *cannot exist* in two variables (windows of consecutive integers
  force linear components — a theorem-shaped dichotomy worth having
  regardless); (4) the literature landscape (has anyone placed 2-var H10
  in the hardness hierarchy at all? has DIVIS been studied?). The skeptic
  pass tries to break whatever the attackers claim before we believe it.

## 2026-07-21 — Smale's Height Bound Hypothesis, first empirics

`experiments/mordell_min_height.py`: sweep x ≤ 10⁶ harvesting the
minimal-height integral point of y² = x³ + k for every |k| ≤ 2000. HBH is
what would put the positive-genus stratum in NP, and within the resolved
range it looks comfortable: the record ratio log(height)/log|k| is only
**2.38** (k = −366, minimal point (11815, 1284253) — a seven-digit height
for a three-digit k, and still tame). 1388 of 4000 k-values resolve inside
the sweep; the honest caveat is censoring — 2612 don't, and the known
monsters live there (k = −1090's minimal point has x ≈ 2.8×10⁷, invisible
below 10⁶). The stress list is exactly where a follow-up should point a
bigger sweep or the Bennett–Ghadermarzi tables
(`experiments/data/mordell_min_heights.csv`).
