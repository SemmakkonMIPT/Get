import matplotlib.pyplot as plt
import numpy as np
from semmakkon import *

Uzag = 194 #Вольт


n = [2, 3, 4]

Ur = [34.3, 32.3, 31.5, 30.6, 27.6, 25.3, 23.5, 22.9, 22.4, 21.7] #Вольт
Ir = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5] #мА

Rdif = (32.3-31.5)/(1-1.5)
print(Rdif)


if 1 in n:
    fig, ax = plt.subplots()
    linGraf(Ur, Ir, tipe=[2], ms=3)
    #k = linGraf(LinT1u, LinP1u, form='.', tipe=[], ms=3, plsize=1.txt.5)
    ax.set(title='Вольт-амперная характеристика разряда  $I_{р}(U_{р})$',
           xlabel='Напряжение разряда U, В', ylabel='Ток через разряд I, мА')
Uz = [[[], []], [[], []], [[], []]]
Iz = [[[], []], [[], []], [[], []]]
Uz[0][0] = [25, 22, 19, 16, 13, 10, 8, 6, 4, 2, 0.5] #Вольт
Iz[0][0] = ([100, 97, 94, 90.5, 84.2, 74, 64.3, 52, 37.7, 23, 10]) #мкА

Uz[0][1] = [25, 22, 19, 16, 13, 10, 8, 6, 4, 2, 0.5][::-1] #Вольт
Iz[0][1] = [33, 44.7, 60, 73, 84, 93, 102.4, 108.4, 112.3, 115.4, 118.4]

k = MNK([100, 97], [25, 22])

Uz[1][0] = [25, 22, 19, 16, 13, 10, 8, 6, 4, 2] #Вольт
Iz[1][0] = [51.3, 49.6, 47.8, 46, 43.5, 38.7, 33.4, 26, 17, 5.5] #мкА

Uz[1][1] = [25, 22, 19, 16, 13, 10, 8, 6, 4, 2][::-1] #Вольт
Iz[1][1] = [24, 34.6, 43, 49.5, 54, 58.2, 60.9, 62.9, 64.9, 66.9] #мкА

Uz[2][0] = [25, 22, 19, 16, 13, 10, 8, 6, 4, 2] #Вольт
Iz[2][0] = [20.5, 19.9, 19.3, 18.6, 17.8, 16, 13.8, 10.8, 6.6, 1] #мкА

Uz[2][1] = [25, 22, 19, 16, 13, 10, 8, 6, 4, 2][::-1] #Вольт
Iz[2][1] = [11.5, 16.2, 20, 22.6, 24.5, 26.1, 27.4, 28.5, 29.5, 30.7] #мкА

U = [[] for i in range(3)]
I = [[] for i in range(3)]

for i in [0, 1, 2]:
    I[i] = toArray(Iz[i][0]+list(-toArray(Iz[i][1])))
    U[i] = toArray(Uz[i][0]+list(-toArray(Uz[i][1])))
print(U)
print(I)
for i in [0, 1, 2]:
    z = sum(I[i]) / len(I[i])
    print(z)
    I[i] -= z
Iin = [0, 0, 0]

for i in [0, 1, 2]:
    Iin[i] = MNK(U[i][0:3], I[i][0:3])[1]

print(Iin)





if 2 in n:
    fig, ax = plt.subplots()
    linGraf(U[0], I[0], tipe=[2], ms=3, flabel='I = 5 мA')
    osiKord(U[0], I[0])
    plt.plot([U[0][0], 0], [I[0][0], Iin[0]], color='k', ls = '--')
    plt.plot([-U[0][0], 0], [-I[0][0], -Iin[0]], color='k', ls = '--')
    ax.set(title='Вольт-амперная характеристика зонда  $I_{р}(U_{р})$',
           xlabel='Напряжение на зонде U, В', ylabel='Ток через зонд I, мк А')

if 3 in n:
    linGraf(U[1], I[1], tipe=[2], ms=3, flabel='I = 3 мA')
    osiKord(U[1], I[1])
    plt.plot([U[1][0], 0], [I[1][0], Iin[1]], color='k', ls='--')
    plt.plot([-U[1][0], 0], [-I[1][0], -Iin[1]], color='k', ls='--')
if 4 in n:
    linGraf(U[2], I[2], tipe=[2], ms=3, flabel='I = 1.txt.5 мA')
    osiKord(U[2], I[2])
    plt.plot([U[2][0], 0], [I[2][0], Iin[2]], color='k', ls='--')
    plt.plot([-U[2][0], 0], [-I[2][0], -Iin[2]], color='k', ls='--')
    plt.legend()
if 5 in n:
    plt.plot(Uz[1][1], Iz[1][1])
if 6 in n:
    plt.plot(Uz[2][0], Iz[2][0])
if 7 in n:
    plt.plot(Uz[2][1], Iz[2][1])
plt.show()