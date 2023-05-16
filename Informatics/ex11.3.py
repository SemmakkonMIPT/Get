import re
with open("colors.txt") as file:
    strings = file.readlines()
text = ''
for elem in strings:
    text += elem

res = re.findall(r'#[\dA-F]{3,6}', text)

print(f'Всего {len(res)} вхождений:', end=' ')
print(*res)
