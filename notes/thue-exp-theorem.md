# Theorem draft v2: pure-cubic Thue equations decide in exponential time

v2 · 2026-07-22 · post-referee. The hostile referee (report archived in
the log; its from-scratch mini-implementation matched certified `thue`
13/13 including the high-index fields d = 12, 45, 175) broke draft v1 in
two places and repaired every break. All referee corrections applied.

## Statement (minimal honest form, referee-endorsed)

> **Theorem (modulo Lemmas A and C).** There is a deterministic,
> unconditional algorithm that, given cube-free d ≥ 2 (not a cube) and
> m ≠ 0 in binary, input size s = O(log d + log m), decides whether
> x³ − d·y³ = m has a solution in ℤ² — listing all solutions — in time
> 2^{O(s)}.
> Lemma A (~1 page) and Lemma C (~2 pages) have all ingredients verified
> to exist; neither is conceptually open.

**The v1 fatal flaw, preserved as a lesson**: v1 cited Sha's Thm 1.2
"black-box, window 2^{O(s)}" — but that bound's s was the extraction's
*redefined* size max(R, h(γ), log m, log d) ⊇ R, and R = 2^{Θ(s_input)}:
in input size the black-box window e^{22.5R} is **doubly exponential**
(measured: d = 9986 has R ≈ 2605, window ≥ 10^{25,454}). Third instance
of the expedition's recurring trap — always ask *exponential in what*.

## Proof skeleton (v2, all referee repairs applied)

1. **Regulator and unit, no class group.** At rank 1 the class group is
   never used: compute R and the cycle by Buchmann–Williams Alg 2.13
   (Math. Comp. 50 (1988) 569–578, Prop 2.14): deterministic O(R·D^ε)
   bit-ops, unconditional, published with proof; R = 2^{O(s)} via
   hR ≤ |Δ|^{1/2}·polylog. ε in expanded form costs 2^{O(s)} digits —
   affordable and needed in step 4 anyway. (Lenstra 1992 Thm 5.5's
   deterministic |Δ|^{3/4} — not 1/2, and hedged "appears to be true" —
   is a fallback citation only.)
2. **Norm-equation representatives.** Trial-divide m; enumerate the
   ≤ d₃(|m|) ideals of norm |m| **in O_K** (Dedekind basis; splitting at
   p | 3b via O_K/pO_K); per candidate: principality + generator by the
   BW baby-step cycle walk (Prop 4.5, O(R·D^ε); Thm 4.7's R^{1/2} rate
   is decision-only). Generators via **Lemma A**.
3. **Unit reduction** (our lemma, referee-sharpened): representatives
   with |log|σ₂(γ')| − ⅓log|m|| ≤ R/4, so |σ₂/σ₁| ≤ e^{3R/4}.
4. **Orbit and recurrence.** z_k = α²-coordinate of γ·(±ε^k), cleared by
   **3b** (NOT 3: for d = ab² cube-free, [O_K : ℤ[α]] = b·(3 if d ≡ ±1
   mod 9 else 1) — Dedekind 1900; referee falsified v1's claim at 91
   values of d < 500, e.g. d = 12, 45, 175). Integer recurrence of order
   3, char poly = min poly of ε; N(ε) = λ|μ|² > 0 forces **N(ε) = +1
   always**. Simple roots; Binet coefficients nonzero (γ ≠ 0, DFT
   weights of modulus 1/(3d^{2/3})); Sha's Galois parameter d = 1.
   Expanding ε and z₀, z₁, z₂ to their 2^{O(s)} digits is part of this
   step's stated cost.
5. **Forward window (elementary, SOUND).** Vanishing at k > 0 forces
   λ^{3k/2} ≤ 2e^{3R/4}, so k₊ ≤ ½ + (2log2)/(3R) ≤ 2 with
   R ≥ 0.28119 (ADF 2016) — plus one rounding slack: **k₊ ≤ 3, exactly
   the empirical maximum**.
6. **Backward window = Lemma C (REQUIRED, to be written ~2 pages).**
   Reverse the recurrence (integral since N(ε) = 1); two maximal-modulus
   roots form the conjugate pair (quotient not a root of unity — Lemma
   B), third root tiny. Re-run Sha's endgame with the TRUE ratio gap
   3R/2 and direct height choices (A₁ = π, A₂ ≤ 12h(γ)+π, A₃ ≤ 4R —
   the R cancels against the gap): k₋ = O((h(γ)+1)·log(h(γ)+2)) =
   O((log|m| + R)·log(·)) = 2^{O(s)}. The Λ = 0 degenerate subcase is
   trivial here: b₂ = b̄₁ exact cancellation leaves b₃λ^{−n} ≠ 0.
   Ingredients: Sha's Lemma 2.8 + the Matveev application, both
   extracted verbatim; the assembled statement is ours.
7. **The walk.** For every representative × sign × k in the two windows:
   exact integer recurrence iteration (2^{O(s)} digits each; 2^{O(s)}
   total), collect z_k = 0 hits, recover (x, y), and apply the
   **mandatory final filter x³ − d·y³ = m** (the walk also emits
   norm-(−m) elements). Windows apply to the UNIT-REDUCED
   representatives (stated). Completeness (ideal-theoretic, PARI-free):
   any solution γ = x − yα ∈ ℤ[α] ⊆ O_K generates an ideal of norm |m|
   among step 2's list; unit orbits under ⟨−1, ε⟩ (full unit group:
   torsion {±1} by the real embedding) cover all generators; γ ↦ −γ
   swaps ±m and the ±-walk covers it. ∎ (modulo A, C)

## Lemma B (root-of-unity exclusion): SOUND, referee-verified

(As in v1, with the cosmetic fix: the contradiction is "σ₂(ε^j) real",
not "ε^j real" — σ₁(ε^j) is always real.)

## Lemma A (tracked generators): referee-repaired plan

The v1 sketch had one thin claim and one muddled claim. Repairs:
- Height bounds come from **BW88 Prop 2.11** (minima are φ-represented
  with poly-size data — explicitly contrasted with coordinates "as large
  as exp √D") and **Prop 3.1(ii)** (composition-then-reduce distance slip
  bounded by c₄ = 2log(D/3), c₅ = 0 at n = 3) — NOT Schoof Prop 7.1.
- The terminal test: maintain the exact invariant I_i = (product so
  far)·I₀ by construction — floats only steer; terminal equality is one
  exact HNF test. Or simpler (referee's simplification, adopted): at the
  2^{O(s)} budget, take the **plain incremental product of the ≤
  7R/log 4 neighbor minima along the cycle** (Williams' sharper
  ε₀ > τ^{p/2} gives p < 2R/log τ ≈ 4.16R) — compact representations are
  a luxury needed only for poly-size *certificates*, not for the EXP
  algorithm. Lemma A then also delivers ε for step 1.

## BW constants: VERIFIED, work item closed

(j, c₁) = (7, log 4) confirmed against the actual Math. Comp. scan and
Williams, *The spacing of the minima in certain cubic lattices*, Pacific
J. Math. 124 (1986) 483–496 — whose scope is ALL complex cubic fields
and arbitrary reduced lattices. Sharper: θ₈ > 4 and ε₀ > τ^{p/2}. Venue
correction: "Continued fractions and number-theoretic computations" is
Rocky Mountain J. Math. 15 (1985) 621–656, not PJM.

## Lemma C (written): the backward window, quasi-linear in R

> **Lemma C.** Let γ be a unit-reduced norm-m representative, v_n the
> 3b-cleared α²-coordinate sequence of γ·ε^{−n} (n ≥ 0). There is an
> absolute, explicitly computable constant c such that v_n ≠ 0 for all
> n > N_C := c·(R + log|m| + log d + 1)·log(R + log|m| + log d + 2).

*Proof.* Write v_n = b₁λ^{−n} + b₂μ^{−n} + b̄₂μ̄^{−n} with all bⱼ ≠ 0
(γ ≠ 0), μ^{−1} = e^{R/2}e^{iθ}, b₂ = |b₂|e^{iφ}. If v_n = 0 then
2|b₂|e^{nR/2}|cos(φ + nθ)| = |b₁|e^{−nR}, so with
|cos x| ≥ (2/π)·dist(x, π/2 + πℤ):
  dist(φ + nθ, π/2 + πℤ) ≤ (π/4)(|b₁|/|b₂|)·e^{−3nR/2}.   (†)
The left side is |Λ_n| for the linear form
Λ_n = a·log(−1) + log(b̄₂/b₂) + n·log(μ̄/μ), a ∈ ℤ, |a| ≤ n + 2.
**Degenerate case is void**: Λ_n = 0 would give b₂μ^{−n} + b̄₂μ̄^{−n} = 0
purely imaginary contribution — wait, precisely: Λ_n = 0 makes the
conjugate-pair term vanish, leaving v_n = b₁λ^{−n} ≠ 0; so on a zero
v_n = 0 we always have Λ_n ≠ 0 and Matveev applies.
Matveev (k = 3, field degree D₀ ≤ 12 = deg of the Galois closure of
K(ω)): log|Λ_n| > −C₀·A₁A₂A₃·log(e(n+2)) with C₀ = 2^{40}·D₀²·log(eD₀)
absolute, A₁ = π, and:
- A₂ ≤ D₀·h(b̄₂/b₂) + π ≤ D₀·2h(b₂) + π. Heights directly (Galois
  invariance of the Weil height; the 3b-clearing shifts by ≤ log 3d):
  h(b₂) ≤ h(γ) + log 3 + (2/3)log d + log 3d =: H₁, so
  A₂ ≤ 24·H₁ + π = O(h(γ) + log d + 1).
- A₃ ≤ D₀·h(μ̄/μ) ≤ D₀·2h(ε) = D₀·(2R/3) ≤ **8R** — since a unit of a
  complex cubic has h(ε) = R/3.
Combining with (†) and |log(|b₁|/|b₂|)| ≤ 12·H₁ (|log|b|| ≤ deg·h):
  (3R/2)·n ≤ 12H₁ + log(π/4) + C₀·π·(24H₁+π)·8R·log(e(n+2)).
Divide by 3R/2: **the R cancels in the Matveev term**, leaving
  n ≤ 8H₁/R + c₂·(H₁ + 1)·log(e(n+2)),  c₂ absolute explicit.
Resolving n against log n (x ≥ 2A log A ⟹ x/log x ≥ A) and inserting
the unit-reduction bound H₁ = O(log|m| + R + log d) gives N_C as stated;
in particular N_C = Õ(R + s) = 2^{O(s)} — quasi-linear in R, in place of
v1's fatal e^{22.5R}. ∎
*(Final write-up bookkeeping flags: compute D₀ exactly (≤ 12); the
constant c traced through 2^{40}·D₀²·log(eD₀)·8π·24; branch conventions
for log(−1) absorbed into |a| ≤ n+2 — all mechanical.)*

## Lemma A (written, referee-simplified): generators along the cycle

> **Lemma A′.** Fixed degree, unit rank 1, cycle length p < 2R/log τ + 1
> (Williams: ε₀ > τ^{p/2}, τ the golden ratio). The neighbor minima
> x₁, …, x_p of the reduced-ideal cycle each carry poly(s)-size data
> (BW88 Prop 2.11), and the incremental exact products γ_k = x₁⋯x_k
> (2^{O(s)} digits each) satisfy: the k-th reduced principal ideal is
> (γ_k), and ε = γ_p. Hence every principality witness and ε itself are
> computable, expanded, in deterministic total time 2^{O(s)}, with exact
> HNF verification of each ideal identity.

*Proof.* The infrastructure cycle at rank 1 is the sequence of reduced
principal ideals I_k = (γ_k)^{−1}-normalized with I_{k+1} = I_k/(x_k)
for the neighbor minimum x_k of I_k; BW88 Prop 2.11 gives x_k as
poly(s)-size data (denominator ≤ √D, numerator coordinates < √D in the
φ-representation), Prop 3.1(ii) controls the distance slip, and the
Williams spacing bound caps p. The products γ_k are maintained by exact
integer arithmetic (digit growth ≤ Σ poly(s) ≤ 2^{O(s)}; total cost
2^{O(s)}); each step's ideal identity I_{k+1}·(x_k) = I_k is one exact
HNF comparison — floats never certify, only steer the walk's bookkeeping.
Compact representations (binary doubling) are needed only if poly-size
*certificates* are desired; the EXP algorithm does not need them. ∎

## Remaining work

- Second referee pass on Lemmas A′ and C (narrow scope).
- Then the manuscript: positioned against Smart (ANTS-II 1996), with
  the prototype (1120/1120) and the first referee's independent 13/13
  as computational companions.
