#!/usr/bin/env python3

from data import names
import string

# https://projecteuler.net/problem=22
# Straightforward calculate all scores and add them.

names.sort()
alphabet = string.ascii_uppercase
# Prepare O(1) lookup table.
letter_scores = {}
for i, letter in zip(range(1, len(alphabet) + 1), alphabet):
    letter_scores[letter] = i
total = 0
for score_order, name in zip(range(1, len(names) + 1), names):
    score_chars = sum(letter_scores[l] for l in name)
    total += score_order * score_chars

print(total)
