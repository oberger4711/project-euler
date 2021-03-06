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
    if i < 2:
        return False
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

def naturalNumbers(start=0, step=1):
    """ This is an endless range().
    :param start: number to start with
    :param step: step to add after each iteration.
    """
    i = start
    while True:
        yield i
        i += step

def primeFactors(n: int):
    """ Finds the prime factors of the given number.
    :param n: an integer number
    :return list of prime factors.
    """
    res = []
    _primeFactors(n, res)
    return res

def _primeFactors(n: int, out_res):
    for div in range(2, int(math.sqrt(n) + 1)):
        if n % div == 0:
            qt = n // div
            _primeFactors(qt, out_res)
            _primeFactors(div, out_res)
            return
    # It is already a prime.
    out_res.append(n)
