# A1-v2: cubic Thue via unit orbits — the Pell walk one rung up

Draft v1 · 2026-07-21 · status: reduction designed, prototype validated
(1120/1120 exact solution-set agreement with PARI's certified `thue`),
key bound conjectured with strong empirical support (max index 3), proof
plan explicit. This attacks the sharpest gap the citation pass exposed:
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

   **Provable weak form (proof sketch, poly window — enough for EXP).**
   Writing c₂(k) = A·λᵏ + 2Re(B·μᵏ) with λ = σ_real(ε), μ the complex
   embedding: A = w₁σ₁(γ) ≠ 0 always (N(γ) = m ≠ 0 kills σ₁(γ) = 0, and
   the interpolation weights wᵢ are nonzero by Vandermonde nondegeneracy
   — the degenerate Skolem case simply cannot occur here). Vanishing
   forces (|λ/μ|)^|k| ≤ 2|B/A|, and |λ/μ| = e^{3R/2}, so
   |k| ≤ (2/3R)·log(2|B/A|) + O(1). Bounding log|B/A| by the
   representative's embedding spread (≤ O(R + log|m|) after unit
   reduction) plus the weight ratio (≤ O(log d) = O(s)), and using the
   absolute lower bound on complex-cubic regulators (minimum at
   x³ − x − 1, R ≈ 0.28), gives unconditionally
   > |k*| ≤ C·s — a polynomial window,
   which is all the EXP claim needs; the O(1) empirics reflect
   log|m|/R being tiny on the grid. To be written up with explicit
   constants and the unit-reduction lemma.
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
