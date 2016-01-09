#!/usr/bin/python

# https://projecteuler.net/problem=23
# Not proud of this one, but it does it's job :D.

import math

MAX = 28123

def isAbundant(n):
    divSum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divSum += i
            d = n / i
            if i != d:
                divSum += d
    return divSum > n

print "Finding abundant numbers..."
aNums = []
for i in range(1, MAX):
    if isAbundant(i):
        aNums.append(i)

print "Filling sums set..."
sums = {}
for i in range(1, MAX):
    sums[i] = True

print "Calculating sums of abundant numbers..."
for a in aNums:
    for b in aNums:
        s = a + b
        if sums.has_key(s):
            del sums[s]

print "Summing up sums..."
sumsum = 0
for i in sums.keys():
    sumsum += i

print sumsum

