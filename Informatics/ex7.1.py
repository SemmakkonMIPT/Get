def n2l(n):
    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return x[n]

def l2n(l):
    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return x.index(l)

def move(k, n, m):
    try:
        if 0 <= k[0]+n <= 7 and 0 <= k[1]+m <= 7:
            if (Desk[k[0]+n][k[1]+m] == None or Desk[k[0]+n][k[1]+m][0] > Desk[k[0]][k[1]][0]+1):
                Desk[k[0]+n][k[1]+m] = [Desk[k[0]][k[1]][0] + 1, Desk[k[0]][k[1]][1]+[[k[0]+n, k[1]+m]]]
                moves([k[0]+n, k[1]+m])
    except IndexError:
        return

def moves(k):
    move(k, 1, 2)
    move(k, -1, 2)
    move(k, 1, -2)
    move(k, -1, -2)
    move(k, 2, 1)
    move(k, -2, 1)
    move(k, 2, -1)
    move(k, -2, -1)

def wayPrint(l):
    for k in l:
        print(n2l(k[0]), k[1]+1, sep = '')

Desk = [[None for i in range(8)] for j in range(8)]
start = input()
end = input()
st = [l2n(start[0]), int(start[1])-1]
en = [l2n(end[0]), int(end[1])-1]
Desk[st[0]][st[1]] = [0, [st]]
moves(st)
#print(Desk[en[0]][en[1]])
wayPrint(Desk[en[0]][en[1]][1])



