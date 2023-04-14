def neibk(k):
    x = k[0]
    y = k[1]
    L = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (not (i==x and j==y) and 0<=i<m and 0<=j<l):
                L.append([i, j])
    return(L)

def neib(k):
    l = [board[K[0]][K[1]] for K in neibk(k)]
    return(l)

def goodneibk(k, s, used):
    x = k[0]
    y = k[1]
    L = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (not (i==x and j==y) and 0<=i<m and 0<=j<l) and board[i][j] == s and ([i, j] not in used):
                L.append([i, j])
    return(L)

def step(w, h, k, used):
    if h == len(w)-1:
        return 1
    else:
        for nk in goodneibk(k, w[h+1], used):
            Used = used
            Used.append(k)
            k = step(w, h+1, nk, Used)
            if k == 1: return 1
    return 0



def isWordIn(w):
    k = 0
    for i in range(m):
        if w[0] in board[i]:
            k += step(w, 0, [i, board[i].index(w[0])], [])
    return(k)

n = int(input())
L = input().split()
d = {l:False for l in L}
m, l = map(int, input().split())
board = [input().split() for i in range(m)]

Ans = []
for i in range(n):
    if isWordIn(L[i]) != 0:
        Ans.append(L[i])
print(*Ans)

'''
4
GEEKS FOR QUIZ GO
3 3
G I Z
U E K
Q S E

2
bcd db
5 2
d d
b f
e c
b c
d c
'''