#!/usr/bin/env python
# coding: utf-8
‘’’
Created by Ninjay4
	On 1/15/24
	File Name: RunnerUp Score.py
  HackerRank Basic Python Challenge
	Description: Given the participants' score sheet for your University Sports Day, 
    you are required to find the runner-up score. You are given scores. 
    Store them in a list and find the score of the runner-up. 
	Python Version: 3
‘’’

# Create the list of scores
scores = [2, 3, 6, 6, 5]
print(scores)  # Print to verify

# Turn the list into a set so that any duplicates are removed
setList = set(scores)
print(setList) # Print to verify

# Turn the set into a revised list
revScores = list(setList)
print(revScores) # Print to verify

# Because the list is in ascending order, the runner-up score
# will be the second to the last element
print(revScores[-2])



