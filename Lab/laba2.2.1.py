import matplotlib.pyplot as plt

f = open('Data/20230329_1680090859552_45.csv', 'r')
f.readline()
File = [l for l in f]
Data = [l[:-2].split(',') for l in File]
T = [float(l[0]) for l in Data]
U = [float(l[1]) for l in Data]
plt.plot(T, U)
plt.show()
