def dfs(links, visited, start):
    visited[start] = True
    for neighbor in links[start]:
        if not visited[neighbor]:
            dfs(links, visited, neighbor)

n, m = map(int, input().split())
visited = [False for i in range(n)]
ribs = []
for i in range(m):
    ribs.append(list(map(int, input().split())))
links = [[] for i in range(n)]
for r in ribs:
    if r[1] not in links[r[0]]:
        links[r[0]].append(r[1])
    if r[0] not in links[r[1]]:
        links[r[1]].append(r[0])

comp = []
for i in range(n):
    if not visited[i]:
        before = [i for i in visited]
        dfs(links, visited, i)
        after = [ i for i in visited]
        comp.append([])
        for j in range(n):
            if after[j] and not before[j]:
                comp[-1].append(j)

ribmass = [0 for i in range(n)]
for r in ribs:
    ribmass[r[0]]+=r[2]
    ribmass[r[1]]+=r[2]

compmass = []
for c in comp:
    m = 0
    for i in c:
        m+=ribmass[i]/2
    compmass.append(int(m))
compmass.sort()
for i in compmass: print(i)