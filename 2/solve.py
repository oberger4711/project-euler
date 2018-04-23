#!/usr/bin/env python3

# https://projecteuler.net/problem=2
# Dynamic programming solution.

def fib(val_max):
    n_2 = 0
    n_1 = 1
    total = n_1 + n_2
    while total < val_max:
        yield total
        n_2 = n_1
        n_1 = total
        total = n_1 + n_2

print(sum(i for i in fib(4000000) if i % 2 == 0))
