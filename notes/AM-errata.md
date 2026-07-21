# Errata and a modernization for Adleman–Manders (1978)

Draft v1 · 2026-07-22 · target: short arXiv/technical note. All claims
below were extracted from page scans of the primary source and verified by
two independent adversarial agents plus machine checks
(`scripts/verify_am_erratum.py`); the ⟨27, 1343⟩ counterexample is
executable in-repo.

**Source.** L. Adleman, K. Manders, *Intractability Proofs and the
Computational Complexity of Binary Quadratics*, UC Berkeley ERL Memorandum
UCB/ERL M78/30 (June 1978) — the full-length companion of the STOC 1977
paper (*Reducibility, Randomness and Intractibility*) and FOCS 1979
(*Reductions that Lie*). Its results are the ONLY known hardness anchors
for two-variable Hilbert's-10th over ℤ, so its statements deserve exact
maintenance.

## E1 — Misprinted theorem statements (Thm 1.3.4(1); Thm 1.3.6, 2nd set)

As printed, both assert γ-completeness of
{⟨a,c⟩ : (ax+1)y = c solvable in ℤ}. This set is all of ℤ² (take x = 0,
y = c) and cannot be hard. The intended — and elsewhere correctly printed
(Thm 1.3.9(2), Thm 2.4.2) — statement carries the side condition "has a
**nonzero** solution in ℤ". Anyone citing 1.3.4(1) verbatim cites a false
sentence; the correct citable ℤ-solvability sets *without* side
conditions are the §2.3 quadratics (below).

## E2 — A bound bug in Theorem 2.4.1, with counterexample and repair

Thm 2.4.1 ({⟨3^{k+1}, c⟩ : (3^{k+1}x + 2)y = c solvable in ℤ}) reduces
from knapsack via primes hᵢ ≡ 2^{aᵢ} (mod 3^{k+1}), with the printed
parameter choice **2·3^k > 1 + Σ|aᵢ|**. Because 2 is a primitive root
mod 3^{k+1}, −1 = 2^{3^k} ∈ ⟨2⟩, and a **negative** divisor
d = −Π_S hᵢ ≡ 2 (mod 3^{k+1}) exists whenever Σ_S ≡ 3^k + 1 (mod 2·3^k)
— which the printed bound does not exclude.

**Concrete false YES** (machine-verified): knapsack {5}, target 2 (a NO
instance) → normal-form list {10, −3}; printed bound gives k = 2, modulus
27; h₁ = 79 ≡ 2¹⁰, h₂ = 17 ≡ 2⁻³ (mod 27); c = 1343. Then
(27·(−3) + 2)·(−17) = 1343: solvable over ℤ via the negative divisor
−79 ≡ 2 (mod 27), while no positive divisor of 1343 is ≡ 2 (mod 27) (the
ℕ-version is unaffected).

**Repair.** Choose k with **3^k > 1 + Σ|aᵢ|** (as §2.3 effectively does).
Then all attainable subset-sums satisfy |Σ_S| ≤ 3^k − 2, so the residue
1 (mod 2·3^k) forces Σ_S = 1 exactly and the negative-divisor residue
3^k + 1 is unattainable. The theorem survives with the stronger bound.

## E3, E4 — Minor errata

E3: the b→1 preprocessing (p. 45) should append a_{n+1} = 1 − 2b (printed:
2b − 1) for the displayed equivalence to hold. E4: Def 1.3.4's weight
inequality is typed "≤ ½" where "≥ ½" is required (cf. Def 1.3.2 and the
proof of Prop 1.3.8).

## M — The AKS modernization

The memo's unconditional results are the *unfaithful* random
completenesses; faithful (hence γ-) completeness is claimed under ERH,
entering only through Miller's primality test inside the prime-sampling
subroutine. Primality testing consumes no nondeterminism there — it runs
deterministically on each guessed candidate — so substituting AKS leaves
the computation tree and all path weights unchanged while making every
output path faithful. Prime *density* in the progressions was always
unconditional (Barban–Linnik–Tchudakov for prime-power moduli). Hence:

> **Theorem (A–M 1978, modernized).** The sets
> {⟨a,c⟩ : x² − a²y² = c solvable in ℤ} and
> {⟨a,c⟩ : x(x + ay) = c solvable in ℤ} (even with a restricted to
> powers of 3) are faithfully random complete, and therefore γ-complete,
> **unconditionally**. Consequently each lies in RP iff RP = NP, in
> NP ∩ coNP iff NP = coNP; membership in P implies NP = coNP. Via
> ⟨a,c⟩ ↦ x² − a²y² − c, the set {f ∈ ℤ[x,y] : ∃(x,y) ∈ ℤ², f = 0} is
> γ-hard and random-hard, with the same consequences.

(For Thm 2.4.2's prime-modulus set the discharge also works — its
generator already certifies p unconditionally via
Brillhart–Lehmer–Selfridge; Thm 2.4.1's set needs the E2 repair first.)

## Remarks

1. The ℕ/ℤ conflation seeded by E1 recurs downstream (e.g. claims that
   ax² + by + c = 0 is NP-complete over ℤ² — false as stated; the
   NP-completeness is Manders–Adleman's ℕ-statement). A corrected record
   may stop the propagation.
2. The still-open problem these results frame is Adleman–McCurley O33a
   (ANTS-I 1994): *deterministic* NP-hardness of binary-quadratic
   ℤ-solvability — open since 1979.

## TODO before posting

- Obtain and cite the STOC 1977 pagination for the affected theorems (the
  memo is the superset; the conference version may not contain E1's slip).
- Courtesy contact: the erratum concerns living authors' early work.
- Re-verify E3/E4 page scans independently (currently single-agent reads;
  E1/E2 are double-verified + machine-checked).
