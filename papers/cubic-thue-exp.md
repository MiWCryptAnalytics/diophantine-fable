# Pure cubic Thue equations are solvable in deterministic exponential time

**The diophantine-fable expedition** (draft — authorship placeholder)

Draft of 2026-07-22 (v2); all corrections from the independent
verification passes applied; the numeric evaluation of one absolute
constant is deferred and flagged (Remark 7.3).

---

## Abstract

We prove that pure cubic Thue equations $x^3 - d\,y^3 = m$ ($d \ge 2$
cube-free, not a cube; $m \ne 0$; input size $s = O(\log d + \log|m|)$ in
binary) are decided, with full solution lists, by a deterministic,
unconditional algorithm in time $2^{O(s)}$. No worst-case bound of this
shape appears in the literature: the best effective height bounds
(Bugeaud–Győry) are exponential in the coefficient *bit-size*, so
enumeration is doubly exponential, and the closest prior (Smart, ANTS-II
1996) is an explicitly practical per-method estimate, not a worst-case
bound. The method walks the rank-one unit orbit of norm-$m$
representatives from the Buchmann–Williams infrastructure and confines Thue-shape indices to a
two-sided window: an elementary $O(1)$ forward bound, and a backward
bound quasi-linear in the regulator $R$, via Sha's Matveev-based endgame
re-run with the true root-ratio gap $3R/2$, against which the $R$ in
Matveev's height parameter cancels. A prototype matches PARI's certified
`thue` on 1120/1120 grid instances; an independent reimplementation
matches 13/13, including three high-index fields. All constants are
explicit modulo one flagged final evaluation.

---

## 1. Introduction

### 1.1 Smale's fifth problem and the Thue gap

Smale's fifth problem (*Mathematical problems for the next century*
[Sma98]; see also Lagarias's quotation of the AMS reprint in [Lag79],
§1.4) asks for an algorithm deciding, given $f \in \mathbb{Z}[u,v]$,
whether $f(x,y) = 0$ has a solution in $\mathbb{Z}^2$, in time
$2^{s^c}$ for a universal constant $c$ — exponential time $2^{\mathrm{poly}(s)}$
in the input size $s$. The size measure is *dense*:
$s(f) = \sum_{|\alpha| \le \deg f} \max(\log|a_\alpha|, 1)$, so every
coefficient slot up to the total degree contributes at least $1$. Smale
notes that even decidability of the general problem is open.

Within this landscape, Thue equations $F(x,y) = m$ with $F$ an irreducible
binary form of degree $\ge 3$ occupy a deceptively classical-looking
stratum. Their finiteness is Thue's theorem; their effectivity is Baker's.
Yet the best general effective height bounds — Bugeaud–Győry [BG96] —
bound $\log\max(|x|,|y|)$ *polynomially in the coefficient magnitude* $H$,
that is, **exponentially in the coefficient bit-size** $\log H$.
Enumeration up to such a bound therefore costs doubly exponential time in
$s$, and the following gap results:

> Even Thue equations of **fixed degree 3** are not known to be decidable
> in time $2^{s^c}$ by the height-bound route.

This paper closes that gap for the pure cubic family. Throughout, $d \ge 2$
is cube-free and not a perfect cube, $m \ne 0$, and
$s = O(\log d + \log |m|)$ denotes the bit-size of the input $(d, m)$ in
binary.

### 1.2 Prior work: effectivity and practicality, but no worst-case bound

The algorithmic Thue literature is rich but states no worst-case complexity
theorem of the shape we prove.

- **Tzanakis–de Weger** [TdW89] set up the now-standard practical pipeline
  (Baker bound, LLL-based reduction, small-solutions search). Their paper
  states no complexity bound; the necessary algebraic data — fundamental
  units and the factorization of $m$ in the field — are *explicitly assumed
  known*.
- **Bilu–Hanrot** [BH96] extend the pipeline to high degree (replacing the
  $r$-dimensional LLL reduction by continued-fraction reduction of
  two-term forms). Again: no complexity bound; the phrase is "solve in
  reasonable time ... provided the necessary algebraic number theory data
  is available".
- **Smart** [Sma96] is the closest prior and the work we position against.
  It is a complexity analysis of the Tzanakis–de Weger method at fixed
  degree $n$, measured in $\log|m| + \log L(F)$ ($L(F)$ the sum of the
  coefficient moduli), and it is explicitly an analysis of practical
  difficulty — "I know of no analysis as to how difficult it is in
  practice to actually find all the solutions" [Sma96, p. 363]. The
  solution space is divided into small solutions (direct search), medium
  solutions (continued-fraction reduction), and large solutions
  (eliminated by linear forms in logarithms), and the announced outcome
  is "an overall exponential complexity bound in terms of $\log L(F)$"
  [Sma96, p. 364] — exponential in the input size — with the practical
  failure modes stated explicitly: large $m$, large regulator or class
  number, near-coincident roots of $F(x,1)$.[^smart] Smart's conclusion,
  quoted verbatim in Stroeker's review of the paper (Zbl 0896.11009):
  "So although solving Thue equations is now considered trivial we seem
  to be a long way off from a 'good' algorithm". It is a per-method
  practical estimate — not a rigorous worst-case decision theorem, and
  no bound of the shape of Theorem 1 appears there.
- **PARI/GP** [PARI] prints one genuine unconditional complexity
  statement for `thue`: when $F(x,1)$ has *no real root* the equation can
  be solved unconditionally in time $|m|^{1/\deg F}$. Every pure cubic
  has a real root, so even this rank-limited printed bound does not cover
  our family; and `thue`'s output is GRH-conditional unless certified.

A systematic literature verification across the books and surveys (Smart's 1998
book, Hanrot's LLL survey, Evertse–Győry, Waldschmidt, Gaál, Kim,
Gherga–Siksek) found effectivity or practicality statements only. The
theorem below therefore appears to be a citable gap in the literature,
positioned — as we have just done — against [Sma96].

### 1.3 The main theorem

> **Theorem 1 (Main Theorem).** There is a deterministic, unconditional
> algorithm that, given cube-free $d \ge 2$ (not a cube) and $m \ne 0$ in
> binary, with input size $s = O(\log d + \log|m|)$, decides whether
> $$x^3 - d\,y^3 = m$$
> has a solution in $\mathbb{Z}^2$ — and lists all solutions — in time
> $2^{O(s)}$.

The algorithm is fully specified and its correctness proof is complete;
every constant in the analysis is effective and explicitly computable. The
single item deferred — flagged wherever it occurs — is the *numeric
evaluation* of one absolute constant chain (Remark 7.3): the theorem holds
as stated, with the window bound of Lemma C semi-explicit, i.e. explicit
modulo final constant evaluation.

### 1.4 Proof strategy: seven steps

Let $K = \mathbb{Q}(\alpha)$, $\alpha = \sqrt[3]{d}$, a complex cubic field
with unit group $\langle -1, \varepsilon\rangle$ of rank one. A solution
$(x, y)$ is an element $\gamma = x - y\alpha$ of norm $m$; all norm-$m$
elements fall into finitely many orbits under the unit action; and "being
of Thue shape" is the vanishing of one coordinate — the
$\alpha^2$-coordinate — along the orbit, which is an integer linear
recurrence of order 3 in the orbit index $k$. The algorithm (Section 3):

1. compute the regulator, the Voronoi cycle, and the fundamental unit by
   the Buchmann–Williams rank-one infrastructure — deterministic,
   unconditional, no class group needed;
2. enumerate the ideals of norm $|m|$ in $O_K$ and extract a generator for
   each principal one, by the same cycle walk (Lemma A′);
3. unit-reduce each generator (Lemma U);
4. set up the order-3 integer recurrences (forward and reversed) for the
   cleared $\alpha^2$-coordinate;
5. bound the forward window elementarily: vanishing indices $k \le 3$
   (Proposition F);
6. bound the backward window by one application of Matveev's theorem with
   the true root-ratio gap $3R/2$: vanishing indices
   $-k \le N_C = \widetilde{O}(R + s)$ (Lemma C);
7. walk the windows with exact integer arithmetic, collect the zeros,
   recover $(x,y)$, and apply the mandatory final filter
   $x^3 - dy^3 = m$.

The technical heart is Step 6, and it turns on the guiding principle of
this program, stated here once and referred forward to Remark 4.6:
**always ask exponential in what** — every bound must be calibrated
against the *input* size $s$, never against an auxiliary quantity such
as the regulator, for the regulator itself is exponential in the input,
$R = 2^{\Theta(s)}$ (Section 2.3). A black-box application of Sha's
explicit Skolem-type theorems [Sha19] gives a window of size
$e^{22.5R}$ — which is $2^{O(s)}$ only under a *redefined* size measure
containing $R$ itself; calibrated against the input it is doubly
exponential (Remark 4.6 preserves this near-miss as a cautionary
lesson). The repair is not a new theorem of transcendence theory but a
re-run of Sha's own endgame with the instance's true data: the two maximal-modulus roots of
the reversed recurrence are the conjugate complex pair, the third root is
smaller by the exact factor $e^{3R/2}$, and in the resulting inequality
the $R$ inside Matveev's height parameter $A_3 = 4R$ **cancels** against
the gap $3R/2$ — leaving a window quasi-linear in $R$, hence $2^{O(s)}$
in honest input size.

### 1.5 Deciding without exhibiting: the Pell analogy

The philosophy is the one the Pell equation teaches one rung down. The
fundamental solution of $x^2 - Dy^2 = 1$ has $\Theta(\sqrt{D})$ digits —
exponential in the bit-size of $D$ — yet solvability questions about
generalized Pell equations are decided by walking orbits and comparing
positions, never by expanding the fundamental solution unless it is
actually needed. One rung up, the obstruction is steeper: by dense size
$s = 20$ the fundamental unit of $\mathbb{Q}(\sqrt[3]{d})$ already reaches
**1593 digits** per coefficient (Section 6.2, all records certified),
against roughly 145 digits for the Pell envelope at the same size. The
infrastructure machinery of Buchmann–Williams [BW88] keeps every *per-step*
object at polynomial size — minima are represented by poly-size ideal
data, "whereas the order of magnitude of a minimum can be as large as
$\exp\sqrt{D}$" [BW88, Prop. 2.11] — and full expansion is invoked only
where the $2^{O(s)}$ budget explicitly covers it. Stated precisely, the
philosophy is that the algorithm never *enumerates solutions* — objects
whose digit counts are exponential in $s$ — not that it never writes
down a large number. At the exponential-time target of this paper,
*expanding* the fundamental unit and the Binet data is a legitimate
simplification, adopted deliberately in Lemma A′: plain exact products
along the cycle suffice. Compact representations become essential only
for the stronger targets — poly-size certificates, NP membership —
discussed in Remark 7.5.

### 1.6 Organization

Section 2 fixes notation and collects the field-theoretic preliminaries,
including the two regulator floors the proof leans on. Section 3 states
the algorithm. Section 4 proves the four supporting results (Lemmas B, U,
A′, C and Proposition F), with all corrections from independent
verification applied.
Section 5 assembles the proof of Theorem 1. Section 6 reports the
computational companions. Section 7 collects remarks and open problems.

---

## 2. Preliminaries

### 2.1 The field, its embeddings, and its units

Fix cube-free $d \ge 2$, not a cube, and write $d = ab^2$ with $a, b$
coprime and squarefree. Let $\alpha = \sqrt[3]{d}$ (real) and
$K = \mathbb{Q}(\alpha)$, a cubic field of signature $(1,1)$: one real
embedding $\sigma_1$ and one conjugate pair $\sigma_2, \sigma_3 =
\bar\sigma_2$, with $\sigma_j(\alpha) = \omega^{j-1}\alpha$ for
$\omega = e^{2\pi i/3}$. The discriminant is $-27a^2b^2$ if
$d \not\equiv \pm 1 \pmod 9$ and $-3a^2b^2$ if $d \equiv \pm 1 \pmod 9$;
in particular, for every pure cubic field
$$|\mathrm{disc}(K)| \ge 108,$$
the minimum being attained at $d = 2$. We will use this floor twice.

The unit group is $O_K^\times = \langle -1, \varepsilon\rangle$ of rank
one. The torsion subgroup is $\{\pm 1\}$: any root of unity in $K$ is
fixed by the real embedding $\sigma_1$, hence equals $\pm 1$. Normalize
the fundamental unit by
$$\lambda := \sigma_1(\varepsilon) > 1, \qquad R := \log\lambda,$$
which is always possible (replace $\varepsilon$ by $\pm\varepsilon^{\pm1}$).
Write $\mu = \sigma_2(\varepsilon)$; then $|\mu| = |\bar\mu| =
\lambda^{-1/2}$, so the embedding moduli of $\varepsilon$ are
$(\lambda, \lambda^{-1/2}, \lambda^{-1/2})$ and $R$ is the regulator of
$K$.

> **Lemma 2.1 ($N(\varepsilon) = +1$ always).** With the normalization
> $\lambda > 1$, the fundamental unit of a complex cubic field has norm
> $+1$.

*Proof.* $N(\varepsilon) = \sigma_1(\varepsilon)\,|\sigma_2(\varepsilon)|^2
= \lambda|\mu|^2 > 0$, and a unit norm is $\pm 1$. $\blacksquare$

This one-liner is load-bearing: it makes the *reversed* orbit recurrence
integral (Step 4).

### 2.2 The index formula and the clearing constant $3b$

By Dedekind [Ded00] (see [AW04] for a standard modern account), for
$d = ab^2$ cube-free,
$$[\,O_K : \mathbb{Z}[\alpha]\,] \;=\; b \cdot \begin{cases} 3 & \text{if } d \equiv \pm 1 \pmod 9,\\ 1 & \text{otherwise.}\end{cases}$$
Consequently the index always divides $3b$, and for every $g \in O_K$,
writing $g = c_0(g) + c_1(g)\alpha + c_2(g)\alpha^2$ with
$c_i(g) \in \mathbb{Q}$, the cleared coordinates $3b\,c_i(g)$ are rational
integers. All integer recurrences below are stated for the $3b$-cleared
$\alpha^2$-coordinate. We emphasize — because a draft of this work got it
wrong, and empirical testing reveals that the naive "clear by 3" recipe
fails at 91 values of $d < 500$ (e.g. $d = 12, 45, 175$) — that clearing
by $3$ alone is **not** sufficient: the correct clearing constant is
$3b$.

### 2.3 Regulator bounds, above and below

**Above.** By Lenstra [Len92, Thm. 6.5], $hR \le |\Delta|^{1/2}\cdot
\mathrm{polylog}|\Delta|$ at fixed degree; since $|\Delta| \le 27d^2 =
2^{O(s)}$, we get
$$R \;\le\; hR \;=\; 2^{O(s)}.$$
This is the honest calibration to keep in view throughout: the regulator
is *exponential* in the input size, so any window or cost "polynomial in
$R$" is exponential in $s$, and anything "exponential in $R$" is doubly
exponential in $s$.

**Below, twice.** Astudillo–Díaz y Díaz–Friedman [ADF16, Thm. 7 and
Table 1] prove the sharp lower bound for complex cubic fields:
$$R \;\ge\; 0.2811995743\ldots,$$
attained uniquely at the field of discriminant $-23$ (defined by
$x^3 - x - 1$; the fundamental unit is the plastic number). Moreover, with
exactly three exceptions — the fields of discriminant $-23, -31, -44$,
with regulators $0.2811\ldots$, $0.3822\ldots$, $0.6093\ldots$ — every
complex cubic field satisfies $R > 0.79$. Since pure cubic fields have
$|\mathrm{disc}| \ge 108$, **none of the three exceptional fields is
pure**, so:
$$\text{every pure cubic field satisfies } R > 0.79.$$
This floor is **load-bearing**: Matveev's theorem imposes the side
condition $A_3 \ge |\log(\bar\mu/\mu)|$, and $|\log(\bar\mu/\mu)|$ can
approach $\pi$. Our choice $A_3 = 4R$ satisfies the side condition
precisely because $4R \ge 3.16 > \pi$ — a margin of $0.018$. At the
overall complex-cubic minimum $R = 0.2812$ the condition would *fail*
($4R = 1.12 < \pi$); the theorem survives on the pure-cubic discriminant
floor by less than two hundredths. (The forward window, by contrast, needs
only the unrestricted floor $R \ge 0.28119$.)

### 2.4 Heights

$h$ denotes the absolute logarithmic Weil height. We use throughout:

- $h$ is Galois-invariant: $h(\sigma_j(\gamma)) = h(\gamma)$.
- $|\log|\beta|| \le [\mathbb{Q}(\beta):\mathbb{Q}]\cdot h(\beta)$ for
  $\beta \ne 0$.
- $h(\varepsilon) = R/3$: the Mahler measure of the minimal polynomial of
  $\varepsilon$ is $\lambda$ (the complex place, of local degree 2,
  contributes nothing since $|\mu| < 1$), so
  $h(\varepsilon) = \tfrac13\log\lambda$. Note the complex place carries
  weight 2 in all such computations; in particular
  $h(\bar\mu/\mu) \le 2h(\varepsilon) = 2R/3$.
- $h(\omega) = 0$, $h(3d^{2/3}) = \log 3 + \tfrac23\log d$.

### 2.5 The coordinate extraction and the orbit recurrence

For $g \in K$ the discrete-Fourier identity of the power basis reads
$$\sigma_1(g) + \omega\,\sigma_2(g) + \omega^2\sigma_3(g) \;=\; 3d^{2/3}\,c_2(g),$$
so the $\alpha^2$-coordinate is a linear combination of the embeddings
with weights of modulus $1/(3d^{2/3})$. An element $\gamma \ne 0$ and the
orbit $g_k = \gamma\varepsilon^k$ give the Binet form
$$c_2(\gamma\varepsilon^k) \;=\; b_1\lambda^k + b_2\mu^k + \bar b_2\bar\mu^k,
\qquad b_1 = \frac{\sigma_1(\gamma)}{3d^{2/3}},\quad b_2 = \frac{\omega\,\sigma_2(\gamma)}{3d^{2/3}},$$
and **all Binet coefficients are nonzero** whenever $\gamma \ne 0$ (the
embeddings of a nonzero element are nonzero, and the DFT weights have
modulus $1/(3d^{2/3}) \ne 0$). This verifies, once and for all, the
implicit "all $b_j \ne 0$" hypothesis under which the Skolem-type
machinery of Section 4 operates.

Since $[K:\mathbb{Q}] = 3$ is prime and $\varepsilon \notin \mathbb{Q}$,
the characteristic polynomial of multiplication by $\varepsilon$ is its
(irreducible) minimal polynomial $X^3 - tX^2 + uX - 1$ (constant term
$N(\varepsilon) = 1$ by Lemma 2.1), with simple roots
$\lambda, \mu, \bar\mu$. Hence the cleared sequence
$$z_k \;:=\; 3b\,c_2(\gamma\varepsilon^k) \;\in\; \mathbb{Z}$$
satisfies the integer recurrence $z_{k+3} = t\,z_{k+2} - u\,z_{k+1} + z_k$
with *rational integer* coefficients — the parameter collapse that keeps
every constant tame (in Sha's notation [Sha19], the Galois-closure degree
of the coefficient field is $1$). The reversed sequence $v_n := z_{-n}$
satisfies the recurrence with characteristic polynomial
$X^3 - uX^2 + tX - 1$, the minimal polynomial of $\varepsilon^{-1}$ —
**integral because $N(\varepsilon) = 1$** — with roots $\lambda^{-1}$ (of
modulus $e^{-R}$) and the conjugate pair $\mu^{-1}, \bar\mu^{-1}$ (of
modulus $e^{R/2}$).

## 3. The algorithm

We display the algorithm, then discuss each step; the seven steps follow
the verified skeleton exactly. Lemmas A′, B, U, C and Proposition F are
stated and proved in Section 4.

### 3.1 Pseudocode

```
Input:  cube-free d >= 2 (not a cube), m != 0, in binary; s = O(log d + log|m|).
Output: the complete list of (x, y) in Z^2 with x^3 - d y^3 = m.

Step 1  (Field data and infrastructure; no class group.)
        Factor d by trial division (cost O(d^{1/2}) poly = 2^{O(s)});
        write d = a b^2 with a, b coprime squarefree; extract the
        clearing constant 3b.
        Run BW88 Algorithm 2.13 on O_K: compute the Voronoi cycle of
        reduced principal ideals, the neighbor minima x_1, ..., x_p, the
        exact incremental products gamma_k = x_1 ... x_k, the fundamental
        unit eps = gamma_p, and the regulator R.        [Lemma A']
        Expand eps in the integral basis (2^{O(s)} digits).

Step 2  (Norm-equation representatives.)
        Factor |m| by trial division. Enumerate all ideals I of O_K with
        N(I) = |m|  (at most d_3(|m|) of them; Dedekind basis, splitting
        at p | 3b read off from O_K/pO_K). For each I: test principality
        by reducing I and searching the cycle stock; if principal,
        extract the generator gamma_I = mu_I * gamma_{k-1}^{-1} and
        verify (gamma_I) = I by one exact HNF check.    [Lemma A']

Step 3  (Unit reduction.)
        Replace each generator gamma_I by gamma' = gamma_I * eps^j with
        | log|sigma_1(gamma')| - (1/3)log|m| | <= R/2.  [Lemma U]

Step 4  (Recurrence data.)
        For each gamma', form z_k = 3b * c_2(gamma' eps^k): an integer
        sequence satisfying the order-3 recurrence with characteristic
        polynomial minpoly(eps); the reversed sequence v_n = z_{-n}
        satisfies the integral reversed recurrence (N(eps) = 1).
        Expand eps and z_0, z_1, z_2 to their 2^{O(s)} digits.

Step 5  (Forward window.)   k_+ := 3.                   [Proposition F]

Step 6  (Backward window.)  N_C := c (R + log|m| + log d + 1) *
                                   log(R + log|m| + log d + 2). [Lemma C]

Step 7  (The walk and the filter.)
        For each representative gamma' and each sign sigma in {+1, -1}:
        iterate the exact integer recurrences over k in [-N_C, k_+];
        whenever z_k = 0, write sigma * gamma' eps^k = x - y alpha and
        KEEP (x, y) if and only if x^3 - d y^3 = m exactly
        (mandatory norm-sign filter).
        Output the collected set of solutions.
```

### 3.2 Step 1 — regulator and unit, no class group

The step opens by factoring $d$ by trial division — cost
$O(d^{1/2})\,\mathrm{poly}(s) = 2^{O(s)}$ — which yields the
decomposition $d = ab^2$ and with it the clearing constant $3b$
consumed by Steps 2 and 4 (Section 2.2). At unit rank one the class
group is never needed: principality of ideals
is decided directly on the cycle of reduced principal ideals, so no
certification burden attaches to $\mathrm{Cl}_K$ at all. We compute $R$
and the cycle by Buchmann–Williams Algorithm 2.13 [BW88, Prop. 2.14]:
deterministic $O(R\,D^{\epsilon})$ bit-operations ($D = |\Delta|$),
unconditional, published with proof. By Section 2.3, $R = 2^{O(s)}$, so
this is $2^{O(s)}$. The fundamental unit in *expanded* form costs
$2^{O(s)}$ digits — affordable at this budget, and needed in Step 4
anyway. (Lenstra [Len92, Thm. 5.5] — whose deterministic exponent is
$|\Delta|^{3/4}$, not $1/2$, and which Lenstra himself hedges with
"appears to be true" — is a fallback citation only; the BW88 route is the
one we rely on.)

### 3.3 Step 2 — norm-equation representatives

Trial-divide $|m|$ (cost $2^{s/2}\mathrm{poly}(s)$). The ideals of $O_K$
of norm $|m|$ number at most $d_3(|m|) = 2^{O(s)}$ (three-fold divisor
function; the counting argument is the proof line of [Len92, Thm. 6.5]).
They are enumerated prime-by-prime: for $p \nmid 3b$, factor
$x^3 - d \bmod p$; for $p \mid 3b$ (the primes dividing the index), read
the splitting off the finite algebra $O_K/pO_K$ in the Dedekind basis;
assemble prime-power blocks by exponent vectors weighted by residue
degrees, and multiply into Hermite normal form, $\mathrm{poly}(s)$ per
ideal. Per candidate ideal, principality and a generator are obtained by
the baby-step cycle walk — decision cost $O(R\,D^\epsilon)$ per candidate
[BW88, Prop. 4.5] — with the tracked generator supplied by Lemma A′. (The
$R^{1/2}$-rate giant-step variant [BW88, Thm. 4.7] is decision-only and is
not used.)

### 3.4 Step 3 — unit reduction

Each generator is reduced along the one-dimensional log-unit lattice
(Lemma U, sharpened form): the reduced representative $\gamma'$
satisfies
$$\bigl|\log|\sigma_1(\gamma')| - \tfrac13\log|m|\bigr| \le \tfrac{R}{2},
\qquad\text{hence}\qquad
\bigl|\log|\sigma_2(\gamma')| - \tfrac13\log|m|\bigr| \le \tfrac{R}{4}
\ \ \text{and}\ \
\Bigl|\frac{\sigma_2(\gamma')}{\sigma_1(\gamma')}\Bigr| \le e^{3R/4}.$$
The windows of Steps 5–6 apply to the **unit-reduced** representatives —
this hypothesis is part of their statements.

### 3.5 Step 4 — orbit and recurrence

As in Section 2.5: $z_k$ is the $\alpha^2$-coordinate of
$\gamma'(\pm\varepsilon)^k$, cleared by $3b$ (**not** by 3; Section 2.2).
The recurrence has order 3, characteristic polynomial equal to the
minimal polynomial of $\varepsilon$, simple roots, and all Binet
coefficients nonzero since $\gamma' \ne 0$ (DFT weights of modulus
$1/(3d^{2/3})$); the coefficients are rational integers, so Sha's Galois
parameter collapses to $1$. $N(\varepsilon) = \lambda|\mu|^2 > 0$ forces
$N(\varepsilon) = +1$ (Lemma 2.1), which makes the reversed recurrence
integral. Expanding $\varepsilon$ and $z_0, z_1, z_2$ to their $2^{O(s)}$
digits is part of this step's stated cost.

### 3.6 Steps 5 and 6 — the two windows

The forward window is elementary and absolute: vanishing at $k > 0$
forces $\lambda^{3k/2} \le 2e^{3R/4}$, giving $k_+ \le 3$ (Proposition F —
which is exactly the empirical maximum, Section 6.1). The backward window
is Lemma C: $v_n \ne 0$ for all
$n > N_C = c\,(R + \log|m| + \log d + 1)\log(R + \log|m| + \log d + 2)$,
an absolute explicitly computable $c$ — quasi-linear in $R$, hence
$N_C = \widetilde O(R + s) = 2^{O(s)}$.

### 3.7 Step 7 — the walk

For every representative $\times$ sign $\times$ index $k \in [-N_C, k_+]$:
one exact integer recurrence iteration ($2^{O(s)}$ digits each, $2^{O(s)}$
total), collect the hits $z_k = 0$, recover $(x, y)$ from the
$1$- and $\alpha$-coordinates, and apply the **mandatory final filter**
$x^3 - dy^3 = m$: the walk also emits norm-$(-m)$ elements, and only the
filter separates the two signs. (Since $c_2$ is linear, the $\pm$
sequences share their zero set; the sign branch matters at recovery, where
$\gamma \mapsto -\gamma$ swaps the norms $\pm m$.)

Completeness is ideal-theoretic and library-free: any solution
$\gamma = x - y\alpha \in \mathbb{Z}[\alpha] \subseteq O_K$ generates an
ideal of norm $|m|$ appearing in Step 2's list; the unit orbits under
$\langle -1, \varepsilon\rangle$ — the full unit group, torsion $\{\pm1\}$
by the real embedding — cover all generators of each principal ideal; and
$\gamma \mapsto -\gamma$ swaps $\pm m$, which the $\pm$-walk covers. The
formal proof is Section 5.

## 4. The supporting lemmas

Throughout this section $\gamma$ denotes a nonzero element of $O_K$ with
$N(\gamma) = \pm m$, and $b_1, b_2, \bar b_2$ the ($3b$-cleared) Binet
coefficients of its orbit sequence (Section 2.5), all nonzero.

### 4.1 Lemma B: root-of-unity exclusion

> **Lemma B.** The quotient $\bar\mu/\mu$ of the complex embeddings of
> $\varepsilon$ is not a root of unity.

*Proof.* Suppose $(\bar\mu/\mu)^t = 1$ for some $t \ge 1$. Then
$\sigma_2(\varepsilon^t) = \sigma_3(\varepsilon^t) =
\overline{\sigma_2(\varepsilon^t)}$, so $\sigma_2(\varepsilon^t)$ is real.
(The contradiction target is "$\sigma_2(\varepsilon^t)$ real" — not
"$\varepsilon^t$ real": $\sigma_1(\varepsilon^t)$ is always real, so that
statement would be empty.) Since $[K:\mathbb{Q}] = 3$ is prime, either
$\varepsilon^t \in \mathbb{Q}$, in which case $\varepsilon^t$ is a
rational unit, $\varepsilon^t = \pm 1$, contradicting
$|\sigma_1(\varepsilon^t)| = e^{tR} > 1$; or
$\mathbb{Q}(\varepsilon^t) = K$, in which case the three conjugates of
$\varepsilon^t$ are pairwise distinct, contradicting
$\sigma_2(\varepsilon^t) = \sigma_3(\varepsilon^t)$. $\blacksquare$

The same argument applied to $|\lambda/\mu| = e^{3R/2} \ne 1$ shows the
full sequence is non-degenerate (no ratio of distinct roots is a root of
unity), so its zero set is finite; but the proof below needs only the
$\bar\mu/\mu$ case.

### 4.2 Lemma U: unit reduction at rank one

> **Lemma U (rank-1 reduction).** Let $K$ be a complex cubic field,
> $\varepsilon$ normalized with $\lambda = \sigma_1(\varepsilon) > 1$,
> $R = \log\lambda$. For every $\gamma \in O_K$ with
> $N(\gamma) = m' \ne 0$ there is $j \in \mathbb{Z}$ such that
> $\gamma' = \gamma\varepsilon^j$ satisfies
> $$\bigl|\log|\sigma_1(\gamma')| - \tfrac13\log|m'|\bigr| \;\le\; \tfrac{R}{2}.$$
> Consequently
> $\bigl|\log|\sigma_2(\gamma')| - \tfrac13\log|m'|\bigr| \le R/4$,
> $\ |\sigma_2(\gamma')/\sigma_1(\gamma')| \le e^{3R/4}$, and
> $h(\gamma') \le \tfrac13\log|m'| + R + O(1)$.

*Proof.* $|\sigma_1(\gamma)|\,|\sigma_2(\gamma)|^2 = |m'|$, and for
$t(\gamma) := \log|\sigma_1(\gamma)| - \tfrac13\log|m'|$ we have
$t(\gamma\varepsilon^j) = t(\gamma) + jR$; take
$j = -\mathrm{round}(t(\gamma)/R)$. The consequences follow from
$|\sigma_2|^2 = |m'|/|\sigma_1|$ and from bounding the house of
$\gamma'$. $\blacksquare$

This is a one-dimensional reduction in the log-unit lattice — genuinely
trivial as mathematics. Two computational remarks are part of the record:
computing $j$ rigorously requires $\sigma_1(\gamma)$ to polynomially many
digits via interval arithmetic, cost $2^{O(s)}$ on $2^{O(s)}$-digit
inputs; and a borderline rounding at half-integers only widens the
forward window by 1 — a slack already accounted for in Proposition F.

### 4.3 Lemma A′: tracked generators along the Voronoi cycle

> **Lemma A′ (generators along the cycle).** Fix the degree and unit rank
> one, and let $p$ be the cycle length, so $p < 2R/\log\tau + 1$ with
> $\tau$ the golden ratio (Williams: $\varepsilon_0 > \tau^{p/2}$). The
> neighbor minima $x_1, \ldots, x_p$ of the reduced-ideal cycle each carry
> $\mathrm{poly}(s)$-size data [BW88, Prop. 2.11], and the incremental
> exact products $\gamma_k = x_1\cdots x_k$ ($2^{O(s)}$ digits each)
> satisfy: the $(k{+}1)$-st reduced principal ideal is
> $I_{k+1} = (\gamma_k)^{-1}$, and $\varepsilon = \gamma_p$. Hence every
> principality witness and $\varepsilon$ itself are computable, expanded,
> in deterministic total time $2^{O(s)}$, with exact HNF verification of
> each ideal identity.

*Proof (with the corrected orientation and certification).* The
Voronoi chain at rank one is $I_1 = O_K$ and
$I_{k+1} = (1/x_k)\,I_k$, where $x_k$ is the neighbor minimum of $I_k$,
**computed exactly by BW88 Algorithm 2.13 / Williams [Wil85]**. Exactness
of the neighbor step is what certifies completeness of the stock: floats
used for steering alone could skip a minimum and still pass every HNF
test, so the per-step computation must be the exact one. Telescoping,
$\gamma_k = x_1\cdots x_k$ is the $(k{+}1)$-st minimum and
$I_{k+1} = (\gamma_k)^{-1}$; after a full cycle, $\gamma_p = \varepsilon$
exactly, under the $\sigma_1 > 0$, increasing-$\lambda$ normalization.
$\mathrm{poly}(s)$-size of each $x_k$ follows from [BW88, Prop. 2.4]
($|N(x)| \le \sqrt{D}\,N(\mathfrak{a})$), [BW88, Prop. 2.7(i)] (log-step
$< \log\sqrt{D}$), and denominators $\le \sqrt{D}$. Digit growth of the
exact products is additive, $O(p\cdot\mathrm{poly}(s)) = 2^{O(s)}$ per
$\gamma_k$ and $2^{O(s)}$ in total, including the per-step exact HNF
chain identity $I_{k+1}\cdot(x_k) = I_k$.

**Candidate-side recipe** (Step 2's need): given an ideal $I$ of norm
$|m|$, reduce exactly to obtain the relative minimum $\mu_I$
($\mathrm{poly}(s)$-size); $I$ is principal if and only if the reduction
lands on the cycle stock at some position $k$, and then its generator is
$$g \;=\; \mu_I\cdot\gamma_{k-1}^{-1}$$
(exact division on $2^{O(s)}$-digit integers), certified by one terminal
exact HNF check $(g) = I$. $\blacksquare$

Three remarks on the constants and the design, verified against the
primary sources.

1. **Cycle length.** [BW88, Cor. 2.8] gives
   $R/\log\sqrt{D} < p \le jR/c_1$ with $(j, c_1) = (7, \log 4)$ at
   degree 3 — constants confirmed against the Math. Comp. text and
   against Williams [Wil86], whose scope is *all* complex cubic fields
   and arbitrary reduced lattices (the paper also has the sharper
   $\theta_8 > 4$, and $\varepsilon_0 > \tau^{p/2}$, whence
   $p < 2R/\log\tau + 1 \approx 4.16R$ as used in the statement). A venue
   correction carried in our records: Williams' *Continued fractions and
   number-theoretic computations* is Rocky Mountain J. Math. 15 (1985)
   [Wil85], not Pacific J. Math.; the Pacific J. Math. paper is [Wil86].
2. **Why plain products.** An earlier plan routed height bounds through
   composition-then-reduce distance-slip estimates. The simplification
   adopted here: at the $2^{O(s)}$ budget one simply
   takes the plain incremental exact products of the at most
   $7R/\log 4$ neighbor minima along the cycle. Compact representations
   (Thiel) are a luxury needed only for $\mathrm{poly}$-size
   *certificates*, not for the EXP algorithm.
3. **What Lemma A′ delivers to Step 1.** The full cycle walk computes
   $\varepsilon = \gamma_p$ and $R$ along the way; Steps 1 and 2 share
   one infrastructure computation.

### 4.4 Proposition F: the forward window is $O(1)$

> **Proposition F (forward window).** Let $\gamma'$ be a unit-reduced
> representative (Lemma U) and $z_k$ the $3b$-cleared
> $\alpha^2$-coordinate sequence of $\pm\gamma'\varepsilon^k$. If
> $z_k = 0$ with $k > 0$, then
> $$\lambda^{3k/2} \;\le\; 2\,\Bigl|\frac{\sigma_2(\gamma')}{\sigma_1(\gamma')}\Bigr| \;\le\; 2e^{3R/4},
> \qquad\text{so}\qquad
> k \;\le\; \frac12 + \frac{2\log 2}{3R} \;\le\; 2$$
> using the sharp complex-cubic floor $R \ge 0.2811995743$ [ADF16].
> Allowing the one-step rounding slack of Lemma U:
> $$k_+ \;\le\; 3,$$
> which is exactly the maximum observed empirically (Section 6.1).

*Proof.* By the DFT form (Section 2.5), $z_k = 0$ means
$b_1\lambda^k = -(b_2\mu^k + \bar b_2\bar\mu^k)$, whence
$|\sigma_1(\gamma')|\lambda^k \le 2|\sigma_2(\gamma')|\lambda^{-k/2}$
(the weights share the modulus $1/(3d^{2/3})$, which cancels; the $3b$
clearing also cancels). Rearranged: $\lambda^{3k/2} \le
2|\sigma_2(\gamma')/\sigma_1(\gamma')| \le 2e^{3R/4}$ by Lemma U. Taking
logarithms, $k \le \tfrac12 + \tfrac{2\log 2}{3R}$, and with
$R \ge 0.28119$ the right side is $\le 2.15$, so $k \le 2$; the possible
half-integer rounding in Lemma U widens the admissible window by at most
one index. $\blacksquare$

Note the phenomenon the empirical data confirm:
after unit reduction the $R$'s cancel — the forward window is not merely
$\mathrm{poly}(s)$, it is *bounded by an absolute constant*.

### 4.5 Lemma C: the backward window, quasi-linear in $R$

> **Lemma C (backward window).** Let $\gamma$ be a unit-reduced
> representative with $N(\gamma) = \pm m$, and let $v_n$ be the
> $3b$-cleared $\alpha^2$-coordinate sequence of $\gamma\varepsilon^{-n}$
> ($n \ge 0$). There is an absolute, explicitly computable constant $c$
> such that $v_n \ne 0$ for all
> $$n \;>\; N_C \;:=\; c\,\bigl(R + \log|m| + \log d + 1\bigr)\,\log\bigl(R + \log|m| + \log d + 2\bigr).$$

*Proof.* Write
$v_n = b_1\lambda^{-n} + b_2\mu^{-n} + \bar b_2\bar\mu^{-n}$ with all
$b_j \ne 0$ ($\gamma \ne 0$; Section 2.5), and set
$\mu^{-1} = e^{R/2}e^{i\theta}$, $b_2 = |b_2|e^{i\varphi}$. The two
maximal-modulus roots of the reversed recurrence are the conjugate pair
$\mu^{-1}, \bar\mu^{-1}$ (modulus $e^{R/2}$), the third root
$\lambda^{-1}$ is smaller by the exact factor $e^{3R/2}$, and the
quotient $\bar\mu/\mu$ of the maximal pair is not a root of unity
(Lemma B).

If $v_n = 0$, then
$2|b_2|e^{nR/2}|\cos(\varphi + n\theta)| = |b_1|e^{-nR}$, so with
$|\cos x| \ge \tfrac{2}{\pi}\,\mathrm{dist}(x, \tfrac{\pi}{2} + \pi\mathbb{Z})$:
$$\mathrm{dist}\Bigl(\varphi + n\theta,\ \tfrac{\pi}{2} + \pi\mathbb{Z}\Bigr)
\;\le\; \frac{\pi}{4}\,\frac{|b_1|}{|b_2|}\,e^{-3nR/2}.
\tag{$\dagger$}$$

The distance on the left is measured exactly by the linear form in
logarithms (with the corrected conjugation and exact
factor 2, both verified numerically on two fields):
$$\Lambda_n \;=\; a\,\log(-1) \;+\; \log\!\frac{b_2}{\bar b_2} \;+\; n\,\log\!\frac{\bar\mu}{\mu},
\qquad a \in \mathbb{Z} \text{ odd},\ |a| \le n + 2,$$
with
$$|\Lambda_n| \;=\; 2\,\mathrm{dist}\Bigl(\varphi + n\theta,\ \tfrac{\pi}{2} + \pi\mathbb{Z}\Bigr)
\quad\text{exactly.}$$

**The degenerate case is void.** $\Lambda_n = 0$ if and only if
$\cos(\varphi + n\theta) = 0$, i.e. the conjugate-pair term of $v_n$
vanishes — but then $v_n = b_1\lambda^{-n} \ne 0$. So at any actual zero
$v_n = 0$ we always have $\Lambda_n \ne 0$, and Matveev's theorem
applies.

Apply Matveev [Mat00] (as restated in [Sha19, §2.4]) with $k = 3$
logarithms in the field $L = \mathbb{Q}(\sqrt[3]{d}, \omega)$ of degree
$$D_0 = 6.$$
$L$ **is** the Galois closure of $K$: $\sqrt{\mathrm{disc}(K)}$ generates
$\mathbb{Q}(\sqrt{-3}) = \mathbb{Q}(\omega)$ for *every* pure cubic field
(the discriminant is $-3$ times a square in both Dedekind types), and $L$
is stable under complex conjugation and contains $-1$, $b_2/\bar b_2$,
and $\bar\mu/\mu$. The conclusion is
$$\log|\Lambda_n| \;>\; -\,C_0\,A_1A_2A_3\,\log\bigl(e(n+2)\bigr),
\qquad C_0 = 2^{40}\,D_0^2\,\log(eD_0),$$
where the $2^{40}$-versus-$2^{38}$ slack absorbs the factor 2 in
$|\Lambda_n| = 2\,\mathrm{dist}$, and:

- $A_1 = \pi$;
- $A_2 \le D_0\,h(b_2/\bar b_2) + \pi \le 12H_1 + \pi$, where (heights
  are Galois-invariant, and the $3b$-clearing adds at most $\log 3d$):
  $$h(b_2) \;\le\; h(\gamma) + \log 3 + \tfrac23\log d + \log 3d \;=:\; H_1
  \;=\; O\bigl(h(\gamma) + \log d + 1\bigr);$$
- $A_3 = \max\bigl(D_0\,h(\bar\mu/\mu),\ |\log(\bar\mu/\mu)|\bigr) \le
  \max(4R, \pi) = 4R$, using $h(\bar\mu/\mu) \le 2h(\varepsilon) = 2R/3$
  ($h(\varepsilon) = R/3$; the complex place carries weight 2). Matveev's
  side condition $A_3 \ge |\log(\bar\mu/\mu)|$ — a quantity which can
  approach $\pi$ — is met because pure cubic fields have
  $|\mathrm{disc}| \ge 108$, hence $R > 0.79$ (the exceptional fields of
  [ADF16] at discriminants $-23, -31, -44$ are not pure), so
  $4R \ge 3.16 > \pi$ — **margin $0.018$**.

Combining Matveev's lower bound with $(\dagger)$ and
$|\log(|b_1|/|b_2|)| \le 12H_1$ (via $|\log|b|| \le \deg(b)\cdot h(b)$
and $\deg \le 6$):[^slack]
$$\frac{3R}{2}\,n \;\le\; 12H_1 + \log\frac{\pi}{4}
\;+\; C_0\,\pi\,(24H_1 + \pi)\,(8R)\,\log\bigl(e(n+2)\bigr).$$
Divide by $3R/2$: **the $R$ cancels in the Matveev term**, leaving
$$n \;\le\; \frac{8H_1}{R} \;+\; c_2\,(H_1 + 1)\,\log\bigl(e(n+2)\bigr),
\qquad c_2 \text{ absolute and explicit.}$$
Resolving $n$ against $\log n$ (via $x \ge 2A\log A \Rightarrow
x/\log x \ge A$; the term $8H_1/R$ is $O(H_1)$ by the regulator floor)
and inserting the unit-reduction bound
$H_1 = O(\log|m| + R + \log d)$ (Lemma U) gives $N_C$ as stated. In
particular
$$N_C \;=\; \widetilde O(R + s) \;=\; 2^{O(s)}$$
— quasi-linear in $R$, in place of the fatal $e^{22.5R}$ of the
black-box route (Remark 4.6). $\blacksquare$

*Final write-up bookkeeping, carried forward visibly from the verified
notes:* the absolute constant $c$ is traced through the chain
$2^{40}\cdot 36\cdot\log(6e)\cdot\pi\cdot(12H_1+\pi)\cdot 4R$ (before the
$R$-cancellation), with $D_0 = 6$ throughout, and the branch conventions
for $\log(-1)$ absorbed into $|a| \le n + 2$ — all mechanical; the
numeric evaluation is carried out in Remark 7.3.

### 4.6 Remark: why the black-box window does not suffice (a preserved lesson)

An earlier draft of this work cited Sha's Theorem 1.2 [Sha19] as a black
box, with "window $2^{O(s)}$". The claim was wrong in the way that
matters most in this subject: the $s$ in that statement was the
extraction's *redefined* size $\max(R, h(\gamma), \log|m|, \log d)
\supseteq R$, and $R = 2^{\Theta(s_{\mathrm{input}})}$. In honest input
size, the black-box window $e^{22.5R}$ is **doubly exponential** — a
measured instance: $d = 9986$ has $R \approx 2605$ and a black-box window
exceeding $10^{25{,}454}$ steps. The exponential loss is entirely an
artifact of the worst-case Mahler-type root-separation quantity in Sha's
theorems, which is $e^{-\Theta(R)}$ for our instances even though the
*true* ratio gap is $3R/2$ — exponentially larger. Substituting the true
gap into Sha's own endgame (a change of the proofs, not of the theorems —
which is why Lemma C is stated as ours, with Sha's Lemma 2.8 and the
Matveev application as extracted ingredients) is what produces the
quasi-linear window. This was the third instance of the same trap in this
program's history, and it has earned a name we record for the reader:
**always ask exponential in what.**

## 5. Proof of the Main Theorem

**Theorem 1.** *There is a deterministic, unconditional algorithm that,
given cube-free $d \ge 2$ (not a cube) and $m \ne 0$ in binary, with
$s = O(\log d + \log|m|)$, decides whether $x^3 - dy^3 = m$ has a
solution in $\mathbb{Z}^2$ — listing all solutions — in time $2^{O(s)}$.*

*Proof.* We show the algorithm of Section 3 is sound, complete, and runs
in time $2^{O(s)}$.

**Soundness.** Every pair the algorithm outputs has passed the exact
integer filter $x^3 - dy^3 = m$ in Step 7, so no false positives occur —
in particular the norm-$(-m)$ elements that the walk necessarily emits
are discarded there.

**Completeness (ideal-theoretic).** Let $(x, y) \in \mathbb{Z}^2$ satisfy
$x^3 - dy^3 = m$, and set $\gamma = x - y\alpha \in \mathbb{Z}[\alpha]
\subseteq O_K$, so $N(\gamma) = m$. The ideal $(\gamma)$ has norm $|m|$
and therefore appears in Step 2's enumeration; it is principal, so
Step 2 (Lemma A′) finds a generator $\gamma_I$ with
$(\gamma_I) = (\gamma)$, and Step 3 replaces it by the unit-reduced
$\gamma'$ in the same orbit. Two generators of the same ideal differ by a
unit, and the unit group is $\langle -1, \varepsilon\rangle$ — the full
unit group, since the torsion is $\{\pm 1\}$ by the real embedding — so
$$\gamma \;=\; \pm\,\gamma'\,\varepsilon^{k} \quad\text{for some } k \in \mathbb{Z}.$$
The $\alpha^2$-coordinate of $\gamma$ vanishes (Thue shape), so the
cleared sequence of $\gamma'$ has $z_k = 0$. Since $\gamma'$ is
unit-reduced, Proposition F bounds the positive side, $k \le k_+ = 3$,
and Lemma C bounds the negative side, $-k \le N_C$; both windows apply
precisely because they are stated for unit-reduced representatives. Hence
$k \in [-N_C, k_+]$, the walk of Step 7 visits index $k$, detects
$z_k = 0$, and recovers from $\pm\gamma'\varepsilon^k$ both candidate
pairs $\pm(x, y)$; the filter retains exactly the one(s) of norm $m$ —
among them $(x, y)$. Both norm signs are covered: if
$N(\gamma') = -m$, the solution appears through the sign branch
$\gamma = -\gamma'\varepsilon^k$, since $\gamma \mapsto -\gamma$ swaps
$\pm m$ at odd degree. No step of this argument appeals to any external
solver; completeness is purely ideal-theoretic.

**Cost accounting.** Write $D = |\Delta| \le 27d^2 = 2^{O(s)}$ and recall
$R \le hR = 2^{O(s)}$ (Section 2.3).

- *Step 1:* trial-division factorization of $d$,
  $O(d^{1/2})\,\mathrm{poly}(s) = 2^{O(s)}$; then
  $O(R\,D^\epsilon) = 2^{O(s)}$ bit-operations [BW88,
  Alg. 2.13, Prop. 2.14]; expanding $\varepsilon$ costs $2^{O(s)}$
  digits (Lemma A′).
- *Step 2:* trial division $2^{s/2}\mathrm{poly}(s)$; at most
  $d_3(|m|) = 2^{O(s)}$ candidate ideals, each assembled in
  $\mathrm{poly}(s)$; per candidate one cycle search,
  $O(R\,D^\epsilon) = 2^{O(s)}$ [BW88, Prop. 4.5], with generator
  extraction and one exact HNF verification (Lemma A′).
- *Step 3:* interval arithmetic to polynomially many digits on
  $2^{O(s)}$-digit inputs: $2^{O(s)}$ (Lemma U).
- *Step 4:* expanding $z_0, z_1, z_2$ and the recurrence coefficients:
  $2^{O(s)}$ digits, stated cost of the step.
- *Steps 5–6:* window sizes $k_+ \le 3$ and
  $N_C = \widetilde O(R + s) = 2^{O(s)}$.
- *Step 7:* at most $(N_C + k_+ + 1)$ iterations per representative and
  sign; each iteration is exact integer arithmetic on $2^{O(s)}$-digit
  numbers; total $2^{O(s)}\cdot 2^{O(s)} = 2^{O(s)}$.

The product of a $2^{O(s)}$ number of representatives with $2^{O(s)}$
work each is $2^{O(s)}$, completing the proof. $\blacksquare$

We record the honest caveat once more: to *run* Step 6 one needs a
numeric value for $c$; the constant chain of Lemma C supplies one
mechanically, and its final evaluation is deferred (Remark 7.3). The
theorem is unconditional and its proof complete; the window constant is
semi-explicit — explicit modulo final constant evaluation.

## 6. Computational companion

Two experiments and one independent reimplementation accompany the
proof. Neither is part of the logical argument; both
shaped it.

### 6.1 The orbit-walk prototype: 1120/1120

`experiments/cubic_orbit_prototype.py` implements the orbit walk with
PARI/GP [PARI] supplying the algebraic data: representatives from
`bnfisintnorm` over `bnfinit(x^3 - d, 1)`, the $\pm\varepsilon^{\pm k}$
walk over $k \in [-60, 60]$, Thue-shape detection on the
$\alpha^2$-coordinate, and the exact final filter $x^3 - dy^3 = m$. The
validation grid is
$$d \in \{2, 3, 5, 6, 7, 10, 11, 12, 13, 15, 17, 19, 20, 22\},
\qquad m \in [-40, 40] \setminus \{0\}$$
— 14 fields $\times$ 80 right-hand sides $=$ **1120 cases** — and the
reference is PARI's `thue` over `thueinit(x^3 - d, 1)`, whose flag-1
certification is unconditional. Result: **1120/1120 exact solution-set
agreement**, and across all hits the maximum vanishing index was
$$\max |k| = 3$$
— exactly the bound $k_+ \le 3$ that Proposition F later proved
(the prototype's fixed cutoff $K_0 = 60$ was the honest gap between
prototype and theorem; the two windows of Section 4 close it). We
stress the boundary between the proven algorithm and this practical
code: the cutoff $K_0 = 60$ operates under the strong empirical window
conjecture of Remark 7.4, not under the proven bound of Lemma C; the
proven window $N_C$ — of order $10^{17}\cdot H_1\log H_1$ steps once
the constants of Remark 7.3 are inserted — is $2^{O(s)}$ in theory but
is not what the prototype executes. For completeness: `bnfisintnorm`
returns a complete system modulo units of
*positive* norm, and the $\langle -1, \varepsilon \rangle$ walk covers a
superset of those orbits.

### 6.2 Unit growth: the wall being dodged

`experiments/thue_unit_growth.py` charts why any method that must expand
unit data pays exponentially: for the family $x^3 - dy^3 = 1$ it records
$d$ whenever the digit-size of the fundamental unit's coefficients sets a
record (regulators from `bnfinit`, GRH-conditional; every record row
re-certified unconditionally with `bnfcertify`). By dense size $s = 20$
(at $d = 1721$, $R \approx 3669.4$) the coefficients reach **1593
digits**, all records certified — a steeper envelope than the Pell layer
(roughly 145 digits at the same size), one rung down. The data are in
`experiments/data/cubic_unit_records.csv`. This is precisely the
obstruction the infrastructure route dodges: the algorithm expands
$\varepsilon$ only inside its stated $2^{O(s)}$ budget, and every
per-step object it manipulates is polynomially sized (Lemma A′).

### 6.3 An independent reimplementation: 13/13

An independent **from-scratch mini-implementation** of the algorithm,
written separately from the prototype, was validated against certified
`thue`: **13/13 exact agreements**, including the high-index fields
$$d = 12,\ 45,\ 175 \qquad ([\,O_K : \mathbb{Z}[\alpha]\,] = 2,\ 3,\ 5),$$
precisely the fields at which the naive "clear by 3" recipe fails
(Section 2.2) — so the validation deliberately covers the corrected
code path. The same reimplementation verified the linear-form analysis
of Lemma C numerically on two fields and validated the Binet integer
sequence against a Thue-shape zero.

---

## 7. Remarks and open problems

### 7.1 General complex cubic forms (rank 1)

The natural next target is the general irreducible cubic Thue equation of
negative discriminant, $F(x, y) = m$: the associated cubic field is again
complex, the unit rank is again 1, and the entire skeleton — cycle walk,
unit reduction, two-sided window, exact walk — carries over. What grows
is bookkeeping: the ring $\mathbb{Z}[\alpha]$ attached to a general form
is no longer generated by a pure cube root, the index and clearing
analysis of Section 2.2 must be redone for the form's ring, and the
height accounting in $H_1$ acquires the form's coefficients. We see no
conceptual obstruction, and state it as the immediate open problem:
extend Theorem 1 to all complex cubic forms.

### 7.2 Totally real cubics (rank 2) are the honest hard case

For totally real cubic forms the unit rank is 2 and the picture changes
qualitatively: the vanishing locus lives on a $\mathbb{Z}^2$-lattice of
units, the walk has no canonical successor, and no dominant root
separates a forward window — the problem takes on the flavor of S-unit
equations rather than of a one-dimensional Skolem instance. We know of no
route to a $2^{O(s)}$ bound there and explicitly defer it; nothing in
this paper's method addresses it.

### 7.3 The constant chain (evaluated)

The constants of Lemma C are now fully explicit; we record the
evaluation. With $D_0 = 6$ (exact: $\mathbb{Q}(\sqrt[3]{d}, \omega)$
*is* the Galois closure, Section 4.5), the absolute constant $c$ in
$N_C$ is traced through
$$2^{40}\cdot 36\cdot\log(6e)\cdot\pi\cdot(12H_1 + \pi)\cdot 4R$$
— i.e. $C_0 = 2^{40}D_0^2\log(eD_0) = 2^{40}\cdot 36\,(1 + \log 6)
\approx 1.105\times 10^{14}$ against $A_1 = \pi$, $A_2 = 12H_1 + \pi$,
$A_3 = 4R$ — before the $R$-cancellation. Dividing the zero inequality
$\tfrac{3R}{2}\,n \le 12H_1 + \log\tfrac{\pi}{4} + C_0\,\pi\,(12H_1 +
\pi)(4R)\log(e(n+2))$ by $3R/2$ cancels the $R$ in the Matveev term and
leaves
$$n \;\le\; \frac{8H_1}{R} \;+\; K\,(12H_1 + \pi)\,\log\bigl(e(n+2)\bigr),
\qquad K \;:=\; \tfrac{2}{3}\,C_0\,\pi\cdot 4 \;=\; 2^{40}\cdot 96\,\pi\,(1 + \log 6)
\;\approx\; 9.258\times 10^{14}.$$
Resolving $n$ against $\log n$ exactly as in the proof of Lemma C (via
$x \ge 2A\log A \Rightarrow x/\log x \ge A$; the term $8H_1/R$ is
$O(H_1)$ by the regulator floor) yields the explicit window
$$N_C \;\le\; \max\Bigl(\frac{16H_1}{R},\ 4K\,(12H_1 + \pi)\,\log\bigl(2eK\,(12H_1 + \pi)\bigr)\Bigr),$$
whose leading coefficient $48K \approx 4.44\times 10^{16}$ multiplies
$H_1\log(\cdot)$; under the factor-4 safety slack of the displayed
combined inequality in the proof of Lemma C (parameters $24H_1 + \pi$
and $8R$), $K$ is replaced by $4K \approx 3.703\times 10^{15}$ and the
leading coefficient by $\approx 1.78\times 10^{17}$. Either way the
coefficient governing $N_C$ is of order $10^{17}$, and the numeric value
of $c$ is thereby fixed; the elementary constants of Lemma U and
Proposition F and the branch conventions for $\log(-1)$ remain absorbed
into $|a| \le n+2$. Sha
remarks [Sha19, §2.4] that sharper three-logarithm bounds (Mignotte's
kit) carry side conditions that need not hold, so no off-the-shelf
improvement to the $2^{40}$ is available.

### 7.4 Relation to Smale's fifth problem

In the stratification of Smale's fifth problem that this program
maintains, genus-0 components with at least three places at infinity —
the stratum that classically reduces to Thue equations — form the first
wall past the conic/Pell layer. Theorem 1 breaches that wall at its
thinnest point: one fixed family, degree 3, pure. The strong empirical
window conjecture — every Thue-shape index of a unit-reduced
representative satisfies $|k| \le C(1 + \log|m|/R)$ — remains open
(max observed index: 3), as do the general-form extensions above, and, a
fortiori, the uniform question of the full stratum: is
$\{f : \text{every component of genus } 0\}$ decidable in time
$2^{O(s)}$ uniformly in the degree? The order-3 Skolem instance at the
heart of our walk is classically decidable (Mignotte–Shorey–Tijdeman
[MST84], Vereshchagin [Ver85]); our contribution is not decidability but
an instance-specific, fully explicit, two-sided window that is
exponential in the *input*, not in the regulator. We have not pursued
poly-size certificates; compact representations are exactly the extra
ingredient a certificate version would need (Lemma A′), a further
direction we leave open.

### 7.5 Beyond exponential time: the named obstructions

Deterministic *polynomial-time* decision for pure cubic Thue equations
is not a rewrite of this paper away: it faces three independent open
problems, which we name so that the reader can see exactly where the
exponential lives.

1. **The unit.** Polynomial-time computation of the regulator and the
   fundamental unit — even in compact representation — is equivalent to
   the principal ideal problem and is a major open problem of
   computational number theory, classically believed hard: it underlies
   infrastructure-based cryptography, and polynomial time is known only
   quantumly, by Hallgren-type algorithms [Hal07]. Note that even
   negative-Pell *decision*, one degree down, is in
   $\mathrm{NP} \cap \mathrm{coNP}$ (Lagarias [Lag79]) with no
   classical polynomial algorithm known.
2. **The zero test.** Certified zero-testing of the recurrence values
   against their $2^{O(s)}$-digit height bounds via modular evaluation
   needs exponentially many primes; per-prime testing yields only
   randomized decisions (coRP-style, as in straight-line-program
   zero-testing), whose derandomization is open.
3. **The window.** The scan window is quasi-linear in
   $R = 2^{\Theta(s)}$ unless the strong window conjecture of
   Remark 7.4 — empirical maximum index 3, Section 6.1 — is proven.

The natural next target is therefore NP membership — a cubic analogue
of Lagarias's Pell certificates [Lag79] — for which the strong window
conjecture is the enabler.

---

## References

- **[ADF16]** S. Astudillo, F. Díaz y Díaz, E. Friedman, *Sharp lower
  bounds for regulators of small-degree number fields*, J. Number Theory
  167 (2016) 232–258. (Theorem 7 and Table 1: the two regulator floors of
  Section 2.3.)
- **[AW04]** S. Alaca, K. S. Williams, *Introductory Algebraic Number
  Theory*, Cambridge University Press, 2004. (Standard modern account of
  pure cubic integral bases and unit inequalities.)
- **[BG96]** Y. Bugeaud, K. Győry, *Bounds for the solutions of
  Thue–Mahler equations and norm form equations*, Acta Arith. 74 (1996).
  (Best general effective height bounds; polynomial in coefficient
  magnitude, hence exponential in coefficient bit-size.)
- **[BH96]** Y. Bilu, G. Hanrot, *Solving Thue equations of high degree*,
  J. Number Theory 60 (1996) 373–392.
- **[BW87]** J. Buchmann, H. C. Williams, *On principal ideal testing in
  algebraic number fields*, J. Symbolic Comput. 4 (1987) 11–19.
  (Generator recovery $\mathfrak{a} = (\mu\,\alpha_k)$ along the cycle.)
- **[BW88]** J. Buchmann, H. C. Williams, *On the infrastructure of the
  principal ideal class of an algebraic number field of unit rank one*,
  Math. Comp. 50 (1988) 569–579. (The deterministic unconditional
  rank-one toolkit this paper runs on.)
- **[Ded00]** R. Dedekind, *Über die Anzahl der Idealklassen in reinen
  kubischen Zahlkörpern*, J. reine angew. Math. 121 (1900) 40–123. (The
  pure cubic index formula of Section 2.2.)
- **[Hal07]** S. Hallgren, *Polynomial-time quantum algorithms for
  Pell's equation and the principal ideal problem*, J. ACM 54 (2007).
  (The quantum route to the unit; cited in Remark 7.5.)
- **[Lag79]** J. C. Lagarias, *Succinct certificates for the solvability
  of binary quadratic Diophantine equations*, Proc. 20th IEEE FOCS
  (1979) 47–54; extended version arXiv:math/0611209. (§1.4 of the
  extended version quotes Smale's $2^{s^c}$ formulation.)
- **[Len92]** H. W. Lenstra, Jr., *Algorithms in algebraic number
  theory*, Bull. Amer. Math. Soc. 26 (1992) 211–244. (Thm. 6.5:
  $hR \le |\Delta|^{1/2}\mathrm{polylog}$ and the ideal-count bound;
  Thm. 5.5 cited as hedged fallback only.)
- **[Mat00]** E. M. Matveev, *An explicit lower bound for a homogeneous
  rational linear form in the logarithms of algebraic numbers. II*,
  Izv. Math. 64:6 (2000) 1217–1269. (Corollary 2.3, as restated in
  [Sha19, §2.4].)
- **[MST84]** M. Mignotte, T. N. Shorey, R. Tijdeman, *The distance
  between terms of an algebraic recurrence sequence*, J. reine angew.
  Math. 349 (1984) 63–76.
- **[PARI]** The PARI Group, *PARI/GP version 2.17.4*, Univ. Bordeaux.
  (`thueinit`/`thue` — flag-1 certification unconditional; `bnfinit`,
  `bnfcertify`, `bnfisintnorm`.)
- **[Sch08]** R. Schoof, *Computing Arakelov class groups*, in:
  Algorithmic Number Theory (J. P. Buhler, P. Stevenhagen, eds.), MSRI
  Publications 44, Cambridge University Press, 2008, 447–495.
  (General-rank infrastructure context for Sections 7.1–7.2.)
- **[Sha19]** M. Sha, *Effective results on the Skolem Problem for linear
  recurrence sequences*, J. Number Theory 197 (2019) 228–249;
  arXiv:1505.07147. (Theorems 1.1–1.2, Lemma 2.8, and the Matveev
  application — the extracted ingredients of Lemma C.)
- **[Sma96]** N. P. Smart, *How difficult is it to solve a Thue
  equation?*, in: Algorithmic Number Theory (ANTS-II), Lecture Notes in
  Computer Science 1122, Springer, 1996, 363–373. (The closest prior:
  per-method complexity estimate for the Tzanakis–de Weger pipeline.)
- **[Sma98]** S. Smale, *Mathematical problems for the next century*,
  Math. Intelligencer 20:2 (1998) 7–15; reprinted in *Mathematics:
  Frontiers and Perspectives*, AMS, 2000.
- **[TdW89]** N. Tzanakis, B. M. M. de Weger, *On the practical solution
  of the Thue equation*, J. Number Theory 31 (1989) 99–132.
- **[Ver85]** N. K. Vereshchagin, *Occurrence of zero in a linear
  recursive sequence*, Math. Notes Acad. Sci. USSR 38:2 (1985) 609–615.
- **[Wil85]** H. C. Williams, *Continued fractions and number-theoretic
  computations*, Rocky Mountain J. Math. 15 (1985) 621–655. (Venue
  sometimes misquoted as Pacific J. Math.; the correct venue is Rocky
  Mountain J. Math.)
- **[Wil86]** H. C. Williams, *The spacing of the minima in certain cubic
  lattices*, Pacific J. Math. 124 (1986) 483–496. (Spacing constants;
  scope: all complex cubic fields and arbitrary reduced lattices.)

---

[^smart]: Verified against the openly available portion of the primary
    text: the publisher's two-page preview of [Sma96] (pp. 363–364)
    confirms the fixed-degree setting, the complexity measure
    $\log|m| + \log L(F)$, the three-phase division of the solution
    space, the failure modes, and the announced "overall exponential
    complexity bound in terms of $\log L(F)$"; the concluding quotation
    is reproduced verbatim in R. J. Stroeker's zbMATH review
    (Zbl 0896.11009). The remainder of the text (pp. 365–373) is
    paywalled; per-phase exponent shapes reported in secondary sources —
    e.g. a small-solutions cost of $O(|m|^{1/(n-2)})$ — are therefore
    not quoted above, and nothing in Section 1.2 depends on them: the
    gap claim rests on the sweep of the books and surveys, not on the
    exact exponents of [Sma96].

[^slack]: The displayed combined inequality retains the verified notes'
    doubled parameters $24H_1 + \pi$ and $8R$, a factor-4 safety slack
    over the minimal admissible Matveev choices $A_2 = 12H_1 + \pi$,
    $A_3 = 4R$ listed above; the slack is absorbed into the final
    constant evaluation flagged in Remark 7.3 and does not affect the
    shape of $N_C$.
