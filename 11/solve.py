#!/usr/bin/env python3

import numpy as np
from data import grid

# https://projecteuler.net/problem=11
# Search each row, col and diagonal line for the highest adjacent numbers.

class ChainChecker:
    def __init__(self):
        self.prod_highest = 0
        self.chain_highest = []

    def checkChain(self, chain):
        prod = np.prod(chain)
        if prod > self.prod_highest:
            self.prod_highest = prod
            self.chain_highest = chain

# Rows
checker = ChainChecker()
for row in range(grid.shape[0]):
    for col in range(grid.shape[1] - 4):
        checker.checkChain(grid[row, col:col+4])
# Cols
for col in range(grid.shape[0]):
    for row in range(grid.shape[1] - 4):
        checker.checkChain(grid[row:row+4, col])
# Diagonal
for grid_ in [grid, np.flip(np.copy(grid), axis=1)]:
    min_offset = -(grid_.shape[0] - 1)
    max_offset = grid_.shape[1]
    for offset in range(min_offset, max_offset):
        diag = np.diagonal(grid_, offset=offset)
        for i in range(diag.shape[0] - 3):
            checker.checkChain(diag[i:i+4])
print("Highest Product: {}, Chain: {}".format(checker.prod_highest, checker.chain_highest))
