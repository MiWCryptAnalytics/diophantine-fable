# The frontier of Smale's fifth problem, as this expedition leaves it

Phase-4 synthesis · 2026-07-22 · the position paper the original plan
promised. Everything below is verified at the standard this repo built:
cited from primary sources, adversarially refereed, or machine-checked.

## The problem, correctly stated

Decide f(x,y) = 0 over ℤ² in time 2^{s^c}, dense size s. Decidability
itself open; Baker conjectured decidable (Jones 1981). The popular
(2^s)^c rendering is wrong (our first citation pass, against the primary
PDF).

## What is DECIDED, with our additions (Theorem A1, clauses i–v)

Degree ≤ 2 (Lagarias 1979, re-implemented with LMM/orbit machinery);
univariate; rational-function graphs (iii, ours); constant-lead deg-2
fibers with square-class ≤ 2 (iv, ours — congruence riders on the conic
machinery); pure-square fibers A(x)y² + C(x) at ANY genus (v, ours —
Runge's turnstile past the elliptic wall). Budget-scheduled caps make
the implementation honest; ~50 golden tests; the Census (below) is the
coverage instrument.

**The flagship**: pure cubic Thue equations decide in deterministic,
unconditional 2^{O(s)} (papers/cubic-thue-exp.md/.tex, twice refereed;
window quasi-linear in R; validated 1120/1120 + independent 13/13). The
first stratum with unbounded coefficients and certified genus-1 content
carrying a worst-case exponential decision bound — the G2 wall breached
at its thinnest point.

## The complexity map (Track B, corrected to the primary sources)

- γ-hard and random-hard since 1978 (Adleman–Manders, AKS-modernized):
  L ∈ P ⟹ NP = coNP. Hardness lives in the split (factoring-shaped)
  stratum.
- Open since 1979: deterministic NP-hardness (Adleman–McCurley O33a).
- Membership: A1-fragment ∈ NP (our mini-theorem); cubic Thue ∈ MA
  (ours), ∈ NP ⟺ CVP; full DIOPH2 ∈ NP ⟺ certificate schemes for the
  sporadic strata (HBH + HBH₀ the point-guessing instantiation).
- Emerging picture: decidable-but-not-P, factoring-textured — exactly
  Smale-shaped.

## The five named open problems this expedition minted or sharpened

1. **The strong window conjecture** — orbit vanishing indices
   O(1 + log|m|/R); empirical max 3; forward direction proved (k₊ ≤ 3).
2. **HBH₀** — poly-height solutions on genus-0-sporadic components; the
   hypothesis Smale's NP remark silently needs beyond positive genus.
3. **CVP / the multiplicative-to-additive bridge** — test one plane
   membership for an Arakelov-pinned element; sum-of-square-roots class;
   the single bit separating cubic Thue from NP. Four classical routes
   fail for one unified reason: no additive functional crosses compact
   (multiplicative) representations.
4. **O33a** — deterministic NP-hardness of binary-quadratic
   ℤ-solvability.
5. **DIVIS hardness** — {(A,B) : ∃x, A(x) | B(x)} ∈ NP (two proofs, one
   ours); hardness unstudied.

## The instruments

The Census (every f with dense size ≤ 12; frontier begins at s = 10
with 73 surviving specimens, all elliptic; grinding s = 12 as this is
written); growth envelopes (Pell 278 digits by s = 22; cubic units 1593
digits by s = 20; Hall ratios — three records to 10⁷); HBH empirics
(ratio ≤ 2.38 in-sweep); the errata note on the 1978 memo (three bugs,
one machine-verified counterexample ⟨27, 1343⟩).

## The method, which may outlast the results

Adversarial verification as a way of life: two citation workflows, two
hostile referees, an interrogation panel — which found four real
defects in our code and three in our proofs, every one repaired and
regression-tested. Three size-measure traps caught (Nagell's window;
the caps claim; e^{22.5R}) — the expedition's standing question:
**exponential in what?** And the journal (notes/log.md) as first-class
deliverable: every dead end recorded, because the dead ends are where
the walls show their faces.

## What we would climb next

Prove the window conjecture (elementary-feeling); assault the bridge
(the deep one); generalize the flagship to all complex cubic forms;
O33a; the elliptic stratum to move the Census frontier; rank-2 honestly
last. The mountain has more peaks, and the map is now good.
