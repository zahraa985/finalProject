from integration import team5Integrate
 
i = lambda x : x**5
I = lambda x : 1/6 * x**6
a = 0
b = 1
exact = I(b) - I(a)
team5Integral = team5Integrate(i, a, b)
print('team 5 integral =', team5Integral)

error = exact - team5Integral
print('team 5 error =', error)





