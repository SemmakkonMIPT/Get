
#  Вводные данные задачи(на поле 0 - разрешенная, 1 - запрещенная клетки)
game_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

x_thief_start = 1
y_thief_start = 5

x_policeman_start = 1
y_policeman_start = 7

x_exit = 8
y_exit = 8

'''--------------------------------------Вор--------------------------------------'''

thief_matrix = []  # создаем шаблон матрицы с количеством ходов вора до каждой клетки
for i in range(len(game_map)):
    thief_matrix.append([])
    for j in range(len(game_map[i])):
        thief_matrix[-1].append(0)
thief_matrix[x_thief_start][y_thief_start] = 1


def thief_step(k):  # функция, проставляющая количество ходов вора до каждой клетки
    for x in range(len(thief_matrix)):
        for y in range(len(thief_matrix[x])):
            if thief_matrix[x][y] == k:
                if x > 0 and thief_matrix[x - 1][y] == 0 and game_map[x - 1][y] == 0:
                    thief_matrix[x - 1][y] = k + 1
                if y > 0 and thief_matrix[x][y - 1] == 0 and game_map[x][y - 1] == 0:
                    thief_matrix[x][y - 1] = k + 1
                if x < len(thief_matrix) - 1 and thief_matrix[x + 1][y] == 0 and game_map[x + 1][y] == 0:
                    thief_matrix[x + 1][y] = k + 1
                if y < len(thief_matrix[x]) - 1 and thief_matrix[x][y + 1] == 0 and game_map[x][y + 1] == 0:
                    thief_matrix[x][y + 1] = k + 1


p = 0  # проходим по матрице вора и проставляем количество шагов до каждой клетки
while thief_matrix[x_exit][y_exit] == 0:
    p += 1
    thief_step(p)


k0 = thief_matrix[x_exit][y_exit]  # возвращаемся от конечной точки в начало и записываем путь
thief_path = [(x_exit, y_exit)]
i, j = x_exit, y_exit
while k0 > 1:
    if i > 0 and thief_matrix[i - 1][j] == k0 - 1:
        i, j = i - 1, j
        thief_path.append((i, j))
        k0 -= 1
    elif j > 0 and thief_matrix[i][j - 1] == k0 - 1:
        i, j = i, j - 1
        thief_path.append((i, j))
        k0 -= 1
    elif i < len(thief_matrix) - 1 and thief_matrix[i + 1][j] == k0 - 1:
        i, j = i + 1, j
        thief_path.append((i, j))
        k0 -= 1
    elif j < len(thief_matrix[i]) - 1 and thief_matrix[i][j + 1] == k0 - 1:
        i, j = i, j + 1
        thief_path.append((i, j))
        k0 -= 1

print(f'Путь полицейского: {thief_path[::-1]}')
print(f'Вор доберется до выхода за {len(thief_path)} ходов.')
print(' ')

'''--------------------------------------Полицейский--------------------------------------'''

policeman_matrix = []  # создаем шаблон матрицы с количеством ходов полицейского до каждой клетки
for i in range(len(game_map)):
    policeman_matrix.append([])
    for j in range(len(game_map[i])):
        policeman_matrix[-1].append(0)
policeman_matrix[x_thief_start][y_thief_start] = 1


def policeman_step(k):  # функция, проставляющая количество ходов полицейского до каждой клетки
    for x in range(len(policeman_matrix)):
        for y in range(len(policeman_matrix[x])):
            if policeman_matrix[x][y] == k:
                if x > 0 and policeman_matrix[x - 1][y] == 0 and game_map[x - 1][y] == 0:
                    policeman_matrix[x - 1][y] = k + 1
                if y > 0 and policeman_matrix[x][y - 1] == 0 and game_map[x][y - 1] == 0:
                    policeman_matrix[x][y - 1] = k + 1
                if x < len(policeman_matrix) - 1 and policeman_matrix[x + 1][y] == 0 and game_map[x + 1][y] == 0:
                    policeman_matrix[x + 1][y] = k + 1
                if y < len(policeman_matrix[x]) - 1 and policeman_matrix[x][y + 1] == 0 and game_map[x][y + 1] == 0:
                    policeman_matrix[x][y + 1] = k + 1
                if x > 0 and y > 0 and policeman_matrix[x - 1][y - 1] == 0 and game_map[x - 1][y - 1] == 0:
                    policeman_matrix[x - 1][y - 1] = k + 1
                if x < len(policeman_matrix) and y > 0 and policeman_matrix[x + 1][y - 1] == 0 \
                        and game_map[x + 1][y - 1] == 0:
                    policeman_matrix[x + 1][y - 1] = k + 1
                if x > 0 and y < len(policeman_matrix[x]) and policeman_matrix[x - 1][y + 1] == 0 \
                        and game_map[x - 1][y + 1] == 0:
                    policeman_matrix[x - 1][y + 1] = k + 1
                if x < len(policeman_matrix) and y < len(policeman_matrix[x]) and policeman_matrix[x + 1][y + 1] == 0 \
                        and game_map[x + 1][y + 1] == 0:
                    policeman_matrix[x + 1][y + 1] = k + 1


u = 0  # проходим по матрице полицейского и проставляем количество шагов до каждой клетки
while policeman_matrix[x_exit][y_exit] == 0:
    u += 1
    policeman_step(u)


k0 = policeman_matrix[x_exit][y_exit]  # возвращаемся от конечной точки в начало и записываем путь
policeman_path = [(x_exit, y_exit)]
i, j = x_exit, y_exit
while k0 > 1:
    if i > 0 and policeman_matrix[i - 1][j] == k0 - 1:
        i, j = i - 1, j
        policeman_path.append((i, j))
        k0 -= 1
    elif j > 0 and policeman_matrix[i][j - 1] == k0 - 1:
        i, j = i, j - 1
        policeman_path.append((i, j))
        k0 -= 1
    elif i < len(policeman_matrix) - 1 and policeman_matrix[i + 1][j] == k0 - 1:
        i, j = i + 1, j
        policeman_path.append((i, j))
        k0 -= 1
    elif j < len(policeman_matrix[i]) - 1 and policeman_matrix[i][j + 1] == k0 - 1:
        i, j = i, j + 1
        policeman_path.append((i, j))
        k0 -= 1
    elif i > 0 and j > 0 and policeman_matrix[i - 1][j - 1] == k0 - 1:
        i, j = i - 1, j - 1
        policeman_path.append((i, j))
        k0 -= 1
    elif i < len(policeman_matrix) - 1 and j > 0 and policeman_matrix[i + 1][j - 1] == k0 - 1:
        i, j = i + 1, j - 1
        policeman_path.append((i, j))
        k0 -= 1
    elif i < len(policeman_matrix) - 1 and j < len(policeman_matrix) and policeman_matrix[i + 1][j + 1] == k0 - 1:
        i, j = i + 1, j + 1
        policeman_path.append((i, j))
        k0 -= 1
    elif i > 0 and j < len(policeman_matrix) and policeman_matrix[i - 1][j + 1] == k0 - 1:
        i, j = i - 1, j + 1
        policeman_path.append((i, j))
        k0 -= 1

print(f'Путь полицейского: {policeman_path[::-1]}')
print(f'Полицейский доберется до выхода за {len(policeman_path)} ходов.')
print(' ')

'''--------------------------------------Обработка результатов--------------------------------------'''

indicator = 0
for i in range(len(game_map)):
    for j in range(len(game_map)):
        if thief_matrix[i][j] == policeman_matrix[i][j] and thief_matrix[i][j] != 0 and indicator == 0:
            indicator += 1
            print(f'Полицейский победит, догнав вора в клетке ({i+1}, {j+1}) на {policeman_matrix[i][j]}-ом ходу.')
        if policeman_matrix[i][j] == thief_matrix[i][j] + 1 and thief_matrix[i][j] != 0 and indicator == 0:
            indicator += 1
            print(f'Полицейский победит, догнав вора в клетке ({i + 1}, {j + 1}) на {policeman_matrix[i][j]}-ом ходу.')
if policeman_matrix[x_exit][y_exit] < thief_matrix[x_exit][y_exit] and indicator == 0:
    indicator += 1
    print(f'Полицейский победит, догнав вора на выходе.')
