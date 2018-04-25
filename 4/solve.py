#!/usr/bin/env python3

# https://projecteuler.net/problem=4
# Straight forward brute force.

def isPalindrome(n):
    s = str(n)
    return s == s[::-1]

largest_palindrome = -1
lower_bound = 99
a = 999
while a > lower_bound:
    b = 999
    while b > lower_bound:
        prod = a * b
        if isPalindrome(prod):
            lower_bound = min(a, b)
            largest_palindrome = max(largest_palindrome, prod)
            print("{} = {} * {}".format(prod, a, b))
        b -= 1
    a -= 1

print("Largest palindrome: {}".format(largest_palindrome))
