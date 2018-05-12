#!/usr/bin/env python3

import utils

# https://projecteuler.net/problem=46
# Update a list of double squares and check if the leftover is prime.

double_squares = [0]
for n in utils.naturalNumbers(3, 2):
    if utils.isPrime(n):
        continue
    # Expand double squares if necessary.
    okay = False
    while double_squares[-1] < n:
        double_squares.append(2 * len(double_squares) ** 2)
    for ds in double_squares[::-1]:
        first_summand = n - ds
        if utils.isPrime(first_summand):
            okay = True
            break
    if not okay:
        print(n)
        break
