#!/usr/bin/env python3

import math

# https://projecteuler.net/problem=39
# This is similar to problem 9.

hit_counts = {}
for a in range(1, 1000):
    for b in range(a, (1000 - a) + 1):
        c_2 = a ** 2 + b ** 2
        c = int(math.sqrt(c_2))
        if c ** 2 == c_2:
            perimeter = a + b + c
            if perimeter <= 1000:
                if perimeter in hit_counts:
                    hit_counts[perimeter] += 1
                else:
                    hit_counts[perimeter] = 0

best_perimeter = -1
best_count = 0
for perimeter, count in hit_counts.items():
    if count > best_count:
        best_count = count
        best_perimeter = perimeter
        print("p = {} has {} solutions".format(perimeter, count))
