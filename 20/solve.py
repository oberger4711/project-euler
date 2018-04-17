#!/usr/bin/env python3

import math

# https://projecteuler.net/problem=20
# Use divmode in a loop.

num = math.factorial(100)
total = 0
while (num != 0):
    num, dig = divmod(num, 10)
    total += dig
print(total)
