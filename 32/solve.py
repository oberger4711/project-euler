#!/usr/bin/env python3

import math

# https://projecteuler.net/problem=32
# TODO: Description of algorithm.

def isInvalid(n):
    seen = {}
    while n != 0:
        n, dig = divmod(n, 10)
        if dig == 0:
            return False
        if dig in seen:
            return False
        else:
            seen[dig] = True
    return False

def isPandigital(i, j, k):
    seen = {}
    for n in (i, j, k):
        while n != 0:
            n, dig = divmod(n, 10)
            if dig == 0:
                return False
            if dig in seen:
                return False
            else:
                seen[dig] = True
    return len(seen) == 9

print(isPandigital(39, 186, 39 * 186))

seen_products = {}
total = 0
i_max = 98
for i in range(98):
    if not isInvalid(i):
        for j in range(123, 9876):
            prod = i * j
            if prod not in seen_products:
                if isPandigital(i, j, prod):
                    total += prod
                    seen_products[prod] = True
                    print("{} * {} = {}".format(i, j, prod))

print("Sum of products: {}".format(total))
