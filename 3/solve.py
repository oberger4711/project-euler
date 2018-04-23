#!/usr/bin/env python3

import math

# https://projecteuler.net/problem=3
# Start with the lowest possible divisor which should correspond to the highest possible divident.

def isPrime(i: int):
    for d in range(2, int(math.sqrt(i)) + 1):
        if i % d == 0:
            return False
    return True

N = 600851475143
print(next(N // i for i in range(2, N // 2) if N % i == 0 and isPrime(N // i)))
