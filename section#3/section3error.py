from section3 import team5Integrate
import numpy as np

i = lambda x : x**4
I = lambda x : 1/5 * x**5
a = 0


count = 0

while count < 10:
    h = 0.5**count
    value = team5Integrate(i, a, h)
    exact = I(h)-I(a)
    error = abs(exact-value)
    eh = error/h
    eh2 = error/h**2
    eh3 = error/h**3
    eh4 = error/h**4
    eh5 = error/h**5
    #print('error =', error, 'error/h =', eh2, 'error/h**2 =', eh2, 'error/h**3 =', eh3, 'error/h**4 =', eh4)
    print('h =', h, 'error/h**5 =' , eh5)
    count += 1








