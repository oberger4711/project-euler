#!/usr/bin/env python3

# https://projecteuler.net/problem=26
# Use long division and check if the current rest has occured already.

def findRecurringCycle(divisor):
    rest_history = {1: 0} # Resolves rest to iteration.
    divident = 1
    rest = 0
    i = 0
    while True:
        i += 1
        divident *= 10
        result = divident // divisor
        rest = divident - (result * divisor)
        if rest == 0:
            return 0
        if rest in rest_history:
            return i - rest_history[rest]
        rest_history[rest] = i
        divident = rest

longest = (0, 0)
for i in range(2, 1000):
    cycle_len = findRecurringCycle(i)
    if cycle_len > longest[1]:
        longest = (i, cycle_len)

print("Divisor: {}, length of recurring cycle: {}".format(longest[0], longest[1]))
