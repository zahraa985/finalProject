import math
import matplotlib.pyplot as plt
from numpy import tanh, linspace

def newton(f,fp,x0,delta):
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
            plot_line(f, x0, f_value, fp(x0))
            x0 = x0 - float(f(x0)/fp(x0))  # Newton's method
        except:
            raise Exception("Division by zero. f'(x) = 0")
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

def fp(x):
    return 1-tanh(x)**2 


def plot_line(f, xn, f_xn, slope):
    # Plot both f(x) and the tangent
    x_f = linspace(-2,2,100)
    y_f = f(x_f)
    x_t = linspace(xn-2,xn+2,10)
    y_t = slope*x_t + (f_xn - slope*xn)  # Straight line: ax + b
    plt.figure() 
    plt.plot(x_t, y_t, 'r-', x_f, y_f, 'b-');    plt.grid('on')
    plt.xlabel('x');    plt.ylabel('f(x)')
    plt.show()


#print(newton(f,fp,1.08,0.001))
#print(newton(f,fp,1.09,0.001))

def application():
    solution, no_iterations = \
                      newton(f,fp,1.08,0.001)
    
    if no_iterations > 0:    # Solution found
        print("Number of function calls: %d" % (1 + 2*no_iterations)) 
        print("A solution is: %f" % (solution))
    else:
        print("Solution not found!")

if __name__ == '__main__':
    application()