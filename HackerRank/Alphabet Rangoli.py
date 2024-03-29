#!/usr/bin/env python
# coding: utf-8
‘’’
Created by Ninjay4
	On 1/26/24
	File Name: Alphabet Rangoli.py
	Description:  HackerRank Basic Python Challenge 
        Given an integer "n", from 1 to 26, print an alphabet rangoli of size "n"
        Only use lowercase letters and hyphens
	Python Version: 3
‘’’

# Create an alphabet dictionary
alpha = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

print(alpha[6]) # Test

# Create the input integer
n = int(input("Enter an integer from 1 to 26: "))

# Create the print_rangoli Function
def print_rangoli(n):
# Create a loop for the top half
    front = ""
    back = ""
    middle2 = ""
    for i in range(n, 0, -1):
        dashes = ("-")*((i-1)*2)
        middle = alpha[i]
        middle2 = dashes + front + middle + back + dashes
        print(middle2)
        front += (alpha[i] + "-")
        back = ("-" + alpha[i]) + back
# Create a loop for the bottom portion
    for i in range(2, n+1):
        dashes = ("-")*((i-1)*2)
        middle2 = middle2.replace(alpha[i] + "-" + alpha[i-1] +"-"+alpha[i], alpha[i])
        print(dashes + middle2 + dashes)
    
# Run the print_rangoli Function
print_rangoli(n)

