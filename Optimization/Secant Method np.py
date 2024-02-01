# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:44:52 2021
Ninjay4
Secant Method using NumPy
"""
import numpy as np

#print("The Value of G at the Root is", solution)

def df(x):
    df = (2*x-1)**2 + 4*(4-1024*x)**4 #enter your function here
    return df
        
def secant(df,x0,x1,tol=10**(-5)):
    g0 = df(x0)
    g1 = df(x1)
    k = 0

    while np.abs(x1-x0) > np.abs(x0)*tol:
        x = (x0*g1 - x1*g0)/(g1 - g0)
        g = df(x)  
        
        x0 = x1
        x1 = x
        g0 = g1
        g1 = g
        k = k+1
    
        print("Iteration ", k)
        print("The Root is ", x)
        
    return print("The Final Root is", x)


secant(df,0,1,10**(-5))


#print("The value of g at the root is",g)
