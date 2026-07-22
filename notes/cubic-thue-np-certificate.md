# The certificate sketch: cubic Thue ∈ MA, and the isolated NP crux

2026-07-22 · response to the outside review's pivot request. The
architecture below SIMPLIFIES the proposed certificate (unit + reduced
representative + index): all three collapse into one object.

## The certificate is the solution element itself

For a YES instance of x³ − d·y³ = m, the solution (x, y) corresponds to
β = x − y·α ∈ ℤ[α], α = ∛d, with log-height O(R + log|m|) = 2^{O(s)}.
**Certificate: a Thiel-format compact representation of β** —
β = β₀·∏_{i≤T} β_i^{2^i} with T = O(log height) = O(s) factors of
poly(s) bits, integrality-verifiable by format. Existence: constructive
from our Lemma-A′ walk (the prover runs the EXP algorithm once);
poly-size by the standard compact-representation size bounds.

No ε, no representative, no index k, no window: if β is a solution, its
compact representation alone witnesses it. (The strong window conjecture
matters for the *prover's* efficiency narrative and for coNP-side
discussions — not for YES-certificates.)

## The verifier, step by step

1. **Integrality** (β ∈ O_K, and ∈ ℤ[α] after the 3b-bookkeeping):
   deterministic poly — Thiel's format carries denominator data checked
   by exact ideal arithmetic on poly-size objects.
2. **Norm**: N(β) = m. Deterministic poly — **norms are multiplicative
   on power products**: N(β) = N(β₀)·∏N(β_i)^{2^i}, each N(β_i) a small
   explicit integer, binary exponents. (This is exactly the magic that
   powered Lagarias's Pell certificates.)
3. **Thue shape**: z(β) = 0, i.e. the α²-coordinate vanishes,
   equivalently Tr(w·β) = 0 for the fixed dual element w. **This is the
   entire remaining difficulty**, and we name it:

   > **CVP_K (Compact Vanishing Problem).** Given a compact
   > representation of an algebraic integer β in a fixed cubic field,
   > decide in deterministic poly time whether a fixed ℚ-linear
   > coordinate functional vanishes at β.

## What follows immediately

- **Proposition (MA membership, unconditional).** Pure cubic Thue
  solvability is in **MA**. Merlin sends the compact β; Arthur verifies
  integrality and norm deterministically, then tests z(β) = 0 modulo
  poly(s)-bit random primes: z(β)·(3b) is an integer of ≤ 2^{O(s)}
  digits computable mod p in poly time (power products by repeated
  squaring mod p); a nonzero value survives a random prime from a
  2^{s^c}-range with overwhelming probability (it has at most 2^{O(s)}
  prime divisors). One-sided error, amplifiable. ∎(sketch)
- **Corollary.** Cubic Thue ∈ NP **iff-modulo** CVP: if CVP_K ∈ P for
  these instances, membership in NP follows; under standard
  derandomization hypotheses (MA = NP), membership in NP holds
  conditionally today.
- **The Lagarias vacuity remark** (why 1979 stopped at degree 2): in the
  quadratic case the module ℤ + ℤ√d is ALL of ℤ[√d] — the Thue-shape
  condition is vacuous, CVP never arises, and norm-checking alone
  suffices. The coordinate condition is genuinely NEW at degree 3: CVP
  is exactly the object that separates the cubic certificate problem
  from Pell. This, not the unit computation, is the honest frontier of
  the NP question.

## Why CVP is interesting in its own right

CVP is integer zero-testing for a *structured* straight-line program: a
sum of three conjugate power products. General SLP zero-testing in P
would derandomize polynomial identity testing (open); CVP's structure
(fixed field, conjugate symmetry, Tr-functional) may be much weaker.
Two attack routes worth probing: (i) p-adic — ord_p of power products is
poly-computable per prime; vanishing forces compatible valuations at ALL
primes, and the denominator/height data bound which primes can matter;
(ii) canonical-form — Thiel-style equality testing of compact
representations (β vs its projection) if a compact representation of the
projection can be certified alongside. Either yielding CVP ∈ P for
Thue-shaped instances would complete: **cubic Thue ∈ NP,
unconditionally** — Lagarias one rung up, for real.

## Honest status ledger

- MA membership: proposition-with-sketch, needs a careful write-up
  (height bound on z(β) from the compact data; prime-range constants).
- Compact-representation existence & size for β: standard, needs the
  precise citation (Thiel; Buchmann–Thiel–Williams) — next citation
  pass.
- CVP: open, named, isolated. The right-sized next mathematics.
- coNP side (certifying NO): untouched here; the window conjecture and
  class-enumeration certificates would enter there.
