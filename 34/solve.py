#!/usr/bin/python

# https://projecteuler.net/problem=34
# Cache the factorials of each digit in a lookup table for more performance.
# Calculate the limit the following way:
# It is given by the highest number containing only 9s but having a cross factorial lower than itself.
# Any number higher than this limit is garanteed to not have a cross factorial equal to itself.
# The rest is brute force.

from math import factorial

print "Filling the lookup table..."
cache = {}
for i in range(0, 10):
    cache[i] = factorial(i)

def crossFactorial(num):
    res = 0
    while (num > 0):
        res += cache[num % 10]
        num = num / 10
    return res

print "Searching limit..."
limit = 9
while (crossFactorial(limit) > limit):
    limit *= 10
    limit += 9
print "Found limit at", limit

print "Brute forcing curious numbers..."
curiousSum = 0
for i in range(10, limit):
    if (crossFactorial(i) == i):
        curiousSum += i
        print i
print "Sum is", curiousSum
