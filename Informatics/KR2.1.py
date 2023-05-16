n, m = map(int, input().split())
edges = [0] * n
for i in range(m):
    u, v = map(int, input().split())
    edges[u] += 1
    edges[v] += 1
if all(e == edges[0] for e in edges):
    print("YES")
else:
    print("NO")
