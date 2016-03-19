#!/usr/bin/python

# https://projecteuler.net/problem=44
# TODO: Description of algorithm.

latestPenIndex = 2
latestPenNum = 5
lookupTable = { 1 : True, 5 : True }

def isPenNum(n):
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

    return i * (3 * i - 1) / 2

highest = 5
highestIndex = 2
threshold = 0
thresholdIndex = -1
printStep = 0
found = False
while True:
    thresholdIndex += 1
    threshold = calcPenNum(thresholdIndex)
    print threshold
    # Increase upper limit if necessary.
    while (calcPenNum(highestIndex + 1) - calcPenNum(highestIndex) <= threshold):
        highestIndex += 1
        highest = calcPenNum(highestIndex)
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
