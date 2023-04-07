

def distence(n, s, f, links):
    def steps(k):
        for i in nlinks[k]:
            if dist[i[0]][0] == None or dist[i[0]][0] > dist[k][0] + i[1]:
                dist[i[0]][0] = dist[k][0] + i[1]
                dist[i[0]][1] = dist[k][1] + 1
                steps(i[0])

    if s!=n-1:
        nlinks = [links[s]]+links[:s]+links[s+1:]
    else: nlinks = [links[-1]]+links[:-1]
    dist = [[None, None] for i in range(n)]
    dist[0] = [0, 1]
    steps(0)
    return(dist[f+1] if s>f else dist[f])


n, m, s, f = map(int, input().split())
ribs = []
for i in range(m):
    ribs.append(list(map(int, input().split())))
links = [[] for i in range(n)]
for r in ribs:
    if [r[1], r[2]] not in links[r[0]]:
        links[r[0]].append([r[1], r[2]])
    if [r[0], r[2]] not in links[r[1]]:
        links[r[1]].append([r[0], r[2]])
print(distence(n, s, f, links)[1])