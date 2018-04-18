#!/usr/bin/env python3

from data import numbers

# https://projecteuler.net/problem=13
# Treat number as string.

total = sum(num for num in numbers)
print(str(total)[:10])
