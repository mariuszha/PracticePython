#!/usr/bin/python

#
# List_Overlap.py v1.0 by mariuszha
#
# Exercise: List Overlap
# Take two lists, say for example these two:
#
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
#
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def overlap(a,b):
    c = []
    for i in b:
        if i in a and i not in c:
            c.append(i)

    return c

print overlap(a,b)
