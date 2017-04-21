#!/usr/bin/python

#
# 4_Divisors.py v1.0 by mariuszha
#
# Exercise: Divisors
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# If you don not know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.

# Ask for a number
num = raw_input('Please give a number: ')
num = int(num)
# Check all the divisors of that number
potentials_divisors = range(1,num+1)

divisors = []
for i in potentials_divisors:
    if num % i == 0:
        divisors.append(i)

print divisors
