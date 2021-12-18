#Solving the partial differential equation: u''+ u = sin(2πx), u(0) = u(1) = 0
#with finite differences method

import numpy as np
from math import sin, pi
import matplotlib.pyplot as plt


N=100


x = np.linspace(0, 1, N)
h = x[1]-x[0]
A = np.zeros((N,N))
F = np.zeros(N)

A[0, 0] = 2
A[N-1,N-1] = 2

for i in range(0, N-1):
  F[i] = sin(2*pi*x[i])

for i in range(0, N-1):
  A[i, i] = 2
  A[i+1, i] = -1
  A[i, i+1] = -1

h2Q = h**2*np.identity(N)


B = A + h2Q
U = np.linalg.solve(B, F)
U[0]=1
U[N-1]=2


plt.plot(x,U, '-k')