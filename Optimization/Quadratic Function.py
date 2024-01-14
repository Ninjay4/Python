# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 17:58:18 2021
Nina Alexander
Math 4211
Quadratic Formula

Description: This program finds the real roots
of ax^2 + bx + c if b^2 > 4ac. Or it will return
the message "No real root for this equation."

@author: nina_
"""

import math

def discriminant(a, b, c):
    DTotal = (b**2)-(4*a*c)
    return DTotal

print('Find the real roots of ax^2 + bx + c = 0')
print('using the quadratic equation.')
print('')
print('Enter the numerical values for a,b, and c')
print('or enter a zero for "a" to exit the program.')
print('')

a = float(input('Enter the "a" value: '))

while a != 0:
    b = float(input('Enter the "b" value: '))
    c = float(input('Enter the "c" value: '))
    disc = discriminant(a, b, c)
    
    if (b**2)<4*a*c:
        print('The discriminant is: ', disc)
        print('There is no real root for this equation.')
        print('')
        print('Enter another numerical value for a,b, and c')
        print('or enter a zero for "a" to exit program.')
        print('')
        a = float(input('Enter the "a" value: '))
        
    SqrRoot = math.sqrt(disc)
    root1 = (-b+SqrRoot)/(2*a)
    root2 = (-b-SqrRoot)/(2*a)
    print('The Discriminant is: ', disc)
    if disc == 0:
                print('The equation has one real solution.')
                print('Root 1 = ', root1)
                print('Root 2 = ', root2)
    else:
                print('The equation has two real solutions.')
                print('Root 1 = ', root1)
                print('Root 2 = ', root2)
    print('')
    print('Enter another numerical value for a,b, and c')
    print('or enter a zero for "a" to exit program.')
    print('')
    a = int(input('Enter the "a" value: '))

print('Thank you for using the quadratic formula program.')
    
    