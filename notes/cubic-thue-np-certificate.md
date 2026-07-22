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

## Route (ii) deep-dive (2026-07-22, after the reviewer's endorsement)

**Adopted**: the clean trace form. For β = x + yα + zα² (α = ∛d):
βα = zd + xα + yα², and Tr(1) = 3, Tr(α) = Tr(α²) = 0 give
**z = Tr(βα)/(3d)** — CVP is exactly "Tr(βα) = 0 for compact β".

**The additive/multiplicative divide.** Thiel-style deterministic
equality testing is a *multiplicative* technology: β = γ reduces to the
quotient being 1, and units ≠ ±1 are separated from 1 by
Dobrowolski-type lower bounds on the log-embedding lattice — poly
precision suffices. CVP is *additive*: Tr(βα) is a sum of three
conjugate terms. Separation is not the problem — integrality gives
|Tr| ≥ 1/(3b) when nonzero. **Evaluation is the problem**: certifying
the sum numerically needs absolute precision ~ the archimedean spread
max log|σᵢ(β)| − min, and for TRUE Thue solutions the spread is
2^{Θ(s)} forced (a solution has |σ₁(β)| = |m|/|σ₂(β)|² tiny precisely
because it is a solution — the easy "balanced-β" case of CVP can never
contain the instances we care about). Angle formulation hits the same
wall: verifying arg σ₂(βα) ≈ ±π/2 to error e^{−spread} needs the small
factors' arguments to exponentially many bits.

**The conjugate-certificate attempt, and its circle.** One can move to
the Galois closure L = K(ω) and note Tr(βα) = 0 ⟺
β + ωσ₂(β) + ω²σ₃(β) = 0; certifying compact representations of the
conjugates is fine, but the final check is again an additive vanishing
of compact objects — the divide reappears intact. Sums of compact
representations are not compact; that sentence IS the obstacle.

**Where CVP actually lives.** Writing multiplication-by-βᵢ as 3×3
integer matrices, β's compact representation is a MATRIX WORD with
repeated-squaring structure, and CVP is: *decide whether the trace of a
width-3 integer matrix word is zero*. That is polynomial identity
testing for width-3 algebraic branching programs (a highly structured,
whitebox, repeated-squaring instance). This is the right literature
door: bounded-width ABP identity testing has real deterministic results
in special cases — whether the repeated-squaring word class is among
them is precisely the next question to research, and it connects our NP
question to the derandomization frontier in the cleanest possible way.

## The literature verdict (2026-07-22 sweep, 1991–2026)

- **Blömer is structurally inapplicable, not merely insufficient**: his
  determinism rides Siegel's rigidity (independent radicals admit NO
  nontrivial ℚ-linear relations, so zero-testing is coefficient
  collection) — and our trace-zero instances ARE nontrivial relations in
  the rank-2 trace-zero module: the exact phenomenon his theorem
  excludes. Both pillars (rigidity + explicit poly-size arithmetic)
  fail simultaneously.
- **The compact-representation toolbox stops at the trace, precisely**:
  Ge (FOCS 1993; Lenstra's notes Thm 4.75) decides multiplicative
  relations of power products in deterministic poly time — so N(β) = m
  is testable; BTW 1995 adds 2-term sign comparison in real quadratic
  fields; NO additive ≥3-term test exists anywhere in the literature.
- **EquSLP context**: coRP since Schönhage; open for P; ABKM Prop 2.1
  makes iterated squaring the HARD CORE of EquSLP (derandomization ⟹
  circuit lower bounds, Kabanets–Impagliazzo) — a caution, not a
  hardness proof, for our width-3 single words.
- **The Baker route (Galby–Ouaknine–Worrell PosMatPow, dim 3)** decides
  trace-zero of matrix powers in P — for POLY-HEIGHT bases; the
  bounded extension "CVP with O(1) multiplicative rank and poly heights
  ∈ P" is publishable-but-bounded and does NOT cover Thue certificates
  (ε has height 2^{Θ(s)}); at Θ(s) logarithms the Baker constants
  degrade exponentially — the same wall that pins LRS Positivity at
  order ≥ 6 (Ouaknine–Worrell).
- **Verdict: genuinely NEW, sum-of-square-roots-class flavor** — coRP,
  in CH, deterministic open; and the one unexplored asset is exactly
  ours: the three summands are Galois-conjugate and the bases' full
  multiplicative relation lattice is COMPUTABLE (Ge). The additive
  analog of Lenstra's Lemma 4.76 — detecting trace-zero from the
  relation lattice plus unit-lattice geometry — has never been
  attempted. That is the door.

## The Ge-lattice door: first attempt (2026-07-22)

The attempt did not open the door, but it relocated it. The chain:

1. **The verifier can pin β completely.** From the compact representation
   it computes in poly time the full **Arakelov divisor** of β: the exact
   ideal I = (β) (via reduced-ideal arithmetic with tracked distances —
   infrastructure is precisely this) and the log-embeddings log|σᵢ(β)| to
   any poly precision. An element of K is determined by (ideal, exact
   logs) up to ±1. So the certificate pins a *unique* candidate element —
   no ambiguity survives verification except the final question.
2. **The final question is plane membership.** z(β) = 0 ⟺ β ∈ M = ℤ+ℤα,
   and L := I ∩ M is an explicit rank-2 lattice with poly-size basis
   (HNF intersection). So:
   > **CVP (Thue instances) ⟺ does the element pinned by a given
   > Arakelov divisor lie in an explicit rank-2 sublattice?**
3. **Why each classical tool stops here.** The pinned element sits in a
   thin multiplicative strip (|x − yα| ~ e^{ℓ₁} tiny at height
   |y| ~ e^{ℓ₂} huge). Searching L ∩ strip is 2D lattice-point location
   — poly *at poly scales* (Lenstra fixed-dimension) — but our scales
   are e^{2^{O(s)}}, described only by their logs. The multiplicative
   fix (rescale by ε^{−j} to bring the strip to bounded size) fails
   because **M is not stable under units**: ε^{−j}M ≠ M. That
   instability is the same fact, in its fourth costume, that has blocked
   every route: trace non-multiplicativity, sums of compacts not
   compact, the archimedean spread, and now plane non-stability. They
   are one wall.
4. **What a solution needs, stated once**: a *multiplicative-to-additive
   bridge* — any theorem letting membership in a fixed rank-2 plane be
   tested through data carried multiplicatively (relation lattices,
   Arakelov classes, unit orbits). No such tool exists in the 1991–2026
   literature (previous section); building one is the actual open
   problem, and it now has a precise geometric formulation.

Micro-yield: the Arakelov pinning (step 1) is itself a small clean
result — "compact certificates verify everything about β except one
plane membership" — worth a lemma in the eventual write-up.

## Honest status ledger

- MA membership: proposition-with-sketch, needs a careful write-up
  (height bound on z(β) from the compact data; prime-range constants).
- Compact-representation existence & size for β: standard, needs the
  precise citation (Thiel; Buchmann–Thiel–Williams) — next citation
  pass.
- CVP: open, named, isolated. The right-sized next mathematics.
- coNP side (certifying NO): untouched here; the window conjecture and
  class-enumeration certificates would enter there.
