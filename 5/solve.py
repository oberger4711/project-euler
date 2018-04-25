#!/usr/bin/env python3

# https://projecteuler.net/problem=5
# Brute force over multiples of the largest divident.

def isDivisibleBy1To20(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True

def countTwenties():
    i = 20
    while True:
        yield i
        i += 20

print(next(n for n in countTwenties() if isDivisibleBy1To20(n)))
