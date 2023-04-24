n, m = map(int, input().split())
edges = []
for i in range(m):
    edges.append(list(map(int, input().split())))
visited = [False for i in range(n)]

links = [[] for i in range(n)]
for r in edges:
    if r[1] not in links[r[0]]:
        links[r[0]].append(r[1])
    if r[0] not in links[r[1]]:
        links[r[1]].append(r[0])




