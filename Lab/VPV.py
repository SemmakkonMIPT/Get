import matplotlib.pyplot as plt
import numpy as np
from semmakkon import *

#Данные
#50г воды
T = [[], [], [], [], []]
T[0] = [22.7, 23.3, 24.1, 24.5, 24.6, 24.6, 24.9, 25.2, 25.8,
        26.3, 26.8, 27.3, 27.5, 27.6, 27.7, 27.7, 27.7, 27.8,
        27.9, 28.4, 28.5, 28.7, 28.8, 28.9]
T[1] = [23.2, 24.5, 25.3, 25.6, 26.0, 26.5,
        26.9, 27.5, 27.9, 28.5, 29.2, 29.6, 29.9]
T[2] = [23.4, 24.1, 24.4, 25.3, 25.7, 26.0, 26.4,
        26.8, 27.2, 27.8, 28.1, 28.4, 28.9, 29.6,
        30.3, 30.5, 31.1, 31.5, 31.7, 32.2]
T[3] = [24.6, 25.3, 26.3, 27.8, 29.6, 30.5]

T[4] = [22.5, 27.9, 35.3, 42.3, 49, 55, 62.6, 66.9, 72.8, 77.8]
T[4] = [26.7, 33.4, 41.5, 52.8, 61.9, 68.5, 76.6]
#время
t = [[], [], [], [], []]
t[0] = [5*i for i in range(len(T[0]))]
t[1] = [10*i for i in range(len(T[1]))]
t[2] = [10*i for i in range(len(T[2]))]
t[3] = [10*i for i in range(len(T[3]))]
t[4] = [10*i for i in range(len(T[4]))]

k = [1, 1, 1, 1, 1]
k[1]=MNK(t[1][2:], T[1][2:])[0]
k[2]=MNK(t[2], T[2])[0]
k[3]=MNK(t[3], T[3])[0]
k[4]=MNK(t[4], T[4])[0]
k[0]=MNK(t[0][5:11], T[0][5:11])[0]
print(k)

#Рассчеты:
С = 4200
N = [1, 1, 1, 1, 1]
N[1] = k[1]*0.075*4200
N[3] = k[3]*0.075*4200
N[2] = k[2]*0.1*4200
N[0] = k[0]*0.05*4200
N[4] = k[4]*0.005*4200
print(N)

#Графики:
n = [4, 5]
if 1 in n:
    fig, ax = plt.subplots()
    linGraf(t[0], T[0], form = '.', tipe = [2], ms = 6)
    k = linGraf(t[0][5:11], T[0][5:11], form='.', tipe=[], gsize = t[0], ms = 6)
    ax.set(title='Зависимость температуры воды от времени $T(t)$',
           xlabel='Время от начала измерений t, с', ylabel='$Температура T,°С$')
    ax.grid()
if 2 in n:
    fig, ax = plt.subplots()
    linGraf(t[1], T[1], form = '.', tipe = [2], ms = 6)
    k = linGraf(t[1][2:], T[1][2:], form='.', tipe=[], gsize = t[1], ms = 6)
    ax.set(title='Зависимость температуры воды от времени $T(t)$',
           xlabel='Время от начала измерений t, с', ylabel='$Температура T,°С$')
    ax.grid()
if 3 in n:
    fig, ax = plt.subplots()
    linGraf(t[2], T[2], form = '.', tipe = [2], ms = 6)
    k = linGraf(t[2], T[2], form='.', tipe=[], gsize = t[2], ms = 6)
    ax.set(title='Зависимость температуры воды от времени $T(t)$',
           xlabel='Время от начала измерений t, с', ylabel='$Температура T,°С$')
    ax.grid()
if 4 in n:
    fig, ax = plt.subplots()
    linGraf(t[3], T[3], form = '.', tipe = [2], ms = 6)
    k = linGraf(t[3], T[3], form='.', tipe=[], gsize = t[3], ms = 6)
    ax.set(title='Зависимость температуры воды от времени $T(t)$',
           xlabel='Время от начала измерений t, с', ylabel='$Температура T,°С$')
    ax.grid()
if 5 in n:
    fig, ax = plt.subplots()
    linGraf(t[4], T[4], form = '.', tipe = [2], ms = 6)
    k = linGraf(t[4], T[4], form='.', tipe=[], gsize = t[4], ms = 6)
    ax.set(title='Зависимость температуры воды от времени $T(t)$',
           xlabel='Время от начала измерений t, с', ylabel='$Температура T,°С$')
    ax.grid()

plt.show()