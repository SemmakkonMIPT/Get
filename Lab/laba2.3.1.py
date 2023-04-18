import matplotlib.pyplot as plt
import numpy as np
from semmakkon import *

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
Ppr1 = 7.5*10**-5

Pust = 1.3*10**-4
Pfv = 2.7*10**-3
Ppr2 = 8.5*10**-5

P1 = np.array([6, 5.8, 5.4, 4.6, 3.8, 3, 2.5, 2.1, 1.8, 1.5, 1.4, 1.2, 1.1, 1.05, 0.99, 0.95, 0.91,
               0.88, 0.86, 0.84, 0.83, 0.82, 0.81, 0.8, 0.79, 0.78, 0.77, 0.76])
t1 = [i for i in range(len(P1))]
t1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 27, 32, 41]

P_P1 = P1-Ppr1*10**4
lnP_P1 = np.log(P_P1)

st1 = [0.5 for i in t1]
sP1 = np.array([0.05 if p>=1 else 0.005 for p in P1])
sP_P1 = sP1+0.005
slnP_P1 = [sP_P1[i]/P_P1[i] for i in range(len(P_P1))]

P2 = np.array([610, 600, 560, 480, 400, 320, 260, 220, 190, 160, 150, 140, 130, 120, 110, 103, 99,
               97, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86])/100
t2 = [i for i in range(len(P2))]
t2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24, 27, 30, 35, 41, 49]

P_P2 = P2-Ppr2*10**4
lnP_P2 = np.log(P_P2)

st2 = [0.5 for i in t2]
sP2 = np.array([0.05 if p>=1 else 0.005 for p in P2])
sP_P2 = sP2+0.005
slnP_P2 = [sP_P2[i]/P_P2[i] for i in range(len(P_P2))]

P1u = np.array([77, 81, 88, 97, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250,
                260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430,
                440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610])/100
P1n = np.concatenate([P1u, [10*i for i in range(41, 61)]])
t1u = [i for i in range(len(P1u))]
t1u = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30,
       31, 33, 34, 35, 36, 38, 39, 40, 42, 43, 44, 45, 47, 48, 49, 50, 52, 53, 54, 55, 57, 58, 59, 61, 63, 64]
t1un = t1u + [i for i in range(t1u[-1]+1, t1u[-1]+1+len(P1u)-len(t1u))]

st1u = [0.5 for i in t1u]
sP1u = np.array([0.05 if p>=1 else 0.005 for p in P1u])

P2u = np.array([83, 120, 190, 250, 300, 350, 400, 440, 490, 530, 580, 610])/100
t2u = list(np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])-25)

st2u = [0.5 for i in t2u]
sP2u = np.array([0.05 if p>=1 else 0.005 for p in P2u])


n = [1, 2, 3, 4]
if 1 in n:
    fig, ax = plt.subplots()
    linGraf(t1, lnP_P1, st1, slnP_P1, form = '.', tipe = [2], ms = 6)
    LinT1 = t1[4: -4]
    LinLnP_P1 = lnP_P1[4: -4]
    k = linGraf(LinT1, LinLnP_P1, form='.', tipe=[], gsize = t1, ms = 6)
    ax.set(title='Зависимость логарифма давления от времени $ln(P-P_{пр})(t)$',
           xlabel='Время от начала измерений t, с', ylabel='Логарифм разности давлений $ln(P-P_{пр})(t)$, $ln(торр)$')
    ax.grid()
if 1.1 in n:
    fig, ax = plt.subplots()
    linGraf(t1, lnP_P1, st1, slnP_P1, form = 's', tipe = [2], ms = 4, fcolor = 'g')
    LinT1 = t1[5: -4]
    LinLnP_P1 = lnP_P1[5: -4]
    k = linGraf(LinT1, LinLnP_P1, form='.', tipe=[], gsize = t1, ms = 6, fcolor = 'r')
    ax.set(title='Зависимость $ln(P-P_{пр})(t)$',
           xlabel='Время t, с', ylabel='Логарифм давления $ln(P-P_{пр})(t)$, $ln(торр)$')
if 2 in n:
    fig, ax = plt.subplots()
    linGraf(t2, lnP_P2, st2, slnP_P2, form='.', tipe=[2], ms=6)
    LinT2 = t2[3: -5]
    LinLnP_P2 = lnP_P2[3: -5]
    k = linGraf(LinT2, LinLnP_P2, form='.', tipe=[], gsize=t1, ms=6)
    ax.set(title='Зависимость логарифма давления от времени $ln(P-P_{пр})(t)$',
           xlabel='Время от начала измерений t, с', ylabel='Логарифм разности давлений $ln(P-P_{пр})(t)$, $ln(торр)$')
    ax.grid()
if 2.1 in n:
    fig, ax = plt.subplots()
    linGraf(t2, lnP_P2, st2, slnP_P2, form='s', tipe=[2], ms=4, fcolor='g')
    LinT2 = t2[3: -5]
    LinLnP_P2 = lnP_P2[3: -5]
    k = linGraf(LinT2, LinLnP_P2, form='.', tipe=[], gsize=t1, ms=6, fcolor='r')
    ax.set(title='Зависимость $ln(P-P_{пр})(t)$',
           xlabel='Время t, с', ylabel='Логарифм давления $ln(P-P_{пр})$, $ln(торр)$')
if 3 in n:
    fig, ax = plt.subplots()
    linGraf(t1u, P1u, st1u, sP1u, form='.', tipe=[2], ms=3)
    LinT1u = t1u[4:-3]
    LinP1u = P1u[4:-3]
    k = linGraf(LinT1u, LinP1u, form='.', tipe=[], gsize=t1u, ms=3, plsize=1.5)
    ax.set(title='Зависимость давления от времени $P(t)$',
           xlabel='Время от начала измерений t, с', ylabel='Давление $P$, $торр$')
    ax.grid()
if 3.1 in n:
    fig, ax = plt.subplots()
    linGraf(t1u, P1u, st1u, sP1u, form='s', tipe=[2], ms=2, fcolor = 'g')
    LinT1u = t1u[4:-3]
    LinP1u = P1u[4:-3]
    k = linGraf(LinT1u, LinP1u, form='.', tipe=[], gsize=t1u, ms=3, plsize=1.5, fcolor = 'r')
    ax.set(title='Зависимость $P(t)$',
           xlabel='Время t, с', ylabel='Давление $P$, $торр$')
if 4 in n:
    fig, ax = plt.subplots()
    linGraf(t2u, P2u, st2u, sP2u, form='.', tipe=[2], ms=3)
    LinT2u = t2u[1:-1]
    LinP2u = P2u[1:-1]
    print(t2u)
    k = linGraf(LinT2u, LinP2u, form='.', tipe=[], gsize = t2u,  ms=3, plsize=1.5)
    ax.set(title='Зависимость давления от времени $P(t)$',
           xlabel='Время от начала измерений t, с', ylabel='Давление $P$, $торр$')
    ax.grid()
if 4.1 in n:
    fig, ax = plt.subplots()
    linGraf(t2u, P2u, st2u, sP2u, form='s', tipe=[2], ms=2, fcolor='g')
    LinT2u = t2u[1:-1]
    LinP2u = P2u[1:-1]
    k = linGraf(LinT2u, LinP2u, form='.', tipe=[], gsize=t2u, ms=3, plsize=1.5, fcolor='r')
    ax.set(title='Зависимость $P(t)$',
           xlabel='Время t, с', ylabel='Давление $P$, $торр$')
if 5 in n:
    plt.scatter(t1, P1)
if 6 in n:
    plt.scatter(t2, P2)
if 8 in n:
    plt.scatter(t2u, P2u)


plt.show()



