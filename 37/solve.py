#!/usr/bin/env python3

import utils

# https://projecteuler.net/problem=37
# Brute Force. Check from outside to inside because smaller numbers are cheaper to check.

hits = []
for n in utils.naturalNumbers(start=11, step=2):
    s = str(n)
    okay = True
    for i in range(1, len(s)):
        n_left, n_right = int(s[:i]), int(s[-i:])
        if not utils.isPrime(n_left) or not utils.isPrime(n_right):
            okay = False
            break
    if okay and utils.isPrime(n):
        hits.append(n)
        print(n)
        if len(hits) == 11:
            break
print("Sum: {}".format(sum(hits)))
