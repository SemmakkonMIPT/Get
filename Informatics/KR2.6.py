import numpy as np

def step(n, k):
    used[n]=1
    tables[k].append(n)
    for i in links[n]:
        if i in tables[k]:
            return(0)
        if i not in tables[1-k]:
            #tables[1-k].append(i)
            ans = step(i, 1-k)
            if ans == 0: return 0
    return 1


n, m = map(int, input().split())
edges = []
for i in range(m):
    edges.append(np.array(list(map(int, input().split())))-1)
links = [[] for i in range(n)]
for r in edges:
    if r[1] not in links[r[0]]:
        links[r[0]].append(r[1])
    if r[0] not in links[r[1]]:
        links[r[1]].append(r[0])
tables = [[], []]
used = [0 for i in range(n)]
ans = 1
ans = step(0, 0)

while used != [1 for i in range(n)]:
    i = used.index(0)
    ans=min(step(i, 1), ans)
''''''
if ans == 1:
    print('YES')
    print(*(np.array(tables[0])+1))
else: print('NO')


'''
3 2
1 2
1 3
Yes

4 3
1 2
1 3
2 4
Yes

4 3
1 2
2 3
1 3
No

6 4
1 2
1 3
4 6
5 6
Yes


'''