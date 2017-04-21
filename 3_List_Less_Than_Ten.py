#!/usr/bin/python

# 3_List_Less_Than_Ten.py v1.0 by mariuszha
#
# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Printing all numbers that are less than 5 one by one
print 'Given list of numbers %s' % a
print 'Numbers which are less than 5:'
for num in a:
    if num < 5:
        print num

print 

# Printing all numbers that are less than 5 but as a list
num_list = []
for num in a:
    if num < 5:
        num_list.append(num)
print 'Above numbers printed as a list %s' % num_list
