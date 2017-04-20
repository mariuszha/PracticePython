#!/usr/bin/python

#
# Character_Input.py v1.0 by mariuszha
#
# Exercise: Character Input
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#

import datetime

# User input
name = raw_input('Write your name: ')
age = int(raw_input('Write your age: '))

# Calculation
now = datetime.datetime.now()
current_year = now.year
birth_year = current_year - age
hundred_years = birth_year + 100

print 'Your name is %s and you have %d, you will turn your 100 in %d' % (name, age, hundred_years)
