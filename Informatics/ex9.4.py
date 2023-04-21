from collections import defaultdict
from heapq import heappop, heappush, heapify
import random
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np

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

    if gsize == None:
        Right, Left = max(X), min(X)
    else:
        Right, Left = max(gsize), min(gsize)

    MNKcolor = mnkcolor if mnkcolor != None else fcolor
    if 2 not in tipe:
        x = np.arange(Left, Right, (Right - Left)*0.0001)
        plt.plot(x, K[1]+K[0]*x, linewidth = plsize, color = MNKcolor, label = flabel)
    return(MNK(X, Y))

def prim(graph):
    mst = defaultdict(set)
    visited = {0}
    edges = [(cost, 0, to) for to, cost in graph[0].items()]
    heapify(edges)

    while edges:
        cost, frm, to = heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heappush(edges, (cost, to, to_next))

    return mst


def kruskal(graph):
    mst = defaultdict(set)
    edges = [(cost, frm, to) for frm, edges in graph.items() for to, cost in edges.items()]
    edges.sort()
    parent = {i: i for i in range(len(graph))}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        xroot = find(x)
        yroot = find(y)
        parent[xroot] = yroot

    for edge in edges:
        weight, frm, to = edge
        if find(frm) != find(to):
            union(frm, to)
            mst[frm].add(to)

    return mst


def compare_time(graph):
    import time
    start_time = time.time()
    prim(graph)
    prim_time = time.time() - start_time

    start_time = time.time()
    kruskal(graph)
    kruskal_time = time.time() - start_time

    return [prim_time, kruskal_time]


def generate_random_graph(n, max_weight):
    graph = defaultdict(dict)
    for i in range(n):
        for j in range(i + 1, n):
            weight = random.randint(1, max_weight)
            graph[i][j] = weight
            graph[j][i] = weight
    return graph


#Генерируем по 20 тестов с разным числом вершин и исследуем время работы
primTimes = []
kruskTimes = []
n0 = 50
nk = 400
dn = 50
N = list(range(n0, nk, dn))
print(f'Выполняем расчет для различных количеств вершин от {n0} до {nk} c шагом {dn}')
for n in N:
    times = [[], []]
    for i in range(1, 21):
        random_graph = generate_random_graph(n, 5000)
        time = compare_time(random_graph)
        times[0].append(time[0])
        times[1].append(time[1])
    primTimes.append(mean(times[0]))
    kruskTimes.append(mean(times[1]))
    print(f'{n:>2} done')
lnPrT = np.log(np.array(primTimes))
lnKrT = np.log(np.array(kruskTimes))
lnN = np.log(np.array(N))


fig, ax = plt.subplots()
plt.plot(N, primTimes)
plt.plot(N, kruskTimes)

fig, ax = plt.subplots()
kPr = linGraf(lnN, lnPrT, tipe=[])
kKr = linGraf(lnN, lnKrT, tipe=[])

print('По графикам в обычном и логарифмическом масштабе видно что зависимость степенная')
print(f'Степень сложности для алгоритма Прима: {round(kPr[0], 2)}, для алгоритма Краскала: {round(kKr[0], 2)}')

plt.show()



