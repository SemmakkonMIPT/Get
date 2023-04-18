import matplotlib.pyplot as plt
from semmakkon import *
import numpy as np

def fun1(x, y):
    try:
        a = x*y
        return(a)
    except ZeroDivisionError:
        return(0)
def fun2(x, y):
    try:
        a = -5
        return(a)
    except ZeroDivisionError:
        return(0)
def fun3(x, y):
    try:
        a = 10
        return (a)
    except ZeroDivisionError:
        return (0)

n = [1]
if 1 in n:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ArrPlot((Graf3dArr(10, 10, fun1, n = 20)))
    #ArrPlot(AllSwaps(Graf3dArr(10, 10, fun2, -10, -10, n = 10)))
    #ArrPlot(Graf3dArr(10, 10, fun2))
    plt.show()
elif 2 in n:
    fun3(1, 1, fun1)