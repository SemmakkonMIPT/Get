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
