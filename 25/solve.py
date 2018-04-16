#!/usr/bin/env python3

# https://projecteuler.net/problem=25
# TODO: Description of algorithm.

def fib():
    yield 1, 1
    yield 1, 1
    i = 3
    f_prev = 1
    f_prev_prev = 1
    while True:
        f = f_prev + f_prev_prev
        yield i, f
        i += 1
        f_prev_prev = f_prev
        f_prev = f

for f in fib():
    if len(str(f[1])) >= 1000:
        print(f)
        break
