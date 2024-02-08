#!/usr/bin/env python
# coding: utf-8
‘’’
Created by Ninjay4
	On 1/24/24
	File Name: Whats Your Name.py
    HackerRank Basic Python Challenge
	Description: Given the firstname and lastname of a person on two different lines
     read them and print the following:
     "Hello firstname lastname! You just delved into python"
	Python Version: 3
‘’’

# Create a function to print the full name
def print_full_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return print("Hello " + full_name + "!  You just delved into python.")

# Create two inputs: first_name and last_name on two different lines
# Enter "Ross" as first_name - No parentheses needed
# Enter "Taylor" as last_name -- No parentheses needed
first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")

# Run the print_full_name function
print_full_name(first_name, last_name)




