# Track B: the hardness landscape and the candidate reduction

2026-07-21 · source: the war-council's landscape survey (one of four
attackers; the other three and the skeptic starved on session limits and
await resumption). Citations below are **agent-reported and pending our own
verification pass** (the review classifier was unavailable for this agent's
run) — treat as [P] until a citation workflow confirms.

## Status of the question "is two-variable H10 over ℤ NP-hard?"

- **Nobody has claimed hardness.** No published NP-hardness result or even
  an explicit hardness conjecture for the full two-variable problem over ℤ
  (or ℕ) exists. The revealed community expectation is the opposite:
  **Alan Baker conjectured the two-variable problem is DECIDABLE**
  (reported in Jones, JSL 46 (1981) §5; echoed by Rojas math/9811088
  Remark 13). Decidability of ℤ²-, ℕ²-, even ℚ²-root detection is still
  open (Rojas 1998; Gasarch 2021; Grechuk 2022 — whose "smallest open
  instances" are genus-2 quartics such as y³ + xy + x⁴ + 4 = 0).
- **Folklore texture**: Lagarias's negative-Pell is NP ∩ coNP — the
  quadratic stratum looks factoring-like / NP-intermediate, not
  NP-complete. Decidable-but-hard is the consensus guess.

## Upper bounds beyond Lagarias (agent-verified statements)

- Lagarias FOCS 1979: binary quadratics **with a congruence side
  condition** and nonnegativity are in NP — strongest unconditional
  2-variable NP bound known.
- Tung 1987: the ∀∃ sentence class over ℤ is **coNP-complete**, with
  covering-congruence certificates (JST theorem: Jones–Schinzel–Tung).
  The ∀-version of our divisibility problem is exactly this territory.
- Rojas: dimension-0 systems over ℤⁿ in PSPACE; generic ∃∀∃ in coNP; the
  exceptional locus of that algorithm contains precisely the ∃∃ core.
- MFCS 2025 (one-parametric Presburger, arXiv:2506.23730): existential
  PrA[t] with divisibility atoms is NP-complete with poly-size minimal
  solutions. Immediate, apparently unremarked consequence: **DIVIS =
  {(A,B) : ∃x ∈ ℤ, A(x) | B(x)} ∈ NP** — which ALSO follows in one line
  from our graph stratum's pseudo-remainder window (the window is
  2^{O(s)}, so the witness x has O(s) bits). Systems ∧ᵢ Aᵢ(x) | Bᵢ(x)
  are in NP too. No hardness for DIVIS is known; nobody has studied it.

## The candidate reduction (the survey's genuine find)

**Target**: L = {f : ∃(x,y) ∈ ℤ², f = 0} NP-hard under randomized
many-one reductions (deterministic under ERH-type least-prime-in-AP).

**Vehicle**: Adleman–Manders (STOC 1977) proved the *linear divisibility
problem* {(a,c) : ∃x,y ∈ ℕ, (ax+1)·y = c} γ-complete (NP-hard under
randomized reductions). Over ℤ the same single degree-2 equation
(ax+1)y = c says "|c| has a divisor ≡ ±1 (mod a)" — the ± is the gap.
**Sign-rigidification idea**: arrange 3 | a and every prime factor of c
≡ 1 (mod 3) (compatible with the Linnik/Dirichlet sampling already inside
the γ-reduction); then all positive divisors of |c| are ≡ 1 (mod 3) while
a divisor ≡ −1 (mod a) would be ≡ −1 (mod 3) — impossible. On such
instances ℤ- and ℕ-problems coincide and γ-hardness transfers verbatim:
**L would be NP-hard under randomized reductions, via a single binary
quadratic**. Caveats before believing: (i) the STOC 1977 internals
(exact formulation, sampling compatibility) must be read — paywalled at
the time of the survey; (ii) γ-reductions have one-sided error — the
clean statement is "L ∈ BPP ⟹ NP ⊆ BPP"; (iii) coefficient sizes check
out (poly-bit).

**If this survives scrutiny it collides productively with Baker's
decidability conjecture**: decidable + randomized-NP-hard = a natural
candidate for "decidable but not in P", exactly Smale-flavored.

## The two-sided tension (Rojas, math/9809009)

If BigN (max height of integral points on plane curves) is computable,
then a natural 4-variable ∃∃∀∃ class is undecidable. Either some plane
curves have uncomputably large integral points, or undecidability
descends to four quantified variables. Effective Siegel is not free.

## Our two citable-gap targets (updated ledger)

1. **Pure-cubic Thue in EXP, unconditionally** (A1-v2 assembly; vs Smart
   ANTS-II 1996) — `notes/A1v2-cubic-thue.md`.
2. **HBH ⟹ two-variable H10 ∈ NP** — Smale stated the hypothesis; nobody
   has assembled the theorem (HBH for positive genus + Silverman's
   refined Siegel classification [TCS 235 (2000): infinitely many
   integral points iff genus 0 + nonsingular integral point + leading
   form with ≤ 2 roots, all real — note: sharper than what classify.py
   encodes; upgrade candidate] + Lagarias-style Pell certificates for the
   genus-0-infinite stratum). Bookkeeping-hard, idea-light, unclaimed.

## Census cross-reference (2026-07-21)

The Census located the toolkit's own frontier at dense size **s = 10**:
76 undecided canonical polynomials out of 43,439 — and **75 of the 76 are
certified genus-1 curves** (e.g. x³ − x² + xy² + y² + 1 = 0): the
elliptic wall, exactly where theory predicts, decidable-in-principle
(Baker–Coates) but unimplemented. The 76th is a cubic the classifier
cannot yet pin (x³ − x²y − x² − xy² + xy + x + y³ + y + 1 = 0) — the
smallest mystery object in the census. At s = 11: 2,755 undecided of
183,209. Implementing an elliptic-integral-points stratum would move the
whole frontier.

## Queue

- Resume the three starved attackers + skeptic (range-gadget,
  divisibility-hardness, siegel-barrier) after the quota reset.
- Citation-verify this survey's load-bearing claims (Baker-conjecture
  attribution, Tung, MFCS 2025, Adleman–Manders 1977 internals).
- Read STOC 1977; attempt the sign-rigidification composition properly.
- Upgrade classify.py to Silverman's refined criterion.
