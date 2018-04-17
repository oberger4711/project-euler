#!/usr/bin/env python3

import math

# https://projecteuler.net/problem=27
# Brute force algorithm.

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

best = (0, 0, 0) # number of primes, a, b
for a in range(-999, 1000):
    for b in range(1001): # Must be positive because result must be positive for n = 0.
        n = 0
        while isPrime(n * n + a * n + b):
            n += 1
        if n > best[0]:
            best = n, a, b
            print("new best: a: {}, b: {}, a*b: {}, #primes: {}".format(a, b, (a * b), n))
