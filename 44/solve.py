#!/usr/bin/python

# https://projecteuler.net/problem=44
# Iteratively expand the diff threshold and search for hits in the cached pentagon numbers.
# This is extremely slow. Takes about 12 minutes.

latestPenIndex = 2
latestPenNum = 5
lookupTable = { 1 : True, 5 : True }

def isPenNum(n):
    if n < 1:
        return False
    global latestPenIndex
    global latestPenNum
    global lookupTable
    while (latestPenNum < n):
        calcPenNum(latestPenIndex + 1)
    return (n in lookupTable)

def calcPenNum(i):
    global latestPenIndex
    global latestPenNum
    global lookupTable
    while (latestPenIndex < i):
        latestPenIndex += 1
        latestPenNum = latestPenIndex * (3 * latestPenIndex - 1) / 2
        lookupTable[latestPenNum] = True
    return i * (3 * i - 1) // 2

highest = 5
highestIndex = 2
diffIndex = -1
found = False
while not found:
    diffIndex += 1
    diff = calcPenNum(diffIndex)
    print diff
    # Increase upper limit if necessary.
    while (calcPenNum(highestIndex + 1) - calcPenNum(highestIndex) < diff):
        highestIndex += 1
        highest = calcPenNum(highestIndex)
    # Find pairs with this abs difference.
    for i in range(1, highestIndex):
        a = calcPenNum(i)
        b = a + diff
        if isPenNum(b) and isPenNum(a + b):
                print "HIT! Pair:", a, b, "Diff:", b - a
                found = True
                break
