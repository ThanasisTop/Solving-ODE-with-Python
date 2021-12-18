# Solving a general problem u''+p(x)u'+q(x)u = f
# p(x) = x/(1+x^2)
# q(x) = 3/(1+x^2)
# f(x) = (6x-3)/(1+x^2)

import numpy as np
from math import sin, pi
import matplotlib.pyplot as plt


N=100


x = np.linspace(0, 1, N)
h = x[1]-x[0]
A = np.zeros((N,N))
F = np.zeros(N)
Q = np.zeros((N, N))

A[0, 0] = 2
A[N-1,N-1] = 2

def p(x):
  return x/(1+x**2)

for i in range(0, N-1):
  F[i] = (6*x[i]-3)/(1+x[i]**2)

for i in range(0, N-1):
  A[i, i] = 2
  A[i+1, i] = -1 -p(x[i])*h/2
  A[i, i+1] = -1 +p(x[i])*h/2

for i in range(0, N):
  Q[i, i] = 3/(1+x[i]**2)


h2Q = h**2*Q

B = A + h2Q
U = np.linalg.solve(B, F)
U[0]=1
U[N-1]=2


plt.plot(x,U, '-k')