#!/usr/bin/env python3

import math

# https://projecteuler.net/problem=12
# Straight forward brute force.

def countDivisors(n):
    sr = int(math.sqrt(n))
    count = 2 # It is always divisable by 1 and itself.
    for d in range(2, sr + 1):
        div, rest = divmod(n, d)
        if rest == 0:
            if div == d:
                count += 1
            else:
                count += 2
    return count

N_DIVS_TARGET = 500
i = 1
n = 1
divs = 0
while divs <= N_DIVS_TARGET:
    i += 1
    n += i
    divs = countDivisors(n)
print("n = {}: {} divisors".format(n, divs))
