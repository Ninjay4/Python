#!/usr/bin/env python
# coding: utf-8
‘’’
Created by Ninjay4
	On 1/27/24
	File Name: String Validators.py
    HackerRank Basic Python Challenge
	Description: Use built-in string validator methods
        To check if a string is composed of 
        Any Alphabetical, Alphanumeric, Upper,
        or Lower characters
        Given a string, check it to see if
        It contains any of the characters named above
	Python Version: 3
‘’’

# Create the input string as a single line
# Enter "qA2" as the string
s = input("Enter the string: ")

# Must have 5 lines of output
# In the first line, print True if "the String" has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if "the String" has any alphabetical characters. Otherwise, print False.
# In the third line, print True if "the String" has any digits. Otherwise, print False.
# In the fourth line, print True if "the String" has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if "the String" has any uppercase characters. Otherwise, print False.

# Create the code as a series of Conditional statements
# Use the any() Function
if any(e.isalnum() for e in s): # Alphanumeric is alnum
    print('True')
else:
    print('False')
if any(e.isalpha() for e in s): # Alphabetical is alpha
    print('True')
else:
    print('False')
if any(e.isdigit() for e in s): # Digits are numerical digits
    print('True')
else:
    print('False')
if any(e.islower() for e in s): # Lowercase is lower
    print('True')
else:
    print('False')
if any(e.isupper() for e in s): # Uppercase is upper
    print('True')
else:
    print('False')



