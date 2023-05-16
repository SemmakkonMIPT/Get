import re
with open("reg_task_3.txt") as file:
    strings = file.readlines()
text = ''
for elem in strings:
    text += elem

res = re.findall('[0-2]'r'\d'':''[0-5]'r'\d', text)

print(f'Всего {len(res)} вхождений:', end=' ')
print(*res)