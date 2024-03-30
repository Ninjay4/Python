#!/usr/bin/env python
# coding: utf-8
'''
FILE NAME: Capitalize
CREATED BY: Ninjay4
CREATED ON:
MODIFIED ON: none
DESCRIPTION:
Given a first and last name, capitalize the 1st letters of each word
A single line of input contains the full name
'''
# Create a capitalization function
# This function only works when a name section does NOT have
# any apostrophe's nor hyphens
#def solve(s):
#    caps = s.title()
#    return caps

# Create another capitalization function
import string
def solve(s):
    caps = string.capwords(s, " ")
    return caps

# Create the input string
# Enter "chris alan" in lowercase letters
s = input("Enter the first and last name: ")

# Run the function
result = solve(s)
print(result)





