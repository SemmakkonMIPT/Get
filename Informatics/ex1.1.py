def f1(l):
    a = {i: i for i in l}
    return a

l = list(map(int, input().split()))
print(f1(l))