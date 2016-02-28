#!/usr/bin/python

# https://projecteuler.net/problem=28

# Increase the step with every layer.
# Add it to a counter and the counter to a sum.

N = 1001

diagonal_sum = 1
current = 1
step = 0
for n in range(1, (N / 2) + 1):
    step = step + 2
    for i in range(1, 5):
        current += step
        diagonal_sum += current

print diagonal_sum
