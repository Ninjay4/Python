#!/usr/bin/env python
# coding: utf-8
‘’’
Created by Ninjay4
	On 1/20/24
	File Name: Write A Function.py
    HackerRank Basic Python Challenge
	Description: Determine if a given year is a leap year
      In the Gregorian calendar, three conditions are used to identify leap years:
      The year can be evenly divided by 4, is a leap year, unless:
      The year can be evenly divided by 100, it is NOT a leap year, unless:
      The year is also evenly divisible by 400. Then it is a leap year.
	Python Version: 3
‘’’

#  Given a year, determine whether it is a leap year.    
#  If it is a leap year, return the Boolean True, otherwise return False.

def is_leap(year):  # Create the "is_leap" function
    leap = False  # Make False the default value
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # List the conditions
        leap = True  # If the conditions are met, then the value is True for a Leap Year
    return leap # The return value closes the function

# Create the input value
year = int(input("Please enter the year: "))

# Run the is_leap() Function
is_leap(year)



