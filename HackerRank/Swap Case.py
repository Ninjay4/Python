#!/usr/bin/env python
# coding: utf-8
‘’’
Created by Ninjay4
	On 1/23/24
	File Name: Swap Case.py
    HackerRank Basic Python Challenge
	Description: Demonstrate how to use the Swap Case Function
        Swap the cases on a given string
        In other words, convert all lowercase letters to uppercase letters and vice versa
	Python Version: 3
‘’’

# Create a swap case function
# "s" is a single line containing a string
def swap_case(s):
    newstring = s.swapcase()
    return newstring

# Create the input string, "s"
# Enter the string as "HackerRank.com presents "Pythonist 2"."
# Be sure to place the entire string within a pair of parentheses
s = input("Enter a single line string: ")

# Call the swap_case Function as a result
result = swap_case(s)

# Print the result
print(result)




