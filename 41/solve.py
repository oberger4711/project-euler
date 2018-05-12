#!/usr/bin/env python3

from math import sqrt
import utils
import itertools

# https://projecteuler.net/problem=41
# Try out all permutations starting with the longest number.

digits = []
for i in range(1, 10):
    digits.append(str(i))

for length in range(9, 3, -1):
    largest_or_neg_one = -1
    sub_digits = digits[:length]
    for permutation in itertools.permutations(sub_digits):
        num = int("".join(permutation))
        if utils.isPrime(num):
            largest_or_neg_one = max(largest_or_neg_one, num)
    if largest_or_neg_one != -1:
        break

print("Largest: {}".format(largest_or_neg_one))
