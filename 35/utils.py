#!/usr/bin/env python3

import math

def reverseDigitsOf(n: int):
    """ Returns the digits of the given number in reverse order.
    :param n: an integer number
    """
    while n != 0:
        n, d = divmod(n, 10)
        yield d

def isPrime(i: int):
    """ Returns true if the given number is a prime, false if not.
    :param n: an integer number
    """
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            return False
    return True
