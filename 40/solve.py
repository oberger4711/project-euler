#!/usr/bin/env python3

import utils
import numpy as np

# https://projecteuler.net/problem=40
# Straight forward.

def digits():
    for n in utils.naturalNumbers(1):
        s = str(n)
        for ch in s:
            yield int(ch)

ns = (1, 10, 100, 1000, 10000, 100000, 1000000)
factors = []
for i, dig in enumerate(digits(), start=1):
    if i in ns:
        factors.append(dig)
    if i >= ns[-1]:
        break

print(factors)
print(np.prod(factors))
