#!/usr/bin/python

from time import sleep

# https://projecteuler.net/problem=38
# Chose 9876 as a limit.
# There might be a better one but it is still fast enough.
# The rest is brute force.

limit = 9876
print "Limit is", limit

digits = []
for i in range(1, 10):
    digits.append(str(i))
print "Setup digits", digits

def isPandigital(nString):
    if (len(nString) != 9):
        return False
    for digitStr in digits:
        if (digitStr not in nString):
            return False
    return True

maxConcatenated = 0
for src in range(2, limit):
    nString = str(src)
    factor = 2
    while (len(nString) < 9):
        nString += str(src * factor)
        factor += 1
    if (len(nString) == 9) and (isPandigital(nString)):
        n = int(nString)
        maxConcatenated = max(maxConcatenated, n)
        print src, "->", maxConcatenated

