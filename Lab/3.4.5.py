print("Сева,спасибо за помощь")
R0 = 0.3
Ri = 20000
Ci = 2*10**-6
x, kx, N0, tpr, y, ky, s, Ni = float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input())
I = x*kx/R0
print(I)
H = I*N0/tpr
print(H)
B = Ri*Ci*y*ky/s/Ni
print(B)

'''
0.2
100
35
25
2.6
20
3
400

1.txt
50
40
24
2
100
3.8
200


'''