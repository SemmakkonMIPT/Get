from semmakkon import *
'''
357 10
357 28
358 10
0 26
0 36
1 5
2 56
3 33
3 37 желтый

45 град
3 33
3 37
23 44
23 53
60 град
338 28
338 36
359 33
359 44
19 30
19 45
30 град
321 23
321 5
15 50
15 54
'''
dFi60 = toArray([(36-28), 44-33, 45-30])*60
dFi45 = toArray([(37-33), 53-44])*60
dFi30 = toArray([(23-5), 54-50])*60
dLambda = 21
D60 = dFi60/dLambda
D45 = dFi45/dLambda
D30 = dFi30/dLambda
# print(D60)
# print(D45)
# print(D30)
# print(dFi60)



FiData = read_table_from_file("DataLab/4.4.2/1.txt", row_separator=' ')
Fi = minutes_to_degrees(FiData[0], FiData[1])
Fi = 24.5-Fi
sin_Fi = degSinArray(Fi)
# print(Fi)
sin_Fi_sin_Psi = degSinArray(Fi)-degSin(45)

lambd = [5791, 5770,    5461, 4916, 4358, 4077, 4047][::-1]
lambd = toArray(lambd)
# lambd = toArray(lambd)/10**7
k = linGraf(lambd, sin_Fi_sin_Psi, create_plot=True, show_label=True, show_trendline_label=True,
            form='o', name = r'($\sin \varphi - \sin \psi$)($\lambda$)', OXname = r'$\lambda$, Å',
            OYname = r'$\sin \varphi - \sin \psi$')
linGraf([1, 2, 3], []+[i for i in D60], create_plot=True, show_label=True, show_trendline_label=True,
            form='o', name = 'D(m)', OXname = r'порядок спектра m',
            OYname = r'Угловая дисперсия D, $\frac{у.сек}{Å}$')
d = 1.67*10**-6
lamb = 577*10**-9
D = 1/d*degCos(25)*10**(-10)*3600*180/pi
print(D)




# print(k)
# print(k[0]*10**7)

# print(sin_Fi_sin_Psi)
# print(lambd)
# plt.show()
