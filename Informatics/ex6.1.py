def is_connected(adj_list):
    def dfs(node, visited):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    visited = set()
    dfs(0, visited)
    return len(visited) == len(adj_list)


# Пример использования
n = int(input())
edges = []
while True:
    s = input()
    if s == "#":
        break
    u, v = map(int, s.split())
    edges.append((u, v))

adj_list = [[] for _ in range(n)]
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

print(is_connected(adj_list))
