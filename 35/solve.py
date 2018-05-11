#!/usr/bin/env python3

import utils

# https://projecteuler.net/problem=35
# Brute force.

def circularPrime(n):
    s = str(n)
    ds = "".join([s, s])
    for start in range(len(s)):
        s_rotated = ds[start:start + len(s)]
        n_rotated = int(s_rotated)
        if not utils.isPrime(n_rotated):
            return False
    return True

count = 0
for n in range(2, 1000000):
    if circularPrime(n):
        count += 1

print(count)
