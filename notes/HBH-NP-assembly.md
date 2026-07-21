# HBH ⟹ two-variable H10 ∈ NP: the assembly, with honest bookkeeping

Draft v1 · 2026-07-22 · citable-gap #2. Smale (1998) posed the Height
Bound Hypothesis and noted it puts the positive-genus stratum in NP;
nobody has assembled the full-membership statement (landscape survey +
Rojas Remark 4 confirm the gap). Doing the bookkeeping shows the honest
theorem is a *characterization*, not a one-way implication — and yields
an unconditional mini-theorem about our solver strata on the way.

## Mini-theorem (unconditional): the A1-v1 fragment is in NP

Restricted to inputs whose components satisfy clauses (i)–(iv) of
Theorem A1-v1 (`notes/A1.md`), solvability has poly-size certificates:

- **Direct witnesses**: linear, ellipse, parabola, split-hyperbola,
  univariate, graph (iii), and deg2fiber (iv) strata all confine some
  witness to a window of MAGNITUDE 2^{O(s)} — i.e. O(s) bits. Guess it,
  verify by evaluation.
- **Pell-orbit witnesses**: for the indefinite stratum the witness is
  (class representative, sign pattern, exponent k) with k ≤ the orbit
  period mod M ≤ M⁴ = 2^{O(s)} — O(s) bits — and the acceptance
  congruence is verified by **fast matrix exponentiation of σ mod M** in
  poly(s) time. (This generalizes exactly the trick behind Lagarias's
  NP-membership for binary quadratics; our ExtraCong composition keeps
  it working under clause-(iv) congruence riders.)

Nothing here is conditional; the write-up is bookkeeping over machinery
already built and tested in this repo.

## The stratum ledger for full DIOPH2 ∈ NP

Fix f, factor into ℚ-irreducible components (poly time). A YES needs a
certificate for SOME component; NO needs none (NP only). Strata:

1. **Infinite-family components** (Silverman's criterion: genus 0 +
   nonsingular integral point + leading form with ≤ 2 roots, all real):
   Pell-orbit/parametrization certificates as above. For degree > 2
   genus-0 parametrized families this needs the G1 machinery's height
   control — expected poly-bit, to be written (same shape as clause
   (iii)/(iv) windows).
2. **Positive-genus components**: exactly Smale's HBH — solvable ⟹ a
   solution of log-height poly(s). Certificate = the point. CONDITIONAL.
3. **Genus-0 components with finitely many integral points** (≥ 3 places
   at infinity, or no nonsingular integral point): NOT covered by HBH as
   Smale states it (he hypothesizes positive genus). These reduce to
   Thue-type equations whose PROVEN bounds are exponential-in-s bits
   (Bugeaud–Győry shape), so poly certificates need a further
   hypothesis:
   > **HBH₀ (genus-0 sporadic form).** A solvable genus-0 component with
   > finitely many integral points has a solution of log-height poly(s).
   Its plausibility is effective-Roth-flavored (|y| ≤ C(F)·|m|^κ with the
   ineffective constant conjecturally 2^{poly(s)}); it should be stated,
   not smuggled.

## The honest theorem shapes

> **Assembly (conditional membership).** HBH + HBH₀ + (poly-bit
> certificates for the infinite-family stratum, unconditional modulo the
> G1 height-control write-up) ⟹ DIOPH2 ∈ NP.

> **Near-converse.** DIOPH2 ∈ NP forces poly-bit *certificates* — though
> not necessarily poly-height *points* — for every stratum; whether NP
> membership already implies HBH-style height bounds is a separate
> question (certificates could in principle be orbit-compressed even in
> positive genus — cf. how Pell escapes exhibition). So the correct
> slogan is:
> **"DIOPH2 ∈ NP ⟺ every sporadic stratum admits some poly-bit
> certificate scheme"** — with HBH + HBH₀ the natural (point-guessing)
> instantiation, and the Pell/cubic orbit compressions the evidence that
> smarter schemes are sometimes forced.

Combined with Track B (`notes/trackB-hardness.md`): if the assembly
succeeds, DIOPH2 ∈ NP ∩ (γ-hard) — and Baker's decidability conjecture
plus A–M randomized hardness would place two-variable H10 in the same
NP-intermediate-flavored territory as factoring: fully Smale-shaped.

## Next steps

1. Write the mini-theorem properly (fast-exponentiation verifier; the
   ExtraCong composition case) — low risk, all machinery tested.
2. G1 height control for parametrized families (shared with the G1
   solver milestone).
3. State HBH₀ precisely and probe it empirically (the census's genus-0
   UNDECIDED residue at s ≥ 11, if any, is the test set; Thue-family
   minimal-solution data via PARI is cheap to gather).
4. Then the assembly write-up, positioned against Smale 1998 + Lagarias.
