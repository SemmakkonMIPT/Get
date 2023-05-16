def infinite(lists, tries):
    res = []
    if lists[0] == '':
        print(-1)
    else:
        i = iter(lists)
        for j in range(tries):
            res.append(next(i))

    return res


a = [str(i) for i in input().split()]
a[0] = a[0][1:]
a[-1] = a[-1][:-1]
b = int(input())
c = a * (b // len(a) + 1)

print('-'.join(map(str, infinite(c, b))))
