#!/usr/bin/python

# https://projecteuler.net/problem=24
# Swap most right item with most right smaller item and sort the range on the right of it.
# In some way similar to bubblesort.

import math

#digits = [0, 1, 2]
digits = [0, 1, 2, 3]
#digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def nextLexicalPerm(a):
    for r in reversed(range(0, len(a))):
        swapped = False
        for l in reversed(range(0, r)):
            if a[l] < a[r]:
                a[l], a[r] = a[r], a[l]
                a[l + 1:] = sorted(a[l + 1:])
                swapped = True
                break
        if swapped:
            break

print digits
for i in range(0, math.factorial(len(digits)) - 1):
    nextLexicalPerm(digits)
    print digits

