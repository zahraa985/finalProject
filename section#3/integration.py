from numpy import linspace , sum, exp, sin, cos, pi
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

class integration:

    def cubic(f, a, b, n):
        if n%2 ==0:
            h = float(b - a)/n
            #h2 = 2*h; ah = a + h
            result = f(a)+f(b)
            for i in range(1,n):
                xe = a + i*h 
                if i%2 == 0:
                    result = result + 2 * f(xe)
                else:
                    result = result + 3 * f(xe)

            # Finding final integration value
            result = result * 3 * h / 8
            
        else:
            print("n has to be even numbers")
            result= None
        return result    


f = lambda x: ((x-1)**2)*(x-2)
F = lambda x: ((x**4)/4)-((4*x**3)/3)+((5*x**2)/2)-(2*x)
a, b = -1, 2

exact = F(b) - F(a)
nvalues = [2**i for i in range(1,7)]




#print("\t%s\t\t \t\t%s\t\t  \n" %("n", "Cubic Intergration Algorithm"))

for n in nvalues:
    
    errsim=abs(exact-integration.cubic(f, a, b, n))
    print(f"# h = {(b-a)/n}, Cubic Intergration error = {round(errsim,6)}")
    #print(n, integration.simpson(f, a, b, n))

