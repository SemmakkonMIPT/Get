import matplotlib.pyplot as plt
from math import *
from semmakkon import *
import numpy as np

ro = 885
P = 1.1*10**-2
h1 = 39.9
h2 = 13.3
h1f = 36.5
h2f = 17.3
dh1 = h1-h2
sh1=sh2=sh3=sh4 = 0.05
h3 = 35.4
h4 = 18.4
h = (h1+h2)/2
h1n = (h+dh1/2*1.05)
h2n = (h-dh1/2*1.05)
#print(h1n, h2n)
dh2 = h3-h4
h3n = (h+dh2/2*1.05)
h4n = (h-dh2/2*1.05)
#print(h3n, h4n)
P0torr =  746.7
P0 = P0torr*133.3
P1 = dh1*10*ro*10**-2
P2 = dh2*10*ro*10**-2
V0 = 50*10**-6
V1 = V0*P0/P1-V0
#print(V1*10**6*1.05)
V2 = V0*P0/P2
#print((V2-V1-V0)*10**6*1.05)
Ppr = 1.1*10**-4
Ppr = 7.5*10**-5
Pust = 1.3*10**-4
Pfv = 2.7*10**-3
Pprv = 8.5*10**-5

P1 = np.array([6, 5.8, 5.4, 4.6, 3.8, 3, 2.5, 2.1, 1.8, 1.5, 1.4, 1.2, 1.1, 1.05, 0.99, 0.95, 0.91, 0.88, 0.86, 0.84, 0.83, 0.82, 0.81, 0.8, 0.79, 0.78, 0.77, 0.76])
t1 = [i for i in range(len(P1))]
t1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 27, 32, 41]

Ppr1 = np.array([Ppr for i in P1])
P_P1 = P1-Ppr1*10**4
lnP_P1 = np.log(P_P1)

P2 = np.array([610, 600, 560, 480, 400, 320, 260, 220, 190, 160, 150, 140, 130, 120, 110, 103, 99, 97, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86])/100
t2 = [i for i in range(len(P2))]
t2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24, 27, 30, 35, 41, 49]

Ppr2 = np.array([Pprv for i in P2])
P_P2 = P2-Ppr2*10**4
lnP_P2 = np.log(P_P2)

plt.scatter(t1, lnP_P1)
plt.scatter(t2, lnP_P2)

plt.show()



