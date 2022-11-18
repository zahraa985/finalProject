import sys
import math
import matplotlib.pyplot as plt
from math import tanh

                    
def secant(f,x0,x1,delta):
    """
    

    Parameters
    ----------
    f     : function whose root we want to find
 
    x0,x1 : Left and right endpoints, respectively, of initial interval
    delta : The tolerance/accuracy we desire
    Nmax  : Maximum number of iterations to be performed

    Raises
    ------
    Exception
        DESCRIPTION.

    Returns
    -------
    x : The approximation to the root
        DESCRIPTION.
    iter_counter : Number of iterations it takes to satisfy tolerance

    """
    
    iter_counter = 0  # set iteration counter to zero
    
    fx0 = f(x0); fx1=f(x1)
    while abs(fx1) > delta and iter_counter < 100:
        try:
            print(x1)

            dx = float(fx1 - fx0)/(x1-x0)
            x  = x1 - float(fx1)/dx  # Secant method
            
        except ZeroDivisionError:
            print("Error! - denominator zero for x = ", x)
            sys.exit(1)     # Abort with error

        x0 = x1; x1 = x
        fx0 = f(x0); fx1=f(x1)
        iter_counter +=1 
    

    # Here, either a solution is found, or too many iterations
    if abs(f(x1)) > delta:
        iter_counter = -1
    return x, iter_counter

def f(x):
    return tanh(x) 

#x0 = 1.08; x1= 1.09
#x0 = 1.09; x1= 1.1
x0 = 1.0; x1= 2.3
#x0 = 1.0; x1= 2.4

solution, no_iterations = secant(f,x0,x1,1.0e-6)

if no_iterations > 0:    # Solution found
    print("Number of function calls: %d" % (2 + no_iterations))
    print("A solution is: %f" % (solution))
else:
    print("Solution not found!")