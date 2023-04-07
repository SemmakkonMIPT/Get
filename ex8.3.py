def distance(n, S, F, links):
    if S == F: return [0, 1]
    s, f = S, F
    return (distances(n, S, links)[F])

def distances(n, S, links):
    s = S
    def steps(k):
        for i in links[k]:
            if dist[i[0]][0] == None or dist[i[0]][0] > dist[k][0] + i[1]:
                dist[i[0]][0] = dist[k][0] + i[1]
                dist[i[0]][1] = dist[k][1] + 1
                steps(i[0])
    dist = [[None, None] for i in range(n)]
    dist[s] = [0, 1]
    steps(s)
    return(dist)

def summ(l):
    sum = 0
    for i in l: sum += i
    return(sum)


n, m = map(int, input().split())
ribs = []
for i in range(m):
    ribs.append(list(map(int, input().split())))
links = [[] for i in range(n)]
for r in ribs:
    if [r[1], r[2]] not in links[r[0]]:
        links[r[0]].append([r[1], r[2]])
    if [r[0], r[2]] not in links[r[1]]:
        links[r[1]].append([r[0], r[2]])


Alldist = [[i[0] for i in distances(n, s, links)] for s in range(n)]


k = 0
sum = summ(Alldist[0])
for i in range(1, n):
    if sum > summ(Alldist[i]):
        sum = summ(Alldist[i])
        k = i
print(k)



