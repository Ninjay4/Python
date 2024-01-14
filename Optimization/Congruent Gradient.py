# -*- coding: utf-8 -*-
"""
Nina Alexander
Math 4211
Homework #5
#10.11
This program is still in the debugging process. Not working yet...
"""
import numpy as np

# Commands the congruent gradient algorithm to run with the values below
cga(-2,2,100)
#set-up the conjugate gradient algorithm. Vector X contains <x1,x2>
#The maximum number of loops will be 100
def cga(x1,x2,iter=100):
    x = np.array([x1,x2])
    #to count the number of iterations
    k = 0 
    
    for h in range(iter): #the for loop will run no more than 100 times
        #the objective function
        f = 100*(x2- x1**2)**2 + (1- x1)**2 
        #The gradient
        y1 =  400*x1**3 -400*x1*x2 + 2*x1 - 2
        y2 = 200*(x2- x1**2)
        #Creates the gradient vector
        g = np.array([y1,y2])
        
#if the gradient is equal to zero,the loop will terminate early       
        if y1 == 0 and y2 == 0:
            break
    
       #will reinitialize the update direction every six iterations
        if k == 0:
            d1 = -y1
            d2 = -y2
        #Creates the direction vector   
        d = np.array([d1,d2])
        
        #Creates the Q Matrix
        qa = 1200*(x1**2) - 400*x2 + 2
        qb = -400*x1
        qc = 2*x1*(200*(x2-x1**2))
        qd = 200*(x2-x1**2)
        Q = np.array([qa,qb],[qc,qd])
        
        #Creates alpha as the line search function to generate the next "X"
        dQ = d*Q
        alpha = -[(g*d)/(dQ*d)]
        
        #Creates beta as the line search function to generate the next "D"
        gQ = g*Q
        beta = (gQ*d)/(dQ*d)
        #updates the directional vector every 6 iterations
        if k>0 and k%6==0:
            d = -g + beta*d
            
        #update the "x" values
        x1 = x1 + alpha*d1
        x2 = x2 + alpha*d2
        
        #update the iteration number
        k += 1
        
        print("Iteration ", k)
        print("x is ", x)
    
    print("The minimizer of f is ", x)
    print("The number of iterations was ", k)
    print("The objective function, f, at the final point is ", f)

