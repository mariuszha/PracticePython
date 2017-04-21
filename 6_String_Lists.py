#!/usr/bin/python

#
# 6_String_Lists.py v1.0 by mariuszha
#
# Exercise: String Lists
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
#

# Asking user for a word
user_string = raw_input('Write a string: ')

# Checking if this word is a palindrome or not
if user_string == user_string[::-1]:
    print 'The string %s is a palindrome' % user_string
else:
    print 'The string %s is not a palindrome' % user_string
    
