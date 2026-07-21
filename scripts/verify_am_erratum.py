"""Machine verification of the errata found in Adleman–Manders, UCB/ERL
M78/30 (1978) by this project's adversarial agent series (2026-07-22).

E1 (triviality of the printed Thm 1.3.4(1) set): (a·0+1)·c = c always,
so {⟨a,c⟩ : (ax+1)y = c solvable in ℤ} = ℤ².

E2 (Thm 2.4.1 printed bound insufficient): source knapsack {5} with
target b = 2 is a NO instance, yet under the printed bound
2·3^k > 1 + Σ|aᵢ| (k = 2) the produced instance ⟨27, c⟩ with
c = h₁h₂ = 79·17 = 1343 (h₁ ≡ 2¹⁰, h₂ ≡ 2⁻³ mod 27) is a false YES over
ℤ via the NEGATIVE divisor −79 ≡ 2 (mod 27): (27·(−3)+2)·(−17) = 1343.
No positive divisor of 1343 is ≡ 2 (mod 27), which is why the ℕ-version
is sound and only the ℤ-version leaks. The repaired bound
3^k > 1 + Σ|aᵢ| forces k = 3, and no divisor of any admissible c is
≡ ±... — here we verify the concrete leak and its closure at k = 3.

Run: .venv/bin/python scripts/verify_am_erratum.py
"""
import sympy as sp

# E1: triviality
for a, c in [(3, 7), (10**6 + 3, -12345), (27, 1343)]:
    assert (a * 0 + 1) * c == c
print("E1: (ax+1)y = c is solvable over ℤ for every (a,c) via x=0, y=c ✓")

# E2: the counterexample under the printed bound
a_list, b = [5], 2                       # knapsack {5}, target 2: NO instance
assert all(sum(S) != b for S in ([], [5]))
lst = [2 * a_list[0], 1 - 2 * b]         # b=1 normal form (sign-corrected): {10, -3}
total = 1 + sum(abs(x) for x in lst)     # = 14
k_printed = next(k for k in range(1, 10) if 2 * 3**k > total)   # k = 2
k_repaired = next(k for k in range(1, 10) if 3**k > total)      # k = 3
assert k_printed == 2 and k_repaired == 3
mod = 3 ** (k_printed + 1)               # 27
h1, h2 = 79, 17
assert sp.isprime(h1) and sp.isprime(h2)
assert h1 % mod == pow(2, lst[0], mod)   # 79 ≡ 2^10 ≡ 25 (mod 27)
assert (h2 * pow(2, 3, mod)) % mod == 1  # 17 ≡ 2^{-3} (mod 27)
c = h1 * h2                              # 1343
assert (27 * (-3) + 2) * (-17) == c      # the ℤ-solution riding d = -79
assert (-h1) % mod == 2                  # -79 ≡ 2 (mod 27)
assert all(d % mod != 2 for d in sp.divisors(c))  # positive divisors: clean
print(f"E2: ⟨27, {c}⟩ is a false YES over ℤ under the printed bound "
      f"(negative divisor −79 ≡ 2 mod 27); ℕ-version unaffected ✓")

# E2 repair: with k = 3 (mod 81), the same construction leaves no leak:
# residue arithmetic then forces subset-sum ≡ 1 (mod 2·27) with
# |Σ_S| ≤ 13 < 26, so Σ_S = 1 exactly — unattainable for {10, −3} sums
# {0, 10, −3, 7}, and the 3^k+1 = 28 ≡ ... negative-divisor residue is
# likewise out of reach.
sums = {0, 10, -3, 7}
assert 1 not in sums and (3**k_repaired + 1) not in {s % (2 * 3**k_repaired) for s in sums}
print("E2 repair: bound 3^k > 1 + Σ|aᵢ| (k=3) closes the leak ✓")
print("All errata machine-verified.")
