from heapq import *
from math import *

a, b, c = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))
B, C = len(b), len(c)
Ans = []
if C < B:
    b, c, B, C = c, b, C, B
for i in range(B):
    if(b[i] in c and (b[i] not in a)): heappush(Ans, b[i])
print(heappop(Ans), end = '')
for i in range(len(Ans)):
    print(' ', heappop(Ans), end = '', sep = '')