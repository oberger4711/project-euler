#!/usr/bin/env python3

import utils

# https://projecteuler.net/problem=36
# Brute Force.

print(sum(d for d in range(1000000) if utils.isPalindrome(d) and utils.isPalindrome(utils.toBinary(d))))
