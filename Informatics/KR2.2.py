from collections import deque

def bfs(n, edges, start, end):
    visited = [False] * n
    dist = [0] * n
    predecessor = [-1] * n
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        v = queue.popleft()
        for neighbor in edges[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                dist[neighbor] = dist[v] + 1
                predecessor[neighbor] = v
                queue.append(neighbor)
                if neighbor == end:
                    return dist[neighbor], construct_path(predecessor, start, end)
    return -1, []

def construct_path(predecessor, start, end):
    path = []
    v = end
    while v != start:
        path.append(v)
        v = predecessor[v]
    path.append(start)
    return path[::-1]

n, m, start, end = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)
dist, path = bfs(n, edges, start, end)
if dist != -1:
    print(dist)
    print(*path)
else:
    print("No path found")
