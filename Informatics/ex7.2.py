def steps(n):
    for i in links[n]:
        if dist[i] == None or dist[i] > dist[n]+1:
            dist[i] = dist[n]+1
            steps(i)

n, m = map(int, input().split())
ribs = []
for i in range(m):
    ribs.append(list(map(int, input().split())))
links = [[] for i in range(n)]
for r in ribs:
    if r[1] not in links[r[0]]:
        links[r[0]].append(r[1])
    if r[0] not in links[r[1]]:
        links[r[1]].append(r[0])

dist = [None for i in range(n)]
dist[0] = 0
steps(0)
for i in dist: print(i)


