import numpy as np
from gaussian_elimination_w_pp import part_piv_ge as gpp

def f(x,y,z): 
    return x**2 + 50*x + y**2 + z**2 - 200

def g(x,y,z):
    return x**2 + 20*y + z**2 - 50

def h(x,y,z):
    return -x**2 - y**2 + 40*z + 75

v = np.array([2,2,2])

def newton(f,g,h,v,i,delta,Nmax):
    """
    
    Parameters
    ----------
    f,g,h : functions whose root we want to find
    v : initial vector 
    i : Small number for numerical differentiation, otherwise known as "h" but using "i" here to differentiate between the function h and this value.
    delta : The tolerance/accuracy we desire (difference between two approximations)
    Nmax  : Maximum number of iterations to be performed


    Returns
    -------
    v : The approximation to the root
    iter_counter : Number of iterations it takes to satisfy tolerance

    """
    iter_counter = 0  #initialize iteration counter
    diff = float('inf') #initialize diff to be arbitrarily large float

    while diff > delta and iter_counter < Nmax: 

        #Partial derivatives using centered difference, elements for Jacobian Matrix 
        Jfx = (f(v[0]+i,v[1],v[2])-f(v[0]-i,v[1],v[2]))/(2*i)
        Jfy = (f(v[0],v[1]+i,v[2])-f(v[0],v[1]-i,v[2]))/(2*i) 
        Jfz = (f(v[0],v[1],v[2]+i)-f(v[0],v[1],v[2]-i))/(2*i) 
        Jgx = (g(v[0]+i,v[1],v[2])-g(v[0]-i,v[1],v[2]))/(2*i)
        Jgy = (g(v[0],v[1]+i,v[2])-g(v[0],v[1]-i,v[2]))/(2*i) 
        Jgz = (g(v[0],v[1],v[2]+i)-g(v[0],v[1],v[2]-i))/(2*i) 
        Jhx = (h(v[0]+i,v[1],v[2])-h(v[0]-i,v[1],v[2]))/(2*i) 
        Jhy = (h(v[0],v[1]+i,v[2])-h(v[0],v[1]-i,v[2]))/(2*i) 
        Jhz = (h(v[0],v[1],v[2]+i)-h(v[0],v[1],v[2]-i))/(2*i) 

        #Jacobian matrix
        J = np.array([ 
            [Jfx,Jfy,Jfz],
            [Jgx,Jgy,Jgz],
            [Jhx,Jhy,Jhz]
        ]) 

        b = np.array([
            [-1*f(v[0],v[1],v[2])],
            [-1*g(v[0],v[1],v[2])],
            [-1*h(v[0],v[1],v[2])]
        ])

        w = gpp(J,b) #Gaussian with pp to solve for w 
        new_v = np.add(w,v) #Add w and v for new estimate of v
    
        diff = np.amax(np.abs(np.subtract(new_v, v))) #Checking maximum difference between estimates
        
        v = new_v #Reassign v to new estimate

        iter_counter +=1 
        
        print("Iteration: ",iter_counter)
        print("Max Difference: ",diff)
        print("v: ",v)

    return v, iter_counter



v, iter_count = newton(f,g,h,v,0.05,5e-06,100)

print(v, iter_count)