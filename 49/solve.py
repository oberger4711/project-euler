#!/usr/bin/env python3

import utils

# https://projecteuler.net/problem=49
# Brute Force.

for i_0 in range(1000, 10000):
    if utils.isPrime(i_0):
        for inc in range(1, (10000 - i_0) // 2):
            i_1 = i_0 + inc
            i_2 = i_1 + inc
            if utils.arePermutationsShort(i_0, i_1) and utils.arePermutationsShort(i_1, i_2):
                if utils.isPrime(i_1) and utils.isPrime(i_2):
                    print("{}, {}, {} (concatenated: {})".format(i_0, i_1, i_2, "".join((str(i_0), str(i_1), str(i_2)))))
