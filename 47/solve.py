#!/usr/bin/env python3

import math

# https://projecteuler.net/problem=47
# Use dynamic programming-ish sweep.

def primeFactors(n: int):
    res = []
    _primeFactors(n, res)
    return res

def _primeFactors(n: int, out_res):
    for div in range(2, int(math.sqrt(n) + 1)):
        if n % div == 0:
            qt = n // div
            _primeFactors(qt, out_res)
            _primeFactors(div, out_res)
            return
    # It is already a prime.
    out_res.append(n)


history = [set(primeFactors(2)), set(primeFactors(3)), set(primeFactors(4))]
n = 5
while True:
    pfs = set(primeFactors(n))
    if all(len(h) == 4 for h in history + [pfs]):
        print(n, history, pfs)
        break
    # Rotate on for next iteration.
    history = history[1:] + [pfs]
    n += 1
    
