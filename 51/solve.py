#!/usr/bin/env python3

# https://projecteuler.net/problem=51
# TODO: Description of algorithm.
# Brute Force with a dictionary to avoid double checks on the same number.

import utils

TARGET_FAMILY_SIZE = 8
START = 2067997

CACHE_NUMBER_LEN = 2
CACHE_SET = {} # E. g. {"1**7" : True}

def __wildcards(s_n, digit_offset: int, digit_to_skip: int):
    if len(s_n) > 0:
        for rec in __wildcards(s_n[:-1], digit_offset + 1, digit_to_skip):
            if digit_offset != digit_to_skip:
                yield rec + [digit_offset]
            yield rec
    else:
        yield []

def wildcards(s_n, highest_digit_change: int=0):
    yield from __wildcards(s_n, 0, highest_digit_change)

def checkWildcard(s_n, wc, print_res=False):
    global CACHE_SET
    if (len(s_n) - 1 in wc) or (len(wc) == 0):
        # Skip leading zeros.
        return False
    count = 0
    s_n_wc = toWildcardString(s_n, wc)
    if s_n_wc in CACHE_SET:
        return False
    for i in range(10):
        a_n = list(s_n)
        for j in wc:
            a_n[-j - 1] = str(i)
        m = int("".join(a_n))
        if utils.isPrime(m):
            if print_res:
                print("  Prime {}: {}".format(i, m))
            count += 1
    if count >= TARGET_FAMILY_SIZE:
        return True
    CACHE_SET[s_n_wc] = True
    return False

def toWildcardString(s_n, wc):
    a_n_wc = list(str(s_n))
    for i in range(10):
        for i in wc:
            a_n_wc[-i - 1] = "*"
    return "".join(a_n_wc)

s_n_1 = "0"
for n in utils.naturalNumbers(start=START, step=2):
    s_n = str(n)
    a_n = list(s_n)
    if (n - START) % 1000 == 0:
        print(n)
    if len(s_n) > len(s_n_1):
        # Cache is of no use anymore for this number length.
        # Build a new one.
        CACHE_SET = {}
        highest_digit_change = len(s_n)
    else:
        highest_digit_change = len(s_n) - 1 - next(i for i in range(len(s_n)) if s_n[i] != s_n_1[i])
    for wc in wildcards(s_n, highest_digit_change):
        if checkWildcard(s_n, wc):
            print("Hit! {}:".format(toWildcardString(s_n, wc)))
            checkWildcard(s_n, wc, True)
            exit(0)
    s_n_1 = s_n
