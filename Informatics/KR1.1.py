from collections import deque

l = list(map(int, input().split()))

st = deque()
for n in l:
    st.append(n)

even_n = []
odd_n = []

while st:
    n = st.pop()
    if n % 2 == 0:
        even_n.append(n)
    else:
        odd_n.append(n)

res = []
while even_n or odd_n or st:
    if even_n:
        res.append(even_n.pop(0))
    if odd_n:
        res.append(odd_n.pop(0))
    if st:
        res.append(st.pop())

print(*res)
