#!/usr/bin/env python3

# https://projecteuler.net/problem=1
# Straight forward brute force.

print(sum(n for n in range(1000) if n % 3 == 0 or n % 5 == 0))

