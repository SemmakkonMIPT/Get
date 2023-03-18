def shortest_path(edges, start, end):
    # создаем словарь для хранения кратчайших расстояний до каждой вершины
    distances = {vertex: float('inf') for vertex in set([edge[0] for edge in edges] + [edge[1] for edge in edges])}
    # начальная вершина имеет расстояние 0
    distances[start] = 0
    # очередь с приоритетами для выбора следующей вершины для обработки
    queue = [(start, 0)]
    while queue:
        # выбираем вершину с наименьшим расстоянием из очереди
        current, current_distance = min(queue, key=lambda x: x[1])
        # если это конечная вершина, то возвращаем кратчайшее расстояние до нее
        if current == end:
            return current_distance
        # удаляем текущую вершину из очереди
        queue.remove((current, current_distance))
        # для каждой смежной вершины проверяем, можно ли до нее добраться через текущую вершину и если да, то обновляем кратчайшее расстояние до нее
        for edge in edges:
            if edge[0] == current:
                next_vertex = edge[1]
                distance = edge[2]
                if distance in [1, 2, 3]:
                    # новое расстояние до следующей вершины
                    new_distance = distances[current] + distance
                    # если это кратчайший путь до следующей вершины, то обновляем информацию в словаре и добавляем вершину в очередь
                    if new_distance < distances[next_vertex]:
                        distances[next_vertex] = new_distance
                        queue.append((next_vertex, new_distance))
    # если конечная вершина недостижима, то возвращаем None
    return None


edges = eval(input())
start, end = [int(i) for i in input().split()]
print(shortest_path(edges, start, end))

