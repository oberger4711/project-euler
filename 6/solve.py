#!/usr/bin/env python3

# https://projecteuler.net/problem=6
# Straight forward solution.

n = 100
sum_of_squares = sum(i ** 2 for i in range(1, n + 1))
square_of_sum = sum(range(1, n + 1)) ** 2

print(square_of_sum - sum_of_squares)
