import matplotlib.pyplot as plt
from math import *
import numpy as np
from semmakkon import *

def plotEL(A, B):
    x = np.arange(-(1/A)**0.5, (1/A)**0.5, 0.00001)
    plt.plot(x, ((1-A*x**2)/B)**0.5, color = 'b')
    plt.plot(x, -((1-A*x**2)/B)**0.5, color = 'b')


RamkT = [i/10 for i in [25.55, 25.76, 25.63]]
CilTS = [i/10 for i in [38.47, 38.56, 38.54]]
CilTD = [i/10 for i in [42.21, 42.13, 42.02]]
H = 0.0972
D = 0.08795
MC = 4.5624
FP = [0.1002, 0.0503, 0.1503]


IC = MC*(D/2)**2/2
TR = sred(RamkT)[0]
TC = sred(CilTS)[0]
TCD = sred(CilTD)[0]
f = 4*pi**2*IC/(TC**2-TR**2)
#print(IC, TCD, TR)
#print(f)

#Параллелепипед
ParT = [i/10 for i in [list(map(float, '3841 3824 3816 4112 4131 4119 3253 3291 3261 3502 3494 3511 3465 3461 3472 3374 3374 3376 3888 3882 3883'.split()))[i]/100 for i in range(21)]]
TP = [sred(ParT[3*i:3*i+3])[0] for i in range(7)]
RP = [1/((TP[i]**2-TR**2)**0.5) for i in range(7)]
print(TP)
#print(RP)
XTXYP = [RP[0], 0, RP[6]*FP[0]/((FP[0]**2+FP[1]**2)**0.5), -RP[0], 0, -RP[6]*FP[0]/((FP[0]**2+FP[1]**2)**0.5), -RP[6]*FP[0]/((FP[0]**2+FP[1]**2)**0.5), RP[6]*FP[0]/((FP[0]**2+FP[1]**2)**0.5)]
YTXYP = [0, RP[1], RP[6]*FP[1]/((FP[0]**2+FP[1]**2)**0.5), 0, -RP[1], -RP[6]*FP[1]/((FP[0]**2+FP[1]**2)**0.5), RP[6]*FP[1]/((FP[0]**2+FP[1]**2)**0.5), -RP[6]*FP[1]/((FP[0]**2+FP[1]**2)**0.5)]
XP = (TP[0]**2-TR**2)
YP = TP[1]**2-TR**2

XTXZP = [RP[0], 0, RP[4]*FP[0]/((FP[0]**2+FP[2]**2)**0.5), -RP[0], 0, -RP[4]*FP[0]/((FP[0]**2+FP[2]**2)**0.5), -RP[4]*FP[0]/((FP[0]**2+FP[2]**2)**0.5), RP[4]*FP[0]/((FP[0]**2+FP[2]**2)**0.5)]
ZTXZP = [0, RP[2], RP[4]*FP[2]/((FP[0]**2+FP[2]**2)**0.5), 0, -RP[2], -RP[4]*FP[2]/((FP[0]**2+FP[2]**2)**0.5), RP[4]*FP[2]/((FP[0]**2+FP[2]**2)**0.5), -RP[4]*FP[2]/((FP[0]**2+FP[2]**2)**0.5)]
ZP = TP[2]**2-TR**2

YTYZP = [RP[1], 0, RP[5]*FP[1]/((FP[1]**2+FP[2]**2)**0.5), -RP[1], 0, -RP[5]*FP[1]/((FP[1]**2+FP[2]**2)**0.5), -RP[5]*FP[1]/((FP[1]**2+FP[2]**2)**0.5), RP[5]*FP[1]/((FP[1]**2+FP[2]**2)**0.5)]
ZTYZP = [0, RP[2], RP[5]*FP[2]/((FP[1]**2+FP[2]**2)**0.5), 0, -RP[2], -RP[5]*FP[2]/((FP[1]**2+FP[2]**2)**0.5), RP[5]*FP[2]/((FP[1]**2+FP[2]**2)**0.5), -RP[5]*FP[2]/((FP[1]**2+FP[2]**2)**0.5)]

'''
#сечение XYP
plt.scatter(XTXYP, YTXYP, color = 'b')
plotEL(XP, YP)
'''
#сечение XZP
plt.scatter(XTXZP, ZTXZP, color = 'b')
plotEL(XP, ZP)
'''
#сечение YZP
plt.scatter(YTYZP, ZTYZP, color = 'b')
plotEL(YP, ZP)
'''

#Квадрат
FK = [0.0927, 0.0927, 0.0926]
TKvad = [3.09]*21
TK = [sred(TKvad[3*i:3*i+3])[0] for i in range(7)]
RK = [1/((TK[i]**2-TR**2)**0.5) for i in range(7)]
#print(TK)
#print(RK)
XTXYK = [RK[0], 0, RK[6]*FK[0]/((FK[0]**2+FK[1]**2)**0.5), -RK[0], 0, -RK[6]*FK[0]/((FK[0]**2+FK[1]**2)**0.5), -RK[6]*FK[0]/((FK[0]**2+FK[1]**2)**0.5), RK[6]*FK[0]/((FK[0]**2+FK[1]**2)**0.5)]
YTXYK = [0, RK[1], RK[6]*FK[1]/((FK[0]**2+FK[1]**2)**0.5), 0, -RK[1], -RK[6]*FK[1]/((FK[0]**2+FK[1]**2)**0.5), RK[6]*FK[1]/((FK[0]**2+FK[1]**2)**0.5), -RK[6]*FK[1]/((FK[0]**2+FK[1]**2)**0.5)]
XK = (TK[0]**2-TR**2)
YK = TK[1]**2-TR**2

XTXZK = [RK[0], 0, RK[4]*FK[0]/((FK[0]**2+FK[2]**2)**0.5), -RK[0], 0, -RK[4]*FK[0]/((FK[0]**2+FK[2]**2)**0.5), -RK[4]*FK[0]/((FK[0]**2+FK[2]**2)**0.5), RK[4]*FK[0]/((FK[0]**2+FK[2]**2)**0.5)]
ZTXZK = [0, RK[2], RK[4]*FK[2]/((FK[0]**2+FK[2]**2)**0.5), 0, -RK[2], -RK[4]*FK[2]/((FK[0]**2+FK[2]**2)**0.5), RK[4]*FK[2]/((FK[0]**2+FK[2]**2)**0.5), -RK[4]*FK[2]/((FK[0]**2+FK[2]**2)**0.5)]
ZK = TK[2]**2-TR**2

YTYZK = [RK[1], 0, RK[5]*FK[1]/((FK[1]**2+FK[2]**2)**0.5), -RK[1], 0, -RK[5]*FK[1]/((FK[1]**2+FK[2]**2)**0.5), -RK[5]*FK[1]/((FK[1]**2+FK[2]**2)**0.5), RK[5]*FK[1]/((FK[1]**2+FK[2]**2)**0.5)]
ZTYZK = [0, RK[2], RK[5]*FK[2]/((FK[1]**2+FK[2]**2)**0.5), 0, -RK[2], -RK[5]*FK[2]/((FK[1]**2+FK[2]**2)**0.5), RK[5]*FK[2]/((FK[1]**2+FK[2]**2)**0.5), -RK[5]*FK[2]/((FK[1]**2+FK[2]**2)**0.5)]

'''
#сечение XYK
plt.scatter(XTXYK, YTXYK, color = 'b')
plotEL(XK, YK)

#сечение XZK
plt.scatter(XTXZK, ZTXZK, color = 'b')
plotEL(XK, ZK)

#сечение YZK
plt.scatter(YTYZK, ZTYZK, color = 'b')
plotEL(YK, ZK)
'''

#цилиндр
FС = [0.0972, 0.08795]
TCil = [i/10 for i in [38.47, 38.56, 38.54, 42.21, 42.13, 42.02]]
#print(sred(TCil[3:6]))
TС = [sred(TCil[3*i:3*i+3])[0] for i in range(2)]
RС = [1/((TС[i]**2-TR**2)**0.5) for i in range(2)]
#print(TС)
#print(RС)

XTXYС = [RС[0], 0, -RС[0], 0]
YTXYС = [0, RС[1], 0, -RС[1]]
XС = (TС[0]**2-TR**2)
YС = TС[1]**2-TR**2

'''
#сечение Цилиндра
plt.scatter(XTXYС, YTXYС, color = 'b')
plotEL(XС, YС)


a = FP[0]
b = FP[1]
c = FP[2]
TX = TP[0]
TY = TP[1]
TZ = TP[2]
TD = TP[3]
TE = TP[5]
TM = TP[6]
TPP = TP[4]
print((a**2+b**2)*TM**2, (a*TX)**2 + (b*TY)**2)
'''
#print(f)

plt.show()

#print(sred(RamkT))
#print(sred(CilTS))





