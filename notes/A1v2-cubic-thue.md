# A1-v2: cubic Thue via unit orbits — the Pell walk one rung up

Draft v2 · 2026-07-21 · status: reduction designed, prototype validated
(1120/1120 exact solution-set agreement with PARI's certified `thue`),
citation pass complete (5 verdicts, archived in
`notes/citations/2026-07-21-a1v2-verification.json`) — and the citation
pass UPGRADED the goal: the "modulo bnf" hypothesis is dischargeable
unconditionally, and the assembled theorem appears to be a citable gap
in the literature (closest prior: Smart, ANTS-II 1996). See "After the
citation pass" below. This attacks the sharpest gap the citation pass exposed:
**even fixed-degree-3 Thue equations are not known decidable in time
2^(s^c)** — height bounds are exponential in coefficient bit-size, so
enumeration is doubly exponential (`notes/frontier.md`, "the Thue sting").

## The reduction (complex cubic case, prototyped on x³ − d·y³ = m)

Let K = ℚ(α), α = ∛d (d cubefree, not a cube): a *complex* cubic field —
one real embedding, one conjugate pair — so the unit group is ⟨−1, ε⟩ of
**rank 1**. A solution (x, y) is an element γ = x − y·α with Norm(γ) = m.

1. **Classes.** Norm-m elements fall into finitely many orbits under the
   unit action: representatives from `bnfisintnorm` (the LMM analogue).
2. **The Thue condition is one coordinate.** γ·(±ε^k) has coordinates in
   the basis (1, α, α²); being of Thue shape x − y·α means the
   α²-coordinate **vanishes**. Multiplication by ε is an integer 3×3
   matrix, so k ↦ c₂(k) is an order-3 linear recurrence: deciding whether
   it hits 0 is a **Skolem instance of order 3** — the classically
   decidable range (Mignotte–Shorey–Tijdeman / Vereshchagin; citation to
   be pinned by the next verification pass).
3. **Dominant root kills all large k.** The embeddings of ε have moduli
   (|λ|, |λ|^(−1/2), |λ|^(−1/2)) with R = log|λ| the regulator, so
   c₂(k) = Σ aᵢλᵢᵏ has modulus-gap (3/2)·R per step. Once the dominant
   term leads, it never vanishes again: the last vanishing index obeys
   k* ≲ C·(1 + h(rep)/R), and unit-reduced representatives have
   h(rep) = O(R + log|m|), giving the

   > **Conjecture (window bound, strong form).** For unit-reduced class
   > representatives, every Thue-shape index satisfies
   > |k| ≤ C·(1 + log|m| / R) for an absolute constant C.

   Empirics: across 1120 grid cases (14 fields × m ∈ [−40,40]) the max
   vanishing index was **3** (`experiments/cubic_orbit_prototype.py`).

   **Window bound, corrected split (2026-07-21, self-caught overclaim).**
   Writing 3δ²·c₂(k) = σ₁(γ)·λᵏ + 2Re(ζ·σ₂(γ)·μᵏ) with λ = σ_real(ε) > 1,
   |μ| = λ^(−1/2), and all interpolation weights of equal modulus 1/(3δ²)
   (DFT structure of the power basis): the degenerate Skolem case cannot
   occur (N(γ) = m ≠ 0 forces σ₁(γ) ≠ 0).

   - **Positive direction (elementary).** Vanishing forces
     λ^{3k/2} ≤ 2|σ₂(γ)/σ₁(γ)|, so k ≤ (2/3R)·log(2B/A) + O(1) — with
     unit-reduced representatives and the absolute lower bound on
     complex-cubic regulators (minimal field x³ − x − 1, R ≈ 0.28;
     citation pending), a poly(s) bound with explicit constants.
   - **Negative direction (this is where Baker hides — my earlier "no
     linear forms in logarithms" claim was WRONG and is hereby retracted).
     ** For k ≪ 0 the complex pair dominates and exact vanishing requires
     |cos(φ + k·arg μ)| ≤ (A/2B)·λ^{3k/2} — the unit's angle must
     approximate π/2 (mod π) super-exponentially well in |k|. Bounding the
     largest such k IS an inhomogeneous linear form in logarithms;
     Baker–Wüstholz gives an effective k₀ = 2^{O(s)} (polynomial decay of
     the form vs exponential demand). Large solutions (|y| big, real
     embedding small) live precisely on this side, which is why the
     argument cannot be elementary: otherwise Thue would be effective
     without Baker.

   **Net effect — the reduction gets STRONGER, not weaker**: no conjecture
   is needed. Both windows are effectively bounded (elementary + one Baker
   inequality), each ≤ 2^{O(s)}, and each orbit element costs 2^{O(s)}
   bit-operations, so:
   > **Reduction (now unconditional modulo bnf).** Pure-cubic Thue
   > decision in time 2^{poly(s)} follows from certified fundamental-unit
   > and class-representative data computable in time 2^{poly(s)}.
   The strong O(1 + log|m|/R) window remains an (empirically supported)
   conjecture; max observed index 3.

   **Priority caveat for the citation pass**: reorganizing Thue along the
   unit orbit with Baker supplying one inequality is morally close to the
   classical algorithmic pipeline (Tzanakis–de Weger, Bilu–Hanrot). Our
   likely contribution is the explicit EXP-modulo-bnf accounting and the
   sharp empirical window, not the skeleton — to be checked, not assumed.
4. **Certified zero-testing without materialization is available if ever
   needed**: |c₂(k)| ≤ 2^(O(s)) digits, so c₂(k) ≡ 0 modulo a prime set
   with product exceeding the height bound certifies c₂(k) = 0 in
   2^(O(s)) bit-operations. With k* = O(1) the point is moot — the walk
   materializes at most ε^(±(k*+1)).

## What this buys, stated honestly

> **Reduction (target theorem).** For complex cubic forms, Thue decision
> in time 2^(poly(s)) **follows from**: (a) the window bound above (proof
> plan: elementary embedding inequalities — no linear forms in logs
> needed, which is the whole point), and (b) certified fundamental-unit +
> class-representative data (bnf) computable in time 2^(poly(s)).

The wall thus MOVES: from "height bounds are doubly exponential" to a
concrete computational-algebraic-number-theory kernel — *certified bnf
data for complex cubics in exponential time* — exactly where compact
representations (Buchmann-school) live. That is a much better wall to
stare at, and it is the direct analogue of what our LMM/PQa layer already
does for real quadratics.

Unit sizes are genuinely the obstruction being dodged: by s = 20 the
fundamental unit's coefficients reach 1593 digits, all records certified
(`experiments/data/cubic_unit_records.csv`) — steeper than the Pell
envelope (~145 digits at the same size).

## Gaps and next steps

- **Prove the window bound** for pure cubics first (explicit embedding
  inequalities on |c₂(k)|; the degenerate case a_dominant = 0 must be
  ruled out — expected: only for γ = 0).
- **Citation items for the next verification pass**: Skolem order-3
  effectivity attribution; complexity of certified bnfinit/bnfcertify;
  whether bnfisintnorm's representative heights are unit-reduced.
- **Generalize** from x³ − d·y³ to arbitrary irreducible complex cubic
  forms (negative discriminant): same rank-1 skeleton, ℤ[α] bookkeeping
  heavier.
- **Totally real cubics (rank 2)** are the honest hard case: the
  vanishing locus lives on a ℤ²-lattice of units — S-unit-equation
  flavor, no dominant root. Deferred, explicitly.
- **Promotion path**: once the window bound is proved, port the prototype
  from `experiments/` into `smale5/solvers/` with certified caps and the
  never-overclaim contract, and A1 gains clause (v).

## After the citation pass (2026-07-21, five verdicts)

1. **Skolem attributions pinned.** Order ≤ 4 decidable: Mignotte–Shorey–
   Tijdeman (Crelle 349, 1984) + Vereshchagin (Math. Notes 38, 1985), via
   Baker + p-adic methods; effective zero-index bounds of magnitude
   2^poly exist (Chonev–Ouaknine–Worrell JACM 2016 App. C; coRP at order
   ≤ 4: Bacik–Ouaknine–Worrell SODA 2026). For our dominant-real-root
   order-3 case, **Min Sha (J. Number Theory 197, 2019) gives fully
   explicit zero-free thresholds** — the exact tool for the window
   constants. ("Skolem meets Bayes" does not exist; the real papers are
   Skolem-Meets-Schanuel and Skolem-Meets-Bateman–Horn. Corrected.)
2. **The bnf hypothesis is dischargeable — unconditionally.** For FIXED
   degree, certified class group + units are computable in deterministic
   time |Δ|^(1/2+o(1)) = 2^(O(s)) with units in compact representation
   (Lenstra, Bull. AMS 26 (1992), Thm 5.5; Schoof, MSRI 44 (2008), §11 —
   Arakelov class group). Buchmann's subexponential is heuristic-laden
   (GRH + smoothness), rigorous-under-GRH only for quadratics — cite
   carefully.
3. **Minimal complex-cubic regulator**: R = log(plastic number) =
   0.2811995743…, attained uniquely at disc −23 (x³−x−1); sharp bound
   proven by Astudillo–Díaz y Díaz–Friedman (JNT 167, 2016) — NOT Artin;
   only three fields (−23, −31, −44) lie below 0.79. Do not say "smallest
   regulator of any number field" (that is 0.205216…, a sextic).
4. **bnfisintnorm semantics confirmed** (PARI 2.17.4, verbatim + an
   empirical orbit check): complete system modulo units of POSITIVE norm;
   our ⟨±ε⟩ walk covers a superset of those orbits, so the prototype's
   completeness stands. Two load-bearing caveats: representatives are NOT
   size-reduced (the docs' own example overflows 100 GB when expanded —
   the walk must unit-reduce reps first; since 2.17.0 a compact-form flag
   exists), and results are GRH-conditional unless `bnfcertify(bnf) = 1`.
5. **Priority verdict — the theorem is a citable gap.** No source states
   a worst-case "fixed-degree Thue decidable in exponential time" theorem
   (with or without bnf given). Closest prior, must be positioned
   against: **N. P. Smart, "How difficult is it to solve a Thue
   equation?", ANTS-II 1996** — a complexity estimate for the
   Tzanakis–de Weger method (reduction phase polynomial in the regulator
   and input; small-solutions phase O(|m|^(1/(d−2)))), heuristic-unit-
   supply assumed, practical failure modes noted. Everything else
   (TdW 1989, Bilu–Hanrot 1996, all books/surveys checked) states
   effectivity only.

**Upgraded target (assembly theorem).**
> Pure-cubic Thue equations are decidable, with full solution list, in
> deterministic time 2^(O(s)) — unconditionally.
Assembly: certified bnf in 2^(O(s)) (Lenstra/Schoof) → norm-equation
class representatives → unit-reduce → orbit walk with the two-sided
window (elementary + one Baker/Skolem inequality with Sha-explicit
constants). Remaining verification items before claiming it: (i) the
complexity of the norm-equation representative step given certified bnf
(ideal enumeration above divisors of m + principal-ideal generators —
believed 2^(O(s)), needs a careful write-up); (ii) rep unit-reduction
lemma; (iii) the explicit negative-window constants. None looks
conceptually hard; all look bookkeeping-hard. This would be the
expedition's first publishable increment, positioned against Smart 1996.
