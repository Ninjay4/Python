# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:44:52 2021
Nina Alexander
7.10
Math 4211
@author: nina_
"""

tolerance = 10**(-5)

def g(x):
    g = (2*x-1)**2 + 4*(4-1024*x)**4 #enter your function here
    return g

x0 = int(input("enter first guess "))
x1 = int(input("enter second guess "))

while abs(x1-x0) > abs(x0)*tolerance:
    temp = x1
    x1 = (x0*g(x1) - x1*g(x0))/(g(x1) - g(x0))
    x0 = temp
    solution = g(x0)

print("The Root is",x0)
print("The Value of G at the Root is", solution)

