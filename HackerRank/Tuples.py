#!/usr/bin/env python
# coding: utf-8


# Given an integer,"n", and "n" space-separated integers as input, 
# create a tuple,"t", of those "n" integers
# Then compute and print the result of hash(t) 

n = int(input()) # Enter "2"

integer_list = map(int, input().split()) # Enter "1 2" - separated by one space

t = tuple(integer_list) # Create the tuple, t

print(hash(t)) # Print hash(t)

# Generates an answer of -3550055125485641917 with Python3
# This is different than the HackerRank answer of 3713081631934410656
# which may work with Pypy; Perhaps the answer needs to be
# updated in HackerRank



