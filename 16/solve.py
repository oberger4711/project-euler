#!/usr/bin/env python3

import math

# https://projecteuler.net/problem=16
# Use modulo to get digits.

num = 2 ** 1000

total = 0
while num != 0:
    num, dig = divmod(num, 10)
    total += dig
print(total)
