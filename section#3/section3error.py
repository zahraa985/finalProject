from integration import team5Integrate
 
i = lambda x : x**5 # function
I = lambda x : 1/6 * x**6 # integral of i
a = 0 
b = 1
exact = I(b) - I(a)
team5Integral = team5Integrate(i, a, b)
print('team 5 integral =', team5Integral)

error = exact - team5Integral
print('team 5 error =', error)





