def intersection(a1, b1, c1, a2, b2, c2):
    if (a1, b1) == (a2, b2) or b1/b2 == a1/a2:return("NO")
    D = (a1*b2-a2*b1)
    Dx = -(c1*b2-c2*b1)
    Dy = -(a1*c2-a2*c1)
    return(str(round(Dx/D))+' '+str(round(Dy/D)))



a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
print(intersection(a1, b1, c1, a2, b2, c2))
