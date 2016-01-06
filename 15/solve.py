#!/usr/bin/python

# https://projecteuler.net/problem=15
# This is a simple recursive backtracking algorithm with a cache to prevent multiple calculations.
# Grid origin is top left.

class PathFinder:
    def __init__(self, dimension):
        self.dim = dimension
        self.cache = {}

    def find(self, x, y):
        foundPathes = 0
        # Stop condition
        if (x, y) == (self.dim, self.dim):
            foundPathes = 1
        else:
            if self.cache.has_key( (x, y) ):
                foundPathes = self.cache[ (x, y) ]
            else:
                if x < self.dim:
                    foundPathes += self.find(x + 1, y)
                if y < self.dim:
                    foundPathes += self.find(x, y + 1)
                self.cache[ (x, y) ] = foundPathes
        return foundPathes

DIMENSION = 20
finder = PathFinder(DIMENSION)
print "Counting pathes with dimension =", DIMENSION, "..."
foundPathes = finder.find(0, 0)
print "Found", foundPathes, "pathes."
