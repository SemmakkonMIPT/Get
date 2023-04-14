def get_edges(s):
    S = s[2:-2]
    e = S.split('}, {')
    edges = [(list(map(int, i.split(', '))) if i!='' else []) for i in e]
    return(edges)

def alg(a, b):
    visited[a] = True
    for i in edges[a]:
        if visited[i] and i!=b:
            return(1)
        elif not visited[i]:
            return(alg(i, a))
    return(0)



n, m = map(int, input().split())
edges = get_edges(input())

k = 0
visited = [False for i in range(n)]

for i in range(n):
    if not visited[i]:
        k += alg(i, i)
print("NO" if k==0 else "YES")

'''
5 5
{{1}, {0, 2, 4}, {1, 3}, {2, 4}, {1, 3}}

4 3
{{1}, {0, 2}, {1, 3}, {2}}

3 3
{{1, 2}, {0, 2}, {0, 1}}
'''