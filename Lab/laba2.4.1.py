from semmakkon import *
from tabulate import *


g = 9.81
Ro = 1000

Tc = [15, 16, 17, 18, 19, 20, 22, 24, 26, 28, 30]
#To = [28.8, 28, 27, 25.2, 24, 23, 22.1.txt, 21.1.txt, 20, 19, 18, 17, 16.1.txt]
Toc = [27, 25.2, 24, 23, 22.1, 21.1, 20, 19, 18, 17, 16.1, 15]
T = [t+273 for t in Tc]
To = [t+273 for t in Toc]

#мм
H1 = [54, 54, 60, 61, 62, 63, 66, 69, 72, 76, 80]
H2 = [21, 20, 24, 23, 22, 21, 19, 17, 13, 9, 5]
#H1o = [79, 78, 75, 72, 71, 70, 68, 67, 65, 64, 63, 62]
#H2o = [7, 8, 10, 12.5, 14, 16, 17, 18, 19, 21, 22, 23]
H1o = [75, 72, 71, 70, 68, 67, 65, 64, 63, 62, 61, 60]
H2o = [10, 12.5, 14, 16, 17, 18, 19, 21, 22, 23, 24, 25]

T_1 = [1/t for t in T]
sT = [0.5 for i in T]
sT_1 = [T_1[i]*0.5/T[i] for i in range(len(T))]
T_1o = [1/t for t in To]
sTo = [0.5 for i in To]
sT_1o = [T_1o[i]*0.5/To[i] for i in range(len(To))]

#мм

H = [H1[i]-H2[i] for i in range(len(H1))]
sH = [1 for i in H]
lnH = [log(h) for h in H]
slnH = [1/h for h in H]

Ho = [H1o[i]-H2o[i] for i in range(len(H1o))]
sHo = [1 for i in Ho]
lnHo = [log(h) for h in Ho]
slnHo = [1/h for h in Ho]

PHo = [i*g*Ro/1000 for i in Ho]
PsHo = [i*g*Ro/1000 for i in sHo]
PlnHo = [i*g*Ro/1000 for i in lnHo]
PH = [i*g*Ro/1000 for i in H]
PsH = [i*g*Ro/1000 for i in sH]
PlnH = [i*g*Ro/1000 for i in lnH]

Left = min(T + To)
Left_1 = min(T_1 + T_1o)
Right = max(T + To)
Right_1 = max(T_1 + T_1o)

fig, ax = plt.subplots()
OXname = 'Температура спирта T, K'
OYname = 'Давление паров P, мм.рт.ст.'
OXname1 = 'Обратная температура спирта 1.txt/T, 0.001/K'
OYname1 = 'Нат. логорфм авления паров ln(P)'

ax.set(title = "Зависимость давления насыщенных паров от температуры", xlabel = OXname, ylabel = OYname)
linGraf(T, H, sT, sH, tipe = 2, fcolor = 'b', left = Left, right = Right, flabel = "Нагревание")
linGraf(To, Ho, sTo, sHo, tipe = 2, fcolor = 'g', left = Left, right = Right, flabel = "Охлаждение")
ax.legend()

fig, ax = plt.subplots()
ax.set(title = "Зависимость давления насыщенных паров от температуры", xlabel = OXname1, ylabel = OYname1)
K1 = linGraf([i*1000 for i in T_1], lnH, [i*1000 for i in sT_1], slnH, tipe = 1, fcolor = 'b', left = Left_1*1000, right = Right_1*1000, flabel = "Нагревание")
K2 = linGraf([i*1000 for i in T_1o], lnHo, [i*1000 for i in sT_1o], slnHo, tipe = 1, fcolor = 'g', left = Left_1*1000, right = Right_1*1000, flabel = "Охлаждение")
ax.legend()

print(K1[0], K1[2])
print(K2[0], K2[2])

print(-8.31*K1[0]/1000, 8.31*K1[2]/1000)
print(-8.31*K2[0]/1000, 8.31*K2[2]/1000)

TC = [i-273 for i in T]
TCo = [i-273 for i in To]
tab1 = [TC, H1, H2]
tab2 = [TCo, H1o, H2o]
tab3 = [TC, H, TCo, Ho]

#print(tabulate(tab1, tablefmt="fancy_grid"))
#print(tabulate(tab2, tablefmt="fancy_grid"))
print(tabulate(tab3, tablefmt="fancy_grid"))


plt.show()

