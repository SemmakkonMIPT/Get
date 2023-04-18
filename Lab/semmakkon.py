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


def linGraf(X, Y, Xerr = None, Yerr = None, tipe = [0], plsize = 1, fcolor = None, OXname = None,
            OYname = None, name = None, gsize = None,  flabel = None, form = '', ms = 5,
            grid = True, mnkcolor = None, ecolor = None):
    Label = flabel
    if 0 in tipe:
        fig, ax = plt.subplots()
        ax.set(title = name, xlabel = OXname, ylabel = OYname)
        if grid:
            ax.grid()
    plt.errorbar(X, Y, xerr=Xerr, yerr=Yerr, ecolor = ecolor if ecolor!=None else fcolor,
                 c = fcolor, fmt = form, label = Label, ms = ms)
    K = MNK(X, Y)

    Right = max(gsize) if gsize != None else max(X)
    Left = min(gsize) if gsize != None else min(X)
    MNKcolor = mnkcolor if mnkcolor != None else fcolor
    if 2 not in tipe:
        x = np.arange(Left, Right, (Right - Left)*0.0001)
        plt.plot(x, K[1]+K[0]*x, linewidth = plsize, color = MNKcolor, label = flabel)
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

def dotEllArrZ(A, B, C, n=5):
    x = np.linspace(-A/2**0.5, A/2**0.5, n)
    y = np.linspace(-B/2**0.5, B/2**0.5, n)
    Y = np.concatenate([B * (1 - x ** 2 / A ** 2) ** 0.5, -B * (1 - x ** 2 / A ** 2) ** 0.5, y, y])
    X = np.concatenate([x, x, A * (1 - y ** 2 / B ** 2) ** 0.5, -A * (1 - y ** 2 / B ** 2) ** 0.5])
    Z = np.ones(4*n)*C
    Arr = np.array([X, Y, Z])
    return Arr

def RaddotEllArrZ(A, B, C, n=5):
    F = np.linspace(0, 2*pi, 4*n)
    X = np.cos(F)*A
    Y = np.sin(F)*B
    Z = np.ones(4 * n) * C
    Arr = np.array([X, Y, Z])
    return Arr

def dotEllZ(A, B, C, n=5, fcolor = 'b'):
    Arr = dotEllArrZ(A, B, C, n)
    plt.plot(Arr[0], Arr[1], Arr[2], color = fcolor, linestyle = ' ', marker = '.', markeredgewidth = 0.1)
def dotEllidArrZ(A, B, C, n=5, m=10):
    z = np.linspace(-C, C, m)
    Arr = np.array([[0, 0], [0, 0], [C, -C]])
    X = dotEllArrZ(A, B, 0, n)[0]
    Y = dotEllArrZ(A, B, 0, n)[1]
    for c in z:
        a = (A ** 2 - (c / C * A) ** 2) ** 0.5
        b = (B ** 2 - (c / C * B) ** 2) ** 0.5
        newArr = dotEllArrZ(a, b, c, n)
        Arr = np.hstack([Arr, newArr])
    return Arr

def RaddotEllidArrZ(A, B, C, n=5, m=10):
    z = np.linspace(0, pi, m)
    Arr = np.array([[0, 0], [0, 0], [C, -C]])
    X = RaddotEllArrZ(A, B, 0, n)[0]
    Y = RaddotEllArrZ(A, B, 0, n)[1]
    for c in z:
        a = np.sin(c)*A
        b = np.sin(c)*B
        newArr = dotEllArrZ(a, b, cos(c)*C, n)
        Arr = np.hstack([Arr, newArr])
    return Arr

def dotEllidZ(A, B, C, n=5, m=7, fcolor = 'b'):
    Arr = dotEllidArrZ(A, B, C, n=n, m=m)
    plt.plot(Arr[0], Arr[1], Arr[2], color = fcolor, linestyle = ' ', marker = '.', markeredgewidth = 0.1)

def dotEllidY(A, B, C, n=5, m=10, fcolor = 'b'):
    Arr = dotEllidArrZ(A, C, B, n=5, m=10)
    plt.plot(Arr[0], Arr[2], Arr[1], color = fcolor, linestyle = ' ', marker = '.', markeredgewidth = 0.1)

def ArrPlot(Arr, fcolor = 'b', O = [0, 0, 0]):
    plt.plot(Arr[0]+O[0], Arr[1]+O[1], Arr[2]+O[2], color=fcolor, linestyle=' ', marker='.', markeredgewidth=0.1)

def makeMash(n):
    Arr = np.array([[n, n, n, n, -n, -n, -n, -n], [n, n, -n, -n, n, n, -n, -n], [n, -n, n, -n, n, -n, n, -n]])
    print(Arr)
    ArrPlot(Arr)

def Graf3dArr(A, B, fun, C = None, D = None, n = 10):
    if C==None: c = -A
    else: c = C
    if D==None: d = -B
    else: d = D
    X = np.linspace(c, A, n)
    Y = np.linspace(d, B, n)
    Arr = np.array([[], [], []])
    for x in X:
        for y in Y:
            newArr = np.array([[x], [y], [fun(x, y)]])
            Arr = np.hstack([Arr, newArr])
    return Arr

def swapXZ(Arr):
    newArr = np.array([Arr[2], Arr[1], Arr[0]])
    return newArr

def swapYZ(Arr):
    newArr = np.array([Arr[0], Arr[2], Arr[1]])
    return newArr
def swapXY(Arr):
    newArr = np.array([Arr[1], Arr[0], Arr[2]])
    return newArr

def AllSwaps(Arr):
    newArr = Arr
    newArr = np.hstack([newArr, swapXY(Arr)])
    newArr = np.hstack([newArr, swapXZ(Arr)])
    newArr = np.hstack([newArr, swapYZ(Arr)])
    return newArr

