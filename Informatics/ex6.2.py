from collections import deque


def is_reachable(adj_list, start, end):
    queue = deque([start])
    visited = set([start])
    while queue:
        node = queue.popleft()
        if node == end:
            return True
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return False


# Пример использования
n = int(input())
edges = eval(input())

start, end = map(int, input().split())

adj_list = [[] for _ in range(n)]
for u, v in edges:
    adj_list[u].append(v)

print(is_reachable(adj_list, start, end))
