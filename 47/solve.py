#!/usr/bin/env python3

import math
from utils import primeFactors

# https://projecteuler.net/problem=47
# Use dynamic programming-ish sweep.

history = [set(primeFactors(2)), set(primeFactors(3)), set(primeFactors(4))]
n = 5
while True:
    pfs = set(primeFactors(n))
    if all(len(h) == 4 for h in history + [pfs]):
        print(n, history, pfs)
        print(n - 3)
        break
    # Rotate on for next iteration.
    history = history[1:] + [pfs]
    n += 1
    
