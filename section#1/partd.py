from numpy import tanh
from newtond import newtond

def bisection_Newton(f, fp,x_L, x_R, delta, s=0.1):
    
    
    f_L = f(x_L)
    f_R = f(x_R)
    if f_L*f(x_R) > 0:
        print("Error! Function does not have opposite \ signs at interval endpoints!")
        sys.exit(1)

    print("initial interval: ","a =",x_L," b =",x_R," f(a)=", f_L," f(b) =",f_R)

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

        print("a =",x_L," b =",x_R, "c =",x_M," f(a) =",f_L," f(b) =",f_R," f(c) =",f_M)

        iteration_counter += 1
    solution, no_iterations = newtond(f,fp,x_M,delta)
    return solution, (iteration_counter + no_iterations)

def f(x):
    return tanh(x) 

# Find the forward difference approximation
def fp(x):
    return (f(x+h) - f(x-h))/(2*h)

fp = lambda x: 1-tanh(x)**2 
x = 1;
exact_deriv_value = fp(x)


delta = 1e-6
a = -10;   b = 15



solution, no_iterations = \
                     bisection_Newton(f, fp, a, b, delta)
print("A solution x = %f was reached in %d iterations" % \
(solution,no_iterations))