#NumPy.py
"""
NumPy
Sophia Mo
06/26/2017
"""

import numpy as np
import math

#Problem 1
def prob1():
    A=np.array([[3,-1,4],[1,5,-9]])
    B=np.array([[2,6,-5,3],[5,-8,9,7],[9,-3,-2,-3]])
    C=np.dot(A,B)
    return C
print(prob1())

#Problem 2
def prob2():
    A=np.array([[3,-1,4],[1,5,-9],[-5,3,1]])
    B=-A**3+9*A**2-15*A
    return B
print(prob2())

#Problem 3
def prob3():
    A=np.ones((7,7))
    A=np.triu(A)
    B=np.full((7,7),-6)
    B=np.tril(B)
    B=B+5
    C=A*B*A
    C=C.astype(np.int64)
    return C
print(prob3())

#Problem 4
def prob4(A):
    B=np.copy(A)
    negative=B<0
    B[negative]=0
    return B

#Problem 5
def prob5():
    A=np.array([[0,2,4],[1,3,5]])
    B=np.array([[3,0,0],[3,3,0],[3,3,3]])
    C=np.array([[-2,0,0],[0,-2,0],[0,0,-2]])
    D=np.hstack((np.zeros((3,3)),A.T,np.eye(3)))
    E=np.hstack((A,np.zeros((2,2)),np.zeros((2,3))))
    F=np.hstack((B,np.zeros((3,2)),C))
    G=np.vstack((D,E,F))
    return G
print(prob5())

#Problem 6
def prob6(A):
    B=A/A.sum(axis=1)[:,None]
    return B

#Problem 7
grid = np.load("/Users/Sophia/Desktop/BootCamp2017/Computation/wk1_hw/grid.npy")
def prob7():
    A=np.max(grid[:,:-3] * grid[:,1:-2] * grid[:,2:-1] * grid[:,3:])
    B=np.max(grid[:-3,:] * grid[1:-2,:] * grid[2:-1,:] * grid[3:,:])
    C=np.max(grid[:-3,:-3] * grid[1:-2,1:-2] * grid[2:-1, 2:-1] * grid[3:, 3])
    D=np.max(grid[3:,3] * grid[2:-1,2:-1] * grid[1:-2, 1:-2] * grid[:-3, :-3])
    return max(A,B,C,D)
print(prob7())
