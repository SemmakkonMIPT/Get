'''import matplotlib.pyplot as plt
from math import *
import numpy as np
from tabulate import tabulate
'''
from semmakkon import *
from tabulate import *

g = 9.8
#цена деления 0.05 мм
#диаметры измеренные
Dsd = [[42, 42, 42] for i in range(8)]
Dmd = [[16, 15, 16], [16, 16, 16], [17, 16, 16], [18, 18, 19], [16, 17, 16], [16, 16, 16], [12, 15, 16], [17, 18, 18]]
Ds = [42*0.00005 for i in range(8)]
Dm = [sred(j)[0]*0.00005 for j in Dmd]
Rs = [i/2 for i in Ds]
Rm = [i/2 for i in Dm]
eRs = 1/42/3
eRm = 1/16/3
#Расстояние падения
l = 0.2
#Время падения шариков
Ts = [[53.3, 53.4], [36.0, 35.9], [24.9, 24.8], [18.1, 17.3]]
Tm = [[67.2, 62.2], [45.7, 38.0], [34.4, 31.3], [27.8, 20.4]]
eTs = [[0.4/i for i in j] for j in Ts]
eTm = [[0.4/i for i in j] for j in Tm]
#Плотности
Ps = 2500
Pm = 7800
#Скорости
Vs = [[l/j for j in i] for i in Ts]
Vm = [[l/j for j in i] for i in Tm]
Vst = [Vs[i][j] for j in range(2) for i in range(4)]
Vmt = [Vm[i][j] for j in range(2) for i in range(4)]
#Плотность глицерина
Pg = [1259, 1255, 1252, 1249]
#вязкость
nsd = [[2/9*g*Rs[j+2*i]**2*(Ps-Pg[i])/Vs[i][j] for j in range(2)] for i in range(4)]
nmd = [[2/9*g*Rm[j+2*i]**2*(Pm-Pg[i])/Vm[i][j] for j in range(2)] for i in range(4)]
nsvd = [nsd[i][j] for j in range(2) for i in range(4)]
nmvd = [nmd[i][j] for j in range(2) for i in range(4)]
ensd = [[2*eRs+i for i in j] for j in eTs]
enmd = [[2*eRm+i for i in j] for j in eTm]
ns = [sred(i)[0] for i in nsd]
nm = [sred(i)[0] for i in nmd]
ens = [sred(i)[0] for i in ensd]
enm = [sred(i)[0] for i in enmd]
nsv = [i[0] for i in nsd]+[i[1] for i in nsd]
nmv = [i[0] for i in nmd]+[i[1] for i in nmd]
ensv = [i[0] for i in ensd]+[i[1] for i in ensd]
enmv = [i[0] for i in enmd]+[i[1] for i in enmd]
taus = [2/9*Rs[i]**2*Ps/nsvd[i] for i in range(8)]
taum = [2/9*Rs[i]**2*Ps/nmvd[i] for i in range(8)]
#температура
T = [i+273 for i in [25, 30, 35, 40]]
#массивы для графиков
lnns = [log(i) for i in ns]
lnnm = [log(i) for i in nm]
lnnsv = [log(i) for i in nsv]
lnnmv = [log(i) for i in nmv]
lnn = [sred([lnns[i], lnnm[i]])[0] for i in range(4)]
rT = [1/i for i in T]
rTg = [i*1000 for i in rT]
''''''
W_Ks = MNK(rT, lnns)[0]
W_Km = MNK(rT, lnnm)[0]
#print(W_Ks*1.txt.38/100)
#print(W_Km*1.txt.38/100)

n = [1.1, 2.1]
if(1 in n):
    A = linGraf(rTg, lnns, OXname= 'Обратная температура 1.txt/T, 1.txt/K $10^{-3}$', OYname=r'Нат. логорифм вязкости ln($\eta$)', name = r'Зависимость ln($\eta$)(1.txt/T) для стеклянных шариков', Yerr = ens, fcolor = 'b')
    print(A[0] * 13.8, A[2] * 13.8)
if(2 in n):
    A = linGraf(rTg, lnnm, OXname= 'Обратная температура 1.txt/T, 1.txt/K $10^{-3}$', OYname=r'Нат. логорифм вязкости ln($\eta$)', name = r'Зависимость ln($\eta$)(1.txt/T) для металлических шариков', Yerr = enm, fcolor = 'b')
    print(A[0] * 13.8, A[2] * 13.8)
if(3 in n):
    A = linGraf(rTg*2, lnns+lnnm, OXname='Обратная температура 1.txt/T, 1.txt/K $10^{-3}$', OYname=r'Нат. логорифм вязкости ln($\eta$)', name=r'Зависимость ln($\eta$)(1.txt/T) для всех шариков', Yerr=ens+enm, fcolor='b')
    #print(A[0] * 1000)
if(1.1 in n):
    A = linGraf(rTg*2, lnnsv, OXname= 'Обратная температура 1.txt/T, 1.txt/K $10^{-3}$', OYname=r'Нат. логорифм вязкости ln($\eta$)', name = r'Зависимость ln($\eta$)(1.txt/T) для стеклянных шариков', Yerr = ensv, fcolor = 'b')
    print(A[0] * 13.8, A[2] * 13.8)
    print(A[0], A[2])
if(2.1 in n):
    A = linGraf(rTg*2, lnnmv, OXname='Обратная температура 1.txt/T, 1.txt/K $10^{-3}$', OYname=r'Нат. логорифм вязкости ln($\eta$)',name=r'Зависимость ln($\eta$)(1.txt/T) для металлических шариков', Yerr=enmv, fcolor='b')
    print(A[0] * 13.8, A[2] * 13.8)
    print(A[0], A[2])

Tsv = []
for i in Ts:
    for j in i:
        Tsv+=[j]
Tsv = [Tsv]
Re = [1250*Vst[i]*0.055/nsvd[i] for i in range(8)]
Table = [Re]
if 4 in n:
    headers = ['d, цена деления']
    #print(tabulate(Dmd, tablefmt="fancy_grid", headers = headers))
    #print(tabulate([[i] for i in [i for i in range(1.txt, 9)]], tablefmt="fancy_grid", headers = ['Номер опыта']))
    #print(tabulate(Tsv, tablefmt="fancy_grid", headers = [i for i in range(1.txt, 9)]))
    #print(tabulate(None, tablefmt="fancy_grid", headers=None))
    print(tabulate(Table, tablefmt="fancy_grid", headers=[i for i in range(1, 9)]))


plt.show()