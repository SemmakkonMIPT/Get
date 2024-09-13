import re
def numbers(text):
    res = re.findall(r'\d[^+]', text + '.')

    print(f'Всего {len(res)} вхождений:', end=' ')
    for i in range(len(res)):
        print(res[i][0], end=' ')


text1 = '(3+5)-9*4'
numbers(text1)
print(' ')

text2 = '2*9-6*5'
numbers(text2)
print(' ')

text3 = '8*9+8-1.txt/(3*5+0)'
numbers(text3)
print(' ')