#!/usr/bin/python

import time
import words

# https://projecteuler.net/problem=42
# Use a lookup table to keep already calculated traingle numbers in cache.
# Word list is copied into an array in words.py.
# This way it is not necessary to parse any file.

highestLookupIndex = 0
highestLookupTriangleNumber = 1
lookupTable = { 1 : True }

def isTriangleNumber(n):
    global highestLookupIndex
    global highestLookupTriangleNumber
    global lookupTable
    res = False
    if (n <= highestLookupTriangleNumber):
        res = (n in lookupTable)
    else:
        index = highestLookupIndex + 1
        value = calcTriangleNumber(index)
        while True:
            lookupTable[value] = True
            if (value == n):
                res = True
                break
            elif (value < n):
                index += 1
                value = calcTriangleNumber(index)
            else:
                break
        highestLookupIndex = index
        highestLookupTriangleNumber = value
    return res

def calcTriangleNumber(n):
    return (n * (n + 1)) / 2

def calcWordCrossSum(word):
    total = 0
    for char in word:
        total += ord(char) - ord('@')
    return total

count = 0
for word in words.words:
    value = calcWordCrossSum(word)
    if (isTriangleNumber(value)):
        count += 1

print count
