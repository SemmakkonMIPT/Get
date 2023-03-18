def has_cycle(n, edges):
    # Создаем список смежности для каждой вершины графа
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Функция для обхода графа в глубину
    def dfs(node, parent):
        visited[node] = True
        for neigh in adj_list[node]:
            if not visited[neigh]:
                if dfs(neigh, node):
                    return True
            elif neigh != parent:
                return True
        return False

    # Проверяем наличие циклов
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False


n = int(input())
edges = []
while True:
    s = input()
    if s == "#":
        break
    u, v = map(int, s.split())
    edges.append((u, v))

print(has_cycle(n, edges))
