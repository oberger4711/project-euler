#!/usr/bin/python

# https://projecteuler.net/problem=31
# Start with the smallest coin and add each one multiple times.
# Track how much possibilities are known yet for each value.
# After each check also add the combination with known value pathes.
# Check the image for a handwritten example.

wanted = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
cache = {}

# Initialize cache.
for i in range(1, wanted + 1):
    cache[i] = 0

for coin in coins:
    # Old cache must not be changed until the new one is completely updated.
    newCache = cache.copy()
    for nums in range(1, (wanted / coin) + 1):
        value = nums * coin
        newCache[value] += 1
        for knownValue, knownPathes in cache.items():
            valueSum = knownValue + value
            if (valueSum <= wanted):
                newCache[valueSum] += knownPathes
            else:
                break
    cache = newCache

print cache[wanted]
