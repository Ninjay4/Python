#!/usr/bin/env python
# coding: utf-8
‘’’
Created by Ninjay4
	On 2/10/24
	File Name: Text Wrap.py
    HackerRank Basic Python Challenge
	Description: Given a string and a maximun width, "max_width"
        Wrap the string into a paragraph of where
        Each line does NOT exceed the maximum width
        The wrap has the following parameters:
            string: a long string
            int max_width: the width to wrap to
        Constraints:
            0 < string length < 1,000
            0 < max_width < string length
        Returns a string: a single string with newline characters ('\n') 
            where the breaks should be
	Python Version: 3
‘’’

# import the textwrap function
import textwrap

# Create a wrap function
# The "wrap" function returns a list
# So the print must be converted from a list
# into a string of new lines
# Where each line is of width, "w"
def wrap(string, max_width):
    twstring = textwrap.wrap(string, max_width)
    return '\n'.join(twstring)

# Input Format
# The first line contains the string
# The second line contains the max_width
# Create the inputs
# Use string = "abcdefghijklmnopqrstuvwxyz"
# Use 4 as the max_width
string = input("Enter the String: ")
max_width = int(input("Enter the maximum width of each new line: "))

# Call the wrap function as a result
result = wrap(string, max_width)

# Print the result
print(result)

