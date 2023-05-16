def generate(n, m):
    arr = [[i for j in range(m)] for i in range(n)]
    return(arr)

def nice_print(arr):
    for str in arr:
        print(*str)


n, m = map(int, input().split())
arr = generate(n, m)
nice_print(arr)