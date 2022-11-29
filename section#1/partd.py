from numpy import tanh
from newtond import newtond

def bisection_Newton(f, fp,a, b, delta, s=0.1):
    #x_L=a,x_R=b
    
    fa = f(a)
    fb = f(b)
    if fa*f(b) > 0:
        print("Error! Function does not have opposite \ signs at interval endpoints!")
        sys.exit(1)

    print("initial interval: ","a =",a," b =",b," f(a)=", fa," f(b) =",fb)

    c = float(a + b)/2.0
    fc = f(c)
    iteration_counter = 1
    interval_Newton = s*(b - a)    # Limit for swith to Newton
    
    while (b - a) > interval_Newton:
        if fa*fc > 0:   # i.e. same sign
            a = c
            fa = fc
        else:
            b = c
        c = float(a + b)/2
        fc = f(c)

        print("a =",a," b =",b, "c =",c," f(a) =",fa," f(b) =",fb," f(c) =",fc)

        iteration_counter += 1
    solution, no_iterations = newtond(f,fp,c,delta)
    return solution, (iteration_counter + no_iterations)

def f(x):
    return tanh(x) 

# Find the forward difference approximation
def fp(x):
    return (f(x+h) - f(x-h))/(2*h)

#The discretization sizes
h = 0.1/2



delta = 1e-6
a = -10;   b = 15



solution, no_iterations = \
                     bisection_Newton(f, fp, a, b, delta)
print("A solution x = %f was reached in %d iterations" % \
(solution,no_iterations))