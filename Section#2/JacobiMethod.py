import numpy as np
from numpy import array
from numpy import linalg as LA
from numpy import inf

"""
%Jacobi      Use both the Jacobi method and the Gauss-Seidel method to solve the indicated linear system of equations.
%             
%   
%             
%
%     inputs:
%             A       coefficient matrix for linear system
%                     (matrix must be square)
%             b       right-hand side vector
%
%     output:
%             x       solution vector (i.e., vector for which Ax = b)
%
%
"""
# setting the iteration limit 

ITERATION_LIMIT = 1000

# initialize the matrix
A = array([
    [4.0, -1, 0, -2, 0, 0],
    [-1, 4, -1, 0, -2, 0], 
    [0, -1, 4, 0, 0, -2], 
    [-1, 0, 0, 4, -1, 0], 
    [0, -1, 0, -1, 4, -1], 
    [0, 0, -1, 0, -1, 4]])
# initialize the b vector
b = array([-1.0,0,1,-2,1,2])

# assigning some variables that will be used in the functions
n  = 0  #iteration counter
tol = 5e-6 # iterations should terminate when my iterantions falls bellow 5 X 10^-6
converged = False # for convergence test

# prints the equations of the linear system A for the User (input)
print("System of equations:")
for i in range(A.shape[0]):
    row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    
    #printing the number iterations until the tol is met
    print(f'{" + ".join(row)} = {b[i]}')
print()

# initial vector
x = np.zeros_like(b)

# Jacobi method 
for i_t in range(ITERATION_LIMIT): # i_t = iterations coiunt 
    if i_t != 0: # iteration count is not equal to 0
        print("Iteration {0}: {1}".format(i_t, x))
    x_new = np.zeros_like(x)

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if x_new[i] == x_new[i-1]:
          break

    if np.allclose(x, x_new, atol=5e-6, rtol=0.):
        break

    x = x_new

    # Number of iterations for Jacobi
    xn = LA.norm(x-i_t,inf)
    n = n + 1

    

# Output
print("approximate x = {0}".format(x))
error = np.dot(A, x) - b
print("Error:")
print(error)
