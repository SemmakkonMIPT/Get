a, b = list(map(int, input().split())), list(map(int, input().split()))
l = [complex(float(a[i]), float(b[i])) for i in range(len(a))]
a = {i.real: i.imag for i in l}
print(a)