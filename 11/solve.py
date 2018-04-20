#!/usr/bin/env python3

import numpy as np
from data import grid

# https://projecteuler.net/problem=11
# Search each row, col and diagonal line for the highest adjacent numbers.

# Rows
prod_highest = 0
for row in range(grid.shape[0]):
