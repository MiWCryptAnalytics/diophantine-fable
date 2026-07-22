# Research log

## 2026-07-22 — paper two absorbs its critique; the commutative gift

The outside critique of paper two accepted the architecture ("the
vacuity remark is the crown jewel"; "sums of compacts are not compact
... is the best sentence in the draft") and contributed four fixes, all
applied: (1) **the commutative advantage** — a genuine strengthening I
should have seen myself: the matrices M_{βᵢ} all lie in ℚ[M_α] ≅ K, so
CVP's ABP face is COMMUTATIVE bounded-width PIT, a far better-studied
class than generic non-commutative words — stated explicitly in §4.4;
(2) the Arakelov-pinning proof now clears denominators first (the HNF
intersection needs an integral ideal); (3) the ∃·coRP = MA chain stated
precisely in §3; (4) the Matveev-constant degradation in k is named as
the reason the O(1)-rank restriction in the bounded fragment is
load-bearing. The critique's third ask — strip the honesty flags — is
DEFERRED on principle: flags come off when the debts are paid (the
Thiel-format cubic size-bound pinpoint), not before; recorded as an
explicit pre-submission item in the status ledger.

## 2026-07-22 — paper two exists; paper one reaches submission polish

- **`papers/cubic-thue-certificates.md`** (669 lines): the sequel —
  certificate collapse, the MA proposition with explicit prime-range
  write-up, CVP with its three faces (incl. the Arakelov-pinning lemma),
  the vacuity remark, the five-part impossibility ledger, the bounded-CVP
  positive fragment, four open problems. Its complexity-literature
  references need their own verification pass (flagged in its ledger).
- **Paper one, five review fixes applied** (the most useful outside pass
  yet): (1) Smart's primary text partially obtained — pp. 363–364
  verbatim via the publisher preview + the full Stroeker review; §1.2 now
  quotes the primary directly and the positioning rests only on verified
  content; (2) a genuine catch: the algorithm needed b from d = ab² and
  never said how — Step 1 now factors d by trial division, cost
  accounted; (3) §6.1 states the prototype runs under the empirical
  window conjecture, not the proven ~10¹⁷·H₁ log H₁ bound; (4) the
  review-process rhetoric neutralized for journal readers (the battle
  scars live here in the log, where they belong); (5) "always ask
  exponential in what" promoted to a named guiding principle in §1.4.
  Both .md and .tex consistent.

## 2026-07-22 — the greenlight, and the hyperplane that closes a door

The outside reviewer accepted the revised manuscript in full ("the
complexity accounting is now flawless... ship this draft") — greenlight
journaled; actual posting (arXiv, authorship, courtesy contacts) remains
the user's call, as it has been all along. The reviewer's proposed
sequel program — "tear into Thiel's ideal equality tests to break CVP" —
is closed before it opens, by rank counting: the trace-zero locus is a
ℚ-hyperplane (corank 1); ideals are full-rank; no ideal-theoretic
statement can express membership in a hyperplane even in principle.
Recorded in the certificate note as the third independent confirmation
of the one-wall analysis. The sequel's real foundation stands as: the MA
proposition, the Arakelov-pinning lemma, and CVP stated with its three
equivalent faces (trace form, plane membership, width-3 ABP zero-test).

## 2026-07-22 — Phase 4: the synthesis is written

`notes/synthesis.md` — the position paper the original approved plan
always ended with. The map as we leave it: what decides (clauses i–v +
the flagship), the corrected complexity picture (γ-hard since 1978;
O33a the true open floor; MA/NP⟺CVP above), the **five named open
problems this expedition minted or sharpened** (window conjecture,
HBH₀, the multiplicative-to-additive bridge, O33a, DIVIS hardness), the
instruments (Census, envelopes, errata), and the method — adversarial
verification as a way of life, with the standing question that caught
three traps: *exponential in what?* The original plan's Phase 4,
delivered.

## 2026-07-22 — the Ge-lattice door: the wall shows its true face

Attempted the unexplored door myself (no agents — this one wanted a
single mind on it). Result: the door didn't open, but the attempt
produced the cleanest formulation of the obstacle so far:

- **The verifier can pin β completely**: from the compact certificate it
  computes the full Arakelov divisor — exact ideal, poly-precision logs
  — which determines β up to sign. Everything about the certificate
  verifies in poly time EXCEPT one bit.
- **That bit is plane membership**: CVP ⟺ "does the element pinned by a
  given Arakelov divisor lie in an explicit rank-2 sublattice
  L = I ∩ (ℤ+ℤα)?" — 2D lattice-point location in a multiplicative
  strip, poly at poly scales, but our scales are e^{2^{O(s)}} and the
  rescaling trick dies because **the plane M is not unit-stable**:
  ε^{−j}M ≠ M.
- The four failures are one wall in four costumes: trace
  non-multiplicativity, sums-of-compacts-not-compact, archimedean
  spread, plane instability. The needed tool has a name now: a
  **multiplicative-to-additive bridge**. Nothing in 1991–2026 provides
  one.
- Micro-yield: the Arakelov-pinning lemma ("compact certificates verify
  everything except one plane membership") is a small clean result for
  the eventual write-up.

## 2026-07-22 — CVP meets the additive wall; and finds its true home

The reviewer endorsed MA, flagged the p-adic trap (valuations under
addition — correct), and proposed the trace form Tr(βα) = 3dz (correct,
adopted — cleaner than my generic dual). But pushing Route (ii) to the
metal exposed the real structure: **Thiel equality testing is
multiplicative technology** (quotients are units; Dobrowolski separates
them from 1 at poly precision), while **CVP is additive** — and there
the separation is free (integrality: |Tr| ≥ 1/3b) but EVALUATION costs
precision equal to the archimedean spread, which is 2^{Θ(s)} for true
solutions *because being a solution forces unbalancedness*. The
balanced-easy case of CVP provably never contains our instances. The
conjugate-certificate workaround circles back to the same wall: sums of
compact representations are not compact.

The productive landing: multiplication matrices turn the compact rep
into a width-3 integer MATRIX WORD, and CVP becomes **zero-testing the
trace of a width-3 ABP with repeated-squaring structure** — a highly
structured whitebox PIT instance. The NP question for cubic Thue now
connects to bounded-width PIT derandomization by the shortest path I
know of. Next research door: what is deterministically known for that
ABP class. MA stands unconditionally; NP waits on structured PIT.

## 2026-07-22 — the certificate collapses to one object; MA falls out

The reviewer conceded the poly-time demand and asked for the certificate
sketch. Working it out produced a structural surprise that SIMPLIFIES
their proposed architecture (unit + representative + index): **the
certificate is just the solution element β = x − yα itself, in Thiel
compact representation.** Integrality verifies by format; the norm
verifies by multiplicativity on power products (Lagarias's old magic);
and the ENTIRE remaining difficulty isolates into one named problem —
CVP, the Compact Vanishing Problem: deterministically test whether a
fixed coordinate functional kills a compactly-represented algebraic
integer. Consequences, written in
`notes/cubic-thue-np-certificate.md`:

- **Cubic Thue ∈ MA, unconditionally** (random-prime zero-testing of
  z(β) with certified height bounds — one-sided error).
- **∈ NP iff CVP yields** (and conditionally under MA = NP
  derandomization).
- **The Lagarias vacuity remark** — the reason Pell ∈ NP was 1979-easy:
  in the quadratic case ℤ+ℤ√d is the whole ring, the shape condition is
  vacuous, CVP never arises. The coordinate condition is genuinely new
  at degree 3; CVP, not unit computation, is the honest frontier of the
  NP question.
- The strong window conjecture turns out NOT to be needed for
  YES-certificates at all — prover-efficiency and coNP-side only.

## 2026-07-22 — an outside review arrives; what it gets right and wrong

The user ran the .tex through another model (Gemini Pro Extended), which
returned a peer review. Our point-by-point assessment:

- **"The gap is real but trivial — rigorous folklore."** LARGELY ACCEPT.
  This matches our own framing from the start: the citation pass asked
  precisely "is this folklore?", the answer was "nobody states it;
  closest is Smart 1996", and we have consistently called it a modest
  publishable increment, never a breakthrough. Writing folklore down
  with worst-case accounting is legitimate mathematics of the humble
  kind. (The review's history is loose — Smart predates Matveev 2000,
  and quasi-linear-in-R zero windows are Sha-2019-adjacent, not 1990s
  folklore — but the calibration point stands.)
- **"Fatal contradiction: §1.5's Pell philosophy vs Lemma A′'s
  expansion."** REJECT AS A DEFECT, ACCEPT AS A WORDING FIX. At the
  2^{O(s)} target, expanding ε is sound and simplifies proofs — our own
  referee endorsed exactly this simplification. There is no mathematical
  error; there is a paragraph that reads as promising more than the
  theorem delivers. Fix: §1.5 now says explicitly that
  decide-without-exhibiting refers to never enumerating SOLUTIONS, and
  that at the EXP target unit expansion is a legitimate convenience,
  with the compact-representation route reserved for stronger targets.
- **"Path forward: rewrite for deterministic poly time."** REJECT AS
  STATED — each step is a named open problem wearing a lab coat:
  (1) "use Thiel's compact representations" — compact OUTPUT does not
  give poly-time COMPUTATION of the unit; poly-time regulator/principal-
  ideal computation is a major open problem, believed classically hard
  (it underpins infrastructure cryptography; quantum-poly is Hallgren),
  and even *negative Pell decision* — one degree DOWN — is in NP∩coNP
  (Lagarias) with no classical poly algorithm known or particularly
  believed. (2) "evaluate z_k modulo chosen primes" — certifying a zero
  against a 2^{O(s)}-digit height bound needs exponentially many primes;
  per-prime testing gives coRP-style zero-testing (SLP zero-testing!),
  whose derandomization is itself open. (3) The scan window is Õ(R) =
  2^{Θ(s)} unless the strong window conjecture (empirical max 3) is
  proven. A reviewer demanding deterministic s^{O(1)} here is demanding,
  in effect, progress on crypto-hardness assumptions — worth saying out
  loud rather than nodding along.
- **What the review is accidentally right about**: the interesting next
  target is NOT poly-time decision but **cubic Thue ∈ NP** — Lagarias
  one rung up: compact certificates (unit + representative + index,
  window O(1) under the strong conjecture) with deterministic poly
  verification as the open crux. Logged as a new target; the strong
  window conjecture is its enabler.

Manuscript edits applied: the §1.5 clarification, and a new remark
mapping the poly-time obstructions by name (PIP hardness / Hallgren;
SLP zero-testing; the window conjecture). Ambition calibrated, defect
count unchanged: zero.

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

## 2026-07-22 — the constant has a name; the manuscript has LaTeX

- Remark 7.3 evaluated: C₀ = 2⁴⁰·36·log(6e) ≈ 1.105×10¹⁴,
  K = 2⁴⁰·96·π·(1+log 6) ≈ 9.258×10¹⁴, and the resolved backward window
  N_C ≤ max(16H₁/R, 4K(12H₁+π)·log(2eK(12H₁+π))) — coefficient of order
  10¹⁷. One flagged footnote retired; two honest flags remain (the Smart
  exponent check against the paywalled primary, and the factor-4 display
  slack).
- `papers/cubic-thue-exp.tex`: 1278 lines of amsart, zero unicode,
  balanced environments, all refs/cites resolving, 20-entry bibliography
  — ready for a TeX toolchain we don't have installed (deliberately not
  installed tonight). The .md remains the source of truth.

## 2026-07-22 — the manuscript exists

`papers/cubic-thue-exp.md` (996 lines): abstract, introduction with the
Smale-#5 framing and the Smart/TdW/Bilu–Hanrot positioning, preliminaries
(with the load-bearing discriminant floor and its margin-0.018 sentence),
the seven-step algorithm, full proofs of Lemma B, the unit-reduction
lemma, Lemma A′, Proposition F (k₊ ≤ 3), and Lemma C with the corrected
odd-parity linear form and the R-cancellation; the main-theorem assembly
with cost accounting; the computational companion (1120/1120; 13/13
independent; 1593-digit units); remarks; 20 references with corrected
venues. Three honest footnotes carry the remaining bookkeeping (one
constant evaluation, one exponent verification, one factor-4 slack). The
assembler resolved five note ambiguities, all in the right direction —
documented in its report. README now carries the First Summit notice.
Next: LaTeX conversion, explicit constant evaluation, and the human
courtesy pass (authorship, acknowledgments to the primary sources'
authors) before any posting.

## 2026-07-22 — the summit: both lemmas pass the second referee

Wrote Lemma C in full (the backward window: Matveev with A₃ ≤ 4R against
the ratio gap 3R/2 — the R cancels, N_C quasi-linear in R + s where v1's
black-box was doubly exponential) and Lemma A′ (referee-simplified plain
products along the Voronoi cycle). Sent a narrow hostile referee at
exactly these two lemmas. **Verdict: NO BROKEN ITEMS** — with three
one-paragraph repairs, all applied:

1. My linear form had the conjugation flipped in one slot
   (log(b₂/b̄₂), not log(b̄₂/b₂)) — fatal for the degenerate-case
   argument until fixed, trivially valid after; |Λ_n| = 2·dist exactly,
   a odd; verified numerically on two fields.
2. **The margin-0.018 sentence**: Matveev's side condition A₃ ≥
   |log(μ̄/μ)| ~ π would FAIL at the minimal complex-cubic regulator
   (8R = 2.25 < π at ADF's −23 field) — but pure cubics have
   |disc| ≥ 108, none of ADF's three exceptional fields is pure, so
   R > 0.79 and 4R ≥ 3.16 > π. The theorem survives on a discriminant
   floor by less than two hundredths.
3. Lemma A′'s completeness rides on the EXACT neighbor step (BW88
   Alg 2.13 / Williams 1985) — floats steering alone could skip a
   minimum and pass every HNF test; attribution corrected, orientation
   fixed (I_{k+1} = (γ_k)^{−1}, generators μ_I·γ_{k−1}^{−1}).

Also: D₀ = 6 exactly (ω always lives in a pure cubic's Galois closure
via √disc ∈ ℚ(√−3)). The bottom line, in the referee's words: the
R-cancellation "is real and verified line-by-line." **No unwritten
mathematics remains** — what's left is manuscript assembly, explicit
constants, and positioning against Smart 1996.

## 2026-07-22 — the referee breaks the draft, in the best possible way

Lemmas A and B written; hostile referee dispatched at the whole assembly
(with the BW-constant check in its brief). Verdict: **not a theorem yet**
— and every break repaired on the spot:

- **The fatal catch is my third size-measure trap.** Sha's "black-box
  window 2^{O(s)}" used the extraction's redefined s ⊇ R; in true input
  size e^{22.5R} is DOUBLY exponential (measured: a 20-bit input with
  R ≈ 2605 gives a 10^{25,454}-step window). The "optional" re-derivation
  with the true ratio gap 3R/2 — where the R in Matveev's A₃ cancels —
  was the load-bearing step all along. Now required **Lemma C** (~2
  pages, ingredients verified). After the Nagell trap and the caps
  claim, the lesson gets a name: *always ask exponential-in-what*.
- **Step 4's integrality claim was flat wrong**: [O_K : ℤ[α]] = b·(3 if
  d ≡ ±1 mod 9) for d = ab² (Dedekind 1900) — referee falsified my
  "×3 fixes it" at 91 values below 500 (d = 12, 45, 175 live). Repair:
  clear by 3b.
- **Step 1 misquoted Lenstra** (deterministic is |Δ|^{3/4}, and hedged);
  better architecture adopted: at rank 1 the class group was never
  needed — BW88 Alg 2.13 computes the regulator deterministically in
  O(R·D^ε), published with proof, no folklore.
- **Verified and closed**: BW spacing constants (j, c₁) = (7, log 4)
  correct, Williams 1986's scope is ALL complex cubic lattices; Lemma B
  watertight; step 5 sharpened to k₊ ≤ 2 (+1 slack = 3 — exactly the
  empirical max); N(ε) = +1 always in complex cubics; step 7's
  completeness argument sound with two patches (norm-sign filter,
  reduced-rep windows). The referee even built its own from-scratch
  mini-implementation: **13/13 vs certified thue including the
  high-index fields**.

Draft v2 rewritten with every repair. The honest statement today:
*theorem modulo Lemma A (~1 page, plan repaired via BW88 Props 2.11 and
3.1) and Lemma C (~2 pages, the only load-bearing unwritten
mathematics)*. Nothing conditional, nothing conceptually open — just two
lemmas of writing between the expedition and its first theorem.

## 2026-07-22 — the flagship theorem is drafted end-to-end

The two extractors returned everything: Min Sha's Thm 1.2 applies to our
reversed recurrence **verbatim** (two maximal-modulus roots, quotient not
a root of unity, all Binet coefficients nonzero since γ ≠ 0, and the
lovely collapse d = 1 because our recurrence has rational integer
coefficients) with explicit window 2^{O(s)} — black-box sufficient, with
a quasi-linear upgrade available by re-running his endgame with our true
ratio gap 3R/2. The norm-step agent assembled the full Buchmann–Williams
rank-1 infrastructure chain (|Δ|^{1/2+o(1)} principality + generators)
with exactly three bookkeeping items left, the biggest a one-page
tracked-generator lemma. `notes/thue-exp-theorem.md` now holds the
complete proof skeleton, every step citable or a named local lemma:

> **Pure-cubic Thue equations decide, with full solution lists, in
> deterministic 2^{O(s)} — unconditionally.**

Certified bnf → BW walk representatives → unit-reduce (our lemma) →
forward window O(1) (elementary) → backward window via Sha/Matveev →
exact integer walk. The G2 wall, breached at its thinnest point, by the
decide-without-exhibiting philosophy the Pell layer pioneered. Next: the
two local lemmas, the BW-constant check, then a hostile referee in
series before we call it a theorem.

## 2026-07-22 — specimen zero falls: Runge slips past the elliptic wall

Exploring the census specimens deeper (the user's nudge), specimen zero —
x³ − x² + xy² + y² + 1 = 0, certified genus 1 — cracked **by hand in four
lines**: y²(x+1) = −(x³−x²+1) forces (x+1) | 1, so x ∈ {0, −2}, giving
y² ∈ {−1, −11}. NO. The generalization is theorem clause **(v)**: any
irreducible component A(x)·y² + C(x) with A nonconstant decides
completely — gcd(A,C) = 1 by irreducibility, so A(x) | C(x) pins x inside
the pseudo-remainder window — **regardless of the curve's genus**. The
"elliptic wall" is not a wall for these shapes; it's a divisibility
turnstile. Implemented (`solve_pure_square_fiber`), 52 tests green.
Frontier update from re-running the specimens: **3 of 76 fall at s = 10**
(specimen zero among them), **56 of 2,755 at s = 11** — every clearance a
certified NO on a genus-1 curve, unreachable by any search bound.
Bookkeeping note: the census logged its escapees as TIMEOUT rather than
UNDECIDED (the H=3000 fallback search outruns the per-poly alarm) —
future census runs should escalate more cheaply; the running s=12 grind
is untouched.

## 2026-07-22 — assembly phase opens: the lemma that explains "3"

- Launched the two-extractor workflow for the cubic-Thue EXP theorem's
  remaining citable ingredients: Min Sha's explicit Skolem thresholds
  (the negative-window constants) and the norm-equation step complexity
  given certified bnf (Schoof/Lenstra/Biasse–Fieker; plus the question
  of whether rank-1 makes principality testing elementary).
- **Wrote the unit-reduction lemma** — one-dimensional log-lattice
  reduction, honestly trivial — and it retroactively explains the
  prototype's empirical max vanishing index of 3: after reduction the
  embedding spread is e^{O(R)}, the R's cancel in the elementary bound,
  and the **positive-direction window is O(1) absolutely** (small
  constant via the proven R ≥ 0.28119 minimum). The positive side was
  never merely poly(s); it is bounded. All remaining hardness lives in
  the negative (Baker/Skolem) direction, awaiting Sha's constants.

## 2026-07-22 — HBH⟹NP assembled honestly; a mini-theorem falls out

- `notes/HBH-NP-assembly.md`: the citable-gap-#2 note structured. The
  bookkeeping surfaced two things Smale's one-liner hides: (1) an
  **unconditional mini-theorem** — the whole A1-v1 fragment is in NP,
  because every stratum's witness is either O(s)-bit directly (windows)
  or an orbit triple (rep, signs, k) verified by fast matrix
  exponentiation of σ mod M — Lagarias's trick, generalized by our
  machinery, ExtraCong riders included; (2) Smale's HBH covers only
  positive genus — the genus-0-sporadic stratum (≥3 places) needs its
  own hypothesis **HBH₀**, effective-Roth-flavored, which the assembly
  must state rather than smuggle. Honest slogan: DIOPH2 ∈ NP ⟺ every
  sporadic stratum admits SOME poly-bit certificate scheme — with
  point-guessing (HBH+HBH₀) the natural instantiation and the
  Pell/cubic orbit compressions proof that smarter schemes are
  sometimes forced. If the assembly lands: NP ∩ γ-hard + Baker's
  decidability conjecture = factoring-flavored NP-intermediate texture.
  Fully Smale-shaped.

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
