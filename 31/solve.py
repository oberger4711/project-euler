#!/usr/bin/python

# https://projecteuler.net/problem=31
# Simple depth first search.

coins = [1, 2, 5, 10, 20, 50, 100, 200]
cache = {}

def search(wanted, path = [], maxCoin = min(coins)):
    res = 0
    diff = wanted - sum(path)
    if (diff == 0):
        res = 1
    elif (diff > 0):
        if (diff in cache):
            res = cache[diff]
        else:
            if (coin <= maxCoins):
                extendedPath = path[:]
                extendedPath.append(coin)
                res += search(wanted, extendedPath, coin)
    return res

print search(5)
