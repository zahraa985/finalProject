def team5Integrate(f, a, b):
    A1 = -((a-b)*(3*a-b))/(6*(7*a-3*b))
    A2 = (4*(a-b)**2)/(3*(a+3*b))
    A3 = -(4*(a-b)**2)/(3*(7*a-3*b))
    A4 = -((a-b)*(11*a+b))/(6*(a+3*b))

    return A1*f(a) + A2*f((b-a)/4) + A3*f((3*(b-a))/4) + A4*f(b)

f = lambda x: 1
g = lambda x: x
h = lambda x: x**2
j = lambda x: x**3

print(team5Integrate(f, 0, 1))
print(team5Integrate(g, 0, 1))
print(team5Integrate(h, 0, 1))
print(team5Integrate(j, 0, 1))