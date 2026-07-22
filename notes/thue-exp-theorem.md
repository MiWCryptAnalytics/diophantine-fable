# Theorem draft: pure-cubic Thue equations decide in exponential time

Draft v1 · 2026-07-22 · the expedition's flagship assembly. Positioning:
no worst-case bound of this shape exists in the literature (closest prior:
Smart, ANTS-II 1996 — per-method practical estimate); all ingredient
extractions archived in `notes/citations/2026-07-22-assembly-extraction
.json` and the two A1-v2 verification files.

## Statement

> **Theorem (assembly target).** There is a deterministic algorithm that,
> given cube-free d ≥ 2 (not a cube) and m ≠ 0 in binary, input size
> s = O(log d + log m), decides whether x³ − d·y³ = m has a solution in
> ℤ² — and lists all solutions — in time 2^{O(s)}, unconditionally.

## Proof skeleton (every step now citable or a named local lemma)

1. **Certified bnf.** K = ℚ(∛d), |Δ_K| ≤ 27d² = 2^{O(s)}. Certified
   class group + fundamental unit ε (compact representation), R = log λ:
   deterministic |Δ|^{1/2+o(1)} = 2^{O(s)} [Lenstra 1992 Thm 5.5; Schoof
   2008 §11 Arakelov; R = 2^{O(s)} via hR ≤ |Δ|^{1/2}·polylog].
2. **Norm-equation representatives.** Factor m by trial division
   (2^{O(s)}); ideals of norm |m|: ≤ d(|m|)³ candidates, assembled in HNF
   poly-time each; principality + generator per candidate via
   Buchmann–Williams baby-step walk in the rank-1 infrastructure:
   deterministic |Δ|^{1/2+o(1)} + poly = 2^{O(s)} [BW87 Alg 1.1, BW88
   Prop 4.5/Thm 4.7]. **Local Lemma A (tracked generators, ~1 page):**
   augmenting Schoof's Alg 10.8 doubling with generator tracking yields
   compact representations (O(s) factors of poly(s) bits) for each
   generator — rank-1 case, direct proof.
3. **Unit reduction.** Our one-dimensional log-lattice lemma (A1-v2 note):
   representatives γ with h(γ) ≤ ⅓log|m| + R + O(1), computed rigorously
   with interval arithmetic in 2^{O(s)}.
4. **The orbit and its recurrence.** Solutions = coordinate-vanishing
   points z_k = 0 along γ·(±ε^k); z_k ∈ (1/3)ℤ (multiply by 3 in the
   index-3 case d ≡ ±1 mod 9) satisfies an order-3 integer linear
   recurrence with characteristic polynomial = min poly of ε — simple
   roots λ, μ, μ̄; Binet coefficients all nonzero since γ ≠ 0
   (Vandermonde/DFT weights of equal modulus 1/(3d^{2/3})); **rational
   integer coefficients ⟹ Sha's Galois parameter d = 1**.
5. **Forward window (elementary).** After reduction, k₊ = O(1) absolutely
   — the R's cancel; constant small via R ≥ 0.28119… [ADF 2016].
6. **Backward window (Baker, black-box).** Reverse the recurrence
   (legitimate: a₀ = ±N(ε) = ±1 keeps it integral); the reversed
   sequence has exactly two maximal-modulus roots (1/μ, 1/μ̄) whose
   quotient μ̄/μ is not a root of unity (else ε^j real for some j —
   impossible in a complex cubic except ±1: **Local Lemma B**, three
   lines). Apply Sha Thm 1.2 verbatim: zero indices ≤ N₂ = 2^{O(s)}
   (explicitly ≤ e^{22.5R}·poly). *Optional upgrade (not needed for the
   theorem): re-run Sha's endgame with the true ratio gap 3R/2 to get a
   quasi-linear window k₋ = O((h(γ)+R)·log(·)) — our own theorem citing
   his Lemma 2.8 + the Matveev step.*
7. **The walk.** For each representative × sign × k in the two windows
   (2^{O(s)} values), compute z_k by exact integer recurrence iteration —
   each z_k has 2^{O(s)} digits, total 2^{O(s)} bit-ops — collect the
   zeros, output (x, y) = (z-coordinates). Completeness: bnfisintnorm
   semantics (all norm-solutions = reps × norm-positive units; our ⟨±ε⟩
   walk covers the superset) [PARI docs verified + our empirical orbit
   check; in the write-up, replace PARI by step 2's own representatives].

Total: deterministic 2^{O(s)}. ∎ (modulo Lemmas A, B and the BW-constant
verification below)

## Remaining work items (all bookkeeping-hard)

- **Lemma A** (tracked-generator compact representations, rank 1) —
  direct proof, ~1 page; Thiel's general version is not verbatim-citable
  (thesis inaccessible).
- **Lemma B** (μ̄/μ not a root of unity) — three lines, write it.
- **BW constants at n = 3**: confirm Williams' spacing theorem (Pacific
  J. Math. 124 (1986)) covers all complex cubic orders; only existence of
  the constants matters.
- Exactness bookkeeping: interval-arithmetic precision claims in steps 1,
  3 (standard; cite Schoof's "polynomial in log|Δ|" algorithm statements).
- Then: hostile referee pass (in series), and the write-up positioned
  against Smart 1996 with the prototype (1120/1120 vs PARI) as the
  computational companion.

## Why this matters for Smale #5

This is the first stratum with **certified genus-1 curves and unbounded
coefficients decided in worst-case exponential time** by an assembled,
fully-cited argument — the G2 wall breached at its thinnest point, using
the orbit-compression philosophy (decide without exhibiting) that the
quadratic layer pioneered. The same skeleton is the template for general
complex cubic forms (rank 1) and, more distantly, the rank-2 frontier.
