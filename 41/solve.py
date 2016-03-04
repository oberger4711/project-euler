#!/usr/bin/python

from math import sqrt

# https://projecteuler.net/problem=41
# Pretty slow solution.
# Simple stupid brute force.
# Much room for optimisation.
# Highest result that was calculated in a couple of minutes was correct answer ;).

digits = []
for i in range(1, 10):
    digits.append(str(i))
print "Setup digits", digits
def isPandigital(nString):
    for digitStr in digits[:len(nString)]:
        if (digitStr not in nString):
            return False
    return True

def isPrime(n):
    # Should only go up to sqrt n.
    for i in xrange(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True

relevant = xrange(2143, 987654322)
for n in relevant:
    if (isPandigital(str(n)) and isPrime(n)):
        print n

print "Done."
