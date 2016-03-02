#!/usr/bin/python

# https://projecteuler.net/problem=31
# Simple depth first search.

finalWanted = 5
coins = [1, 2, 5, 10, 20, 50, 100, 200]
cache = {}

def search(wanted, path = [], minCoin = 0):
    res = 0
    diff = wanted - sum(path)
    if (diff == 0):
        res = 1
    elif (diff > 0):
        if (diff in cache):
            res = cache[diff]
        else:
            for coin in coins:
                if (coin >= minCoin):
                    extendedPath = path[:]
                    extendedPath.append(coin)
                    res += search(wanted, extendedPath, coin)
    return res

print "Caching number of pathes..."
for wanted in range(1, finalWanted - 1):
    numOfPathes = search(wanted)
    cache[wanted] = numOfPathes
    print wanted, ":", numOfPathes

print "Calculating pathes for final wanted number", finalWanted, "..."
print search(finalWanted)
