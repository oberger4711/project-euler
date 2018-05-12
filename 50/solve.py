#!/usr/bin/env python3

import utils
import numpy as np

# https://projecteuler.net/problem=50
# This uses an integral image approach and binary search.

TOTAL_UPPER_BOUND = 1000

# Precompute summed-area table.
primes = np.array([n for n in range((TOTAL_UPPER_BOUND // 2) + 1) if utils.isPrime(n)])
cumsum = np.cumsum(primes)

def primeSum(cumsum, i_start, i_end):
    end = cumsum[i_end]
    if i_start == 0:
        start = 0
    else:
        start = cumsum[i_start - 1]
    return end - start

def binSearchEndEnd(cumsum, i_start: int, longest_len: int):
    # Binary Search for i_end_end.
    i_end_end = i_start
    skip = False
    i_lower_bound = min(i_start + longest_len, cumsum.shape[0] - 1)
    if primeSum(cumsum, i_start, i_lower_bound) > TOTAL_UPPER_BOUND:
        return True, i_lower_bound
    i_upper_bound = cumsum.shape[0] - 1
    while i_lower_bound != i_upper_bound:
        if (i_lower_bound - i_start) + 1 < longest_len:
            # Makes no sense to keep searching.
            skip = True
            break
        i_mid = (i_lower_bound + i_upper_bound) // 2
        total = primeSum(cumsum, i_start, i_mid)
        # Shrink bounds.
        if total <= TOTAL_UPPER_BOUND:
            i_lower_bound = i_mid + 1
        else:
            i_upper_bound = i_mid
    i_end_end = i_lower_bound
    return skip, i_end_end

def bruteForceEndEnd(cumsum, i_start, longest_len):
    i_end_end = cumsum.shape[0] - 1
    if primeSum(cumsum, i_start, min(i_start + longest_len, cumsum.shape[0] - 1)) > TOTAL_UPPER_BOUND:
        return True, i_end_end
    return False, i_end_end

longest_len = 0
for i_start in range(cumsum.shape[0]):
    # This is the number at which to stop for prime sums later.
    # Both implementations are just as fast.
    #skip, i_end_end = binSearchEndEnd(cumsum, i_start, longest_len)
    skip, i_end_end = bruteForceEndEnd(cumsum, i_start, longest_len)
    if not skip:
        # Search backwards for primes with brute force.
        i_end_start = min(i_end_end, i_start + longest_len + 1)
        for i_end in range(i_end_start, i_end_end, 1):
            total = primeSum(cumsum, i_start, i_end)
            if total < TOTAL_UPPER_BOUND:
                if utils.isPrime(total):
                    longest_len = (i_end - i_start) + 1
                    print("[{}, {}] -> sum: {}, length: {}".format(i_start, i_end, total, longest_len))
