#!/usr/bin/python

# https://projecteuler.net/problem=33
# Quick and dirty brute force hack.
# Used a calculator to get the product of the fractions.

cache = []

def isCuriousNonTrivialFraction(num, den):
    if (num == den) or ( (num, den) in cache):
        return False
    numDigits = [num / 10, num % 10]
    denDigits = [den / 10, den % 10]
    for numDigitIndex in range(0, 2):
        numDigit = numDigits[numDigitIndex]
        denDigitIndex = 1 - numDigitIndex
        denDigit = denDigits[denDigitIndex]
        if (numDigit == denDigit):
            newNum = numDigits[1 - numDigitIndex]
            newDen = denDigits[1 - denDigitIndex]
            if (newDen != 0) and (newNum / float(newDen) == num / float(den)):
                cache.append( (num, den) )
                cache.append( (den, num) )
                return True
    return False

for num in range(10, 100):
    for den in range(10, 100):
        if (isCuriousNonTrivialFraction(num, den)):
            print num, den
