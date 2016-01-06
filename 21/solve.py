#!/usr/bin/python

# https://projecteuler.net/problem=21
# Calculate all d(1 .. 10000) and find pairs afterwards.

import math

def d(n):
    sum = 1 # All numbers are dividable by 1.
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum += i
            if n / i != i:
                sum += n / i
    return sum

TOP = 10000
amicableSum = 0
processed = {}
for i in range(1, TOP):
    di = d(i)
    if (di != i) and (not processed.has_key(di)):
        ddi = d(di)
        if ddi == i:
            amicableSum += i
            if di < TOP:
                amicableSum += di
    processed[i] = True

print amicableSum
