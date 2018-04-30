#!/usr/bin/env python3

import utils

# https://projecteuler.net/problem=10
# Straight forward solution.

print(sum(i for i in range(2, 2000000) if utils.isPrime(i)))
