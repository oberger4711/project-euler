#!/usr/bin/python

from itertools import permutations

# https://projecteuler.net/problem=43
# Simple stupid brute force.
# Iterate over all permutations without leading zeros and check the conditions.

def arrayToInt(a):
    n = 0
    factor = 1
    for i in reversed(range(0, len(a))):
        n += a[i] * factor
        factor *= 10
    return n

digits = []
for i in range(0, 10):
    digits.append(i)

total = 0
for perm in permutations(digits):
    if (perm[0] != 0):
        if (arrayToInt(perm[1:4]) % 2 == 0) and \
            (arrayToInt(perm[2:5]) % 3 == 0) and \
            (arrayToInt(perm[3:6]) % 5 == 0) and \
            (arrayToInt(perm[4:7]) % 7 == 0) and \
            (arrayToInt(perm[5:8]) % 11 == 0) and \
            (arrayToInt(perm[6:9]) % 13 == 0) and \
            (arrayToInt(perm[7:10]) % 17 == 0):
                print perm
                total += arrayToInt(perm)

print "Sum:", total
