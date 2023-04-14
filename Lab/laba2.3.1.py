ro = 885
P = 1.1*10**-2
h1 = 39.9
h2 = 13.3
h1f = 36.5
h2f = 17.3
dh1 = h1-h2
sh1=sh2=sh3=sh4 = 0.05
h3 = 35.4
h4 = 18.4
h = (h1+h2)/2
h1n = (h+dh1/2*1.05)
h2n = (h-dh1/2*1.05)
print(h1n, h2n)
dh2 = h3-h4
h3n = (h+dh2/2*1.05)
h4n = (h-dh2/2*1.05)
print(h3n, h4n)
P0torr =  746.7
P0 = P0torr*133.3
P1 = dh1*10*ro*10**-2
P2 = dh2*10*ro*10**-2
V0 = 50*10**-6
V1 = V0*P0/P1-V0
print(V1*10**6*1.05)
V2 = V0*P0/P2
print((V2-V1-V0)*10**6*1.05)
Ppr = 1.1*10**-4
Ppr = 7.5*10**-5
Pust = 1.3*10**-4
Pfv = 2.7*10**-3


