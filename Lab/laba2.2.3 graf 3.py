import matplotlib.pyplot as plt
from math import *
import numpy as np
from tabulate import tabulate

def MNK(x, y):
    n = len(x)
    sX = 0
    sY = 0
    sXY = 0
    sXX = 0
    sYY = 0
    for i in range(n):
        X = x[i]
        Y = y[i]
        sX += X/n
        sY += Y/n
        sXY += X*Y/n
        sXX += X*X/n
        sYY += Y*Y/n
    b = (sXY-sX*sY)/(sXX-sX**2)
    a = sY-b*sX
    sb = 1/n**0.5*((sYY-sY**2)/(sXX-sX**2)-b**2)**0.5
    sa = sb*(sXX-sX**2)**0.5
    return [b, a, sb, sa]


'''
l = [i/10 for i in range(10, 0, -1.txt)] + [0.01]
print(l)
x = [20*(1.txt-l[i]**0.5)/(l[i]**0.5) for i in range(11)]
print(x)'''
'''
I в мА
U в В'''
#20 градусов
I = [0 for i in range(6)]
U = [0 for i in range(6)]
R = [0 for i in range(6)]
Q = [0 for i in range(6)]
I[0] = [15, 44, 54, 63, 70, 76.3, 80]
U[0] = [0.3, 0.89, 1.1, 1.3, 1.44, 1.57, 1.65]
R[0] = [0.02, 0.0202, 0.0204, 0.0206, 0.0206, 0.0206, 0.0206]
Q[0] = [4.5, 39.16, 59.4, 81.9, 100.8, 119.791, 132.0]
#30 градусов
I[1] = [14.4, 40.25, 52.7, 61.1, 67.6, 74.4, 77.6]
U[1] = [0.3, 0.834, 1.1, 1.28, 1.42, 1.57, 1.65]
R[1] = [0.0208, 0.0207, 0.0209, 0.0209, 0.021, 0.0211, 0.0213]
Q[1] = [4.32, 33.5685, 57.97, 78.208, 95.992, 116.808, 128.04]
#40 градусов
I[2] = [14.38, 39.78, 51.83, 60, 66.4, 72.7, 77]
U[2] = [0.306, 0.852, 1.12, 1.3, 1.45, 1.59, 1.69]
R[2] = [0.0213, 0.0214, 0.0216, 0.0217, 0.0218, 0.0219, 0.0219]
Q[2] = [4.4003, 33.8926, 58.0496, 78.0, 96.28, 115.593, 130.13]
#50 градусов
I[3] = [14.4, 39.7, 51.6, 59.6, 66, 72.6, 76.3]
U[3] = [0.317, 0.879, 1.15, 1.33, 1.49, 1.65, 1.73]
R[3] = [0.022, 0.0221, 0.0223, 0.0223, 0.0226, 0.0227, 0.0227]
Q[3] = [4.5648, 34.8963, 59.34, 79.268, 98.34, 119.79, 131.999]
#60 градусов
I[4] = [14.45, 39.9, 52, 60.1, 67, 72, 75.2]
U[4] = [0.328, 0.91, 1.2, 1.39, 1.55, 1.67, 1.75]
R[4] = [0.0227, 0.0228, 0.0231, 0.0231, 0.0231, 0.0232, 0.0233]
Q[4] = [4.7396, 36.309, 62.4, 83.539, 103.85, 120.24, 131.6]
#70 градусов
I[5] = [14.36, 39.6, 51.5, 59.3, 65.5, 71.2, 74.7]
U[5] = [0.336, 0.93, 1.22, 1.41, 1.55, 1.71, 1.79]
R[5] = [0.0234, 0.0235, 0.0237, 0.0238, 0.0237, 0.024, 0.024]
Q[5] = [4.825, 36.828, 62.83, 83.613, 101.525, 121.752, 133.713]
for i in range(6):
    for j in range(7):
        I[i][j]*=0.001
        R[i][j]*=1000
        Q[i][j]*=0.001
''''''
n = len(I)
'''
I += [float(input())]
U += [float(input())]

print(I)
print(U)
''''''
R = [round(U[i]/I[i], 4) for i in range(n)]
Q = [round(U[i]*I[i], 4) for i in range(n)]
print(R)
print(Q)
'''
c = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
c = ['r', 'orange', 'y', 'g', 'b', 'm' ]
K = []
R0 = []

for i in range(6):
    #plt.plot(Q[i], R[i], color = c[i], linewidth = 1.txt)
    k = MNK(Q[i], R[i])
    x = np.arange(0, max(Q[i])*1.05, max(Q[i])*1.05*0.0001)
    #plt.plot(x, k[1.txt]+k[0]*x, color = c[i], linewidth = 1.txt)
    K.append([k[0], k[2]])
    R0.append([k[1], k[3]])

#plt.plot([0, 0], [20, 24], color = 'k')

T = [[20, 30, 40, 50, 60, 70][i]+273 for i in range(6)]
#plt.scatter(T, [R0[i][0] for i in range(6)], s = 5)
k1 = MNK(T, [R0[i][0] for i in range(6)])
x1 = np.arange(0, max(T)*1.05, (max(T)-min(T))*0.0001)
#plt.plot(x1, k1[1.txt]+k1[0]*x1, linewidth = 1.txt)
al = k1[0]/k1[1]
ln = 4.95
kx = [k1[0]*ln/(K[i][0]*2*pi*0.4) for i in range(6)]
skx = [kx[i]*(k1[2]/k1[0]+K[i][1]/K[i][0]) for i in range(6)]
#print(kx)
#print(skx)
#print([round(kx[i], 4) for i in range(6)])
lnT = [log(T[i]) for i in range(6)]
lnk = [log(kx[i]) for i in range(6)]
#plt.plot(T, kx)
plt.plot(lnT, lnk)
kln = MNK(lnT, lnk)
x = np.arange(min(lnT), max(lnT), (max(lnT)-min(lnT))*0.0001)
plt.plot(x, kln[1]+kln[0]*x, color = c[i], linewidth = 1)

plt.show()
Ktab = [[0 for i in range(6)] for i in range(2)]
R0tab = [[0 for i in range(6)] for i in range(2)]
for i in range(6):
    for j in range(2):
        Ktab[j][i] = round(K[i][j], 2)
for i in range(6):
    for j in range(2):
        R0tab[j][i] = round(R0[i][j], 2)
kxtab = [round(kx[i]*1000, 2) for i in range(6)]
skxtab = [round(skx[i]*1000, 2) for i in range(6)]
#print(tabulate(Ktab+R0tab, tablefmt="fancy_grid"))
#print(tabulate([T]+[kxtab]+[skxtab], tablefmt="fancy_grid"))
print(al, 1000*al*(k1[2]/k1[0]+k1[3]/k1[1]))