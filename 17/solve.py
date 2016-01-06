#!/usr/python

# https://projecteuler.net/problem=17
# This uses div and modulo to split the number to be written and write it section for section.

writing = {
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        15 : "fifteen",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen",
        20 : "twenty",
        30 : "thirty",
        40 : "forty",
        50 : "fifty",
        60 : "sixty",
        70 : "seventy",
        80 : "eighty",
        90 : "ninety",
        }

def writeNum(out, num):
    if num == 1000:
        out.append("onethousand")
        num = 0
    hundreds = num / 100
    rest = num % 100
    if hundreds != 0:
        out.append(writing[hundreds])
        out.append("hundred")
        if rest != 0:
            out.append("and")
    if writing.has_key(rest):
        out.append(writing[rest])
    else:
        tens = rest / 10
        rest = rest % 10
        if tens != 0:
            out.append(writing[tens * 10])
            if rest != 0:
                out.append(writing[rest])

lst = []
for num in range(1, 1001):
    writeNum(lst, num)

length = 0
for s in lst:
    length += len(s)
print length
