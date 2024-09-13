import matplotlib.pyplot as plt
from semmakkon import *
import numpy as np
import matplotlib.pyplot as plt

def line(a, m = 1, n = 10):
    R = np.linspace(a/2, n*a/2, n*100)
    Y = [0 for i in R]
    X = [0 for i in R]
    for i in range(len(R)):
        r = R[i]
        alfa = acos((2*r*r-a*a)/(2*r*r))
        X[i] = r*cos(m*alfa)
        Y[i] = r*sin(m*alfa)
    return (X, Y)

def line2(a, m = 2, n = 1):
    r = a*n
    Y = [0 for i in range(m)]
    X = [0 for i in range(m)]
    for i in range(m):
        alfa = acos((2*r*r-a*a)/(2*r*r))
        X[i] = r*cos(i*alfa)
        Y[i] = r*sin(i*alfa)
    return (X, Y)

for i in range(4):
    X, Y = line(10, i)
    plt.plot(X, Y)
for i in range(1, 5):
    X, Y = line2(10, 10, i)
    plt.plot(X, Y)

plt.scatter([0], [0])


plt.show()