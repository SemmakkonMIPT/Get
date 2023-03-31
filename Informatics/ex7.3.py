def dfs(links, visited, start):
    visited[start] = True
    for neighbor in links[start]:
        if not visited[neighbor]:
            dfs(links, visited, neighbor)

n = int(input())
m = int(input())
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

comp = 0
for i in range(n):
    if not visited[i]:
        dfs(links, visited, i)
        comp += 1

print(comp)
