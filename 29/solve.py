#!/usr/bin/env python3

import math

# https://projecteuler.net/problem=29
# Use a hash set and brute force.

memory = {}
for a in range(2, 101):
    for b in range(2, 101):
        memory[math.pow(a, b)] = True

print(len(memory))
