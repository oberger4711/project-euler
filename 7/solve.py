#!/usr/bin/env python3

import math

# https://projecteuler.net/problem=7
# Straight forward implementation.

def isPrime(i: int):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            return False
    return True

n_primes = 0
i = 2
while n_primes < 10001:
    if isPrime(i):
        n_primes += 1
    i += 1

print(i - 1)
