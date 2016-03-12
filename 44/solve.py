#!/usr/bin/python

# https://projecteuler.net/problem=44
# TODO: Description of algorithm.

latestPenIndex = 2
latestPenNum = 5
lookupTable = { 1 : True, 5 : True }

def isPenNum(i):
    global latestPenIndex
    global latestPenNum
    global lookupTable
    res = False
    if (i <= latestPenIndex):
        res = (i in lookupTable)
    else:
        while (latestPenNum < i):
            latestPenIndex += 1
            latestPenNum = calcPenNum(latestPenIndex)
            lookupTable[latestPenNum] = True
            if (latestPenNum == i):
                res = True
    return res

def calcPenNum(i):
    if (latestPenIndex < i):

    return i * (3 * i - 1) / 2

highest = 12
thresholdIndex = -1
printStep = 0
found = False
while True:
    thresholdIndex += 1
    threshold = lookupTable.keys()[thresholdIndex]
    if (threshold > printStep):
        print threshold
        printStep += 10000000
    # Increase upper limit if necessary.
    while (isPenNum(highest + threshold)):
        highest = highest + threshold
    # Find pairs with this abs difference.
    for n in lookupTable.keys():
        if (n == highest):
            break
        m = n + threshold
        if (isPenNum(m)):
            pair = (n, m)
            if (isPenNum(pair[0] + pair[1])):
                print "Pair:", pair, "Diff:", pair[1] - pair[0]
                found = True
