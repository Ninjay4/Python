# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:45:51 2021
Ninjay4
Steepest Descent
"""
import numpy as np

#set-up the steepest descent method. Vector X contains <x1,x2,x3>
#The maximum number of loops will be 100
#The stopping criterion will use a tolerance level of 10^(-6)
def sdm(x1,x2,x3,iter=100,tol=10**(-6)):
    
    k = 0 #use k to count the actual number of iterations
    for h in range(iter): #the for loop will only run within 100 loops
        g = (x1-4)**4 + (x2-3)**2 + 4*(x3+5)**4 #the objective function
        
        #The gradient
        y1 = 4*(x1-4)**3 #Here are the Gradient values of each vector component
        y2 = 2*(x2-3)
        y3 = 16*(x3+5)**3
        gradient = np.array([y1,y2,y3]) #Creates the gradient array
        grad_norm = np.linalg.norm(gradient) #Calculates the norm of the gradient
#if the norm of the gradient is less than 10^(-6), the loop will terminate early       
        if grad_norm <= tol:
            break
        
# Introduces the secant method which will calculate the value for alpha
# alpha = arg min f(x-(alpha)*gradient(x))
# the line search function (lsf) that will be used by the Secant method
        def lsf(z): 
            lsf = (-z*y1+x1-4)**4 + (-z*y2+x2-3)**2 + 4*(-z*y3+x3+5)**4 
            return lsf
        # commands the secant method to run with the indicated values
        alpha = secant(lsf,.1,.15,100,10**(-5))
        
        x1 = x1-alpha*y1
        x2 = x2-alpha*y2
        x3 = x3-alpha*y3
        k = k+1 #the current iteration number
        
        print("Iteration ", k)
        print("x1 is ", x1)
        print("x2 is ", x2)
        print("x3 is ", x3)
    
    print("The minimizer of g is ", [x1 ,x2, x3])
    print("The number of iterations was ", k)
    print("The objective function, g, at the final point is ", g)
    
# Creates the secant method which will calculate the alpha value
# Plugs the two starting guesses, z0 and z1, into the line search function
def secant(lsf,z0,z1,iter=100, tol=10**(-5)):
    g0 = lsf(z0)
    g1 = lsf(z1)
# The stopping criterion
    for h in range(iter):
        if np.abs(z1-z0) < np.abs(z0)*tol:
            break
# Calculates the new alpha value, z   
        z = (z0*g1 - z1*g0)/(g1 - g0)
        g = lsf(z)  
# Resets the values for the next loop     
        z0 = z1
        z1 = z
        g0 = g1
        g1 = g
        
    return z
# Commands the steepest descent method to run with the values below
sdm(-4,5,1,100,10**-6)
