import matplotlib.pyplot as plt
from math import *
from semmakkon import *
def f2l(str):
    f = open(str, 'r')
    f.readline()
    File = [l for l in f]
    Data = [l[:-2].split(',') for l in File]
    T = [float(l[0]) for l in Data]
    U = [float(l[1]) for l in Data]
    return T, U

P = [45, 90, 128, 165, 210]
Pnames = ['45 торр', '90 торр', '128 торр', '165 торр', '210 торр']

T45, U45 = f2l('Data/20230329_1680090859552_45.csv')
T90, U90 = f2l('Data/20230329_1680092347982_90.csv')
T128, U128 = f2l('Data/20230329_1680093463553_128.csv')
T165, U165 = f2l('Data/20230329_1680094585393_165.csv')
T210, U210 = f2l('Data/20230329_1680095654091_210.csv')
T = [T45, T90, T128, T165, T210]
U = [U45, U90, U128, U165, U210]

lnU45 = [log(U) for U in U45]
lnU90 = [log(U) for U in U90]
lnU128 = [log(U) for U in U128]
lnU165 = [log(U) for U in U165]
lnU210 = [log(U) for U in U210]
lnU = [lnU45, lnU90, lnU128, lnU165, lnU210]

V = 360*10**-6
sV = 0.5*10**-6
L_S = 13*100
sL_S = 0.5*100
K = V/2*L_S
sK = K*(sL_S/L_S+sV/V)
print(K, sK)

k = []
for i in range(5):
    k.append(MNK(T[i], lnU[i]))
Tau = [-1/k[i][0] for i in range(5)]
sTau = [k[i][2]/(k[i][0]**2) for i in range(5)]
D = [K/Tau[i] for i in range(5)]
sD = [D[i]*(k[i][2]/(k[i][0])+sK/K) for i in range(5)]
P_1 = [1/p for p in P]
sP = [2 for i in range(5)]
sP_1 = [P_1[i]*sP[i]/P[i] for i in range(5)]

k3 = MNK(P_1, D)
D760 = k3[0]*1/760
D738 = k3[0]*1/738
sD760 = k3[2]*1/760
sD738 = k3[2]*1/738
D40 = k3[0]*1/40
K3 = k3[0]
sK3 = k3[2]
K3si = K3*133
sK3si = sK3*133
print(K3si, sK3si)

k0 = 1.38*10**-23
R = 8.31
m = 4*10**-3

T0 = 295
P0 = 100000

Si = k0*T0/3/K3si*(8*R*T0/pi/m)**0.5
sSi = Si*(sK3/K3)

n = P0/k0/T0
l = 1/(2**0.5*Si*n)
sl = l*(sSi/Si)

#print(Tau)

n = []
colors = ['r', 'orange', 'y', 'g', 'b', 'm']

x = [str(round(Tau[i], 2))+' '+str(round(sTau[i], 2)) for i in range(5)]
nD = [i * 10000 for i in D]
nsD = [i * 10000 for i in sD]
y = [str(round(nD[i], 2)) + ' ' + str(round(nsD[i], 2)) for i in range(5)]

if 1 in n:
    fig, ax = plt.subplots()
    for i in range(5):
        linGraf(T[i], U[i], tipe = [2], fcolor = colors[i], flabel = Pnames[i])
    ax.set_xlabel('Время t, с')
    ax.set_ylabel('Напряжение U, мВ')
    ax.set(title = 'Зависимость напряжения от времени U(t)')
    ax.legend()
    '''
    plt.plot(T45, U45)
    plt.plot(T90, U90)
    plt.plot(T128, U128)
    plt.plot(T165, U165)
    plt.plot(T210, U210)
'''
if 2.5 in n:
    plt.plot(T45, lnU45)
    plt.plot(T90, lnU90)
    plt.plot(T128, lnU128)
    plt.plot(T165, lnU165)
    plt.plot(T210, lnU210)
if 2 in n:
    fig, ax = plt.subplots()
    for i in range(5):
        linGraf(T[i], lnU[i], tipe = [2], fcolor = colors[i], flabel = Pnames[i])
    '''
    ax.set_xlabel('Время t, с')
    ax.set_ylabel('Логорифм напряжения ln(U), ln(мВ)')
    '''
    ax.set(title = 'Зависимость логорифма напряжения от времени ln(U)(t)', xlabel = 'Время t, с', ylabel = 'Логорифм напряжения ln(U), ln(мВ)')
    ax.legend()
if 3 in n:
    fig, ax = plt.subplots()
    linGraf(P_1, [i*10000 for i in D], sP_1, [i*10000 for i in sD], tipe = [1])
    '''
    ax.set_xlabel('Обратное давление 1/P, $торр^{-1}$')
    ax.set_ylabel('Коэффицент диффузии D, $м^{2}c^{-1}$')
    '''
    ax.set(title='Зависимость коэффицента диффузии от обратного давления D(1/P)', xlabel = 'Обратное давление 1/P, $торр^{-1}$', ylabel = 'Коэффицент диффузии D, $cм^{2}c^{-1}$')
if 4 in n:
    tab = [P, x]
    print(tabulate(reverseTab(tab), tablefmt="fancy_grid"))
if 5 in n:
    tab = [P, y]
    print(tabulate(reverseTab(tab), tablefmt="fancy_grid"))
if 6 in n:
    print(tabulate(reverseTab([P, x, y]), tablefmt="fancy_grid"))
plt.show()
