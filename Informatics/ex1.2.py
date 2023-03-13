def f2(s):
    a = {str(i): s.count(str(i)) for i in range(10)}
    return a

l = input()
print(f2(l))