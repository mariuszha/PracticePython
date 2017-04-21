#!/usr/bin/python

#
# 2_Odd_or_Even.py v1.0 by mariuszha
# 
# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user. 



# Ask for a number
num = raw_input('Give a number: ')
num = int(num)

# Checking whether the given number is odd or even
if num % 2 == 0:
    print 'Your number is even'
else:
    print 'Your number is odd'
    
