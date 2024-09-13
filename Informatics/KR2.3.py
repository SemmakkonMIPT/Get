def count(n, s, friendedges):
    friends_count = 0
    visited = [False] * n
    queue = [s]
    visited[s] = True

    while queue:
        curr = queue.pop(0)
        friends_count += 1
        for friend in friendedges[curr]:
            if not visited[friend]:
                visited[friend] = True
                queue.append(friend)

    return friends_count


n, s = map(int, input().split())
friendedges = []
for _ in range(n):
    friendedges.append(list(map(int, input().split())))

friends = [set() for _ in range(n)]
for i in range(n):
    for j in range(n):
        if friendedges[i][j] == 1:
            friends[i].add(j)

print(count(n, s, friends))
'''
3 1.txt
0 1.txt 1.txt
0 0 1.txt
0 0 0
'''