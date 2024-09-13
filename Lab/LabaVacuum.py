import matplotlib.pyplot as plt
from semmakkon import *
import numpy as np
import matplotlib.pyplot as plt

# Создаем пустые массивы NumPy для хранения данных из первого файла
x_values_1 = np.array([])
y_values_1 = np.array([])

# Открываем первый файл для чтения
file_path_1 = 'Data/B1.2'  # Укажите путь к первому файлу
with open(file_path_1, 'r') as file_1:
    for line in file_1:
        parts = line.strip().split(',')
        if len(parts) == 2:
            x_values_1 = np.append(x_values_1, float(parts[0]))
            y_values_1 = np.append(y_values_1, float(parts[1]))

# Создаем пустые массивы NumPy для хранения данных из второго файла
x_values_2 = np.array([])
y_values_2 = np.array([])

# Открываем второй файл для чтения
file_path_2 = 'Data/B2.2'  # Укажите путь ко второму файлу
with open(file_path_2, 'r') as file_2:
    for line in file_2:
        parts = line.strip().split(',')
        if len(parts) == 2:
            x_values_2 = np.append(x_values_2, float(parts[0]))
            y_values_2 = np.append(y_values_2, float(parts[1]))

# Создаем пустые массивы NumPy для хранения данных из третьего файла
x_values_3 = np.array([])
y_values_3 = np.array([])

# Открываем третий файл для чтения
file_path_3 = 'Data/FC2'  # Укажите путь к третьему файлу
with open(file_path_3, 'r') as file_3:
    for line in file_3:
        parts = line.strip().split(',')
        if len(parts) == 2:
            x_values_3 = np.append(x_values_3, float(parts[0]))
            y_values_3 = np.append(y_values_3, float(parts[1]))

x_values_5 = np.array([])
y_values_5 = np.array([])

# Открываем третий файл для чтения
file_path_5 = 'Data/B3'  # Укажите путь к третьему файлу
with open(file_path_5, 'r') as file_5:
    for line in file_5:
        parts = line.strip().split(',')
        if len(parts) == 2:
            x_values_5 = np.append(x_values_5, float(parts[0]))
            y_values_5 = np.append(y_values_5, float(parts[1]))

# Создаем график

plt.figure(figsize=(8, 6))
plt.plot(x_values_1, y_values_1, marker='.', linestyle='-', markersize=1)
plt.plot(x_values_2, y_values_2, marker='.', linestyle='-', markersize=1)


plt.xlabel('t, c')
plt.ylabel('p, торр')
plt.grid(True)

plt.figure(figsize=(8, 6))
plt.plot(x_values_3, y_values_3, marker='.', linestyle='-', markersize=1)
plt.xlabel('t, c')
plt.ylabel('Q, sccm')
plt.grid(True)

x_values_4 = [0.212, 0.301, 0.386, 0.462, 0.538, 0.612, 0.685]
y_values_4 = [5, 10, 15, 20, 25, 30, 35]

plt.figure(figsize=(8, 6))
k1 = linGraf(x_values_4, y_values_4, fcolor = 'g', tipe = [], form = 'o')
#plt.plot(x_values_4, y_values_4, color = 'r', marker='o', linestyle='', markersize=6)
print(k1[0], k1[2])
plt.xlabel('t, c')
plt.ylabel('Q, sccm')
plt.grid(True)

plt.figure(figsize=(8, 6))
plt.plot(x_values_5, y_values_5, marker='.', linestyle='-', markersize=1)
plt.xlabel('t, c')
plt.ylabel('p, торр')
plt.grid(True)

x_values_6 = y_values_2[8367:9367]
y_values_6 = y_values_5[1500:2500]
x_values_7 = x_values_5[1500:2500]
y_values_7 = y_values_5[1500:2500]
y_values_7 = np.log(y_values_7 - y_values_7[-1])

plt.figure(figsize=(8, 6))
k1 = linGraf(x_values_6, y_values_6, fcolor = 'g', tipe = [], form = 'o', ms = 1)
#plt.plot(x_values_6, y_values_6, marker='.', linestyle='-', markersize=1.txt)
plt.xlabel('$P_{B2}$, торр')
plt.ylabel('$P_{B3}$, торр')
plt.grid(True)

plt.figure(figsize=(8, 6))
#k1 = linGraf(x_values_6, y_values_6, fcolor = 'g', tipe = [], form = 'o', ms = 1.txt)
plt.plot(x_values_7, y_values_7, marker='.', linestyle='-', markersize=1)
plt.xlabel('t, c')
plt.ylabel('ln(p(t)-$p_{0}$), ln(торр)')
plt.grid(True)

# Отображаем график

plt.show()
