# The frontier of Smale's 5th problem — claim map

Status legend: **[V]** machine-verified in this repo · **[C]** cited &
adversarially checked (citation workflow, nine verifiers, 2026-07-20) ·
**[P]** pending. Rule adopted after this pass: primary sources only —
Wikipedia was the error vector for both of our wrong claims.

## Problem statement [C — corrected 2026-07-20]

Smale's 5th problem ("Height bounds for diophantine curves", in *Mathematical
problems for the next century*, Math. Intelligencer 20(2) (1998) 7–15;
reprinted AMS 2000): decide whether f(x,y) = 0 (f ∈ ℤ[u,v]) has a solution in
ℤ² in time **2^(s^c)** for a universal constant c — *exponential time*
2^(poly(s)). NOT the single-exponential (2^s)^c that Wikipedia prints; the
primary PDF and Lagarias's quotation of the AMS reprint (arXiv:math/0611209
§1.4) agree on 2^(s^c). Our earlier draft inherited Wikipedia's rendering —
caught by the citation workflow.

Size is **dense**: s(f) = Σ_{|α| ≤ d} max(log|a_α|, 1) — every exponent slot
up to total degree d contributes ≥ 1, so s(f) ≥ ~(d+1)(d+2)/2. Smale states
even decidability is open. His **Height Bound Hypothesis** (positive-genus
curve solvable ⇒ a solution of log-height poly(s)) would put the
positive-genus case in NP.

## Hardness floor [C — rescoped 2026-07-20]

- **ℕ-variant NP-complete**: Manders–Adleman, *NP-complete decision problems
  for binary quadratics*, JCSS 16(2) (1978) 168–184: {⟨a,b,c⟩ : ∃x,y ∈ ℕ,
  ax² + by = c}, binary encoding. Companion: bounded quadratic congruence
  (Garey–Johnson AN1), NP-hard even given the factorization of b. Caution:
  the authors' own tech report (ERL M78/30 §2.2) wrongly claims the ℤ-variant
  is poly-time via Jacobi symbols — do not cite that sentence.
- **Over ℤ the floor is thinner than we first wrote**: the ℤ-variant of
  ax² + by = c is in NP ∩ coNP (≡ quadratic residuosity mod |b|; contains the
  Goldwasser–Micali QR problem; not NP-complete unless NP = coNP). Lagarias
  (FOCS 1979; arXiv:math/0611209): solvability of the general binary
  quadratic over ℤ is in NP, and decidable in time 2^(O(L)).
  **Open (Track B target): is two-variable H10 over ℤ NP-hard at all?**
  **[V]** Beyond the Lagarias stratum, two clauses proved and implemented
  here: rational-function graphs (degree 1 in one variable;
  Runge-in-miniature window, `smale5/solvers/graph.py`) and constant-lead
  degree-2 fibers with discriminant square-class ≤ 2 (conic + divisibility
  as an orbit congruence, `smale5/solvers/deg2fiber.py`) — `notes/A1.md`
  clauses (iii) and (iv).
- **[V]** Pell witness sizes: fundamental solution of x²−61y²=1 is
  (1766319049, 226153980); record digits(t) reach 278 by d = 17341 with
  log₁₀ t ≈ 2√d (`experiments/data/pell_records.csv`); d = 1000099 has a
  1128-digit fundamental solution yet decides instantly via LMM/PQa.
  **[C]** theory: R_d < √d(log 4d + 2) (Schur 1918 / Hua BAMS 1942 /
  Lenstra Notices AMS 2002); Lenstra: infinitely many d (families d₀d₁^{2n},
  non-squarefree) with R_d = c√d exactly ⇒ digit counts exponential in the
  bit-size of d infinitely often; for squarefree d even R_d > d^δ i.o. is
  open (best: Yamamoto 1971, (log √D)³).

## Structure [C]

- **Siegel 1929** (*Über einige Anwendungen diophantischer Approximationen*,
  Abh. Preuss. Akad. Wiss. 1929 Nr. 1 — Abhandlungen, not the
  Sitzungsberichte Wikipedia lists): a geometrically irreducible affine curve
  has infinitely many integral points only if genus 0 with ≤ 2 places at
  infinity (places over ℚ̄ on the normalization). Exact iff-classification:
  Silverman 2000; Poulakis, Proc. AMS 131 (2003); Alvanos–Bilu–Poulakis,
  IJNT 5 (2009). Encoded as routing metadata in `smale5/classify.py`.
- **Baker-type bounds [C — with a sting]**: Thue (Baker, Phil. Trans. A 263
  (1967/68); best general: Bugeaud–Győry, Acta Arith. 74 (1996), Győry–Yu
  2006): log max(|x|,|y|) < c(d)·H^(2d−2)(log H)^(2d−1)·log B — polynomial in
  the coefficient **magnitude** H, i.e. exponential in its bit-size.
  **Consequence (this pass's sharpest yield): even fixed-degree Thue
  equations are not known decidable in time 2^(s^c) via height bounds** —
  enumeration to the bound is doubly exponential. Genus 1: Baker–Coates 1970
  is triple-exponential in H; Schmidt (Compositio 81 (1992)) single-exp.
  Mordell y² = x³+k: Baker's exp{(10¹⁰|k|)^(10⁴)} (parenthesized — secondary
  sources misquote it), Stark 1973: exp(C_ε|k|^(1+ε)).
- **Effective Mordell [C — corrected & updated]**: Faltings 1983, Vojta 1991,
  Lawrence–Venkatesh 2020 are all height-ineffective for genus ≥ 2 (uniform
  *counting* is now proven — Dimitrov–Gao–Habegger, Kühne — but uniform ≠
  effective). Baker IS effective for hyperelliptic/superelliptic *models* of
  any genus; effectivity is open already for genus-2 minus a non-Weierstrass
  point (dense families: Corvaja–Lombardo–Zannier, arXiv:2411.17930).
  Conditional routes: Elkies (IMRN 1991, abc ⇒ Mordell, effective reduction);
  effective Vojta; Kim's program + Bloch–Kato + Kim's conjecture
  (effective depth-2: Balakrishnan–Dogra, Compositio 155 (2019)).
  **2024–26**: Alpöge–Lawrence, *Conditional algorithmic Mordell*
  (arXiv:2408.11653): explicit algorithm for C(K), termination conditional on
  Hodge + Tate + Fontaine–Mazur; Garcia-Fritz–Pasten (arXiv:2503.10443):
  unconditional effective heights for curves with enough automorphisms.
- **Hall / Mordell data [C]**: Hall's original conjecture (1971) has NO ε:
  |x|^(1/2) < C|k| (believed false, not disproved; Hall suggested C = 5);
  weak form 2+ε: Stark–Trotter ~1980; Danilov 1982: exponent optimal.
  Gebel–Pethő–Zimmer (Compositio 110 (1998)): all |k| ≤ 10⁴ (partial 10⁵);
  **Bennett–Ghadermarzi (LMS JCM 18 (2015)): all |k| ≤ 10⁷**. Largest known
  Hall ratio: Elkies, 46.6 at k = −1641843. **[V]** our sweep rediscovered
  the classical extremal point x = 5234 (ratio 4.2557), one of only three
  records to x = 10⁷ (`experiments/data/hall_records.csv`).

## Undecidability calibration [C — attribution fixed]

Over ℕ: undecidable in 9 unknowns — **Matiyasevich's theorem** (announced
1975), full proof written up by Jones (JSL 47 (1982)), who credits
Matiyasevich (we had the attribution backwards). Over ℤ: 11 unknowns,
Zhi-Wei Sun (announced 1992; Sci. China Math. 64 (2021)). Over ℤ, ν = 1 is
decidable and every 2 ≤ ν ≤ 10 is open; the two-variable case is open in
both directions (Gasarch, arXiv:2104.07220). Post-2024: H10 undecidable over
rings of integers of all number fields (Koymans–Pagano; Alpöge–Bhargava–
Ho–Shnidman); over ℤ[i]: 20 unknowns (Matiyasevich–Sun 2025), 18 (2026).

## Toolchain [C]

PARI `thueinit(P, flag≠0)` certifies unconditionally (verbatim from the
2.17.4 docs; default flag 0 assumes GRH). Caveats: finiteness precondition on
P (else domain error); failures are loud (overflow errors), never silent
truncation; irreducible P with no real root is decided by |a|^(1/deg)
enumeration. **[V]** used by `smale5/solvers/thue_pari.py`.

## Repo-local verified artifacts [V]

- x³ − 2y³ = 19: passes all prime-power congruence filters ≤ 81, certified
  unsolvable by PARI — NO can live strictly beyond local reasons.
- y² = x³ + 7: pipeline honestly returns UNDECIDED (the classical proof is
  global; congruence filters pass).
- Full citation list with URLs: `notes/citations/` (workflow output,
  2026-07-20).
