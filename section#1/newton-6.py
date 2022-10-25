import math
import matplotlib.pyplot as plt
from math import tanh

def newton(f,fp,x0,delta,Nmax):
    """
    
    Parameters
    ----------
    f     : function whose root we want to find
    fp    : first derivative of f 
    x0    : Initial guess for the root of f
    delta : The tolerance/accuracy we desire
    Nmax  : Maximum number of iterations to be performed

    Raises
    ------
    Exception
        DESCRIPTION.

    Returns
    -------
    x0 : The approximation to the root
        DESCRIPTION.
    iter_counter : Number of iterations it takes to satisfy tolerance

    """
    
    iter_counter = 0  # set iteration counter to zero
    
    while abs(f(x0)) > delta and iter_counter < Nmax:
        try:
            x0 = x0 - f(x0)/fp(x0)  # Newton's method
            print(x0)
        except:
            raise Exception("Division by zero. f'(x) = 0")
            
        iter_counter +=1 
          
    return x0, iter_counter

def f(x):
    return tanh(x) #x**2-3 #(5.0-x)*math.exp(x)-5

def fp(x):
    return 1-tanh(x)**2 

print(newton(f,fp,1.09,0.001,7))
