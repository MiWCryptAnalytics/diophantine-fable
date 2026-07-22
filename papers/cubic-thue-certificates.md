# Certificates for pure cubic Thue equations: Merlin–Arthur membership and the Compact Vanishing Problem

**The diophantine-fable expedition** (draft — authorship placeholder)

Sequel draft of 2026-07-22, assembled from the certificate notes; a
companion to the exponential-time paper [companion], whose notation
it reuses. Every honesty flag of the notes is carried forward:
sketches are labeled, quoted-standard facts are flagged, the status
ledger is reproduced in Section 7, and no claim below exceeds what
the underlying notes established.

---

## Abstract

For the pure cubic Thue equation $x^3 - d\,y^3 = m$, the companion
paper gave a deterministic $2^{O(s)}$ decision algorithm. Here we ask
what *certifies* solvability. The certificate collapses to a single
object: a Thiel-format compact representation of the solution element
$\beta = x - y\alpha$ itself. Integrality and the norm equation
$N(\beta) = m$ verify deterministically in polynomial time — the
latter by multiplicativity of norms on power products, the mechanism
behind Lagarias's Pell certificates and Ge's equality tests.
Membership in **MA** follows unconditionally. Membership in **NP** is
equivalent, modulo this architecture, to one newly isolated problem —
the **Compact Vanishing Problem** (CVP): decide deterministically
whether a fixed coordinate functional vanishes at a compactly
represented algebraic integer. We classify CVP into the
sum-of-square-roots family, prove that ideal-theoretic and
radical-rigidity methods cannot express it, and explain by a vacuity
remark why Lagarias's degree-2 certificates never met it.

---

## 1. Introduction

### 1.1 From decision to certification

The companion paper [companion] proved that pure cubic Thue equations
$x^3 - d\,y^3 = m$ ($d \ge 2$ cube-free, not a cube; $m \ne 0$; input
size $s = O(\log d + \log|m|)$ in binary) are decided, with full
solution lists, by a deterministic unconditional algorithm in time
$2^{O(s)}$ — a first worst-case bound of this shape for a Thue
stratum of Smale's fifth problem [Sma98]. Its Remark 7.5 named the
three obstructions to *polynomial-time* decision: the unit (the
principal ideal problem, classically believed hard, polynomial only
quantumly [Hal07]); the zero test (certified zero-testing against
$2^{O(s)}$-digit height bounds); and the window (quasi-linear in
$R = 2^{\Theta(s)}$ [companion, Lemma C, after Sha [Sha19]] unless
the strong window conjecture is proven).

The natural target below polynomial time is therefore **NP
membership**: poly-size certificates, deterministic poly-time
verification. This paper is that pivot, and its outcome is
asymmetric: two thirds of the verifier's work is classical and easy,
and the entire remaining difficulty isolates into one new problem.

### 1.2 One rung down: Lagarias's Pell certificates

Lagarias [Lag79] proved that solvability of binary quadratic
Diophantine equations over $\mathbb{Z}$ is in NP, although the
fundamental solutions have exponentially many digits: the certificate
is a power-product representation, and both verifiable conditions —
integrality and the norm equation — are *multiplicative*, hence
compatible with power products. (Negative Pell decision is even in
NP $\cap$ coNP by the same technology, with no classical polynomial
algorithm known.) This paper asks what happens to that magic one rung
up, at degree 3.

### 1.3 The two main results, and the crux they isolate

The certificate architecture (Section 2) simplifies an outside
reviewer's proposed three-part scheme (unit + reduced representative
+ orbit index): all three collapse into the single object $\beta$,
the solution element itself in compact representation. Verification
splits into three steps — integrality, norm, Thue shape — and:

- **Integrality and norm verify deterministically in polynomial
  time** (Section 2), by the format's denominator bookkeeping and by
  norm multiplicativity on power products, the latter a special case
  of Ge's deterministic multiplicative-relation testing [Ge93].
- **Proposition 3.1 (MA membership, unconditional).** Pure cubic Thue
  solvability is in MA, with one-sided error: the remaining condition
  — the vanishing of one coordinate — is testable modulo random
  primes, with the prime range calibrated against an explicit height
  bound extracted from the compact data.
- **The crux (Section 4).** The single non-derandomized step is
  named: **CVP, the Compact Vanishing Problem** — decide
  deterministically whether a fixed $\mathbb{Q}$-linear coordinate
  functional vanishes at a compactly represented algebraic integer.
  Cubic Thue $\in$ NP **iff-modulo** CVP (Corollary 4.1, with the
  honest gloss given there); conditionally, under derandomization
  hypotheses implying MA = NP, membership in NP holds today.
- **The vacuity remark (Remark 4.5).** At degree 2 the module
  $\mathbb{Z} + \mathbb{Z}\sqrt{d}$ is *all* of
  $\mathbb{Z}[\sqrt{d}]$: the shape condition is vacuous and CVP
  never arises. The coordinate condition is genuinely new at degree 3
  — CVP, not the unit computation, is the honest frontier of the NP
  question.

Section 5 explains why CVP resists the classical toolbox: four
attack routes — Thiel/Ge equality testing, Blömer's radical sums,
ideal-theoretic reformulations, the Baker route — are each shown
inapplicable, for one unified reason.

### 1.4 Organization

Section 2 fixes the certificate and verifier; Section 3 proves MA
membership; Section 4 states CVP, its three faces, and the vacuity
remark; Section 5 is the impossibility ledger; Sections 6–7 collect
positive fragments, open problems, and the status ledger.

---

## 2. The certificate and the verifier

### 2.1 Notation (from the companion)

$d = ab^2 \ge 2$ cube-free, not a cube, $a, b$ coprime squarefree;
$\alpha = \sqrt[3]{d}$; $K = \mathbb{Q}(\alpha)$, complex cubic, one
real embedding $\sigma_1$ and a conjugate pair $\sigma_2, \sigma_3$;
unit group $\langle -1, \varepsilon \rangle$ of rank one, regulator
$R = \log \sigma_1(\varepsilon) = 2^{O(s)}$ [companion, §2.3]. For
$g \in K$ write $g = c_0(g) + c_1(g)\alpha + c_2(g)\alpha^2$; the
index $[O_K : \mathbb{Z}[\alpha]]$ divides $3b$, so $3b\,c_i(g) \in
\mathbb{Z}$ for $g \in O_K$ [companion, §2.2]. A solution $(x, y)$ of
$x^3 - dy^3 = m$ is the element $\beta = x - y\alpha \in
\mathbb{Z}[\alpha]$ with $N(\beta) = m$ and **Thue shape**
$z(\beta) := c_2(\beta) = 0$. We write $M := \mathbb{Z} +
\mathbb{Z}\alpha$ for the rank-2 module in which solutions live.

### 2.2 Compact representations

A **compact representation** (Thiel format) of $\beta \in O_K$ is a
power product
$$\beta \;=\; \beta_0 \cdot \prod_{i=1}^{T} \beta_i^{2^i},$$
with $T = O(\log h(\beta))$ factors, each $\beta_i \in K$ given by
$\mathrm{poly}(s)$ bits of coordinate and denominator data. We quote
the existence and size bounds as standard [Thi95; BTW95] *(ledger
flag: quoted, not re-derived; a dedicated citation pass is owed)*.

For our instances a solution element has $\log$-height
$O(R + \log|m|) = 2^{O(s)}$ (unit reduction and the two-sided window
of [companion, Lemmas U and C]), so $T = O(s)$: the certificate has
$\mathrm{poly}(s)$ size. Existence is *constructive*: the honest
prover runs the companion's exponential algorithm once; the
tracked-generator walk of [companion, Lemma A′], compacted by
repeated-squaring doubling [BW88; Sch08], emits exactly this format.

### 2.3 The certificate is the solution element itself

> **Certificate (YES instances).** A Thiel-format compact
> representation of $\beta = x - y\alpha$.

No $\varepsilon$, no reduced representative, no orbit index $k$, no
window: if $\beta$ is a solution, its compact representation alone
witnesses it. In particular the strong window conjecture of
[companion, Remark 7.4] is *not needed* for YES-certificates at all;
it re-enters only for the prover-efficiency narrative and on the coNP
side (Section 6.2).

### 2.4 The verifier, step by step

1. **V1 — Integrality**: $\beta \in O_K$, and $\beta \in
   \mathbb{Z}[\alpha]$ after the $3b$-bookkeeping. Deterministic
   polynomial time: the format carries denominator data checked by
   exact ideal arithmetic on $\mathrm{poly}$-size objects; and since
   coordinate denominators in $O_K$ divide $3b$, membership in
   $\mathbb{Z}[\alpha]$ is a *congruence* condition modulo $3b$,
   computable by repeated squaring in a $\mathrm{poly}(s)$-size
   quotient ring. *(Mechanism sketch; the format-level details are
   Thiel's.)*
2. **V2 — Norm**: $N(\beta) = m$. Deterministic polynomial time,
   because **norms are multiplicative on power products**:
   $$N(\beta) \;=\; N(\beta_0)\cdot\prod_{i=1}^{T}
   N(\beta_i)^{2^i},$$
   each $N(\beta_i)$ a small explicit rational, exponents in binary —
   exactly the magic that powered Lagarias's Pell certificates
   [Lag79]. Verifying the exponent identity without factoring is
   standard multiplicative technology: coprime-basis bookkeeping
   [vG25], or a special case of Ge's multiplicative-relation test
   [Ge93]; the sign is read off certified embedding data. *(Sketch;
   the point is that every ingredient is multiplicative.)*
3. **V3 — Thue shape**: $z(\beta) = 0$. **This is the entire
   remaining difficulty.** It is testable *randomly* in polynomial
   time (Section 3); whether *deterministically* is precisely CVP
   (Section 4).

Completeness of the architecture is immediate: $\beta \in
\mathbb{Z}[\alpha]$ with $N(\beta) = m$ and $c_2(\beta) = 0$ *is* a
solution $(x, y) = (c_0(\beta), -c_1(\beta))$, and conversely.

---

## 3. Merlin–Arthur membership

> **Proposition 3.1 (MA membership, unconditional).** Pure cubic Thue
> solvability is in MA, with perfect completeness and one-sided,
> amplifiable soundness error.

*Proof (complete modulo the compact-representation format bounds
quoted in Section 2.2).* Merlin sends the compact representation of a
claimed solution element $\beta$. Arthur runs V1 and V2 of Section
2.4 deterministically, then tests V3 modulo random primes.

**The integer to test.** Since $\alpha, \beta \in O_K$, the trace
$W := \mathrm{Tr}_{K/\mathbb{Q}}(\beta\alpha)$ is a rational integer,
and by the trace identity of Section 4.2,
$$z(\beta) = 0 \iff W = 0.$$

**Height bound from the compact data.** Embeddings are multiplicative
on the format: for each $j$,
$$\log|\sigma_j(\beta)| \;=\; \log|\sigma_j(\beta_0)| +
\sum_{i=1}^{T} 2^i \log|\sigma_j(\beta_i)|.$$
Each factor carries $\mathrm{poly}(s)$ bits, so
$\log|\sigma_j(\beta_i)| \le P(s)$ for an explicit polynomial $P$,
and $T = O(s)$ gives $\log_2\mathrm{house}(\beta) \le P(s)\,2^{T+1}
\le 2^{c_3 s}$ for an explicit $c_3$. Hence
$|W| \le 3\,\mathrm{house}(\beta)\,\mathrm{house}(\alpha)$, so
$\log_2 |W| \le 2^{c_3 s} + O(s) \le 2^{c_4 s}$; if $W \ne 0$, its
number of distinct prime divisors obeys $\omega(W) \le \log_2|W| \le
2^{c_4 s}$.

**The prime range for a $2/3$ threshold.** Let $E$ be the set of
primes dividing $3d$ or any denominator in the format;
$\#E \le \mathrm{poly}(s)$. Arthur draws $p$ uniformly from the
primes in $[17, 2^t]$: by Chebyshev-type bounds ($\pi(x) > x/\ln x$
for $x \ge 17$), the choice $t = c_4\,s + O(\log s)$, with explicit
absolute constants, supplies at least $3\,(\omega(W) + \#E)$ primes,
so $\Pr[\,p \in E \text{ or } p \mid W\,] \le 1/3$. If $p \in E$,
Arthur accepts vacuously (inside the $1/3$). Otherwise he computes
$W \bmod p$ in polynomial time: writing multiplication-by-$\beta_i$
as $3\times 3$ rational matrices $M_{\beta_i}$ in the power basis, he
evaluates $M_\beta \equiv M_{\beta_0}\prod_i M_{\beta_i}^{2^i}
\pmod p$ by repeated squaring, then
$W \equiv \mathrm{tr}(M_\beta M_\alpha) \bmod p$, accepting iff
$W \equiv 0$.

**Completeness.** For a YES instance Merlin sends a true solution
element: V1, V2 pass deterministically and $W = 0$, so $W \equiv 0$
modulo *every* prime — Arthur accepts with probability 1.

**Soundness (one-sided).** For a NO instance, any certificate passing
V1 and V2 must have $z(\beta) \ne 0$ — otherwise $\beta$ would be a
solution — hence $W \ne 0$, and Arthur rejects with probability
$\ge 2/3$. Arthur never rejects a valid certificate.

**Amplification.** $k$ independent primes give error $(1/3)^k$;
widening the range to $2^{s^c}$, $c \ge 2$, already makes a single
prime's error exponentially small, since $\omega(W)/\pi(2^{s^c}) \le
2^{c_4 s - s^c}\,\mathrm{poly}(s)$. $\blacksquare$

*Complexity-class bookkeeping.* Step V3 alone is a coRP test:
vanishing instances are accepted with probability 1, non-vanishing
instances rejected with high probability. The outer existential
quantifier over certificates therefore places the decision problem in
$\exists\cdot\mathrm{coRP} = \mathrm{MA}$ — which is the precise sense
of Proposition 3.1.

*(Provenance: the notes' ledger listed this as "proposition-with-
sketch, needs a careful write-up (height bound on $z(\beta)$ from the
compact data; prime-range constants)". The bounds above discharge
those two items; the residual dependence is the quoted format bounds
of Section 2.2.)*

---

## 4. The Compact Vanishing Problem

### 4.1 Statement and consequence

> **CVP$_K$ (Compact Vanishing Problem).** Given a compact
> representation of an algebraic integer $\beta$ in a fixed cubic
> field $K$, decide in deterministic polynomial time whether a fixed
> $\mathbb{Q}$-linear coordinate functional vanishes at $\beta$.

For our instances the functional is $c_2$, the $\alpha^2$-coordinate
in $K = \mathbb{Q}(\sqrt[3]{d})$. (The acronym clash with the lattice
Closest Vector Problem is noted; no lattice problem appears here.)

> **Corollary 4.1 (NP iff-modulo CVP).** If CVP$_K \in$ P for the
> instances arising from Thue certificates, then pure cubic Thue
> solvability is in NP, unconditionally. Conversely — the
> "iff-modulo" gloss, architectural rather than formal — CVP is the
> *only* step of the canonical verifier that is not deterministic
> polynomial time: any NP proof through this certificate collapses to
> deciding CVP on these instances. Under standard derandomization
> hypotheses (which give MA = NP), NP membership holds conditionally
> today.

The notes established three equivalent faces of CVP: a trace form, a
lattice-membership form, a bounded-width branching-program form.

### 4.2 Face one: the trace form

For $\beta = x + y\alpha + z\alpha^2$ one computes $\beta\alpha =
zd + x\alpha + y\alpha^2$, and $\mathrm{Tr}(1) = 3$,
$\mathrm{Tr}(\alpha) = \mathrm{Tr}(\alpha^2) = 0$ give
$$\mathrm{Tr}(\beta\alpha) \;=\; 3d\,z, \qquad\text{i.e.}\qquad
z(\beta) \;=\; \frac{\mathrm{Tr}(\beta\alpha)}{3d}.$$
CVP for our functional is exactly: *is $\mathrm{Tr}(\beta\alpha) = 0$
for compact $\beta$?* The coordinate functionals *are* trace forms —
the dual basis of the power basis under the trace pairing gives
$c_2(\beta) = \mathrm{Tr}(w\beta)$ with $w = \alpha/(3d)$, and
likewise for $c_1, c_0$ (identities machine-checked during this
draft's assembly).

### 4.3 Face two: plane membership for Arakelov-pinned elements

The second face rests on a small clean result, the micro-yield of the
notes' Ge-lattice attempt.

> **Lemma 4.3 (Arakelov pinning).** From a valid compact
> representation of $\beta \in O_K$, a deterministic polynomial-time
> verifier computes the full **Arakelov divisor** of $\beta$: the
> exact ideal $I = (\beta)$ in Hermite normal form, and the
> log-embeddings $\log|\sigma_j(\beta)|$ to any requested
> $\mathrm{poly}(s)$ precision. This data determines $\beta$ up to
> sign.

*Proof sketch.* The ideal: clear the format's denominators first and
work with the numerator ideal of the compacted element — so that $I$
is integral, as the HNF intersection $L = I \cap M$ of Section 4.3
strictly requires — then reduce the power product by repeated
squaring on reduced ideals with tracked distances — infrastructure
arithmetic is precisely this machinery [BW88; Sch08] — every
intermediate object staying $\mathrm{poly}$-size. The logs: interval
arithmetic on the factors' certified embedding data, via the exact
telescoping of Section 3. Uniqueness: if $(\beta) = (\beta')$ with
equal log vectors, $\beta/\beta'$ is a unit with vanishing
log-embeddings, hence torsion, hence $\pm 1$ (the torsion of $K$ is
$\{\pm 1\}$ by the real embedding). $\blacksquare$ *(sketch)*

So the certificate pins a *unique* candidate (up to sign, harmless
since $z(-\beta) = -z(\beta)$): **compact certificates verify
everything about $\beta$ except one plane membership.** Indeed
$z(\beta) = 0 \iff \beta \in M$, and $L := I \cap M$ is an explicit
rank-2 lattice with a $\mathrm{poly}$-size basis (HNF intersection).
Hence:

> **CVP (Thue instances) $\iff$ does the element pinned by a given
> Arakelov divisor lie in an explicit rank-2 sublattice?**

### 4.4 Face three: width-3 ABP trace zero-testing

Writing multiplication-by-$\beta_i$ as $3\times 3$ integer matrices
(after clearing the format's denominators), the compact
representation becomes a **matrix word with repeated-squaring
structure**, and by the trace form CVP reads: *decide whether the
trace of a width-3 integer matrix word is zero*. That is polynomial
identity testing for width-3 algebraic branching programs — a highly
structured, whitebox, repeated-squaring instance, and the right
literature door: it connects the NP question for cubic Thue equations
to bounded-width PIT derandomization by the shortest path we know of
(Section 5.4). One structural advantage must be stated explicitly: the
matrices $M_{\beta_i}$ all lie in the commutative subalgebra
$\mathbb{Q}[M_\alpha] \cong K$ of $3\times 3$ matrices — the word is
not a generic non-commutative width-3 ABP but one over a
**commutative** matrix ring, a class significantly better understood
in the PIT literature and correspondingly a more tempting target for
derandomization.

### 4.5 Remark (Lagarias vacuity: why 1979 stopped at degree 2)

In the quadratic case the module $\mathbb{Z} + \mathbb{Z}\sqrt{d}$ is
*all* of $\mathbb{Z}[\sqrt{d}]$: the Thue-shape condition is vacuous,
CVP never arises, and norm-checking alone suffices — which is why
Lagarias's certificates [Lag79] close at degree 2 with purely
multiplicative technology. The coordinate condition is genuinely
**new at degree 3**: CVP is exactly what separates the cubic
certificate problem from Pell — this, not the unit computation, is
the honest frontier of the NP question, and the explanation of the
shift from degree 2 (NP since 1979) to degree 3 (MA now).

---

## 5. Why the classical toolbox stops

We place CVP on the map, then close four attack routes — distilling
the notes' 1991–2026 literature sweep and recorded attempts. No route
is closed by a hardness theorem; each is closed by structural
inapplicability, a different and more instructive thing.

### 5.0 Where CVP sits: the sum-of-square-roots family

The cleared trace value admits a $\mathrm{poly}(s)$-size
straight-line program (repeated squaring), so CVP is an instance of
EquSLP — zero-testing SLP-given integers — in coRP (the random-prime
test of Section 3; the observation goes back to Schönhage [Sch79]),
with its positivity cousin PosSLP in the counting hierarchy [ABKM09;
ESY14]. Deterministic polynomial time is open for the whole family,
whose totem is the sum-of-square-roots problem: poly-time for
explicitly given radical sums [Blo91], uniform TC$^0$ for deciding
whether a rational radical sum is rational [HBMOW10], the
separation-bound frontier only recently moved by the subspace theorem
[EHS24]. The notes' verdict, adopted here: CVP is **genuinely new, of
sum-of-square-roots-class flavor** — in coRP, in CH, deterministic
case open — with one unexplored asset recorded in Section 7.2.

### 5.1 The additive/multiplicative divide

Thiel-style deterministic *equality* testing of compact
representations is a **multiplicative** technology: $\beta = \gamma$
reduces to the quotient being $1$, and units $\ne \pm1$ are separated
from $1$ by Dobrowolski-type height lower bounds [Dob79] on the
log-embedding lattice — polynomial precision suffices. Ge's theorem
[Ge93] (see [vG25, Thm. 165]) extends this: *multiplicative
relations* among power products are decidable in deterministic
polynomial time — exactly why the norm step V2 is easy. The
compact-representation toolbox stops at the trace, precisely: [BTW95]
adds two-term sign comparison in real quadratic fields, and **no
additive $\ge 3$-term test exists anywhere in the literature**.

CVP is **additive**: $\mathrm{Tr}(\beta\alpha)$ is a sum of three
conjugate terms. Separation is not the problem — integrality gives it
for free (the cleared value is a rational integer, so nonzero means
$\ge 1$). **Evaluation is the problem**: certifying the sum
numerically needs absolute precision comparable to the archimedean
spread $\max_j \log|\sigma_j(\beta)| - \min_j \log|\sigma_j(\beta)|$,
and for *true* Thue solutions the spread is $2^{\Theta(s)}$ forced: a
solution has $|\sigma_1(\beta)| = |m|/|\sigma_2(\beta)|^2$ tiny
*precisely because* it is a solution. The easy "balanced-$\beta$"
case of CVP can therefore never contain the instances we care about.
The angle formulation hits the same wall: verifying
$\arg \sigma_2(\beta\alpha) \approx \pm\pi/2$ to error
$e^{-\mathrm{spread}}$ needs the small factors' arguments to
exponentially many bits.

**The conjugate-certificate attempt, and its circle.** One can move
to the Galois closure $L = K(\omega)$ and note
$\mathrm{Tr}(\beta\alpha) = 0 \iff \beta + \omega\sigma_2(\beta) +
\omega^2\sigma_3(\beta) = 0$; certifying compact representations of
the conjugates is fine, but the final check is again an additive
vanishing of compact objects — the divide reappears intact. **Sums of
compact representations are not compact; that sentence is the
obstacle.**

### 5.2 Blömer is structurally inapplicable, not merely insufficient

Blömer's deterministic polynomial-time algorithms for sums of
radicals [Blo91; Blo93] might look like the natural import: our
elements are $\mathbb{Q}$-combinations of $1, d^{1/3}, d^{2/3}$. But
his determinism rides on *Siegel-type rigidity*: independent radicals
admit **no** nontrivial $\mathbb{Q}$-linear relations, so
zero-testing reduces to coefficient collection on explicit poly-size
coefficients. Our trace-zero instances **are** nontrivial relations
in the rank-2 trace-zero module — the exact phenomenon his theorem
excludes — with coefficients $x, y, z$ compact rather than explicit.
Both pillars — rigidity and explicit arithmetic — fail
simultaneously.

### 5.3 No ideal-theoretic route: the hyperplane argument

The tempting program "tear into Thiel's ideal equality tests to break
CVP" is closed before it opens, by rank counting.

> **Proposition 5.1.** No ideal containment, equality, or
> divisibility statement in $O_K$ can express the condition
> $z(\beta) = 0$, even in principle.

*Proof.* The trace-zero condition $\mathrm{Tr}(\beta\alpha) = 0$
defines a $\mathbb{Q}$-**hyperplane** in $K$ (the coordinate
functionals are trace forms, Section 4.2). Ideals are **full-rank**
$\mathbb{Z}$-modules: any nonzero ideal of $O_K$ has rank 3, while
any module contained in the hyperplane has rank $\le 2$. $\blacksquare$

Thiel/Ge machinery tests relations among full-rank multiplicative
objects; CVP lives in a corank-1 additive slice invisible to all of
them. The bridge of Section 5.5 is not hiding inside ideal
arithmetic; it must be genuinely new.

### 5.4 The EquSLP caution, and the Baker route's ceiling

Two doors from complexity theory, each honestly measured:

- **Iterated squaring is the hard core.** ABKM [ABKM09, Prop. 2.1]
  show that EquSLP's difficulty concentrates on repeated-squaring
  instances — our shape — and derandomizing such identity tests
  implies circuit lower bounds [KI04]. This is **a caution, not a
  hardness proof**, for our width-3 single words: CVP could be easy
  without lower-bound consequences, but the precedent says the
  general-toolbox route is priced.
- **The Baker route has a height ceiling.** Galby–Ouaknine–Worrell
  [GOW15] decide sign and zero questions for entries of $M^n$,
  $\dim \le 3$, in polynomial time — for **poly-height** inputs: the
  engine is lower bounds for linear forms in logarithms [Mat00],
  whose constants stay polynomial only while heights and the number
  of logarithms stay bounded. Thue certificates have
  $h(\varepsilon) = R/3 = 2^{\Theta(s)}$; at $\Theta(s)$ logarithms
  the Baker constants degrade exponentially — the same wall that pins
  LRS Positivity at order $\ge 6$ [OW14]. The bounded fragment this
  route *does* give is Proposition 6.1.

### 5.5 One wall, four costumes; the missing tool, named

The four failures above are one wall:

1. **Trace non-multiplicativity** (Section 5.1).
2. **Sums of compacts are not compact** (Section 5.1).
3. **The archimedean spread** (Section 5.1): $2^{\Theta(s)}$
   precision forced exactly on true solutions.
4. **Plane non-stability** (the notes' Ge-lattice attempt): the
   rescaling trick — bring the thin strip
   $\{|x - y\alpha| \sim e^{\ell_1}\}$ to bounded size by
   $\varepsilon^{-j}$ — dies because $M$ is not stable under units:
   $\varepsilon^{-j}M \ne M$. Lattice-point location in the plane is
   polynomial *at polynomial scales*, but our scales are
   $e^{2^{O(s)}}$, described only by their logs.

What a solution needs, stated once: a **multiplicative-to-additive
bridge** — any theorem letting membership in a fixed rank-2 plane be
tested through data carried multiplicatively (relation lattices,
Arakelov classes, unit orbits). Nothing in the 1991–2026 literature
provides one; building it is the actual open problem, and by Section
4.3 it now has a precise geometric formulation.

---

## 6. Positive fragments

### 6.1 The bounded fragment: CVP at bounded rank and small height

> **Proposition 6.1 (bounded CVP — stated with a proof plan).**
> Restrict CVP$_K$ to instances whose factor list
> $\{\beta_0, \ldots, \beta_T\}$ generates a subgroup of
> $K^\times/\{\pm1\}$ of multiplicative rank $O(1)$ admitting
> generators of Weil height $\mathrm{poly}(s)$. This fragment is
> decidable in deterministic polynomial time.

*Proof plan (honestly flagged: a plan, not a proof).* (1) Compute the
relation lattice of the factors — deterministic polynomial time by Ge
[Ge93; vG25, Thm. 165] — and rewrite the word over $O(1)$
independent poly-height generators with binary exponents. (2) The
trace becomes a fixed short sum of conjugate power products in $O(1)$
poly-height bases. (3) Zero-test via the Baker–Matveev machinery as
in the dimension-3 matrix-power analysis of [GOW15]: with $O(1)$
logarithms of poly-height numbers and binary exponents, Matveev's
bounds [Mat00] are polynomial — noting that Matveev's constant
degrades exponentially in the number $k$ of logarithms, which is
exactly why the $O(1)$ multiplicative-rank restriction is
load-bearing and cannot be relaxed, so certified interval evaluation at
$\mathrm{poly}(s)$ precision decides against the free integrality
separation. Steps (2)–(3) need the same case-discipline GOW exercise
at dimension 3 and are not written out here.

*What this fragment is and is not.* It is the notes' verdict
"publishable-but-bounded". It does **not** cover Thue certificates:
their factor lists contain $\varepsilon$ (or its walk factors), of
height $R/3 = 2^{\Theta(s)}$ — precisely the ceiling of Section 5.4.
No claim of progress on the Thue NP question is made here.

### 6.2 The strong window conjecture: prover efficiency and coNP

The strong window conjecture [companion, Remark 7.4] — every
Thue-shape index of a unit-reduced representative satisfies
$|k| \le C(1 + \log|m|/R)$, hence $O(s)$ by the regulator floor
[ADF16] — turned out to be unnecessary for YES-certificates
(Section 2.3). Its remaining roles: **prover efficiency** — the
honest prover runs the companion's algorithm once ($2^{O(s)}$); the
conjecture caps the final scan at $O(s)$ indices per representative,
though the infrastructure walk remains $\widetilde{\Theta}(R)$, so it
trims the narrative, not the exponential — and **the coNP side**,
where certifying a NO instance would require certifying every ideal
class's orbit window zero-free, and the conjecture caps the indices
to certify per orbit at $\mathrm{poly}(s)$, making class-enumeration
NO-certificates conceivable. *(Ledger flag, preserved: the coNP side
is untouched in this work.)*

---

## 7. Open problems

### 7.1 CVP itself

Is CVP$_K$ — even just for Thue-shaped instances — in P? The notes'
two probed routes are blocked, not dead: the *p-adic route*
($\mathrm{ord}_p$ of power products is poly-computable per prime)
stumbles on the fact that valuations do not see addition; the
*canonical-form route* (Thiel equality of $\beta$ against its
projection) needs a compact representation of the projection, and
sums of compacts are not compact. The sharpest open formulation is
the ABP face: **is the repeated-squaring width-3 matrix-word class
among the deterministically testable bounded-width PIT cases?** A
positive answer completes: cubic Thue $\in$ NP, unconditionally —
Lagarias one rung up, for real.

### 7.2 The multiplicative-to-additive bridge

Build any theorem letting membership in a fixed rank-2 plane be
tested through multiplicatively carried data (Section 5.5). The one
unexplored asset, recorded in the notes' literature verdict: our
three summands are Galois-conjugate, and the bases' full
multiplicative relation lattice is *computable* (Ge). The additive
analog of [vG25, Lemma 166] — detecting trace-zero from the relation
lattice plus unit-lattice geometry — has never been attempted. That
is the door.

### 7.3 DIVIS hardness

The program's synthesis records that the divisibility language
$\mathrm{DIVIS} = \{(A, B) \in \mathbb{Z}[x]^2 : \exists x \in
\mathbb{Z},\ A(x) \mid B(x)\}$ is in NP (two proofs, one the
expedition's, by an elementary integer-remainder argument — Runge in
miniature); its hardness is unstudied. It is the nearest candidate
for a hardness foothold adjacent to the Thue stratum.

### 7.4 The coNP certificate question

Is pure cubic Thue solvability in coNP? Degree 2 says yes one rung
down (negative Pell is in NP $\cap$ coNP [Lag79]). At degree 3 the
ingredients on the table are the strong window conjecture and
class-enumeration certificates (Section 6.2); nothing beyond the
framing exists yet.

### Status ledger (carried from the notes, unchanged in spirit)

- MA membership: proposition with the height-bound and prime-range
  write-up now supplied (Section 3); residual dependence on the
  quoted compact-representation format bounds (Section 2.2).
- Compact-representation existence and size for $\beta$: standard;
  the precise citation pass (Thiel; Buchmann–Thiel–Williams) is still
  owed.
- CVP: open, named, isolated — the right-sized next mathematics.
- coNP side: untouched here.
- Pre-submission (per outside critique): pinpoint the exact theorem
  extending Thiel-format size bounds to cubic fields (Thiel's thesis;
  BW88; Sch08) — and only after that debt is paid, strip the ledger
  flags from the final text. Flags come off when debts are paid, not
  before.

---

## References

- **[ABKM09]** E. Allender, P. Bürgisser, J. Kjeldgaard-Pedersen, P. B. Miltersen,
  *On the complexity of numerical analysis*, SIAM J. Comput. 38:5 (2009) 1987–2006.
- **[ADF16]** S. Astudillo, F. Díaz y Díaz, E. Friedman, *Sharp lower bounds for
  regulators of small-degree number fields*, J. Number Theory 167 (2016) 232–258.
- **[Blo91]** J. Blömer, *Computing sums of radicals in polynomial time*,
  Proc. 32nd IEEE FOCS (1991) 670–677.
- **[Blo93]** J. Blömer, *Simplifying expressions involving radicals*, PhD thesis,
  Freie Universität Berlin, 1993.
- **[BTW95]** J. Buchmann, C. Thiel, H. C. Williams, *Short representation of
  quadratic integers*, in: Computational Algebra and Number Theory,
  Math. Appl. 325, Kluwer, 1995, 159–185.
- **[BW88]** J. Buchmann, H. C. Williams, *On the infrastructure of the principal
  ideal class of an algebraic number field of unit rank one*, Math. Comp. 50
  (1988) 569–579.
- **[companion]** The diophantine-fable expedition, *Pure cubic Thue equations are
  solvable in deterministic exponential time*, companion manuscript,
  `papers/cubic-thue-exp.md` in this repository (draft of 2026-07-22).
- **[Dob79]** E. Dobrowolski, *On a question of Lehmer and the number of
  irreducible factors of a polynomial*, Acta Arith. 34 (1979) 391–401.
- **[EHS24]** F. Eisenbrand, M. Haeberle, N. Singer, *An improved bound on sums of
  square roots via the subspace theorem*, Proc. SoCG 2024, LIPIcs 293, art. 54.
- **[ESY14]** K. Etessami, A. Stewart, M. Yannakakis, *A note on the complexity of
  comparing succinctly represented integers, with an application to maximum
  probability parsing*, ACM Trans. Comput. Theory 6:2 (2014), art. 9.
- **[Ge93]** G. Ge, *Testing equalities of multiplicative representations in
  polynomial time*, Proc. 34th IEEE FOCS (1993) 422–426; and PhD thesis
  (*Algorithms related to multiplicative representations of algebraic numbers*),
  U.C. Berkeley, 1993.
- **[GOW15]** E. Galby, J. Ouaknine, J. Worrell, *On matrix powering in low
  dimensions*, Proc. STACS 2015, LIPIcs 30, 329–340.
- **[Hal07]** S. Hallgren, *Polynomial-time quantum algorithms for Pell's equation
  and the principal ideal problem*, J. ACM 54:1 (2007), art. 4.
- **[HBMOW10]** P. Hunter, P. Bouyer, N. Markey, J. Ouaknine, J. Worrell,
  *Computing rational radical sums in uniform TC⁰*, Proc. FSTTCS 2010, LIPIcs 8,
  308–316.
- **[KI04]** V. Kabanets, R. Impagliazzo, *Derandomizing polynomial identity tests
  means proving circuit lower bounds*, Comput. Complexity 13 (2004) 1–46.
- **[Lag79]** J. C. Lagarias, *Succinct certificates for the solvability of binary
  quadratic Diophantine equations*, Proc. 20th IEEE FOCS (1979) 47–54; extended
  version arXiv:math/0611209.
- **[Mat00]** E. M. Matveev, *An explicit lower bound for a homogeneous rational
  linear form in the logarithms of algebraic numbers. II*, Izv. Math. 64:6 (2000)
  1217–1269.
- **[OW14]** J. Ouaknine, J. Worrell, *Positivity problems for low-order linear
  recurrence sequences*, Proc. SODA 2014, 366–379.
- **[Sch79]** A. Schönhage, *On the power of random access machines*, Proc. ICALP
  1979, LNCS 71, 520–529.
- **[Sch08]** R. Schoof, *Computing Arakelov class groups*, in: Algorithmic Number
  Theory, MSRI Publ. 44, Cambridge University Press, 2008, 447–495.
- **[Sha19]** M. Sha, *Effective results on the Skolem Problem for linear
  recurrence sequences*, J. Number Theory 197 (2019) 228–249.
- **[Sma98]** S. Smale, *Mathematical problems for the next century*, Math.
  Intelligencer 20:2 (1998) 7–15.
- **[Thi95]** C. Thiel, *Short proofs using compact representations of algebraic
  integers*, J. Complexity 11 (1995) 310–329; and PhD thesis, Universität des
  Saarlandes, 1995.
- **[vG25]** D. M. H. van Gent (lectures by H. W. Lenstra), *Polynomial-time
  algorithms in algebraic number theory*, arXiv:2502.19036. (Thm. 165 = Ge's
  theorem; Lemma 166; coprime bases.)
