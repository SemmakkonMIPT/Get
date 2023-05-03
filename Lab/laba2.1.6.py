import matplotlib.pyplot as plt
import numpy as np
from semmakkon import *
U0_20c = 4*10**-6 #В
U0_30c = -2*10**-6 #В
U0_40c = -6*10**-6 #В
U0_50c = -8*10**-6 #В
T = np.array([20, 30, 40, 50])+273
Tts_20c = np.array([20.3, 20.45, 20.55, 20.72, 20.83])
Tts_30c = np.array([30.1, 30.1, 30.1, 30.11, 30.12])
Tts_40c = np.array([40.07, 40.04, 40.03, 40.01])
Tts_50c = np.array([50.05, 50.05, 50.05, 50.03])
P = np.array([4, 3.5, 3, 2.5, 2]) #Атм
sP = 6/100
Pk = np.array([4, 3.5, 3, 2.5]) #Атм
U_20c = np.array([-0.174, -0.151, -0.121, -0.09, -0.07])/10**3-U0_20c
U_30c = np.array([-0.164, -0.140, -0.114, -0.089, -0.066])/10**3-U0_30c
U_40c = np.array([-0.155, -0.131, -0.106, -0.084])/10**3-U0_40c
U_50c = (np.array([-0.155, -0.129, -0.100, -0.08])*0.95)/10**3-U0_50c
allTV = np.array([39.1, 39.8, 40.7, 41.5, 42.4, 43.2])*10**-6
TV = np.array([(allTV[1]+allTV[2])/2, (allTV[2]+allTV[3])/2, (allTV[3]+allTV[4])/2, (allTV[4]+allTV[5])/2])
dT_20c = -U_20c/TV[0]
dT_30c = -U_30c/TV[1]
dT_40c = -U_40c/TV[2]
dT_50c = -U_50c/TV[3]
sU = 2*10**-6
sT = sU/TV

m = ([0 for i in range(4)])
sm = ([0 for i in range(4)])
m[0], sm[0] = MNK(P, dT_20c)[0]/10**5, MNK(P, dT_20c)[2]/10**5
m[1], sm[1] = MNK(P, dT_30c)[0]/10**5, MNK(P, dT_30c)[2]/10**5
m[2], sm[2] = MNK(Pk, dT_40c)[0]/10**5, MNK(Pk, dT_40c)[2]/10**5
m[3], sm[3] = MNK(Pk, dT_50c)[0]/10**5, MNK(Pk, dT_50c)[2]/10**5
m = np.array(m)
sm = np.array(sm)

ro = 44
R = 8.31
Cp = 4*R
a1 = (m[0]-m[1])*Cp*R*T[0]*T[1]/2/(T[1]-T[0])
a2 = (m[2]-m[3])*Cp*R*T[2]*T[3]/2/(T[3]-T[2])
b1 = Cp*(m[1]*T[1]-m[0]*T[0])/(T[0]-T[1])
b2 = Cp*(m[3]*T[3]-m[2]*T[2])/(T[2]-T[3])
T_1 = 1/T
sTt = 0.01
sT_1 = T_1*sTt/T
k = MNK(T_1, m)
a = k[0]*R*Cp/2
sa = a*k[2]/k[0]
b = -k[1]*Cp
sb = -b*k[3]/k[1]
Ti = 2*a/R/b
sTi = Ti*(sa/a+sb/b)
print(a, sa, b, sb, Ti, sTi, 'a, sa, b, sb, Ti, sTi')

n = [1, 2]
c1 = ['r', 'orange', 'y', 'g', 'b', 'm' ]
c2 = [c1[i] for i in range(5, -1, -1)]
if 1 in n:
    fig, ax = plt.subplots()
    #linGraf(P, dT_20c, sP, sT[0], form = '.', tipe = [2], ms = 6, fcolor = c1[0])
    k = [0 for i in range(4)]
    k[0] = linGraf(P, dT_20c, sP, sT[0], form='.', tipe=[], gsize = P, ms = 6, fcolor = c1[0], flabel = '20°C')
    k[1] = linGraf(P, dT_30c, sP, sT[1], form='.', tipe=[], gsize = P, ms = 6, fcolor = c1[1], flabel = '30°C')
    k[2] = linGraf(Pk, dT_40c, sP, sT[2], form='.', tipe=[], gsize = P, ms = 6, fcolor = c1[2], flabel = '40°C')
    k[3] = linGraf(Pk, dT_50c, sP, sT[3], form='.', tipe=[], gsize = P, ms = 6, fcolor = c1[3], flabel = '50°C')
    ax.set(title='Зависимость повышения температуры от давления $\Delta T(\Delta p)$',
           xlabel='Повышение температуры $\Delta T, °C$', ylabel='Давление $P, Атм$')
    ax.legend()
    ax.grid()
if 1.1 in n:
    fig, ax = plt.subplots()
    linGraf(P, dT_20c, form = 's', tipe = [2], ms = 4, fcolor = 'g')
    k = linGraf(P, dT_20c, form='.', tipe=[], gsize = P, ms = 6, fcolor = 'r')
    ax.set(title='Зависимость $ln(P-P_{пр})(t)$',
           xlabel='Время t, с', ylabel='Логарифм давления $ln(P-P_{пр})(t)$, $ln(торр)$')
if 2 in n:
    fig, ax = plt.subplots()
    # linGraf(P, dT_20c, sP, sT[0], form = '.', tipe = [2], ms = 6, fcolor = c1[0])
    k = linGraf(T_1*10**5, m*10**5, sT_1*10**5, sm*10**5, form='.', tipe=[], ms=6, fcolor=c1[0])
    ax.set(title='Зависимость коэффициента Дж.Том. от обратной температуры $\mu(1/{T})$',
           xlabel='Обратная температура $1/T, K^{-1} \cdot 10^{-5}$', ylabel='Коэффициент Джоуля-Томсона $\mu, K/Атм \cdot 10^{-5}$')
    ax.grid()


plt.show()