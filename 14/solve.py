#!/usr/bin/env python3

# https://projecteuler.net/problem=14
# Brute force solution. Could be optimized but is fast enough.

def lenSequence(num : int):
    n = num
    length = 1
    while n > 1:
        if n % 2 == 0:
            # Even
            n = n // 2
        else:
            # Odd
            n = 3 * n + 1
        length += 1
    return length

n_start_longest = 1
length_longest = 0
for n in range(1000000):
    length = lenSequence(n)
    if length > length_longest:
        n_start_longest = n
        length_longest = length
print("Starting number: {}, Length: {}".format(n_start_longest, length_longest))
