from numpy import tanh
from newton_a import newton

def bisection_Newton(f, fp, x_L, x_R, delta, s=0.1):
    f_L = f(x_L)
    if f_L*f(x_R) > 0:
        print("Error! Function does not have opposite \ signs at interval endpoints!")
        sys.exit(1)
    x_M = float(x_L + x_R)/2.0
    f_M = f(x_M)
    iteration_counter = 1
    interval_Newton = s*(x_R - x_L)    # Limit for swith to Newton
    
    while (x_R - x_L) > interval_Newton:
        if f_L*f_M > 0:   # i.e. same sign
            x_L = x_M
            f_L = f_M
        else:
            x_R = x_M
        x_M = float(x_L + x_R)/2
        f_M = f(x_M)
        iteration_counter += 1
    solution, no_iterations = newton(f,fp,x0,delta,Nmax)
    return solution, (iteration_counter + no_iterations)

def f(x):
    return tanh(x) 

def fp(x):
    return 1-tanh(x)**2 

delta = 1e-6
a = -10;   b = 15
x0=1.08
Nmax = 100

solution, no_iterations = \
                     bisection_Newton(f, fp, a, b, delta)
print("A solution x = %f was reached in %d iterations" % \
(solution,no_iterations))