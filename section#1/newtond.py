import math
import matplotlib.pyplot as plt
from numpy import tanh, linspace

def newtond(f,fp,x0,delta):
    """
    
    Parameters
    ----------
    f     : function whose root we want to find
    fp    : first derivative of f 
    x0    : Initial guess for the root of f
    delta : The tolerance/accuracy we desire
    Nmax  : Maximum number of iterations=100

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
    f_value = f(x0)

    while abs(f(x0)) > delta and iter_counter < 100:
        try:
            print('x value: ', x0)
            x0 = x0 - float(f(x0)/fp(x0))  # Newton's method
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", x)
            sys.exit(1)     # Abort with error
        f_value = f(x0)
        iter_counter +=1 

    # Here, either a solution is found, or too many iterations
    if abs(f_value) > delta:
        iteration_counter = -1
    return x0, iter_counter

def f(x):
    return tanh(x) 

# Find the forward difference approximation
def fp(x):
    return (f(x+h) - f(x-h))/(2*h)

#The discretization sizes
h = 0.1/2




