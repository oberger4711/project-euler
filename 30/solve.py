#!/usr/bin/env python3

import math

# https://projecteuler.net/problem=30
# Brute force 5 digits which form the greatest number that
# may be written as the sum of fifth powers of it's digits.
# Run plot.py for vizualization.

def isSumOfPowersOfItsDigits(num, exponent=5):
    current = num
    total = 0
    for i in range(len(str(num))):
        current, dig = divmod(current, 10)
        total += math.pow(dig, exponent)
    return total == num

exp = 5
total = 0
for i in range(10, 999999):
    if isSumOfPowersOfItsDigits(i, exp):
        print("Found one: {}".format(i))
        total += i
print("Sum: {}".format(total))
