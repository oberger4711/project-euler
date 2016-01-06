#!/usr/bin/python

# https://projecteuler.net/problem=18
# Simple stupid recursive backtracking algorithm.
# Could maybe be inproved by checking only pathes that can possibly be better than the best that has been found yet.

import sys

# Parse file.
with open("pyramid.txt") as inFile:
    PYRAMID = [ line.replace('\n', '').split(' ') for line in inFile ]

def find(x, y):
    bestSubpath = int(PYRAMID[y][x])
    if y < len(PYRAMID) - 1:
        subPath0 = find(x, y + 1)
        subPath1 = find(x + 1, y + 1)
        bestSubpath += max(subPath0, subPath1)
    return bestSubpath

print find(0, 0)
