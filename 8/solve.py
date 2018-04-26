#!/usr/bin/env python3

from utils import reverseDigitsOf
import numpy as np
from data import number

# https://projecteuler.net/problem=8
# Sweep algorithm.

digits = [d for d in reverseDigitsOf(number)]
print(max(np.prod(digits[i:i+13]) for i in range(len(digits) - 13)))
