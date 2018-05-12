#!/usr/bin/env python3

import utils

# https://projecteuler.net/problem=45
# Iterate through hexagonal and pull up the other sequences for checking.

def hexagonal(n_start):
    for n in utils.naturalNumbers(n_start):
        yield n, int(n * (2 * n - 1))

def pentagonal(n_start):
    for n in utils.naturalNumbers(n_start):
        yield n, int(n * (3 * n - 1) / 2)

def triangle(n_start):
    for n in utils.naturalNumbers(n_start):
        yield n, int(n * (n + 1) / 2)

n_h = 144
n_p = 165
n_t = 285
for i in utils.naturalNumbers(144):
    for n_h_cur, h in hexagonal(n_h):
        n_h = n_h_cur
        for n_p_cur, p in pentagonal(n_p):
            n_p = n_p_cur
            if p > h:
                break
            if p == h:
                for n_t_cur, t in triangle(n_t):
                    n_t = n_t_cur
                    if t > p:
                        break
                    if t == p:
                        print(t)
                        exit(0)
