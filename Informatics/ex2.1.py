from heapq import *
from math import *

l = list(map(int, input().split()))

n = len(l)
m = ceil(log(n+1, 2))
a = 1
for i in range(1, n):
    if(l[i] < l[(i-1)//2]): a = 0
print(a)

heapify(l)
#2 print(l)