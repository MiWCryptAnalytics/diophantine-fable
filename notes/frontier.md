# The frontier of Smale's 5th problem — claim map

Status legend: **[V]** machine-verified in this repo · **[C]** cited &
checked · **[P]** pending citation check (do not build on without verifying).

## Problem statement

**[C]** Smale #5 (Smale, "Mathematical problems for the next century", Math.
Intelligencer 20 (1998)): given f ∈ ℤ[u,v] of size s, decide whether
f(x,y)=0 has a solution in ℤ² in time (2^s)^c — single-exponential time.
Even decidability (two-variable Hilbert 10) is open.

## Hardness floor

- **[P]** Manders–Adleman 1978 (JCSS): deciding ∃x,y ∈ ℕ, ax² + by = c with
  binary-encoded coefficients is NP-complete. Pin down the exact ℤ-variant.
- **[V]** Pell minimal solutions are enormous: fundamental solution of
  x² − 61y² = 1 is (1766319049, 226153980) (`tests/test_solvers.py`); in
  general ~2^Θ(√d) — doubly exponential in s = O(log d). **[P]** for the
  general growth statement (regulator bounds). **[V]** empirically: record
  digits(t) reach 278 by d = 17341 with log₁₀t ≈ 2√d
  (`experiments/data/pell_records.csv`); d = 1000099 has a 1128-digit
  fundamental solution yet decides instantly via LMM/PQa. Consequence: a (2^s)^c
  algorithm cannot work by exhibiting solutions; our Pell orbit walk
  (`smale5/solvers/pell.py`) is the constructive counterpoint — decision via
  residue cycles.

## Structure (the positive track's skeleton)

- **[P]** Siegel 1929: an irreducible affine plane curve has infinitely many
  integral points only if genus 0 with ≤ 2 places at infinity. Encoded as
  routing metadata in `smale5/classify.py` (labels never used as decisions).
- **[P]** Baker 1968 / Baker–Coates 1970: effective height bounds for Thue
  and genus-1 integral points; bound shapes to be tabulated precisely
  (they are far above single-exponential in general).
- **[P]** Faltings/Siegel ineffectivity for general genus ≥ 2; conditional
  effective routes: Elkies (abc ⇒ Mordell) with effective abc, Vojta, Kim.
- **[P]** Hall's conjecture vs Baker for Mordell y² = x³ + k: conjectured
  polynomial-in-k integral point bounds vs proven doubly-exponential-in-log-k
  — the Smale-5 gap in miniature. Gebel–Pethő–Zimmer computed all |k| ≤ 10⁴.
- **[V]** The classical stratum is decidable in practice: linear (Bézout),
  all binary quadratics (this repo: ellipse/parabola/split/Pell-orbit paths),
  Thue via PARI `thueinit(·,1)` (unconditional certification — **[P]** for
  the "unconditional" claim from PARI documentation).

## Undecidability heuristic (negative track calibration)

- **[P]** H10 undecidable over ℤ in ~11 unknowns (Zhi-Wei Sun), over ℕ in 9
  (Matiyasevich/Jones); 2-variable case open in both directions. Heuristic:
  Siegel's classification makes 2-variable Diophantine sets too structured to
  encode computation — undecidability would be a shock; the realistic
  "disprove" is a hardness/lower-bound result against (2^s)^c.

## Repo-local verified artifacts

- **[V]** x³ − 2y³ = 19: passes all prime-power congruence filters ≤ 81,
  certified unsolvable by PARI — NO can live strictly beyond local reasons.
- **[V]** y² = x³ + 7: pipeline honestly returns UNDECIDED (the classical
  proof of unsolvability is global; congruence filters pass). A good target
  for the first "beyond-quadratic certified NO" milestone.
