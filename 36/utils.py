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
    """ Returns True if the given number is a prime, False if not.
    :param n: an integer number
    """
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            return False
    return True

def toBinary(i: int):
    """ Transforms the given number to binary formatted as string.
    :param i: an integer number
    """
    return "{0:b}".format(i)

def isPalindrome(v):
    """ Returns True if str(v) is a palindrome, False if not.
    :param v: object to be checked
    """
    s = str(v)
    return s == s[::-1]
