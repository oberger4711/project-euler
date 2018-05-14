#!/usr/bin/env python3

import utils

# https://projecteuler.net/problem=52
# Brute Force. Jump forward if length would differ to speed it up a bit.

n = 10
found = False
while not found:
    l = len(str(n))
    if len(str(n*6)) > l:
        n = n*6 - 2
        print("Jumping to {}".format(n))
    elif utils.arePermutationsShort(n, 2*n) and \
            utils.arePermutationsShort(n, 3*n) and \
            utils.arePermutationsShort(n, 4*n) and \
            utils.arePermutationsShort(n, 5*n) and \
            utils.arePermutationsShort(n, 6*n):
            print(n)
            found = True
    else:
        n += 1
