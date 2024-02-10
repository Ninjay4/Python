#!/usr/bin/env python
# coding: utf-8
‘’’
Created by Ninjay4
	On 1/26/24
	File Name: Tuples.py
  HackerRank Basic Python Challenge
	Description: Given an integer,"n", and "n" space-separated integers as input, 
    create a tuple,"t", of those "n" integers
    Then compute and print the result of hash(t) 
	Python Version: 3
‘’’

n = int(input()) # Enter "2"

integer_list = map(int, input().split()) # Enter "1 2" - separated by one space

t = tuple(integer_list) # Create the tuple, t

print(hash(t)) # Print hash(t)

# Generates an answer of -3550055125485641917 with Python3
# This is different than the HackerRank answer of 3713081631934410656
# which may work with Pypy; Perhaps the answer needs to be
# updated in HackerRank



