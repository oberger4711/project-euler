#!/usr/bin/python

# https://projecteuler.net/problem=24
# Swap first item from the right with first smaller item from the right and sort the range on the right.
# In some way similar to bubblesort.

import math

#digits = [0, 1, 2]
#digits = [0, 1, 2, 3]
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def nextLexicalPerm(a):
    for l in reversed(range(0, len(a))):
        swapped = False
        for r in reversed(range(l, len(a))):
            if a[l] < a[r]:
                a[l], a[r] = a[r], a[l]
                a[l + 1:] = sorted(a[l + 1:])
                swapped = True
                break
        if swapped:
            break

#LIMIT = math.factorial(len(digits)) - 1
LIMIT = 1000000 - 1
print digits
for i in range(0, LIMIT):
    nextLexicalPerm(digits)
    #print digits

print digits

