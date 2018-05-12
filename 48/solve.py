#!/usr/bin/env python3

# https://projecteuler.net/problem=48
# One line in python.

print(str(sum(i ** i for i in range(1, 1001)))[-10:])
