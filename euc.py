"""Script to explore numerically the conjecture that the Euclidean algorithm is
optimal for gcd computation among all algorithms which call the remainder
function as its only primitive.

"""

import math

max_input = 15000
inputs_and_cx = []


def find_least_m(a, b, gcd):
    """Returns the least m such that gcd(a, b) belongs to the mth generated
subalgebra.

    """

    G = []
    G.append({0, 1, a, b})

    for m in range(max_input):
        if gcd in G[m]:
            return m
        else:
            G.append(G[m] | {x % y for x in G[m] for y in G[m] if y != 0})


def find_least_of_cx_n(n):
    """Returns the lexicographically least (a, b, n) in inputs_and_cx."""
    for (a, b, m) in inputs_and_cx:
        if m == n: return (a,b,m)


def find_max_cx():
    """Returns the largest complexity m such that for some inputs a, b < max_input,
(a, b, m) belongs to inputs_and_cx.

    """
    max_cx = 0
    for (_, _, m) in inputs_and_cx:
        if m > max_cx:
            max_cx = m
    print("max_cx =", max_cx)
    return max_cx


for a in range(max_input):
    for b in range(a):
        gcd = math.gcd(a, b)
        m = find_least_m(a, b, gcd)
        inputs_and_cx.append((a, b, m))

for n in range(1 + find_max_cx()):
    print(find_least_of_cx_n(n))
