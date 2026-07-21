# Track B: the hardness of two-variable H10 over ℤ — verified picture

2026-07-21/22 · sources: war-council landscape survey, then a two-agent
adversarial series (STOC-1977/ERL-M78/30 reader + hostile referee), both
working from the primary PDF (Adleman–Manders, UCB/ERL M78/30, 1978; page
scans read directly, arithmetic script-verified). Status: **verified** —
every load-bearing claim below survived the referee.

## The theorem that was there all along

> **(Adleman–Manders 1978/79, AKS-modernized.)** The sets
> {⟨a,c⟩ : x² − a²y² = c solvable in ℤ} and
> {⟨a,c⟩ : x(x+ay) = c solvable in ℤ} (even with a restricted to powers
> of 3) are **random complete and γ-complete, unconditionally**.
> Via ⟨a,c⟩ ↦ x² − a²y² − c, the two-variable Hilbert-10 set
> L = {f ∈ ℤ[x,y] : ∃(x,y) ∈ ℤ², f = 0} is γ-hard and random-hard:
> **L ∈ P ⟹ NP = coNP**, and **L ∈ RP ⟹ RP = NP**.

Provenance discipline (referee-enforced): the printed theorems give
*unfaithful* random completeness unconditionally and faithful/γ only under
ERH (Miller's test); substituting AKS in the prime-certification slot —
which consumes no nondeterminism and leaves path weights unchanged —
makes the faithful version unconditional. Cite: A–M ERL M78/30 §2.3
(Thm 2.3.1, Cors 2.3.3/2.3.4) + "Reductions that Lie" (FOCS 1979) + the
AKS substitution. The reduction: SET PARTITION → primes hᵢ ≡ 4^{aᵢ}
(mod 3^{k+1}), c = ∏hᵢ, a = 3^{k+1}; ℤ-direction soundness rides on
sign-symmetry plus the odd-order subgroup ⟨4⟩ ∌ −1.

**Structural note for our program**: both hardness anchors live in the
split-hyperbola stratum of our own pipeline (Δ = 4a² square → divisor
enumeration). The hardness of two-variable H10 concentrates in the
factoring-shaped stratum — not the Pell stratum — matching the
NP-intermediate texture of the quadratic layer (Lagarias's negative-Pell
in NP ∩ coNP).

## What died on the way (the adversarial series earning its keep)

- The survey's proposed path — (ax+1)y = c with CRT "sign-rigidification"
  — is **unfixable**: x = 0, y = c solves it for every (a,c); the trivial
  divisor d = 1 belongs to every congruence class mod everything. No
  instance-side condition can repair it; only solution-side conditions
  (A–M's own "nonzero solution") or a shifted constant term (their
  (3^k·x + 2)y = c) make the set nontrivial.
- **Errata found in the 1978 memo itself** (48 years old): printed
  Thms 1.3.4(1) and 1.3.6 state the trivial (ax+1)-set without the
  "nonzero" qualifier — false as printed (the real theorem is 2.4.2 /
  1.3.9(2)); Thm 2.4.1's printed bound 2·3^k > 1 + Σ|aᵢ| admits a
  concrete false-YES (⟨27, 1343⟩: −79 ≡ 2 (mod 27), (27·(−3)+2)(−17) =
  1343 with the source knapsack a NO) — repaired by 3^k > 1 + Σ|aᵢ|;
  plus a sign slip in the b=1 preprocessing (aₙ₊₁ = 1−2b, not 2b−1) and
  a ≤/≥ typo in Def 1.3.4. The theorems all survive with repairs.

## The corrected status board

- **Hardness (KNOWN)**: L γ-hard and random-hard unconditionally (above).
  The earlier draft of this note said "nobody has claimed hardness" —
  wrong: the landscape agent missed §2.3 of the very memo it cited.
- **Open (the real Track B target)**: *deterministic* Karp NP-hardness of
  ℤ-solvability of binary quadratics = Adleman–McCurley Open Problem
  O33a (ANTS-I 1994), open since 1979. Also open: L ∈ NP? (Lagarias
  covers the quadratic stratum only.)
- **Decidability**: still open; Baker conjectured decidable (Jones, JSL
  46 (1981) §5). The emerging picture — decidable-conjectured, yet
  randomized-hard, with L ∈ P forcing NP = coNP — is exactly the
  "decidable but not in P" texture Smale's problem list anticipates.
- **Upper bounds** (agent-verified, from the survey): Lagarias FOCS 1979
  (binary quadratics + congruence conditions ∈ NP); Tung 1987 (∀∃ over ℤ
  coNP-complete, covering-congruence certificates); Rojas (dim-0 systems
  in PSPACE; generic ∃∀∃ in coNP, exceptional locus = the ∃∃ core);
  MFCS 2025 one-parametric Presburger (∃PrA[t] NP-complete) ⟹ **DIVIS =
  {(A,B) : ∃x, A(x) | B(x)} ∈ NP** — also one line from our graph
  stratum's window. DIVIS hardness: unstudied; closest hit is the
  ℕ-linear-divisibility γ-completeness (x ≥ 1 load-bearing).
- **The two-sided tension** (Rojas math/9809009): computable BigN ⟹ a
  4-variable ∃∃∀∃ class is undecidable.

## Our citable-gap ledger (updated)

1. **Pure-cubic Thue in EXP, unconditionally** (A1-v2 assembly; position
   against Smart ANTS-II 1996) — `notes/A1v2-cubic-thue.md`.
2. **HBH ⟹ two-variable H10 ∈ NP** (assembly: Smale's hypothesis +
   Silverman's refined Siegel + Lagarias certificates) — unclaimed.
3. **The A–M errata note** (misprinted theorems, the 2.4.1 bound bug with
   counterexample ⟨27,1343⟩ and repair, AKS modernization with the
   faithful/unfaithful bookkeeping) — small, concrete, publishable as a
   historical/technical note; our agents found and repaired bugs in a
   foundational 1978 memo.
4. (Retired: the sign-rigidification reduction — killed by d = 1.)

## Census cross-reference (2026-07-21)

The toolkit's own frontier: s = 10, 76 undecided of 43,439 canonical
polynomials, 75 of them certified genus-1 (specimen zero:
x³ − x² + xy² + y² + 1 = 0), one unclassifiable cubic. s = 11: 2,755 of
183,209. An elliptic-integral-points stratum moves the whole frontier.

## Queue

- O33a attack session (deterministic NP-hardness): now the sharpest Track
  B target, with the A–M machinery fully understood.
- Optional: the Siegel/Bombieri–Pila "no range gadgets in two variables"
  barrier theorem — decorative now that hardness rides divisor structure,
  but still a nice standalone statement.
- Citation-verify the remaining survey claims (Baker-conjecture
  attribution, Tung, MFCS 2025) in the next citation workflow.
- Write the A–M errata note properly.
