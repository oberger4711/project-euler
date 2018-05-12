#!/usr/bin/env python3

import utils

# https://projecteuler.net/problem=49
# Brute Force.

primes = {}
for i in range(1000, 10000):
    if utils.isPrime(i):
        primes[i] = True

def arePermutations(a, b):
    str_a = str(a)
    str_b = str(b)
    return sorted(str_a) == sorted(str_b)

for i_0 in range(1000, 10000):
    if i_0 in primes:
        for inc in range(1, (10000 - i_0) // 2):
            i_1 = i_0 + inc
            i_2 = i_1 + inc
            if arePermutations(i_0, i_1) and arePermutations(i_1, i_2):
                if i_1 in primes and i_2 in primes:
                    print("{}, {}, {} (concatenated: {})".format(i_0, i_1, i_2, "".join((str(i_0), str(i_1), str(i_2)))))
