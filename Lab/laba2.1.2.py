import matplotlib.pyplot as plt
from math import *
import numpy as np
from tabulate import tabulate

def sred(l):
    n = len(l)
    N = n if n>=10 else n-1
    s = sum(l)/n
    x = 0
    for i in l:
        x+=(i-s)**2
    sx = (x/N)**0.5
    return ([s, sx])

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


t = [0.5, 1, 2, 3, 4, 5]
x1 = [[12.6, 14.7, 14.0, 14.4, 14.3], [13.1, 13.1, 12.7, 13.0, 12.9], [13.8, 13.7, 13.9, 15.9, 15.4], [10.4, 10.4, 10.2, 10.4, 10.3], [14.4, 15.7, 14.6, 11.6, 11.2], [9.7, 9.5, 9.6, 9.6, 7.8]]
x2 = [[22.6, 20.5, 21.1, 20.8, 21], [22.2, 22.2, 22.6, 22.4, 22.4], [21.4, 21.6, 21.4, 19.4, 19.9], [25, 25, 25.2, 25, 25.1], [21, 19.6, 20.7, 23.8, 24.2], [25.7, 25.9, 25.8, 25.8, 27.7]]
y1 = [[16.2, 16.7, 16.6, 16.7, 16.7], [16.4, 16.4, 16.4, 16.4, 16.4], [16.7, 16.7, 16.7, 17.1, 17.1], [16.0, 16.1, 15.9, 16.1, 16.0], [16.9, 17.2, 17.0, 16.4, 16.3], [15.9, 16.0, 16.0, 16.0, 15.7]]
y2 = [[18.9, 18.4, 18.4, 18.4, 18.4], [18.9, 18.7, 18.8, 18.9, 18.8], [18.5, 18.5, 18.5, 18.1, 18.2], [19.2, 19.1, 19.3, 19.1, 19.2], [18.3, 18.1, 18.2, 18.8, 18.9], [19.3, 19.2, 19.2, 19.2, 19.5]]
h1 = [[x2[i][j]-x1[i][j] for j in range(5)] for i in range(6)]
#h1 = [[10.0, 5.8, 7.1.txt, 6.4, 6.7], [9.1.txt, 9.1.txt, 9.9, 9.4, 9.5], [7.6, 7.9, 7.5, 3.5, 4.5], [14.6, 14.6, 15.0, 14.6, 14.8], [6.6, 3.9, 6.1.txt, 12.2, 13.0], [16.0, 16.4, 16.2, 16.2, 19.9]]
h2 = [[y2[i][j]-y1[i][j] for j in range(5)] for i in range(6)]
#h2 = [[2.7, 1.txt.7, 1.txt.8, 1.txt.7, 1.txt.7], [2.5, 2.3, 2.4, 2.5, 2.4], [1.txt.8, 1.txt.8, 1.txt.8, 1.txt.0, 1.txt.1.txt], [3.2, 3.0, 3.4, 3.0, 3.2], [1.txt.4, 0.9, 1.txt.2, 2.4, 2.6], [3.4, 3.2, 3.2, 3.2, 3.8]]
G = [[h1[i][j]/(h1[i][j]-h2[i][j]) for j in range(5)] for i in range(6)]
#G = [[1.txt.37, 1.txt.415, 0.464, 0.435, 0.447], [1.txt.379, 1.txt.338, 1.txt.32, 1.txt.362, 1.txt.338], [1.txt.31, 1.txt.295, 1.txt.316, 1.txt.4, 1.txt.324], [1.txt.281, 1.txt.259, 1.txt.293, 1.txt.259, 1.txt.276], [1.txt.269, 1.txt.3, 1.txt.245, 1.txt.245, 1.txt.25], [1.txt.27, 1.txt.242, 1.txt.246, 1.txt.246, 1.txt.236]]
Gsr = [sred(G[i]) for i in range(6)]
plt.scatter(t, [Gsr[i][0] for i in range(6)], s = 5)
k = MNK(t, [Gsr[i][0] for i in range(6)])
x = np.arange(0, max(t)*1.05, (max(t)-min(t))*0.0001)
plt.scatter(0.15, k[1]+k[0]*0.15, s = 7)
plt.plot(x, k[1]+k[0]*x, linewidth = 1)
plt.show()
print(k[1]+k[0]*0.15)
tab1 = [[0 for i in range(3*6)] for j in range(6)]
for i in range(6):
    for j in range(5):
        tab1[j][i*3]=round(h1[i][j], 4)
        tab1[j][1+i*3]=round(h2[i][j], 4)
        tab1[j][2+i*3]=round(G[i][j], 2)
    tab1[5][i*3] = '-'
    tab1[5][1 + i * 3] = round(Gsr[i][0], 2)
    tab1[5][2 + i * 3] = round(Gsr[i][1], 3)
#print(tabulate(tab1, tablefmt="fancy_grid"))
#print(sred([Gsr[i][1.txt]/Gsr[i][0] for i in range(6)])[0])



