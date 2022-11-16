from numpy import linspace , sum, exp, sin, cos, pi

class integration:
    def lhs(f,a,b,n): # left-hand Riemann sum
        h  = float(b - a)/n
        result = 0.0
        for i in range(0,n):
            x = a + i*h
            result += f(x)
        return h*result

    def lhs_vec(f,a,b,n): # left-hand Riemann sum (Vectorized version)
        h  = float(b - a)/n
        x  = linspace(a, b, n+1)
        result = sum(f(x[:-1]))
        return h*result
#%%    Double integration
    def lhs_double(f, a, b, c, d, nx, ny):
        def g(x):
            return integration.lhs(lambda y: f(x, y), c, d, ny)
        
        return integration.lhs(g, a, b, nx)
#%%        
    def rhs(f,a,b,n): # right-hand Riemann sum
        h  = float(b - a)/n
        x  = linspace(a, b, n+1)
        result = sum(f(x[1:]))
        return h*result
    
    def midpoint(f, a, b, n):
        h  = float(b - a)/n
        result = 0.0
        for i in range(0,n):
            x = a + (0.5+i)*h
            result += f(x)
        return h*result
    
    def trapezoidal(f, a, b, n):
        h  = float(b - a)/n
        result = 0.5*(f(a)+f(b))
        for i in range(1,n):
            x = a + i*h
            result += f(x)
        return h*result

    def simpson(f, a, b, n):
        if n%2 ==0:
            h = float(b - a)/n
            #h2 = 2*h; ah = a + h
            result = f(a)+f(b)
            for i in range(1,int(n/2)):
                j = 2*i; j1=j-1
                xe = a + j*h #even x
                x0 = a + j1*h #odd x
                result += 2.0*f(xe) + 4.0*f(x0)
            
            x0 = a + (n-1)*h
            result += 4.0*f(x0)
        else:
            print("n has to be even numbers")
            result= None
        return h*result/3.0    


f = lambda x: ((x-1)**2)*(x-2)
F = lambda x: ((x**4)/4)-((4*x**3)/3)+((5*x**2)/2)-(2*x)
a, b = -1, 2

exact = F(b) - F(a)
nvalues = [2**i for i in range(1,7)]



print("\t%s\t \t%s\t   \t%s\t \t\t%s \t\t%s \t\t%s \n" %("n", "lhs error", "rhs error", "midpoint error", "trapezoidal error", "simpson error"))
#print("\t\t%s\t\t    \t\t%s\t\t    \t\t%s\t\t   \t\t%s \t\t  \t\t\t%s \t\t\t%s    \n" %("n", "lhs", "rhs", "midpoint", "trapezoidal", "simpson"))

for n in nvalues:
    errlhs=abs(exact-integration.lhs(f,a,b,n))
    errrhs=abs(exact-integration.rhs(f,a,b,n))
    errmdpt=abs(exact-integration.midpoint(f,a,b,n))
    errtrap=abs(exact-integration.trapezoidal(f,a,b,n))
    errsim=abs(exact-integration.simpson(f, a, b, n))
    print(f"# h = {(b-a)/n}")

    print("%3d\t %8.6e\t\t %8.6e\t\t %8.6e\t\t %8.6e\t\t %8.6e\n" %(n,errlhs, errrhs, errmdpt, errtrap, round(errsim,6)))
    #print("%3d\t %9.6e\t\t %8.6e\t\t %8.6e \t\t %8.6e\t\t %8.6e\n" %(n, integration.lhs(f,a,b,n), integration.rhs(f,a,b,n), integration.midpoint(f,a,b,n), integration.trapezoidal(f,a,b,n), integration.simpson(f, a, b, n)))
    
    