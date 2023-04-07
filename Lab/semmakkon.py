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

def sred(l):
    n = len(l)
    N = n if n>=10 else n-1
    s = sum(l)/n
    x = 0
    for i in l:
        x+=(i-s)**2
    sx = (x/N)**0.5
    return ([s, sx])


def linGraf(X, Y, Xerr = None, Yerr = None, tipe = [0], plsize = 1, fcolor = None, OXname = None, OYname = None, name = None, left = None, right = None, flabel = None, form = ''):
    Label = flabel
    if 0 in tipe:
        fig, ax = plt.subplots()
        ax.set(title = name, xlabel = OXname, ylabel = OYname)
    plt.errorbar(X, Y, xerr=Xerr, yerr=Yerr, ecolor = fcolor, c = fcolor, fmt = form, label = Label)
    K = MNK(X, Y)
    Right = right if right != None else max(X)
    Left = left if left != None else min(X)
    if 2 not in tipe:
        x = np.arange(Left, Right, (Right - Left)*0.0001)
        plt.plot(x, K[1]+K[0]*x, linewidth = plsize, color = fcolor, label = flabel)
    return(MNK(X, Y))

def reverseTab(l):
    n = len(l)
    m = len(l[0])
    tab = [[None for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            tab[j][i] = l[i][j]
    return tab

def plotEL(A, B):
    x = np.arange(-(1/A)**0.5, (1/A)**0.5, 0.00001)
    plt.plot(x, ((1-A*x**2)/B)**0.5, color = 'b')
    plt.plot(x, -((1-A*x**2)/B)**0.5, color = 'b')

def plotELd(A, B, C):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    '''
    x = np.arange(-(1 / A) ** 0.5, (1 / A) ** 0.5, 0.00001)
    plt.plot(x, ((1 - A * x ** 2) / B) ** 0.5, 0*x, color='b')
    plt.plot(x, -((1 - A * x ** 2) / B) ** 0.5, 0*x, color='b')
    '''
    z = np.linspace(-(1 / C) ** 0.5, (1 / C) ** 0.5, 20)
    for c in z:
        a = (A**2+(c/C*A)**2)**0.5
        b = (B**2+(c/C*B)**2)**0.5

        plotEL3d(a, b, c)


def plotEL3d(A, B, C):
    x = np.linspace(-(1 / A) ** 0.5, (1 / A) ** 0.5, 10)
    plt.plot(x, ((1 - A * x ** 2) / B) ** 0.5, 0 * x + C, color='b')
    plt.plot(x, -((1 - A * x ** 2) / B) ** 0.5, 0 * x + C, color='b')

def Elips(A, B, n=100, fcolor='b'):
    x = np.linspace(-A, A, n)
    plt.plot(x, B * (1 - x ** 2 / A ** 2) ** 0.5, color=fcolor)
    plt.plot(x, -B * (1 - x ** 2 / A ** 2) ** 0.5, color=fcolor)
def ZElips3d(A, B, C, n=50, fcolor='b'):
    x = np.linspace(-A, A, n)
    plt.plot(x, B * (1 - x ** 2 / A ** 2) ** 0.5, x*0 + C, color=fcolor)
    plt.plot(x, -B * (1 - x ** 2 / A ** 2) ** 0.5, x*0 + C, color=fcolor)

def YElips3d(A, B, C, n=50, fcolor='b'):
    x = np.linspace(-A, A, n)
    plt.plot(x, x*0 + B, C * (1 - x ** 2 / A ** 2) ** 0.5, color=fcolor)
    plt.plot(x, x*0 + B, -C * (1 - x ** 2 / A ** 2) ** 0.5, color=fcolor)

def XElips3d(A, B, C, n=50, fcolor='b'):
    y = np.linspace(-B, B, n)
    plt.plot(y*0 + A, y, C * (1 - y ** 2 / B ** 2) ** 0.5, color=fcolor)
    plt.plot(y*0 + A, y, -C * (1 - y ** 2 / B ** 2) ** 0.5, color=fcolor)

def ZWayElipsoid(A, B, C, n=5):
    z = np.linspace(-C, C, n)
    for c in z:
        a = (A ** 2 - (c / C * A) ** 2) ** 0.5
        b = (B ** 2 - (c / C * B) ** 2) ** 0.5
        ZElips3d(a, b, c)

def YWayElipsoid(A, B, C, n=5):
    y = np.linspace(-B, B, n)
    for b in y:
        a = (A ** 2 - (b / B * A) ** 2) ** 0.5
        c = (C ** 2 - (b / B * C) ** 2) ** 0.5
        YElips3d(a, b, c)

def XWayElipsoid(A, B, C, n=5):
    x = np.linspace(-A, A, n)
    for a in x:
        b = (B ** 2 - (a / A * B) ** 2) ** 0.5
        c = (C ** 2 - (a / A * C) ** 2) ** 0.5
        XElips3d(a, b, c)

def Elipsoid(A, B, C, n=5):
    XWayElipsoid(A, B, C, n=n)
    YWayElipsoid(A, B, C, n=n)
    ZWayElipsoid(A, B, C, n=n)

def ZHiperbaloid(A, B, C, n=10):
    z = np.linspace(-C, C, n)
    for c in z:
        a = (A ** 2 + (c / C * A) ** 2) ** 0.5
        b = (B ** 2 + (c / C * B) ** 2) ** 0.5
        ZElips3d(a, b, c)


