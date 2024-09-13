import numpy as np
import matplotlib.pyplot as plt
from semmakkon import *

# Константы
lambda_laser = 532e-9  # длина волны лазера в метрах
L = 1340e-3  # расстояние от решетки до экрана в метрах
a = 50e-3    # расстояние от линзы до сетки в метрах
#b_values = np.array([47.7, 26.3, 19.7, 6.6, 4.6]) * 1e-3  # расстояния от линзы до экрана для каждой решетки


# Данные измерений
x_values = np.array([216.5, 144, 73, 140, 100]) * 1e-3  # перевод в метры
num_peaks = np.array([6, 6, 6, 24, 23])
D_values = np.array([70, 60, 40, 10, 5]) * 1e-3  # размеры изображений в метрах
sec_num_peaks = np.array([17, 20, 26, 14, 11])

# Расчет периода решеток по спектру
periods_spectral = lambda_laser * L / (x_values / num_peaks) * 1e3  # в миллиметрах
# Расчет периода с использованием линзы
periods_lens = D_values / sec_num_peaks * a / (L-a) * 1e3  # в миллиметрах


# Вывод результатов спектрального метода
print("Периоды решеток по спектру (мм):", periods_spectral)
print("Периоды решеток с использованием линзы (мм):", periods_lens[::-1])

# Подготовка данных для отображения
fig, axes = plt.subplots(2, 1, figsize=(8, 12))  # Создаем 2 графика в столбец

# Расчеты для саморепродукции
# Предположим, что shifts - это данные, как в примере выше
shifts = [
    np.array([20.45, 47.7]) * 1e-3,
    np.array([11.2, 26.3, 38.3, 52.35]) * 1e-3,
    np.array([2.4, 6.1, 9.6, 13.05, 15.7, 19.7]) * 1e-3,
    np.array([1.1, 2.2, 3.3, 4.4, 5.4, 6.6]) * 1e-3,
    np.array([0.7, 1.5, 2.3, 3.15, 3.8, 4.6]) * 1e-3
][::-1]

# Метод наименьших квадратов для нахождения угла наклона
periods_method3 = []
i = 0
for d, shifts_set in zip(periods_spectral, shifts):
    n_values = np.arange(1, len(shifts_set) + 1)
    z_n = 2 * (d*1e-3)**2 / lambda_laser * n_values  # переводим d обратно в метры для расчета
    z_n = shifts[i]+a
    coef = np.polyfit(n_values, z_n, 1)  # линейная аппроксимация
    k = coef[0]
    periods_method3.append(np.sqrt(k * lambda_laser / 2) * 1e3)  # перевод в мм
    axes[0].plot(n_values, z_n * 1e3, label=f'Решетка {i+1} (k={k:.2e})')
    i+=1

# Отображение результатов саморепродукции
axes[0].set_title('Саморепродукция для разных решеток')
axes[0].set_xlabel('Порядок n')
axes[0].set_ylabel('$z_{n}$ (мм)')
axes[0].legend()
axes[0].grid(True)

# Данные миры (пример, аналогично предыдущему коду)
miras = {
    'Mira 25': np.array([2.5, 5.4, 8.6, 11.4, 14.2, 17.1]) * 1e-3,
    'Mira 20': np.array([4.7, 10.1, 15.4, 20.2, 25.3, 30.1]) * 1e-3
}

# График данных миры
i = 0
k = [[], []]
for mira, distances in miras.items():
    n_values = np.arange(1, len(distances) + 1)
    axes[1].plot(n_values, distances * 1e3, 'o-', label=f'{mira}')
    k[i] = MNK(n_values, distances)
    i+=1
axes[1].set_title('Измеренные расстояния саморепродукции для миры')
axes[1].set_xlabel('Порядок n')
axes[1].set_ylabel('Расстояние (мм)')
axes[1].legend()
axes[1].grid(True)

# print(k)

periods_mira_25 = (np.sqrt(k[0][0] * lambda_laser / 2) * 1e3)  # перевод в мм
periods_mira_20 = (np.sqrt(k[1][0] * lambda_laser / 2) * 1e3)  # перевод в мм

# print(periods_mira_25)
# print(periods_mira_20)

periods_spectral_25 = lambda_laser * L / (0.110 / 6) * 1e3  # в миллиметрах
periods_spectral_20 = lambda_laser * L / (0.070 / 5) * 1e3  # в миллиметрах

periods_lens_25 = 18 / 17 * a / (L-a) * 1e3  # в миллиметрах
periods_lens_20 = 18 / 13 * a / (L-a) * 1e3  # в миллиметрах

# print(periods_spectral_25)
# print(periods_spectral_20)

# print(periods_lens_25)
# print(periods_lens_20)




# Показать графики
# plt.tight_layout()

# Вывод периодов решеток, вычисленных тремя методами
print("Периоды решеток по третьему методу (мм):", periods_method3)

plt.show()
