from semmakkon import *
import matplotlib.pyplot as plt
from math import *
import numpy as np

# Открываем файл для чтения
with open('Data/VAH_Shottky', 'r') as file:
    # Пропускаем заголовок
    file.readline()

    # Создаем пустые списки для смещения, текущего и логарифма текущего
    bias_data = []
    current_data = []
    mod_current_data = []
    log_current_data = []
    mod_log_current_data = []


    # Читаем данные из файла
    for line in file:
        # Разделяем строку на значения
        values = line.split()
        # Преобразуем строки в числа с плавающей запятой
        bias = -float(values[0])
        current = -float(values[1])
        # Добавляем данные в соответствующие списки
        bias_data.append(bias)
        current_data.append(current)
        mod_current = -float(values[1]) - current_data[0]
        mod_current_data.append(mod_current)

        # Проверяем, что текущее значение положительно, иначе пропускаем
        if current > 0:
            log_current_data.append(np.log(current))
        else:
            log_current_data.append(None) # Добавляем None для пропуска точек в графике

        if mod_current > 0:
            mod_log_current_data.append(np.log(mod_current))
        else:
            mod_log_current_data.append(None)

# mod_current_data = np.array(current_data)-current_data[0]
# mod_log_current_data = np.log(mod_current_data)

# Создаем фигуру и оси для обычного графика
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(bias_data, mod_current_data)
plt.xlabel('Напряжение U, В')
plt.ylabel('Ток I, А')
plt.title('ВАХ Диода Шоттки')
plt.grid(True)

# Создаем фигуру и оси для графика ln(Current) от Bias
# plt.subplot(1.txt, 2, 2)
# plt.plot(bias_data, log_current_data, marker = 'o')
# plt.xlabel('Напряжение U, В')
# plt.ylabel('Нат. логорифм тока ln(I)')
# plt.title('ВАХ в полулогарифмическом масштабе')
# plt.grid(True)

# Создаем фигуру и оси для графика ln(Current) от Bias
plt.subplot(1, 2, 2)
plt.plot(bias_data, mod_log_current_data, marker = 'o')
plt.xlabel('Напряжение U, В')
plt.ylabel('Нат. логорифм тока ln(I)')
plt.title('ВАХ в полулогарифмическом масштабе')
plt.grid(True)

U = bias_data[1:4]
I = mod_log_current_data[1:4]
k = linGraf(U, I, tipe = [], gsize = bias_data[0:4])
print(k)
# Регулируем расположение графиков
plt.tight_layout()
I_0 = exp(k[1])
print(I_0)
# Отображаем оба графика
plt.show()
# 0.0000e+00   4.5816e-07   0.0000e+00
# -2.0000e-01   2.7792e-07   -7.1963e+05
# -4.0000e-01   -3.1710e-06   1.txt.2614e+05
# -6.0000e-01   -1.txt.3802e-04   4.3472e+03



