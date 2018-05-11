#!/usr/bin/env python3

import math

# https://projecteuler.net/problem=9
# Brute Force.

for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c_2 = a ** 2 + b ** 2
        c = int(math.sqrt(c_2))
        if c ** 2 == c_2 and a + b + c == 1000:
            print("{} + {} = {}".format(a, b, c))
            print(a * b * c)

